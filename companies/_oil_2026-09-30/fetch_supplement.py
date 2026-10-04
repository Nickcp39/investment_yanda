#!/usr/bin/env python3
"""fetch_supplement.py — 石油批次的 XBRL 补丁（fetch_data.py 之后运行）

处理三件 fetch_data.py 的通用逻辑做不到的事：
  1. XOM 于 2026 年改由新注册人 "ExxonMobil Holdings Corp"（CIK 2115436）申报；
     旧 CIK 34088 的数据停在 2026-03-31。本脚本合并两个 CIK 的事实后再算 TTM。
  2. 油企不用 us-gaap:ShareBasedCompensation（现金流量表）；SBC 取年报的
     AllocatedShareBasedCompensationExpense（FY2025，年度口径，标注为近似）。
  3. COP 的资本开支用自定义标签；在 cop: 命名空间里按名称搜索。
另取：股息、回购（TTM）、封面股数。输出 data/supplement_<AS_OF>.json。
"""
from __future__ import annotations

import datetime as dt
import json
import urllib.request
from pathlib import Path

AS_OF = "2026-09-30"
UA = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}
OUT = Path(__file__).resolve().parent / "data"
CIKS = {"XOM": [34088, 2115436], "CVX": [93410], "OXY": [797468], "COP": [1163165], "KMI": [1506307]}
DUR = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerIncludingAssessedTax",
                "RevenueFromContractWithCustomerExcludingAssessedTax"],
    "net_income": ["NetIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
              "PaymentsToAcquireOilAndGasPropertyAndEquipment"],
    "dividends": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
    "dd_a": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization"],
}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def d(s):
    return dt.date.fromisoformat(s)


def rows_for(cfs, concept, ns=("us-gaap",), unit="USD"):
    best = {}
    for cf in cfs:
        for n in ns:
            node = cf["facts"].get(n, {}).get(concept)
            if not node or unit not in node["units"]:
                continue
            for r in node["units"][unit]:
                if not r.get("form", "").startswith("10"):
                    continue
                k = (r.get("start"), r["end"])
                if k not in best or r["filed"] > best[k]["filed"]:
                    best[k] = r
    return list(best.values())


def ttm(rows):
    rows = [r for r in rows if r.get("start")]
    if not rows:
        return None
    dur = lambda r: (d(r["end"]) - d(r["start"])).days  # noqa: E731
    le = max(r["end"] for r in rows)
    at = [r for r in rows if r["end"] == le]
    ann = [r for r in at if 330 <= dur(r) <= 380]
    if ann:
        return {"period_end": le, "ttm": ann[0]["val"], "method": "annual"}
    ytd = max(at, key=dur)
    s = d(ytd["start"])
    fy = [r for r in rows if 330 <= dur(r) <= 380 and 0 <= (s - d(r["end"])).days <= 10]
    tgt = d(le) - dt.timedelta(days=364)
    py = [r for r in rows if abs((d(r["end"]) - tgt).days) <= 10 and abs(dur(r) - dur(ytd)) <= 10]
    if fy and py:
        return {"period_end": le, "ttm": fy[0]["val"] + ytd["val"] - py[0]["val"], "method": "FY+YTD-priorYTD",
                "fy_end": fy[0]["end"]}
    return None


def main():
    out = {"as_of": AS_OF, "tickers": {}}
    for tk, ciks in CIKS.items():
        cfs = [get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json") for c in ciks]
        ns = tuple({"us-gaap"} | {n for cf in cfs for n in cf["facts"] if n not in ("dei", "srt", "ifrs-full")})
        rec = {"ciks": ciks, "entities": [cf.get("entityName") for cf in cfs]}
        for key, concepts in DUR.items():
            for c in concepts:
                t = ttm(rows_for(cfs, c))
                if t and d(t["period_end"]) >= d(AS_OF) - dt.timedelta(days=200):
                    rec[key] = {**t, "concept": c}
                    break
        if "capex" not in rec:  # 自定义命名空间里找资本开支
            for cf in cfs:
                for n, node in cf["facts"].items():
                    if n in ("us-gaap", "dei", "srt"):
                        continue
                    for c in node:
                        if "Capital" in c and ("Expenditure" in c or "Investment" in c):
                            t = ttm(rows_for(cfs, c, ns=(n,)))
                            if t and d(t["period_end"]) >= d(AS_OF) - dt.timedelta(days=200):
                                rec["capex"] = {**t, "concept": f"{n}:{c}"}
                                break
                    if "capex" in rec:
                        break
        sbc = [r for r in rows_for(cfs, "AllocatedShareBasedCompensationExpense")
               if r.get("start") and 330 <= (d(r["end"]) - d(r["start"])).days <= 380]
        if sbc:
            r = max(sbc, key=lambda x: x["end"])
            rec["sbc_fy"] = {"fy_end": r["end"], "val": r["val"], "concept": "AllocatedShareBasedCompensationExpense (FY, approx)"}
        sh = [r for cf in cfs for r in cf["facts"].get("dei", {}).get("EntityCommonStockSharesOutstanding", {})
              .get("units", {}).get("shares", [])]
        if sh:
            r = max(sh, key=lambda x: (x["end"], x["filed"]))
            rec["cover_shares"] = {"val": r["val"], "as_of": r["end"], "filed": r["filed"]}
        out["tickers"][tk] = rec
    (OUT / f"supplement_{AS_OF}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    B = 1e9
    for tk, r in out["tickers"].items():
        g = lambda k: round(r[k]["ttm"] / B, 2) if k in r else None  # noqa: E731
        print(tk, "end", r.get("ocf", {}).get("period_end"), "rev", g("revenue"), "NI", g("net_income"), "OCF", g("ocf"),
              "capex", g("capex"), r.get("capex", {}).get("concept"), "div", g("dividends"), "buyback", g("buybacks"),
              "DD&A", g("dd_a"), "SBC_FY", round(r["sbc_fy"]["val"] / B, 2) if "sbc_fy" in r else None,
              "shares", round(r["cover_shares"]["val"] / 1e6, 1) if "cover_shares" in r else None,
              r.get("cover_shares", {}).get("as_of"))


if __name__ == "__main__":
    main()
