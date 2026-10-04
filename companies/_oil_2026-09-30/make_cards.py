#!/usr/bin/env python3
"""make_cards.py — 石油批次 5 张 decision_card.json：数字只读 data/valuation_<AS_OF>.json 与 freshness.json，
判断字段在此集中登记（与各 decision_card.md 对应）。结构沿用 _pelosi_book_2026-09-28/make_cards.py。"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-09-30"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VAL = json.loads((HERE / "data" / f"valuation_{AS_OF}.json").read_text(encoding="utf-8"))

COMMON = {
    "as_of": AS_OF, "pipeline_version": "lean-6module-v1.1", "weights_version": "none", "run_date": AS_OF,
    "batch": "oil_2026-09-30", "run_type": "first_dossier", "refresh_of": None, "status": "DECISION_DRAFT",
    "clean": False, "clean_blocked_reason": "Checker != Runner (PROTOCOL §3) not met: single agent, self-checked only",
    "price_sources": ["yahoo_chart_api", "nasdaq_historical_api"], "price_date": "2026-09-29",
    "valuation_method": "batch valuation_model.py (same formula as 2026-09-28); OE0 normalized to mid-cycle deck "
                        "(base WTI $65 / Brent $70, ~2016-2025 average); g gives 50% credit to management FCF plans in base",
    "oil_price_deck": {"bear": "WTI 55 / Brent 60", "base": "WTI 65 / Brent 70", "bull": "WTI 80 / Brent 85"},
    "new_money_verdict": "WATCH", "runner_proposed_verdict": "WATCH", "runner_proposed_size_pct": 0,
    "existing_position_verdict": "HOLD", "suggested_initial_size_pct": 0,
}

CARDS = {
    "XOM": dict(context_label="cyclical_inflection", business_verdict="good",
                module_signals={"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": -1, "M6": -2}, suggested_max_size_pct=12,
                binding_constraint="PRICE: market price implies long-run Brent ~$94 for an 8% 10y IRR",
                completeness_pct=58, share_count_yoy_pct=-3.8, sensitivity="$0.70B after-tax upstream earnings per $1 Brent (10-K, primary)",
                buffett="BRK bought ~40M sh 2013Q3 (cost $3.74B at YE2013), exited 2014Q4 as oil collapsed (13F)",
                kill_criteria=["K-X1 Brent 12m avg < $65 while $20B buyback kept (debt-funded buybacks) -> watch",
                               "K-X2 Guyana/Permian growth below plan -> green", "K-X3 debt/capital > 25% -> green (13.7%)"],
                next_monitor_event="Q3 2026 earnings (~late Oct 2026)",
                sources=[("XOM-10K-2025", "2026-02-18", "https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/xom-20251231.htm"),
                         ("XOM-10Q-Q2", "2026-08-03", "https://www.sec.gov/Archives/edgar/data/2115436/000003408826000093/xom-20260630.htm"),
                         ("XOM-8K-Q2", "2026-07-31", "https://www.sec.gov/Archives/edgar/data/2115436/000211543626000006/livef8k2q26991.htm")]),
    "CVX": dict(context_label="cyclical_inflection", business_verdict="good",
                module_signals={"M1": 1, "M2": 1, "M3": 1, "M4": 0, "M5": -1, "M6": -2}, suggested_max_size_pct=12,
                binding_constraint="PRICE: market price implies long-run Brent ~$83.5; BRK sold 35% in 2026Q1 near $207",
                completeness_pct=57, share_count_yoy_pct=14.5, sensitivity="~$0.60B after-tax earnings/cash flow per $1 Brent (company IR, secondary retrieval)",
                buffett="BRK: 2020Q4 48.5M sh (~$84) -> 2022Q1 159.2M (~$163) -> peak 165.4M -> 2026Q1 84.4M after selling ~35% (~$8B) at ~$207",
                kill_criteria=["K-C1 normalized adj FCF < $17B at $70 Brent after downstream normalizes -> watch",
                               "K-C2 TCO/Guyana growth below plan -> green", "K-C3 another large stock-funded deal -> watch"],
                next_monitor_event="Q3 2026 earnings: downstream normalization",
                sources=[("CVX-10K-2025", "2026-02-24", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000078/cvx-20251231.htm"),
                         ("CVX-10Q-Q2", "2026-08-06", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000167/cvx-20260630.htm"),
                         ("CVX-8K-Q2", "2026-07-31", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000162/a06302026ex9918-k.htm")]),
    "OXY": dict(context_label="cyclical_inflection", business_verdict="uncertain",
                module_signals={"M1": 1, "M2": 1, "M3": 0, "M4": -1, "M5": -1, "M6": -2}, suggested_max_size_pct=5,
                binding_constraint="PRICE + CAPITAL STRUCTURE: implies long-run WTI ~$75.5; common ranks behind $11.8B debt + $8.5B BRK 8% preferred",
                completeness_pct=60, share_count_yoy_pct=0.18, sensitivity="$0.24B pre-tax cash per $1 WTI + $0.025B per $1 Brent (10-K, primary); ~$0.212B after tax",
                buffett="BRK holds 26.7% of common (264.9M sh, approx cost ~$58 proxy), $8.5B 8% preferred, warrants 83.9M @ $59.59; bought OxyChem 2026-01-02 for ~$9.4B",
                kill_criteria=["K-O1 principal debt back above $15B -> green ($11.8B)", "K-O2 WTI 12m avg < $60 -> green",
                               "K-O3 BRK sells common -> green (unchanged since 2025Q1)"],
                next_monitor_event="Q3 2026 earnings: debt <= $10B, new CEO capital allocation",
                sources=[("OXY-10K-2025", "2026-02-18", "https://www.sec.gov/Archives/edgar/data/797468/000162828026009059/oxy-20251231.htm"),
                         ("OXY-10Q-Q2", "2026-08-05", "https://www.sec.gov/Archives/edgar/data/797468/000162828026053388/oxy-20260630.htm"),
                         ("OXY-8K-Q2", "2026-08-05", "https://www.sec.gov/Archives/edgar/data/797468/000162828026053377/oxyex9916-30x26earningsrel.htm"),
                         ("BRK-10Q-Q2", "2026-08", "https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm")]),
    "COP": dict(context_label="cyclical_inflection", business_verdict="good",
                module_signals={"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": -1, "M6": -1}, suggested_max_size_pct=8,
                binding_constraint="PRICE: implies long-run WTI ~$71.9 (closest to history among producers); 22% above the 8% line",
                completeness_pct=57, share_count_yoy_pct=-3.55, sensitivity="~$0.29B after-tax per $1 WTI (derived from 10-Q price-variance disclosure)",
                buffett="Buffett's self-described 2008 'major mistake of commission': 84.9M sh cost $7.0B, YE2008 value $4.4B; sold down 2009-2014",
                kill_criteria=["K-P1 Willow first oil slips beyond 2030 -> green", "K-P2 buybacks < 30% of CFO -> green",
                               "K-P3 losses on new Iraq/Syria projects -> new"],
                next_monitor_event="Q3 2026 earnings; Willow progress",
                sources=[("COP-10K-2025", "2026-02-17", "https://www.sec.gov/Archives/edgar/data/1163165/000116316526000009/cop-20251231.htm"),
                         ("COP-10Q-Q2", "2026-08-06", "https://www.sec.gov/Archives/edgar/data/1163165/000116316526000032/cop-20260630.htm"),
                         ("COP-8K-Q2", "2026-08-06", "https://www.sec.gov/Archives/edgar/data/1163165/000116316526000030/cop-20260806x8kexx991.htm")]),
    "KMI": dict(context_label="yield_or_balance_sheet_trap", business_verdict="good",
                module_signals={"M1": 1, "M2": 1, "M3": 2, "M4": 0, "M5": -1, "M6": 0}, suggested_max_size_pct=8,
                binding_constraint="PRICE (about 4% above the 8% line) + leverage 3.6x net debt/EBITDA (2015 dividend-cut precedent)",
                completeness_pct=58, share_count_yoy_pct=0.14, sensitivity="fee-based; CO2 segment hedged ~$64 crude 2026-28",
                buffett="BRK owns gas pipelines directly via BHE rather than listed pipeline equities (unsourced background)",
                kill_criteria=["K-K1 net debt/EBITDA > 4.5x -> green (3.6x)", "K-K2 expansion needs external equity -> green",
                               "K-K3 major shipper credit event -> green", "K-K4 data-center gas demand projects cancelled -> watch"],
                next_monitor_event="Q3 2026 earnings (~mid/late Oct 2026)",
                sources=[("KMI-10K-2025", "2026-02-13", "https://www.sec.gov/Archives/edgar/data/1506307/000150630726000011/kmi-20251231.htm"),
                         ("KMI-10Q-Q2", "2026-07-24", "https://www.sec.gov/Archives/edgar/data/1506307/000150630726000085/kmi-20260630.htm"),
                         ("KMI-8K-Q2", "2026-07-22", "https://www.sec.gov/Archives/edgar/data/1506307/000150630726000063/kmi2026q28-kex991.htm")]),
}


def main():
    for tk, c in CARDS.items():
        v = VAL["tickers"][tk]
        man = json.loads((ROOT / tk.lower() / AS_OF / "freshness.json").read_text(encoding="utf-8"))
        lf = {f["field"]: f for f in man["live_fields"]}
        hp = v["hurdle_prices"]
        card = {"ticker": tk, **COMMON, "as_of_price": v["price"], "as_of_market_cap": lf["market_cap"]["value"],
                "shares_out_m": lf["shares_out"]["value"], "wk52_high": lf["52wk_high"]["value"], "wk52_low": lf["52wk_low"]["value"],
                **{k: c[k] for k in ("context_label", "business_verdict", "module_signals", "suggested_max_size_pct",
                                     "binding_constraint", "completeness_pct", "share_count_yoy_pct", "sensitivity",
                                     "kill_criteria", "next_monitor_event")},
                "buy_below_price": hp["8pct"], "hurdle_prices": hp,
                "zones": {"starter": f"<= {hp['8pct']} (base >= 8%)", "add": f"<= {hp['10pct']} (base >= 10%)",
                          "no_chase": f"> {hp['8pct']}", "avoid": f"> {hp['8pct_on_bull']}"},
                "implied_oil_price_for_8pct": v.get("implied_oil_price_for_8pct"),
                "scenarios_10y": v["scenarios"], "buffett_record": c["buffett"],
                "factor_check": "oil/energy factor, weakly correlated with the user's AI + liquidity factor (KMI partially AI via data-center gas demand)",
                "sources_used": [{"source_id": s, "public_date": d, "url": u} for s, d, u in c["sources"]]}
        (ROOT / tk.lower() / AS_OF / "decision_card.json").write_text(json.dumps(card, indent=1, ensure_ascii=False), encoding="utf-8")
        print(tk, card["new_money_verdict"], "base", v["scenarios"]["base"]["irr"], "bb", hp["8pct"], "implied", card["implied_oil_price_for_8pct"])


if __name__ == "__main__":
    main()
