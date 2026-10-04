#!/usr/bin/env python3
"""make_cards.py — 电力大国批次 decision_card.json：数字只读 data/valuation_<AS_OF>.json 与各 freshness.json，
判断字段在此集中登记（与各 decision_card.md 对应）。结构沿用 _oil_2026-09-30/make_cards.py。"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-10-03"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VAL = json.loads((HERE / "data" / f"valuation_{AS_OF}.json").read_text(encoding="utf-8"))

COMMON = {
    "as_of": AS_OF, "pipeline_version": "lean-6module-v1.1", "weights_version": "none", "run_date": AS_OF,
    "batch": "power_majors_2026-10-03", "run_type": "first_dossier", "refresh_of": None, "status": "DECISION_DRAFT",
    "clean": False, "clean_blocked_reason": "Checker != Runner (PROTOCOL §3) not met: single agent, self-checked only",
    "price_sources": ["yahoo_chart_api", "cnbc_quote_api"], "price_date": "2026-10-02 (A-shares 2026-09-30)",
    "valuation_method": "batch valuation_model.py (same formula as oil / Pelosi batches); OE0 triangulated between "
                        "net income (or company EPS measures) and OCF - D&A; management growth guidance given 50% credit in base",
    "existing_position_verdict": "N/A (not held)", "suggested_initial_size_pct": 0,
    "study": "studies/电力大国百年_英日中_2026-10-03/report.md",
}

CARDS = {
    "tepco": dict(ticker="9501.T", context_label="turnaround", business_verdict="uncertain",
                  new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                  module_signals={"M1": 1, "M2": -1, "M3": -2, "M4": -2, "M5": -2, "M6": -2}, suggested_max_size_pct=0,
                  binding_constraint="CAPITAL STRUCTURE: NDF preferred convertible into 3,333.3M common (3.08x dilution) + "
                                     "open-ended Fukushima liabilities (FY3/2026 +JPY 903.0B estimate change); then price",
                  completeness_pct=48, share_count_note="common flat; fully diluted basis used (company's own diluted EPS method)",
                  kill_criteria=["K-T1 Fukushima estimate raised > JPY 500B again -> red (just raised 903B)",
                                 "K-T2 NDF announces conversion / sale -> re-evaluate", "K-T3 KK7 grid connection -> green",
                                 "K-T4 common dividend resumed -> green"],
                  next_monitor_event="H1 FY3/2027 tanshin (~late Oct 2026): is full-year guidance still 'undetermined'?",
                  history="TR x0.27 2000-01->2026-10 (-4.8%/yr); max TR drawdown -97%; zero common dividend since 2011",
                  sources=[("TEPCO-TANSHIN-FY26", "2026-04-30", "https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260430/20260427512236.pdf"),
                           ("TEPCO-TANSHIN-Q1FY27", "2026-07-29", "https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260729/20260724599600.pdf")]),
    "kansai": dict(ticker="9503.T", context_label="cyclical_inflection", business_verdict="good",
                   new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                   module_signals={"M1": 1, "M2": 0, "M3": 1, "M4": 1, "M5": -1, "M6": -1}, suggested_max_size_pct=5,
                   binding_constraint="PRICE: 8% line JPY 2,047.51 sits at the 52-week low; non-diversifiable nuclear-accident tail",
                   completeness_pct=55, share_count_note="period-end shares ~+25% in FY3/2025 (issuance + treasury sale); flat since",
                   kill_criteria=["K-K1 nuclear utilization < 60% -> watch (FY27 guide ~70%)", "K-K2 equity ratio < 25% -> green (35.1%)",
                                  "K-K3 new equity issuance -> green (none announced)", "K-K4 any Japanese nuclear accident forcing nationwide shutdown -> green"],
                   next_monitor_event="H1 FY3/2027 tanshin (~late Oct 2026): utilization and full-year guidance",
                   history="TR x2.83 2000-01->2026-10 (+4.0%/yr) vs Nikkei price x3.5; zero dividends 2013-2016",
                   sources=[("KEPCO-TANSHIN-FY26", "2026-04-30", "https://www.kepco.co.jp/ir/brief/disclosure/pdf/kaiji20260430_1.pdf"),
                            ("KEPCO-TANSHIN-Q1FY27", "2026-07-31", "https://www.kepco.co.jp/ir/brief/disclosure/pdf/kaiji20260731_1.pdf")]),
    "kyushu": dict(ticker="642A.T", context_label="cyclical_inflection", business_verdict="good",
                   new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                   module_signals={"M1": 1, "M2": 1, "M3": 1, "M4": -1, "M5": -1, "M6": 0}, suggested_max_size_pct=4,
                   binding_constraint="COMPLETENESS (<60% caps at WATCH) + LEVERAGE (equity ratio 19.9%; anchor A/B gap unexplained); "
                                      "price 0.4% above the 8% line",
                   completeness_pct=53, share_count_note="flat; 9508 -> 642A 1:1 on 2026-10-01 (sole-share transfer)",
                   instrument_change="Kyushu Electric (9508) delisted end-Sep 2026; holders received 1 Kyuden Holdings (642A) share per share on 2026-10-01",
                   kill_criteria=["K-Q1 equity ratio < 17% -> green (19.9%)", "K-Q2 dividend suspended again -> green (JPY 50 guided)",
                                  "K-Q3 equity issuance after HD transition -> none announced",
                                  "K-Q4 Sendai/Genkai long unplanned outage -> green (FY27 guide 84.7%)"],
                   next_monitor_event="first Kyuden Holdings interim tanshin (~late Oct 2026); content of 2026-10-02 representative-director change",
                   history="TR x2.23 2001-01->2026-10 (+3.2%/yr) vs Nikkei price x4.9; 5 zero-dividend years incl. 2023",
                   sources=[("KYUDEN-TANSHIN-FY26", "2026-04-30", "https://www.kyuden.co.jp/var/rev0/0842/4374/0Oebsb62.pdf"),
                            ("KYUDEN-TANSHIN-Q1FY27", "2026-07-31", "https://www.kyuden.co.jp/var/rev0/0888/5400/fbYEeqt2.pdf"),
                            ("KYUDEN-HD-PLAN", "2026-03-26", "https://www.fse.or.jp/files/lis_tkj/26032695084.pdf")]),
    "jpower": dict(ticker="9513.T", context_label="structural_decline_trap", business_verdict="uncertain",
                   new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                   module_signals={"M1": 1, "M2": -1, "M3": 0, "M4": 1, "M5": -1, "M6": -1}, suggested_max_size_pct=4,
                   binding_constraint="PRICE (+47% in 12 months) + undefined coal exit path",
                   completeness_pct=52, share_count_note="-3.8% YoY (buyback); total payout policy 30%",
                   kill_criteria=["K-J1 large coal impairment / early retirement without replacement returns -> not checked",
                                  "K-J2 total payout ratio cut -> green", "K-J3 Ohma nuclear further write-off / cancellation -> watch",
                                  "K-J4 ROE back above cost of equity -> not yet (company's own admission)"],
                   next_monitor_event="H1 FY3/2027 tanshin; new medium-term plan (2024-2026 plan expires)",
                   history="TR x3.90 2004-10->2026-10 (+6.4%/yr) vs Nikkei price x6.3; never suspended dividends; drawdown trough 2020-11",
                   sources=[("JPOWER-TANSHIN-FY26", "2026-04-30", "https://www.jpower.co.jp/news/pdf/kessan2026-4/all.pdf"),
                            ("JPOWER-PRES-FY26", "2026-05-12", "https://www.jpower.co.jp/ir/pdf/260512presentation_1.pdf"),
                            ("JPOWER-TANSHIN-Q1FY27", "2026-07-31", "https://www.jpower.co.jp/news/pdf/kessan2027-1/all.pdf")]),
    "nationalgrid": dict(ticker="NG.L", context_label="exceptional_bottleneck", business_verdict="good",
                         new_money_verdict="WATCH", runner_proposed_verdict="STARTER", runner_proposed_size_pct=2.5,
                         module_signals={"M1": 1, "M2": 1, "M3": 2, "M4": 0, "M5": -1, "M6": 1}, suggested_max_size_pct=6,
                         binding_constraint="PROCESS: independent Checker required before STARTER (PROTOCOL §3); economically the "
                                            "regulatory-return x multiple risk; margin below the 8% line only 1.9%",
                         completeness_pct=60, share_count_note="+~1-1.5%/yr via 25% scrip assumption (derived); 2024/25 rights issue GBP 6.84B",
                         checker_requested=["OE0 = midpoint of adjusted 58.5p and underlying 78.0p EPS",
                                            "g 6% vs management 8-10% EPS CAGR guidance", "8% attainability at EV/RAV 1.42x"],
                         kill_criteria=["K-N1 2026/27 underlying EPS growth < 10% (guide +13-15%)", "K-N2 FFO/net debt < 10% -> green (13.0%)",
                                        "K-N3 another rights issue / large equity raise -> green", "K-N4 adverse major US rate case -> watch"],
                         next_monitor_event="2026/27 half-year results (~Nov 2026)",
                         history="TR x21.7 1995-12->2026-10 (+10.5%/yr) vs FTSE All-Share price x3.1; since 2009 +9.1%/yr vs FTSE 100 TR +8.3%/yr",
                         sources=[("NG-6K-FY26", "2026-05-14", "https://www.sec.gov/Archives/edgar/data/1004315/000165495426004849/a2416e.htm"),
                                  ("NG-20F-FY26", "2026-06-03", "https://www.sec.gov/Archives/edgar/data/1004315/000100431526000006/nggtf-20260331.htm"),
                                  ("NG-6K-OPMODEL", "2026-08-03", "https://www.sec.gov/Archives/edgar/data/1004315/000165495426007117/a8707o.htm"),
                                  ("NG-6K-TVR", "2026-07-23", "https://www.sec.gov/Archives/edgar/data/1004315/000165495426006813/a6117n.htm")]),
    "sse": dict(ticker="SSE.L", context_label="exceptional_bottleneck", business_verdict="good",
                new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                module_signals={"M1": 1, "M2": 1, "M3": 1, "M4": 0, "M5": -1, "M6": 0}, suggested_max_size_pct=5,
                binding_constraint="PRICE (+41% in 12 months; 9% above the 8% line); adjusted EPS excludes deferred tax",
                completeness_pct=56, share_count_note="+9.6% (Nov 2025 GBP 2bn placing); scrip capped at 25%",
                kill_criteria=["K-S1 2026/27 adjusted EPS < 168p", "K-S2 net debt/EBITDA > 4.5x -> green (3.3x)",
                               "K-S3 third dividend cut or another placing -> green", "K-S4 renewables output -20% YoY two quarters -> green"],
                next_monitor_event="2026/27 half-year results (~Nov 2026)",
                history="TR x52 1991-06->2026-10 (+11.8%/yr); dividend cut twice (FY2019/20 -18%, FY2023/24 -38%)",
                sources=[("SSE-FY26-RESULTS", "2026-05-28", "https://www.sse.com/media/jjzbfm1e/fy26-full-year-results-statement-vfinal2.pdf"),
                         ("SSE-Q1-TS", "2026-07-16", "https://www.sse.com/news-and-views/2026/07/sse-has-published-its-q1-trading-statement/")]),
    # ---- 中国（Phase 2）
    "cypc": dict(ticker="600900.SS", context_label="exceptional_bottleneck", business_verdict="exceptional",
                 new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                 module_signals={"M1": 1, "M2": 1, "M3": 2, "M4": 2, "M5": -1, "M6": -1}, suggested_max_size_pct=6,
                 binding_constraint="PRICE: 20.5x OE / 3.5% yield already prices the bond-like dividend story; "
                                    "8% needs 5.5%/yr growth from a fully-developed hydro portfolio",
                 completeness_pct=58, share_count_note="flat; payout >= 70% of NI committed for 2026-2030 (annual report)",
                 kill_criteria=["K-Y1 payout < 70% -> green (70.9%)", "K-Y2 average on-grid tariff -5% -> not checked",
                                "K-Y3 China 10y yield > 3% -> not checked", "K-Y4 two consecutive years of lower generation -> green"],
                 next_monitor_event="Q3 2026 report (~late Oct 2026)",
                 history="TR x13.9 2003-11->2026-10 (+12.2%/yr) vs SSE Composite price x2.75; since 2012-05 +14.7%/yr vs CSI300 ETF TR +5.3%/yr",
                 sources=[("CYPC-AR2025", "2026-04-30", "https://static.cninfo.com.cn/finalpage/2026-04-30/1225262036.PDF"),
                          ("CYPC-IR2026", "2026-08-30", "http://dataclouds.cninfo.com.cn/shgonggao/hsomarket/2026/20260830/ee373d6d0d9347cdb810847c08bf39f7.PDF")]),
    "cgnpower": dict(ticker="1816.HK", context_label="cyclical_inflection", business_verdict="good",
                     new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                     module_signals={"M1": 1, "M2": 0, "M3": 0, "M4": 0, "M5": -1, "M6": -1}, suggested_max_size_pct=4,
                     binding_constraint="PRICE + tariff marketization; growth absorbed by capex (CIP +RMB 28.8B in 2025)",
                     completeness_pct=54, share_count_note="flat; A-share convertible bond in conversion period (~1-2% potential dilution, derived)",
                     kill_criteria=["K-C1 NI down > 5% two years running -> watch (2025 -9.9%, H1 2026 +2.7%)",
                                    "K-C2 major delay of units under construction -> green", "K-C3 payout < 40% -> green (~45%)",
                                    "K-C4 domestic nuclear safety event -> green"],
                     next_monitor_event="Q3 2026 A-share report (~late Oct 2026)",
                     history="H TR x1.38 2014-12->2026-10 (+2.8%/yr) vs Tracker Fund TR +3.5%/yr; A TR x0.98 since 2019-08",
                     sources=[("CGN-AR2025-HKEX", "2026-03-25", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0325/2026032501034_c.pdf"),
                              ("CGN-IR2026-HKEX", "2026-08-25", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0825/2026082500980_c.pdf")]),
    "huaneng": dict(ticker="0902.HK", context_label="cyclical_inflection", business_verdict="uncertain",
                    new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                    module_signals={"M1": 1, "M2": -1, "M3": -1, "M4": -1, "M5": -2, "M6": -1}, suggested_max_size_pct=3,
                    binding_constraint="PRICE on mid-cycle earnings + coal-price cycle; 7.8% trailing yield computed on peak 2025 profit",
                    completeness_pct=55, share_count_note="flat; RMB 77.5B perpetual bonds rank ahead of common",
                    kill_criteria=["K-H1 unit fuel cost +10% -> not checked", "K-H2 full-year common NI < RMB 7B -> watch (H1 5.5B)",
                                   "K-H3 payout < 50% -> green (54%)", "K-H4 perpetual bonds rising again -> green"],
                    next_monitor_event="Q3 2026 report (~late Oct 2026)",
                    history="A TR x3.13 2001-12->2026-10 (+4.7%/yr), price -60% vs 2007-09 peak; H -64% 2015-06->2020-12, +176% 2020-12->2026-09",
                    sources=[("HNP-AR2025", "2026-03-25", "https://cniis.aastocks.com/CNSESH_STOCK/2026/2026-3/2026-03-25/12015930.pdf"),
                             ("HNP-IR2026", "2026-08-19", "https://stockmc.xueqiu.com/202608/600011_20260819_APXK.pdf")]),
    "crpower": dict(ticker="0836.HK", context_label="cyclical_inflection", business_verdict="uncertain",
                    new_money_verdict="WATCH", runner_proposed_verdict="WATCH", runner_proposed_size_pct=0,
                    module_signals={"M1": 1, "M2": 0, "M3": 0, "M4": -1, "M5": -1, "M6": 0}, suggested_max_size_pct=4,
                    binding_constraint="COMPLETENESS (<60% caps at WATCH: minority share after CR New Energy spin-off unchecked); "
                                       "base g 3% runs against H1 2026 renewables core profit -31%",
                    completeness_pct=52, share_count_note="flat in 2026; earlier issuance (Yahoo 4.81B -> 5.18B)",
                    kill_criteria=["K-R1 renewables core profit -20% YoY two halves running -> watch (H1 2026 -31%)",
                                   "K-R2 net debt / equity > 150% -> green (115.5%)", "K-R3 payout < 35% -> green",
                                   "K-R4 thermal core profit turns down -> green (+16%)"],
                    next_monitor_event="FY2026 results (~Mar 2027); monthly generation releases",
                    history="TR x16.1 2003-11->2026-10 (+12.9%/yr) but -52% 2007-10->2020-12; price still -30% vs 2007-10 peak",
                    sources=[("CRP-AR2025-HKEX", "2026-03-18", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800238_c.pdf"),
                             ("CRP-IR2026-HKEX", "2026-08-26", "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600196_c.pdf")]),
}

PASS_THROUGH = ("context_label", "business_verdict", "new_money_verdict", "runner_proposed_verdict", "runner_proposed_size_pct",
                "module_signals", "suggested_max_size_pct", "binding_constraint", "completeness_pct", "share_count_note",
                "kill_criteria", "next_monitor_event", "instrument_change", "checker_requested")


def main():
    for folder, c in CARDS.items():
        tk = c["ticker"]
        v = VAL["tickers"][tk]
        man = json.loads((ROOT / folder / AS_OF / "freshness.json").read_text(encoding="utf-8"))
        lf = {f["field"]: f for f in man["live_fields"]}
        hp = v["hurdle_prices"]
        card = {"ticker": tk, "name": v["name"], **COMMON, "currency": v["ccy"], "quote_unit": lf["price"]["unit"],
                "as_of_price": v["price"], "as_of_market_cap": lf["market_cap"]["value"],
                "shares_out_m": lf["shares_out"]["value"], "wk52_high": lf["52wk_high"]["value"], "wk52_low": lf["52wk_low"]["value"],
                **{k: c[k] for k in PASS_THROUGH if k in c},
                "buy_below_price": hp["8pct"], "hurdle_prices": hp,
                "zones": {"starter": f"<= {hp['8pct']} (base >= 8%)", "add": f"<= {hp['10pct']} (base >= 10%)",
                          "no_chase": f"> {hp['8pct']}", "avoid": f"> {hp['8pct_on_bull']}"},
                "implied_g_for_8pct": v["implied_g_for_8pct"], "scenarios_10y": v["scenarios"],
                "history_shareholder_record": c["history"],
                "factor_check": "rates / regulation / local-currency factor; weakly correlated with the user's AI + liquidity factor",
                "sources_used": [{"source_id": s, "public_date": d, "url": u} for s, d, u in c["sources"]]}
        (ROOT / folder / AS_OF / "decision_card.json").write_text(json.dumps(card, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{folder:13} {tk:8} {card['new_money_verdict']:6} (runner {card['runner_proposed_verdict']}) base {v['scenarios']['base']['irr']:+.1%} "
              f"bb {hp['8pct']} px {v['price']} completeness {c['completeness_pct']}%")


if __name__ == "__main__":
    main()
