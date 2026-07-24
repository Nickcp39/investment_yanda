#!/usr/bin/env python
"""Latest-5Y channel with one major peak/trough per time segment."""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "macro" / "market_panel" / "log_trend" / "last5y_window_review"
OUT = BASE / "channel_review_major_points"
OUT.mkdir(parents=True, exist_ok=True)

ASSETS = [
    "QQQ", "SPY", "GOLD",
    "GOOG", "GOOGL", "MSFT", "AAPL", "NVDA", "AMZN", "META", "TSLA",
    "KO", "PEP", "PG", "WMT", "COST", "MCD", "CL", "KMB", "JNJ", "PM",
]
SEGMENT_MONTHS = 12


def load(label: str) -> pd.DataFrame:
    df = pd.read_csv(BASE / f"{label}_last5y_log_trend.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


def pct(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def major_points(df: pd.DataFrame, months: int = SEGMENT_MONTHS) -> tuple[list[int], list[int]]:
    resid = np.log(df["price"].to_numpy(dtype=float)) - np.log(df["log_trend_5y_window"].to_numpy(dtype=float))
    dates = df["date"]
    start = dates.iloc[0]
    end = dates.iloc[-1]

    lows: list[int] = []
    highs: list[int] = []
    seg_start = start
    while seg_start <= end:
        seg_end = seg_start + pd.DateOffset(months=months)
        mask = (dates >= seg_start) & (dates < seg_end)
        idx = np.where(mask.to_numpy())[0]
        if len(idx) >= 40:
            seg_resid = resid[idx]
            lows.append(int(idx[np.nanargmin(seg_resid)]))
            highs.append(int(idx[np.nanargmax(seg_resid)]))
        seg_start = seg_end

    # Remove duplicate indices if a short segment overlaps oddly.
    lows = sorted(set(lows))
    highs = sorted(set(highs))
    return lows, highs


def channel_from_major_points(df: pd.DataFrame, lows: list[int], highs: list[int]) -> tuple[pd.DataFrame, dict]:
    price = df["price"].to_numpy(dtype=float)
    trend = df["log_trend_5y_window"].to_numpy(dtype=float)
    resid = np.log(price) - np.log(trend)

    low_resid = resid[lows] if lows else resid
    high_resid = resid[highs] if highs else resid

    # Median of one-point-per-segment extremes is robust: it avoids a single 2021/2022
    # extreme defining the whole channel while still anchoring on major swings.
    lower_shift = float(np.nanmedian(low_resid))
    upper_shift = float(np.nanmedian(high_resid))
    lower_extreme = float(np.nanmin(low_resid))
    upper_extreme = float(np.nanmax(high_resid))

    out = df.copy()
    out["support_major"] = trend * math.exp(lower_shift)
    out["resistance_major"] = trend * math.exp(upper_shift)
    out["support_extreme_major"] = trend * math.exp(lower_extreme)
    out["resistance_extreme_major"] = trend * math.exp(upper_extreme)
    out["dev_pct_vs_center"] = price / trend - 1.0
    out["dev_pct_vs_support"] = price / out["support_major"].to_numpy() - 1.0
    out["dev_pct_vs_resistance"] = price / out["resistance_major"].to_numpy() - 1.0

    stats = {
        "price": float(price[-1]),
        "center": float(trend[-1]),
        "support": float(out["support_major"].iloc[-1]),
        "resistance": float(out["resistance_major"].iloc[-1]),
        "support_extreme": float(out["support_extreme_major"].iloc[-1]),
        "resistance_extreme": float(out["resistance_extreme_major"].iloc[-1]),
        "center_dev": float(out["dev_pct_vs_center"].iloc[-1]),
        "support_dev": float(out["dev_pct_vs_support"].iloc[-1]),
        "resistance_dev": float(out["dev_pct_vs_resistance"].iloc[-1]),
        "lower_shift_pct": math.exp(lower_shift) - 1.0,
        "upper_shift_pct": math.exp(upper_shift) - 1.0,
        "lower_extreme_pct": math.exp(lower_extreme) - 1.0,
        "upper_extreme_pct": math.exp(upper_extreme) - 1.0,
        "n_low_points": len(lows),
        "n_high_points": len(highs),
    }
    return out, stats


def plot_asset(label: str, df: pd.DataFrame, lows: list[int], highs: list[int], stats: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax, ax_dev) = plt.subplots(
        2,
        1,
        figsize=(12.8, 7.2),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.05]},
    )
    ax.plot(df["date"], df["price"], color="#1a1d21", lw=1.25, label=f"{label} price")
    ax.plot(df["date"], df["resistance_major"], color="#dc2626", lw=2.0, label=f"major upper ({pct(stats['upper_shift_pct'])})")
    ax.plot(df["date"], df["log_trend_5y_window"], color="#16a34a", lw=2.0, label="center 5Y log trend")
    ax.plot(df["date"], df["support_major"], color="#16a34a", lw=2.0, ls="--", label=f"major lower ({pct(stats['lower_shift_pct'])})")
    ax.plot(df["date"], df["resistance_extreme_major"], color="#dc2626", lw=0.9, ls=":", alpha=0.45, label="outer extreme major")
    ax.plot(df["date"], df["support_extreme_major"], color="#16a34a", lw=0.9, ls=":", alpha=0.45)

    ax.scatter(df["date"].iloc[lows], df["price"].iloc[lows], s=42, facecolors="white", edgecolors="#16a34a", linewidths=1.5, zorder=5)
    ax.scatter(df["date"].iloc[highs], df["price"].iloc[highs], s=42, facecolors="white", edgecolors="#dc2626", linewidths=1.5, zorder=5)
    ax.scatter([df["date"].iloc[-1]], [stats["price"]], color="#111827", s=36, zorder=6)
    ax.annotate(f" {stats['price']:,.2f}", (df["date"].iloc[-1], stats["price"]), color="#111827", va="center")
    ax.set_title(f"{label} - one major peak/trough per {SEGMENT_MONTHS}M segment")
    ax.set_ylabel("price")
    ax.grid(True, alpha=0.15)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    ax_dev.plot(df["date"], df["dev_pct_vs_center"] * 100, color="#111827", lw=1.1, label="price vs center")
    ax_dev.axhline(0, color="#555555", lw=0.8)
    ax_dev.axhline(stats["upper_shift_pct"] * 100, color="#dc2626", lw=1.0, ls="--", alpha=0.7)
    ax_dev.axhline(stats["lower_shift_pct"] * 100, color="#16a34a", lw=1.0, ls="--", alpha=0.7)
    ax_dev.set_ylabel("center dev %")
    ax_dev.grid(True, alpha=0.14)
    ax_dev.legend(loc="upper left", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(OUT / f"{label}_major_points_channel.png", dpi=130)
    plt.close(fig)


def plot_dashboard(rows: list[dict], filename: str, title: str, tickers: list[str]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    selected = [r for r in rows if r["ticker"] in tickers]
    if not selected:
        return
    labels = [r["ticker"] for r in selected]
    x = np.arange(len(labels))
    center = [r["center_dev"] * 100 for r in selected]
    lower = [r["lower_shift_pct"] * 100 for r in selected]
    upper = [r["upper_shift_pct"] * 100 for r in selected]

    fig, ax = plt.subplots(figsize=(max(11.5, len(labels) * 0.68), 5.6))
    ax.scatter(x, center, color="#111827", s=45, label="current vs center")
    for i, (lo, hi) in enumerate(zip(lower, upper)):
        ax.vlines(i, lo, hi, color="#9ca3af", lw=7, alpha=0.55)
        ax.scatter([i], [lo], color="#16a34a", s=32)
        ax.scatter([i], [hi], color="#dc2626", s=32)
    ax.axhline(0, color="#555555", lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("deviation vs center trend %")
    ax.set_title(title)
    ax.grid(axis="y", alpha=0.15)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=130)
    plt.close(fig)


def main() -> int:
    rows = []
    point_rows = []
    for label in ASSETS:
        base = load(label)
        lows, highs = major_points(base)
        channel, stats = channel_from_major_points(base, lows, highs)
        channel.to_csv(OUT / f"{label}_major_points_channel.csv", index=False)
        plot_asset(label, channel, lows, highs, stats)
        rows.append({"ticker": label, **stats})

        for kind, idxs in [("low", lows), ("high", highs)]:
            for i in idxs:
                point_rows.append({
                    "ticker": label,
                    "kind": kind,
                    "date": channel["date"].iloc[i].date().isoformat(),
                    "price": float(channel["price"].iloc[i]),
                    "dev_pct_vs_center": float(channel["dev_pct_vs_center"].iloc[i]),
                })

    summary = pd.DataFrame(rows)
    points = pd.DataFrame(point_rows)
    summary.to_csv(OUT / "major_points_channel_summary.csv", index=False)
    points.to_csv(OUT / "major_points_used.csv", index=False)
    plot_dashboard(
        rows,
        "major_points_big_tech_dashboard.png",
        "Major-points 5Y log channel - big tech / indices",
        ["QQQ", "SPY", "GOOG", "GOOGL", "MSFT", "AAPL", "NVDA", "AMZN", "META", "TSLA"],
    )
    plot_dashboard(
        rows,
        "major_points_consumer_leaders_dashboard.png",
        "Major-points 5Y log channel - consumer / life-necessity leaders",
        ["KO", "PEP", "PG", "WMT", "COST", "MCD", "CL", "KMB", "JNJ", "PM"],
    )
    plot_dashboard(
        rows,
        "major_points_cross_asset_dashboard.png",
        "Major-points 5Y log channel - cross asset",
        ["QQQ", "SPY", "GOLD", "GOOG", "MSFT", "KO", "COST", "PG"],
    )

    lines = [
        "# Major-Points Channel Review",
        "",
        f"Rule: split the latest 5Y window into {SEGMENT_MONTHS}-month segments.",
        "Each segment contributes only one major peak and one major trough.",
        "The channel is still the same center log trend shifted up/down in log space.",
        "",
        "## Latest",
        "",
        "| ticker | price | lower | center | upper | vs center | vs lower | room to upper | points low/high |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['ticker']} | {r['price']:,.2f} | {r['support']:,.2f} | {r['center']:,.2f} | "
            f"{r['resistance']:,.2f} | {pct(r['center_dev'])} | {pct(r['support_dev'])} | "
            f"{pct(r['resistance_dev'])} | {r['n_low_points']}/{r['n_high_points']} |"
        )
    lines += [
        "",
        "## Files",
        "",
        "- `<TICKER>_major_points_channel.png`",
        "- `<TICKER>_major_points_channel.csv`",
        "- `major_points_big_tech_dashboard.png`",
        "- `major_points_consumer_leaders_dashboard.png`",
        "- `major_points_cross_asset_dashboard.png`",
        "- `major_points_channel_summary.csv`",
        "- `major_points_used.csv`",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(summary[["ticker", "price", "support", "center", "resistance", "center_dev", "support_dev", "resistance_dev", "n_low_points", "n_high_points"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
