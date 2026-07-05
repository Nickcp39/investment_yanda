# SYK Audit

Last updated: 2026-07-05 | pipeline: lean-6module-v1.1 | as_of: 2026-07-05

---

## Stale-Claim Check

**Result: NO STALE CLAIMS** — cold-start run; no prior version of this dossier existed at `companies/syk/`.

All claims carry `as_of` <= 2026-07-05. Most recent filed data is Q1 2026 (period ended 2026-03-31, 8-K/10-Q reported ~2026-04-30). Most recent LIVE data (price) is 2026-07-02 close.

---

## Internal Consistency Verification

| Check | Status | Notes |
|---|---|---|
| as_of_price appears in all price-bearing files | PASS | $326.54 appears identically in: facts.md, valuation.md, model/scenario_model.csv (methodology notes), decision_card.json, decision_card.md, brief-v1.html, freshness.json |
| Market cap calculation | PASS | 383.36M x $326.54 = $125,182.37M (matches claimed ~$125.18B across sources, delta <0.01%) |
| EV calculation | PASS | Market cap $125.18B + net debt ~$11.85B (Q1 2026 basis) = ~$137.03B, used consistently in valuation.md and model/scenario_model.csv |
| FY2025 revenue cross-check | PASS | $25,116M in facts.md / claim_ledger.csv / business_model.md / financial_quality.md — identical across all files |
| Q1 2026 balance sheet detail | PASS | Cash $2,878M / debt $14,723M / equity $22,979M / goodwill+intangibles $24,704M — identical in facts.md, claim_ledger.csv, financial_quality.md |
| 52-wk high/low band check | PASS | $281.00 <= $326.54 <= $404.87 (price correctly within stated 52wk range) |
| Mako installed-base figures | PASS | 3,000+ systems, 1M+/2M+ procedures — consistent across facts.md, business_model.md, moat_map.md, bottleneck_map.md, decision_card.json/md, brief-v1.html |
| China VBP growth-rate figures | PASS | -1.4% (2024) / -1.5% guided (2025) — consistent across facts.md, business_model.md, bottleneck_map.md, decision_card.json |
| decision_card.json pipeline_version | PASS | lean-6module-v1.1 |
| sources_used in card covers all load-bearing claims | PASS | 12 sources listed in card (subset of the 22 in source_register.md, selected for the highest-load-bearing claims) |
| Verdict consistency | PASS | STARTER (new money) / HOLD_TO_ADD (existing) consistent across decision_card.json, decision_card.md, ic_panel.md (unanimous 5/5), valuation.md, brief-v1.html |
| Buy-below / sizing consistency | PASS | Initial 3% / max 7%, STARTER already qualifies at current price, CORE zone ~$292-334 — consistent across valuation.md, decision_card.json, decision_card.md, ic_panel.md, brief-v1.html |
| IRR figures consistent | PASS | Bear -14.0%/-5.0%, Base +11.1%/+12.5%, Bull +21.6%/+21.1% (3yr/5yr) — identical in valuation.md, model/scenario_model.csv, decision_card.json, decision_card.md, brief-v1.html |
| Peer forward P/E consistency | PASS | MDT 13.67x, ZBH 10.98x, ISRG 45.96x, SYK 20.86x cited identically in facts.md, claim_ledger.csv, valuation.md, model/scenario_model.csv |
| Cyber incident figures ($375M, March 11 2026, ~3wk shutdown) | PASS | Consistent across facts.md, business_model.md, financial_quality.md, inversion_map.md, decision_card.json/md, freshness.json, brief-v1.html |

---

## One-Off / Non-Recurring Registration Check

All material one-offs identified and flagged:
- [x] March 2026 cyber incident (~$375M deferred/lost Q1 sales, ~3-week shutdown, restored by early April) → registered in facts.md E21, financial_quality.md, inversion_map.md
- [x] Tariff cost impact (~$400M FY2026 total, incremental ~$200M vs 2025, weighted to H1) → registered in facts.md E23, financial_quality.md
- [x] ~$5.0B FY2025 acquisitions cash outlay (AVS ~$435M+$400M milestones in 2026, Inari 2025) → registered in facts.md E15/E44-E45, financial_quality.md, operator_underwriting.md
- [x] Orthopaedics segment reported-vs-organic growth divergence (+4.3% vs +9.5%) flagged as an unresolved item, not assumed benign → registered in facts.md I4/O2, moat_map.md, bottleneck_map.md

**Note vs GEV/GEHC exemplar patterns**: Unlike GEV (large earnings-INFLATING one-offs requiring normalization), SYK's identified one-offs this run are predominantly on the COST/disruption side (cyber incident, tariffs) and are DEPRESSING rather than inflating reported figures — similar in character to GEHC's one-off pattern, but here the one-off is a SINGLE, dated, well-explained event (not three consecutive quarters of unexplained margin compression), a meaningfully more favorable financial-quality signal than the GEHC comparison.

---

## Source Coverage Check

| Source ID | Used In | Tier |
|---|---|---|
| SYK-10K-FY25 | source_register.md, raw/10k_fy2025_extract.md (noted but not directly accessed — SEC 403) | A1 |
| SYK-Q4-PR | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, card | A1 |
| SYK-Q1-PR | facts.md, claim_ledger.csv, financial_quality.md, inversion_map.md, freshness.json, card | A2 |
| STOCKTITAN-SYK-10K | facts.md, claim_ledger.csv, business_model.md, moat_map.md, raw/10k_fy2025_extract.md | A2 (proxy) |
| SYK-STOCKTITAN-1Q26 | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, raw/q1_2026_earnings_extract.md, card | A2 (proxy) |
| STOCKTITAN-SYK-CYBER | facts.md, financial_quality.md, inversion_map.md, freshness.json | B1 |
| STOCKTITAN-SYK-MAKO | facts.md, claim_ledger.csv, business_model.md, moat_map.md, bottleneck_map.md, freshness.json, card | B1 |
| STOCKTITAN-SYK-MA | facts.md, claim_ledger.csv, operator_underwriting.md, card | B1 |
| SYK-8K-AVS | source_register.md (corroborating) | B2 |
| SYK-SA-STATS | facts.md, claim_ledger.csv, freshness.json, valuation.md, card | B1 |
| SYK-SA-FINANCIALS | facts.md, claim_ledger.csv, financial_quality.md, card | B1 |
| SYK-SA-BALANCESHEET | facts.md, claim_ledger.csv, financial_quality.md | B1 |
| YAHOO-SYK-PRICE | facts.md, freshness.json, claim_ledger.csv, card | B1 |
| SYK-PROXY | facts.md, claim_ledger.csv, operator_underwriting.md | B2 |
| SYK-PROXY-2026 | facts.md, claim_ledger.csv, operator_underwriting.md, card | B2 |
| LINKEDIN-LOBO | facts.md, operator_underwriting.md | C1 |
| STOCKTITAN-SYK-NEWS | facts.md (corroborating) | B1 |
| STOCKTITAN-SYK-CEO-PROFILE | facts.md, operator_underwriting.md | B2 |
| AAOS-2025-COVERAGE | facts.md, moat_map.md | B2 |
| ISRG-10K-CROSSCHECK | facts.md, moat_map.md, bottleneck_map.md | B1 |
| MDT-10K-CROSSCHECK | facts.md, moat_map.md | B1 |
| SYK-Q1-EARNINGS-CALL-COMMENTARY | facts.md, ic_panel.md, decision_card.json | B2 |

---

## SEC Access Limitation Note

SEC EDGAR direct HTML access returned HTTP 403 Forbidden on the FIRST attempt for direct filing document fetches. Per the robustness rule ("max 2 attempts per URL, no retry-loop"), NO second attempt was made against SEC EDGAR directly — the run immediately pivoted to secondary sources. This is a deliberate, rule-compliant behavior, not an oversight. Workaround sources used:
1. Official Stryker IR press releases (Q4/FY2025 and Q1 2026 earnings releases) — A1 tier
2. StockTitan.net structured filing mirrors (10-K and 8-K/10-Q) — these reproduce primary SEC filing text and are treated as A2-proxy tier
3. StockAnalysis.com aggregated financials/balance sheet (B1)
4. Web search corroboration across multiple independent secondary sources

Every load-bearing FY2025/Q1 2026 financial figure is cross-checked across >=2 of the above. Mako-specific unit/procedure-volume figures (installed base, procedure counts) trace to official IR press releases and are treated as A1/A2; Mako-specific FINANCIAL estimates (direct revenue ~$1.0B, market share ~85%+) are explicitly flagged B2/analyst-estimate tier, NOT company-disclosed segment data (facts.md O5). China-specific competitive-landscape names (Tinavi, MicroPort, Weigao, AK Medical, Chunli) are NOT Stryker-filed — sourced from independent industry research, clearly flagged B2 tier in facts.md.

---

## Robustness-Rule Compliance Check (per RUNNER instructions)

| Rule | Compliance |
|---|---|
| Write each file to disk immediately, not held in memory | PASS — facts.md written first, followed incrementally by claim_ledger.csv, source_register.md, then each module in sequence |
| Max 2 fetch attempts per URL | PASS — SEC EDGAR attempted once per URL, immediately failed over to secondary sources; no retry-loop occurred anywhere in this run |
| DECISION_DRAFT ~65-70% target, not perfection | PASS — completeness assessed at ~65-70% in M1/decision_card.json; explicit OPEN items registered rather than papered over (O1-O9 in facts.md) |

---

## Audit Verdict

**CLEAN, DECISION_DRAFT (~65-70% complete).** No stale claims, no internal inconsistencies found across 17 files, all one-offs registered, all sources traced to their usage. The dossier is fit for its stated purpose (a DECISION_DRAFT-grade primary-sourced dossier) but is explicitly NOT COMPLETE-grade — see facts.md OPEN items O1-O9 for the specific gaps, most importantly O3 (China-specific revenue/robotics-competitive data), O4 (implant pull-through quantification), O2 (Orthopaedics segment growth divergence), and O8 (no earnings call transcript fetched this run).
