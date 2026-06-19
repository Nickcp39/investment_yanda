#!/usr/bin/env python
"""Collect public TradesMax articles for research archiving.

This script only reads publicly accessible pages from tradesmax.com. It uses the
homepage/category pages as indexes, fetches article pages, and stores a small
manifest plus Markdown snapshots for later research review.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.tradesmax.com/"
DEFAULT_CATEGORY_URLS = [
    urljoin(BASE_URL, "component/k2/itemlist/category/40"),
    urljoin(BASE_URL, "component/k2/itemlist/category/45"),
    urljoin(BASE_URL, "component/k2/itemlist/category/44"),
    urljoin(BASE_URL, "component/k2/itemlist/category/39"),
]
DEFAULT_OUTPUT_DIR = Path("sources/news/tradesmax")


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


@dataclass(frozen=True)
class ArticleLink:
    title: str
    url: str
    source_index_url: str


@dataclass(frozen=True)
class Article:
    title: str
    url: str
    author: str
    published_date: str
    description: str
    keywords: str
    text: str
    source_index_url: str
    fetched_at: str


def fetch_html(session: requests.Session, url: str, timeout: int) -> str:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    if "text/html" not in response.headers.get("content-type", ""):
        raise ValueError(f"Expected HTML from {url}, got {response.headers.get('content-type')}")
    response.encoding = response.encoding or "utf-8"
    return response.text


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def is_tradesmax_article_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.netloc in {"www.tradesmax.com", "tradesmax.com"} and "/component/k2/item/" in parsed.path


def collect_article_links(html: str, index_url: str) -> list[ArticleLink]:
    soup = BeautifulSoup(html, "lxml")
    links: list[ArticleLink] = []
    seen: set[str] = set()

    for anchor in soup.select("a[href]"):
        url = urljoin(index_url, anchor.get("href", ""))
        title = title_for_anchor(anchor)
        if not title or not is_tradesmax_article_url(url) or url in seen:
            continue
        seen.add(url)
        links.append(ArticleLink(title=title, url=url, source_index_url=index_url))

    return links


def title_for_anchor(anchor) -> str:
    title = normalize_space(anchor.get_text(" ", strip=True))
    if title and title != "阅读更多...":
        return title

    container = anchor.find_parent(class_=re.compile(r"catItemView|itemView"))
    if not container:
        return ""

    text = normalize_space(container.get_text(" ", strip=True))
    for marker in [" 作者 ", "作者 ", " | "]:
        if marker in text:
            text = text.split(marker, 1)[0]
            break
    return text.replace("订阅此RSS源", "").strip()


def text_or_empty(soup: BeautifulSoup, selector: str) -> str:
    node = soup.select_one(selector)
    return normalize_space(node.get_text(" ", strip=True)) if node else ""


def meta_content(soup: BeautifulSoup, name: str) -> str:
    node = soup.select_one(f'meta[name="{name}"]')
    return normalize_space(node.get("content", "")) if node else ""


def parse_article(html: str, link: ArticleLink) -> Article:
    soup = BeautifulSoup(html, "lxml")

    title = text_or_empty(soup, "h2.itemTitle") or meta_content(soup, "title")
    if not title and soup.title:
        title = normalize_space(soup.title.get_text(" ", strip=True).replace(" - 美股投资网", ""))

    text = text_or_empty(soup, "div.itemFullText") or text_or_empty(soup, "div.itemIntroText")
    if not text:
        raise ValueError(f"No article body found for {link.url}")

    date = (
        text_or_empty(soup, "span.itemDateCreated")
        or text_or_empty(soup, ".itemDateCreated")
        or infer_date_from_text(soup.get_text(" ", strip=True))
    )

    return Article(
        title=title or link.title,
        url=link.url,
        author=meta_content(soup, "author"),
        published_date=date,
        description=meta_content(soup, "description"),
        keywords=meta_content(soup, "keywords"),
        text=text,
        source_index_url=link.source_index_url,
        fetched_at=datetime.now(timezone.utc).isoformat(),
    )


def infer_date_from_text(text: str) -> str:
    match = re.search(r"20\d{2}-\d{2}-\d{2}", text)
    return match.group(0) if match else ""


def slug_for_article(article: Article) -> str:
    parsed = urlparse(article.url)
    tail = parsed.path.rstrip("/").split("/")[-1]
    article_id = parsed.path.rstrip("/").split("/")[-2] if tail and not tail[:1].isdigit() else tail
    digest = hashlib.sha1(article.url.encode("utf-8")).hexdigest()[:8]
    safe_title = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", article.title, flags=re.UNICODE).strip("-")
    safe_title = safe_title[:80] or "article"
    if article_id and article_id.isdigit():
        return f"{article_id}-{safe_title}-{digest}"
    id_match = re.search(r"/item/(\d+)-", parsed.path)
    prefix = f"{id_match.group(1)}-" if id_match else ""
    return f"{prefix}{safe_title}-{digest}"


def article_to_markdown(article: Article) -> str:
    metadata = [
        "---",
        f'title: "{article.title.replace(chr(34), chr(39))}"',
        f"url: {article.url}",
        f"published_date: {article.published_date}",
        f"author: {article.author}",
        f"source_index_url: {article.source_index_url}",
        f"fetched_at: {article.fetched_at}",
        "---",
        "",
        f"# {article.title}",
        "",
        f"Source: {article.url}",
        "",
    ]
    if article.description and article.description != article.title:
        metadata.extend([f"> {article.description}", ""])
    metadata.extend([article.text, ""])
    return "\n".join(metadata)


def iter_limited(items: Iterable[ArticleLink], limit: int | None) -> Iterable[ArticleLink]:
    count = 0
    for item in items:
        if limit is not None and count >= limit:
            return
        yield item
        count += 1


def write_outputs(articles: list[Article], output_dir: Path) -> None:
    articles_dir = output_dir / "articles"
    output_dir.mkdir(parents=True, exist_ok=True)
    articles_dir.mkdir(parents=True, exist_ok=True)

    manifest_jsonl = output_dir / "manifest.jsonl"
    manifest_csv = output_dir / "manifest.csv"

    with manifest_jsonl.open("w", encoding="utf-8") as jsonl_file:
        for article in articles:
            row = {
                "title": article.title,
                "url": article.url,
                "author": article.author,
                "published_date": article.published_date,
                "description": article.description,
                "keywords": article.keywords,
                "source_index_url": article.source_index_url,
                "fetched_at": article.fetched_at,
                "text_length": len(article.text),
            }
            jsonl_file.write(json.dumps(row, ensure_ascii=False) + "\n")

    with manifest_csv.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "title",
                "url",
                "author",
                "published_date",
                "description",
                "keywords",
                "source_index_url",
                "fetched_at",
                "text_length",
                "markdown_path",
            ],
        )
        writer.writeheader()
        for article in articles:
            slug = slug_for_article(article)
            markdown_path = articles_dir / f"{slug}.md"
            markdown_path.write_text(article_to_markdown(article), encoding="utf-8")
            writer.writerow(
                {
                    "title": article.title,
                    "url": article.url,
                    "author": article.author,
                    "published_date": article.published_date,
                    "description": article.description,
                    "keywords": article.keywords,
                    "source_index_url": article.source_index_url,
                    "fetched_at": article.fetched_at,
                    "text_length": len(article.text),
                    "markdown_path": markdown_path.as_posix(),
                }
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect public TradesMax articles.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum article pages to fetch.")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests in seconds.")
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of category pages to scan when using the default index set.",
    )
    parser.add_argument("--page-size", type=int, default=10, help="K2 category page size for start offsets.")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for manifest files and Markdown snapshots.",
    )
    parser.add_argument(
        "--index-url",
        action="append",
        default=[],
        help="Index page to scan. Can be repeated. Defaults to homepage plus public category pages.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Only list discovered article links.")
    return parser.parse_args()


def build_default_index_urls(pages: int, page_size: int) -> list[str]:
    urls = [BASE_URL]
    for category_url in DEFAULT_CATEGORY_URLS:
        for page_number in range(max(1, pages)):
            start = page_number * page_size
            urls.append(f"{category_url}?start={start}")
    return urls


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    args = parse_args()
    index_urls = args.index_url or build_default_index_urls(args.pages, args.page_size)
    session = requests.Session()
    session.headers.update(HEADERS)

    discovered: dict[str, ArticleLink] = {}
    for index_url in index_urls:
        print(f"Scanning index: {index_url}", file=sys.stderr)
        html = fetch_html(session, index_url, args.timeout)
        for link in collect_article_links(html, index_url):
            discovered.setdefault(link.url, link)
        time.sleep(args.delay)

    links = list(discovered.values())
    print(f"Discovered {len(links)} unique article links.", file=sys.stderr)

    if args.dry_run:
        for link in iter_limited(links, args.limit):
            print(f"{link.title}\t{link.url}")
        return 0

    articles: list[Article] = []
    for link in iter_limited(links, args.limit):
        print(f"Fetching article: {link.title}", file=sys.stderr)
        html = fetch_html(session, link.url, args.timeout)
        articles.append(parse_article(html, link))
        time.sleep(args.delay)

    write_outputs(articles, args.output_dir)
    print(f"Wrote {len(articles)} articles to {args.output_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
