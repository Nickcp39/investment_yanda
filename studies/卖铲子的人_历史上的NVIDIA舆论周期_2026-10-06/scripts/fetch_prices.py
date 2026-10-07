#!/usr/bin/env python3
"""fetch_prices.py — "卖铲子的人"舆论周期研究的股价数据（可原地重跑）。

输出 data/prices_monthly.json：各股票月末收盘（close = 仅拆股调整；adj = Yahoo 含分红调整，仅作参考）。
时间戳：Yahoo 月线时间戳是交易所当地 0 点，先加 meta.gmtoffset 再取日期（否则东京 / 上海月份标签早一个月）。
20 家里只有 11 家（含 Cisco / NVIDIA 参照）有可下载的连续月线；18–19 世纪的合伙制公司、RCA（1986 年被 GE 收购）、
Marconi（2006 年退市）、尚德（2014 年从纽交所摘牌）没有可用的免费连续数据，报告里用文献中的价格点代替。
"""
from __future__ import annotations

import datetime as dt
import json
import time
import urllib.request
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
UA = {"User-Agent": "Mozilla/5.0"}
TICKERS = {
    "CSCO": "思科", "NVDA": "英伟达", "INTC": "英特尔", "IBM": "IBM", "GE": "通用电气（2024 年拆分后为 GE Aerospace）",
    "ERIC": "爱立信（ADR）", "SIE.DE": "西门子", "6701.T": "NEC", "7011.T": "三菱重工", "6201.T": "丰田自动织机",
    "600150.SS": "中国船舶", "601766.SS": "中国中车（原中国南车）",
    "^GSPC": "标普 500", "^IXIC": "纳斯达克综指", "^N225": "日经 225", "000001.SS": "上证综指",
}


def get(url):
    err = None
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def yahoo(tk):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}?period1=0&period2=9999999999"
           f"&interval=1mo&events=div%2Csplits")
    r = json.loads(get(url))["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0) or 0
    ts = [t + off for t in (r.get("timestamp") or [])]
    q = r["indicators"]["quote"][0]
    adj = (r["indicators"].get("adjclose") or [{}])[0].get("adjclose") or [None] * len(ts)
    return r, ts, q["close"], adj


def main():
    DATA.mkdir(exist_ok=True)
    out = {}
    for tk, name in TICKERS.items():
        try:
            r, ts, close, adj = yahoo(tk)
        except Exception as e:  # noqa: BLE001
            print("FAIL", tk, e)
            continue
        m = {}
        for t, c, a in zip(ts, close, adj):
            if c is not None:
                m[dt.datetime.utcfromtimestamp(t).strftime("%Y-%m")] = {"close": c, "adj": a}
        ks = sorted(m)
        out[tk] = {"name": name, "currency": r["meta"].get("currency"), "series": m}
        print(f"{tk:10} {ks[0]} -> {ks[-1]}  n={len(ks)}  last={m[ks[-1]]['close']:.2f}")
        time.sleep(0.4)
    (DATA / "prices_monthly.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
