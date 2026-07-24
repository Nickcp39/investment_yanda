#!/usr/bin/env python
"""Latest-5Y log trend channel: support / center / resistance lines."""
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
OUT = BASE / "channel_review"
OUT.mkdir(parents=True, exist_ok=True)

ASSETS = ["QQQ", "GOOG", "MSFT", "SPY", "GOLD", "KO", "COST", "PG"]


def load(label: str) -> pd.DataFrame:
    path = BASE / f"{label}_last5y_log_trend.csv"
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def local_extrema(df: pd.DataFrame, radius: int = 21) -> tuple[list[int], list[int]]:
    resid = np.log(df["price"].to_numpy()) - np.log(df["log_trend_5y_window"].to_numpy())
    lows: list[int] = []
    highs: list[int] = []
    for i in range(radius, len(resid) - radius):
        window = resid[i - radius:i + radius + 1]
        if resid[i] == np.nanmin(window):
            lows.append(i)
        if resid[i] == np.nanmax(window):
            highs.append(i)
    lows = sorted(lows, key=lambda i: resid[i])[:6]
    highs = sorted(highs, key=lambda i: resid[i], reverse=True)[:6]
    return lows, highs


def pct(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def make_channel(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    trend = df["log_trend_5y_window"].to_numpy(dtype=float)
    price = df["price"].to_numpy(dtype=float)
    resid = np.log(price) - np.log(trend)

    lower_shift = float(np.nanquantile(resid, 0.10))
    upper_shift = float(np.nanquantile(resid, 0.90))
    lower_extreme = float(np.nanquantile(resid, 0.02))
    upper_extreme = float(np.nanquantile(resid, 0.98))

    out = df.copy()
    out["support_q10"] = trend * math.exp(lower_shift)
    out["resistance_q90"] = trend * math.exp(upper_shift)
    out["support_q02"] = trend * math.exp(lower_extreme)
    out["resistance_q98"] = trend * math.exp(upper_extreme)
    out["dev_pct_vs_center"] = price / trend - 1.0
    out["dev_pct_vs_support_q10"] = price / out["support_q10"].to_numpy() - 1.0
    out["dev_pct_vs_resistance_q90"] = price / out["resistance_q90"].to_numpy() - 1.0

    stats = {
        "price": float(price[-1]),
        "center": float(trend[-1]),
        "support_q10": float(out["support_q10"].iloc[-1]),
        "resistance_q90": float(out["resistance_q90"].iloc[-1]),
        "support_q02": float(out["support_q02"].iloc[-1]),
        "resistance_q98": float(out["resistance_q98"].iloc[-1]),
        "center_dev": float(out["dev_pct_vs_center"].iloc[-1]),
        "support_dev": float(out["dev_pct_vs_support_q10"].iloc[-1]),
        "resistance_dev": float(out["dev_pct_vs_resistance_q90"].iloc[-1]),
        "lower_shift_pct": math.exp(lower_shift) - 1.0,
        "upper_shift_pct": math.exp(upper_shift) - 1.0,
        "lower_extreme_pct": math.exp(lower_extreme) - 1.0,
        "upper_extreme_pct": math.exp(upper_extreme) - 1.0,
    }
    return out, stats


def plot_asset(label: str, df: pd.DataFrame, stats: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    lows, highs = local_extrema(df)
    fig, (ax, ax_dev) = plt.subplots(
        2,
        1,
        figsize=(12.8, 7.2),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.05]},
    )

    ax.plot(df["date"], df["price"], color="#1a1d21", lw=1.25, label=f"{label} price")
    ax.plot(df["date"], df["resistance_q90"], color="#dc2626", lw=2.0, label=f"upper q90 ({pct(stats['upper_shift_pct'])} vs center)")
    ax.plot(df["date"], df["log_trend_5y_window"], color="#16a34a", lw=2.0, label="center 5Y log trend")
    ax.plot(df["date"], df["support_q10"], color="#16a34a", lw=2.0, ls="--", label=f"lower q10 ({pct(stats['lower_shift_pct'])} vs center)")
    ax.plot(df["date"], df["resistance_q98"], color="#dc2626", lw=0.9, ls=":", alpha=0.5, label="outer q98/q02")
    ax.plot(df["date"], df["support_q02"], color="#16a34a", lw=0.9, ls=":", alpha=0.5)

    if lows:
        ax.scatter(df["date"].iloc[lows], df["price"].iloc[lows], s=28, facecolors="white", edgecolors="#16a34a", zorder=5)
    if highs:
        ax.scatter(df["date"].iloc[highs], df["price"].iloc[highs], s=28, facecolors="white", edgecolors="#dc2626", zorder=5)

    ax.scatter([df["date"].iloc[-1]], [stats["price"]], color="#111827", s=34, zorder=6)
    ax.annotate(f" {stats['price']:,.2f}", (df["date"].iloc[-1], stats["price"]), color="#111827", va="center")
    ax.set_title(f"{label} - latest 5Y log trend channel: lower / center / upper")
    ax.set_ylabel("price")
    ax.grid(True, alpha=0.15)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    ax_dev.plot(df["date"], df["dev_pct_vs_center"] * 100, color="#111827", lw=1.1, label="price vs center")
    ax_dev.axhline(0, color="#555555", lw=0.8)
    ax_dev.axhline(stats["upper_shift_pct"] * 100, color="#dc2626", lw=1.0, ls="--", alpha=0.7, label="upper q90 threshold")
    ax_dev.axhline(stats["lower_shift_pct"] * 100, color="#16a34a", lw=1.0, ls="--", alpha=0.7, label="lower q10 threshold")
    ax_dev.set_ylabel("center dev %")
    ax_dev.grid(True, alpha=0.14)
    ax_dev.legend(loc="upper left", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(OUT / f"{label}_last5y_log_trend_channel.png", dpi=130)
    plt.close(fig)


def plot_dashboard(rows: list[dict]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(11.5, 5.4))
    labels = [r["ticker"] for r in rows]
    x = np.arange(len(labels))
    center = [r["center_dev"] * 100 for r in rows]
    lower = [r["lower_shift_pct"] * 100 for r in rows]
    upper = [r["upper_shift_pct"] * 100 for r in rows]

    ax.scatter(x, center, color="#111827", s=45, label="current vs center")
    for i, (lo, hi) in enumerate(zip(lower, upper)):
        ax.vlines(i, lo, hi, color="#9ca3af", lw=7, alpha=0.55)
        ax.scatter([i], [lo], color="#16a34a", s=32)
        ax.scatter([i], [hi], color="#dc2626", s=32)
    ax.axhline(0, color="#555555", lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("deviation vs center trend %")
    ax.set_title("Latest position inside 5Y log trend channel")
    ax.grid(axis="y", alpha=0.15)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "last5y_channel_position_dashboard.png", dpi=130)
    plt.close(fig)


def main() -> int:
    rows = []
    for label in ASSETS:
        base = load(label)
        channel, stats = make_channel(base)
        channel.to_csv(OUT / f"{label}_last5y_log_trend_channel.csv", index=False)
        plot_asset(label, channel, stats)
        rows.append({"ticker": label, **stats})

    plot_dashboard(rows)
    summary = pd.DataFrame(rows)
    summary.to_csv(OUT / "last5y_channel_summary.csv", index=False)

    lines = [
        "# Latest 5Y Log-Trend Channel Review",
        "",
        "Three main lines:",
        "",
        "- upper: same 5Y log trend shifted upward to the 90th percentile residual",
        "- center: 5Y log trend",
        "- lower: same 5Y log trend shifted downward to the 10th percentile residual",
        "",
        "Dotted outer lines show 2nd/98th percentile residuals as extreme-touch context.",
        "",
        "## Latest",
        "",
        "| ticker | price | lower q10 | center | upper q90 | vs center | vs lower | room to upper | channel shifts |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['ticker']} | {r['price']:,.2f} | {r['support_q10']:,.2f} | "
            f"{r['center']:,.2f} | {r['resistance_q90']:,.2f} | {pct(r['center_dev'])} | "
            f"{pct(r['support_dev'])} | {pct(r['resistance_dev'])} | "
            f"{pct(r['lower_shift_pct'])} / {pct(r['upper_shift_pct'])} |"
        )
    lines += [
        "",
        "## Files",
        "",
        "- `last5y_channel_position_dashboard.png`",
        "- `<TICKER>_last5y_log_trend_channel.png`",
        "- `<TICKER>_last5y_log_trend_channel.csv`",
        "- `last5y_channel_summary.csv`",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(summary[["ticker", "price", "support_q10", "center", "resistance_q90", "center_dev", "support_dev", "resistance_dev"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
