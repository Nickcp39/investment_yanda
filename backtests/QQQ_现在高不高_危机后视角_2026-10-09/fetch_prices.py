#!/usr/bin/env python
"""Fetch daily history for QQQ, ^NDX, SPY, ^GSPC from Yahoo v8 chart API.
Same endpoint/field as backtests/SPY_QQQ_5年滚动回报_2026-07-25/.
Outputs data/<label>_daily.csv  (date,close,adj_close) + data/manifest.json
"""
import csv, datetime as dt, json, sys, urllib.request
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
HERE = Path(__file__).resolve().parent; DATA = HERE/"data"; DATA.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (research-lab qqq-level-check)"}
TPL = ("https://query1.finance.yahoo.com/v8/finance/chart/{s}?period1=0&period2={p2}"
       "&interval=1d&events=div%2Csplits&includeAdjustedClose=true")
SYMS = {"QQQ":"QQQ", "NDX":"^NDX", "SPY":"SPY", "GSPC":"^GSPC"}
p2 = int((dt.datetime.utcnow()+dt.timedelta(days=2)).timestamp())
man = {"fetched_utc": dt.datetime.utcnow().isoformat(timespec="seconds"), "series":{}}
for label, sym in SYMS.items():
    url = TPL.format(s=urllib.parse.quote(sym), p2=p2)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r: js = json.load(r)
    res = js["chart"]["result"][0]
    ts = res["timestamp"]; q = res["indicators"]["quote"][0]["close"]
    adj = res["indicators"]["adjclose"][0]["adjclose"]
    # drop an in-progress session: Yahoo appends today's live quote as a daily row while the market is open
    meta = res["meta"]; reg = meta.get("currentTradingPeriod", {}).get("regular", {})
    live = meta.get("regularMarketTime", 0) < reg.get("end", 0) and len(ts) and ts[-1] >= reg.get("start", 10**12)
    if live: ts, q, adj = ts[:-1], q[:-1], adj[:-1]; print(label, "dropped live in-progress row")
    rows = []
    for t, c, a in zip(ts, q, adj):
        if c is None or a is None: continue
        d = dt.datetime.utcfromtimestamp(t).date()
        rows.append((d.isoformat(), float(c), float(a)))
    out = DATA/f"{label}_daily.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["date","close","adj_close"]); w.writerows(rows)
    man["series"][label] = {"symbol":sym, "url":url, "rows":len(rows), "first":rows[0][0], "last":rows[-1][0],
                            "last_close":rows[-1][1], "currency":res["meta"].get("currency"),
                            "exchange":res["meta"].get("exchangeName")}
    print(label, sym, len(rows), rows[0][0], "->", rows[-1][0], "last close", rows[-1][1])
json.dump(man, open(DATA/"manifest.json","w",encoding="utf-8"), indent=2, ensure_ascii=False)
