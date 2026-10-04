#!/usr/bin/env python3
"""fetch_data.py — 电力大国批次（日本 / 英国 / 中国 10 家）的行情与多年财务（可原地重跑）。

价格（LIVE，双源）：
  源 1  Yahoo chart API 日线，取 last close <= AS_OF
  源 2  CNBC quote API（日股、英股、港股、A 股）；CNBC 缺失时，日股用雅虎日本页面，A 股 / 港股用新浪行情
52 周高低：Yahoo 一年日线（盘中高低）。
多年财务（二手，供应商口径）：Yahoo fundamentals-timeseries（年度，约 4 年）—— 一手数字以各 dossier raw/ 中的公司原文为准。
SEC XBRL 不覆盖这些公司（非美国申报人）。
"""
from __future__ import annotations

import datetime as dt
import json
import re
import time
import urllib.request
from pathlib import Path

AS_OF = "2026-10-03"
OUT = Path(__file__).resolve().parent / "data"
UA = {"User-Agent": "Mozilla/5.0"}
COS = {  # yahoo: (名称, CNBC 代码, 地区)
    "9501.T": ("东京电力 TEPCO", "9501-JP", "JP"), "9503.T": ("关西电力", "9503-JP", "JP"),
    # 九州电力 9508 已于 2026-09 末退市：2026-10-01 以 1:1 单独股份转移成为 Kyuden Holdings（642A）全资子公司，
    # 新控股公司当日技术性上市（福冈证交所 2026-03-26 公告）。可投资标的 = 642A.T；Yahoo 的 642A.T 历史已拼接 9508。
    "642A.T": ("九州电力 → Kyuden Holdings", "642A-JP", "JP"), "9513.T": ("电源开发 J-POWER", "9513.T", "JP"),
    "NG.L": ("National Grid", "NG.-GB", "UK"), "SSE.L": ("SSE", "SSE-GB", "UK"),
    "600900.SS": ("长江电力", "600900-CN", "CN"), "1816.HK": ("中广核电力", "1816-HK", "HK"),
    "0902.HK": ("华能国际（H）", "902-HK", "HK"), "0836.HK": ("华润电力", "836-HK", "HK"),
}
FUND = ("annualTotalRevenue,annualOperatingIncome,annualNetIncomeCommonStockholders,annualOperatingCashFlow,"
        "annualCapitalExpenditure,annualFreeCashFlow,annualDepreciationAndAmortization,annualCashDividendsPaid,"
        "annualRepurchaseOfCapitalStock,annualIssuanceOfCapitalStock,annualTotalDebt,annualCashAndCashEquivalents,"
        "annualStockholdersEquity,annualOrdinarySharesNumber,annualInterestPaidCFF,annualInterestPaidCFO,"
        "annualStockBasedCompensation,annualPreferredStockDividends")


def get(url, headers=UA, enc="utf-8"):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
                return r.read().decode(enc, "replace")
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def yahoo_daily(tk):
    r = json.loads(get(f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}?range=1y&interval=1d"))["chart"]["result"][0]
    rows = [(dt.datetime.utcfromtimestamp(t).date(), c, h, lo) for t, c, h, lo in
            zip(r["timestamp"], r["indicators"]["quote"][0]["close"], r["indicators"]["quote"][0]["high"],
                r["indicators"]["quote"][0]["low"]) if c is not None]
    rows = [x for x in rows if x[0] <= dt.date.fromisoformat(AS_OF)]
    last = rows[-1]
    return {"last_close": round(last[1], 3), "last_close_date": str(last[0]), "currency": r["meta"].get("currency"),
            "wk52_high": round(max(x[2] for x in rows if x[2]), 3), "wk52_low": round(min(x[3] for x in rows if x[3]), 3),
            "close_1y_ago": round(rows[0][1], 3), "close_1y_ago_date": str(rows[0][0])}


def cnbc(sym):
    j = json.loads(get("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols="
                       f"{sym}&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json"))
    q = j["FormattedQuoteResult"]["FormattedQuote"][0]
    if not q.get("last"):
        return None
    return {"source": "cnbc", "last": float(q["last"].replace(",", "")), "date": q.get("last_time", "")[:10],
            "url": f"https://www.cnbc.com/quotes/{sym}"}


def yahoo_japan(tk):
    h = get(f"https://finance.yahoo.co.jp/quote/{tk}")
    m = re.search(r'"price":"([\d,\.]+)"', h)
    if not m:
        return None
    return {"source": "yahoo_japan", "last": float(m.group(1).replace(",", "")), "date": "",
            "url": f"https://finance.yahoo.co.jp/quote/{tk}"}


def sina(tk):
    code = ("sh" + tk.split(".")[0]) if tk.endswith(".SS") else ("hk0" + tk.split(".")[0]) if tk.endswith(".HK") else None
    if not code:
        return None
    t = get(f"https://hq.sinajs.cn/list={code}", headers={**UA, "Referer": "https://finance.sina.com.cn"}, enc="gbk")
    f = t.split('"')[1].split(",")
    if code.startswith("sh"):
        return {"source": "sina", "last": float(f[3]), "date": f[30], "url": f"https://hq.sinajs.cn/list={code}"}
    return {"source": "sina", "last": float(f[6]), "date": f[17].replace("/", "-"), "url": f"https://hq.sinajs.cn/list={code}"}


def fundamentals(tk):
    d = json.loads(get(f"https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{tk}"
                       f"?type={FUND}&period1=1420070400&period2=1790000000"))
    out = {}
    for res in d["timeseries"]["result"]:
        t = res["meta"]["type"][0]
        out[t] = {v["asOfDate"]: v["reportedValue"]["raw"] for v in (res.get(t) or []) if v}
    return out


def main():
    OUT.mkdir(exist_ok=True)
    snap = {"as_of": AS_OF, "fetched_at": dt.datetime.now().isoformat(timespec="seconds"), "tickers": {}}
    for tk, (name, csym, region) in COS.items():
        rec = {"name": name, "region": region, "yahoo": yahoo_daily(tk)}
        src2 = None
        if csym:
            try:
                src2 = cnbc(csym)
            except Exception:  # noqa: BLE001
                src2 = None
        if not src2 and region == "JP":
            src2 = yahoo_japan(tk)
        if not src2 and region in ("CN", "HK"):
            src2 = sina(tk)
        rec["second_source"] = src2
        rec["fundamentals"] = fundamentals(tk)
        snap["tickers"][tk] = rec
        y = rec["yahoo"]
        print(f"{tk:10} {name:14} yahoo {y['last_close']} ({y['last_close_date']}) | 2nd {src2} | 52w {y['wk52_low']}-{y['wk52_high']}")
        time.sleep(0.5)
    (OUT / f"snapshot_{AS_OF}.json").write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
