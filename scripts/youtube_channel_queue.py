#!/usr/bin/env python3
"""
Resume-safe YouTube channel metadata collector.

The script consumes a frozen flat channel manifest, fetches each video one at a
time with yt-dlp, stores one checkpoint JSON per video id, and exports CSV,
JSONL, and Markdown manifests from the successful checkpoints.
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
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
MOJIBAKE_MARKERS = ("Ã", "Â", "â", "ç", "è", "æ", "å", "é", "ï¼")
EXPORT_FIELDS = ["index", "upload_date", "id", "title", "url", "duration", "view_count"]


@dataclass(frozen=True)
class VideoItem:
    index: int
    id: str
    title: str
    url: str
    duration: str = ""
    view_count: str = ""


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch YouTube video metadata from a flat channel manifest with "
            "checkpointing, retries, and final missing/failed reports."
        )
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Flat manifest CSV or JSONL containing at least id/url/title columns.",
    )
    parser.add_argument(
        "--channel-slug",
        help="Stable folder/output prefix slug. Defaults to deriving it from --input.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        help="Directory for per-video <id>.info.json checkpoints.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory for exported CSV/JSONL/Markdown manifests.",
    )
    parser.add_argument(
        "--state-dir",
        type=Path,
        help="Directory for this run's progress, failed, missing, and summary files.",
    )
    parser.add_argument(
        "--output-prefix",
        help="Output manifest basename without extension.",
    )
    parser.add_argument(
        "--date-stamp",
        default=dt.date.today().isoformat(),
        help="Date stamp used in default output names. Default: today.",
    )
    parser.add_argument(
        "--start-date",
        help="Optional inclusive upload-date filter, YYYY-MM-DD.",
    )
    parser.add_argument(
        "--end-date",
        help="Optional inclusive upload-date filter, YYYY-MM-DD.",
    )
    parser.add_argument(
        "--yt-dlp",
        type=Path,
        help="Path to yt-dlp. Defaults to .venv/Scripts/yt-dlp.exe, then PATH.",
    )
    parser.add_argument("--retries", type=int, default=10, help="yt-dlp network retries.")
    parser.add_argument(
        "--extractor-retries",
        type=int,
        default=10,
        help="yt-dlp extractor retries.",
    )
    parser.add_argument(
        "--socket-timeout",
        type=int,
        default=30,
        help="yt-dlp socket timeout in seconds.",
    )
    parser.add_argument(
        "--item-timeout",
        type=int,
        default=240,
        help="Hard timeout for one video metadata fetch in seconds.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.5,
        help="Seconds to sleep between successful/failed item attempts.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only process the first N videos from the manifest. Useful for smoke tests.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch videos even when a checkpoint already exists.",
    )
    parser.add_argument(
        "--export-only",
        action="store_true",
        help="Do not call yt-dlp; only export from existing checkpoints.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate paths and show the plan without fetching or writing files.",
    )
    parser.add_argument(
        "--skip-known-failures",
        action="store_true",
        help="Skip videos that already have an <id>.error.json file.",
    )
    return parser.parse_args()


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

    match = re.search(r"/(?:embed|shorts|live)/([A-Za-z0-9_-]{11})", value)
    if match:
        return match.group(1)

    raise ValueError(f"Could not parse a YouTube video id from: {value}")


def cjk_count(value: str) -> int:
    return sum(1 for ch in value if "\u4e00" <= ch <= "\u9fff")


def mojibake_score(value: str) -> int:
    return sum(value.count(marker) for marker in MOJIBAKE_MARKERS)


def repair_mojibake(value: str) -> str:
    """Repair common UTF-8-as-latin1/cp1252 mojibake from yt-dlp output."""
    if not value or not any(marker in value for marker in MOJIBAKE_MARKERS):
        return value

    candidates = []
    for encoding in ("latin-1", "cp1252"):
        try:
            candidates.append(value.encode(encoding).decode("utf-8"))
        except UnicodeError:
            continue

    best = value
    for candidate in candidates:
        if cjk_count(candidate) > cjk_count(best):
            best = candidate
        elif (
            cjk_count(candidate) == cjk_count(best)
            and mojibake_score(candidate) < mojibake_score(best)
        ):
            best = candidate
    return best


def best_title(*values: Any) -> str:
    best = ""
    for value in values:
        candidate = repair_mojibake(str(value or "").strip())
        if not candidate:
            continue
        if not best:
            best = candidate
            continue
        if mojibake_score(candidate) < mojibake_score(best):
            best = candidate
        elif (
            mojibake_score(candidate) == mojibake_score(best)
            and cjk_count(candidate) > cjk_count(best)
        ):
            best = candidate
    return best


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"_videos(?:_flat|_detailed)?(?:_\d{4}-\d{2}-\d{2})?$", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "channel"


def default_channel_slug(input_path: Path) -> str:
    return slugify(input_path.stem)


def resolve_path(path: Path | None, default: Path) -> Path:
    chosen = path if path is not None else default
    if chosen.is_absolute():
        return chosen
    return (ROOT / chosen).resolve()


def load_manifest(path: Path) -> list[VideoItem]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        rows = load_csv_manifest(path)
    elif suffix in {".jsonl", ".ndjson"}:
        rows = load_jsonl_manifest(path)
    else:
        raise ValueError(f"Unsupported manifest extension: {path.suffix}")

    items: list[VideoItem] = []
    seen: set[str] = set()
    for fallback_index, row in enumerate(rows, start=1):
        raw_id = str(row.get("id") or "").strip()
        raw_url = str(row.get("url") or row.get("webpage_url") or "").strip()
        video_id = raw_id if VIDEO_ID_RE.fullmatch(raw_id) else parse_video_id(raw_url)
        if video_id in seen:
            continue

        raw_index = str(row.get("index") or "").strip()
        try:
            index = int(raw_index)
        except ValueError:
            index = fallback_index

        title = repair_mojibake(str(row.get("title") or "").strip())
        url = raw_url or canonical_url(video_id)
        items.append(
            VideoItem(
                index=index,
                id=video_id,
                title=title,
                url=url,
                duration=str(row.get("duration") or "").strip(),
                view_count=str(row.get("view_count") or "").strip(),
            )
        )
        seen.add(video_id)
    return items


def load_csv_manifest(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_jsonl_manifest(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return rows


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

    raise FileNotFoundError(
        "Could not find yt-dlp. Install it in .venv or pass --yt-dlp."
    )


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
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        first = stdout.find("{")
        last = stdout.rfind("}")
        if first == -1 or last == -1 or last <= first:
            raise
        return json.loads(stdout[first : last + 1])


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
        return None, {
            "id": item.id,
            "url": item.url,
            "title": item.title,
            "started_at": started_at.isoformat(),
            "finished_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "error_type": "timeout",
            "returncode": None,
            "stderr": str(exc),
        }

    finished_at = dt.datetime.now(dt.timezone.utc)
    if proc.returncode != 0:
        return None, {
            "id": item.id,
            "url": item.url,
            "title": item.title,
            "started_at": started_at.isoformat(),
            "finished_at": finished_at.isoformat(),
            "error_type": "yt-dlp",
            "returncode": proc.returncode,
            "stderr": proc.stderr[-4000:],
            "stdout": proc.stdout[-1000:],
        }

    try:
        info = parse_yt_dlp_json(proc.stdout)
    except json.JSONDecodeError as exc:
        return None, {
            "id": item.id,
            "url": item.url,
            "title": item.title,
            "started_at": started_at.isoformat(),
            "finished_at": finished_at.isoformat(),
            "error_type": "json",
            "returncode": proc.returncode,
            "stderr": proc.stderr[-4000:],
            "stdout": proc.stdout[-4000:],
            "message": str(exc),
        }

    info["_collector"] = {
        "fetched_at": finished_at.isoformat(),
        "source_url": item.url,
        "source_index": item.index,
        "source_title": item.title,
    }
    return info, None


def parse_upload_date(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if not text:
        return ""
    if re.fullmatch(r"\d{8}", text):
        return f"{text[0:4]}-{text[4:6]}-{text[6:8]}"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return text
    return ""


def duration_to_text(info: dict[str, Any], fallback: str = "") -> str:
    duration_string = info.get("duration_string")
    if duration_string:
        return str(duration_string)

    duration = info.get("duration")
    if isinstance(duration, (int, float)) and duration >= 0:
        total = int(duration)
        hours, rem = divmod(total, 3600)
        minutes, seconds = divmod(rem, 60)
        if hours:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"

    return fallback


def compact_row(item: VideoItem, info: dict[str, Any] | None) -> dict[str, Any]:
    info = info or {}
    collector = info.get("_collector") or {}
    title = best_title(info.get("title"), collector.get("source_title"), item.title)
    url = str(info.get("webpage_url") or info.get("original_url") or item.url)
    return {
        "index": item.index,
        "upload_date": parse_upload_date(info.get("upload_date")),
        "id": str(info.get("id") or item.id),
        "title": title,
        "url": url or canonical_url(item.id),
        "duration": duration_to_text(info, item.duration),
        "view_count": info.get("view_count", item.view_count),
    }


def parse_date_filter(value: str | None, name: str) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be YYYY-MM-DD, got: {value}") from exc


def include_row(row: dict[str, Any], start: dt.date | None, end: dt.date | None) -> bool:
    upload_date = row.get("upload_date") or ""
    if not upload_date:
        return start is None and end is None

    try:
        parsed = dt.date.fromisoformat(str(upload_date))
    except ValueError:
        return start is None and end is None

    if start is not None and parsed < start:
        return False
    if end is not None and parsed > end:
        return False
    return True


def default_output_prefix(
    channel_slug: str,
    start: dt.date | None,
    end: dt.date | None,
    date_stamp: str,
) -> str:
    if start or end:
        start_year = str(start.year) if start else "beginning"
        end_year = str(end.year) if end else "latest"
        return f"{channel_slug}_videos_{start_year}_to_{end_year}_{date_stamp}"
    return f"{channel_slug}_videos_detailed_{date_stamp}"


def write_exports(rows: list[dict[str, Any]], output_dir: Path, prefix: str) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / f"{prefix}.csv"
    jsonl_path = output_dir / f"{prefix}.jsonl"
    md_path = output_dir / f"{prefix}.md"

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=EXPORT_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in EXPORT_FIELDS})

    with jsonl_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=False))
            handle.write("\n")

    with md_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(f"# {prefix}\n\n")
        handle.write(f"- Exported rows: {len(rows)}\n")
        handle.write(f"- Generated at: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}\n\n")
        handle.write("| # | Upload date | Title | URL | Duration | Views |\n")
        handle.write("|---:|---|---|---|---:|---:|\n")
        for row in rows:
            title = str(row.get("title") or "").replace("|", "\\|")
            url = str(row.get("url") or "")
            handle.write(
                f"| {row.get('index', '')} | {row.get('upload_date', '')} | "
                f"{title} | {url} | {row.get('duration', '')} | {row.get('view_count', '')} |\n"
            )

    return {"csv": csv_path, "jsonl": jsonl_path, "markdown": md_path}


def write_state_files(
    items: list[VideoItem],
    cache_dir: Path,
    state_dir: Path,
    run_failures: list[dict[str, Any]],
    summary: dict[str, Any],
) -> dict[str, Path]:
    state_dir.mkdir(parents=True, exist_ok=True)
    progress_path = state_dir / "progress.csv"
    failed_path = state_dir / "failed.csv"
    missing_path = state_dir / "missing.csv"
    summary_path = state_dir / "run_summary.json"

    error_by_id = {
        path.stem.replace(".error", ""): read_json(path)
        for path in cache_dir.glob("*.error.json")
    }

    progress_rows: list[dict[str, Any]] = []
    failed_rows: list[dict[str, Any]] = []
    missing_rows: list[dict[str, Any]] = []

    for item in items:
        info_path = cache_dir / f"{item.id}.info.json"
        error = error_by_id.get(item.id)
        if info_path.exists():
            status = "success"
        elif error:
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
        progress_rows.append(row)
        if status == "failed":
            failed_rows.append(row)
        if status != "success":
            missing_rows.append(row)

    with progress_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["index", "id", "title", "url", "status", "error_type", "returncode"],
        )
        writer.writeheader()
        writer.writerows(progress_rows)

    with failed_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["index", "id", "title", "url", "status", "error_type", "returncode"],
        )
        writer.writeheader()
        writer.writerows(failed_rows)

    with missing_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["index", "id", "title", "url", "status", "error_type", "returncode"],
        )
        writer.writeheader()
        writer.writerows(missing_rows)

    summary = dict(summary)
    summary["run_failures"] = len(run_failures)
    atomic_write_json(summary_path, summary)
    return {
        "progress": progress_path,
        "failed": failed_path,
        "missing": missing_path,
        "summary": summary_path,
    }


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


def main() -> int:
    args = parse_args()
    input_path = args.input if args.input.is_absolute() else (ROOT / args.input).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Input manifest does not exist: {input_path}")

    channel_slug = args.channel_slug or default_channel_slug(input_path)
    base_dir = ROOT / "sources" / "channels" / channel_slug
    run_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    cache_dir = resolve_path(args.cache_dir, base_dir / "metadata")
    output_dir = resolve_path(args.output_dir, base_dir / "manifests")
    state_dir = resolve_path(args.state_dir, base_dir / "runs" / run_stamp)
    start_date = parse_date_filter(args.start_date, "--start-date")
    end_date = parse_date_filter(args.end_date, "--end-date")
    output_prefix = args.output_prefix or default_output_prefix(
        channel_slug,
        start_date,
        end_date,
        args.date_stamp,
    )

    items = load_manifest(input_path)
    if args.limit:
        items = items[: args.limit]

    if args.dry_run:
        print("Dry run only; no files will be written.")
        print(f"Input: {input_path}")
        print(f"Items: {len(items)}")
        print(f"Channel slug: {channel_slug}")
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
    run_failures: list[dict[str, Any]] = []

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

            if error_path.exists() and args.skip_known_failures and not args.force:
                skipped += 1
                print(f"[{position}/{len(items)}] skip known failure {item.id}")
                continue

            print(f"[{position}/{len(items)}] fetch {item.id} {item.title}")
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
                run_failures.append(error)
                failed += 1
                eprint(f"  failed {item.id}: {error.get('error_type')}")

            if args.sleep > 0 and position < len(items):
                time.sleep(args.sleep)

    success_rows, corrupt_count = load_success_rows(items, cache_dir)
    filtered_rows = [
        row for row in success_rows if include_row(row, start=start_date, end=end_date)
    ]
    exports = write_exports(filtered_rows, output_dir, output_prefix)

    success_count = len(success_rows)
    missing_count = max(len(items) - success_count, 0)
    summary = {
        "input": str(input_path),
        "channel_slug": channel_slug,
        "total_items": len(items),
        "success_checkpoints": success_count,
        "missing_or_failed": missing_count,
        "corrupt_checkpoints": corrupt_count,
        "processed_this_run": processed,
        "skipped_this_run": skipped,
        "failed_this_run": failed,
        "exported_rows": len(filtered_rows),
        "start_date": args.start_date or "",
        "end_date": args.end_date or "",
        "cache_dir": str(cache_dir),
        "output_dir": str(output_dir),
        "state_dir": str(state_dir),
        "outputs": {key: str(path) for key, path in exports.items()},
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    state_files = write_state_files(items, cache_dir, state_dir, run_failures, summary)

    print("")
    print("Done.")
    print(f"  total items:          {len(items)}")
    print(f"  success checkpoints: {success_count}")
    print(f"  missing or failed:   {missing_count}")
    print(f"  exported rows:       {len(filtered_rows)}")
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
