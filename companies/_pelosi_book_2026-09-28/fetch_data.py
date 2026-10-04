#!/usr/bin/env python3
"""fetch_data.py — batch _pelosi_book_2026-09-28 的一手数据抓取（可原地重跑）

每个 ticker 取：
  1. 价格：Yahoo chart API 与 Nasdaq historical API 两个独立源，取 last close <= AS_OF
  2. 52 周高低（Yahoo meta，盘中口径；另算收盘口径）
  3. SEC XBRL companyfacts：TTM 营收 / 营业利润 / 净利 / OCF / capex / SBC / D&A，
     资产负债表现金与债务，封面在外股数，近 5 个财年营收
TTM 算法：若最新期末有 12 个月事实则直接用；否则 = 上一财年 + 本年 YTD − 上年同期 YTD。
每个数字都记录所用 XBRL concept 与期末日，便于人工复核。

用法: python companies/_pelosi_book_2026-09-28/fetch_data.py
输出: data/snapshot_<AS_OF>.json + data/snapshot_<AS_OF>.md
"""
from __future__ import annotations

import datetime as dt
import json
import time
import urllib.request
from pathlib import Path

AS_OF = "2026-09-28"
TICKERS = {
    "AVGO": 1730168, "BE": 1664703, "INTC": 50863, "CRWD": 1535527,
    "VST": 1692819, "AB": 825313, "UBER": 1543151, "PANW": 1327567,
}
SEC_UA = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}
WEB_UA = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
OUT = Path(__file__).resolve().parent / "data"

DURATION = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"],
    "gross_profit": ["GrossProfit"],
    "operating_income": ["OperatingIncomeLoss"],
    "net_income": ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
              "PaymentsToAcquireOtherPropertyPlantAndEquipment"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "d_and_a": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
                "DepreciationAmortizationAndAccretionNet"],
    "interest_expense": ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
    "dividends_paid": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "rd": ["ResearchAndDevelopmentExpense",
           "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost"],
}
INSTANT = {
    "cash": ["CashAndCashEquivalentsAtCarryingValue",
             "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "st_investments": ["ShortTermInvestments", "MarketableSecuritiesCurrent",
                       "AvailableForSaleSecuritiesDebtSecuritiesCurrent"],
    "lt_debt_noncurrent": ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"],
    "debt_current": ["LongTermDebtCurrent", "DebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent"],
    "short_term_borrowings": ["ShortTermBorrowings", "CommercialPaper"],
    "total_debt_tag": ["LongTermDebt", "DebtLongtermAndShorttermCombinedAmount"],
    "equity": ["StockholdersEquity",
               "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
               "PartnersCapital"],
    "total_assets": ["Assets"],
    "deferred_revenue_current": ["ContractWithCustomerLiabilityCurrent", "DeferredRevenueCurrent"],
    "deferred_revenue_noncurrent": ["ContractWithCustomerLiabilityNoncurrent", "DeferredRevenueNoncurrent"],
    "goodwill": ["Goodwill"],
}


def get_json(url, headers, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def d(s):
    return dt.date.fromisoformat(s)


def facts_for(cf, concept, unit="USD"):
    for ns in ("us-gaap", "dei"):
        node = cf.get("facts", {}).get(ns, {}).get(concept)
        if node and unit in node.get("units", {}):
            rows = [r for r in node["units"][unit] if r.get("form") in ("10-Q", "10-K", "10-K/A", "10-Q/A")]
            # 同一 (start,end) 取最近提交的一条
            best = {}
            for r in rows:
                k = (r.get("start"), r["end"])
                if k not in best or r["filed"] > best[k]["filed"]:
                    best[k] = r
            return list(best.values())
    return []


def ttm(cf, concepts):
    for c in concepts:
        rows = [r for r in facts_for(cf, c) if r.get("start")]
        if not rows:
            continue
        latest_end = max(r["end"] for r in rows)
        # 如果某个 concept 已停用（最新期末早于一年前）则换下一个
        if d(latest_end) < d(AS_OF) - dt.timedelta(days=200):
            continue
        at_end = [r for r in rows if r["end"] == latest_end]
        dur = lambda r: (d(r["end"]) - d(r["start"])).days  # noqa: E731
        annual = [r for r in at_end if 330 <= dur(r) <= 380]
        q3m = [r for r in at_end if 80 <= dur(r) <= 100]
        latest_q = q3m[0]["val"] if q3m else None
        prior_q = None
        if q3m:
            tgt = d(latest_end) - dt.timedelta(days=364)
            cands = [r for r in rows if 80 <= dur(r) <= 100 and abs((d(r["end"]) - tgt).days) <= 10]
            if cands:
                prior_q = cands[0]["val"]
        if annual:
            return {"concept": c, "period_end": latest_end, "method": "annual", "ttm": annual[0]["val"],
                    "latest_q": latest_q, "prior_year_q": prior_q}
        ytd = max(at_end, key=dur)
        s = d(ytd["start"])
        fy = [r for r in rows if 330 <= dur(r) <= 380 and 0 <= (s - d(r["end"])).days <= 10]
        tgt = d(latest_end) - dt.timedelta(days=364)
        pytd = [r for r in rows if abs((d(r["end"]) - tgt).days) <= 10 and abs(dur(r) - dur(ytd)) <= 10]
        if fy and pytd:
            return {"concept": c, "period_end": latest_end, "method": "FY+YTD-priorYTD",
                    "ttm": fy[0]["val"] + ytd["val"] - pytd[0]["val"],
                    "fy_val": fy[0]["val"], "fy_end": fy[0]["end"], "ytd": ytd["val"],
                    "ytd_days": dur(ytd), "prior_ytd": pytd[0]["val"],
                    "latest_q": latest_q, "prior_year_q": prior_q}
    return None


def instant(cf, concepts):
    for c in concepts:
        rows = [r for r in facts_for(cf, c) if not r.get("start")]
        if not rows:
            continue
        r = max(rows, key=lambda x: (x["end"], x["filed"]))
        if d(r["end"]) < d(AS_OF) - dt.timedelta(days=200):
            continue
        return {"concept": c, "period_end": r["end"], "val": r["val"], "filed": r["filed"], "form": r["form"]}
    return None


def annual_series(cf, concepts, n=6):
    for c in concepts:
        rows = [r for r in facts_for(cf, c) if r.get("start")]
        out = {}
        for r in rows:
            days = (d(r["end"]) - d(r["start"])).days
            if 330 <= days <= 380 and r["form"].startswith("10-K"):
                out[r["end"]] = r["val"]
        if out and max(out) >= str(d(AS_OF) - dt.timedelta(days=600)):
            ks = sorted(out)[-n:]
            return {"concept": c, "series": {k: out[k] for k in ks}}
    return None


def shares(cf):
    rows = facts_for(cf, "EntityCommonStockSharesOutstanding", unit="shares")
    out = {}
    if rows:
        r = max(rows, key=lambda x: (x["end"], x["filed"]))
        out["cover_shares"] = {"val": r["val"], "as_of": r["end"], "filed": r["filed"], "form": r["form"]}
        # 多类股（如 BE 有 A/B 类）：同一日期多条时求和
        same = [x for x in rows if x["end"] == r["end"] and x["filed"] == r["filed"]]
        if len(same) > 1:
            out["cover_shares"]["val_sum_all_classes"] = sum(x["val"] for x in same)
    for c in ("WeightedAverageNumberOfDilutedSharesOutstanding",):
        rows = [x for x in facts_for(cf, c, unit="shares") if x.get("start")]
        q = [x for x in rows if 80 <= (d(x["end"]) - d(x["start"])).days <= 100]
        if q:
            r = max(q, key=lambda x: (x["end"], x["filed"]))
            out["diluted_wtd_latest_q"] = {"val": r["val"], "period_end": r["end"]}
    return out


def yahoo(tk):
    j = get_json(f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}?range=1y&interval=1d", WEB_UA)
    res = j["chart"]["result"][0]
    m = res["meta"]
    ts = res["timestamp"]
    q = res["indicators"]["quote"][0]
    rows = [(dt.datetime.utcfromtimestamp(t).date(), c, h, lo) for t, c, h, lo in
            zip(ts, q["close"], q["high"], q["low"]) if c is not None]
    rows = [r for r in rows if r[0] <= d(AS_OF)]
    last = rows[-1]
    return {"last_close": round(last[1], 2), "last_close_date": str(last[0]),
            "wk52_high_meta": m.get("fiftyTwoWeekHigh"), "wk52_low_meta": m.get("fiftyTwoWeekLow"),
            "wk52_high_close": round(max(r[1] for r in rows), 2),
            "wk52_low_close": round(min(r[1] for r in rows), 2),
            "wk52_high_intraday": round(max(r[2] for r in rows if r[2]), 2),
            "wk52_low_intraday": round(min(r[3] for r in rows if r[3]), 2),
            "close_1y_ago": round(rows[0][1], 2), "close_1y_ago_date": str(rows[0][0]),
            "long_name": m.get("longName")}


def nasdaq(tk):
    frm = (d(AS_OF) - dt.timedelta(days=10)).isoformat()
    j = get_json(f"https://api.nasdaq.com/api/quote/{tk}/historical?assetclass=stocks"
                 f"&fromdate={frm}&todate={AS_OF}&limit=20", WEB_UA)
    rows = j["data"]["tradesTable"]["rows"]
    parsed = [(dt.datetime.strptime(r["date"], "%m/%d/%Y").date(), float(r["close"].replace("$", "").replace(",", "")))
              for r in rows]
    parsed = [p for p in parsed if p[0] <= d(AS_OF)]
    last = max(parsed)
    return {"last_close": last[1], "last_close_date": str(last[0])}


def main():
    OUT.mkdir(exist_ok=True)
    snap = {"as_of": AS_OF, "fetched_at": dt.datetime.now().isoformat(timespec="seconds"), "tickers": {}}
    for tk, cik in TICKERS.items():
        print("fetching", tk)
        rec = {"cik": cik}
        try:
            rec["yahoo"] = yahoo(tk)
        except Exception as e:  # noqa: BLE001
            rec["yahoo_error"] = str(e)
        try:
            rec["nasdaq"] = nasdaq(tk)
        except Exception as e:  # noqa: BLE001
            rec["nasdaq_error"] = str(e)
        cf = get_json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", SEC_UA)
        rec["entity"] = cf.get("entityName")
        rec["ttm"] = {k: ttm(cf, v) for k, v in DURATION.items()}
        rec["balance"] = {k: instant(cf, v) for k, v in INSTANT.items()}
        rec["shares"] = shares(cf)
        rec["annual_revenue"] = annual_series(cf, DURATION["revenue"])
        rec["annual_net_income"] = annual_series(cf, DURATION["net_income"])
        rec["annual_ocf"] = annual_series(cf, DURATION["ocf"])
        rec["annual_capex"] = annual_series(cf, DURATION["capex"])
        snap["tickers"][tk] = rec
        time.sleep(0.4)
    (OUT / f"snapshot_{AS_OF}.json").write_text(json.dumps(snap, indent=1), encoding="utf-8")

    # 人读摘要
    B = 1e9
    lines = [f"# 数据快照 {AS_OF}（fetch_data.py 生成，勿手改）", "",
             "| Ticker | Yahoo 收盘 | Nasdaq 收盘 | 日期 | 52w 高/低(盘中) | 封面股数(M) | 市值($B) | TTM 营收 | 营业利润 | 净利 | OCF | capex | FCF | SBC | 期末 |",
             "|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for tk, r in snap["tickers"].items():
        y, n, t = r.get("yahoo", {}), r.get("nasdaq", {}), r["ttm"]
        sh = r["shares"].get("cover_shares", {})
        shv = sh.get("val_sum_all_classes", sh.get("val"))
        mc = (y.get("last_close") or 0) * (shv or 0) / B
        g = lambda k: (t[k]["ttm"] / B) if t.get(k) else float("nan")  # noqa: E731
        fcf = g("ocf") - g("capex")
        pe = t["revenue"]["period_end"] if t.get("revenue") else "?"
        lines.append(f"| {tk} | {y.get('last_close')} | {n.get('last_close')} | {y.get('last_close_date')} | "
                     f"{y.get('wk52_high_intraday')}/{y.get('wk52_low_intraday')} | {(shv or 0)/1e6:,.1f} | {mc:,.1f} | "
                     f"{g('revenue'):.2f} | {g('operating_income'):.2f} | {g('net_income'):.2f} | {g('ocf'):.2f} | "
                     f"{g('capex'):.2f} | {fcf:.2f} | {g('sbc'):.2f} | {pe} |")
    (OUT / f"snapshot_{AS_OF}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
