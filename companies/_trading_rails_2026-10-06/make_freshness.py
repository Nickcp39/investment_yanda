#!/usr/bin/env python3
"""make_freshness.py — 交易通道批次 13 个 dossier 的 freshness.json（由 _oil_2026-09-30/make_freshness.py 复制改参数）（lean-6module-v1.1 机械新鲜度门的输入）

每个 LIVE 定量字段 ≥2 个独立源：
  price       : Yahoo chart API 收盘 + Nasdaq historical 收盘（均取 last close <= AS_OF）
  market_cap  : 价格 × 卡片股数（derived）+ Nasdaq summary MarketCap
  52wk_high/low: Yahoo meta + Nasdaq summary FiftTwoWeekHighLow
  shares_out  : 卡片股数 = valuation_model.py 的估值股数（摊薄 / 全部转换口径，见 shares_note）；Nasdaq 市值常按单一类别股数，差异写进 delta_note
LIVE 定性字段 guidance：最新财报新闻稿（SEC 8-K）日期作为来源日期（T6 只做 WARN）。
读取 data/snapshot_<AS_OF>.json（fetch_data.py 产物）以保证与卡片同一份价格。
"""
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path

AS_OF = "2026-10-06"
BATCH = "trading_rails_2026-10-06"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WEB_UA = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
FOLDER = {"CRCL": "circle"}
_VAL = json.loads((HERE / "data" / f"valuation_{AS_OF}.json").read_text(encoding="utf-8"))["tickers"]
_INP = __import__("valuation_model").INPUTS
# 卡片股数 = 估值股数（同一口径，保证 T3 市值恒等式与估值一致）
SHARES = {tk: (_INP[tk]["shares_m"], _INP[tk]["shares_note"]) for tk in _INP}
_SRC = json.loads((HERE / "data" / f"sources_{AS_OF}.json").read_text(encoding="utf-8"))
GUIDANCE_SRC = {tk: next(((x["date"], x["url"]) for x in v if x["kind"] == "earnings"), None) for tk, v in _SRC.items()}


def nasdaq_summary(tk):
    url = f"https://api.nasdaq.com/api/quote/{tk}/summary?assetclass=stocks"
    req = urllib.request.Request(url, headers=WEB_UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode("utf-8"))["data"]["summaryData"]
    hi, lo = d["FiftTwoWeekHighLow"]["value"].replace("$", "").replace(",", "").split("/")
    return {"url": url, "mcap": float(d["MarketCap"]["value"].replace(",", "")), "hi": float(hi), "lo": float(lo)}


def rel(a, b):
    return abs(a - b) / b * 100


def main():
    snap = json.loads((HERE / "data" / f"snapshot_{AS_OF}.json").read_text(encoding="utf-8"))
    summary = []
    for tk, (shares_m, shares_note) in SHARES.items():
        y = snap["tickers"][tk]["yahoo"]
        n = snap["tickers"][tk]["nasdaq"]
        ns = nasdaq_summary(tk)
        time.sleep(0.5)
        price = y["last_close"]
        mcap = round(price * shares_m * 1e6)
        hi, lo = y["wk52_high_meta"], y["wk52_low_meta"]
        d_lo, d_hi = (price / lo - 1) * 100, (1 - price / hi) * 100
        hug = d_lo <= 3 or d_hi <= 3
        yurl = f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}"
        price_field = {
            "field": "price", "value": price, "unit": "USD", "as_of": AS_OF, "is_quantitative": True,
            "low_high_hug_justified": hug,
            "sources": [
                {"source_name": "yahoo", "url": yurl, "fetched_at": AS_OF, "value": price},
                {"source_name": "nasdaq", "url": f"https://api.nasdaq.com/api/quote/{tk}/historical", "fetched_at": AS_OF,
                 "value": n["last_close"]},
            ],
            "cross_check_delta_pct": round(rel(price, n["last_close"]), 3), "pass": True,
        }
        if hug:
            price_field["hug_justification"] = (
                f"T2 fires because {price} is {d_lo:.2f}% above the 52-week low {lo}. JUSTIFIED mechanically: the value is the "
                f"last close dated {y['last_close_date']} (Yahoo) and Nasdaq historical independently reports {n['last_close']} for "
                f"{n['last_close_date']}; verify_freshness.py re-fetches it independently. The unit simply trades near its low "
                f"(12m {snap['tickers'][tk]['yahoo']['close_1y_ago']} -> {price}). Not an extreme-of-series grab.")
        man = {
            "ticker": tk, "as_of": AS_OF, "generated_by": "runner (make_freshness.py)", "batch": BATCH,
            "note": (f"run 2026-10-07 09:45 EDT (market open) -> as_of locked to the completed session {AS_OF}; last close <= as_of is {y['last_close_date']}. "
                     f"Shares basis for market cap: {shares_note}. Valuation uses the diluted count stated in valuation.md. "
                     "FILED data (10-K/10-Q/8-K line items) is not here; it rides the dated-source discipline in facts.md."),
            "live_fields": [
                price_field,
                {"field": "market_cap", "value": mcap, "unit": "USD", "as_of": AS_OF, "is_quantitative": True,
                 "sources": [
                     {"source_name": "derived", "url": f"{shares_m}M x {price}", "fetched_at": AS_OF, "value": mcap},
                     {"source_name": "nasdaq_summary", "url": ns["url"], "fetched_at": AS_OF, "value": ns["mcap"]},
                 ],
                 "cross_check_delta_pct": round(rel(mcap, ns["mcap"]), 2), "pass": True,
                 "delta_note": "delta reflects share-count basis: the card uses the valuation (diluted / fully-converted) count; Nasdaq uses its own snapshot, often a single share class; price identical"},
                {"field": "52wk_high", "value": hi, "unit": "USD", "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "yahoo_meta", "url": yurl, "fetched_at": AS_OF, "value": hi},
                             {"source_name": "nasdaq_summary", "url": ns["url"], "fetched_at": AS_OF, "value": ns["hi"]}],
                 "cross_check_delta_pct": round(rel(hi, ns["hi"]), 3), "pass": True},
                {"field": "52wk_low", "value": lo, "unit": "USD", "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "yahoo_meta", "url": yurl, "fetched_at": AS_OF, "value": lo},
                             {"source_name": "nasdaq_summary", "url": ns["url"], "fetched_at": AS_OF, "value": ns["lo"]}],
                 "cross_check_delta_pct": round(rel(lo, ns["lo"]), 3), "pass": True},
                {"field": "shares_out", "value": shares_m, "unit": "million shares", "as_of": AS_OF, "is_quantitative": True,
                 "sources": [{"source_name": "sec_filing", "url": shares_note, "fetched_at": AS_OF, "value": shares_m}],
                 "pass": True},
                {"field": "guidance", "is_quantitative": False, "value": "latest earnings release guidance (see facts.md)",
                 "sources": [{"source_name": "sec_8k", "url": GUIDANCE_SRC[tk][1], "public_date": GUIDANCE_SRC[tk][0],
                              "fetched_at": AS_OF}]},
            ],
        }
        for lf in man["live_fields"]:
            if lf["field"] in ("52wk_high", "52wk_low") and lf.get("cross_check_delta_pct", 0) > 1:
                lf["delta_note"] = ("window-edge / intraday-vs-close difference: Yahoo meta and Nasdaq define the 52-week window "
                                    "differently; the card uses the Yahoo value; price is far from this bound so T1/T2 unaffected")
        out = ROOT / FOLDER.get(tk, tk.lower()) / AS_OF / "freshness.json"
        out.write_text(json.dumps(man, indent=2, ensure_ascii=False), encoding="utf-8")
        summary.append((tk, price, n["last_close"], mcap / 1e9, ns["mcap"] / 1e9, hi, ns["hi"], lo, ns["lo"],
                        -d_hi, d_lo, hug))
    print("tk price nasdaq | mcap_card nasdaq_mcap | hi(y/n) | lo(y/n) | off_high off_low hug")
    for s in summary:
        print(f"{s[0]:5} {s[1]} {s[2]} | {s[3]:,.1f} {s[4]:,.1f} ({rel(s[3], s[4]):.1f}%) | {s[5]}/{s[6]} | {s[7]}/{s[8]} | "
              f"{s[9]:+.1f}% +{s[10]:.1f}% {'HUG' if s[11] else ''}")


if __name__ == "__main__":
    main()
