#!/usr/bin/env python
"""Rolling log-trend review for cross-asset checks such as SPY and gold."""
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
OUT = ROOT / "macro" / "market_panel" / "log_trend" / "cross_asset_review"
OUT.mkdir(parents=True, exist_ok=True)

ASSETS = [
    ("SPY", "S&P 500 ETF, adjusted close"),
    ("GOLD", "Gold futures GC=F"),
]

WINDOWS = {"5y": 5, "10y": 10}
COLORS = {"price": "#1a1d21", "5y": "#16a34a", "10y": "#2563eb"}


def load(label: str) -> pd.DataFrame:
    df = pd.read_csv(PANEL / f"{label}.csv")
    cols = list(df.columns)
    df = df.rename(columns={cols[0]: "date", cols[1]: "price"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["price"]).sort_values("date").reset_index(drop=True)
    df = df[df["price"] > 0].reset_index(drop=True)
    return df


def rolling_fit(df: pd.DataFrame, years: int) -> pd.DataFrame:
    dates = df["date"]
    t_all = (dates - dates.iloc[0]).dt.days.to_numpy(dtype=float)
    y_all = np.log(df["price"].to_numpy(dtype=float))
    price = df["price"].to_numpy(dtype=float)

    trend = np.full(len(df), np.nan)
    cagr = np.full(len(df), np.nan)
    dev_pct = np.full(len(df), np.nan)
    dev_sigma = np.full(len(df), np.nan)

    min_date = dates.iloc[0] + pd.DateOffset(years=years)
    for i, current_date in enumerate(dates):
        if current_date < min_date:
            continue
        cutoff = current_date - pd.DateOffset(years=years)
        start = int(dates.searchsorted(cutoff, side="left"))
        end = i + 1
        if end - start < max(252, years * 180):
            continue

        x = t_all[start:end]
        y = y_all[start:end]
        b, a = np.polyfit(x, y, 1)
        fit = a + b * x
        resid = y - fit
        sigma = float(resid.std(ddof=1))
        today_fit = a + b * t_all[i]
        today_trend = math.exp(today_fit)

        trend[i] = today_trend
        cagr[i] = math.exp(b * 365.25) - 1.0
        dev_pct[i] = price[i] / today_trend - 1.0
        dev_sigma[i] = (y_all[i] - today_fit) / sigma if sigma else np.nan

    return pd.DataFrame({
        "date": dates,
        f"trend_{years}y": trend,
        f"cagr_{years}y": cagr,
        f"dev_pct_{years}y": dev_pct,
        f"dev_sigma_{years}y": dev_sigma,
    })


def pct(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def cagr_text(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:.1f}%"


def scenario_ann_return(price: float, trend: float, trend_cagr: float, years: int) -> float:
    future_trend = trend * ((1.0 + trend_cagr) ** years)
    total = future_trend / price - 1.0
    return (1.0 + total) ** (1.0 / years) - 1.0


def plot_asset(label: str, desc: str, df: pd.DataFrame) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax, ax_dev) = plt.subplots(
        2,
        1,
        figsize=(12.5, 7.2),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.1]},
    )
    ax.plot(df["date"], df["price"], lw=1.15, color=COLORS["price"], label=f"{label} price")
    for key in ["10y", "5y"]:
        ax.plot(df["date"], df[f"trend_{key}"], lw=1.7, color=COLORS[key], label=f"rolling {key} log trend")
        last = df.dropna(subset=[f"trend_{key}"]).tail(1)
        if not last.empty:
            ax.annotate(
                f" {key}",
                (last["date"].iloc[0], last[f"trend_{key}"].iloc[0]),
                color=COLORS[key],
                fontsize=9,
                va="center",
            )

    last_price = float(df["price"].iloc[-1])
    last_date = df["date"].iloc[-1]
    ax.scatter([last_date], [last_price], color="#dc2626", s=34, zorder=5)
    ax.annotate(f" {last_price:,.2f}", (last_date, last_price), color="#dc2626", va="center")
    ax.set_title(f"{label} - rolling log trend ({desc})")
    ax.set_ylabel("price / adjusted close")
    ax.grid(True, alpha=0.16)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    for key in ["10y", "5y"]:
        ax_dev.plot(df["date"], df[f"dev_pct_{key}"] * 100, lw=1.25, color=COLORS[key], label=f"vs rolling {key}")
    ax_dev.axhline(0, color="#555555", lw=0.85)
    ax_dev.axhline(20, color="#b91c1c", lw=0.75, ls="--", alpha=0.45)
    ax_dev.axhline(-20, color="#0f766e", lw=0.75, ls="--", alpha=0.45)
    ax_dev.set_ylabel("deviation %")
    ax_dev.grid(True, alpha=0.14)
    ax_dev.legend(loc="upper left", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(OUT / f"{label}_rolling_log_trend.png", dpi=130)
    plt.close(fig)


def plot_dashboard(results: dict[str, pd.DataFrame]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(15, 5.6), sharex=False)
    for ax, (label, desc) in zip(axes, ASSETS):
        df = results[label]
        recent = df[df["date"] >= df["date"].iloc[-1] - pd.DateOffset(years=10)]
        last = df.iloc[-1]
        ax.plot(recent["date"], recent["price"], lw=1.1, color=COLORS["price"], label="price")
        ax.plot(recent["date"], recent["trend_10y"], lw=1.5, color=COLORS["10y"], label="10y")
        ax.plot(recent["date"], recent["trend_5y"], lw=1.5, color=COLORS["5y"], label="5y")
        ax.set_title(f"{label}: 5Y {pct(last['dev_pct_5y'])}, 10Y {pct(last['dev_pct_10y'])}", fontsize=10)
        ax.grid(True, alpha=0.14)
        ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.suptitle("SPY and Gold - rolling log trend review", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT / "spy_gold_rolling_dashboard.png", dpi=130)
    plt.close(fig)


def main() -> int:
    latest_rows = []
    scenario_rows = []
    results: dict[str, pd.DataFrame] = {}

    for label, desc in ASSETS:
        base = load(label)
        df = base.copy()
        for _, years in WINDOWS.items():
            df = df.merge(rolling_fit(base, years), on="date", how="left")

        df.to_csv(OUT / f"{label}_rolling_log_trend.csv", index=False)
        plot_asset(label, desc, df)
        results[label] = df

        last = df.iloc[-1]
        row = {
            "ticker": label,
            "description": desc,
            "last_date": last["date"].date().isoformat(),
            "price": float(last["price"]),
            "trend_5y": float(last["trend_5y"]),
            "dev_pct_5y": float(last["dev_pct_5y"]),
            "cagr_5y": float(last["cagr_5y"]),
            "trend_10y": float(last["trend_10y"]),
            "dev_pct_10y": float(last["dev_pct_10y"]),
            "cagr_10y": float(last["cagr_10y"]),
        }
        latest_rows.append(row)

        for key in ["5y", "10y"]:
            for horizon in [1, 2, 3]:
                scenario_rows.append({
                    "ticker": label,
                    "trend_window": key,
                    "horizon_years": horizon,
                    "annualized_return_if_revert_to_trend": scenario_ann_return(
                        float(last["price"]),
                        float(last[f"trend_{key}"]),
                        float(last[f"cagr_{key}"]),
                        horizon,
                    ),
                })

    plot_dashboard(results)
    latest = pd.DataFrame(latest_rows)
    scenarios = pd.DataFrame(scenario_rows)
    latest.to_csv(OUT / "spy_gold_latest.csv", index=False)
    scenarios.to_csv(OUT / "spy_gold_reversion_scenarios.csv", index=False)

    lines = [
        "# SPY and Gold Rolling Log-Trend Review",
        "",
        "Source series:",
        "",
        "- `SPY`: Yahoo Finance adjusted close, dividend-adjusted.",
        "- `GOLD`: Yahoo Finance `GC=F` gold futures series from `macro/market_panel/data/GOLD.csv`.",
        "",
        "## Latest",
        "",
        "| ticker | date | price | rolling 5Y trend | vs 5Y | 5Y CAGR | rolling 10Y trend | vs 10Y | 10Y CAGR |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in latest.iterrows():
        lines.append(
            f"| {r['ticker']} | {r['last_date']} | {r['price']:,.2f} | {r['trend_5y']:,.2f} | "
            f"{pct(r['dev_pct_5y'])} | {cagr_text(r['cagr_5y'])} | {r['trend_10y']:,.2f} | "
            f"{pct(r['dev_pct_10y'])} | {cagr_text(r['cagr_10y'])} |"
        )

    lines += [
        "",
        "## Reversion Math",
        "",
        "| ticker | trend | 1Y | 2Y ann. | 3Y ann. |",
        "|---|---|---:|---:|---:|",
    ]
    for label, _ in ASSETS:
        for key in ["5y", "10y"]:
            sc = scenarios[(scenarios["ticker"] == label) & (scenarios["trend_window"] == key)]
            vals = {int(r["horizon_years"]): float(r["annualized_return_if_revert_to_trend"]) for _, r in sc.iterrows()}
            lines.append(f"| {label} | rolling {key} | {pct(vals[1])} | {pct(vals[2])} | {pct(vals[3])} |")

    lines += [
        "",
        "## Files",
        "",
        "- `spy_gold_rolling_dashboard.png`",
        "- `SPY_rolling_log_trend.png`",
        "- `GOLD_rolling_log_trend.png`",
        "- `spy_gold_latest.csv`",
        "- `spy_gold_reversion_scenarios.csv`",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(latest[["ticker", "last_date", "price", "trend_5y", "dev_pct_5y", "cagr_5y", "trend_10y", "dev_pct_10y", "cagr_10y"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
