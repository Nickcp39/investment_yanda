#!/usr/bin/env python
"""Collect WeChat MP article URLs copied from the local WeChat client.

The script does not use WeChat passwords, cookies, or tokens. It watches the
Windows clipboard for public mp.weixin.qq.com article URLs, fetches each article
page, and stores a manifest plus Markdown snapshot for research use.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

import requests
from bs4 import BeautifulSoup

try:
    import win32clipboard
except Exception:  # pragma: no cover - non-Windows fallback.
    win32clipboard = None


DEFAULT_OUTPUT_DIR = Path("sources/news/wechat_mp")
SAFE_LONG_PARAMS = ("__biz", "mid", "idx", "sn")
SHORT_ARTICLE_RE = re.compile(r"https?://mp\.weixin\.qq\.com/s/([A-Za-z0-9_-]{22})")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


@dataclass(frozen=True)
class WechatArticle:
    title: str
    account_name: str
    url: str
    biz: str
    publish_time: str
    author: str
    description: str
    text: str
    fetched_at: str


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def get_clipboard_text() -> str:
    if win32clipboard is None:
        raise RuntimeError("win32clipboard is unavailable. Install pywin32 on Windows.")

    win32clipboard.OpenClipboard()
    try:
        if not win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
            return ""
        return win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT) or ""
    finally:
        win32clipboard.CloseClipboard()


def canonicalize_wechat_url(raw: str) -> str | None:
    """Return a public, session-free WeChat article URL."""
    cleaned = html.unescape(raw).strip().rstrip(").,;，。；、")

    short_match = SHORT_ARTICLE_RE.search(cleaned)
    if short_match:
        return f"https://mp.weixin.qq.com/s/{short_match.group(1)}"

    parsed = urlparse(cleaned)
    if parsed.netloc != "mp.weixin.qq.com" or parsed.path != "/s":
        return None

    query = parse_qs(parsed.query)
    if not all(query.get(key) for key in SAFE_LONG_PARAMS):
        return None

    safe_query = urlencode([(key, query[key][0]) for key in SAFE_LONG_PARAMS])
    return f"https://mp.weixin.qq.com/s?{safe_query}#rd"


def extract_wechat_urls(text: str) -> list[str]:
    candidates = re.findall(r"https?://mp\.weixin\.qq\.com/[^\s\"'<>]+", text)
    urls: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        cleaned = canonicalize_wechat_url(candidate)
        if not cleaned:
            continue
        if cleaned not in seen:
            urls.append(cleaned)
            seen.add(cleaned)
    return urls


def regex_value(pattern: str, text: str) -> str:
    match = re.search(pattern, text)
    return normalize_space(match.group(1)) if match else ""


def meta_content(soup: BeautifulSoup, prop: str) -> str:
    node = soup.select_one(f'meta[property="{prop}"], meta[name="{prop}"]')
    return normalize_space(node.get("content", "")) if node else ""


def timestamp_to_local(value: str) -> str:
    if not value or not value.isdigit():
        return ""
    try:
        return datetime.fromtimestamp(int(value)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return ""


def parse_article(url: str, timeout: int = 20) -> WechatArticle:
    response = requests.get(url, headers=HEADERS, timeout=timeout)
    response.raise_for_status()
    response.encoding = response.encoding or "utf-8"
    html = response.text
    soup = BeautifulSoup(html, "lxml")

    title = normalize_space(soup.select_one("#activity-name").get_text(" ", strip=True)) if soup.select_one("#activity-name") else ""
    account = normalize_space(soup.select_one("#js_name").get_text(" ", strip=True)) if soup.select_one("#js_name") else ""
    publish_time = normalize_space(soup.select_one("#publish_time").get_text(" ", strip=True)) if soup.select_one("#publish_time") else ""
    text = normalize_space(soup.select_one("#js_content").get_text(" ", strip=True)) if soup.select_one("#js_content") else ""

    biz = regex_value(r'var\s+biz\s*=\s*"([^"]+)"', html)
    ct = regex_value(r'var\s+ct\s*=\s*"([^"]+)"', html)
    author = regex_value(r'var\s+author\s*=\s*"([^"]*)"', html)
    description = meta_content(soup, "og:description") or meta_content(soup, "description")

    if not publish_time:
        publish_time = timestamp_to_local(ct)
    if not title:
        title = meta_content(soup, "og:title") or (soup.title.get_text(" ", strip=True) if soup.title else "")
    if not account:
        account = regex_value(r'var\s+nickname\s*=\s*"([^"]+)"', html)

    if not title or not text:
        raise ValueError(f"Could not parse title/body from {url}")

    return WechatArticle(
        title=title,
        account_name=account,
        url=url,
        biz=biz or parse_qs(urlparse(url).query).get("__biz", [""])[0],
        publish_time=publish_time,
        author=author,
        description=description,
        text=text,
        fetched_at=datetime.now(timezone.utc).isoformat(),
    )


def slug_for(article: WechatArticle) -> str:
    digest = hashlib.sha1(article.url.encode("utf-8")).hexdigest()[:10]
    safe_title = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", article.title, flags=re.UNICODE).strip("-")
    return f"{safe_title[:90] or 'wechat-article'}-{digest}"


def article_to_markdown(article: WechatArticle) -> str:
    title = article.title.replace('"', "'")
    lines = [
        "---",
        f'title: "{title}"',
        f"account_name: {article.account_name}",
        f"url: {article.url}",
        f"biz: {article.biz}",
        f"publish_time: {article.publish_time}",
        f"author: {article.author}",
        f"fetched_at: {article.fetched_at}",
        "---",
        "",
        f"# {article.title}",
        "",
        f"Account: {article.account_name}",
        f"Source: {article.url}",
        "",
    ]
    if article.description and article.description != article.title:
        lines.extend([f"> {article.description}", ""])
    lines.extend([article.text, ""])
    return "\n".join(lines)


def load_seen(output_dir: Path) -> set[str]:
    path = output_dir / "manifest.jsonl"
    seen: set[str] = set()
    if not path.exists():
        return seen
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
            if row.get("url"):
                seen.add(row["url"])
        except json.JSONDecodeError:
            continue
    return seen


def save_article(article: WechatArticle, output_dir: Path) -> Path:
    articles_dir = output_dir / "articles"
    output_dir.mkdir(parents=True, exist_ok=True)
    articles_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = articles_dir / f"{slug_for(article)}.md"
    markdown_path.write_text(article_to_markdown(article), encoding="utf-8")

    row = asdict(article)
    row["text_length"] = len(article.text)
    row["markdown_path"] = markdown_path.as_posix()
    row.pop("text", None)

    with (output_dir / "manifest.jsonl").open("a", encoding="utf-8") as jsonl_file:
        jsonl_file.write(json.dumps(row, ensure_ascii=False) + "\n")

    csv_path = output_dir / "manifest.csv"
    write_header = not csv_path.exists()
    with csv_path.open("a", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(row.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(row)

    return markdown_path


def collect_url(url: str, output_dir: Path, timeout: int, seen: set[str]) -> bool:
    if url in seen:
        print(f"Already collected: {url}", file=sys.stderr)
        return False

    article = parse_article(url, timeout=timeout)
    path = save_article(article, output_dir)
    seen.add(url)
    print(f"Saved: {article.publish_time} | {article.account_name} | {article.title}", file=sys.stderr)
    print(f"  {path}", file=sys.stderr)
    return True


def watch_clipboard(output_dir: Path, poll: float, timeout: int) -> None:
    seen = load_seen(output_dir)
    last_text = ""
    print("Watching clipboard for mp.weixin.qq.com article URLs. Press Ctrl+C to stop.", file=sys.stderr)
    while True:
        try:
            text = get_clipboard_text()
            if text != last_text:
                last_text = text
                for url in extract_wechat_urls(text):
                    try:
                        collect_url(url, output_dir, timeout, seen)
                    except Exception as exc:
                        print(f"Failed: {url} | {exc}", file=sys.stderr)
            time.sleep(poll)
        except KeyboardInterrupt:
            print("Stopped.", file=sys.stderr)
            return


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect WeChat MP article links copied from WeChat.")
    parser.add_argument("--once", action="append", default=[], help="Parse one URL. Can be repeated.")
    parser.add_argument("--watch", action="store_true", help="Watch the Windows clipboard for copied article URLs.")
    parser.add_argument("--poll", type=float, default=1.0, help="Clipboard polling interval in seconds.")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory.")
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    args = parse_args()
    seen = load_seen(args.output_dir)
    for raw in args.once:
        urls = extract_wechat_urls(raw) or [raw]
        for url in urls:
            collect_url(url, args.output_dir, args.timeout, seen)

    if args.watch:
        watch_clipboard(args.output_dir, args.poll, args.timeout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
