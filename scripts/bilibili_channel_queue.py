#!/usr/bin/env python3
"""
Resume-safe Bilibili space metadata collector.

The script consumes a flat Bilibili manifest, fetches each BV video with
yt-dlp, stores one checkpoint JSON per BVID, and exports compact CSV, JSONL,
and Markdown manifests from successful checkpoints.
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
from dataclasses import dataclass
from pathlib import Path
from typing import Any


try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass


ROOT = Path(__file__).resolve().parents[1]
BVID_RE = re.compile(r"^BV[0-9A-Za-z]{10}$")
EXPORT_FIELDS = [
    "index",
    "upload_date",
    "id",
    "title",
    "url",
    "duration",
    "view_count",
    "like_count",
    "comment_count",
    "uploader",
    "uploader_id",
    "tags",
    "subtitle_languages",
]


@dataclass(frozen=True)
class VideoItem:
    index: int
    id: str
    title: str
    url: str


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch Bilibili video metadata from a flat space manifest."
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Flat CSV or JSONL manifest containing id/url columns.",
    )
    parser.add_argument(
        "--channel-slug",
        default="bilibili-1039025435",
        help="Stable folder/output prefix slug.",
    )
    parser.add_argument("--cache-dir", type=Path, help="Checkpoint directory.")
    parser.add_argument("--output-dir", type=Path, help="Manifest export directory.")
    parser.add_argument("--state-dir", type=Path, help="Run report directory.")
    parser.add_argument("--output-prefix", help="Output basename without extension.")
    parser.add_argument(
        "--date-stamp",
        default=dt.date.today().isoformat(),
        help="Date stamp for default output names.",
    )
    parser.add_argument("--yt-dlp", type=Path, help="Path to yt-dlp.")
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--extractor-retries", type=int, default=5)
    parser.add_argument("--socket-timeout", type=int, default=30)
    parser.add_argument("--item-timeout", type=int, default=240)
    parser.add_argument("--sleep", type=float, default=0.8)
    parser.add_argument("--limit", type=int, help="Only process first N rows.")
    parser.add_argument("--force", action="store_true", help="Re-fetch existing items.")
    parser.add_argument("--export-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def canonical_url(bvid: str) -> str:
    return f"https://www.bilibili.com/video/{bvid}"


def parse_bvid(value: str) -> str:
    value = (value or "").strip()
    if BVID_RE.fullmatch(value):
        return value
    match = re.search(r"/video/(BV[0-9A-Za-z]{10})", value)
    if match:
        return match.group(1)
    match = re.search(r"\b(BV[0-9A-Za-z]{10})\b", value)
    if match:
        return match.group(1)
    raise ValueError(f"Could not parse Bilibili BVID from: {value}")


def resolve_path(path: Path | None, default: Path) -> Path:
    chosen = path if path is not None else default
    if chosen.is_absolute():
        return chosen
    return (ROOT / chosen).resolve()


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
        bvid = parse_bvid(str(row.get("id") or row.get("url") or ""))
        if bvid in seen:
            continue
        raw_index = str(row.get("index") or "").strip()
        try:
            index = int(raw_index)
        except ValueError:
            index = fallback_index
        items.append(
            VideoItem(
                index=index,
                id=bvid,
                title=str(row.get("title") or "").strip(),
                url=str(row.get("url") or canonical_url(bvid)).strip(),
            )
        )
        seen.add(bvid)
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


def parse_yt_dlp_json(stdout: str) -> dict[str, Any]:
    stdout = stdout.strip()
    if not stdout:
        raise ValueError("yt-dlp returned empty stdout")
    return json.loads(stdout)


def fetch_one(
    yt_dlp: Path,
    item: VideoItem,
    retries: int,
    extractor_retries: int,
    socket_timeout: int,
    item_timeout: int,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    command = [
        str(yt_dlp),
        "--skip-download",
        "--dump-single-json",
        "--no-playlist",
        "--no-warnings",
        "--retries",
        str(retries),
        "--extractor-retries",
        str(extractor_retries),
        "--socket-timeout",
        str(socket_timeout),
        item.url,
    ]

    started_at = dt.datetime.now(dt.timezone.utc)
    try:
        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=item_timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return None, error_payload(item, started_at, "timeout", None, str(exc), "")

    finished_at = dt.datetime.now(dt.timezone.utc)
    if proc.returncode != 0:
        return None, error_payload(
            item,
            started_at,
            "yt-dlp",
            proc.returncode,
            proc.stderr[-4000:],
            proc.stdout[-1000:],
            finished_at,
        )

    try:
        info = parse_yt_dlp_json(proc.stdout)
    except json.JSONDecodeError as exc:
        return None, error_payload(
            item,
            started_at,
            "json",
            proc.returncode,
            proc.stderr[-4000:],
            proc.stdout[-4000:],
            finished_at,
            str(exc),
        )

    info["_collector"] = {
        "fetched_at": finished_at.isoformat(),
        "source_url": item.url,
        "source_index": item.index,
        "source_title": item.title,
    }
    return info, None


def error_payload(
    item: VideoItem,
    started_at: dt.datetime,
    error_type: str,
    returncode: int | None,
    stderr: str,
    stdout: str,
    finished_at: dt.datetime | None = None,
    message: str = "",
) -> dict[str, Any]:
    finished_at = finished_at or dt.datetime.now(dt.timezone.utc)
    return {
        "id": item.id,
        "url": item.url,
        "title": item.title,
        "started_at": started_at.isoformat(),
        "finished_at": finished_at.isoformat(),
        "error_type": error_type,
        "returncode": returncode,
        "stderr": stderr,
        "stdout": stdout,
        "message": message,
    }


def parse_upload_date(value: Any) -> str:
    if isinstance(value, (int, float)) and value > 0:
        return dt.datetime.fromtimestamp(value, dt.timezone.utc).date().isoformat()
    text = str(value or "").strip()
    if re.fullmatch(r"\d{8}", text):
        return f"{text[0:4]}-{text[4:6]}-{text[6:8]}"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return text
    return ""


def duration_to_text(info: dict[str, Any]) -> str:
    if info.get("duration_string"):
        return str(info["duration_string"])
    duration = info.get("duration")
    if isinstance(duration, (int, float)) and duration >= 0:
        total = int(duration)
        hours, rem = divmod(total, 3600)
        minutes, seconds = divmod(rem, 60)
        if hours:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"
    return ""


def subtitle_languages(info: dict[str, Any]) -> str:
    subtitles = info.get("subtitles")
    if isinstance(subtitles, dict) and subtitles:
        return ",".join(sorted(str(key) for key in subtitles))
    return ""


def compact_row(item: VideoItem, info: dict[str, Any]) -> dict[str, Any]:
    collector = info.get("_collector") or {}
    tags = info.get("tags")
    if isinstance(tags, list):
        tag_text = ";".join(str(tag) for tag in tags)
    else:
        tag_text = ""
    return {
        "index": item.index,
        "upload_date": parse_upload_date(info.get("upload_date") or info.get("timestamp")),
        "id": str(info.get("id") or item.id),
        "title": str(info.get("title") or collector.get("source_title") or item.title),
        "url": str(info.get("webpage_url") or item.url),
        "duration": duration_to_text(info),
        "view_count": info.get("view_count", ""),
        "like_count": info.get("like_count", ""),
        "comment_count": info.get("comment_count", ""),
        "uploader": info.get("uploader", ""),
        "uploader_id": info.get("uploader_id", ""),
        "tags": tag_text,
        "subtitle_languages": subtitle_languages(info),
    }


def write_exports(rows: list[dict[str, Any]], output_dir: Path, prefix: str) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / f"{prefix}.csv"
    jsonl_path = output_dir / f"{prefix}.jsonl"
    md_path = output_dir / f"{prefix}.md"

    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=EXPORT_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in EXPORT_FIELDS})

    with jsonl_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False))
            handle.write("\n")

    with md_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(f"# {prefix}\n\n")
        handle.write(f"- Exported rows: {len(rows)}\n")
        handle.write(f"- Generated at: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}\n\n")
        handle.write("| # | Date | Title | URL | Duration | Views | Subs |\n")
        handle.write("|---:|---|---|---|---:|---:|---|\n")
        for row in rows:
            title = str(row.get("title") or "").replace("|", "\\|")
            handle.write(
                f"| {row.get('index', '')} | {row.get('upload_date', '')} | "
                f"{title} | {row.get('url', '')} | {row.get('duration', '')} | "
                f"{row.get('view_count', '')} | {row.get('subtitle_languages', '')} |\n"
            )
    return {"csv": csv_path, "jsonl": jsonl_path, "markdown": md_path}


def load_success_rows(items: list[VideoItem], cache_dir: Path) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    corrupt_count = 0
    for item in items:
        info_path = cache_dir / f"{item.id}.info.json"
        if not info_path.exists():
            continue
        info = read_json(info_path)
        if info is None:
            corrupt_count += 1
            continue
        rows.append(compact_row(item, info))
    rows.sort(key=lambda row: int(row.get("index") or 0))
    return rows, corrupt_count


def write_state(
    items: list[VideoItem],
    cache_dir: Path,
    state_dir: Path,
    summary: dict[str, Any],
) -> dict[str, Path]:
    state_dir.mkdir(parents=True, exist_ok=True)
    progress_path = state_dir / "progress.csv"
    failed_path = state_dir / "failed.csv"
    missing_path = state_dir / "missing.csv"
    summary_path = state_dir / "run_summary.json"

    rows: list[dict[str, Any]] = []
    failed_rows: list[dict[str, Any]] = []
    missing_rows: list[dict[str, Any]] = []
    for item in items:
        info_path = cache_dir / f"{item.id}.info.json"
        error_path = cache_dir / f"{item.id}.error.json"
        error = read_json(error_path) if error_path.exists() else {}
        if info_path.exists():
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
            "error_type": (error or {}).get("error_type", ""),
            "returncode": (error or {}).get("returncode", ""),
        }
        rows.append(row)
        if status == "failed":
            failed_rows.append(row)
        if status != "success":
            missing_rows.append(row)

    fields = ["index", "id", "title", "url", "status", "error_type", "returncode"]
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
    cache_dir = resolve_path(args.cache_dir, base_dir / "metadata")
    output_dir = resolve_path(args.output_dir, base_dir / "manifests")
    state_dir = resolve_path(args.state_dir, base_dir / "runs" / run_stamp)
    output_prefix = args.output_prefix or f"{args.channel_slug}_videos_detailed_{args.date_stamp}"
    items = load_manifest(input_path)
    if args.limit:
        items = items[: args.limit]

    if args.dry_run:
        print("Dry run only; no files will be written.")
        print(f"Input: {input_path}")
        print(f"Items: {len(items)}")
        print(f"Cache dir: {cache_dir}")
        print(f"Output dir: {output_dir}")
        print(f"State dir: {state_dir}")
        print(f"Output prefix: {output_prefix}")
        return 0

    yt_dlp: Path | None = None
    if not args.export_only:
        yt_dlp = find_yt_dlp(args.yt_dlp)
        print(f"Using yt-dlp: {yt_dlp}")

    cache_dir.mkdir(parents=True, exist_ok=True)
    state_dir.mkdir(parents=True, exist_ok=True)

    processed = skipped = failed = 0
    if args.export_only:
        print("Export-only mode; skipping fetch loop.")
    else:
        assert yt_dlp is not None
        for position, item in enumerate(items, start=1):
            info_path = cache_dir / f"{item.id}.info.json"
            error_path = cache_dir / f"{item.id}.error.json"
            if info_path.exists() and not args.force:
                skipped += 1
                print(f"[{position}/{len(items)}] skip existing {item.id}")
                continue
            print(f"[{position}/{len(items)}] fetch {item.id} {item.title or item.url}")
            info, error = fetch_one(
                yt_dlp=yt_dlp,
                item=item,
                retries=args.retries,
                extractor_retries=args.extractor_retries,
                socket_timeout=args.socket_timeout,
                item_timeout=args.item_timeout,
            )
            if info is not None:
                atomic_write_json(info_path, info)
                if error_path.exists():
                    error_path.unlink()
                processed += 1
            else:
                assert error is not None
                atomic_write_json(error_path, error)
                eprint(f"  failed {item.id}: {error.get('error_type')}")
                failed += 1
            if args.sleep > 0 and position < len(items):
                time.sleep(args.sleep)

    rows, corrupt_count = load_success_rows(items, cache_dir)
    exports = write_exports(rows, output_dir, output_prefix)
    missing_count = max(len(items) - len(rows), 0)
    summary = {
        "input": str(input_path),
        "channel_slug": args.channel_slug,
        "total_items": len(items),
        "success_checkpoints": len(rows),
        "missing_or_failed": missing_count,
        "corrupt_checkpoints": corrupt_count,
        "processed_this_run": processed,
        "skipped_this_run": skipped,
        "failed_this_run": failed,
        "exported_rows": len(rows),
        "cache_dir": str(cache_dir),
        "output_dir": str(output_dir),
        "state_dir": str(state_dir),
        "outputs": {key: str(path) for key, path in exports.items()},
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    state_files = write_state(items, cache_dir, state_dir, summary)

    print("")
    print("Done.")
    print(f"  total items:          {len(items)}")
    print(f"  success checkpoints: {len(rows)}")
    print(f"  missing or failed:   {missing_count}")
    print(f"  exported rows:       {len(rows)}")
    print(f"  CSV:                 {exports['csv']}")
    print(f"  JSONL:               {exports['jsonl']}")
    print(f"  Markdown:            {exports['markdown']}")
    print(f"  Missing report:      {state_files['missing']}")
    print(f"  Failed report:       {state_files['failed']}")
    return 0 if missing_count == 0 and corrupt_count == 0 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        eprint("Interrupted.")
        raise SystemExit(130)
