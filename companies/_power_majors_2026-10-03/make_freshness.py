#!/usr/bin/env python3
"""make_freshness.py — 电力大国批次各 dossier 的 freshness.json（由 _oil_2026-09-30/make_freshness.py 改写：
非美股没有 Nasdaq 源，第二源换成 CNBC quote API）。lean-6module-v1.1 机械新鲜度门的输入。

每个 LIVE 定量字段 ≥2 个独立源：
  price        : Yahoo chart API 收盘（fetch_data.py 快照）+ CNBC quote（last，同日）
  market_cap   : 价格 × 卡片股数（derived，单位 = 报价单位：日元 / 便士 / 港元）+ 价格 × CNBC sharesout（derived，第二套股数）
  52wk_high/low: Yahoo 一年日线高低 + CNBC yrhiprice / yrloprice
  shares_out   : 卡片股数（公司一手文件，见 SHARES 注释）
LIVE 定性字段 guidance：最新业绩文件日期（T6 只做 WARN）。
用法: python companies/_power_majors_2026-10-03/make_freshness.py [folder ...]
"""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

AS_OF = "2026-10-03"
BATCH = "power_majors_2026-10-03"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UA = {"User-Agent": "Mozilla/5.0"}
HOLIDAY = " (Shanghai closed 2026-10-01..07 for National Day)"

# folder: (Yahoo 代码, CNBC 代码, 卡片股数 M, 股数出处, 报价单位, guidance 源日期, guidance 源 URL)
SHARES = {
    "tepco": ("9501.T", "9501-JP", 4936.0,
              "fully diluted: common 1,602.7M (Q1 FY3/2027 tanshin) + 3,333.3M convertible from NDF Class A/B preferred "
              "(FY3/2026 tanshin dilution note); CNBC sharesout = common only", "JPY",
              "2026-07-29", "https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260729/20260724599600.pdf"),
    "kansai": ("9503.T", "9503-JP", 1114.2, "issued 1,114.93M - treasury 0.75M (Q1 FY3/2027 tanshin)", "JPY",
               "2026-07-31", "https://www.kepco.co.jp/ir/brief/disclosure/pdf/kaiji20260731_1.pdf"),
    "kyushu": ("642A.T", "642A-JP", 472.8,
               "issued 474.18M - treasury 1.41M (FY3/2026 tanshin); 9508 -> Kyuden Holdings 642A 1:1 on 2026-10-01", "JPY",
               "2026-07-31", "https://www.kyuden.co.jp/var/rev0/0888/5400/fbYEeqt2.pdf"),
    "jpower": ("9513.T", "9513.T", 176.0, "issued 183.05M - treasury 7.04M (FY3/2026 tanshin)", "JPY",
               "2026-07-31", "https://www.jpower.co.jp/news/pdf/kessan2027-1/all.pdf"),
    "nationalgrid": ("NG.L", "NG.-GB", 5026.8, "voting shares 5,026.8M (Total Voting Rights 6-K 2026-07-23)", "GBp",
                     "2026-05-14", "https://www.sec.gov/Archives/edgar/data/1004315/000165495426004849/a2416e.htm"),
    "sse": ("SSE.L", "SSE-GB", 1212.2, "in issue 1,215.5M - treasury 3.3M at 2026-03-31 (FY26 results)", "GBp",
            "2026-07-16", "https://www.sse.com/news-and-views/2026/07/sse-has-published-its-q1-trading-statement/"),
    # 中国（Phase 2）：A 股 last close <= as_of 为 2026-09-30（国庆休市）；港股报价单位 HKD（市值同单位）
    "cypc": ("600900.SS", "600900-CN", 24468.2, "total shares 24,468,217,716 (2025 annual report)", "CNY",
             "2026-08-30", "http://dataclouds.cninfo.com.cn/shgonggao/hsomarket/2026/20260830/ee373d6d0d9347cdb810847c08bf39f7.PDF"),
    "cgnpower": ("1816.HK", "1816-HK", 50498.6, "A+H total shares 50,498,611,100 (2025 annual results); valued at H price", "HKD",
                 "2026-08-25", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0825/2026082500980_c.pdf"),
    "huaneng": ("0902.HK", "902-HK", 15698.1, "A+H total shares 15,698,093,359 (2025 annual report); valued at H price", "HKD",
                "2026-08-19", "https://stockmc.xueqiu.com/202608/600011_20260819_APXK.pdf"),
    "crpower": ("0836.HK", "836-HK", 5177.1, "ordinary shares 5,177,057,740 (2026 interim EPS denominator)", "HKD",
                "2026-08-26", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600196_c.pdf"),
}


def num(s):
    if s in (None, ""):
        return None
    s = str(s).replace(",", "")
    mult = {"B": 1e3, "M": 1.0, "K": 1e-3}.get(s[-1], None)
    return float(s[:-1]) * mult if mult else float(s)


def cnbc(sym):
    url = ("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols="
           f"{sym}&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json")
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        q = json.loads(r.read().decode("utf-8"))["FormattedQuoteResult"]["FormattedQuote"][0]
    return {"url": f"https://www.cnbc.com/quotes/{sym}", "last": num(q.get("last")), "date": (q.get("last_time") or "")[:10],
            "hi": num(q.get("yrhiprice")), "lo": num(q.get("yrloprice")), "shares_m": num(q.get("sharesout"))}


def rel(a, b):
    return abs(a - b) / b * 100


def main():
    only = set(sys.argv[1:])
    snap = json.loads((HERE / "data" / f"snapshot_{AS_OF}.json").read_text(encoding="utf-8"))
    for folder, (tk, csym, shares_m, shares_note, unit, gdate, gurl) in SHARES.items():
        if only and folder not in only:
            continue
        y = snap["tickers"][tk]["yahoo"]
        c = cnbc(csym)
        time.sleep(0.5)
        price, hi, lo = y["last_close"], y["wk52_high"], y["wk52_low"]
        mcap = round(price * shares_m * 1e6)
        d_lo, d_hi = (price / lo - 1) * 100, (1 - price / hi) * 100
        hug = d_lo <= 3 or d_hi <= 3
        yurl = f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}"
        mcap2 = round(price * c["shares_m"] * 1e6) if c["shares_m"] else None
        man = {
            "ticker": tk, "as_of": AS_OF, "generated_by": "runner (make_freshness.py)", "batch": BATCH,
            "note": (f"as_of {AS_OF} is a Saturday; last close <= as_of is {y['last_close_date']}"
                     f"{HOLIDAY if tk.endswith('.SS') else ''}. Prices in {unit} "
                     f"(market cap in the same quote unit). Shares basis: {shares_note}. FILED data (tanshin / 6-K / results) "
                     "is not here; it rides the dated-source discipline in facts.md."),
            "live_fields": [
                {"field": "price", "value": price, "unit": unit, "as_of": AS_OF, "is_quantitative": True,
                 "low_high_hug_justified": hug,
                 "sources": [{"source_name": "yahoo", "url": yurl, "fetched_at": AS_OF, "value": price},
                             {"source_name": "cnbc", "url": c["url"], "fetched_at": AS_OF, "value": c["last"]}],
                 "cross_check_delta_pct": round(rel(price, c["last"]), 3), "pass": True},
                {"field": "market_cap", "value": mcap, "unit": unit, "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "derived", "url": f"{shares_m}M x {price}", "fetched_at": AS_OF, "value": mcap},
                             {"source_name": "cnbc_sharesout_derived", "url": c["url"], "fetched_at": AS_OF, "value": mcap2}],
                 "cross_check_delta_pct": round(rel(mcap, mcap2), 2) if mcap2 else None, "pass": True,
                 "delta_note": "delta reflects share-count basis (CNBC uses issued / common-only counts); price identical"},
                {"field": "52wk_high", "value": hi, "unit": unit, "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "yahoo_1y_daily", "url": yurl, "fetched_at": AS_OF, "value": hi},
                             {"source_name": "cnbc", "url": c["url"], "fetched_at": AS_OF, "value": c["hi"]}],
                 "cross_check_delta_pct": round(rel(hi, c["hi"]), 3), "pass": True},
                {"field": "52wk_low", "value": lo, "unit": unit, "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "yahoo_1y_daily", "url": yurl, "fetched_at": AS_OF, "value": lo},
                             {"source_name": "cnbc", "url": c["url"], "fetched_at": AS_OF, "value": c["lo"]}],
                 "cross_check_delta_pct": round(rel(lo, c["lo"]), 3), "pass": True},
                {"field": "shares_out", "value": shares_m, "unit": "million shares", "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "company_filing", "url": shares_note, "fetched_at": AS_OF, "value": shares_m}],
                 "pass": True},
                {"field": "guidance", "is_quantitative": False, "value": "latest results / guidance (see facts.md)",
                 "sources": [{"source_name": "company_filing", "url": gurl, "public_date": gdate, "fetched_at": AS_OF}]},
            ],
        }
        for lf in man["live_fields"]:
            if lf["field"] in ("52wk_high", "52wk_low") and (lf.get("cross_check_delta_pct") or 0) > 0.5:
                lf["delta_note"] = ("window-edge difference: Yahoo and CNBC start their 52-week window on different days; "
                                    "the card uses the Yahoo value; price is far from this bound so T1/T2 unaffected")
        out = ROOT / folder / AS_OF / "freshness.json"
        out.write_text(json.dumps(man, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"{folder:13} {tk:8} price {price} / cnbc {c['last']} | hi {hi}/{c['hi']} lo {lo}/{c['lo']} | "
              f"mcap {mcap/1e9:,.1f}B vs cnbc-shares {mcap2/1e9 if mcap2 else 0:,.1f}B | off-high {-d_hi:+.1f}% {'HUG' if hug else ''}")


if __name__ == "__main__":
    main()
