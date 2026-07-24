#!/usr/bin/env python
"""Rolling log-trend review for essential-consumption / life-necessity leaders."""
from __future__ import annotations

import datetime as dt
import json
import math
import sys
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "macro" / "market_panel" / "log_trend" / "consumer_leaders_review"
DATA = OUT / "data"
OUT.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (consumer-leaders-log-trend-review)"}

ASSETS = [
    ("KO", "Coca-Cola", "beverages"),
    ("PEP", "PepsiCo", "snacks + beverages"),
    ("PG", "Procter & Gamble", "household/personal care"),
    ("WMT", "Walmart", "essential retail"),
    ("COST", "Costco", "warehouse retail"),
    ("MCD", "McDonald's", "quick-service restaurant"),
    ("CL", "Colgate-Palmolive", "oral/personal care"),
    ("KMB", "Kimberly-Clark", "paper/personal care"),
    ("JNJ", "Johnson & Johnson", "healthcare staples"),
    ("PM", "Philip Morris", "nicotine"),
]

WINDOWS = {"5y": 5, "10y": 10}
COLORS = {"price": "#1a1d21", "5y": "#16a34a", "10y": "#2563eb"}


def _epoch(d: str) -> int:
    return int(time.mktime(dt.datetime.strptime(d, "%Y-%m-%d").timetuple()))


def fetch_yahoo(symbol: str, start: str, end: str) -> pd.DataFrame:
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(symbol, safe='^=.-')}"
        f"?period1={_epoch(start)}&period2={_epoch(end)}&interval=1d"
        f"&events=div%2Csplits&includeAdjustedClose=true"
    )
    with urlopen(Request(url, headers=UA), timeout=30) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    ts = res["timestamp"]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
    close = res["indicators"]["quote"][0].get("close")
    vals = adj if adj else close
    dates = [dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d") for t in ts]
    df = pd.DataFrame({"date": pd.to_datetime(dates), "price": vals})
    df = df.dropna(subset=["price"]).drop_duplicates(subset=["date"], keep="last")
    df = df[df["price"] > 0].sort_values("date").reset_index(drop=True)
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


def plot_asset(label: str, name: str, theme: str, df: pd.DataFrame) -> None:
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
    ax.set_title(f"{label} - rolling log trend ({name}; {theme})")
    ax.set_ylabel("adjusted close")
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

    ncols = 2
    nrows = math.ceil(len(ASSETS) / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(14, 4.1 * nrows))
    axes = np.array(axes).reshape(-1)

    for ax, (label, name, _) in zip(axes, ASSETS):
        df = results[label]
        recent = df[df["date"] >= df["date"].iloc[-1] - pd.DateOffset(years=10)]
        last = df.iloc[-1]
        ax.plot(recent["date"], recent["price"], lw=1.05, color=COLORS["price"], label="price")
        ax.plot(recent["date"], recent["trend_10y"], lw=1.45, color=COLORS["10y"], label="10y")
        ax.plot(recent["date"], recent["trend_5y"], lw=1.45, color=COLORS["5y"], label="5y")
        ax.set_title(
            f"{label}: 5Y {pct(last['dev_pct_5y'])}, 10Y {pct(last['dev_pct_10y'])}",
            fontsize=10,
        )
        ax.grid(True, alpha=0.14)
        ax.legend(loc="upper left", fontsize=8, frameon=False)

    for ax in axes[len(ASSETS):]:
        ax.axis("off")

    fig.suptitle("Consumer / life-necessity leaders - rolling log trend review", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.985])
    fig.savefig(OUT / "consumer_leaders_rolling_dashboard.png", dpi=130)
    plt.close(fig)


def main() -> int:
    end = (dt.date.today() + dt.timedelta(days=1)).isoformat()
    start = "2010-01-01"
    latest_rows = []
    scenario_rows = []
    results: dict[str, pd.DataFrame] = {}

    for label, name, theme in ASSETS:
        base = fetch_yahoo(label, start, end)
        base.to_csv(DATA / f"{label}.csv", index=False)

        df = base.copy()
        for _, years in WINDOWS.items():
            df = df.merge(rolling_fit(base, years), on="date", how="left")
        df.to_csv(OUT / f"{label}_rolling_log_trend.csv", index=False)
        plot_asset(label, name, theme, df)
        results[label] = df

        last = df.iloc[-1]
        row = {
            "ticker": label,
            "name": name,
            "theme": theme,
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
    latest.to_csv(OUT / "consumer_leaders_latest.csv", index=False)
    scenarios.to_csv(OUT / "consumer_leaders_reversion_scenarios.csv", index=False)

    latest_sorted = latest.sort_values("dev_pct_5y", ascending=False)
    lines = [
        "# Consumer Leaders Rolling Log-Trend Review",
        "",
        "Review universe: KO, PEP, PG, WMT, COST, MCD, CL, KMB, JNJ, PM.",
        "Source: Yahoo Finance chart API adjusted close. This is a review artifact, not a promoted indicator yet.",
        "",
        f"Built through {latest['last_date'].max()}.",
        "",
        "## Latest",
        "",
        "| ticker | name | price | vs 5Y | 5Y CAGR | vs 10Y | 10Y CAGR |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for _, r in latest_sorted.iterrows():
        lines.append(
            f"| {r['ticker']} | {r['name']} | ${r['price']:,.2f} | "
            f"{pct(r['dev_pct_5y'])} | {cagr_text(r['cagr_5y'])} | "
            f"{pct(r['dev_pct_10y'])} | {cagr_text(r['cagr_10y'])} |"
        )

    lines += [
        "",
        "## 1Y/2Y/3Y Annualized Return If Price Reverts To Trend",
        "",
        "| ticker | trend | 1Y | 2Y ann. | 3Y ann. |",
        "|---|---|---:|---:|---:|",
    ]
    for label, _, _ in ASSETS:
        for key in ["5y", "10y"]:
            sc = scenarios[(scenarios["ticker"] == label) & (scenarios["trend_window"] == key)]
            vals = {int(r["horizon_years"]): float(r["annualized_return_if_revert_to_trend"]) for _, r in sc.iterrows()}
            lines.append(f"| {label} | rolling {key} | {pct(vals[1])} | {pct(vals[2])} | {pct(vals[3])} |")

    lines += [
        "",
        "## Files",
        "",
        "- `consumer_leaders_rolling_dashboard.png`",
        "- `<TICKER>_rolling_log_trend.png`",
        "- `<TICKER>_rolling_log_trend.csv`",
        "- `consumer_leaders_latest.csv`",
        "- `consumer_leaders_reversion_scenarios.csv`",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT}")
    print(latest_sorted[["ticker", "price", "dev_pct_5y", "cagr_5y", "dev_pct_10y", "cagr_10y"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
