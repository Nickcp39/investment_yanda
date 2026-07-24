#!/usr/bin/env python
"""Last-5-year-only log trend review.

This matches the visual question: show only the latest five-year chart window
and fit one log-linear trend using only that visible window.
"""
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
PANEL = ROOT / "macro" / "market_panel" / "data"
OUT = ROOT / "macro" / "market_panel" / "log_trend" / "last5y_window_review"
OUT.mkdir(parents=True, exist_ok=True)

ASSETS = [
    ("QQQ", "Nasdaq-100 ETF"),
    ("GOOG", "Alphabet Class C"),
    ("GOOGL", "Alphabet Class A"),
    ("MSFT", "Microsoft"),
    ("AAPL", "Apple"),
    ("NVDA", "Nvidia"),
    ("AMZN", "Amazon"),
    ("META", "Meta"),
    ("TSLA", "Tesla"),
    ("SPY", "S&P 500 ETF"),
    ("GOLD", "Gold futures GC=F"),
    ("KO", "Coca-Cola"),
    ("PEP", "PepsiCo"),
    ("COST", "Costco"),
    ("PG", "Procter & Gamble"),
    ("WMT", "Walmart"),
    ("MCD", "McDonald's"),
    ("CL", "Colgate-Palmolive"),
    ("KMB", "Kimberly-Clark"),
    ("JNJ", "Johnson & Johnson"),
    ("PM", "Philip Morris"),
]

EXTERNAL_DATA = {
    "KO": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "KO.csv",
    "PEP": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "PEP.csv",
    "COST": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "COST.csv",
    "PG": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "PG.csv",
    "WMT": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "WMT.csv",
    "MCD": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "MCD.csv",
    "CL": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "CL.csv",
    "KMB": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "KMB.csv",
    "JNJ": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "JNJ.csv",
    "PM": ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review" / "data" / "PM.csv",
}


def load(label: str) -> pd.DataFrame:
    path = EXTERNAL_DATA.get(label, PANEL / f"{label}.csv")
    df = pd.read_csv(path)
    cols = list(df.columns)
    df = df.rename(columns={cols[0]: "date", cols[1]: "price"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["price"]).sort_values("date").reset_index(drop=True)
    df = df[df["price"] > 0].reset_index(drop=True)
    return df


def fit_last5(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    end = df["date"].iloc[-1]
    start = end - pd.DateOffset(years=5)
    window = df[df["date"] >= start].copy().reset_index(drop=True)
    t = (window["date"] - window["date"].iloc[0]).dt.days.to_numpy(dtype=float)
    price = window["price"].to_numpy(dtype=float)
    y = np.log(price)

    b, a = np.polyfit(t, y, 1)
    trend_log = a + b * t
    trend = np.exp(trend_log)
    resid = y - trend_log
    sigma = float(resid.std(ddof=1))

    # Ordinary price-space straight line, included only as a visual contrast.
    b_price, a_price = np.polyfit(t, price, 1)
    price_line = a_price + b_price * t

    window["log_trend_5y_window"] = trend
    window["price_straight_line"] = price_line
    window["dev_pct_vs_log_trend"] = price / trend - 1.0
    window["dev_sigma_vs_log_trend"] = resid / sigma if sigma else np.nan

    stats = {
        "start": window["date"].iloc[0].date().isoformat(),
        "end": window["date"].iloc[-1].date().isoformat(),
        "n": int(len(window)),
        "price": float(price[-1]),
        "trend": float(trend[-1]),
        "dev_pct": float(price[-1] / trend[-1] - 1.0),
        "dev_sigma": float((y[-1] - trend_log[-1]) / sigma) if sigma else float("nan"),
        "trend_cagr": math.exp(b * 365.25) - 1.0,
        "price_line": float(price_line[-1]),
        "dev_pct_vs_price_line": float(price[-1] / price_line[-1] - 1.0),
    }
    return window, stats


def pct(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def cagr_text(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:.1f}%"


def plot_asset(label: str, desc: str, window: pd.DataFrame, stats: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax, ax_dev) = plt.subplots(
        2,
        1,
        figsize=(12.5, 7.0),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.05]},
    )
    ax.plot(window["date"], window["price"], color="#1a1d21", lw=1.25, label=f"{label} price")
    ax.plot(
        window["date"],
        window["log_trend_5y_window"],
        color="#16a34a",
        lw=2.0,
        label=f"5Y-window log trend ({cagr_text(stats['trend_cagr'])}/yr)",
    )
    ax.plot(
        window["date"],
        window["price_straight_line"],
        color="#f97316",
        lw=1.3,
        ls="--",
        alpha=0.8,
        label="ordinary price straight line",
    )
    ax.scatter([window["date"].iloc[-1]], [stats["price"]], color="#dc2626", s=34, zorder=5)
    ax.annotate(f" {stats['price']:,.2f}", (window["date"].iloc[-1], stats["price"]), color="#dc2626", va="center")
    ax.set_title(f"{label} - latest 5Y window only ({desc})")
    ax.set_ylabel("price")
    ax.grid(True, alpha=0.15)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    ax_dev.plot(window["date"], window["dev_pct_vs_log_trend"] * 100, color="#16a34a", lw=1.3, label="price vs 5Y-window log trend")
    ax_dev.axhline(0, color="#555555", lw=0.85)
    ax_dev.axhline(20, color="#b91c1c", lw=0.75, ls="--", alpha=0.45)
    ax_dev.axhline(-20, color="#0f766e", lw=0.75, ls="--", alpha=0.45)
    ax_dev.set_ylabel("deviation %")
    ax_dev.grid(True, alpha=0.14)
    ax_dev.legend(loc="upper left", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(OUT / f"{label}_last5y_log_trend.png", dpi=130)
    plt.close(fig)


def plot_dashboard(items: list[tuple[str, pd.DataFrame, dict]]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ncols = 2
    nrows = math.ceil(len(items) / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(14, 4.0 * nrows))
    axes = np.array(axes).reshape(-1)

    for ax, (label, window, stats) in zip(axes, items):
        ax.plot(window["date"], window["price"], color="#1a1d21", lw=1.05, label="price")
        ax.plot(window["date"], window["log_trend_5y_window"], color="#16a34a", lw=1.7, label="5Y-window log trend")
        ax.set_title(f"{label}: vs trend {pct(stats['dev_pct'])}, CAGR {cagr_text(stats['trend_cagr'])}", fontsize=10)
        ax.grid(True, alpha=0.14)
        ax.legend(loc="upper left", fontsize=8, frameon=False)

    for ax in axes[len(items):]:
        ax.axis("off")

    fig.suptitle("Latest five-year window only - log trend converted to price", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.985])
    fig.savefig(OUT / "last5y_window_dashboard.png", dpi=130)
    plt.close(fig)


def main() -> int:
    rows = []
    items = []
    for label, desc in ASSETS:
        df = load(label)
        window, stats = fit_last5(df)
        window.to_csv(OUT / f"{label}_last5y_log_trend.csv", index=False)
        plot_asset(label, desc, window, stats)
        rows.append({"ticker": label, "description": desc, **stats})
        items.append((label, window, stats))

    plot_dashboard(items)
    summary = pd.DataFrame(rows)
    summary.to_csv(OUT / "last5y_window_summary.csv", index=False)

    lines = [
        "# Latest 5Y Window Log-Trend Review",
        "",
        "This version only displays the latest five-year window and fits one log-linear",
        "trend using only that visible window. It does not show older rolling history.",
        "",
        "## Latest",
        "",
        "| ticker | window | price | 5Y-window trend | vs trend | trend CAGR | vs ordinary price line |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['ticker']} | {r['start']} to {r['end']} | {r['price']:,.2f} | "
            f"{r['trend']:,.2f} | {pct(r['dev_pct'])} | {cagr_text(r['trend_cagr'])} | "
            f"{pct(r['dev_pct_vs_price_line'])} |"
        )
    lines += [
        "",
        "## Files",
        "",
        "- `last5y_window_dashboard.png`",
        "- `<TICKER>_last5y_log_trend.png`",
        "- `<TICKER>_last5y_log_trend.csv`",
        "- `last5y_window_summary.csv`",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(summary[["ticker", "start", "end", "price", "trend", "dev_pct", "trend_cagr"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
