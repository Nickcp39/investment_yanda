#!/usr/bin/env python3
"""
Create an investment research note from a YouTube URL.

The script first tries to fetch YouTube caption tracks directly from the
watch page. If OPENAI_API_KEY is configured and --llm is passed, it also
turns the transcript into a structured investment research note.
"""

from __future__ import annotations

import argparse
import datetime as dt
import http.cookiejar
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LANGS = ["zh-Hans", "zh-CN", "zh", "en", "en-US"]
COOKIE_JAR = http.cookiejar.CookieJar()
OPENER = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(COOKIE_JAR))

KEY_TERMS = [
    "AI",
    "EPS",
    "FOMC",
    "财报",
    "预期",
    "营收",
    "利润",
    "利润率",
    "现金流",
    "估值",
    "资本支出",
    "看涨",
    "看空",
    "做空",
    "买入",
    "卖出",
    "上车",
    "突破",
    "支撑",
    "压力",
    "风险",
    "期权",
    "暗池",
    "大单",
    "目标价",
    "指引",
    "超预期",
    "低于预期",
]

TICKER_STOPWORDS = {
    "AI",
    "API",
    "APP",
    "ASIC",
    "AWS",
    "CEO",
    "CFO",
    "CPU",
    "DRAM",
    "EPS",
    "ETF",
    "FOMC",
    "GDP",
    "GPU",
    "IPO",
    "IR",
    "LLM",
    "MTIA",
    "NAND",
    "NYSE",
    "OBBBA",
    "PDF",
    "PE",
    "PUE",
    "RPO",
    "SEC",
    "SMR",
    "TPU",
    "URL",
    "VIP",
    "WWDC",
}


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def parse_video_id(value: str) -> str:
    value = value.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value

    parsed = urllib.parse.urlparse(value)
    host = parsed.netloc.lower()

    if host.endswith("youtu.be"):
        video_id = parsed.path.strip("/").split("/")[0]
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            return video_id

    query = urllib.parse.parse_qs(parsed.query)
    if "v" in query and query["v"]:
        video_id = query["v"][0]
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            return video_id

    path_parts = [part for part in parsed.path.split("/") if part]
    for marker in ("embed", "shorts", "live"):
        if marker in path_parts:
            idx = path_parts.index(marker)
            if idx + 1 < len(path_parts):
                video_id = path_parts[idx + 1]
                if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                    return video_id

    raise ValueError(f"Could not parse a YouTube video id from: {value}")


def http_get_text(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0 Safari/537.36"
            ),
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "identity",
        },
    )
    with OPENER.open(request, timeout=timeout) as response:
        data = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
    return data.decode(charset, errors="replace")


def http_post_json(url: str, payload: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, method="POST", headers=headers)
    with OPENER.open(request, timeout=120) as response:
        raw = response.read().decode("utf-8", errors="replace")
    return json.loads(raw)


def extract_balanced_json(page: str, marker: str) -> dict[str, Any] | None:
    idx = page.find(marker)
    if idx == -1:
        return None

    start = page.find("{", idx + len(marker))
    if start == -1:
        return None

    depth = 0
    in_string = False
    escape = False

    for pos in range(start, len(page)):
        ch = page[pos]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue

        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                snippet = page[start : pos + 1]
                try:
                    return json.loads(snippet)
                except json.JSONDecodeError:
                    return None

    return None


def extract_player_response(page: str) -> dict[str, Any]:
    markers = [
        "ytInitialPlayerResponse =",
        "var ytInitialPlayerResponse =",
        '"ytInitialPlayerResponse":',
    ]
    for marker in markers:
        data = extract_balanced_json(page, marker)
        if data:
            return data
    raise RuntimeError("Could not find ytInitialPlayerResponse in the YouTube page.")


def get_nested(data: dict[str, Any], path: list[str], default: Any = None) -> Any:
    cur: Any = data
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def track_name(track: dict[str, Any]) -> str:
    name = track.get("name", {})
    if "simpleText" in name:
        return str(name["simpleText"])
    if "runs" in name:
        return "".join(str(run.get("text", "")) for run in name["runs"])
    return track.get("languageCode", "unknown")


def choose_caption_track(
    tracks: list[dict[str, Any]],
    preferred_langs: list[str],
    prefer_manual: bool = True,
) -> dict[str, Any]:
    def score(track: dict[str, Any]) -> int:
        lang = str(track.get("languageCode", ""))
        kind = track.get("kind", "")
        value = 0
        for idx, preferred in enumerate(preferred_langs):
            if lang == preferred:
                value += 1000 - idx * 20
            elif lang.startswith(preferred.split("-")[0]):
                value += 700 - idx * 20
        if prefer_manual and kind != "asr":
            value += 50
        if not prefer_manual and kind == "asr":
            value += 50
        return value

    ranked = sorted(tracks, key=score, reverse=True)
    if not ranked or score(ranked[0]) <= 0:
        available = ", ".join(
            f"{track.get('languageCode', '?')}:{track_name(track)}" for track in tracks
        )
        raise RuntimeError(
            "No caption track matched preferred languages. "
            f"Available tracks: {available}"
        )
    return ranked[0]


def add_query_param(url: str, key: str, value: str) -> str:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(k, v) for k, v in query if k != key]
    query.append((key, value))
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query)))


def parse_json3_captions(raw: str) -> list[dict[str, Any]]:
    data = json.loads(raw)
    segments: list[dict[str, Any]] = []
    for event in data.get("events", []):
        segs = event.get("segs")
        if not segs:
            continue
        text = "".join(seg.get("utf8", "") for seg in segs)
        text = clean_caption_text(text)
        if not text:
            continue
        start_ms = int(event.get("tStartMs", 0))
        duration_ms = int(event.get("dDurationMs", 0))
        segments.append({"start_ms": start_ms, "duration_ms": duration_ms, "text": text})
    return segments


def parse_xml_captions(raw: str) -> list[dict[str, Any]]:
    if not raw.strip():
        return []
    root = ET.fromstring(raw)
    segments: list[dict[str, Any]] = []
    for node in root.iter():
        if node.tag not in {"text", "p"}:
            continue
        text = clean_caption_text("".join(node.itertext()))
        if not text:
            continue
        start = node.attrib.get("start") or node.attrib.get("t") or "0"
        duration = node.attrib.get("dur") or node.attrib.get("d") or "0"
        if node.attrib.get("t"):
            start_ms = int(float(start))
            duration_ms = int(float(duration or 0))
        else:
            start_ms = int(float(start) * 1000)
            duration_ms = int(float(duration or 0) * 1000)
        segments.append({"start_ms": start_ms, "duration_ms": duration_ms, "text": text})
    return segments


def clean_caption_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def fetch_captions(track: dict[str, Any]) -> list[dict[str, Any]]:
    base_url = track["baseUrl"]
    json_url = add_query_param(base_url, "fmt", "json3")
    raw = http_get_text(json_url)
    try:
        segments = parse_json3_captions(raw)
        if segments:
            return segments
    except (json.JSONDecodeError, KeyError, TypeError):
        pass

    segments: list[dict[str, Any]] = []
    for caption_url in (add_query_param(base_url, "fmt", "srv3"), base_url):
        raw = http_get_text(caption_url)
        try:
            segments = parse_xml_captions(raw)
        except ET.ParseError:
            segments = []
        if segments:
            break

    if not segments:
        raise RuntimeError("Caption track was fetched but no text segments were found.")
    return segments


def fetch_with_youtube_transcript_api(
    video_id: str,
    preferred_langs: list[str],
) -> list[dict[str, Any]]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore
    except ImportError:
        return []

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=preferred_langs)
    except Exception:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, languages=preferred_langs
            )
        except Exception:
            return []

    segments: list[dict[str, Any]] = []
    for item in transcript:
        if isinstance(item, dict):
            text = item.get("text", "")
            start = float(item.get("start", 0))
            duration = float(item.get("duration", 0))
        else:
            text = getattr(item, "text", "")
            start = float(getattr(item, "start", 0))
            duration = float(getattr(item, "duration", 0))
        text = clean_caption_text(text)
        if text:
            segments.append(
                {
                    "start_ms": int(start * 1000),
                    "duration_ms": int(duration * 1000),
                    "text": text,
                }
            )
    return segments


def extract_inner_tube_data(page: str) -> tuple[str | None, dict[str, Any] | None]:
    key_match = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', page)
    api_key = key_match.group(1) if key_match else None
    context = extract_balanced_json(page, '"INNERTUBE_CONTEXT":')
    return api_key, context


def extract_transcript_params(page: str) -> str | None:
    match = re.search(r'"getTranscriptEndpoint":\{"params":"([^"]+)"\}', page)
    return match.group(1) if match else None


def text_from_runs(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    if "simpleText" in value:
        return str(value["simpleText"])
    if "runs" in value:
        return "".join(str(run.get("text", "")) for run in value["runs"])
    return ""


def walk_transcript_cues(value: Any) -> list[dict[str, Any]]:
    cues: list[dict[str, Any]] = []
    if isinstance(value, dict):
        renderer = value.get("transcriptCueRenderer")
        if isinstance(renderer, dict):
            text = clean_caption_text(text_from_runs(renderer.get("cue", {})))
            start_ms = int(renderer.get("startOffsetMs", 0) or 0)
            duration_ms = int(renderer.get("durationMs", 0) or 0)
            if text:
                cues.append(
                    {
                        "start_ms": start_ms,
                        "duration_ms": duration_ms,
                        "text": text,
                    }
                )
        for child in value.values():
            cues.extend(walk_transcript_cues(child))
    elif isinstance(value, list):
        for child in value:
            cues.extend(walk_transcript_cues(child))
    return cues


def fetch_with_inner_tube_transcript(page: str, watch_url: str) -> list[dict[str, Any]]:
    api_key, context = extract_inner_tube_data(page)
    params = extract_transcript_params(page)
    if not api_key or not context or not params:
        return []

    endpoint = f"https://www.youtube.com/youtubei/v1/get_transcript?key={api_key}"
    payload = {"context": context, "params": params}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://www.youtube.com",
        "Referer": watch_url,
    }
    try:
        response = http_post_json(endpoint, payload, headers)
    except urllib.error.HTTPError:
        return []
    segments = walk_transcript_cues(response)
    return sorted(segments, key=lambda item: item["start_ms"])


def parse_vtt_timestamp(value: str) -> int:
    value = value.strip().replace(",", ".")
    parts = value.split(":")
    if len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
        seconds = float(parts[1])
    else:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
    return int(((hours * 3600) + (minutes * 60) + seconds) * 1000)


def parse_vtt_captions(raw: str) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        if "-->" not in line:
            idx += 1
            continue
        start_text, end_text = [part.strip().split(" ")[0] for part in line.split("-->", 1)]
        idx += 1
        text_lines: list[str] = []
        while idx < len(lines) and lines[idx].strip():
            text_lines.append(lines[idx].strip())
            idx += 1
        text = " ".join(text_lines)
        text = re.sub(r"<[^>]+>", "", text)
        text = clean_caption_text(text)
        if text:
            start_ms = parse_vtt_timestamp(start_text)
            end_ms = parse_vtt_timestamp(end_text)
            segments.append(
                {
                    "start_ms": start_ms,
                    "duration_ms": max(0, end_ms - start_ms),
                    "text": text,
                }
            )
        idx += 1
    return segments


def parse_caption_file(path: Path) -> list[dict[str, Any]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    suffix = path.suffix.lower()
    if suffix == ".json3":
        return parse_json3_captions(raw)
    if suffix == ".vtt":
        return parse_vtt_captions(raw)
    if suffix in {".srv3", ".xml"}:
        return parse_xml_captions(raw)
    return []


def fetch_with_ytdlp(
    video_id: str,
    watch_url: str,
    preferred_langs: list[str],
) -> list[dict[str, Any]]:
    ytdlp = shutil.which("yt-dlp")
    if not ytdlp:
        local_candidate = Path(sys.executable).with_name("yt-dlp.exe")
        if local_candidate.exists():
            ytdlp = str(local_candidate)
    if not ytdlp:
        return []

    lang_expr = ",".join(dict.fromkeys(preferred_langs + ["zh.*", "en.*"]))
    with tempfile.TemporaryDirectory() as temp_dir:
        output_template = str(Path(temp_dir) / "%(id)s.%(ext)s")
        cmd = [
            ytdlp,
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            lang_expr,
            "--sub-format",
            "json3/vtt/srv3/best",
            "-o",
            output_template,
            watch_url,
        ]
        try:
            subprocess.run(
                cmd,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=120,
            )
        except Exception:
            return []

        files = sorted(Path(temp_dir).glob(f"{video_id}.*"))
        preferred_suffixes = [".json3", ".vtt", ".srv3", ".xml"]
        files.sort(
            key=lambda path: (
                preferred_suffixes.index(path.suffix.lower())
                if path.suffix.lower() in preferred_suffixes
                else 99,
                str(path),
            )
        )
        for path in files:
            if path.suffix.lower() not in preferred_suffixes:
                continue
            try:
                segments = parse_caption_file(path)
            except Exception:
                segments = []
            if segments:
                return segments
    return []


def fetch_transcript_segments(
    video_id: str,
    watch_url: str,
    page: str,
    tracks: list[dict[str, Any]],
    preferred_langs: list[str],
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    errors: list[str] = []
    track: dict[str, Any] | None = None

    if tracks:
        try:
            track = choose_caption_track(tracks, preferred_langs)
            segments = fetch_captions(track)
            if segments:
                return segments, {
                    "source": "youtube_caption_track",
                    "language": str(track.get("languageCode", "")),
                    "name": track_name(track),
                    "kind": str(track.get("kind", "manual")),
                }
        except Exception as exc:
            errors.append(f"caption track: {exc}")

    segments = fetch_with_youtube_transcript_api(video_id, preferred_langs)
    if segments:
        return segments, {
            "source": "youtube_transcript_api",
            "language": ",".join(preferred_langs),
            "name": "youtube-transcript-api",
            "kind": "fallback",
        }
    errors.append("youtube-transcript-api: unavailable or no transcript")

    segments = fetch_with_inner_tube_transcript(page, watch_url)
    if segments:
        return segments, {
            "source": "youtubei_get_transcript",
            "language": ",".join(preferred_langs),
            "name": "YouTube transcript endpoint",
            "kind": "fallback",
        }
    errors.append("youtubei get_transcript: unavailable or blocked")

    segments = fetch_with_ytdlp(video_id, watch_url, preferred_langs)
    if segments:
        return segments, {
            "source": "yt-dlp",
            "language": ",".join(preferred_langs),
            "name": "yt-dlp subtitles",
            "kind": "fallback",
        }
    errors.append("yt-dlp: not installed or no subtitles downloaded")

    hint = (
        "No transcript text could be fetched automatically. "
        "Install fallback tools once with `python -m pip install yt-dlp "
        "youtube-transcript-api`, then rerun. If the video truly has no usable "
        "captions, use an audio transcription fallback."
    )
    raise RuntimeError(hint + " Attempts: " + " | ".join(errors))


def format_ts(ms: int) -> str:
    total_seconds = round(ms / 1000)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def slugify(text: str, fallback: str) -> str:
    text = text.lower()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = text.strip("-")
    return (text[:70].strip("-") or fallback).lower()


def detect_tickers(
    segments: list[dict[str, Any]],
    extra_texts: list[str] | None = None,
) -> list[str]:
    counts: dict[str, int] = {}
    pattern = re.compile(r"(?<![A-Z0-9])\$?([A-Z]{2,5})(?![A-Z0-9])")
    texts = [segment["text"] for segment in segments]
    if extra_texts:
        texts.extend(extra_texts)
    for text in texts:
        for match in pattern.finditer(text):
            ticker = match.group(1)
            if ticker in TICKER_STOPWORDS:
                continue
            counts[ticker] = counts.get(ticker, 0) + 1
    return [ticker for ticker, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))]


def grouped_segments(
    segments: list[dict[str, Any]],
    max_gap_ms: int = 2500,
    max_chars: int = 260,
) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for segment in segments:
        text = segment["text"]
        if not current:
            current = {
                "start_ms": segment["start_ms"],
                "duration_ms": segment["duration_ms"],
                "text": text,
                "end_ms": segment["start_ms"] + segment["duration_ms"],
            }
            continue

        gap = segment["start_ms"] - current["end_ms"]
        next_text = f"{current['text']} {text}".strip()
        if gap <= max_gap_ms and len(next_text) <= max_chars:
            current["text"] = next_text
            current["end_ms"] = segment["start_ms"] + segment["duration_ms"]
            current["duration_ms"] = current["end_ms"] - current["start_ms"]
        else:
            groups.append(current)
            current = {
                "start_ms": segment["start_ms"],
                "duration_ms": segment["duration_ms"],
                "text": text,
                "end_ms": segment["start_ms"] + segment["duration_ms"],
            }

    if current:
        groups.append(current)
    for group in groups:
        group.pop("end_ms", None)
    return groups


def score_segment(text: str, tickers: set[str]) -> int:
    score = 0
    upper = text.upper()
    for ticker in tickers:
        if re.search(rf"(?<![A-Z0-9])\$?{re.escape(ticker)}(?![A-Z0-9])", upper):
            score += 4
    for term in KEY_TERMS:
        if term in text:
            score += 2
    if re.search(r"\d+(\.\d+)?\s*(美元|%|亿|万|billion|million)", text, re.I):
        score += 2
    return score


def candidate_segments(
    segments: list[dict[str, Any]],
    tickers: list[str],
    limit: int = 80,
) -> list[dict[str, Any]]:
    ticker_set = set(tickers)
    scored = []
    for segment in segments:
        score = score_segment(segment["text"], ticker_set)
        if score > 0:
            scored.append((score, segment))
    scored.sort(key=lambda item: (-item[0], item[1]["start_ms"]))
    selected = sorted([segment for _, segment in scored[:limit]], key=lambda item: item["start_ms"])
    return selected


def transcript_lines(segments: list[dict[str, Any]]) -> list[str]:
    return [f"[{format_ts(seg['start_ms'])}] {seg['text']}" for seg in segments]


def build_metadata(video_id: str, player_response: dict[str, Any], url: str) -> dict[str, str]:
    details = player_response.get("videoDetails", {})
    micro = get_nested(player_response, ["microformat", "playerMicroformatRenderer"], {})
    return {
        "title": str(details.get("title") or micro.get("title", {}).get("simpleText") or video_id),
        "channel": str(details.get("author") or micro.get("ownerChannelName") or ""),
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "input_url": url,
        "published": str(micro.get("publishDate") or ""),
        "length_seconds": str(details.get("lengthSeconds") or ""),
        "view_count": str(details.get("viewCount") or ""),
        "retrieved": now_iso(),
    }


def metadata_md(metadata: dict[str, str]) -> str:
    rows = [
        ("Title", metadata["title"]),
        ("Channel", metadata["channel"]),
        ("Published", metadata["published"]),
        ("Retrieved", metadata["retrieved"]),
        ("URL", metadata["url"]),
        ("Video ID", metadata["video_id"]),
        ("Length Seconds", metadata["length_seconds"]),
        ("View Count", metadata["view_count"]),
    ]
    return "\n".join(f"- {key}: {value}" for key, value in rows if value)


def write_transcript_file(
    out_dir: Path,
    filename_base: str,
    metadata: dict[str, str],
    track: dict[str, Any],
    segments: list[dict[str, Any]],
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{filename_base}_transcript.md"
    content = "\n".join(
        [
            f"# Transcript: {metadata['title']}",
            "",
            "## Metadata",
            metadata_md(metadata),
            "",
            "## Caption Track",
            f"- Language: {track.get('languageCode', '')}",
            f"- Name: {track_name(track)}",
            f"- Kind: {track.get('kind', 'manual')}",
            "",
            "## Transcript",
            "\n".join(transcript_lines(segments)),
            "",
        ]
    )
    path.write_text(content, encoding="utf-8")
    return path


def build_extract_note(
    metadata: dict[str, str],
    track: dict[str, Any],
    segments: list[dict[str, Any]],
) -> str:
    grouped = grouped_segments(segments)
    tickers = detect_tickers(segments, [metadata["title"]])
    candidates = candidate_segments(grouped, tickers)
    ticker_text = ", ".join(tickers) if tickers else "None detected"
    candidate_text = "\n".join(
        f"- [{format_ts(seg['start_ms'])}] {seg['text']}" for seg in candidates
    )
    if not candidate_text:
        candidate_text = "- No high-signal candidate segments detected."

    prompt = textwrap.dedent(
        """\
        Copy the transcript into an LLM with this prompt:

        请把这段美股投资视频 transcript 转成研究笔记。
        1. 提取所有股票代码和公司。
        2. 对每只股票标记：看多、看空、中性、只提及。
        3. 提取明确预测：价格、时间、财报方向、涨跌幅、买卖点。
        4. 区分事实、推论、情绪、营销话术。
        5. 标出需要核验的数据点。
        6. 保留关键时间戳。
        7. 判断内容适合：短线信号、财报观察、长期研究，还是市场情绪样本。
        """
    )

    return "\n".join(
        [
            f"# Video Research Draft: {metadata['title']}",
            "",
            "> Generated without LLM. This is an extractive draft based on tickers,",
            "> finance keywords, numbers, and timestamped transcript segments.",
            "",
            "## Metadata",
            metadata_md(metadata),
            "",
            "## Caption Track",
            f"- Language: {track.get('languageCode', '')}",
            f"- Name: {track_name(track)}",
            f"- Kind: {track.get('kind', 'manual')}",
            "",
            "## Detected Tickers",
            ticker_text,
            "",
            "## Candidate Timestamped Claims",
            candidate_text,
            "",
            "## Next-Step Prompt",
            "```text",
            prompt.strip(),
            "```",
            "",
        ]
    )


def chunk_lines(lines: list[str], max_chars: int) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for line in lines:
        line_len = len(line) + 1
        if current and current_len + line_len > max_chars:
            chunks.append("\n".join(current))
            current = []
            current_len = 0
        current.append(line)
        current_len += line_len
    if current:
        chunks.append("\n".join(current))
    return chunks


def call_llm(prompt: str, model: str, base_url: str, api_key: str) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "temperature": 0.1,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an investment research assistant. "
                    "Extract claims carefully, distinguish facts from opinions, "
                    "and keep timestamp references."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    response = http_post_json(url, payload, headers)
    return response["choices"][0]["message"]["content"].strip()


def build_llm_note(
    metadata: dict[str, str],
    segments: list[dict[str, Any]],
    model: str,
    base_url: str,
    api_key: str,
    chunk_chars: int,
) -> str:
    lines = transcript_lines(segments)
    chunks = chunk_lines(lines, chunk_chars)
    chunk_notes: list[str] = []

    for idx, chunk in enumerate(chunks, start=1):
        prompt = textwrap.dedent(
            f"""\
            下面是一个美股投资视频 transcript 的第 {idx}/{len(chunks)} 段。
            请只基于这段文字提取信息，不要补脑。

            输出 Markdown，包含：
            - 本段一句话总结
            - 股票观点表：Ticker/公司/看多看空中性/时间框架/证据时间戳
            - 明确预测：价格、时间、财报方向、涨跌幅、买卖点
            - 事实 / 推论 / 情绪 / 营销话术
            - 需要核验的数据点

            Transcript:
            {chunk}
            """
        )
        chunk_notes.append(call_llm(prompt, model, base_url, api_key))

    combined = "\n\n---\n\n".join(
        f"## Chunk {idx}\n\n{note}" for idx, note in enumerate(chunk_notes, start=1)
    )
    final_prompt = textwrap.dedent(
        f"""\
        请把以下分段摘录合并成一篇中文投资视频研究笔记。

        视频信息：
        - 标题：{metadata['title']}
        - 频道：{metadata['channel']}
        - 发布时间：{metadata['published']}
        - 链接：{metadata['url']}

        最终输出结构：
        # Video Research Note: {metadata['title']}
        ## One-Line Summary
        ## Stocks Mentioned
        用表格：Ticker / View / Time Frame / Evidence / Confidence
        ## Key Timestamped Claims
        ## Verifiable Predictions
        ## Fact / Inference / Emotion / Marketing Split
        ## Missing Risk Controls
        ## Follow-Up Checks
        ## Research Use
        判断它适合短线信号、财报观察、长期研究、市场情绪样本中的哪几类。

        分段摘录如下：
        {combined}
        """
    )
    return call_llm(final_prompt, model, base_url, api_key)


def write_note_file(out_dir: Path, filename_base: str, content: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{filename_base}_note.md"
    path.write_text(content + "\n", encoding="utf-8")
    return path


def list_tracks(tracks: list[dict[str, Any]]) -> None:
    for idx, track in enumerate(tracks, start=1):
        print(
            f"{idx}. lang={track.get('languageCode', '')} "
            f"kind={track.get('kind', 'manual')} name={track_name(track)}"
        )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a timestamped investment note from a YouTube URL."
    )
    parser.add_argument("url", help="YouTube URL or 11-character video id")
    parser.add_argument(
        "--lang",
        action="append",
        dest="langs",
        help="Preferred caption language. Can be repeated. Defaults to zh/en.",
    )
    parser.add_argument(
        "--list-tracks",
        action="store_true",
        help="List available caption tracks and exit.",
    )
    parser.add_argument(
        "--llm",
        action="store_true",
        help="Use an OpenAI-compatible chat completions API to create the note.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        help="Chat model for --llm. Defaults to OPENAI_MODEL or gpt-4o-mini.",
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        help="OpenAI-compatible API base URL.",
    )
    parser.add_argument(
        "--chunk-chars",
        type=int,
        default=18000,
        help="Maximum transcript characters per LLM chunk.",
    )
    parser.add_argument(
        "--sources-dir",
        type=Path,
        default=ROOT / "sources" / "videos",
        help="Directory for transcript source files.",
    )
    parser.add_argument(
        "--notes-dir",
        type=Path,
        default=ROOT / "notes" / "videos",
        help="Directory for generated research notes.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    preferred_langs = args.langs or DEFAULT_LANGS
    video_id = parse_video_id(args.url)
    url = f"https://www.youtube.com/watch?v={video_id}"

    page = http_get_text(url)
    player_response = extract_player_response(page)
    metadata = build_metadata(video_id, player_response, args.url)

    tracks = get_nested(
        player_response,
        ["captions", "playerCaptionsTracklistRenderer", "captionTracks"],
        [],
    )

    if args.list_tracks:
        if not tracks:
            print("No caption tracks found in the YouTube page.")
            return 0
        list_tracks(tracks)
        return 0

    segments, track = fetch_transcript_segments(
        video_id=video_id,
        watch_url=url,
        page=page,
        tracks=tracks,
        preferred_langs=preferred_langs,
    )

    date_raw = metadata["published"] or dt.date.today().isoformat()
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", date_raw)
    date_part = date_match.group(0) if date_match else slugify(date_raw, dt.date.today().isoformat())
    filename_base = f"{date_part}_{video_id}_{slugify(metadata['title'], video_id)}"

    transcript_path = write_transcript_file(
        args.sources_dir, filename_base, metadata, track, segments
    )

    if args.llm:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("Set OPENAI_API_KEY or run without --llm.")
        note = build_llm_note(
            metadata=metadata,
            segments=segments,
            model=args.model,
            base_url=args.base_url,
            api_key=api_key,
            chunk_chars=args.chunk_chars,
        )
    else:
        note = build_extract_note(metadata, track, segments)

    note_path = write_note_file(args.notes_dir, filename_base, note)

    print(f"Transcript: {transcript_path}")
    print(f"Note: {note_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (RuntimeError, ValueError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
