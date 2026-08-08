#!/usr/bin/env python
"""Gold valuation vs US money supply: sigma channel + a real-time forward-return test.

Idea (the user's): gold has no cash flow, so its "fair value" anchor is the amount
of money chasing a slow-growing physical stock. Above-ground gold grows ~1.7%/yr;
money grows much faster. So the honest ratio is gold price relative to M2, and the
question each year is only "how far from normal is that ratio".

Three indicators, all on ln(gold):
  A. time         ln(gold) ~ a + b*t              (the QQQ log-trend recipe)
  B. money        ln(gold) ~ a + b*ln(M2)         (main model, sigma channel)
  C. real gold    ln(gold / CPI)                  (cross-check, no money data)

Two ways of reading each, and the difference is the whole point:
  * full-sample   fit on all data 1971-2026 -> uses information from the future.
                  Good for describing history, NOT a signal you could have traded.
  * real-time     expanding window, refit every month on data available then.
                  This is the only version the forward-return test is run on.

Inputs : data/*.csv  (run fetch_data.py first)
Outputs: monthly_panel.csv, annual_table.csv, forward_return_test.csv,
         gold_vs_money.png, analysis_snapshot.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

START = pd.Period("1971-09", "M")   # first full month after the Nixon shock closed the gold window
MIN_HISTORY = 120                   # months of history before a real-time reading is emitted
STOCK_GROWTH = 0.017                # above-ground gold stock growth, ~3,600t mined on ~215,000t


# ------------------------------------------------------------------ build panel
def load_panel() -> pd.DataFrame:
    gold = pd.read_csv(DATA / "gold_lbma_pm_daily.csv", parse_dates=["date"])
    gold["month"] = gold["date"].dt.to_period("M")
    monthly_avg = gold.groupby("month")["gold_usd_per_oz"].mean().rename("gold")
    month_end = gold.groupby("month")["gold_usd_per_oz"].last().rename("gold_month_end")

    m2 = pd.read_csv(DATA / "us_m2_monthly.csv")
    m2["month"] = pd.PeriodIndex(m2["month"], freq="M")
    m2 = m2.set_index("month")["m2_sa_usd_bn"].rename("m2")

    cpi = pd.read_csv(DATA / "us_cpi_monthly.csv")
    cpi["month"] = pd.PeriodIndex(cpi["month"], freq="M")
    cpi = cpi.set_index("month")["cpi_u_nsa"].rename("cpi")

    df = pd.concat([monthly_avg, month_end, m2, cpi], axis=1)
    # The money model only needs gold and M2. CPI has one true hole: the October 2025
    # CPI was never published (federal shutdown), so interpolate it rather than let a
    # cross-check series delete a month from the main model.
    df["cpi_interpolated"] = df["cpi"].isna() & df["gold"].notna() & df["m2"].notna()
    df["cpi"] = df["cpi"].interpolate(limit_area="inside")
    df = df.dropna(subset=["gold", "m2"])
    df = df[df.index >= START].copy()

    df["t_years"] = np.arange(len(df)) / 12.0
    df["ln_gold"] = np.log(df["gold"])
    df["ln_m2"] = np.log(df["m2"])
    # gold expressed in constant latest-month dollars
    df["real_gold"] = df["gold"] * (df["cpi"].iloc[-1] / df["cpi"])
    return df


# --------------------------------------------------------------- the indicators
def full_sample_fit(df: pd.DataFrame, xcol: str | None) -> dict:
    """OLS of ln(gold) on one regressor (or on a constant when xcol is None)."""
    y = df["ln_gold"].values
    if xcol is None:
        fit = np.full_like(y, y.mean())
        slope, intercept = 0.0, float(y.mean())
    else:
        x = df[xcol].values
        slope, intercept = np.polyfit(x, y, 1)
        fit = intercept + slope * x
    resid = y - fit
    sigma = float(resid.std(ddof=1))
    return {"slope": float(slope), "intercept": float(intercept),
            "sigma": sigma, "fit": fit, "z": resid / sigma}


def real_time(df: pd.DataFrame, xcol: str | None) -> tuple[pd.Series, pd.Series]:
    """Refit every month on data available up to that month. No look-ahead.

    Returns (sigma deviation, percentile rank of that deviation within its own history).
    """
    y = df["ln_gold"].values
    x = None if xcol is None else df[xcol].values
    z = np.full(len(y), np.nan)
    pct = np.full(len(y), np.nan)

    for i in range(MIN_HISTORY, len(y)):
        yy = y[: i + 1]
        if x is None:
            resid = yy - yy.mean()
        else:
            xx = x[: i + 1]
            b, a = np.polyfit(xx, yy, 1)
            resid = yy - (a + b * xx)
        sigma = resid.std(ddof=1)
        z[i] = resid[-1] / sigma
        pct[i] = float((resid <= resid[-1]).mean())

    return pd.Series(z, index=df.index), pd.Series(pct, index=df.index)


def raw_ratio_percentile(series: pd.Series) -> pd.Series:
    """Expanding percentile of a raw series - no regression, no fitted parameters."""
    values = series.values
    out = np.full(len(values), np.nan)
    for i in range(MIN_HISTORY, len(values)):
        history = values[: i + 1]
        out[i] = float((history <= values[i]).mean())
    return pd.Series(out, index=series.index)


# ---------------------------------------------------------------------- testing
def forward_returns(df: pd.DataFrame, months: int) -> pd.Series:
    return (df["gold"].shift(-months) / df["gold"]) ** (12 / months) - 1


def bucket_test(signal: pd.Series, fwd: pd.Series) -> pd.DataFrame:
    sample = pd.DataFrame({"signal": signal, "fwd": fwd}).dropna()
    if sample.empty:
        return pd.DataFrame()
    edges = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    labels = ["0-20% (cheapest)", "20-40%", "40-60%", "60-80%", "80-100% (dearest)"]
    buckets = pd.cut(sample["signal"], edges, labels=labels, include_lowest=True)
    out = sample.groupby(buckets, observed=False)["fwd"].agg(
        n="count", mean="mean", median="median", worst="min", best="max")
    return out


def main() -> int:
    df = load_panel()
    last = df.index[-1]
    print(f"panel {df.index[0]} -> {last}, {len(df)} months, "
          f"gold ${df['gold'].iloc[-1]:,.0f}/oz, M2 ${df['m2'].iloc[-1]:,.0f}bn")

    fits = {
        "time": full_sample_fit(df, "t_years"),
        "money": full_sample_fit(df, "ln_m2"),
        "real": None,  # handled separately: deflated level, no regressor
    }
    real_log = np.log(df["real_gold"].values)
    real_resid = real_log - real_log.mean()
    real_sigma = float(real_resid.std(ddof=1))
    fits["real"] = {"slope": 0.0, "intercept": float(real_log.mean()),
                    "sigma": real_sigma, "fit": np.full(len(df), real_log.mean()),
                    "z": real_resid / real_sigma}

    for name, xcol in [("time", "t_years"), ("money", "ln_m2")]:
        df[f"fair_{name}"] = np.exp(fits[name]["fit"])
        df[f"z_full_{name}"] = fits[name]["z"]
        z_rt, pct_rt = real_time(df, xcol)
        df[f"z_rt_{name}"] = z_rt
        df[f"pct_rt_{name}"] = pct_rt

    df["z_full_real"] = fits["real"]["z"]
    df["z_rt_real"] = (real_log - pd.Series(real_log, index=df.index).expanding().mean()) / \
                      pd.Series(real_log, index=df.index).expanding().std(ddof=1)
    df.loc[df.index[:MIN_HISTORY], "z_rt_real"] = np.nan
    df["pct_rt_real"] = raw_ratio_percentile(pd.Series(real_log, index=df.index))

    # the parameter-free version of the user's idea: gold priced against M2 directly
    df["ln_gold_over_m2"] = df["ln_gold"] - df["ln_m2"]
    df["pct_rt_ratio"] = raw_ratio_percentile(df["ln_gold_over_m2"])
    # same, but crediting the ~1.7%/yr growth in above-ground ounces
    df["ln_mcap_over_m2"] = df["ln_gold_over_m2"] + STOCK_GROWTH * df["t_years"]
    df["pct_rt_mcap"] = raw_ratio_percentile(df["ln_mcap_over_m2"])

    for horizon in (36, 60, 120):
        df[f"fwd_{horizon//12}y"] = forward_returns(df, horizon)

    # ------------------------------------------------------------------ testing
    signals = {
        "pct_rt_ratio": "gold / M2 ratio, real-time percentile (parameter-free)",
        "pct_rt_mcap": "gold market cap / M2, real-time percentile (+1.7%/yr ounces)",
        "pct_rt_money": "regression on ln(M2), real-time percentile",
        "pct_rt_real": "CPI-deflated gold, real-time percentile",
        "pct_rt_time": "log time trend, real-time percentile",
    }
    test_rows = []
    print("\n=== real-time forward-return test (no look-ahead) ===")
    for key, label in signals.items():
        for horizon in (3, 5, 10):
            fwd = df[f"fwd_{horizon}y"]
            table = bucket_test(df[key], fwd)
            if table.empty:
                continue
            sample = pd.DataFrame({"s": df[key], "f": fwd}).dropna()
            corr = float(sample["s"].corr(sample["f"]))
            cheap = table["mean"].iloc[0]
            dear = table["mean"].iloc[-1]
            monotone = bool(table["mean"].is_monotonic_decreasing)
            print(f"{label[:44]:<46} {horizon:>2}y  corr={corr:+.2f}  "
                  f"cheapest={cheap*100:+6.1f}%/yr  dearest={dear*100:+6.1f}%/yr  "
                  f"monotone={'yes' if monotone else 'no'}")
            for bucket, row in table.iterrows():
                test_rows.append({
                    "signal": key, "signal_label": label, "horizon_years": horizon,
                    "bucket": bucket, "n_months": int(row["n"]),
                    "mean_cagr": row["mean"], "median_cagr": row["median"],
                    "worst_cagr": row["worst"], "best_cagr": row["best"],
                    "full_sample_corr": corr, "monotonic": monotone,
                })
    test_df = pd.DataFrame(test_rows)
    test_df.to_csv(HERE / "forward_return_test.csv", index=False)

    # look-ahead comparison: same signal, full-sample fit
    print("\n=== same signal but fitted on the FULL sample (look-ahead - not tradeable) ===")
    lookahead = []
    for key in ("z_full_money", "z_full_real", "z_full_time"):
        for horizon in (3, 5, 10):
            sample = pd.DataFrame({"s": df[key], "f": df[f"fwd_{horizon}y"]}).dropna()
            corr = float(sample["s"].corr(sample["f"]))
            rt_key = key.replace("z_full", "pct_rt")
            rt_sample = pd.DataFrame({"s": df[rt_key], "f": df[f"fwd_{horizon}y"]}).dropna()
            rt_corr = float(rt_sample["s"].corr(rt_sample["f"]))
            print(f"{key:<16} {horizon:>2}y  full-sample corr={corr:+.2f}   "
                  f"real-time corr={rt_corr:+.2f}")
            lookahead.append({"signal": key, "horizon_years": horizon,
                              "full_sample_corr": corr, "real_time_corr": rt_corr})

    # ------------------------------------------------------------------ outputs
    keep = ["gold", "gold_month_end", "m2", "cpi", "real_gold",
            "fair_money", "fair_time",
            "z_full_money", "z_full_real", "z_full_time",
            "z_rt_money", "z_rt_real", "z_rt_time",
            "pct_rt_ratio", "pct_rt_mcap", "pct_rt_money", "pct_rt_real", "pct_rt_time",
            "fwd_3y", "fwd_5y", "fwd_10y"]
    panel = df[keep].copy()
    panel.index = panel.index.astype(str)
    panel.round(6).to_csv(HERE / "monthly_panel.csv", index_label="month")

    annual = df[df.index.month == 12].copy()
    if df.index[-1].month != 12:
        annual = pd.concat([annual, df.iloc[[-1]]])
    annual_out = annual[["gold", "m2", "real_gold", "fair_money",
                         "z_full_money", "pct_rt_ratio", "pct_rt_real",
                         "fwd_5y", "fwd_10y"]].copy()
    annual_out.insert(0, "year", annual.index.year)
    annual_out["gold_vs_fair_pct"] = annual["gold"] / annual["fair_money"] - 1
    annual_out.index = annual_out.index.astype(str)
    annual_out.round(6).to_csv(HERE / "annual_table.csv", index_label="month")

    # current fair-value band implied by today's M2
    money = fits["money"]
    ln_fair_now = money["intercept"] + money["slope"] * df["ln_m2"].iloc[-1]
    band = {f"{k}sigma": float(np.exp(ln_fair_now + k * money["sigma"]))
            for k in (-2, -1, 0, 1, 2)}

    snapshot = {
        "generated_at": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "panel": {"start": str(df.index[0]), "end": str(last), "months": len(df)},
        "latest": {
            "month": str(last),
            "gold_monthly_avg_usd": float(df["gold"].iloc[-1]),
            "m2_sa_usd_bn": float(df["m2"].iloc[-1]),
            "real_gold_in_latest_dollars": float(df["real_gold"].iloc[-1]),
            "z_full_money": float(df["z_full_money"].iloc[-1]),
            "z_rt_money": float(df["z_rt_money"].iloc[-1]),
            "pct_rt_ratio": float(df["pct_rt_ratio"].iloc[-1]),
            "pct_rt_real": float(df["pct_rt_real"].iloc[-1]),
            "pct_rt_mcap": float(df["pct_rt_mcap"].iloc[-1]),
        },
        "money_model": {
            "form": "ln(gold) = a + b * ln(M2_sa)",
            "a": money["intercept"], "b": money["slope"], "sigma_log": money["sigma"],
            "sigma_as_pct": float(np.exp(money["sigma"]) - 1),
            "implied_band_at_current_m2": band,
        },
        "time_model": {
            "form": "ln(gold) = a + b * t_years",
            "a": fits["time"]["intercept"], "b": fits["time"]["slope"],
            "trend_cagr": float(np.exp(fits["time"]["slope"]) - 1),
            "sigma_log": fits["time"]["sigma"],
        },
        "real_gold_model": {"mean_log": fits["real"]["intercept"],
                            "sigma_log": fits["real"]["sigma"]},
        "look_ahead_vs_real_time": lookahead,
        "caveat": "1971-2026 contains roughly two and a half gold cycles. Overlapping "
                  "monthly windows inflate apparent sample size; treat every bucket "
                  "statistic as a handful of independent observations.",
    }
    (HERE / "analysis_snapshot.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== latest reading, {last} ===")
    print(f"gold (monthly avg)      ${df['gold'].iloc[-1]:,.0f}/oz")
    print(f"M2 fair value           ${np.exp(ln_fair_now):,.0f}/oz  "
          f"(+/-1 sigma: ${band['-1sigma']:,.0f} - ${band['1sigma']:,.0f})")
    print(f"deviation, full sample  {df['z_full_money'].iloc[-1]:+.2f} sigma")
    print(f"deviation, real time    {df['z_rt_money'].iloc[-1]:+.2f} sigma")
    print(f"gold/M2 percentile      {df['pct_rt_ratio'].iloc[-1]*100:.1f}%")
    print(f"real gold percentile    {df['pct_rt_real'].iloc[-1]*100:.1f}%")

    plot(df, fits, band)
    print("\nwrote monthly_panel.csv, annual_table.csv, forward_return_test.csv, "
          "analysis_snapshot.json, gold_vs_money.png")
    return 0


def plot(df: pd.DataFrame, fits: dict, band: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    dates = df.index.to_timestamp()
    money = fits["money"]
    fair = df["fair_money"].values
    sigma = money["sigma"]

    fig, axes = plt.subplots(3, 1, figsize=(13, 11), sharex=True,
                             gridspec_kw={"height_ratios": [3, 1.4, 1.4]})

    ax = axes[0]
    ax.set_yscale("log")
    ax.fill_between(dates, fair * np.exp(-2 * sigma), fair * np.exp(2 * sigma),
                    color="#c8d8e8", alpha=0.35, label="+/-2 sigma")
    ax.fill_between(dates, fair * np.exp(-sigma), fair * np.exp(sigma),
                    color="#8fb0cc", alpha=0.40, label="+/-1 sigma")
    ax.plot(dates, fair, color="#1f4e79", lw=1.7,
            label=f"fair value from M2  (b={money['slope']:.2f})")
    ax.plot(dates, df["gold"], color="#1a1d21", lw=1.2, label="LBMA gold PM, monthly avg")
    ax.scatter([dates[-1]], [df["gold"].iloc[-1]], color="#d62728", s=36, zorder=5)
    ax.annotate(f"  ${df['gold'].iloc[-1]:,.0f}", (dates[-1], df["gold"].iloc[-1]),
                color="#d62728", fontsize=9, va="center")
    ax.set_ylabel("USD / oz (log scale)")
    ax.set_title("Gold vs US M2: sigma channel  (full-sample fit - descriptive, uses future data)")
    ax.grid(True, which="both", alpha=0.16)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    ax = axes[1]
    ax.plot(dates, df["z_full_money"], color="#1f4e79", lw=1.2, label="full-sample fit")
    ax.plot(dates, df["z_rt_money"], color="#c0392b", lw=1.2, label="real-time (expanding) fit")
    for level, style in [(0, "-"), (1, "--"), (-1, "--"), (2, ":"), (-2, ":")]:
        ax.axhline(level, color="#606060", lw=0.7, ls=style, alpha=0.6)
    ax.set_ylabel("deviation, sigma")
    ax.grid(True, alpha=0.14)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    ax.set_title("The same model read two ways - they disagree for decades at a time",
                 fontsize=10)

    ax = axes[2]
    ax.plot(dates, df["pct_rt_ratio"] * 100, color="#2c7a7b", lw=1.3,
            label="gold / M2, real-time percentile")
    ax.plot(dates, df["pct_rt_real"] * 100, color="#b8860b", lw=1.1, alpha=0.85,
            label="CPI-deflated gold, real-time percentile")
    ax.axhline(50, color="#606060", lw=0.7)
    ax.axhline(80, color="#c0392b", lw=0.7, ls="--", alpha=0.6)
    ax.axhline(20, color="#2c7a7b", lw=0.7, ls="--", alpha=0.6)
    ax.set_ylabel("percentile of own history")
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.14)
    ax.legend(loc="lower left", fontsize=8, frameon=False)
    ax.set_title("Parameter-free version - this is the one the forward-return test uses",
                 fontsize=10)

    fig.tight_layout()
    fig.savefig(HERE / "gold_vs_money.png", dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    raise SystemExit(main())
