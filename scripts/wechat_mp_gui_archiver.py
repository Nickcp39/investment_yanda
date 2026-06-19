#!/usr/bin/env python
"""Drive the local WeChat official-account page and archive opened articles.

The workflow is intentionally conservative:

1. The user opens the target official-account profile in WeChat.
2. This script clicks visible article cards.
3. Newly opened public mp.weixin.qq.com URLs are read from local WeChat
   WebView history/cache.
4. Matching target-account articles are parsed and saved as Markdown.

It does not ask for or export WeChat cookies, tokens, passwords, or session
query parameters.
"""

from __future__ import annotations

import argparse
import ctypes
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import uiautomation as auto

from wechat_mp_clipboard_collector import DEFAULT_OUTPUT_DIR, load_seen, parse_article, save_article
from wechat_mp_local_history import (
    DEFAULT_BIZ,
    DEFAULT_PROFILE_ROOT,
    discover_candidates,
    is_target_article,
    load_existing_manifest,
    parse_publish_time,
)


DEFAULT_ACCOUNT_NAME = "美股投资网"
DEFAULT_CARD_Y_OFFSETS = (285, 525, 765)

HWND_TOPMOST = -1
HWND_NOTOPMOST = -2
SW_RESTORE = 9
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_SHOWWINDOW = 0x0040
MOUSEEVENTF_WHEEL = 0x0800
DWMWA_EXTENDED_FRAME_BOUNDS = 9


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


class User32:
    user32 = ctypes.windll.user32
    dwmapi = ctypes.windll.dwmapi

    @classmethod
    def set_topmost(cls, hwnd: int, enabled: bool) -> None:
        insert_after = HWND_TOPMOST if enabled else HWND_NOTOPMOST
        cls.user32.SetWindowPos(
            ctypes.c_void_p(hwnd),
            ctypes.c_void_p(insert_after),
            0,
            0,
            0,
            0,
            SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW,
        )

    @classmethod
    def restore(cls, hwnd: int) -> None:
        cls.user32.ShowWindow(ctypes.c_void_p(hwnd), SW_RESTORE)
        cls.user32.SetForegroundWindow(ctypes.c_void_p(hwnd))

    @classmethod
    def move_cursor(cls, x: int, y: int) -> None:
        cls.user32.SetCursorPos(x, y)

    @classmethod
    def wheel(cls, clicks: int) -> None:
        cls.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, clicks * 120, 0)

    @classmethod
    def screen_size(cls) -> tuple[int, int]:
        return cls.user32.GetSystemMetrics(0), cls.user32.GetSystemMetrics(1)

    @classmethod
    def hwnd_rect(cls, hwnd: int) -> tuple[int, int, int, int]:
        rect = RECT()
        try:
            cls.dwmapi.DwmGetWindowAttribute(
                ctypes.c_void_p(hwnd),
                DWMWA_EXTENDED_FRAME_BOUNDS,
                ctypes.byref(rect),
                ctypes.sizeof(rect),
            )
        except Exception:
            cls.user32.GetWindowRect(ctypes.c_void_p(hwnd), ctypes.byref(rect))
        return rect.left, rect.top, rect.right, rect.bottom


@dataclass(frozen=True)
class WindowRect:
    left: int
    top: int
    right: int
    bottom: int

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top


def find_profile_window() -> auto.Control:
    root = auto.GetRootControl()
    for child in root.GetChildren():
        if child.Name == "Official Accounts" or child.ClassName == "H5SubscriptionProfileWnd":
            return child
    raise RuntimeError("Could not find the WeChat 'Official Accounts' window.")


def window_rect(window: auto.Control) -> WindowRect:
    try:
        rect = window.BoundingRectangle
        return WindowRect(rect.left, rect.top, rect.right, rect.bottom)
    except Exception:
        hwnd = int(window.NativeWindowHandle or 0)
        if not hwnd:
            raise
        left, top, right, bottom = User32.hwnd_rect(hwnd)
        return WindowRect(left, top, right, bottom)


def parse_offsets(raw: str) -> tuple[int, ...]:
    offsets = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not offsets:
        raise argparse.ArgumentTypeError("At least one card y-offset is required.")
    return offsets


def target_rows(output_dir: Path, account_name: str, biz: str) -> list[dict[str, str]]:
    rows = [
        row
        for row in load_existing_manifest(output_dir).values()
        if row.get("account_name") == account_name or (biz and row.get("biz") == biz)
    ]
    return sorted(rows, key=lambda row: parse_publish_time(row.get("publish_time", "")), reverse=True)


def print_recent(output_dir: Path, account_name: str, biz: str, limit: int) -> None:
    rows = target_rows(output_dir, account_name, biz)
    print(f"Target articles in manifest: {len(rows)}", file=sys.stderr)
    for row in rows[:limit]:
        print(f"- {row.get('publish_time', '')} | {row.get('title', '')}", file=sys.stderr)


def candidate_urls(profile_root: Path) -> set[str]:
    return {candidate.url for candidate in discover_candidates(profile_root)}


def activate_profile(window: auto.Control, keep_topmost: bool) -> WindowRect:
    hwnd = int(window.NativeWindowHandle or 0)
    if hwnd:
        User32.restore(hwnd)
        User32.set_topmost(hwnd, keep_topmost)
    try:
        window.SetActive()
    except Exception:
        pass
    time.sleep(0.3)
    return window_rect(window)


def visible_card_points(rect: WindowRect, offsets: tuple[int, ...], x_offset: int) -> list[tuple[int, int]]:
    screen_w, screen_h = User32.screen_size()
    x = max(0, min(rect.left + x_offset, screen_w - 80))
    points: list[tuple[int, int]] = []
    for offset in offsets:
        y = max(0, min(rect.top + offset, screen_h - 40))
        if rect.top + 120 < y < min(rect.bottom, screen_h):
            points.append((x, y))
    return points


def scroll_profile(rect: WindowRect, wheel_clicks: int, direction: str) -> None:
    screen_w, screen_h = User32.screen_size()
    scroll_x = max(0, min(rect.right - 90, screen_w - 80))
    scroll_y = max(0, min(rect.top + rect.height - 170, screen_h - 80))
    User32.move_cursor(scroll_x, scroll_y)
    time.sleep(0.2)
    sign = 1 if direction == "newer" else -1
    User32.wheel(sign * abs(wheel_clicks))
    print(f"Scrolled {direction} by {wheel_clicks} wheel clicks.", file=sys.stderr)


def harvest_new_articles(
    urls: set[str],
    output_dir: Path,
    account_name: str,
    biz: str,
    timeout: int,
    dry_run: bool,
    skip_urls: set[str] | None = None,
) -> tuple[int, datetime | None]:
    seen = load_seen(output_dir)
    skip_urls = skip_urls if skip_urls is not None else set()
    saved = 0
    oldest_seen: datetime | None = None

    for url in sorted(urls):
        if url in seen or url in skip_urls:
            continue
        try:
            article = parse_article(url, timeout=timeout)
        except Exception as exc:
            skip_urls.add(url)
            print(f"  Could not parse new URL: {url} | {exc}", file=sys.stderr)
            continue

        if not is_target_article(article, account_name, biz):
            skip_urls.add(url)
            print(f"  Skip non-target: {article.account_name or article.biz or 'unknown'} | {article.title}", file=sys.stderr)
            continue

        published = parse_publish_time(article.publish_time)
        if published != datetime.min:
            oldest_seen = published if oldest_seen is None else min(oldest_seen, published)

        print(f"  Target: {article.publish_time} | {article.title}", file=sys.stderr)
        if not dry_run:
            path = save_article(article, output_dir)
            seen.add(url)
            skip_urls.add(url)
            saved += 1
            print(f"    Saved: {path}", file=sys.stderr)
        else:
            skip_urls.add(url)

    return saved, oldest_seen


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Click visible WeChat official-account cards and archive target articles.")
    parser.add_argument("--profile-root", type=Path, default=DEFAULT_PROFILE_ROOT, help="WeChat WebView profile root.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory.")
    parser.add_argument("--account-name", default=DEFAULT_ACCOUNT_NAME, help="Target account display name.")
    parser.add_argument("--biz", default=DEFAULT_BIZ, help="Target WeChat __biz id.")
    parser.add_argument("--until-date", type=str, default="", help="Stop after reaching articles older than this YYYY-MM-DD date.")
    parser.add_argument("--max-articles", type=int, default=5, help="Stop after saving this many new target articles. 0 means no limit.")
    parser.add_argument("--max-cards", type=int, default=12, help="Maximum visible cards to click.")
    parser.add_argument("--max-scrolls", type=int, default=4, help="Maximum scroll batches.")
    parser.add_argument("--card-y-offsets", type=parse_offsets, default=DEFAULT_CARD_Y_OFFSETS, help="Comma-separated click y-offsets from the profile window top.")
    parser.add_argument("--card-x-offset", type=int, default=220, help="Click x-offset from the profile window left; tune this to hit title text.")
    parser.add_argument("--scroll-wheel-clicks", type=int, default=5, help="Mouse wheel clicks per scroll batch.")
    parser.add_argument(
        "--scroll-direction",
        choices=("older", "newer"),
        default="older",
        help="Scroll direction between batches. older moves down the profile; newer moves back toward recent posts.",
    )
    parser.add_argument("--click-delay", type=float, default=2.5, help="Seconds to wait after clicking a card.")
    parser.add_argument("--scan-delay", type=float, default=0.4, help="Seconds to wait before rescanning local history.")
    parser.add_argument("--timeout", type=int, default=10, help="HTTP timeout for opened article pages.")
    parser.add_argument("--dry-run", action="store_true", help="Click and parse, but do not write article files.")
    parser.add_argument("--plan-only", action="store_true", help="Print computed click points without clicking or scrolling.")
    parser.add_argument("--scroll-only", action="store_true", help="Do not click cards; scroll the profile and harvest newly exposed URLs from local history.")
    parser.add_argument("--delta-only", action="store_true", help="In scroll-only mode, only harvest URLs first seen after each scroll.")
    parser.add_argument("--no-topmost", action="store_true", help="Do not force the WeChat profile window topmost during the run.")
    parser.add_argument("--recent", type=int, default=8, help="Print this many recent manifest rows at the end.")
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    args = parse_args()
    until = datetime.min
    if args.until_date:
        until = datetime.strptime(args.until_date, "%Y-%m-%d")

    window = find_profile_window()
    known_urls = candidate_urls(args.profile_root)
    print(f"Known local WeChat article URLs before GUI run: {len(known_urls)}", file=sys.stderr)
    print_recent(args.output_dir, args.account_name, args.biz, min(args.recent, 5))

    total_saved = 0
    clicked = 0
    stop_for_date = False
    session_skipped: set[str] = set()

    try:
        if args.scroll_only:
            for scroll_index in range(args.max_scrolls + 1):
                rect = activate_profile(window, keep_topmost=not args.no_topmost)
                after_urls = candidate_urls(args.profile_root)
                new_urls = after_urls - known_urls
                scan_urls = new_urls if args.delta_only else after_urls
                known_urls = after_urls
                print(
                    f"Scroll batch {scroll_index + 1}: new local URLs {len(new_urls)}; scan candidates {len(scan_urls)}",
                    file=sys.stderr,
                )
                saved, oldest = harvest_new_articles(
                    scan_urls,
                    output_dir=args.output_dir,
                    account_name=args.account_name,
                    biz=args.biz,
                    timeout=args.timeout,
                    dry_run=args.dry_run,
                    skip_urls=session_skipped,
                )
                total_saved += saved

                if until != datetime.min and oldest is not None and oldest < until:
                    stop_for_date = True
                    break
                if args.max_articles and total_saved >= args.max_articles:
                    break
                if scroll_index >= args.max_scrolls:
                    break

                scroll_profile(rect, args.scroll_wheel_clicks, args.scroll_direction)
                time.sleep(max(1.0, args.click_delay))
            raise StopIteration

        for scroll_index in range(args.max_scrolls + 1):
            rect = activate_profile(window, keep_topmost=not args.no_topmost)
            points = visible_card_points(rect, args.card_y_offsets, args.card_x_offset)
            print(f"Scroll batch {scroll_index + 1}: clicking {len(points)} visible card slots.", file=sys.stderr)
            if args.plan_only:
                for point_index, (x, y) in enumerate(points, start=1):
                    print(f"  Slot {point_index}: ({x}, {y})", file=sys.stderr)
                break

            for point_index, (x, y) in enumerate(points, start=1):
                if args.max_cards and clicked >= args.max_cards:
                    raise StopIteration
                if args.max_articles and total_saved >= args.max_articles:
                    raise StopIteration

                clicked += 1
                rect = activate_profile(window, keep_topmost=not args.no_topmost)
                print(f"Click {clicked}: slot {point_index} at ({x}, {y})", file=sys.stderr)
                auto.Click(x, y)
                time.sleep(args.click_delay)
                time.sleep(args.scan_delay)

                after_urls = candidate_urls(args.profile_root)
                new_urls = after_urls - known_urls
                known_urls = after_urls
                print(f"  New local URLs after click: {len(new_urls)}", file=sys.stderr)
                saved, oldest = harvest_new_articles(
                    new_urls,
                    output_dir=args.output_dir,
                    account_name=args.account_name,
                    biz=args.biz,
                    timeout=args.timeout,
                    dry_run=args.dry_run,
                )
                total_saved += saved

                if until != datetime.min and oldest is not None and oldest < until:
                    stop_for_date = True
                    raise StopIteration

            if scroll_index >= args.max_scrolls:
                break

            rect = activate_profile(window, keep_topmost=not args.no_topmost)
            scroll_profile(rect, args.scroll_wheel_clicks, args.scroll_direction)
            time.sleep(1.0)
    except StopIteration:
        pass
    finally:
        if not args.no_topmost:
            hwnd = int(window.NativeWindowHandle or 0)
            if hwnd:
                User32.set_topmost(hwnd, False)

    print(f"GUI run clicked {clicked} slots and saved {total_saved} new target articles.", file=sys.stderr)
    if stop_for_date:
        print(f"Stopped because an opened article was older than {args.until_date}.", file=sys.stderr)
    print_recent(args.output_dir, args.account_name, args.biz, args.recent)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
