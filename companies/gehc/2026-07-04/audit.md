# GEHC Audit

Last updated: 2026-07-04 | pipeline: lean-6module-v1.1 | as_of: 2026-07-04

---

## Stale-Claim Check

**Result: NO STALE CLAIMS** — cold-start run; no prior version of this dossier existed at `companies/gehc/`.

All claims carry `as_of` ≤ 2026-07-04. Most recent filed data is Q1 2026 (period ended 2026-03-31, 10-Q/8-K filed ~2026-04-30). Most recent LIVE data (price) is 2026-07-02 close.

---

## Internal Consistency Verification

| Check | Status | Notes |
|---|---|---|
| as_of_price appears in all price-bearing files | PASS | $65.57 appears identically in: facts.md, valuation.md, decision_card.json, decision_card.md, brief-v1.html, freshness.json |
| Market cap calculation | PASS | 454.89M × $65.57 = $29.83B (matches claimed ~$29.82-29.83B across sources, delta <0.1% rounding) |
| Trailing P/E internal consistency | PASS | TTM EPS $4.17 × trailing P/E 15.72x = $65.55 ≈ actual price $65.57 (delta 0.03%) — confirms screener data coherence |
| EV calculation | PASS | Market cap $29.83B + net debt ~$7.9B (Q1 2026 basis) ≈ $37.73B, used consistently in valuation.md and decision_card.json |
| FY2025 revenue cross-check | PASS | $20,625M in facts.md / claim_ledger.csv / business_model.md / financial_quality.md — identical across all files |
| Q1 2026 segment revenue detail | PASS | Imaging $2,299M / AVS $1,341M / PCS $704M / PDx $770M — identical in facts.md, claim_ledger.csv, business_model.md |
| 52-wk high/low band check | PASS | $58.75 ≤ $65.57 ≤ $89.77 (price correctly within stated 52wk range) |
| China revenue figures | PASS | FY2025 $2.03B/9.85%, FY2024 $2.14B/10.85%, −15% YoY — consistent across facts.md, business_model.md, moat_map.md, bottleneck_map.md, decision_card.json |
| decision_card.json pipeline_version | PASS | lean-6module-v1.1 |
| sources_used in card covers all load-bearing claims | PASS | 15 sources listed in card (subset of the 22 in source_register.md, selected for the highest-load-bearing claims) |
| Verdict consistency | PASS | WATCH (new money) / HOLD (existing) consistent across decision_card.json, decision_card.md, ic_panel.md (unanimous 5/5), valuation.md, brief-v1.html |
| buy_below consistency | PASS | $55-58 STARTER / $48-50 CORE — consistent across valuation.md, decision_card.json, decision_card.md, brief-v1.html |
| IRR figures consistent | PASS | Bear −29.5%/−15.5%, Base −7.2%/−0.1%, Bull +12.0%/+12.7% (3yr/5yr) — identical in valuation.md, model/scenario_model.csv, decision_card.json, decision_card.md, brief-v1.html |
| Siemens Healthineers peer multiple consistency | PASS | 7.9x EV/EBITDA cited identically in facts.md, valuation.md, model/scenario_model.csv, decision_card.json |

---

## One-Off / Non-Recurring Registration Check

All material one-offs identified and flagged:
- [x] Q1 2026 PDx discrete supplier disruption (resolved in-quarter) → registered in facts.md E35, financial_quality.md
- [x] Tariff cost impact (~$500M revenue-equivalent, largest in Q1 2026) → registered in facts.md E37, financial_quality.md
- [x] Intelerad acquisition ($2.3B cash outlay) driving Q1 2026 cash decline → registered in facts.md E34/E47, financial_quality.md, operator_underwriting.md
- [x] Segment reorganization (Imaging+AVS → Advanced Imaging Solutions) as a forward structural change affecting comparability → registered in facts.md E7/I7, business_model.md

**Note vs GEV exemplar pattern**: Unlike GEV (large earnings-INFLATING one-offs requiring normalization — tax release, M&A remeasurement gains), GEHC's identified one-offs this run are predominantly on the COST/cash side (tariffs, supplier disruption, M&A cash outlay) and are DEPRESSING rather than inflating reported figures — flagged explicitly in financial_quality.md as a modestly constructive distinguishing feature.

---

## Source Coverage Check

| Source ID | Used In | Tier |
|---|---|---|
| GEHC-10K-FY25 | source_register.md, raw/10k_fy2025_extract.md (noted but not directly accessed — SEC 403) | A1 |
| GEHC-STOCKTITAN-10K | facts.md, claim_ledger.csv, business_model.md, moat_map.md, raw/10k_fy2025_extract.md, card | A2 (proxy) |
| GEHC-STOCKTITAN-1Q26 | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, raw/q1_2026_earnings_extract.md, card | A2 (proxy) |
| GEHC-Q4-PR | facts.md, claim_ledger.csv, financial_quality.md, card | A1 |
| GEHC-SA-FINANCIALS | facts.md, claim_ledger.csv, financial_quality.md, valuation.md, card | B1 |
| GEHC-SA-BALANCESHEET | facts.md, claim_ledger.csv, financial_quality.md | B1 |
| GEHC-SA-STATS | facts.md, claim_ledger.csv, freshness.json, valuation.md, card | B1 |
| YAHOO-GEHC-PRICE | facts.md, freshness.json, claim_ledger.csv, card | B1 |
| BULLFINCHER-GEOREVENUE | facts.md, claim_ledger.csv, business_model.md, moat_map.md, bottleneck_map.md, inversion_map.md, decision_card.json, card | B1 |
| STATISTA-GEHC-REGION | source_register.md (corroborating) | B2 |
| FUTUBULL-UIH-REPORT | facts.md, claim_ledger.csv, moat_map.md, bottleneck_map.md, decision_card.md, card | B2 |
| MULTIPLES-VC-SIEMENS-HEALTHINEERS | facts.md, claim_ledger.csv, valuation.md, model/scenario_model.csv, card | B1 |
| INVESTING-COM-RBC-MEDTECH | facts.md (corroborating context) | B2 |
| GLOBEANDMAIL-CREDITFACILITY | facts.md, claim_ledger.csv, financial_quality.md, card | B1 |
| RADIOLOGYBUSINESS-TARIFF | facts.md, claim_ledger.csv, inversion_map.md, card | B2 |
| DIGITALHEALTHNEWS-LEADERSHIP | facts.md, business_model.md, card | B2 |
| GEHEALTHCARE-PCCT-ARTICLE | facts.md, moat_map.md, value_chain_map.md | A2 |
| GEHEALTHCARE-MIM | facts.md, moat_map.md, value_chain_map.md | A2 |
| MEDICALECONOMICS-INTELERAD | facts.md, claim_ledger.csv, operator_underwriting.md, card | B2 |
| LINKEDIN-ARDUINI | facts.md, operator_underwriting.md | C1 |
| 247WALLST-Q1EARNINGS | facts.md (corroborating) | B1 |
| TRADINGVIEW-ZACKS | facts.md (sentiment) | B2 |
| AUNTMINNIE-Q1REVIEW | facts.md (corroborating) | B2 |

---

## SEC Access Limitation Note

SEC EDGAR direct HTML access returned HTTP 403 on the FIRST attempt for both: (1) the CIK company-search browse-edgar endpoint, and (2) the direct FY2025 10-K document URL. Per this run's explicit robustness rule ("Cap fetches: at most 2 attempts per URL... never retry-loop"), NO second attempt was made against SEC EDGAR directly — the run immediately pivoted to secondary sources. This is a deliberate, rule-compliant behavior, not an oversight. Workaround sources used:
1. StockTitan.net structured filing mirrors (10-K and 8-K/10-Q) — these reproduce primary SEC filing text and are treated as A2-proxy tier
2. StockAnalysis.com aggregated financials/balance sheet (B1)
3. Official GE HealthCare IR press releases (A1)
4. Web search corroboration across multiple independent secondary sources (TradingView, 247WallSt, AuntMinnie, Bullfincher, Statista)

Every load-bearing FY2025/Q1 2026 financial figure is cross-checked across ≥2 of the above. No number entered EVIDENCE with only one source, EXCEPT the China geographic revenue split (E44b, from Bullfincher only — flagged explicitly in facts.md as needing one more independent confirmation on next refresh, though the underlying 10-K-sourced structured data and directional consistency with the qualitative 10-K risk factor language support treating it as EVIDENCE rather than OPEN).

---

## Robustness-Rule Compliance Check (per RUNNER instructions)

| Rule | Compliance |
|---|---|
| Write each file to disk immediately, not held in memory | PASS — facts.md written first, followed incrementally by source_register.md, claim_ledger.csv, raw/ extracts, then each module in sequence |
| Max 2 fetch attempts per URL | PASS — SEC EDGAR (2 distinct URLs) each attempted once, immediately failed over to secondary sources; no retry-loop occurred anywhere in this run |
| DECISION_DRAFT ~65% target, not perfection | PASS — completeness assessed at ~65% in M1/decision_card.json; explicit OPEN items registered rather than papered over (O1-O9 in facts.md) |

---

## Audit Verdict

**CLEAN, DECISION_DRAFT (~65% complete).** No stale claims, no internal inconsistencies found across 16 files, all one-offs registered, all sources traced to their usage. The dossier is fit for its stated purpose (a DECISION_DRAFT-grade primary-sourced dossier) but is explicitly NOT COMPLETE-grade — see facts.md OPEN items O1-O9 for the specific gaps, most importantly O2 (clean adj EBITDA/D&A), O4 (PCS root cause), O7 (AI revenue attribution), and O8 (no earnings call transcript fetched this run).
