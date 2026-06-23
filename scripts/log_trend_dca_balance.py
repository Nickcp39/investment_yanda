#!/usr/bin/env python
"""Realistic version: FIXED salary in every month, un-deployed money piles up as
dry powder (earning a cash rate), and gets DEPLOYED when the index is below the
-1σ band. Then sweep the base-vs-dry-powder split to find the balance point.

This fixes the prior backtest, which stranded skipped cash forever (unfairly
handicapping dip-buying). Here the dip-buyer actually accumulates and deploys.

Model (monthly):
  cash *= (1+cash_rate);  cash += salary/12
  deploy `base` fraction of THIS month's salary into the index (the always-in leg)
  if PIT dev <= dip_thresh (real-time, NO look-ahead): deploy `dip_deploy` of the
     remaining accumulated cash (the dry-powder leg)
Anchors:
  base=1.0                -> pure DCA (all-in always, no dry powder)
  base=0.0, dip_deploy=1  -> pure dip-buyer (hoard salary, dump it all on -1σ dips)
Balance = sweep base in [0..1] (with dip_deploy=1) -> the split that maximizes wealth.
"""
from __future__ import annotations
import sys, math
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from log_trend_dca_backtest import fetch_yahoo_monthly, load_local_monthly, pit_dev, WARMUP  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OUT = Path(__file__).resolve().parents[1] / "macro" / "market_panel" / "log_trend"
SALARY = 100_000.0                  # fixed annual income
INC = SALARY / 12.0                 # monthly
CASH_RATE_ANN = 0.04               # T-bills on un-deployed cash
CR = (1 + CASH_RATE_ANN) ** (1 / 12) - 1
THRESH = -1.0                       # "below the std band"


def irr(cfs):
    lo, hi = -0.05, 0.05
    f = lambda r: sum(c / (1 + r) ** k for k, c in enumerate(cfs))  # noqa: E731
    if not math.isfinite(f(lo)) or f(lo) * f(hi) > 0:
        return float("nan")
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) > 0 else (lo, m)
    return (1 + (lo + hi) / 2) ** 12 - 1


def simulate(v, dev, base, dip_deploy, thresh=THRESH):
    n = len(v); cash = 0.0; shares = 0.0; cfs = []
    cash_track = []
    for i in range(n):
        cash = cash * (1 + CR) + INC
        cfs.append(-INC)
        inv = min(base * INC, cash)
        cash -= inv; shares += inv / v[i]
        if dip_deploy > 0 and not np.isnan(dev[i]) and dev[i] <= thresh:
            extra = dip_deploy * cash
            cash -= extra; shares += extra / v[i]
        cash_track.append(cash / (cash + shares * v[i] + 1e-9))
    final = shares * v[-1] + cash
    cfs.append(final)
    return {"final": final, "irr": irr(cfs), "avg_cash_pct": float(np.mean(cash_track[WARMUP:]))}


def run(symbol, label, lines):
    df = fetch_yahoo_monthly(symbol)
    src = symbol
    if df is None:
        df = load_local_monthly(label); src = f"{label} (local 2010+)"
    v = df["value"].values
    dev = pit_dev(v)
    contributed = INC * len(v)
    d0, d1 = df["date"].iloc[0].date(), df["date"].iloc[-1].date()

    print(f"\n=== {src}  ({d0} → {d1}, {len(v)} mo, ${SALARY:,.0f}/yr, cash@{CASH_RATE_ANN*100:.0f}%) ===")
    print(f"total salary in over the period: ${contributed:,.0f}")
    lines += [f"## {src} — {d0}→{d1}  (${SALARY:,.0f}/yr salary, total in ${contributed/1e6:.2f}M, cash@{CASH_RATE_ANN*100:.0f}%)", ""]

    # anchors
    anchors = {
        "Pure DCA (base=1.0)":             simulate(v, dev, 1.0, 0.0),
        "Pure dip (base=0, dump on -1σ)":  simulate(v, dev, 0.0, 1.0),
    }
    print(f"\n{'strategy':<34}{'final':>14}{'IRR':>7}{'avg cash%':>10}")
    lines += ["| strategy | final wealth | IRR | avg cash drag |", "|---|---:|---:|---:|"]
    for nm, r in anchors.items():
        print(f"{nm:<34}{r['final']:>14,.0f}{r['irr']*100:>6.1f}%{r['avg_cash_pct']*100:>9.0f}%")
        lines.append(f"| {nm} | ${r['final']:,.0f} | {r['irr']*100:.1f}% | {r['avg_cash_pct']*100:.0f}% |")

    # sweep base, deploy all dry powder on dips
    print(f"\n  -- balance sweep (deploy 100% dry powder on <= -1σ) --")
    lines += ["", "### Balance sweep (deploy 100% dry powder on ≤ −1σ; vary the always-in base)", "",
              "| base (always-in) | dry-powder for dips | final wealth | IRR | avg cash drag |", "|---:|---:|---:|---:|---:|"]
    best = None
    for base in [0.0, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0]:
        r = simulate(v, dev, base, 1.0)
        tag = ""
        if best is None or r["final"] > best[1]["final"]:
            best = (base, r)
        print(f"     base={base:<4}  final ${r['final']:>13,.0f}  IRR {r['irr']*100:>5.1f}%  cash {r['avg_cash_pct']*100:>3.0f}%")
        lines.append(f"| {base:.2f} | {1-base:.2f} | ${r['final']:,.0f} | {r['irr']*100:.1f}% | {r['avg_cash_pct']*100:.0f}% |")
    bb, br = best
    print(f"  >> balance point: base={bb} (keep {(1-bb)*100:.0f}% as dry powder) -> ${br['final']:,.0f}, IRR {br['irr']*100:.1f}%")
    lines += ["", f"**Balance point: base ≈ {bb:.2f}** (always-invest {bb*100:.0f}% of salary, keep {(1-bb)*100:.0f}% as dry powder for −1σ dips) "
              f"→ **${br['final']:,.0f}, IRR {br['irr']*100:.1f}%**.", ""]
    return best


def main():
    lines = ["# Fixed-salary DCA + dry-powder dip-buying — where's the balance?", "",
             f"Fixed salary **${SALARY:,.0f}/yr**; un-deployed cash earns **{CASH_RATE_ANN*100:.0f}%**; "
             "dip trigger = price **≤ PIT −1σ** (real-time, no look-ahead).", ""]
    for sym, lab in [("^GSPC", "SPY"), ("^IXIC", "QQQ")]:
        run(sym, lab, lines)
    lines += ["---", "## Honest caveats",
              "- The balance point is **fit in-sample** on a 41-yr US bull (1985→). It is the wrong number for a flat market (Nikkei 1990→ would punish dry-powder hoarding for 30 yrs).",
              "- Cash rate held flat at 4%; real T-bills ranged ~0–8% over the window.",
              "- Price indices (ex-dividends): absolute wealth understates ~1.5–2%/yr; the cross-strategy comparison is unaffected.",
              "", "Built by `scripts/log_trend_dca_balance.py`."]
    (OUT / "dca_balance.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nsummary -> {OUT / 'dca_balance.md'}")


if __name__ == "__main__":
    main()
