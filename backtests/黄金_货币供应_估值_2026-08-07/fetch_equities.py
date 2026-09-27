#!/usr/bin/env python
"""Pull the equity benchmarks gold has to beat.

Source: Yahoo Finance v8 chart API, adjusted close (splits + dividends reinvested),
the same endpoint and field used by backtests/SPY_QQQ_5年滚动回报_2026-07-25/.

  SPY       S&P 500 ETF, total return           1993-01-29 ->
  QQQ       Nasdaq-100 ETF, total return        1999-03-10 ->
  SP500TR   S&P 500 Total Return index          1988-01-04 ->   (extends SPY by 5 years)
  GSPC      S&P 500 price index, NO dividends   1970-01-02 ->   (only way to reach the
                                                                 1970s gold bull; flatters
                                                                 gold by the dividend yield)

Outputs: data/<LABEL>_daily_adjusted.csv  (date,adj_close)
         data/equity_manifest.json

Re-run: python fetch_equities.py
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
DATA.mkdir(parents=True, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (research-lab gold-vs-equities)"}
TEMPLATE = ("https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            "?period1=0&period2={period2}&interval=1d&events=div%2Csplits"
            "&includeAdjustedClose=true")

SERIES = {
    "SPY": ("SPY", "S&P 500 ETF, adjusted close (dividends reinvested)"),
    "QQQ": ("QQQ", "Nasdaq-100 ETF, adjusted close (dividends reinvested)"),
    "SP500TR": ("%5ESP500TR", "S&P 500 Total Return index"),
    "GSPC": ("%5EGSPC", "S&P 500 price index - EXCLUDES dividends"),
}


def fetch(symbol: str) -> tuple[list[tuple[str, float]], str]:
    period2 = int(dt.datetime.now().timestamp()) + 86400 * 2
    url = TEMPLATE.format(symbol=symbol, period2=period2)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as resp:
        body = json.loads(resp.read().decode("utf-8"))

    if body["chart"].get("error"):
        raise RuntimeError(f"{symbol}: {body['chart']['error']}")

    result = body["chart"]["result"][0]
    stamps = result["timestamp"]
    adj = result["indicators"]["adjclose"][0]["adjclose"]

    rows = []
    for stamp, value in zip(stamps, adj):
        if value is None:
            continue
        day = dt.datetime.utcfromtimestamp(stamp).strftime("%Y-%m-%d")
        rows.append((day, float(value)))
    rows.sort()
    return rows, url


def main() -> int:
    manifest = {"fetched_at": dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z"),
                "series": []}

    for label, (symbol, description) in SERIES.items():
        rows, url = fetch(symbol)
        path = DATA / f"{label}_daily_adjusted.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["date", "adj_close"])
            writer.writerows(rows)
        print(f"{label:<8} {len(rows):>6,} rows  {rows[0][0]} -> {rows[-1][0]}  "
              f"last = {rows[-1][1]:,.2f}")
        manifest["series"].append({
            "file": f"data/{label}_daily_adjusted.csv", "symbol": symbol,
            "name": description, "url": url, "rows": len(rows),
            "first": rows[0][0], "last": rows[-1][0],
        })

    (DATA / "equity_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nwrote data/equity_manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
