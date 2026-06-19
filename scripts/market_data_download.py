#!/usr/bin/env python3
"""Download a reusable market + macro indicator panel to Excel + CSV.

Primary source (works in this environment):
  * Yahoo Finance v8 chart API -> equities, commodities, crypto, FX, CBOE rate indices,
    and credit-risk ETF proxies (HYG/LQD).
Merged from local repo data:
  * macro/us_japan_yield_curve_sp500 -> US/Japan 2Y+10Y yields, term spread, US-JP 10Y diff
    (daily since 2020). This is how 美日利差 / term-spread enter the panel.
Best-effort (currently BLOCKED here -> logged as FAIL, fills in when run from an open network):
  * FRED fredgraph.csv -> longer-history yields + true high-yield OAS credit spread.

Outputs under macro/market_panel/:
  * data/<LABEL>.csv  -> one tidy CSV per series (date,value)
  * market_panel.xlsx -> sheets: metadata | daily (wide, aligned) | us_japan_yield_gap

Re-run : .venv/Scripts/python.exe scripts/market_data_download.py --start 2010-01-01
Extend : add a row to YAHOO or FRED below and re-run (idempotent overwrite).
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import pandas as pd

REPO = Path(__file__).resolve().parents[1]
OUTDIR = REPO / "macro" / "market_panel"
USJP_CSV = REPO / "macro" / "us_japan_yield_curve_sp500" / "data" / "us_japan_yield_gaps_vs_sp500_recent.csv"
UA = {"User-Agent": "Mozilla/5.0 (financial-analysis-lab market_data_download)"}
NET_ERRORS = (HTTPError, URLError, OSError, KeyError, ValueError, IndexError, pd.errors.EmptyDataError)

# LABEL -> (yahoo_symbol, category, description, unit)
YAHOO = {
    "SPY":       ("SPY",      "equity_index", "S&P 500 ETF (adj close, div-reinvested)", "USD"),
    "QQQ":       ("QQQ",      "equity_index", "Nasdaq-100 ETF (adj close, div-reinvested)", "USD"),
    "IWM":       ("IWM",      "equity_index", "Russell 2000 small-cap ETF (adj close)", "USD"),
    "SOXX":      ("SOXX",     "equity_index", "iShares Semiconductor ETF (adj close)", "USD"),
    "GOLD":      ("GC=F",     "commodity",    "Gold front-month futures (COMEX)", "USD/oz"),
    "WTI":       ("CL=F",     "commodity",    "WTI crude front-month futures (NYMEX)", "USD/bbl"),
    "BRENT":     ("BZ=F",     "commodity",    "Brent crude front-month futures (ICE)", "USD/bbl"),
    "BTC":       ("BTC-USD",  "crypto",       "Bitcoin spot (USD)", "USD"),
    "DXY":       ("DX-Y.NYB", "fx",           "US Dollar Index (ICE)", "index"),
    "USDJPY":    ("JPY=X",    "fx",           "USD/JPY spot", "JPY per USD"),
    "US5Y_FVX":  ("^FVX",     "rate",         "US 5Y Treasury yield (CBOE, in percent)", "pct"),
    "US10Y_TNX": ("^TNX",     "rate",         "US 10Y Treasury yield (CBOE, in percent)", "pct"),
    "US30Y_TYX": ("^TYX",     "rate",         "US 30Y Treasury yield (CBOE, in percent)", "pct"),
    "HYG":       ("HYG",      "credit",       "iShares HY corp-bond ETF (credit-risk proxy, adj close)", "USD"),
    "LQD":       ("LQD",      "credit",       "iShares IG corp-bond ETF (adj close)", "USD"),
    # --- common trader-desk indices / instruments ---
    "VIX":       ("^VIX",     "volatility",   "CBOE Volatility Index (S&P 500 implied vol, fear gauge)", "index"),
    "DOW":       ("^DJI",     "equity_index", "Dow Jones Industrial Average", "index"),
    "RUT":       ("^RUT",     "equity_index", "Russell 2000 index level", "index"),
    "EURUSD":    ("EURUSD=X", "fx",           "EUR/USD spot (most-traded pair)", "USD per EUR"),
    "GBPUSD":    ("GBPUSD=X", "fx",           "GBP/USD spot (cable)", "USD per GBP"),
    "COPPER":    ("HG=F",     "commodity",    "Copper front-month futures (Dr. Copper)", "USD/lb"),
    "SILVER":    ("SI=F",     "commodity",    "Silver front-month futures", "USD/oz"),
    "NATGAS":    ("NG=F",     "commodity",    "Henry Hub natural gas futures", "USD/MMBtu"),
    "ETH":       ("ETH-USD",  "crypto",       "Ethereum spot (USD)", "USD"),
    "TLT":       ("TLT",      "rate",         "iShares 20+ Year Treasury Bond ETF (adj close)", "USD"),
}
# LABEL -> (fred_id, category, description, unit)   [best-effort; blocked in this env]
FRED = {
    "US2Y_FRED":     ("DGS2",         "rate",   "US 2Y Treasury constant maturity (long history)", "pct"),
    "SPREAD_10Y2Y":  ("T10Y2Y",       "spread", "Term spread: US 10Y minus 2Y (long history)", "pct"),
    "SPREAD_HY_OAS": ("BAMLH0A0HYM2", "spread", "ICE BofA US High-Yield OAS (true credit spread)", "pct"),
}


def _epoch(d: str) -> int:
    return int(time.mktime(dt.datetime.strptime(d, "%Y-%m-%d").timetuple()))


def _retry(fn, *a, attempts=3, backoff=2.0):
    last = None
    for i in range(attempts):
        try:
            return fn(*a)
        except NET_ERRORS as e:
            last = e
            if i < attempts - 1:
                time.sleep(backoff * (i + 1))
    raise last


def fetch_yahoo(symbol: str, start: str, end: str) -> pd.Series:
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(symbol, safe='^=.-')}"
        f"?period1={_epoch(start)}&period2={_epoch(end)}&interval=1d"
        f"&events=div%2Csplits&includeAdjustedClose=true"
    )
    with urlopen(Request(url, headers=UA), timeout=30) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    ts = res["timestamp"]
    quote_block = res["indicators"]["quote"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
    vals = adj if adj else quote_block.get("close")
    idx = [dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d") for t in ts]
    s = pd.Series(vals, index=idx, name="value").astype("float64")
    return s[~s.index.duplicated(keep="last")].dropna()


def fetch_fred(series_id: str) -> pd.Series:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    with urlopen(Request(url, headers=UA), timeout=15) as r:
        raw = r.read().decode("utf-8")
    if not raw.strip():
        raise ValueError("empty FRED body (blocked in this environment)")
    df = pd.read_csv(io.StringIO(raw))
    datecol, valcol = df.columns[0], df.columns[1]
    s = pd.Series(pd.to_numeric(df[valcol], errors="coerce").values,
                  index=df[datecol].astype(str), name="value")
    return s.dropna()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--start", default="2010-01-01", help="YYYY-MM-DD (default 2010-01-01)")
    ap.add_argument("--end", default=dt.date.today().isoformat(), help="YYYY-MM-DD (default today)")
    ap.add_argument("--no-fred", action="store_true", help="skip the (currently blocked) FRED pulls")
    args = ap.parse_args()

    (OUTDIR / "data").mkdir(parents=True, exist_ok=True)
    series: dict[str, pd.Series] = {}
    meta: list[dict] = []

    plan = [("yahoo", k, *v) for k, v in YAHOO.items()]
    if not args.no_fred:
        plan += [("fred", k, *v) for k, v in FRED.items()]

    for source, label, ident, category, desc, unit in plan:
        try:
            if source == "yahoo":
                s = _retry(fetch_yahoo, ident, args.start, args.end)
            else:
                s = _retry(fetch_fred, ident, attempts=2, backoff=1.0)
            s = s[s.index >= args.start]
            if s.empty:
                raise ValueError("no rows in range")
            s.rename("value").to_csv(OUTDIR / "data" / f"{label}.csv", index_label="date")
            series[label] = s
            meta.append(dict(label=label, category=category, source=source, ticker_id=ident,
                             description=desc, unit=unit, frequency="daily",
                             first=s.index.min(), last=s.index.max(), n_obs=int(s.shape[0])))
            print(f"  OK  {label:14s} {source:5s} {ident:14s} {s.shape[0]:>5} rows  {s.index.min()}..{s.index.max()}")
        except NET_ERRORS as e:
            print(f"  FAIL {label:14s} {source:5s} {ident:14s} -> {type(e).__name__}: {e}")

    if not series:
        print("ERROR: no series fetched; aborting.")
        return 1

    wide = pd.concat(series, axis=1)
    wide.index = pd.to_datetime(wide.index)
    wide = wide.sort_index()
    wide.index.name = "date"

    usjp = pd.DataFrame()
    if USJP_CSV.exists():
        usjp = pd.read_csv(USJP_CSV)
        meta.append(dict(label="USJP_yield_gap", category="spread", source="local",
                         ticker_id=str(USJP_CSV.relative_to(REPO)).replace("\\", "/"),
                         description="US/JP 2Y+10Y yields, term spreads, US-JP 10Y diff (DIFF_10Y)",
                         unit="pct", frequency="daily",
                         first=str(usjp["DATE"].min()), last=str(usjp["DATE"].max()), n_obs=len(usjp)))

    meta_df = pd.DataFrame(meta, columns=["label", "category", "source", "ticker_id",
                                          "description", "unit", "frequency", "first", "last", "n_obs"])

    xlsx = OUTDIR / "market_panel.xlsx"
    with pd.ExcelWriter(xlsx, engine="openpyxl") as xl:
        meta_df.to_excel(xl, sheet_name="metadata", index=False)
        wide.to_excel(xl, sheet_name="daily")
        if not usjp.empty:
            usjp.to_excel(xl, sheet_name="us_japan_yield_gap", index=False)

    print(f"\nWrote {xlsx}  ({wide.shape[0]} daily rows x {wide.shape[1]} series)")
    print(f"Per-series CSVs in {OUTDIR / 'data'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
