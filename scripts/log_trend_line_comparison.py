#!/usr/bin/env python
"""Compare rolling log trend against fixed log-straight and literal price-straight lines."""
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
ROLL = ROOT / "macro" / "market_panel" / "log_trend" / "rolling_review"
OUT = ROLL / "line_comparison"
OUT.mkdir(parents=True, exist_ok=True)

ASSETS = [
    ("QQQ", "Nasdaq-100 ETF"),
    ("GOOG", "Alphabet Class C"),
    ("MSFT", "Microsoft"),
    ("AAPL", "Apple"),
    ("NVDA", "Nvidia"),
    ("AMZN", "Amazon"),
]

COLORS = {
    "price": "#1a1d21",
    "roll5": "#16a34a",
    "roll10": "#2563eb",
    "fixed5": "#16a34a",
    "fixed10": "#2563eb",
    "linear": "#f97316",
}


def load_price(label: str) -> pd.DataFrame:
    df = pd.read_csv(PANEL / f"{label}.csv")
    cols = list(df.columns)
    df = df.rename(columns={cols[0]: "date", cols[1]: "price"})
    df["date"] = pd.to_datetime(df["date"])
    return df.dropna(subset=["price"]).query("price > 0").sort_values("date").reset_index(drop=True)


def load_rolling(label: str) -> pd.DataFrame:
    df = pd.read_csv(ROLL / f"{label}_rolling_log_trend.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


def fixed_log_trend(df: pd.DataFrame, years: int) -> pd.Series:
    cutoff = df["date"].iloc[-1] - pd.DateOffset(years=years)
    mask = df["date"] >= cutoff
    t_all = (df["date"] - df["date"].iloc[0]).dt.days.to_numpy(dtype=float)
    y_all = np.log(df["price"].to_numpy(dtype=float))
    x = t_all[mask.to_numpy()]
    y = y_all[mask.to_numpy()]
    b, a = np.polyfit(x, y, 1)
    trend = np.full(len(df), np.nan)
    trend[mask.to_numpy()] = np.exp(a + b * t_all[mask.to_numpy()])
    return pd.Series(trend, index=df.index), math.exp(b * 365.25) - 1.0


def fixed_price_linear(df: pd.DataFrame, years: int) -> pd.Series:
    cutoff = df["date"].iloc[-1] - pd.DateOffset(years=years)
    mask = df["date"] >= cutoff
    t_all = (df["date"] - df["date"].iloc[0]).dt.days.to_numpy(dtype=float)
    y_all = df["price"].to_numpy(dtype=float)
    x = t_all[mask.to_numpy()]
    y = y_all[mask.to_numpy()]
    b, a = np.polyfit(x, y, 1)
    line = np.full(len(df), np.nan)
    line[mask.to_numpy()] = a + b * t_all[mask.to_numpy()]
    return pd.Series(line, index=df.index)


def pct(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def plot_rolling_vs_fixed_log(label: str, desc: str, df: pd.DataFrame) -> dict:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fixed5, cagr5 = fixed_log_trend(df, 5)
    fixed10, cagr10 = fixed_log_trend(df, 10)
    recent = df[df["date"] >= df["date"].iloc[-1] - pd.DateOffset(years=10)].copy()

    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    ax.plot(recent["date"], recent["price"], lw=1.15, color=COLORS["price"], label="price")
    ax.plot(recent["date"], recent["trend_10y"], lw=1.8, color=COLORS["roll10"], label="rolling 10Y log trend")
    ax.plot(recent["date"], recent["trend_5y"], lw=1.8, color=COLORS["roll5"], label="rolling 5Y log trend")
    ax.plot(
        recent["date"],
        fixed10.loc[recent.index],
        lw=1.4,
        color=COLORS["fixed10"],
        ls="--",
        alpha=0.7,
        label=f"fixed latest-10Y log line ({cagr10 * 100:.1f}%/yr)",
    )
    ax.plot(
        recent["date"],
        fixed5.loc[recent.index],
        lw=1.4,
        color=COLORS["fixed5"],
        ls="--",
        alpha=0.7,
        label=f"fixed latest-5Y log line ({cagr5 * 100:.1f}%/yr)",
    )
    ax.set_title(f"{label} - rolling curve vs fixed log-straight line converted to price ({desc})")
    ax.set_ylabel("adjusted close")
    ax.grid(True, alpha=0.15)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / f"{label}_rolling_vs_fixed_log.png", dpi=130)
    plt.close(fig)

    last = df.iloc[-1]
    return {
        "ticker": label,
        "price": float(last["price"]),
        "rolling_5y": float(last["trend_5y"]),
        "fixed_5y": float(fixed5.iloc[-1]),
        "rolling_10y": float(last["trend_10y"]),
        "fixed_10y": float(fixed10.iloc[-1]),
        "fixed_5y_cagr": cagr5,
        "fixed_10y_cagr": cagr10,
    }


def plot_price_linear_vs_log(label: str, desc: str, df: pd.DataFrame) -> dict:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fixed_log5, log_cagr5 = fixed_log_trend(df, 5)
    linear5 = fixed_price_linear(df, 5)
    recent = df[df["date"] >= df["date"].iloc[-1] - pd.DateOffset(years=5)].copy()

    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    ax.plot(recent["date"], recent["price"], lw=1.15, color=COLORS["price"], label="price")
    ax.plot(recent["date"], recent["trend_5y"], lw=1.9, color=COLORS["roll5"], label="rolling 5Y log trend")
    ax.plot(
        recent["date"],
        fixed_log5.loc[recent.index],
        lw=1.45,
        color="#7c3aed",
        ls="--",
        label="fixed 5Y log line converted to price",
    )
    ax.plot(
        recent["date"],
        linear5.loc[recent.index],
        lw=1.45,
        color=COLORS["linear"],
        ls="-.",
        label="literal 5Y price straight line",
    )
    ax.set_title(f"{label} - log trend vs literal price straight line ({desc})")
    ax.set_ylabel("adjusted close")
    ax.grid(True, alpha=0.15)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / f"{label}_log_vs_price_straight.png", dpi=130)
    plt.close(fig)

    last = df.iloc[-1]
    return {
        "ticker": label,
        "price": float(last["price"]),
        "rolling_5y": float(last["trend_5y"]),
        "fixed_log_5y": float(fixed_log5.iloc[-1]),
        "price_linear_5y": float(linear5.iloc[-1]),
        "price_vs_rolling_5y": float(last["price"] / last["trend_5y"] - 1),
        "price_vs_price_linear_5y": float(last["price"] / linear5.iloc[-1] - 1),
        "fixed_log_5y_cagr": log_cagr5,
    }


def plot_dashboard(rows: list[dict]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    labels = [r["ticker"] for r in rows]
    x = np.arange(len(labels))
    vs_roll = [r["price_vs_rolling_5y"] * 100 for r in rows]
    vs_lin = [r["price_vs_price_linear_5y"] * 100 for r in rows]

    fig, ax = plt.subplots(figsize=(11, 5.2))
    width = 0.38
    ax.bar(x - width / 2, vs_roll, width, color=COLORS["roll5"], label="price vs rolling 5Y log trend")
    ax.bar(x + width / 2, vs_lin, width, color=COLORS["linear"], label="price vs literal 5Y price line")
    ax.axhline(0, color="#555555", lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("current deviation %")
    ax.set_title("Current deviation: log-compound trend vs literal price-straight line")
    ax.grid(axis="y", alpha=0.15)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "current_deviation_log_vs_price_line.png", dpi=130)
    plt.close(fig)


def main() -> int:
    fixed_rows = []
    linear_rows = []
    for label, desc in ASSETS:
        price_df = load_price(label)
        roll_df = load_rolling(label)
        df = price_df.merge(roll_df.drop(columns=["price"]), on="date", how="left")
        fixed_rows.append(plot_rolling_vs_fixed_log(label, desc, df))
        linear_rows.append(plot_price_linear_vs_log(label, desc, df))

    plot_dashboard(linear_rows)
    pd.DataFrame(fixed_rows).to_csv(OUT / "rolling_vs_fixed_log_latest.csv", index=False)
    pd.DataFrame(linear_rows).to_csv(OUT / "log_vs_price_straight_latest.csv", index=False)

    lines = [
        "# Line Comparison Review",
        "",
        "Two comparisons are included:",
        "",
        "1. `rolling_vs_fixed_log`: solid lines are rolling 5Y/10Y log trends; dashed lines are",
        "   the latest fixed-window log-straight line converted back into real price.",
        "2. `log_vs_price_straight`: rolling 5Y log trend versus a literal straight line in",
        "   normal price space.",
        "",
        "Important: rolling and fixed log lines share the same final value because the final",
        "day uses the same latest 5Y/10Y window. The historical path is what differs.",
        "",
        "## Current 5Y Comparison",
        "",
        "| ticker | price | rolling 5Y log trend | price-straight 5Y line | vs rolling | vs price-straight |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for r in linear_rows:
        lines.append(
            f"| {r['ticker']} | ${r['price']:,.2f} | ${r['rolling_5y']:,.2f} | "
            f"${r['price_linear_5y']:,.2f} | {pct(r['price_vs_rolling_5y'])} | "
            f"{pct(r['price_vs_price_linear_5y'])} |"
        )

    lines += [
        "",
        "## Files",
        "",
        "- `<TICKER>_rolling_vs_fixed_log.png`",
        "- `<TICKER>_log_vs_price_straight.png`",
        "- `current_deviation_log_vs_price_line.png`",
        "- `rolling_vs_fixed_log_latest.csv`",
        "- `log_vs_price_straight_latest.csv`",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(pd.DataFrame(linear_rows)[[
        "ticker",
        "price",
        "rolling_5y",
        "price_linear_5y",
        "price_vs_rolling_5y",
        "price_vs_price_linear_5y",
    ]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
