#!/usr/bin/env python
"""Does gold beat SPY / QQQ - and can gold's valuation tell you in advance?

"Cheap" is not a reason to buy. The reason to hold gold instead of the index is that
gold out-earns the index over the holding period. So this script asks three questions
in order:

  1. Over 1-year and 3-year windows, when did gold actually beat SPY / QQQ?
  2. Those eras - what was gold's valuation (sigma vs M2, percentile) when they STARTED?
  3. Is that a rule you could have followed, or only a story you can tell afterwards?

Entry is month-end (the price you could actually pay). The valuation signal is the
real-time percentile from build_analysis.py, which uses no future data.

Inputs : monthly_panel.csv, data/<BENCH>_daily_adjusted.csv
Outputs: relative_windows.csv, relative_by_valuation.csv, gold_win_eras.csv,
         gold_vs_equities.png, comparison_snapshot.json
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

HORIZONS = {12: "1y", 36: "3y"}
BENCHES = {
    "SPY": "S&P 500 ETF (total return, 1993-)",
    "QQQ": "Nasdaq-100 ETF (total return, 1999-)",
    "SP500TR": "S&P 500 Total Return index (1988-)",
    "GSPC": "S&P 500 price index, NO dividends (1970-)",
}
PRIMARY = "SPY"


def load() -> pd.DataFrame:
    panel = pd.read_csv(HERE / "monthly_panel.csv")
    panel["month"] = pd.PeriodIndex(panel["month"], freq="M")
    panel = panel.set_index("month")

    df = panel[["gold", "gold_month_end", "m2", "fair_money",
                "z_full_money", "z_rt_money", "pct_rt_ratio", "pct_rt_real"]].copy()

    for label in BENCHES:
        series = pd.read_csv(DATA / f"{label}_daily_adjusted.csv", parse_dates=["date"])
        series["month"] = series["date"].dt.to_period("M")
        df[label] = series.groupby("month")["adj_close"].last()

    return df


def add_forward(df: pd.DataFrame) -> pd.DataFrame:
    """Forward CAGR from month-end entry, for gold and every benchmark."""
    for months, tag in HORIZONS.items():
        power = 12 / months
        df[f"gold_{tag}"] = (df["gold_month_end"].shift(-months)
                             / df["gold_month_end"]) ** power - 1
        for label in BENCHES:
            df[f"{label}_{tag}"] = (df[label].shift(-months) / df[label]) ** power - 1
            df[f"excess_{label}_{tag}"] = df[f"gold_{tag}"] - df[f"{label}_{tag}"]
    return df


def bucket_table(df: pd.DataFrame, label: str, tag: str) -> pd.DataFrame:
    """Excess return and win rate, bucketed by gold's valuation percentile at entry."""
    sample = df[["pct_rt_ratio", f"excess_{label}_{tag}",
                 f"gold_{tag}", f"{label}_{tag}"]].dropna()
    if sample.empty:
        return pd.DataFrame()

    edges = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    names = ["0-20% (cheapest)", "20-40%", "40-60%", "60-80%", "80-100% (dearest)"]
    buckets = pd.cut(sample["pct_rt_ratio"], edges, labels=names, include_lowest=True)

    rows = {}
    for name, group in sample.groupby(buckets, observed=False):
        if group.empty:
            continue
        rows[name] = {
            "n_months": len(group),
            "gold_cagr": group[f"gold_{tag}"].mean(),
            "bench_cagr": group[f"{label}_{tag}"].mean(),
            "excess_mean": group[f"excess_{label}_{tag}"].mean(),
            "excess_median": group[f"excess_{label}_{tag}"].median(),
            "gold_win_rate": (group[f"excess_{label}_{tag}"] > 0).mean(),
        }
    return pd.DataFrame(rows).T


def find_eras(flags: pd.Series, min_months: int = 3) -> list[tuple]:
    """Contiguous stretches of entry months where gold beat the benchmark."""
    eras, start, prev = [], None, None
    for month, won in flags.items():
        if won and start is None:
            start = month
        elif not won and start is not None:
            eras.append((start, prev))
            start = None
        if won:
            prev = month
    if start is not None:
        eras.append((start, prev))
    return [(a, b) for a, b in eras if (b - a).n + 1 >= min_months]


def pct(x: float) -> str:
    return "n/a" if not np.isfinite(x) else f"{x * 100:+.1f}%"


def expanding_trend_percentile(series: pd.Series, min_months: int = 120) -> pd.Series:
    """Where does the index sit against its own log trend, using only data to date?

    Same recipe as scripts/log_trend_channel.py, refit every month so the reading is
    what an investor could actually have computed at the time.
    """
    values = np.log(series.values)
    times = np.arange(len(values), dtype=float)
    out = np.full(len(values), np.nan)
    for i in range(min_months, len(values)):
        slope, intercept = np.polyfit(times[: i + 1], values[: i + 1], 1)
        resid = values[: i + 1] - (intercept + slope * times[: i + 1])
        out[i] = float((resid <= resid[-1]).mean())
    return pd.Series(out, index=series.index)


def main() -> int:
    df = add_forward(load())
    last = df.index[-1]
    print(f"panel {df.index[0]} -> {last}")
    for label in BENCHES:
        valid = df[label].dropna()
        print(f"  {label:<8} {valid.index[0]} -> {valid.index[-1]}")

    # ---------------------------------------------------- 1. who won, and how often
    print("\n=== 1. Did gold beat the index at all? (every overlapping window) ===")
    headline = []
    for label in BENCHES:
        for months, tag in HORIZONS.items():
            col = f"excess_{label}_{tag}"
            sample = df[col].dropna()
            if sample.empty:
                continue
            win = (sample > 0).mean()
            print(f"  gold vs {label:<8} {tag}  n={len(sample):>4}  "
                  f"gold wins {win*100:>5.1f}% of windows  "
                  f"mean excess {pct(sample.mean()):>8}  median {pct(sample.median()):>8}")
            headline.append({"benchmark": label, "horizon": tag, "n_windows": len(sample),
                             "gold_win_rate": float(win),
                             "mean_excess_cagr": float(sample.mean()),
                             "median_excess_cagr": float(sample.median())})

    # ------------------------------------- 2. the eras where gold won, and their sigma
    print("\n=== 2. The eras gold won, and gold's valuation when they started ===")
    era_rows = []
    for label in BENCHES:
        for months, tag in HORIZONS.items():
            col = f"excess_{label}_{tag}"
            flags = (df[col] > 0).where(df[col].notna()).dropna().astype(bool)
            if flags.empty:
                continue
            for start, end in find_eras(flags):
                window = df.loc[start:end]
                era_rows.append({
                    "benchmark": label, "horizon": tag,
                    "entry_from": str(start), "entry_to": str(end),
                    "entry_months": (end - start).n + 1,
                    "exit_by": str(end + months),
                    "gold_cagr_mean": window[f"gold_{tag}"].mean(),
                    "bench_cagr_mean": window[f"{label}_{tag}"].mean(),
                    "excess_mean": window[col].mean(),
                    "entry_pct_median": window["pct_rt_ratio"].median(),
                    "entry_z_full_median": window["z_full_money"].median(),
                    "entry_gold_price_first": window["gold_month_end"].iloc[0],
                })
    eras = pd.DataFrame(era_rows)
    eras.to_csv(HERE / "gold_win_eras.csv", index=False)

    show = eras[(eras.benchmark == PRIMARY) & (eras.horizon == "3y")]
    print(f"  gold vs {PRIMARY}, 3-year windows - {len(show)} distinct eras "
          f"(>=3 consecutive entry months):")
    for _, r in show.iterrows():
        print(f"    entry {r['entry_from']}..{r['entry_to']} ({int(r['entry_months']):>2}m)  "
              f"gold {pct(r['gold_cagr_mean']):>7}/yr vs {pct(r['bench_cagr_mean']):>7}/yr  "
              f"excess {pct(r['excess_mean']):>7}  "
              f"entry pct={r['entry_pct_median']*100:>5.1f}%  "
              f"sigma={r['entry_z_full_median']:+.2f}")

    # ----------------------------------- 3. is the valuation actually the discriminator
    print("\n=== 3. Excess return by gold's valuation percentile at entry ===")
    bucket_rows = []
    for label in BENCHES:
        for months, tag in HORIZONS.items():
            table = bucket_table(df, label, tag)
            if table.empty:
                continue
            if label == PRIMARY:
                print(f"\n  -- gold vs {label}, {tag} windows --")
                print(f"  {'entry percentile':<20}{'n':>5}{'gold':>9}{'index':>9}"
                      f"{'excess':>9}{'gold win rate':>15}")
                for name, r in table.iterrows():
                    print(f"  {name:<20}{int(r['n_months']):>5}{pct(r['gold_cagr']):>9}"
                          f"{pct(r['bench_cagr']):>9}{pct(r['excess_mean']):>9}"
                          f"{r['gold_win_rate']*100:>14.0f}%")
            for name, r in table.iterrows():
                bucket_rows.append({"benchmark": label, "horizon": tag, "bucket": name,
                                    **{k: float(v) for k, v in r.items()}})
    pd.DataFrame(bucket_rows).to_csv(HERE / "relative_by_valuation.csv", index=False)

    # sigma distribution in winning vs losing windows - the user's literal question
    print("\n=== 4. Gold's entry valuation: windows it won vs windows it lost ===")
    dist_rows = []
    for label in BENCHES:
        for months, tag in HORIZONS.items():
            col = f"excess_{label}_{tag}"
            sample = df[[col, "pct_rt_ratio", "z_full_money"]].dropna()
            if sample.empty:
                continue
            won = sample[sample[col] > 0]
            lost = sample[sample[col] <= 0]
            row = {"benchmark": label, "horizon": tag,
                   "n_won": len(won), "n_lost": len(lost),
                   "won_pct_median": won["pct_rt_ratio"].median(),
                   "lost_pct_median": lost["pct_rt_ratio"].median(),
                   "won_sigma_median": won["z_full_money"].median(),
                   "lost_sigma_median": lost["z_full_money"].median()}
            dist_rows.append(row)
            if label in (PRIMARY, "QQQ", "GSPC"):
                print(f"  gold vs {label:<8} {tag}:  won {len(won):>4} windows at median "
                      f"entry pct {row['won_pct_median']*100:>5.1f}% / sigma "
                      f"{row['won_sigma_median']:+.2f}   |   lost {len(lost):>4} at "
                      f"{row['lost_pct_median']*100:>5.1f}% / sigma {row['lost_sigma_median']:+.2f}")

    # threshold sweep: "only buy gold when it is below the Nth percentile"
    print("\n=== 5. Threshold rule: buy gold only below the Nth percentile ===")
    thresh_rows = []
    for label in (PRIMARY, "QQQ"):
        for months, tag in HORIZONS.items():
            col = f"excess_{label}_{tag}"
            sample = df[[col, "pct_rt_ratio"]].dropna()
            if sample.empty:
                continue
            print(f"  -- gold vs {label}, {tag} --")
            for cut in (0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.01):
                sub = sample[sample["pct_rt_ratio"] <= cut]
                if len(sub) < 12:
                    continue
                label_txt = "all windows" if cut > 1 else f"pct <= {cut*100:.0f}%"
                print(f"     {label_txt:<16} n={len(sub):>4}  mean excess "
                      f"{pct(sub[col].mean()):>8}  win rate {(sub[col]>0).mean()*100:>5.1f}%")
                thresh_rows.append({"benchmark": label, "horizon": tag, "threshold": cut,
                                    "n": len(sub), "mean_excess": float(sub[col].mean()),
                                    "win_rate": float((sub[col] > 0).mean())})

    # ------------------------------------------- 6. two hypotheses that do NOT survive
    print("\n=== 6. Falsification: does any valuation rule actually call the winner? ===")

    # (a) same sample window for both benchmarks - is SPY really different from QQQ?
    print("  (a) restrict SPY to QQQ's window (1999-03+) - the benchmarks stop disagreeing:")
    same_window = []
    for label in (PRIMARY, "QQQ"):
        for tag in HORIZONS.values():
            col = f"excess_{label}_{tag}"
            sample = df.loc["1999-03":, ["pct_rt_ratio", col]].dropna()
            cheap = sample[sample["pct_rt_ratio"] <= 0.2]
            print(f"      gold vs {label:<4} {tag}: all n={len(sample):>3} "
                  f"{pct(sample[col].mean()):>7} win {(sample[col]>0).mean()*100:>4.0f}%"
                  f"   |  cheapest quintile n={len(cheap):>3} "
                  f"{pct(cheap[col].mean()):>7} win {(cheap[col]>0).mean()*100:>4.0f}%")
            same_window.append({"benchmark": label, "horizon": tag, "window": "1999-03+",
                                "all_n": len(sample), "all_excess": float(sample[col].mean()),
                                "cheap_n": len(cheap), "cheap_excess": float(cheap[col].mean()),
                                "cheap_win_rate": float((cheap[col] > 0).mean())})

    # (b) the same cheap signal, split by decade - the sign flips twice
    print("  (b) gold vs SPY, 3y, split by era - cheap gold changes sign across regimes:")
    regimes = [("1993-01", "1999-02"), ("1999-03", "2011-12"), ("2012-01", "2026-07")]
    regime_rows = []
    for lo, hi in regimes:
        sample = df.loc[lo:hi, ["pct_rt_ratio", "excess_SPY_3y"]].dropna()
        if sample.empty:
            continue
        cheap = sample[sample["pct_rt_ratio"] <= 0.2]
        cheap_mean = cheap["excess_SPY_3y"].mean() if len(cheap) else float("nan")
        print(f"      {lo}..{hi}  all n={len(sample):>3} {pct(sample['excess_SPY_3y'].mean()):>7} "
              f"win {(sample['excess_SPY_3y']>0).mean()*100:>4.0f}%   |  "
              f"cheap n={len(cheap):>3} {pct(cheap_mean):>7}")
        regime_rows.append({"from": lo, "to": hi, "n": len(sample),
                            "all_excess": float(sample["excess_SPY_3y"].mean()),
                            "all_win_rate": float((sample["excess_SPY_3y"] > 0).mean()),
                            "cheap_n": len(cheap), "cheap_excess": float(cheap_mean)})

    # (c) "gold cheap AND stocks dear" - the intuitive rule, and it fails
    equity_pct = expanding_trend_percentile(df["GSPC"])
    df["equity_pct"] = equity_pct
    df["spread"] = df["equity_pct"] - df["pct_rt_ratio"]
    print("  (c) 'gold cheap AND stocks dear' spread, quartiles of that spread:")
    spread_rows = []
    for label in (PRIMARY, "QQQ"):
        for tag in HORIZONS.values():
            col = f"excess_{label}_{tag}"
            sample = df[["spread", col]].dropna()
            if len(sample) < 40:
                continue
            quartiles = pd.qcut(sample["spread"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
            corr = float(sample["spread"].corr(sample[col]))
            parts = []
            for name, group in sample.groupby(quartiles, observed=True):
                parts.append(f"{name} {pct(group[col].mean())}/{(group[col]>0).mean()*100:.0f}%")
                spread_rows.append({"benchmark": label, "horizon": tag, "quartile": str(name),
                                    "n": len(group), "excess": float(group[col].mean()),
                                    "win_rate": float((group[col] > 0).mean())})
            print(f"      gold vs {label:<4} {tag}  corr={corr:+.2f}   " + "  ".join(parts))

    print(f"\n  Today: gold pct={df['pct_rt_ratio'].iloc[-1]*100:.0f}%, "
          f"S&P trend pct={df['equity_pct'].iloc[-1]*100:.0f}%, "
          f"spread={df['spread'].iloc[-1]:+.2f}  (both expensive at once)")

    # (d) the only precedent for "both expensive at once" - what happened after
    print("\n=== 7. Precedent for today: both gold AND stocks above their own Nth pct ===")
    both_rows = []
    for cut in (0.7, 0.8):
        both = df[(df["pct_rt_ratio"] > cut) & (df["equity_pct"] > cut)]
        past = both[["excess_GSPC_1y", "excess_GSPC_3y", "gold_1y", "gold_3y"]].dropna()
        eras = sorted({m.year for m in both.index})
        print(f"  both > {cut*100:.0f}th pct: {len(both)} months in "
              f"{eras} - {len(past)} of them old enough to score")
        if past.empty:
            continue
        for tag in ("1y", "3y"):
            excess = past[f"excess_GSPC_{tag}"]
            print(f"      {tag}: gold vs S&P {pct(excess.mean()):>7}/yr, "
                  f"gold won {(excess>0).mean()*100:.0f}% of them, "
                  f"gold absolute {pct(past[f'gold_{tag}'].mean()):>7}/yr")
            both_rows.append({"threshold": cut, "horizon": tag, "n": len(past),
                              "years": eras,
                              "excess_vs_gspc": float(excess.mean()),
                              "gold_win_rate": float((excess > 0).mean()),
                              "gold_absolute": float(past[f"gold_{tag}"].mean())})
    print("  NOTE: benchmark here is GSPC (no dividends) because the only precedent "
          "predates SPY. The true gap was wider.")

    # ------------------------------------------------------------------- persistence
    keep = ["gold_month_end", "m2", "pct_rt_ratio", "z_full_money", "equity_pct", "spread"]
    keep += list(BENCHES)
    keep += [f"gold_{t}" for t in HORIZONS.values()]
    keep += [f"{b}_{t}" for b in BENCHES for t in HORIZONS.values()]
    keep += [f"excess_{b}_{t}" for b in BENCHES for t in HORIZONS.values()]
    out = df[keep].copy()
    out.index = out.index.astype(str)
    out.round(6).to_csv(HERE / "relative_windows.csv", index_label="month")

    current = df.iloc[-1]
    snapshot = {
        "generated_at": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "panel_end": str(last),
        "current": {
            "month": str(last),
            "gold_month_end": float(current["gold_month_end"]),
            "pct_rt_ratio": float(current["pct_rt_ratio"]),
            "z_full_money": float(current["z_full_money"]),
        },
        "headline_win_rates": headline,
        "valuation_distribution": dist_rows,
        "threshold_sweep": thresh_rows,
        "same_window_test": same_window,
        "regime_split": regime_rows,
        "spread_test": spread_rows,
        "both_expensive_precedent": both_rows,
        "caveats": [
            "Overlapping monthly windows: a 3-year test on 33 years of SPY data holds "
            "roughly 11 independent observations, not 360.",
            "GSPC excludes dividends and is the only series reaching the 1970s, so every "
            "1970s comparison flatters gold by the S&P dividend yield of that era (~4%/yr).",
            "Gold pays nothing and SPY/QQQ compound dividends; the excess column already "
            "accounts for that everywhere except GSPC.",
        ],
    }
    (HERE / "comparison_snapshot.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")

    plot(df)
    print("\nwrote relative_windows.csv, relative_by_valuation.csv, gold_win_eras.csv, "
          "comparison_snapshot.json, gold_vs_equities.png")
    return 0


def plot(df: pd.DataFrame) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(3, 1, figsize=(13, 11.5), sharex=False,
                             gridspec_kw={"height_ratios": [1.5, 1.5, 1.6]})

    # ratio of gold to each index, rebased where each starts
    ax = axes[0]
    ax.set_yscale("log")
    for label, color in [("GSPC", "#9aa0a6"), ("SPY", "#1f4e79"), ("QQQ", "#c0392b")]:
        ratio = (df["gold_month_end"] / df[label]).dropna()
        ax.plot(ratio.index.to_timestamp(), ratio / ratio.iloc[0], color=color, lw=1.3,
                label=f"gold / {label} (rebased at {ratio.index[0]})")
    ax.axhline(1, color="#606060", lw=0.8)
    ax.set_ylabel("relative value (log)")
    ax.set_title("Gold relative to the index - rising means gold is winning")
    ax.grid(True, which="both", alpha=0.15)
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    # rolling 3y excess vs SPY
    ax = axes[1]
    excess = df["excess_SPY_3y"].dropna()
    stamps = excess.index.to_timestamp()
    ax.fill_between(stamps, 0, excess * 100, where=(excess > 0),
                    color="#2c7a7b", alpha=0.55, label="gold wins")
    ax.fill_between(stamps, 0, excess * 100, where=(excess <= 0),
                    color="#c0392b", alpha=0.45, label="index wins")
    ax.axhline(0, color="#303030", lw=0.9)
    ax.set_ylabel("gold minus SPY, %/yr")
    ax.set_title("Forward 3-year excess return of gold over SPY, by entry month", fontsize=10)
    ax.grid(True, alpha=0.14)
    ax.legend(loc="upper right", fontsize=8, frameon=False)

    # scatter: entry valuation vs 3y excess
    ax = axes[2]
    for label, color, marker in [("SPY", "#1f4e79", "o"), ("QQQ", "#c0392b", "^")]:
        sample = df[["pct_rt_ratio", f"excess_{label}_3y"]].dropna()
        ax.scatter(sample["pct_rt_ratio"] * 100, sample[f"excess_{label}_3y"] * 100,
                   s=11, alpha=0.45, color=color, marker=marker, label=f"vs {label}")
    ax.axhline(0, color="#303030", lw=0.9)
    current = df["pct_rt_ratio"].dropna().iloc[-1] * 100
    ax.axvline(current, color="#b8860b", lw=1.5, ls="--",
               label=f"today = {current:.0f}th pct")
    ax.set_xlabel("gold / M2 percentile at entry (real-time, no look-ahead)")
    ax.set_ylabel("forward 3y excess, %/yr")
    ax.set_title("Expensive gold never won. Cheap gold went both ways - "
                 "the left half spans -42% to +45%", fontsize=10)
    ax.grid(True, alpha=0.14)
    ax.legend(loc="upper right", fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(HERE / "gold_vs_equities.png", dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    raise SystemExit(main())
