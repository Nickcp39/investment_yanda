#!/usr/bin/env python
"""Common log-linear trend indicators for QQQ and mega-cap tech.

Idea:
  On a log price scale, constant compound growth is a straight line. Fit:
      ln(price) = a + b * t
  Then:
      trend price = exp(a + b * t)
      trend CAGR  = exp(b * 365.25) - 1

This is intentionally shown across several windows because one full-history line
can be misleading when the monetary/liquidity regime changes. Read the 5y and
10y rows first; keep the full-history fit as context.

Inputs : macro/market_panel/data/<TICKER>.csv
Outputs: macro/market_panel/log_trend/<TICKER>_channel.csv
         macro/market_panel/log_trend/<TICKER>_log_trend.png
         macro/market_panel/log_trend/common_log_trend_summary.csv
         macro/market_panel/log_trend/summary.md
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
OUT = ROOT / "macro" / "market_panel" / "log_trend"
OUT.mkdir(parents=True, exist_ok=True)

ASSETS = [
    ("QQQ", "Nasdaq-100 ETF"),
    ("SPY", "S&P 500 ETF"),
    ("MSFT", "Microsoft"),
    ("GOOG", "Alphabet Class C"),
    ("GOOGL", "Alphabet Class A"),
    ("AAPL", "Apple"),
    ("NVDA", "Nvidia"),
    ("AMZN", "Amazon"),
    ("META", "Meta"),
    ("TSLA", "Tesla"),
]

WINDOWS = {
    "full": None,
    "10y": 10,
    "5y": 5,
}

TREND_COLORS = {
    "full": "#9aa0a6",
    "10y": "#1f77b4",
    "5y": "#2ca02c",
}


def load(label: str) -> pd.DataFrame:
    path = PANEL / f"{label}.csv"
    if not path.exists():
        raise FileNotFoundError(path)

    df = pd.read_csv(path)
    cols = list(df.columns)
    df = df.rename(columns={cols[0]: "date", cols[1]: "value"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["value"]).sort_values("date").reset_index(drop=True)
    df = df[df["value"] > 0]
    return df.reset_index(drop=True)


def fit_window(df: pd.DataFrame, years: int | None) -> dict:
    """OLS of ln(price) on calendar days for one window."""
    t_all = (df["date"] - df["date"].iloc[0]).dt.days.values.astype(float)
    y_all = np.log(df["value"].values)

    if years is None:
        mask = np.ones(len(df), bool)
    else:
        cutoff = df["date"].iloc[-1] - pd.DateOffset(years=years)
        mask = (df["date"] >= cutoff).values

    t = t_all[mask]
    y = y_all[mask]
    if len(t) < 30:
        raise ValueError("not enough observations for regression")

    b, a = np.polyfit(t, y, 1)
    fit_log = a + b * t
    resid = y - fit_log
    sigma = float(resid.std(ddof=1))

    trend_all_log = a + b * t_all
    current_trend = float(math.exp(trend_all_log[-1]))
    current_price = float(df["value"].iloc[-1])
    cur_dev_log = float(y_all[-1] - trend_all_log[-1])

    return {
        "a": float(a),
        "b": float(b),
        "sigma": sigma,
        "cagr": math.exp(b * 365.25) - 1.0,
        "cur_dev_log": cur_dev_log,
        "cur_dev_pct": current_price / current_trend - 1.0,
        "cur_sigma": cur_dev_log / sigma if sigma else float("nan"),
        "current_trend": current_trend,
        "n": int(mask.sum()),
        "mask": mask,
        "t_all": t_all,
        "y_all": y_all,
        "trend_all_log": trend_all_log,
    }


def verdict(sig: float) -> str:
    if sig > 2:
        return "overheated (>+2 sigma)"
    if sig > 1:
        return "hot (+1..+2 sigma)"
    if sig < -2:
        return "broken/cheap (<-2 sigma)"
    if sig < -1:
        return "cool (-1..-2 sigma)"
    return "normal (+/-1 sigma)"


def trailing_growth(df: pd.DataFrame, days: int = 252) -> float:
    if len(df) <= days:
        return float("nan")
    return float(df["value"].iloc[-1] / df["value"].iloc[-1 - days] - 1.0)


def pct(x: float) -> str:
    if not math.isfinite(x):
        return "n/a"
    return f"{x * 100:+.1f}%"


def cagr(x: float) -> str:
    if not math.isfinite(x):
        return "n/a"
    return f"{x * 100:.1f}%"


def make_channel(df: pd.DataFrame, fits: dict[str, dict]) -> pd.DataFrame:
    full = fits["full"]
    t_all = full["t_all"]
    y_all = full["y_all"]
    full_trend = full["trend_all_log"]
    full_sigma = full["sigma"]

    chan = pd.DataFrame({
        "date": df["date"].dt.date,
        "price": df["value"].values,
        # Legacy columns used by earlier experiments.
        "trend": np.exp(full_trend),
        "minus1sd": np.exp(full_trend - full_sigma),
        "plus1sd": np.exp(full_trend + full_sigma),
        "minus2sd": np.exp(full_trend - 2 * full_sigma),
        "plus2sd": np.exp(full_trend + 2 * full_sigma),
        "dev_sigma": (y_all - full_trend) / full_sigma,
    })

    for name, fit in fits.items():
        trend = np.exp(fit["trend_all_log"])
        sigma = fit["sigma"]
        mask = fit["mask"]
        chan[f"trend_{name}"] = np.where(mask, trend, np.nan)
        chan[f"dev_pct_{name}"] = np.where(mask, df["value"].values / trend - 1.0, np.nan)
        chan[f"dev_sigma_{name}"] = np.where(
            mask,
            (np.log(df["value"].values) - fit["trend_all_log"]) / sigma,
            np.nan,
        )

    return chan


def plot_asset(label: str, desc: str, df: pd.DataFrame, fits: dict[str, dict]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    last_date = df["date"].iloc[-1]
    price = float(df["value"].iloc[-1])

    fig, (ax, ax_dev) = plt.subplots(
        2,
        1,
        figsize=(12.5, 7.5),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.0]},
    )

    ax.set_yscale("log")
    ax.plot(df["date"], df["value"], lw=1.15, color="#1a1d21", label=f"{label} price")

    for name in ["full", "10y", "5y"]:
        fit = fits[name]
        trend = np.exp(fit["trend_all_log"])
        trend = np.where(fit["mask"], trend, np.nan)
        linestyle = "--" if name == "full" else "-"
        alpha = 0.65 if name == "full" else 0.95
        ax.plot(
            df["date"],
            trend,
            lw=1.6,
            ls=linestyle,
            color=TREND_COLORS[name],
            alpha=alpha,
            label=f"{name} trend ({cagr(fit['cagr'])}/yr)",
        )

        valid = np.where(np.isfinite(trend))[0]
        if len(valid):
            i = valid[-1]
            ax.annotate(
                f" {name}",
                (df["date"].iloc[i], trend[i]),
                color=TREND_COLORS[name],
                fontsize=9,
                va="center",
            )

    ax.scatter([last_date], [price], color="#d62728", s=34, zorder=5)
    ax.annotate(
        f" {price:,.2f}",
        (last_date, price),
        color="#d62728",
        fontsize=9,
        va="center",
    )
    ax.set_title(f"{label} - log trend lines ({desc})")
    ax.set_ylabel("adjusted close, log scale")
    ax.grid(True, which="both", alpha=0.16)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    for name in ["10y", "5y"]:
        fit = fits[name]
        trend = np.exp(fit["trend_all_log"])
        dev = df["value"].values / trend - 1.0
        dev = np.where(fit["mask"], dev, np.nan)
        ax_dev.plot(
            df["date"],
            dev * 100,
            lw=1.25,
            color=TREND_COLORS[name],
            label=f"vs {name} trend",
        )

    ax_dev.axhline(0, color="#606060", lw=0.8)
    ax_dev.axhline(20, color="#c0392b", lw=0.75, ls="--", alpha=0.45)
    ax_dev.axhline(-20, color="#2c7a7b", lw=0.75, ls="--", alpha=0.45)
    ax_dev.set_ylabel("deviation %")
    ax_dev.grid(True, alpha=0.14)
    ax_dev.legend(loc="upper left", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(OUT / f"{label}_log_trend.png", dpi=130)
    plt.close(fig)


def plot_dashboard(asset_results: list[dict]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ncols = 2
    nrows = math.ceil(len(asset_results) / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(14, 4.2 * nrows))
    axes = np.array(axes).reshape(-1)

    for ax, item in zip(axes, asset_results):
        label = item["label"]
        df = item["df"]
        fits = item["fits"]
        ax.set_yscale("log")
        ax.plot(df["date"], df["value"], lw=1.0, color="#1a1d21")
        for name in ["10y", "5y"]:
            fit = fits[name]
            trend = np.exp(fit["trend_all_log"])
            trend = np.where(fit["mask"], trend, np.nan)
            ax.plot(df["date"], trend, lw=1.25, color=TREND_COLORS[name], label=name)
        ax.set_title(
            f"{label}: 5Y {pct(fits['5y']['cur_dev_pct'])}, "
            f"10Y {pct(fits['10y']['cur_dev_pct'])}",
            fontsize=10,
        )
        ax.grid(True, which="both", alpha=0.13)
        ax.legend(loc="upper left", fontsize=8, frameon=False)

    for ax in axes[len(asset_results):]:
        ax.axis("off")

    fig.suptitle("Common log-trend indicators: price vs 5Y/10Y trend", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.985])
    fig.savefig(OUT / "common_log_trend_dashboard.png", dpi=130)
    plt.close(fig)


def main() -> int:
    rows: list[dict] = []
    latest_rows: list[dict] = []
    asset_results: list[dict] = []
    missing: list[str] = []

    for label, desc in ASSETS:
        try:
            df = load(label)
        except FileNotFoundError:
            missing.append(label)
            continue

        last_date = df["date"].iloc[-1].date()
        price = float(df["value"].iloc[-1])
        fits = {name: fit_window(df, years) for name, years in WINDOWS.items()}
        g1y = trailing_growth(df)

        print(f"\n=== {label} ({desc}) through {last_date}, ${price:,.2f} ===")
        print(f"{'window':>6} {'n':>6} {'CAGR':>8} {'trend':>12} {'vs trend':>10} {'sigma':>7}  verdict")
        for name in WINDOWS:
            fit = fits[name]
            print(
                f"{name:>6} {fit['n']:>6} {cagr(fit['cagr']):>8} "
                f"{fit['current_trend']:>12,.2f} {pct(fit['cur_dev_pct']):>10} "
                f"{fit['cur_sigma']:>+7.2f}  {verdict(fit['cur_sigma'])}"
            )
            rows.append({
                "ticker": label,
                "description": desc,
                "last_date": str(last_date),
                "price": price,
                "window": name,
                "n": fit["n"],
                "trend_cagr": fit["cagr"],
                "trend_value": fit["current_trend"],
                "current_vs_trend_pct": fit["cur_dev_pct"],
                "current_sigma": fit["cur_sigma"],
                "verdict": verdict(fit["cur_sigma"]),
                "trailing_1y_growth": g1y,
            })

        latest_rows.append({
            "ticker": label,
            "description": desc,
            "last_date": str(last_date),
            "price": price,
            "trend_5y": fits["5y"]["current_trend"],
            "vs_5y_pct": fits["5y"]["cur_dev_pct"],
            "cagr_5y": fits["5y"]["cagr"],
            "trend_10y": fits["10y"]["current_trend"],
            "vs_10y_pct": fits["10y"]["cur_dev_pct"],
            "cagr_10y": fits["10y"]["cagr"],
            "trend_full": fits["full"]["current_trend"],
            "vs_full_pct": fits["full"]["cur_dev_pct"],
            "cagr_full": fits["full"]["cagr"],
            "trailing_1y_growth": g1y,
        })

        channel = make_channel(df, fits)
        channel.to_csv(OUT / f"{label}_channel.csv", index=False)
        plot_asset(label, desc, df, fits)
        asset_results.append({"label": label, "desc": desc, "df": df, "fits": fits})

    if not asset_results:
        print("ERROR: no input series found. Refresh macro/market_panel/data first.")
        return 1

    plot_dashboard(asset_results)

    summary_df = pd.DataFrame(rows)
    latest_df = pd.DataFrame(latest_rows)
    summary_df.to_csv(OUT / "common_log_trend_summary.csv", index=False)
    latest_df.to_csv(OUT / "common_log_trend_latest.csv", index=False)

    latest_sorted = latest_df.sort_values("vs_5y_pct", ascending=False)
    lines = [
        "# Common Log-Trend Indicators",
        "",
        "This folder tracks QQQ, SPY, and large-cap tech against log-linear trend lines.",
        "Use 5Y and 10Y first; use full-history only as background because liquidity and",
        "rate regimes can change the slope.",
        "",
        f"Built through {latest_df['last_date'].max()} from `macro/market_panel/data/`.",
        "",
        "## Latest Snapshot",
        "",
        "| ticker | price | vs 5Y trend | 5Y CAGR | vs 10Y trend | 10Y CAGR | vs full | 1Y growth |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in latest_sorted.iterrows():
        lines.append(
            f"| {r['ticker']} | ${r['price']:,.2f} | {pct(r['vs_5y_pct'])} | "
            f"{cagr(r['cagr_5y'])} | {pct(r['vs_10y_pct'])} | {cagr(r['cagr_10y'])} | "
            f"{pct(r['vs_full_pct'])} | {pct(r['trailing_1y_growth'])} |"
        )

    lines += [
        "",
        "## Files",
        "",
        "- `common_log_trend_dashboard.png` - quick visual dashboard.",
        "- `<TICKER>_log_trend.png` - price plus full/10Y/5Y log trend lines and deviation panel.",
        "- `<TICKER>_channel.csv` - price, trend values, and deviation columns.",
        "- `common_log_trend_summary.csv` - one row per ticker/window.",
        "- `common_log_trend_latest.csv` - one latest row per ticker.",
        "",
        "## Method",
        "",
        "Fit `ln(price) = a + b * time` with ordinary least squares.",
        "The trend line is `exp(a + b * time)`, and trend CAGR is `exp(b * 365.25) - 1`.",
        "",
        "Missing input series: " + (", ".join(missing) if missing else "none") + ".",
    ]
    (OUT / "summary.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"\nsummary -> {OUT / 'summary.md'}")
    print(f"dashboard -> {OUT / 'common_log_trend_dashboard.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
