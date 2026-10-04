#!/usr/bin/env python3
"""fetch_history.py — 英 / 日 / 中电力公司历史回顾的原始数据（可原地重跑）。

输出 data/：
  owid-energy-data.csv           Our World in Data 能源数据集（发电量 1985 起、一次能源 1965 起、电源结构）
  uk_electricity_since_1920.xlsx 英国政府 DUKES《Electricity since 1920》历史表
  prices_monthly.json            各股票 / 指数 / 总回报 ETF 的月末收盘（close = 仅拆股调整；adj = 含分红）
  dividends.json                 各股票逐笔分红（Yahoo events）
  prices_daily_tail.json         最近 30 个交易日日线（用于 as_of 价格核对）
  wb_cmo_monthly.xlsx            世界银行 Pink Sheet 月度商品价格（澳大利亚动力煤 $/t，1970-01 起；2026-10-02 版）
  boe_uk_macro_1900_2016.csv     英格兰银行《A millennium of macroeconomic data》A1 表摘录：CPI（2015=100）、Bank Rate、
                                 10 年期国债收益率、实际 GDP（原 xlsx 27.5MB 不入库，extract_boe() 按需下载并摘录）
时间戳：Yahoo 的月线 / 分红时间戳是交易所当地 0 点，换成 UTC 会落到前一天（东京、香港、上海、夏令时伦敦），
       导致月份标签整体早一个月 —— 一律先加 meta.gmtoffset 再取日期。
不可用的源（本环境）：stooq（需过 JS 人机验证，按规定不绕过）、FRED（HTTP 000）。
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
    # 日本
    "9501.T": "东京电力 TEPCO", "9503.T": "关西电力", "9508.T": "九州电力", "9513.T": "电源开发 J-POWER",
    "9502.T": "中部电力（参照）", "^N225": "日经 225（价格指数）", "1306.T": "TOPIX ETF（Yahoo 历史有未调整的拆股，本报告不用）",
    "1321.T": "日经 225 ETF（含息代理，Yahoo 历史 2009 起）",
    # 英国
    "NG.L": "National Grid", "SSE.L": "SSE", "^FTAS": "富时全股（价格指数）", "^FTSE": "富时 100（价格指数）",
    "ISF.L": "iShares 富时 100 ETF（总回报代理）",
    # 中国
    "600900.SS": "长江电力", "1816.HK": "中广核电力（H）", "003816.SZ": "中广核电力（A）", "600011.SS": "华能国际（A）",
    "0902.HK": "华能国际（H）", "0836.HK": "华润电力", "000001.SS": "上证综指（价格指数）", "^HSI": "恒生指数（价格指数）",
    "2800.HK": "盈富基金（恒指总回报代理）", "510300.SS": "沪深 300 ETF（总回报代理）",
}


def get(url, binary=False):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                b = r.read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def yahoo(tk, interval):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}?period1=0&period2=9999999999"
           f"&interval={interval}&events=div%2Csplits")
    r = json.loads(get(url))["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0) or 0
    ts = [t + off for t in (r.get("timestamp") or [])]
    q = r["indicators"]["quote"][0]
    adj = (r["indicators"].get("adjclose") or [{}])[0].get("adjclose") or [None] * len(ts)
    return r, ts, q["close"], adj


BOE_URL = ("https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/"
           "a-millennium-of-macroeconomic-data-for-the-uk.xlsx")


def extract_boe():
    """下载英格兰银行千年数据集（下载常在 ~11MB 处中断，需续传：建议 curl -C -），摘录 1900 起的 A1 表四列。"""
    import csv
    import subprocess
    import openpyxl
    x = DATA / "boe_millennium.xlsx"
    for _ in range(6):
        subprocess.run(["curl", "-s", "-L", "-A", "Mozilla/5.0", "-C", "-", "--max-time", "300", "-o", str(x), BOE_URL])
        try:
            wb = openpyxl.load_workbook(x, read_only=True, data_only=True)
            break
        except Exception:  # noqa: BLE001  未下完整，继续续传
            continue
    rows = list(wb["A1. Headline series"].iter_rows(values_only=True))
    out = []
    for r in rows[7:]:
        try:
            y = int(str(r[0]).strip())
        except ValueError:
            continue
        if y >= 1900:
            out.append({"year": y, "cpi": r[40], "bank_rate": r[44], "gilt_10y": r[46], "real_gdp_mn": r[1]})
    with (DATA / "boe_uk_macro_1900_2016.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    x.unlink()


def main():
    DATA.mkdir(exist_ok=True)
    if not (DATA / "owid-energy-data.csv").exists():
        # 只保留本研究用到的三国（全量约 9MB）
        import csv
        import io
        raw = get("https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv")
        rows = [r for r in csv.DictReader(io.StringIO(raw)) if r["country"] in ("Japan", "China", "United Kingdom")]
        with (DATA / "owid-energy-data.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
    (DATA / "wb_cmo_monthly.xlsx").write_bytes(get(
        "https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx",
        binary=True))
    (DATA / "uk_electricity_since_1920.xlsx").write_bytes(get(
        "https://assets.publishing.service.gov.uk/media/6a69e449229c578debc1a84d/Electricity_since_1920.xlsx", binary=True))
    monthly, divs, daily = {}, {}, {}
    for tk, name in TICKERS.items():
        try:
            r, ts, close, adj = yahoo(tk, "1mo")
        except Exception as e:  # noqa: BLE001
            print("FAIL", tk, e)
            continue
        m = {}
        for t, c, a in zip(ts, close, adj):
            if c is None:
                continue
            m[dt.datetime.utcfromtimestamp(t).strftime("%Y-%m")] = {"close": c, "adj": a}
        monthly[tk] = {"name": name, "currency": r["meta"].get("currency"), "series": m}
        ev = (r.get("events") or {}).get("dividends") or {}
        off = r["meta"].get("gmtoffset", 0) or 0
        divs[tk] = sorted((dt.datetime.utcfromtimestamp(int(v.get("date", k)) + off).strftime("%Y-%m-%d"), v["amount"])
                          for k, v in ev.items())
        try:
            rd, tsd, cd, ad = yahoo(tk, "1d")
            pts = [(dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"), c) for t, c in zip(tsd, cd) if c is not None]
            daily[tk] = pts[-30:]
        except Exception as e:  # noqa: BLE001
            daily[tk] = str(e)[:80]
        ks = sorted(m)
        print(f"{tk:10} {name:22} {ks[0]} -> {ks[-1]}  n={len(ks)}  divs={len(divs[tk])}  last_daily={daily[tk][-1] if isinstance(daily[tk], list) and daily[tk] else daily[tk]}")
        time.sleep(0.4)
    (DATA / "prices_monthly.json").write_text(json.dumps(monthly, ensure_ascii=False), encoding="utf-8")
    (DATA / "dividends.json").write_text(json.dumps(divs, ensure_ascii=False, indent=0), encoding="utf-8")
    (DATA / "prices_daily_tail.json").write_text(json.dumps(daily, ensure_ascii=False, indent=0), encoding="utf-8")


if __name__ == "__main__":
    main()
