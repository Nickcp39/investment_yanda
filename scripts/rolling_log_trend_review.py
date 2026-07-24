#!/usr/bin/env python
"""Rolling log-trend review charts.

For each date, fit ln(price) = a + b * time using only the previous 5y or 10y
of data, then convert the fitted value back into real price space:

    rolling_trend_today = exp(a + b * today)

This makes the trend line itself bend over time as the market regime changes.
It is intended as a review artifact before promoting the signal into the common
indicator panel.
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
OUT = ROOT / "macro" / "market_panel" / "log_trend" / "rolling_review"
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
    n_obs = np.zeros(len(df), dtype=int)

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
        current_trend = math.exp(a + b * t_all[i])
        trend[i] = current_trend
        cagr[i] = math.exp(b * 365.25) - 1.0
        dev_pct[i] = price[i] / current_trend - 1.0
        dev_sigma[i] = (y_all[i] - (a + b * t_all[i])) / sigma if sigma else np.nan
        n_obs[i] = end - start

    return pd.DataFrame({
        "date": dates,
        f"trend_{years}y": trend,
        f"cagr_{years}y": cagr,
        f"dev_pct_{years}y": dev_pct,
        f"dev_sigma_{years}y": dev_sigma,
        f"n_{years}y": n_obs,
    })


def pct(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:+.1f}%"


def cagr_text(x: float) -> str:
    if not math.isfinite(float(x)):
        return "n/a"
    return f"{x * 100:.1f}%"


def scenario_return(price: float, trend: float, trend_cagr: float, years: int) -> float:
    future_trend = trend * ((1.0 + trend_cagr) ** years)
    return future_trend / price - 1.0


def scenario_ann_return(price: float, trend: float, trend_cagr: float, years: int) -> float:
    total = scenario_return(price, trend, trend_cagr, years)
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
        ax.plot(
            df["date"],
            df[f"trend_{key}"],
            lw=1.7,
            color=COLORS[key],
            label=f"rolling {key} log trend (real price)",
        )
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
    ax.set_title(f"{label} - rolling log trend converted back to price ({desc})")
    ax.set_ylabel("adjusted close")
    ax.grid(True, alpha=0.16)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    for key in ["10y", "5y"]:
        ax_dev.plot(
            df["date"],
            df[f"dev_pct_{key}"] * 100,
            lw=1.25,
            color=COLORS[key],
            label=f"price vs rolling {key}",
        )
    ax_dev.axhline(0, color="#555555", lw=0.85)
    ax_dev.axhline(20, color="#b91c1c", lw=0.75, ls="--", alpha=0.45)
    ax_dev.axhline(-20, color="#0f766e", lw=0.75, ls="--", alpha=0.45)
    ax_dev.set_ylabel("deviation %")
    ax_dev.grid(True, alpha=0.14)
    ax_dev.legend(loc="upper left", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(OUT / f"{label}_rolling_log_trend.png", dpi=130)
    plt.close(fig)


def plot_focus_dashboard(results: dict[str, pd.DataFrame]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    focus = ["QQQ", "GOOG", "MSFT", "AAPL", "NVDA", "AMZN"]
    fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharex=False)
    axes = axes.reshape(-1)

    for ax, label in zip(axes, focus):
        df = results[label]
        recent = df[df["date"] >= df["date"].iloc[-1] - pd.DateOffset(years=5)]
        ax.plot(recent["date"], recent["price"], lw=1.15, color=COLORS["price"], label="price")
        ax.plot(recent["date"], recent["trend_10y"], lw=1.5, color=COLORS["10y"], label="rolling 10y")
        ax.plot(recent["date"], recent["trend_5y"], lw=1.5, color=COLORS["5y"], label="rolling 5y")
        last = df.iloc[-1]
        ax.set_title(
            f"{label}: vs 5Y {pct(last['dev_pct_5y'])}, vs 10Y {pct(last['dev_pct_10y'])}",
            fontsize=10,
        )
        ax.grid(True, alpha=0.14)
        ax.legend(loc="upper left", fontsize=8, frameon=False)

    fig.suptitle("Rolling log trend review - recent 5Y view", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.98])
    fig.savefig(OUT / "rolling_log_trend_focus_dashboard.png", dpi=130)
    plt.close(fig)


def main() -> int:
    rows = []
    scenario_rows = []
    results: dict[str, pd.DataFrame] = {}

    for label, desc in ASSETS:
        base = load(label)
        df = base.copy()
        for _, years in WINDOWS.items():
            fit = rolling_fit(base, years)
            df = df.merge(fit, on="date", how="left")

        df["date_out"] = df["date"].dt.date
        df.drop(columns=["date_out"]).to_csv(OUT / f"{label}_rolling_log_trend.csv", index=False)
        plot_asset(label, desc, df)
        results[label] = df

        last = df.iloc[-1]
        row = {
            "ticker": label,
            "description": desc,
            "last_date": last["date"].date().isoformat(),
            "price": float(last["price"]),
        }
        for key in ["5y", "10y"]:
            row[f"trend_{key}"] = float(last[f"trend_{key}"])
            row[f"cagr_{key}"] = float(last[f"cagr_{key}"])
            row[f"dev_pct_{key}"] = float(last[f"dev_pct_{key}"])
            row[f"dev_sigma_{key}"] = float(last[f"dev_sigma_{key}"])
        rows.append(row)

        for key in ["5y", "10y"]:
            trend = float(last[f"trend_{key}"])
            cg = float(last[f"cagr_{key}"])
            for horizon in [1, 2, 3]:
                scenario_rows.append({
                    "ticker": label,
                    "trend_window": key,
                    "horizon_years": horizon,
                    "price_today": float(last["price"]),
                    "trend_today": trend,
                    "trend_cagr": cg,
                    "future_trend_price": trend * ((1.0 + cg) ** horizon),
                    "total_return_if_revert_to_trend": scenario_return(float(last["price"]), trend, cg, horizon),
                    "annualized_return_if_revert_to_trend": scenario_ann_return(float(last["price"]), trend, cg, horizon),
                })

    plot_focus_dashboard(results)

    latest = pd.DataFrame(rows)
    scenarios = pd.DataFrame(scenario_rows)
    latest.to_csv(OUT / "rolling_log_trend_latest.csv", index=False)
    scenarios.to_csv(OUT / "rolling_log_trend_reversion_scenarios.csv", index=False)

    latest_sorted = latest.sort_values("dev_pct_5y", ascending=False)
    lines = [
        "# Rolling Log-Trend Review",
        "",
        "This is the review version of the trend-line indicator. Each date uses only",
        "the previous 5Y or 10Y of prices, fits `ln(price)=a+b*time`, then converts",
        "the fitted value back into real price space with `exp(a+b*time)`.",
        "",
        "This makes the trend line itself bend when the regime changes.",
        "",
        "## Latest",
        "",
        "| ticker | price | rolling 5Y trend | vs 5Y | 5Y trend CAGR | rolling 10Y trend | vs 10Y | 10Y trend CAGR |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in latest_sorted.iterrows():
        lines.append(
            f"| {r['ticker']} | ${r['price']:,.2f} | ${r['trend_5y']:,.2f} | "
            f"{pct(r['dev_pct_5y'])} | {cagr_text(r['cagr_5y'])} | "
            f"${r['trend_10y']:,.2f} | {pct(r['dev_pct_10y'])} | {cagr_text(r['cagr_10y'])} |"
        )

    focus = latest[latest["ticker"].isin(["QQQ", "GOOG", "MSFT"])].set_index("ticker")
    lines += [
        "",
        "## Reversion Math",
        "",
        "If price returns to the current rolling trend line after H years, the return is:",
        "",
        "`future_trend = trend_today * (1 + trend_cagr)^H`",
        "",
        "`return = future_trend / price_today - 1`",
        "",
        "| ticker | trend | 1Y revert | 2Y revert ann. | 3Y revert ann. |",
        "|---|---|---:|---:|---:|",
    ]
    for label in ["QQQ", "GOOG", "MSFT"]:
        for key in ["5y", "10y"]:
            sc = scenarios[(scenarios["ticker"] == label) & (scenarios["trend_window"] == key)]
            one = sc[sc["horizon_years"] == 1]["total_return_if_revert_to_trend"].iloc[0]
            two = sc[sc["horizon_years"] == 2]["annualized_return_if_revert_to_trend"].iloc[0]
            three = sc[sc["horizon_years"] == 3]["annualized_return_if_revert_to_trend"].iloc[0]
            lines.append(f"| {label} | rolling {key} | {pct(one)} | {pct(two)} | {pct(three)} |")

    lines += [
        "",
        "## Files",
        "",
        "- `rolling_log_trend_focus_dashboard.png` - recent 5Y review dashboard.",
        "- `<TICKER>_rolling_log_trend.png` - full chart with rolling 5Y/10Y trend and deviation.",
        "- `<TICKER>_rolling_log_trend.csv` - daily rolling trend values.",
        "- `rolling_log_trend_latest.csv` - current readings.",
        "- `rolling_log_trend_reversion_scenarios.csv` - 1Y/2Y/3Y trend-reversion return math.",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(latest_sorted[["ticker", "price", "trend_5y", "dev_pct_5y", "cagr_5y", "trend_10y", "dev_pct_10y", "cagr_10y"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
