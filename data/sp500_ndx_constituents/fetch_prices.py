#!/usr/bin/env python
"""Batch-fetch adjusted-close daily history for every historical S&P500 + Nasdaq-100
constituent ticker via Yahoo v8 chart API.

- Resumable: skips tickers already saved as prices/<ticker>.csv
- Saves one CSV per ticker: date,adj_close  (split+dividend adjusted)
- Records failures in fetch_failed.txt
"""
import csv, json, sys, time, urllib.parse, urllib.request, datetime as dt
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
PRICES = HERE / "prices"
PRICES.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (research-lab constituent-prices)"}
P1 = int(dt.datetime(1989, 1, 1).timestamp())  # pull from 1989 for safety


def load_tickers():
    tickers = set()
    with open(HERE / "sp500_historical_components.csv", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 2:
                continue
            for t in row[1].split(","):
                t = t.strip()
                if t:
                    tickers.add(t)
    with open(HERE / "ndx100_historical_components.csv", encoding="utf-8-sig") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if row and row[0].strip():
                tickers.add(row[0].strip())
    return sorted(tickers)


def fetch(ticker):
    p2 = int(dt.datetime.utcnow().timestamp()) + 86400 * 2
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(ticker)}"
        f"?period1={P1}&period2={p2}&interval=1d&events=div%2Csplits&includeAdjustedClose=true"
    )
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        js = json.load(r)
    res = js["chart"]["result"][0]
    ts = res["timestamp"]
    adj = res["indicators"]["adjclose"][0]["adjclose"]
    rows = []
    for t, a in zip(ts, adj):
        if a is None:
            continue
        d = dt.datetime.utcfromtimestamp(t).date()
        rows.append((d.isoformat(), round(float(a), 6)))
    return rows


def main():
    tickers = load_tickers()
    done = set(f.stem for f in PRICES.glob("*.csv"))
    todo = [t for t in tickers if t not in done]
    print(f"total={len(tickers)} done={len(done)} todo={len(todo)}", flush=True)

    failed = []
    ok = 0
    for i, t in enumerate(todo):
        safe = t.replace("/", "_").replace("\\", "_")
        try:
            rows = fetch(t)
            if not rows:
                failed.append((t, "empty"))
            else:
                with open(PRICES / f"{safe}.csv", "w", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    w.writerow(["date", "adj_close"])
                    w.writerows(rows)
                ok += 1
        except Exception as e:
            failed.append((t, str(e)[:70]))
        if (i + 1) % 25 == 0:
            print(f"progress {i+1}/{len(todo)} ok={ok} failed={len(failed)}", flush=True)
            time.sleep(0.6)

    with open(HERE / "fetch_failed.txt", "w", encoding="utf-8") as f:
        for t, e in failed:
            f.write(f"{t}\t{e}\n")
    print(f"DONE ok={ok} failed={len(failed)}", flush=True)
    for t, e in failed[:40]:
        print("FAIL", t, e)


if __name__ == "__main__":
    main()
