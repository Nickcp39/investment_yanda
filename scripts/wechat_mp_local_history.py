#!/usr/bin/env python
"""Collect WeChat MP articles from the local WeChat browser cache.

This reads local WeChat WebView cache/history files and extracts public
mp.weixin.qq.com article URLs. It never exports local session parameters such as
keys, pass_ticket, uin, or exportkey; URLs are canonicalized before use.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile

from wechat_mp_clipboard_collector import (
    DEFAULT_OUTPUT_DIR,
    WechatArticle,
    canonicalize_wechat_url,
    load_seen,
    parse_article,
    save_article,
)


DEFAULT_PROFILE_ROOT = (
    Path.home() / "AppData/Roaming/Tencent/WeChat/radium/web/profiles"
)
DEFAULT_ACCOUNT_NAME = "美股投资网"
DEFAULT_BIZ = "MjM5ODU5NjIzMg=="
CACHE_FILE_NAMES = {"History", "Share Data"}
SHORT_URL_RE = re.compile(r"https?://mp\.weixin\.qq\.com/s/[A-Za-z0-9_-]{22}")
LONG_URL_RE = re.compile(r"https?://mp\.weixin\.qq\.com/s\?[^\s\x00-\x1f\"'<>]+")


@dataclass(frozen=True)
class Candidate:
    url: str
    source: Path


def cache_files(profile_root: Path) -> list[Path]:
    if not profile_root.exists():
        return []
    files = [
        path
        for path in profile_root.rglob("*")
        if path.is_file() and path.name in CACHE_FILE_NAMES
    ]
    return sorted(files, key=lambda path: path.stat().st_mtime, reverse=True)


def extract_urls_from_file(path: Path) -> list[str]:
    try:
        text = path.read_bytes().decode("latin1", errors="ignore")
    except OSError as exc:
        print(f"Skip unreadable cache file: {path} | {exc}", file=sys.stderr)
        return []

    urls: list[str] = []
    seen: set[str] = set()
    for pattern in (SHORT_URL_RE, LONG_URL_RE):
        for match in pattern.finditer(text):
            raw = match.group(0)
            if len(raw) > 1000:
                continue
            url = canonicalize_wechat_url(raw)
            if url and url not in seen:
                seen.add(url)
                urls.append(url)
    return urls


def extract_urls_from_sqlite_history(path: Path) -> list[str]:
    if path.name != "History":
        return []

    tmp_name = ""
    try:
        with NamedTemporaryFile(prefix="wechat_history_", suffix=".sqlite", delete=False) as tmp:
            tmp_name = tmp.name
        shutil.copy2(path, tmp_name)
        connection = sqlite3.connect(tmp_name)
        try:
            rows = connection.execute(
                """
                select url
                from urls
                where url like 'http://mp.weixin.qq.com/%'
                   or url like 'https://mp.weixin.qq.com/%'
                order by last_visit_time desc
                """
            ).fetchall()
        finally:
            connection.close()
    except Exception as exc:
        print(f"Skip unreadable SQLite history: {path} | {exc}", file=sys.stderr)
        rows = []
    finally:
        if tmp_name:
            try:
                Path(tmp_name).unlink(missing_ok=True)
            except OSError:
                pass

    urls: list[str] = []
    seen: set[str] = set()
    for (raw,) in rows:
        url = canonicalize_wechat_url(raw)
        if url and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def discover_candidates(profile_root: Path) -> list[Candidate]:
    candidates: list[Candidate] = []
    seen: set[str] = set()
    for path in cache_files(profile_root):
        urls = extract_urls_from_sqlite_history(path) + extract_urls_from_file(path)
        for url in urls:
            if url in seen:
                continue
            seen.add(url)
            candidates.append(Candidate(url=url, source=path))
    return candidates


def is_target_article(article: WechatArticle, account_name: str, biz: str) -> bool:
    return article.account_name == account_name or bool(biz and article.biz == biz)


def parse_publish_time(value: str) -> datetime:
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y/%m/%d %H:%M:%S", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return datetime.min


def load_existing_manifest(output_dir: Path) -> dict[str, dict[str, str]]:
    path = output_dir / "manifest.jsonl"
    rows: dict[str, dict[str, str]] = {}
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        url = row.get("url")
        if url:
            rows[url] = row
    return rows


def print_recent(rows: list[dict[str, str]], limit: int) -> None:
    rows = sorted(rows, key=lambda row: parse_publish_time(row.get("publish_time", "")), reverse=True)
    if not rows:
        print("No target account articles found.", file=sys.stderr)
        return

    print(f"Recent {min(limit, len(rows))} target articles:", file=sys.stderr)
    for row in rows[:limit]:
        print(
            f"- {row.get('publish_time', '')} | {row.get('account_name', '')} | {row.get('title', '')}",
            file=sys.stderr,
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect WeChat MP articles from local WeChat cache/history.")
    parser.add_argument("--profile-root", type=Path, default=DEFAULT_PROFILE_ROOT, help="WeChat WebView profile root.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory.")
    parser.add_argument("--account-name", default=DEFAULT_ACCOUNT_NAME, help="Target account display name.")
    parser.add_argument("--biz", default=DEFAULT_BIZ, help="Target WeChat __biz id.")
    parser.add_argument("--limit", type=int, default=0, help="Stop after saving this many target articles. 0 means no limit.")
    parser.add_argument("--candidate-offset", type=int, default=0, help="Skip this many discovered candidate URLs before checking.")
    parser.add_argument("--max-candidates", type=int, default=0, help="Stop after checking this many candidate URLs. 0 means no limit.")
    parser.add_argument("--recent", type=int, default=5, help="Print this many recent target titles at the end.")
    parser.add_argument("--delay", type=float, default=0.8, help="Delay between article fetches in seconds.")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds.")
    parser.add_argument("--dry-run", action="store_true", help="Parse and filter, but do not write article files.")
    parser.add_argument("--force", action="store_true", help="Fetch/save URLs even if they are already in the manifest.")
    parser.add_argument("--show-candidates", action="store_true", help="Print discovered canonical candidate URLs.")
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    args = parse_args()
    candidates = discover_candidates(args.profile_root)
    print(f"Cache files: {len(cache_files(args.profile_root))}", file=sys.stderr)
    print(f"Canonical WeChat article candidates: {len(candidates)}", file=sys.stderr)
    if args.candidate_offset:
        print(f"Candidate offset: {args.candidate_offset}", file=sys.stderr)

    if args.show_candidates:
        for candidate in candidates:
            print(candidate.url)

    existing = load_existing_manifest(args.output_dir)
    seen = load_seen(args.output_dir)
    recent_rows: list[dict[str, str]] = [
        row
        for row in existing.values()
        if row.get("account_name") == args.account_name or (args.biz and row.get("biz") == args.biz)
    ]

    saved = 0
    checked = 0
    target_hits = 0
    failures = 0

    for candidate in candidates[args.candidate_offset :]:
        if args.max_candidates and checked >= args.max_candidates:
            break

        checked += 1
        if candidate.url in seen and not args.force:
            continue

        try:
            article = parse_article(candidate.url, timeout=args.timeout)
        except Exception as exc:
            failures += 1
            print(f"Failed: {candidate.url} | {exc}", file=sys.stderr)
            continue

        if not is_target_article(article, args.account_name, args.biz):
            print(f"Skip non-target: {article.account_name or article.biz or 'unknown'} | {article.title}", file=sys.stderr)
            time.sleep(args.delay)
            continue

        target_hits += 1
        row = {
            "title": article.title,
            "account_name": article.account_name,
            "url": article.url,
            "biz": article.biz,
            "publish_time": article.publish_time,
        }
        recent_rows.append(row)
        print(f"Target: {article.publish_time} | {article.account_name} | {article.title}", file=sys.stderr)

        if not args.dry_run:
            path = save_article(article, args.output_dir)
            seen.add(candidate.url)
            saved += 1
            print(f"  Saved: {path}", file=sys.stderr)

        if args.limit and target_hits >= args.limit:
            break

        time.sleep(args.delay)

    print(
        f"Checked {checked}; target hits {target_hits}; saved {saved}; failures {failures}.",
        file=sys.stderr,
    )
    print_recent(recent_rows, args.recent)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
