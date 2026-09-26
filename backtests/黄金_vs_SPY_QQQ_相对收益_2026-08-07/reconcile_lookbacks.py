#!/usr/bin/env python
"""Why do the two gold studies in this repo disagree about the sign of sigma?

backtests/黄金_货币供应_估值_2026-08-07/  says: dear gold underperforms  (expanding window)
backtests/黄金_vs_SPY_QQQ_相对收益_.../   says: dear gold outperforms    (120m rolling)

Both are honest - neither uses future data. They differ in exactly two choices:

  * LOOKBACK: how much history goes into the fit that defines "normal"
  * SAMPLE:   which years the forward-return test is scored over

This script varies those two and holds everything else fixed - same gold series, same
M2, same month-end entry, same benchmark, same forward returns - so the disagreement
can be attributed rather than argued about.

Run: python reconcile_lookbacks.py
Out: lookback_reconciliation.csv
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
VALUATION = HERE.parent / "黄金_货币供应_估值_2026-08-07"

MIN_HISTORY = 120
LOOKBACKS = {"expanding": None, "rolling_10y": 120, "rolling_20y": 240}
SAMPLES = {"1993-01+ (SPY full)": "1993-01", "1999-03+ (QQQ common)": "1999-03"}
HORIZONS = {12: "1y", 36: "3y"}


def load() -> pd.DataFrame:
    panel = pd.read_csv(VALUATION / "monthly_panel.csv")
    panel["month"] = pd.PeriodIndex(panel["month"], freq="M")
    df = panel.set_index("month")[["gold_month_end", "m2"]].copy()

    for label in ("SPY", "QQQ"):
        series = pd.read_csv(VALUATION / "data" / f"{label}_daily_adjusted.csv",
                             parse_dates=["date"])
        series["month"] = series["date"].dt.to_period("M")
        df[label] = series.groupby("month")["adj_close"].last()

    for months, tag in HORIZONS.items():
        power = 12 / months
        df[f"gold_{tag}"] = (df["gold_month_end"].shift(-months)
                             / df["gold_month_end"]) ** power - 1
        for label in ("SPY", "QQQ"):
            bench = (df[label].shift(-months) / df[label]) ** power - 1
            df[f"excess_{label}_{tag}"] = df[f"gold_{tag}"] - bench
    return df


def sigma_series(df: pd.DataFrame, window: int | None) -> pd.Series:
    """Deviation of ln(gold) from ln(gold)~ln(M2), refit each month. No look-ahead."""
    y = np.log(df["gold_month_end"].values)
    x = np.log(df["m2"].values)
    out = np.full(len(y), np.nan)
    for i in range(MIN_HISTORY - 1, len(y)):
        lo = 0 if window is None else max(0, i + 1 - window)
        xx, yy = x[lo:i + 1], y[lo:i + 1]
        if len(yy) < MIN_HISTORY:
            continue
        slope, intercept = np.polyfit(xx, yy, 1)
        resid = yy - (intercept + slope * xx)
        sigma = resid.std(ddof=0)
        out[i] = resid[-1] / sigma
    return pd.Series(out, index=df.index)


def main() -> int:
    df = load()
    for name, window in LOOKBACKS.items():
        df[f"z_{name}"] = sigma_series(df, window)

    rows = []
    print("Same gold, same M2, same entries, same benchmarks.")
    print("Only the lookback window and the scoring sample change.\n")

    for bench in ("SPY", "QQQ"):
        for tag in HORIZONS.values():
            print(f"=== gold vs {bench}, {tag} holding ===")
            print(f"  {'lookback':<13}{'sample':<24}{'n':>5}{'corr':>8}"
                  f"{'dear(>+1s)':>12}{'cheap(<-1s)':>13}")
            for lb in LOOKBACKS:
                for sample_name, start in SAMPLES.items():
                    col = f"excess_{bench}_{tag}"
                    sub = df.loc[start:, [f"z_{lb}", col]].dropna()
                    if len(sub) < 30:
                        continue
                    z, ex = sub[f"z_{lb}"], sub[col]
                    corr = float(z.corr(ex))
                    dear = ex[z > 1]
                    cheap = ex[z < -1]
                    dear_m = dear.mean() if len(dear) else float("nan")
                    cheap_m = cheap.mean() if len(cheap) else float("nan")
                    print(f"  {lb:<13}{sample_name:<24}{len(sub):>5}{corr:>+8.2f}"
                          f"{dear_m*100:>11.1f}%{cheap_m*100:>12.1f}%")
                    rows.append({"benchmark": bench, "horizon": tag, "lookback": lb,
                                 "sample": sample_name, "n": len(sub), "corr": corr,
                                 "n_dear": len(dear), "excess_when_dear": dear_m,
                                 "n_cheap": len(cheap), "excess_when_cheap": cheap_m})
            print()

    pd.DataFrame(rows).to_csv(HERE / "lookback_reconciliation.csv", index=False)

    print("Current reading under each lookback (latest month with M2):")
    latest = df.dropna(subset=["m2"]).index[-1]
    for lb in LOOKBACKS:
        value = df.loc[latest, f"z_{lb}"]
        print(f"  {lb:<13} {value:+.2f} sigma")
    print(f"  (month = {latest}, gold month-end ${df.loc[latest,'gold_month_end']:,.2f})")
    print("\nwrote lookback_reconciliation.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
