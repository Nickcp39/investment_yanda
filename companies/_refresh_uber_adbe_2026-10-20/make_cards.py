#!/usr/bin/env python3
"""make_cards.py — UBER / ADBE 刷新批次的 decision_card.json：数字只读 data/valuation_<AS_OF>.json 与各 freshness.json，
判断字段在此集中登记（与各 decision_card.md 对应）。结构沿用 _trading_rails_2026-10-06。"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-10-20"
RUN_DATE = "2026-10-20"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VAL = json.loads((HERE / "data" / f"valuation_{AS_OF}.json").read_text(encoding="utf-8"))["tickers"]

COMMON = {
    "as_of": AS_OF, "pipeline_version": "lean-6module-v1.1", "weights_version": "none", "run_date": RUN_DATE,
    "batch": "refresh_uber_adbe_2026-10-20", "run_type": "refresh", "status": "DECISION_DRAFT",
    "clean": False, "clean_blocked_reason": "Checker != Runner (PROTOCOL §3) not met for this version: single agent, self-checked",
    "price_sources": ["yahoo_chart_api", "nasdaq_historical_api"], "price_date": AS_OF, "currency": "USD",
    "valuation_method": "batch valuation_model.py (same 10y formula as Pelosi / oil / power / trading-rails batches); "
                        "UBER adds a Delivery Hero cash-flow overlay (year-2 outflow $11.1B, then DH FCF); OE0 = after-tax owner earnings",
    "suggested_initial_size_pct": 0,
}

CARDS = {
    "UBER": dict(
        folder="uber", name="Uber Technologies", refresh_of="companies/uber/2026-09-28", context_label="structural_decline_trap",
        business_verdict="good", new_money_verdict="WATCH", runner_proposed_verdict="STARTER", runner_proposed_size_pct=2,
        existing_position_verdict="HOLD", suggested_max_size_pct=8, completeness_pct=72,
        module_signals={"M1": 1, "M2": 0, "M3": 1, "M4": 1, "M5": -1, "M6": 1},
        binding_constraint="THIN CUSHION (0.9pt over 8%: g -2pt, exit -3x or OE0 -10% each breaks it) + Delivery Hero outcome "
                           "(acceptance period ends 2026-11-05; antitrust long-stop 2027-11-10) + independent Checker not run on the corrected version",
        buy_below_key="8pct",
        zones=lambda hp: {"starter": f"<= {hp['8pct']} (base >= 8%, incl. Delivery Hero overlay)", "add": f"<= {hp['10pct']} (base >= 10%) AND K-U1 green",
                          "no_chase": f"> {hp['8pct']}", "avoid": f"> {hp['8pct_on_bull']}"},
        checker_fixes_applied=["C.1-1 Delivery Hero terms/financing in facts, M4, M5, M6", "C.1-2 OE0 on completed-tax basis (cash tax normalised -$1.44B)",
                               "C.1-3 'half of AV spend' now actually deducted ($1.25B)", "C.1-4 p lowered to 0.5/0.6/0.7",
                               "C.1-5 O-U3 (EUR 4.5B notes) and O-U4 ($15.7B buyback authorisation) closed",
                               "C.1-6 zones aligned to library convention (starter <= 8% line, add <= 10% line)"],
        kill_criteria=["K-U1 Mobility GB cc <10% two straight quarters OR >=2 more top-10 US cities go AV-direct -> green",
                       "K-U2 AV spend >$3B/yr with no volume/revenue disclosure -> yellow",
                       "K-U3 buybacks < SBC -> green (2027 DH closing year may trigger; treat as neutral)",
                       "K-U4 Mobility segment profit/GB falls two straight quarters -> green (7.28% -> 7.64%)",
                       "K-U5 driver-classification regulation >1pp GB cost -> unquantified",
                       "K-U6 NEW: DH offer fails with EUR 700M fee, OR post-close gross leverage >2.5x with buybacks halted >4 quarters -> green",
                       "K-U7 NEW: another CFO change, or AV lead vacant >2 quarters -> yellow (3rd CFO in 3 years; AV lead leaving Nov)"],
        next_monitor_event="2026-11-04 Q3 2026 earnings (Mobility GB cc, segment profit/GB, AV trips); 2026-11-05 Delivery Hero acceptance period ends",
        factor_check="negative exposure to AV success -> diversifier vs BTC/GOOGL/NBIS; but GOOGL (Waymo) is the counterparty",
        sources=[("UBER-10Q-Q2", "2026-08-05", "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm"),
                 ("UBER-8K-DH", "2026-07-16", "https://www.sec.gov/Archives/edgar/data/0001543151/000155278126000382/e26302_ex99-1.htm"),
                 ("UBER-8K-0915", "2026-09-15", "https://www.sec.gov/Archives/edgar/data/1543151/000155278126000486/e26383_uber-8k.htm"),
                 ("UBER-IR-OFFER", "2026-08-27", "https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Publishes-Offer-Document-for-its-Takeover-Offer-for-Delivery-Hero/default.aspx"),
                 ("UBER-8K-CFO", "2026-02-04", "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000011/uber-20260130.htm")]),
    "ADBE": dict(
        folder="adbe", name="Adobe", refresh_of="companies/adbe/2026-08-07", context_label="multiple_broke_not_the_business_but_the_proof_metric_was_retired",
        business_verdict="good", new_money_verdict="WATCH", runner_proposed_verdict="STARTER", runner_proposed_size_pct=3,
        existing_position_verdict="HOLD_TO_ADD", suggested_max_size_pct=6, completeness_pct=74,
        module_signals={"M1": 1, "M2": 1, "M3": 0, "M4": 2, "M5": -1, "M6": 2},
        binding_constraint="COMPLETENESS / VERIFIABILITY + LEADERSHIP TRANSITION, not price: net-new ARR is undisclosed (derived -36% YoY), "
                           "CFO still interim (4 months), Digital Media president leaving, outgoing CEO sold $18.7M; the 'growth-for-users' trade is only "
                           "falsifiable at Q4 FY26 (mid-Dec)",
        buy_below_key="12pct",
        zones=lambda hp: {"starter": f"<= {hp['12pct']} (base >= 12%: verifiability discount, as in 2026-08-07)", "add": "<= 240 (base ~15%) OR K-I passes",
                          "no_chase": f"> {hp['10pct']} (base 10%)", "avoid": f"> {hp['8pct_on_bull']}"},
        checker_fixes_applied=[],
        kill_criteria=["K-A organic Total ARR growth <7% two straight quarters -> yellow (Q3 +11.2% incl. ~1.8pt Semrush)",
                       "K-B revenue cc growth <8% -> green (+12%)", "K-C non-GAAP op margin <40% -> green (44-45%)",
                       "K-D leadership: CEO named (Dec 1) -> half-cleared; interim CFO reaches 2 quarters mid-Dec -> yellow",
                       "K-E disclosure degradation -> green this quarter (MAU, Firefly ARR QoQ added)",
                       "K-F buybacks > FCF -> green (9M 91% of FCF)", "K-G price > ~$352 without upgrade -> green",
                       "K-H quantifiable share loss -> yellow (indirect: net-new ARR -36%, RPO +8%, Figma +48%, Canva +35-43%)",
                       "K-I NEW: growth-for-users trade fails: Q4 net-new ARR <$0.6B or FY27 ARR guide <8% -> decided mid-Dec"],
        next_monitor_event="Adobe MAX (~2026-11-10); new CEO effective 2026-12-01; Q4 FY26 results + FY27 targets mid-Dec 2026",
        factor_check="software/subscription factor; AI is a threat narrative -> diversifier vs the user's AI + liquidity factor",
        sources=[("ADBE-8K-Q3FY26", "2026-09-10", "https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm"),
                 ("ADBE-10Q-Q3FY26", "2026-09-22", "https://www.sec.gov/Archives/edgar/data/0000796343/000079634326000156/adbe-20260828.htm"),
                 ("ADBE-8K-CEO", "2026-09-08", "https://www.sec.gov/Archives/edgar/data/796343/000079634326000144/adbeex9918-k9826.htm"),
                 ("ADBE-CALL", "2026-09-11", "https://www.fool.com/earnings/call-transcripts/2026/09/11/adobe-adbe-q3-2026-earnings-call-transcript/")]),
}


def main():
    for tk, c in CARDS.items():
        v = VAL[tk]
        man = json.loads((ROOT / c["folder"] / AS_OF / "freshness.json").read_text(encoding="utf-8"))
        lf = {f["field"]: f for f in man["live_fields"]}
        hp = v["hurdle_prices"]
        sc = v["scenarios"]
        card = {"ticker": tk, "name": c["name"], **COMMON, "refresh_of": c["refresh_of"],
                "as_of_price": v["price"], "as_of_market_cap": lf["market_cap"]["value"], "shares_out_m": lf["shares_out"]["value"],
                "wk52_high": lf["52wk_high"]["value"], "wk52_low": lf["52wk_low"]["value"],
                **{k: c[k] for k in ("context_label", "business_verdict", "new_money_verdict", "runner_proposed_verdict",
                                     "runner_proposed_size_pct", "existing_position_verdict", "suggested_max_size_pct",
                                     "completeness_pct", "module_signals", "binding_constraint", "kill_criteria",
                                     "next_monitor_event", "factor_check", "checker_fixes_applied")},
                "buy_below_price": hp[c["buy_below_key"]], "buy_below_basis": f"base {c['buy_below_key']} hurdle",
                "hurdle_prices": hp, "zones": c["zones"](hp), "implied_g_for_8pct": v["implied_g_for_8pct"],
                "sensitivity_base": v["sensitivity_base"], "scenarios_10y": sc,
                "sources_used": [{"source_id": s, "public_date": d, "url": u} for s, d, u in c["sources"]]}
        (ROOT / c["folder"] / AS_OF / "decision_card.json").write_text(json.dumps(card, indent=1, ensure_ascii=False), encoding="utf-8")
        print(tk, card["new_money_verdict"], "proposed", c["runner_proposed_verdict"], c["runner_proposed_size_pct"], "base",
              sc["base"]["irr"], "bb", card["buy_below_price"])


if __name__ == "__main__":
    main()
