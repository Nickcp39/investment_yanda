#!/usr/bin/env python3
"""
Resume-safe YouTube audio transcription queue.

The script consumes a channel manifest CSV/JSONL, downloads one best-audio file
per video with yt-dlp, transcribes it with faster-whisper, and writes one
Markdown plus one JSON checkpoint per video id.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import time
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Any


try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass

warnings.filterwarnings("ignore", message="pkg_resources is deprecated.*")

ROOT = Path(__file__).resolve().parents[1]
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


@dataclass(frozen=True)
class VideoItem:
    index: int
    id: str
    title: str
    url: str
    upload_date: str = ""
    duration: str = ""
    view_count: str = ""


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Transcribe YouTube channel audio.")
    parser.add_argument("--input", required=True, type=Path, help="Manifest CSV/JSONL.")
    parser.add_argument("--channel-slug", required=True, help="Stable output folder slug.")
    parser.add_argument("--audio-dir", type=Path, help="Directory for downloaded audio.")
    parser.add_argument("--transcripts-dir", type=Path, help="Directory for transcript outputs.")
    parser.add_argument("--state-dir", type=Path, help="Run report directory.")
    parser.add_argument("--yt-dlp", type=Path, help="Path to yt-dlp.")
    parser.add_argument("--model", default="base", help="faster-whisper model name/path.")
    parser.add_argument("--device", default="cpu", help="faster-whisper device.")
    parser.add_argument("--compute-type", default="int8", help="faster-whisper compute type.")
    parser.add_argument("--language", default="zh", help="Language hint, blank for auto.")
    parser.add_argument("--beam-size", type=int, default=5)
    parser.add_argument("--sleep", type=float, default=5.0, help="Seconds between videos.")
    parser.add_argument("--limit", type=int, help="Only process first N manifest items.")
    parser.add_argument("--start-index", type=int, help="Only process rows with index >= N.")
    parser.add_argument("--end-index", type=int, help="Only process rows with index <= N.")
    parser.add_argument("--force", action="store_true", help="Re-transcribe existing outputs.")
    parser.add_argument("--download-only", action="store_true", help="Only download audio.")
    parser.add_argument("--export-only", action="store_true", help="Only rebuild progress files.")
    parser.add_argument("--dry-run", action="store_true", help="Show plan without writes.")
    return parser.parse_args()


def resolve_path(path: Path | None, default: Path) -> Path:
    chosen = path if path is not None else default
    if chosen.is_absolute():
        return chosen
    return (ROOT / chosen).resolve()


def canonical_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def parse_video_id(value: str) -> str:
    value = (value or "").strip()
    if VIDEO_ID_RE.fullmatch(value):
        return value
    match = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", value)
    if match:
        return match.group(1)
    match = re.search(r"youtu\.be/([A-Za-z0-9_-]{11})", value)
    if match:
        return match.group(1)
    raise ValueError(f"Could not parse YouTube id from: {value}")


def load_manifest(path: Path) -> list[VideoItem]:
    if path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    elif path.suffix.lower() in {".jsonl", ".ndjson"}:
        rows = []
        with path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                if line.strip():
                    rows.append(json.loads(line))
    else:
        raise ValueError(f"Unsupported manifest extension: {path.suffix}")

    items: list[VideoItem] = []
    seen: set[str] = set()
    for fallback_index, row in enumerate(rows, start=1):
        video_id = parse_video_id(str(row.get("id") or row.get("url") or ""))
        if video_id in seen:
            continue
        raw_index = str(row.get("index") or "").strip()
        try:
            index = int(raw_index)
        except ValueError:
            index = fallback_index
        items.append(
            VideoItem(
                index=index,
                id=video_id,
                title=str(row.get("title") or "").strip(),
                url=str(row.get("url") or canonical_url(video_id)).strip(),
                upload_date=str(row.get("upload_date") or "").strip(),
                duration=str(row.get("duration") or "").strip(),
                view_count=str(row.get("view_count") or "").strip(),
            )
        )
        seen.add(video_id)
    return items


def find_yt_dlp(path_arg: Path | None) -> Path:
    candidates: list[Path] = []
    if path_arg is not None:
        candidates.append(path_arg)
    candidates.append(ROOT / ".venv" / "Scripts" / "yt-dlp.exe")
    for candidate in candidates:
        candidate = candidate if candidate.is_absolute() else ROOT / candidate
        if candidate.exists():
            return candidate.resolve()
    found = shutil.which("yt-dlp")
    if found:
        return Path(found).resolve()
    raise FileNotFoundError("Could not find yt-dlp.")


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    temp_path.replace(path)


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None


def format_ts(seconds: float) -> str:
    total = int(round(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def audio_candidates(audio_dir: Path, video_id: str) -> list[Path]:
    return sorted(
        path
        for path in audio_dir.glob(f"{video_id}.*")
        if path.suffix.lower() not in {".part", ".ytdl", ".json"}
    )


def download_audio(yt_dlp: Path, item: VideoItem, audio_dir: Path, timeout: int = 900) -> Path:
    existing = audio_candidates(audio_dir, item.id)
    if existing:
        return existing[0]

    audio_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(audio_dir / "%(id)s.%(ext)s")
    command = [
        str(yt_dlp),
        "-f",
        "ba",
        "--no-playlist",
        "--retries",
        "10",
        "--extractor-retries",
        "10",
        "-o",
        output_template,
        item.url,
    ]
    proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout)[-4000:])
    candidates = audio_candidates(audio_dir, item.id)
    if not candidates:
        raise RuntimeError("yt-dlp finished but no audio file was found.")
    return candidates[0]


def transcript_paths(transcripts_dir: Path, video_id: str) -> tuple[Path, Path, Path]:
    return (
        transcripts_dir / f"{video_id}_asr.md",
        transcripts_dir / f"{video_id}_asr.json",
        transcripts_dir / f"{video_id}.error.json",
    )


def transcribe_audio(model: Any, audio_path: Path, language: str, beam_size: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    lang = language.strip() or None
    segments_iter, info = model.transcribe(
        str(audio_path),
        language=lang,
        vad_filter=False,
        beam_size=beam_size,
    )
    segments: list[dict[str, Any]] = []
    for segment in segments_iter:
        segments.append(
            {
                "start": float(segment.start),
                "end": float(segment.end),
                "text": segment.text.strip(),
            }
        )
    info_dict = {
        "language": info.language,
        "language_probability": float(info.language_probability),
        "duration": float(info.duration),
    }
    return info_dict, segments


def write_transcript(item: VideoItem, audio_path: Path, model_name: str, info: dict[str, Any], segments: list[dict[str, Any]], md_path: Path, json_path: Path) -> None:
    md_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "video": item.__dict__,
        "audio_path": str(audio_path),
        "model": model_name,
        "info": info,
        "segments": segments,
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    atomic_write_json(json_path, payload)

    lines = [
        f"# ASR Transcript: {item.title or item.id}",
        "",
        "## Metadata",
        f"- Date: {item.upload_date}",
        f"- URL: {item.url}",
        f"- Video ID: {item.id}",
        f"- Duration: {item.duration}",
        f"- Views: {item.view_count}",
        f"- ASR model: {model_name}",
        f"- ASR language: {info.get('language', '')}",
        f"- Language probability: {info.get('language_probability', ''):.3f}",
        "",
        "## Transcript",
    ]
    for segment in segments:
        text = segment.get("text", "").strip()
        if text:
            lines.append(f"[{format_ts(float(segment['start']))}] {text}")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_progress(items: list[VideoItem], transcripts_dir: Path, state_dir: Path, summary: dict[str, Any]) -> dict[str, Path]:
    state_dir.mkdir(parents=True, exist_ok=True)
    progress_path = state_dir / "progress.csv"
    failed_path = state_dir / "failed.csv"
    missing_path = state_dir / "missing.csv"
    summary_path = state_dir / "run_summary.json"
    fields = ["index", "id", "title", "url", "status", "transcript", "error_type", "message"]
    rows: list[dict[str, Any]] = []
    failed_rows: list[dict[str, Any]] = []
    missing_rows: list[dict[str, Any]] = []

    for item in items:
        md_path, _json_path, error_path = transcript_paths(transcripts_dir, item.id)
        error = read_json(error_path) if error_path.exists() else {}
        if md_path.exists():
            status = "success"
        elif error_path.exists():
            status = "failed"
        else:
            status = "missing"
        row = {
            "index": item.index,
            "id": item.id,
            "title": item.title,
            "url": item.url,
            "status": status,
            "transcript": str(md_path) if md_path.exists() else "",
            "error_type": (error or {}).get("error_type", ""),
            "message": (error or {}).get("message", ""),
        }
        rows.append(row)
        if status == "failed":
            failed_rows.append(row)
        if status != "success":
            missing_rows.append(row)

    for path, output_rows in (
        (progress_path, rows),
        (failed_path, failed_rows),
        (missing_path, missing_rows),
    ):
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(output_rows)
    atomic_write_json(summary_path, summary)
    return {
        "progress": progress_path,
        "failed": failed_path,
        "missing": missing_path,
        "summary": summary_path,
    }


def main() -> int:
    args = parse_args()
    input_path = args.input if args.input.is_absolute() else (ROOT / args.input).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Input manifest does not exist: {input_path}")

    base_dir = ROOT / "sources" / "channels" / args.channel_slug
    run_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_dir = resolve_path(args.audio_dir, base_dir / "audio")
    transcripts_dir = resolve_path(args.transcripts_dir, base_dir / "transcripts")
    state_dir = resolve_path(args.state_dir, base_dir / "runs" / f"asr_{run_stamp}")
    items = load_manifest(input_path)
    if args.start_index is not None:
        items = [item for item in items if item.index >= args.start_index]
    if args.end_index is not None:
        items = [item for item in items if item.index <= args.end_index]
    if args.limit:
        items = items[: args.limit]

    if args.dry_run:
        print("Dry run only; no files will be written.")
        print(f"Input: {input_path}")
        print(f"Items: {len(items)}")
        print(f"Audio dir: {audio_dir}")
        print(f"Transcripts dir: {transcripts_dir}")
        print(f"State dir: {state_dir}")
        print(f"Model: {args.model}")
        return 0

    yt_dlp = find_yt_dlp(args.yt_dlp)
    audio_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    state_dir.mkdir(parents=True, exist_ok=True)

    model = None
    if not args.export_only and not args.download_only:
        from faster_whisper import WhisperModel

        print(f"Loading faster-whisper model: {args.model}")
        model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)
        print("Model loaded.")

    processed = skipped = failed = downloaded = 0
    for position, item in enumerate(items, start=1):
        md_path, json_path, error_path = transcript_paths(transcripts_dir, item.id)
        if md_path.exists() and json_path.exists() and not args.force:
            skipped += 1
            print(f"[{position}/{len(items)}] skip existing {item.id}")
            continue
        if args.export_only:
            continue

        print(f"[{position}/{len(items)}] audio {item.id} {item.title}")
        try:
            audio_path = download_audio(yt_dlp, item, audio_dir)
            downloaded += 1
            if args.download_only:
                processed += 1
                continue
            assert model is not None
            print(f"[{position}/{len(items)}] transcribe {item.id}")
            info, segments = transcribe_audio(model, audio_path, args.language, args.beam_size)
            write_transcript(item, audio_path, args.model, info, segments, md_path, json_path)
            if error_path.exists():
                error_path.unlink()
            processed += 1
        except Exception as exc:
            failed += 1
            error = {
                "id": item.id,
                "url": item.url,
                "title": item.title,
                "error_type": type(exc).__name__,
                "message": str(exc)[-4000:],
                "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            }
            atomic_write_json(error_path, error)
            eprint(f"  failed {item.id}: {type(exc).__name__}: {exc}")

        summary = {
            "input": str(input_path),
            "channel_slug": args.channel_slug,
            "total_items": len(items),
            "processed_this_run": processed,
            "skipped_this_run": skipped,
            "failed_this_run": failed,
            "downloaded_or_reused_audio_this_run": downloaded,
            "audio_dir": str(audio_dir),
            "transcripts_dir": str(transcripts_dir),
            "state_dir": str(state_dir),
            "model": args.model,
            "device": args.device,
            "compute_type": args.compute_type,
            "language": args.language,
            "updated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        }
        write_progress(items, transcripts_dir, state_dir, summary)
        if args.sleep > 0 and position < len(items):
            time.sleep(args.sleep)

    success_count = sum(1 for item in items if transcript_paths(transcripts_dir, item.id)[0].exists())
    missing_count = max(len(items) - success_count, 0)
    summary = {
        "input": str(input_path),
        "channel_slug": args.channel_slug,
        "total_items": len(items),
        "success_transcripts": success_count,
        "missing_or_failed": missing_count,
        "processed_this_run": processed,
        "skipped_this_run": skipped,
        "failed_this_run": failed,
        "downloaded_or_reused_audio_this_run": downloaded,
        "audio_dir": str(audio_dir),
        "transcripts_dir": str(transcripts_dir),
        "state_dir": str(state_dir),
        "model": args.model,
        "device": args.device,
        "compute_type": args.compute_type,
        "language": args.language,
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    state_files = write_progress(items, transcripts_dir, state_dir, summary)

    print("")
    print("Done.")
    print(f"  total items:          {len(items)}")
    print(f"  success transcripts: {success_count}")
    print(f"  missing or failed:   {missing_count}")
    print(f"  transcripts dir:     {transcripts_dir}")
    print(f"  progress:            {state_files['progress']}")
    return 0 if missing_count == 0 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        eprint("Interrupted.")
        raise SystemExit(130)
