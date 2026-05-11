#!/usr/bin/env python3
"""Scan QQQ history for unusually steep recent rallies.

The script downloads daily prices, computes rolling log-price regression slopes
over multiple lookback windows, and ranks the latest window against history.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import os
from pathlib import Path
import sys
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_WINDOWS = (5, 10, 20, 40, 60, 120)
TRADING_DAYS_PER_YEAR = 252


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rank the latest QQQ rally slope against historical windows."
    )
    parser.add_argument("--symbol", default="QQQ", help="Ticker symbol, default: QQQ")
    parser.add_argument(
        "--start",
        default="1999-03-10",
        help="Start date in YYYY-MM-DD. QQQ inception was 1999-03-10.",
    )
    parser.add_argument(
        "--end",
        default=dt.date.today().isoformat(),
        help="End date in YYYY-MM-DD, default: today.",
    )
    parser.add_argument(
        "--windows",
        default=",".join(str(x) for x in DEFAULT_WINDOWS),
        help="Comma-separated rolling window lengths in trading days.",
    )
    parser.add_argument(
        "--source",
        choices=("auto", "yahoo", "stooq"),
        default="auto",
        help="Price source. Yahoo uses adjusted close; Stooq is the fallback.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of non-overlapping top historical episodes per window.",
    )
    parser.add_argument(
        "--output-dir",
        default="data/processed/market_slope",
        help="Directory for generated CSV/Markdown/PNG outputs.",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Skip optional PNG chart generation.",
    )
    return parser.parse_args()


def utc_timestamp(date_text: str) -> int:
    date = dt.datetime.strptime(date_text, "%Y-%m-%d").date()
    return int(dt.datetime(date.year, date.month, date.day, tzinfo=dt.timezone.utc).timestamp())


def fetch_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as response:
        return json.load(response)


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8")


def fetch_yahoo(symbol: str, start: str, end: str) -> tuple[list[dict], str]:
    end_plus_one = (dt.datetime.strptime(end, "%Y-%m-%d").date() + dt.timedelta(days=1)).isoformat()
    params = {
        "period1": utc_timestamp(start),
        "period2": utc_timestamp(end_plus_one),
        "interval": "1d",
        "events": "history",
        "includeAdjustedClose": "true",
    }
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?{urlencode(params)}"
    payload = fetch_json(url)
    chart = payload.get("chart", {})
    if chart.get("error"):
        raise RuntimeError(chart["error"])
    result = (chart.get("result") or [None])[0]
    if not result or not result.get("timestamp"):
        raise RuntimeError("Yahoo returned no daily price data")

    timestamps = result["timestamp"]
    quote = result["indicators"]["quote"][0]
    adjclose = (result["indicators"].get("adjclose") or [{}])[0].get("adjclose") or []
    rows: list[dict] = []
    for i, timestamp in enumerate(timestamps):
        close = adjclose[i] if i < len(adjclose) else quote["close"][i]
        if close is None:
            continue
        date = dt.datetime.fromtimestamp(timestamp, tz=dt.timezone.utc).date().isoformat()
        rows.append({"date": date, "close": float(close)})
    return rows, "Yahoo Finance chart API adjusted close"


def fetch_stooq(symbol: str, start: str, end: str) -> tuple[list[dict], str]:
    stooq_symbol = f"{symbol.lower()}.us"
    params = {
        "s": stooq_symbol,
        "i": "d",
        "d1": start.replace("-", ""),
        "d2": end.replace("-", ""),
    }
    url = f"https://stooq.com/q/d/l/?{urlencode(params)}"
    text = fetch_text(url)
    rows: list[dict] = []
    for row in csv.DictReader(text.splitlines()):
        if not row.get("Date") or row.get("Close") in (None, ""):
            continue
        rows.append({"date": row["Date"], "close": float(row["Close"])})
    if not rows:
        raise RuntimeError("Stooq returned no daily price data")
    return rows, "Stooq daily close"


def fetch_prices(symbol: str, start: str, end: str, source: str) -> tuple[list[dict], str]:
    errors: list[str] = []
    sources: Iterable[str] = ("yahoo", "stooq") if source == "auto" else (source,)
    for chosen in sources:
        try:
            if chosen == "yahoo":
                return fetch_yahoo(symbol, start, end)
            return fetch_stooq(symbol, start, end)
        except (HTTPError, URLError, TimeoutError, RuntimeError, KeyError, ValueError) as exc:
            errors.append(f"{chosen}: {exc}")
    raise RuntimeError("Unable to fetch price data. " + " | ".join(errors))


def ols_slope(values: list[float]) -> float:
    n = len(values)
    x_mean = (n - 1) / 2
    y_mean = sum(values) / n
    numerator = sum((i - x_mean) * (value - y_mean) for i, value in enumerate(values))
    denominator = sum((i - x_mean) ** 2 for i in range(n))
    return numerator / denominator


def max_drawdown(values: list[float]) -> float:
    peak = values[0]
    worst = 0.0
    for value in values:
        peak = max(peak, value)
        worst = min(worst, value / peak - 1.0)
    return worst


def percent(value: float) -> str:
    return f"{value * 100:.2f}%"


def compute_windows(price_rows: list[dict], windows: list[int]) -> list[dict]:
    closes = [row["close"] for row in price_rows]
    dates = [row["date"] for row in price_rows]
    log_closes = [math.log(value) for value in closes]
    results: list[dict] = []

    for window in windows:
        if window < 2:
            raise ValueError("Windows must be at least 2 trading days")
        if window > len(price_rows):
            continue
        for end_idx in range(window - 1, len(price_rows)):
            start_idx = end_idx - window + 1
            window_closes = closes[start_idx : end_idx + 1]
            window_logs = log_closes[start_idx : end_idx + 1]
            regression_daily = ols_slope(window_logs)
            regression_window = math.exp(regression_daily * (window - 1)) - 1.0
            regression_ann = math.exp(regression_daily * TRADING_DAYS_PER_YEAR) - 1.0
            realized_log_return = window_logs[-1] - window_logs[0]
            realized_return = math.exp(realized_log_return) - 1.0
            endpoint_ann = math.exp(realized_log_return * TRADING_DAYS_PER_YEAR / (window - 1)) - 1.0
            results.append(
                {
                    "window": window,
                    "start_idx": start_idx,
                    "end_idx": end_idx,
                    "start_date": dates[start_idx],
                    "end_date": dates[end_idx],
                    "start_close": closes[start_idx],
                    "end_close": closes[end_idx],
                    "realized_return": realized_return,
                    "endpoint_ann_return": endpoint_ann,
                    "regression_daily_log_slope": regression_daily,
                    "regression_window_return": regression_window,
                    "regression_ann_return": regression_ann,
                    "max_drawdown": max_drawdown(window_closes),
                }
            )
    return results


def rank_latest(rows: list[dict], window: int) -> dict:
    subset = [row for row in rows if row["window"] == window]
    latest = subset[-1]
    ordered = sorted(subset, key=lambda row: row["regression_window_return"], reverse=True)
    rank = next(i + 1 for i, row in enumerate(ordered) if row is latest)
    values = [row["regression_window_return"] for row in subset]
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / max(1, len(values) - 1)
    stdev = math.sqrt(variance)
    percentile = 100.0 * (len(subset) - rank) / max(1, len(subset) - 1)
    best = ordered[0]
    return {
        "window": window,
        "latest": latest,
        "rank": rank,
        "count": len(subset),
        "percentile": percentile,
        "z_score": (latest["regression_window_return"] - mean) / stdev if stdev else 0.0,
        "best": best,
    }


def top_non_overlapping(rows: list[dict], window: int, limit: int) -> list[dict]:
    subset = sorted(
        (row for row in rows if row["window"] == window),
        key=lambda row: row["regression_window_return"],
        reverse=True,
    )
    chosen: list[dict] = []
    for row in subset:
        if all(row["end_idx"] < item["start_idx"] or row["start_idx"] > item["end_idx"] for item in chosen):
            chosen.append(row)
        if len(chosen) >= limit:
            break
    return chosen


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fields})


def build_markdown(
    symbol: str,
    source_name: str,
    price_rows: list[dict],
    ranks: list[dict],
    top_rows: dict[int, list[dict]],
    output_paths: dict[str, Path],
) -> str:
    latest_price = price_rows[-1]
    lines = [
        f"# {symbol} Rally Slope Scan",
        "",
        f"- Run date: {dt.date.today().isoformat()}",
        f"- Price source: {source_name}",
        f"- Latest price date: {latest_price['date']}",
        f"- Latest close used: {latest_price['close']:.2f}",
        "",
        "## Latest Window Rank",
        "",
        "| Window | Latest period | Latest return | Regression fitted window return | Rank | Percentile | Z-score | Historical max period | Historical max fitted return |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for item in ranks:
        latest = item["latest"]
        best = item["best"]
        lines.append(
            "| "
            f"{item['window']}d | "
            f"{latest['start_date']} to {latest['end_date']} | "
            f"{percent(latest['realized_return'])} | "
            f"{percent(latest['regression_window_return'])} | "
            f"{item['rank']}/{item['count']} | "
            f"{item['percentile']:.2f} | "
            f"{item['z_score']:.2f} | "
            f"{best['start_date']} to {best['end_date']} | "
            f"{percent(best['regression_window_return'])} |"
        )

    lines.extend(["", "## Top Non-Overlapping Historical Episodes", ""])
    for item in ranks:
        window = item["window"]
        lines.extend(
            [
                f"### {window} Trading Days",
                "",
                "| Rank | Period | Return | Regression fitted window return | Max drawdown inside window |",
                "| ---: | --- | ---: | ---: | ---: |",
            ]
        )
        for rank, row in enumerate(top_rows[window], start=1):
            lines.append(
                "| "
                f"{rank} | "
                f"{row['start_date']} to {row['end_date']} | "
                f"{percent(row['realized_return'])} | "
                f"{percent(row['regression_window_return'])} | "
                f"{percent(row['max_drawdown'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Output Files",
            "",
            f"- Rolling window data: `{output_paths['rolling'].as_posix()}`",
            f"- Top episodes: `{output_paths['top'].as_posix()}`",
            f"- This report: `{output_paths['report'].as_posix()}`",
        ]
    )
    if output_paths.get("plot"):
        lines.append(f"- Chart: `{output_paths['plot'].as_posix()}`")
    lines.append("")
    lines.extend(
        [
            "## Notes",
            "",
            "- The main ranking metric is an OLS regression slope on log adjusted close, converted into fitted return over the same window.",
            "- Annualized slope is still included in the CSV, but the report avoids annualized short-window numbers because they can look absurd.",
            "- A high annualized slope is a speed/rhythm measure, not a forecast.",
            "- Yahoo adjusted close includes dividends/splits when available; Stooq fallback may differ slightly.",
        ]
    )
    return "\n".join(lines) + "\n"


def maybe_plot(price_rows: list[dict], ranks: list[dict], path: Path, symbol: str) -> bool:
    try:
        import matplotlib.dates as mdates
        import matplotlib.pyplot as plt
    except Exception:
        return False

    dates = [dt.datetime.strptime(row["date"], "%Y-%m-%d").date() for row in price_rows]
    closes = [row["close"] for row in price_rows]
    fig, axes = plt.subplots(2, 1, figsize=(13, 8), sharex=False)

    axes[0].plot(dates, closes, color="#1f77b4", linewidth=1.2)
    axes[0].set_yscale("log")
    axes[0].set_title(f"{symbol} adjusted close (log scale)")
    axes[0].grid(True, alpha=0.25)

    windows = [item["window"] for item in ranks]
    latest_returns = [item["latest"]["realized_return"] * 100 for item in ranks]
    percentiles = [item["percentile"] for item in ranks]
    bars = axes[1].bar([str(window) for window in windows], latest_returns, color="#2ca02c", alpha=0.75)
    axes[1].set_title("Latest window realized return; labels show historical slope percentile")
    axes[1].set_xlabel("Window in trading days")
    axes[1].set_ylabel("Realized return (%)")
    axes[1].grid(True, axis="y", alpha=0.25)
    for bar, percentile in zip(bars, percentiles):
        axes[1].text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{percentile:.1f} pct",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    axes[0].xaxis.set_major_locator(mdates.YearLocator(base=2))
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return True


def main() -> int:
    args = parse_args()
    symbol = args.symbol.upper()
    windows = sorted({int(item.strip()) for item in args.windows.split(",") if item.strip()})
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    price_rows, source_name = fetch_prices(symbol, args.start, args.end, args.source)
    rolling = compute_windows(price_rows, windows)
    ranks = [rank_latest(rolling, window) for window in windows if any(row["window"] == window for row in rolling)]
    top_rows = {item["window"]: top_non_overlapping(rolling, item["window"], args.top) for item in ranks}

    stamp = dt.date.today().isoformat()
    base = f"{symbol.lower()}_slope_{stamp}"
    rolling_path = output_dir / f"{base}_rolling.csv"
    top_path = output_dir / f"{base}_top_episodes.csv"
    report_path = output_dir / f"{base}_report.md"
    plot_path = output_dir / f"{base}_chart.png"

    rolling_fields = [
        "window",
        "start_date",
        "end_date",
        "start_close",
        "end_close",
        "realized_return",
        "endpoint_ann_return",
        "regression_daily_log_slope",
        "regression_window_return",
        "regression_ann_return",
        "max_drawdown",
    ]
    write_csv(rolling_path, rolling, rolling_fields)

    flattened_top: list[dict] = []
    for window, rows in top_rows.items():
        for rank, row in enumerate(rows, start=1):
            flattened = dict(row)
            flattened["episode_rank"] = rank
            flattened_top.append(flattened)
    write_csv(top_path, flattened_top, ["episode_rank"] + rolling_fields)

    paths: dict[str, Path] = {"rolling": rolling_path, "top": top_path, "report": report_path}
    if not args.no_plot and maybe_plot(price_rows, ranks, plot_path, symbol):
        paths["plot"] = plot_path

    report = build_markdown(symbol, source_name, price_rows, ranks, top_rows, paths)
    report_path.write_text(report, encoding="utf-8")

    print(report)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
