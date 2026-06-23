#!/usr/bin/env python
"""Backtest: does DCA-only-below-the-log-trend-band 'basically always win'?

Answers the user's question on LONG data (S&P 500 ^GSPC ~1950, Nasdaq ^IXIC ~1971),
and exposes the trap: the log-trend "fair value" line is normally fit on the WHOLE
history (including the future) -> using it as a buy signal is LOOK-AHEAD CHEATING.
So we compute the trend two ways:
  * PIT  = point-in-time / expanding window: at each month, fit using ONLY past data
           (>=120-month warmup). This is the honest, tradeable signal.
  * FULL = whole-sample fit (knows the future). Shown only to demonstrate the cheat.

Strategies (contribute $1 each month; skipped $ goes to cash @ 0%):
  S0  DCA always (baseline)
  S1  buy only when price <= PIT trend            (below the line)
  S2  buy only when price <= PIT trend - 1 sigma  ("below the std", what user asked)
  S3  buy only when price <= PIT trend - 2 sigma  (deep crash only)
  S4  DCA always, DOUBLE the buy when <= PIT -1 sigma   (the realistic overlay)
  SX  buy only when price <= FULL trend - 1 sigma  (LOOK-AHEAD; the cheat, for contrast)

Metrics: total contributed, final value, money-weighted IRR (annualized),
% of months it actually buys (cash drag), and the "稳赢" test = of all the buy
lots, what % are in profit today + the worst lot's deepest drawdown.

Note: ^GSPC/^IXIC are PRICE indices (ex-dividends) -> absolute returns understate
~1.5-2%/yr, but the RELATIVE comparison between strategies is unaffected.
"""
from __future__ import annotations
import sys, json, math, urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "macro" / "market_panel" / "data"
OUT = ROOT / "macro" / "market_panel" / "log_trend"
OUT.mkdir(parents=True, exist_ok=True)
WARMUP = 120  # months of history required before the PIT trend is usable


def fetch_yahoo_monthly(symbol: str) -> pd.DataFrame | None:
    sym = symbol.replace("^", "%5E")
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?period1=-631152000&period2=9999999999&interval=1mo")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            j = json.load(r)
        res = j["chart"]["result"][0]
        ts = res["timestamp"]
        ind = res["indicators"]
        vals = (ind.get("adjclose", [{}])[0].get("adjclose")
                or ind["quote"][0]["close"])
        df = pd.DataFrame({"date": pd.to_datetime(ts, unit="s"), "value": vals})
        df = df.dropna()
        df = df[df["value"] > 0].reset_index(drop=True)
        return df if len(df) > WARMUP else None
    except Exception as e:  # noqa: BLE001
        print(f"  (fetch {symbol} failed: {e})")
        return None


def load_local_monthly(label: str) -> pd.DataFrame:
    df = pd.read_csv(PANEL / f"{label}.csv")
    c = list(df.columns)
    df = df.rename(columns={c[0]: "date", c[1]: "value"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna().set_index("date").resample("ME").last().dropna().reset_index()
    return df


def pit_dev(values: np.ndarray):
    """Expanding-window log-trend deviation in sigma, real-time (no look-ahead)."""
    n = len(values)
    y = np.log(values)
    t = np.arange(n, dtype=float)
    dev = np.full(n, np.nan)
    for i in range(WARMUP, n):
        b, a = np.polyfit(t[: i + 1], y[: i + 1], 1)
        resid = y[: i + 1] - (a + b * t[: i + 1])
        s = resid.std(ddof=1)
        if s:
            dev[i] = (y[i] - (a + b * t[i])) / s
    return dev


def full_dev(values: np.ndarray):
    y = np.log(values); t = np.arange(len(values), dtype=float)
    b, a = np.polyfit(t, y, 1)
    resid = y - (a + b * t)
    return resid / resid.std(ddof=1)


def irr_monthly(cashflows: list[float]) -> float:
    """Annualized IRR from a monthly cashflow stream (last entry = liquidation).
    Bracket kept sane (monthly -5%..+5%) so (1+r)**k can't under/overflow."""
    lo, hi = -0.05, 0.05
    def npv(r):
        df = 1.0 / (1.0 + r)
        return sum(cf * df ** k for k, cf in enumerate(cashflows))
    flo, fhi = npv(lo), npv(hi)
    if flo * fhi > 0 or not math.isfinite(flo) or not math.isfinite(fhi):
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid) > 0: lo = mid
        else: hi = mid
    return (1 + (lo + hi) / 2) ** 12 - 1


def simulate(values, buy_units):
    """buy_units[i] = how many $ to invest in the index that month (rest -> cash)."""
    n = len(values); shares = 0.0; cash = 0.0
    lots = []  # (price,) of index purchases
    cfs = []
    for i in range(n):
        contrib = 1.0 + (1.0 if buy_units[i] > 1 else 0.0)  # S4 doubles -> contrib 2
        invest = buy_units[i]
        if invest > 0:
            shares += invest / values[i]
            lots.append(values[i])
        cash += contrib - invest
        cfs.append(-contrib)
    final = shares * values[-1] + cash
    cfs.append(final)
    contributed = sum(c for c in (-x for x in cfs[:-1]))
    last = values[-1]
    lots = np.array(lots) if lots else np.array([np.nan])
    win = float(np.mean(lots <= last)) if len(lots) and not np.isnan(lots[0]) else float("nan")
    return {
        "contributed": contributed, "final": final, "mult": final / contributed,
        "irr": irr_monthly(cfs), "buy_pct": float(np.mean(np.asarray(buy_units) > 0)),
        "lot_win": win, "n_lots": int(np.sum(~np.isnan(lots))),
    }


def run(symbol, label, lines):
    df = fetch_yahoo_monthly(symbol)
    src = symbol
    if df is None:
        df = load_local_monthly(label); src = f"{label} (local 2010+, fetch blocked)"
    v = df["value"].values
    dpit = pit_dev(v); dfull = full_dev(v)
    last_date = df["date"].iloc[-1].date()
    yrs = (df["date"].iloc[-1] - df["date"].iloc[0]).days / 365.25

    # buy_units arrays
    ones = np.ones(len(v))
    def gate(mask):  # invest $1 only where mask True (and past warmup)
        u = np.where(mask & ~np.isnan(dpit), 1.0, 0.0); u[:WARMUP] = 0.0; return u
    strat = {
        "S0 DCA always":            ones.copy(),
        "S1 <= PIT trend":          gate(dpit <= 0),
        "S2 <= PIT -1σ":            gate(dpit <= -1),
        "S3 <= PIT -2σ":            gate(dpit <= -2),
        "S4 always +2x<-1σ":        np.where((~np.isnan(dpit)) & (dpit <= -1), 2.0, 1.0),
        "SX <= FULL -1σ (CHEAT)":   np.where(dfull <= -1, 1.0, 0.0),
    }
    print(f"\n=== {src}  ({df['date'].iloc[0].date()} → {last_date}, {yrs:.0f}y, {len(v)} mo) ===")
    print(f"{'strategy':<24}{'buys%':>6}{'contrib':>9}{'final':>9}{'mult':>6}{'IRR':>7}{'lot win%':>9}")
    lines += [f"## {src} — {df['date'].iloc[0].date()} → {last_date} ({yrs:.0f}y)", "",
              "| strategy | buys % of mo | contributed | final value | multiple | IRR (ann) | lots in profit |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for name, u in strat.items():
        r = simulate(v, u)
        print(f"{name:<24}{r['buy_pct']*100:>5.0f}%{r['contributed']:>9.0f}{r['final']:>9.0f}"
              f"{r['mult']:>6.2f}{r['irr']*100:>6.1f}%{r['lot_win']*100:>8.0f}%")
        lines.append(f"| {name} | {r['buy_pct']*100:.0f}% | ${r['contributed']:.0f} | "
                     f"${r['final']:.0f} | {r['mult']:.2f}x | {r['irr']*100:.1f}% | {r['lot_win']*100:.0f}% |")
    lines.append("")
    return last_date


def main():
    lines = ["# DCA below the log-trend band — does it 'always win'?", ""]
    for sym, lab in [("^GSPC", "SPY"), ("^IXIC", "QQQ")]:
        run(sym, lab, lines)
    lines += [
        "---", "## Read this before believing any 稳赢 claim",
        "- **Look-ahead**: `SX (CHEAT)` uses the full-sample trend (knows the future) — it looks great and is **not tradeable**. Compare it to `S2 (<= PIT -1σ)`, the honest real-time version.",
        "- **Cash drag + rarity**: dip-only strategies (S1–S3) sit in cash for years in a melt-up, so on EQUAL contributions they can LOSE to plain DCA (S0) on final value even though each buy is cheaper. `S4 (always + double the dip)` is the realistic way to use the band.",
        "- **Regime/survivorship**: this works because the US index trended up and always recovered. Buying 'below trend' on Japan's Nikkei from 1990, or Nasdaq from 2000, left you underwater for 10–30 years — the index-level version of the value trap.",
        "", f"Built by `scripts/log_trend_dca_backtest.py`. PIT warmup = {WARMUP} mo. Price indices (ex-dividends)."]
    (OUT / "dca_backtest.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nsummary -> {OUT / 'dca_backtest.md'}")


if __name__ == "__main__":
    main()
