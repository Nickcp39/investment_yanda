#!/usr/bin/env python
"""Same fixed-salary DCA-vs-dry-powder test, but run separately over three start
windows (1995 / 2005 / 2015 -> today) to see if "all-in your salary" stays optimal
across regimes. The -1σ trend signal is computed point-in-time off the FULL history
(what the investor would actually have); only the salary simulation is windowed.

Salary = 1万/月 (10,000/mo); un-deployed cash @ 4%/yr; dip trigger = PIT <= -1σ.
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
INC = 10_000.0
CR = (1 + 0.04) ** (1 / 12) - 1
THRESH = -1.0
STARTS = ["1995-01-01", "2005-01-01", "2015-01-01"]


def irr(cfs):
    lo, hi = -0.05, 0.05
    f = lambda r: sum(c / (1 + r) ** k for k, c in enumerate(cfs))  # noqa: E731
    if not math.isfinite(f(lo)) or f(lo) * f(hi) > 0:
        return float("nan")
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) > 0 else (lo, m)
    return (1 + (lo + hi) / 2) ** 12 - 1


def simulate(v, dev, start_i, base, dip_deploy):
    n = len(v); cash = 0.0; shares = 0.0; cfs = []
    for i in range(start_i, n):
        cash = cash * (1 + CR) + INC
        cfs.append(-INC)
        inv = min(base * INC, cash); cash -= inv; shares += inv / v[i]
        if dip_deploy > 0 and not np.isnan(dev[i]) and dev[i] <= THRESH:
            extra = dip_deploy * cash; cash -= extra; shares += extra / v[i]
    final = shares * v[-1] + cash
    cfs.append(final)
    return {"final": final, "irr": irr(cfs)}


def best_base(v, dev, start_i):
    grid = [0.0, 0.25, 0.5, 0.75, 0.9, 1.0]
    rs = {b: simulate(v, dev, start_i, b, 1.0) for b in grid}
    bb = max(grid, key=lambda b: rs[b]["final"])
    return bb, rs


def run(symbol, label, lines):
    df = fetch_yahoo_monthly(symbol)
    src = symbol
    if df is None:
        df = load_local_monthly(label); src = f"{label}(local)"
    v = df["value"].values
    dev = pit_dev(v)
    dates = df["date"]
    print(f"\n############ {src} ############")
    lines.append(f"## {src}")
    for start in STARTS:
        si = int((dates >= start).values.argmax())
        if not (dates >= start).any():
            continue
        months = len(v) - si
        total_in = INC * months
        dca = simulate(v, dev, si, 1.0, 0.0)        # pure all-in
        dip = simulate(v, dev, si, 0.0, 1.0)        # pure dry-powder dip-buyer
        bb, rs = best_base(v, dev, si)
        winner = "ALL-IN" if dca["final"] >= dip["final"] else "DRY-POWDER"
        edge = dca["final"] / dip["final"] - 1
        print(f"\n  [{start[:4]}→now]  {months} mo, in {total_in/1e6:.2f}M")
        print(f"     all-in (base1)  final {dca['final']/1e6:>7.2f}M  IRR {dca['irr']*100:>5.1f}%")
        print(f"     pure-dip(base0) final {dip['final']/1e6:>7.2f}M  IRR {dip['irr']*100:>5.1f}%")
        print(f"     best base = {bb}  final {rs[bb]['final']/1e6:>7.2f}M  IRR {rs[bb]['irr']*100:>5.1f}%")
        print(f"     >> winner: {winner}  (all-in vs dip edge {edge*100:+.0f}%)")
        lines += [
            f"### {start[:4]} → now  ({months} mo, salary in ${total_in/1e6:.2f}M)",
            "| strategy | final | IRR |", "|---|---:|---:|",
            f"| all-in (deploy every paycheck) | ${dca['final']/1e6:.2f}M | {dca['irr']*100:.1f}% |",
            f"| pure dip (hoard, dump on −1σ) | ${dip['final']/1e6:.2f}M | {dip['irr']*100:.1f}% |",
            f"| **best base={bb:.2f}** (keep {(1-bb)*100:.0f}% dry powder) | **${rs[bb]['final']/1e6:.2f}M** | {rs[bb]['irr']*100:.1f}% |",
            f"\n**Winner: {winner}** — all-in vs pure-dip edge **{edge*100:+.0f}%**. "
            f"Optimal always-in fraction = **{bb:.0%}**.\n"]


def main():
    lines = ["# All-in vs dry-powder, by start window (salary 1万/月, cash@4%, −1σ trigger)", ""]
    for sym, lab in [("^GSPC", "SPY"), ("^IXIC", "QQQ")]:
        run(sym, lab, lines)
    lines += ["---",
              "Trend signal is point-in-time off full 1985+ history (no look-ahead); only the salary sim is windowed.",
              "Price indices (ex-dividends). Cash flat 4% (real T-bills varied)."]
    (OUT / "dca_windows.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nsummary -> {OUT / 'dca_windows.md'}")


if __name__ == "__main__":
    main()
