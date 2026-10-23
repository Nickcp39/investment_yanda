#!/usr/bin/env python
"""整理成分股名单为「每年年初成分股列表」格式，供冠军股回测使用。

输入:
  sp500_historical_components.csv  (fja05680: date,tickers 逐日快照)
  ndx100_historical_components.csv (unliftedq: symbol,name,opt-in,opt-out)
输出:
  sp500_yearly_constituents.csv    year,tickers(逗号分隔),n
  ndx100_yearly_constituents.csv   year,tickers(逗号分隔),n
"""
import csv, datetime as dt
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve().parent

def build_sp500():
    # fja05680: event-driven 快照 date,tickers（仅成分变动时记录，非逐日）。
    # 取「每年最早日期的快照」作为该年年初名单（1 月无变动时自动回退到该年首个变动日）。
    yearly = {}
    first_date = {}
    with open(HERE / "sp500_historical_components.csv", encoding="utf-8") as f:
        r = csv.reader(f); next(r)
        for row in r:
            if len(row) < 2:
                continue
            d = row[0].strip()
            try:
                ymd = dt.date.fromisoformat(d)
            except Exception:
                continue
            y = ymd.year
            if y not in first_date or ymd < first_date[y]:
                first_date[y] = ymd
                yearly[y] = row[1].strip()
    return yearly

def build_ndx():
    # unliftedq: symbol,name,opt-in,opt-out
    # 每年年初(1/1)在编 = opt-in <= 该年1/1 且 (opt-out 空 或 opt-out > 该年1/1)
    recs = []
    with open(HERE / "ndx100_historical_components.csv", encoding="utf-8-sig") as f:
        r = csv.reader(f); next(r)
        for row in r:
            if not row or not row[0].strip():
                continue
            sym = row[0].strip()
            optin = row[2].strip() if len(row) > 2 else ""
            optout = row[3].strip() if len(row) > 3 else ""
            recs.append((sym, optin, optout))
    # 确定年份范围
    years = range(2006, 2027)
    yearly = {}
    for y in years:
        jan1 = dt.date(y, 1, 1)
        members = []
        for sym, optin, optout in recs:
            try:
                di = dt.date.fromisoformat(optin) if optin else dt.date(1900,1,1)
            except Exception:
                continue
            if di > jan1:
                continue
            if optout:
                try:
                    do = dt.date.fromisoformat(optout)
                except Exception:
                    do = None
                if do and do <= jan1:
                    continue
            members.append(sym)
        yearly[y] = ",".join(sorted(members))
    return yearly

def write(path, yearly):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "tickers", "n"])
        for y in sorted(yearly):
            tk = yearly[y]
            n = len([t for t in tk.split(",") if t]) if tk else 0
            w.writerow([y, tk, n])

def main():
    sp = build_sp500()
    write(HERE / "sp500_yearly_constituents.csv", sp)
    print("标普500 逐年名单: %d 年  %s -> %s" % (len(sp), min(sp), max(sp)))
    for y in sorted(sp):
        print("  ", y, len([t for t in sp[y].split(',') if t]), "只")

    ndx = build_ndx()
    write(HERE / "ndx100_yearly_constituents.csv", ndx)
    print("纳指100 逐年名单: %d 年  %s -> %s" % (len(ndx), min(ndx), max(ndx)))
    for y in sorted(ndx):
        print("  ", y, len([t for t in ndx[y].split(',') if t]), "只")

if __name__ == "__main__":
    main()
