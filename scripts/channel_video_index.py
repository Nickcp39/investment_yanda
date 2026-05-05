#!/usr/bin/env python3
"""
Index YouTube channel videos into CSV, JSONL, and Markdown files.

Use --detailed when upload dates are needed. Detailed mode is slower because
yt-dlp fetches individual video metadata, but it enables date filtering.
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
from pathlib import Path
from typing import Any


try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parents[1]


def slugify(text: str, fallback: str = "youtube_channel") -> str:
    text = text.lower()
    text = re.sub(r"https?://", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = text.strip("-")
    return text[:80].strip("-") or fallback


def find_ytdlp() -> str:
    ytdlp = shutil.which("yt-dlp")
    if ytdlp:
        return ytdlp
    local = Path(sys.executable).with_name("yt-dlp.exe")
    if local.exists():
        return str(local)
    raise RuntimeError("yt-dlp not found. Install it with: python -m pip install yt-dlp")


def run_ytdlp(channel_url: str, detailed: bool, timeout: int) -> list[dict[str, Any]]:
    cmd = [find_ytdlp(), "--ignore-errors", "--skip-download", "--dump-json", channel_url]
    if not detailed:
        cmd.insert(1, "--flat-playlist")

    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        timeout=timeout,
    )

    rows: list[dict[str, Any]] = []
    for line in proc.stdout.splitlines():
        if not line.strip() or not line.lstrip().startswith("{"):
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        video_id = data.get("id") or ""
        upload_date = data.get("upload_date") or ""
        upload_iso = (
            f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
            if len(upload_date) == 8
            else ""
        )
        rows.append(
            {
                "index": data.get("playlist_index"),
                "upload_date": upload_iso,
                "id": video_id,
                "title": data.get("title"),
                "url": data.get("webpage_url")
                or data.get("url")
                or ("https://www.youtube.com/watch?v=" + video_id),
                "duration": data.get("duration_string") or data.get("duration"),
                "view_count": data.get("view_count"),
            }
        )

    rows.sort(key=lambda row: row.get("index") or 999999)
    if proc.returncode != 0:
        print("warning: yt-dlp returned a non-zero status; partial results may be saved.", file=sys.stderr)
        if proc.stderr:
            print(proc.stderr[-1200:], file=sys.stderr)
    return rows


def filter_rows(rows: list[dict[str, Any]], date_after: str | None) -> list[dict[str, Any]]:
    if not date_after:
        return rows
    return [row for row in rows if row.get("upload_date") and row["upload_date"] >= date_after]


def write_outputs(
    rows: list[dict[str, Any]],
    out_dir: Path,
    base_name: str,
    channel_url: str,
    date_after: str | None,
) -> tuple[Path, Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_dir / f"{base_name}.jsonl"
    csv_path = out_dir / f"{base_name}.csv"
    md_path = out_dir / f"{base_name}.md"

    jsonl_path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["index", "upload_date", "id", "title", "url", "duration", "view_count"],
        )
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        f"# {base_name}",
        "",
        f"Retrieved: {dt.date.today().isoformat()}",
        f"Channel: {channel_url}",
        f"Date after: {date_after or ''}",
        f"Total: {len(rows)}",
        "",
        "| # | Date | Title | URL | Duration | Views |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        title = str(row.get("title") or "").replace("|", "/")
        lines.append(
            f"| {row.get('index') or ''} | {row.get('upload_date') or ''} | "
            f"{title} | {row.get('url') or ''} | {row.get('duration') or ''} | "
            f"{row.get('view_count') or ''} |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return jsonl_path, csv_path, md_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Index YouTube channel videos.")
    parser.add_argument("channel_url", help="YouTube channel videos URL")
    parser.add_argument("--detailed", action="store_true", help="Fetch full metadata including upload dates.")
    parser.add_argument("--date-after", help="Keep only videos uploaded on or after YYYY-MM-DD.")
    parser.add_argument("--name", help="Output base name.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "sources" / "channels",
        help="Output directory.",
    )
    parser.add_argument("--timeout", type=int, default=900, help="yt-dlp timeout in seconds.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    rows = run_ytdlp(args.channel_url, detailed=args.detailed, timeout=args.timeout)
    rows = filter_rows(rows, args.date_after)
    today = dt.date.today().isoformat()
    base = args.name or f"{slugify(args.channel_url)}_{today}"
    if args.date_after:
        base += f"_from_{args.date_after}"
    paths = write_outputs(rows, args.out_dir, base, args.channel_url, args.date_after)
    print(f"Rows: {len(rows)}")
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
