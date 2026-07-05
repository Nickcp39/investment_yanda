# TMO Audit

Last updated: 2026-07-05 | pipeline: lean-6module-v1.1 | as_of: 2026-07-05

---

## Stale-Claim Check

**Result: NO STALE CLAIMS** — cold-start run; no prior version of this dossier existed at `companies/tmo/`.

All claims carry `as_of` ≤ 2026-07-05. Most recent filed data is Q1 2026 (period ended 2026-03-28, 10-Q filed ~2026-04). Most recent LIVE data (price) is 2026-07-02 close.

---

## Internal Consistency Verification

| Check | Status | Notes |
|---|---|---|
| as_of_price appears in all price-bearing files | PASS | $523.44 appears identically in: facts.md, valuation.md, decision_card.json, decision_card.md, brief-v1.html, model/scenario_model.csv |
| Market cap calculation | PASS | 371.62M × $523.44 = $194.52B (matches claimed ~$194.52B across sources) |
| EV calculation | PASS | Market cap $194.52B + net debt ~$39.9B (Q1 2026 basis) ≈ $234.4B, used consistently in valuation.md, model/scenario_model.csv, and decision_card.json |
| FY2025 revenue cross-check | PASS | $44,556M in facts.md / claim_ledger.csv / business_model.md / financials/financial_quality.md — identical across all files |
| FY2025 segment revenue detail | PASS | Life Sciences Solutions $10,374M / Analytical Instruments $7,554M / Specialty Diagnostics $4,676M / Laboratory Products and Biopharma Services $23,984M — identical in facts.md, claim_ledger.csv, business_model.md |
| 52-wk high/low band check | PASS | $403.36 ≤ $523.44 ≤ $643.99 (price correctly within stated 52wk range; independent Yahoo re-fetch $403.47-$638.18 also contains the price, minor ~0.9% cross-source variance on the high noted and flagged) |
| Q1 2026 balance sheet figures | PASS | Cash $3,300M, debt $43,200M, leverage 3.5x net debt/EBITDA — consistent across facts.md, claim_ledger.csv, financials/financial_quality.md, decision_card.json |
| decision_card.json pipeline_version | PASS | lean-6module-v1.1 |
| sources_used in card covers all load-bearing claims | PASS | 17 sources listed in card (subset of the 23 in source_register.md, selected for the highest-load-bearing claims) |
| Verdict consistency | PASS | WATCH (new money) / HOLD (existing) consistent across decision_card.json, decision_card.md, ic_panel.md (unanimous 5/5), valuation.md, brief-v1.html |
| buy_below consistency | PASS | $440-450 STARTER / $375-405 CORE — consistent across valuation.md, decision_card.json, decision_card.md, brief-v1.html |
| IRR figures consistent | PASS | Bear −20.8%/−13.6%, Base +0.3%/+4.6%, Bull +12.8%/+14.1% (3yr/5yr) — identical in valuation.md, model/scenario_model.csv, decision_card.json, decision_card.md, brief-v1.html |
| Danaher peer multiple consistency | PASS | ~18.8x EV/EBITDA cited identically in facts.md, valuation.md, model/scenario_model.csv, decision_card.json |
| CEO grade consistency | PASS | Marc Casper 4/5 cited consistently in operator_underwriting.md, moat_map.md, ic_panel.md, decision_card.md |

---

## One-Off / Non-Recurring Registration Check

All material one-offs identified and flagged:
- [x] Clario acquisition ($8.875B cash outlay, closed 2026-03-24) driving Q1 2026 cash decline and debt increase → registered in facts.md E36-E38, financials/financial_quality.md, operator_underwriting.md
- [x] Microbiology business divestiture to Astorg ($1.1B, expected H2 2026 close) → registered in facts.md E39, financials/financial_quality.md, operator_underwriting.md
- [x] Tariff cost impact (~$375M estimate, NOT independently confirmed against a primary source) → registered in facts.md E46/O5, financials/financial_quality.md
- [x] FY2025 FCF decline (−13.5% YoY, cause unconfirmed) → registered in facts.md I6/O3, financials/financial_quality.md — flagged as the single most important unresolved financial-quality item

**Note vs GEHC/GEV exemplar pattern**: TMO's identified one-offs this run are a genuine MIX — the Clario cash outlay and pending Astorg divestiture are clean, dated, one-time balance-sheet events (similar in kind to GEHC's Intelerad acquisition), while the tariff impact and FCF decline are potentially more structural or at minimum not yet disambiguated (unlike GEHC, where one-offs were more cleanly cost-side/depressing). This mixed picture is flagged explicitly in financials/financial_quality.md as requiring the next refresh's earnings-call-transcript read to fully resolve.

---

## Source Coverage Check

| Source ID | Used In | Tier |
|---|---|---|
| TMO-10K-FY25 | source_register.md, raw/10k_fy2025_extract.md (noted but not directly accessed — SEC 403) | A1 |
| TMO-STOCKTITAN-10K | facts.md, claim_ledger.csv, business_model.md, raw/10k_fy2025_extract.md, card | A2 (proxy) |
| TMO-IR-Q4PR | facts.md, claim_ledger.csv, business_model.md, financials/financial_quality.md, card | A1 |
| TMO-Q1-26-EARNINGS-MULTI | facts.md, claim_ledger.csv, business_model.md, financials/financial_quality.md, raw/q1_2026_extract.md, card | A2 (multi-source corroborated) |
| TMO-SA-FINANCIALS | facts.md, claim_ledger.csv, financials/financial_quality.md, valuation.md, card | B1 |
| TMO-SA-BALANCESHEET | facts.md, claim_ledger.csv, financials/financial_quality.md | B1 |
| TMO-SA-STATS | facts.md, claim_ledger.csv, freshness.json, valuation.md, card | B1 |
| YAHOO-TMO-PRICE | facts.md, freshness.json, claim_ledger.csv, source_register.md, card | B1 (independently re-fetched via repo script) |
| APPLIEDCLINICALTRIALS-CLARIO | facts.md, claim_ledger.csv, business_model.md, moat_map.md, operator_underwriting.md, card | B1 |
| CLINICALLAB-ASTORG-DIVESTITURE | facts.md, claim_ledger.csv, operator_underwriting.md, card | B1 |
| BULLFINCHER-TMO-GEOREVENUE | facts.md, claim_ledger.csv, business_model.md, moat_map.md, bottleneck_map.md, decision_card.json, card | B2 |
| VISIONLIFESCIENCES-BIOSECURE | facts.md, claim_ledger.csv, bottleneck_map.md, inversion_map.md, card | B2 |
| BIOPHARMABOARDROOM-CASPER-JPM | facts.md, business_model.md, operator_underwriting.md, card | B2 |
| SELECTSCIENCE-ASMS2026 | facts.md, moat_map.md, value_chain_map.md, card | B2 (event coverage of A2 announcement) |
| BUSINESSWIRE-NVIDIA-TMO | facts.md, moat_map.md, value_chain_map.md, card | A2 |
| BUSINESSWIRE-ASMS2026 | facts.md, moat_map.md | A2 |
| FINTOOL-CASPER-COMP | facts.md (O6 flagged), operator_underwriting.md | B2 |
| IR-CASPER-BIO | facts.md, operator_underwriting.md, source_register.md | A1 |
| GURUFOCUS-TMO-EVEBITDA | facts.md, valuation.md, model/scenario_model.csv, card | B2 |
| YCHARTS-TMO | facts.md, valuation.md, model/scenario_model.csv | B2 |
| AAII-DANAHER-VALUATION | facts.md, valuation.md, model/scenario_model.csv, card | B1 |
| TIKR-TMO-TARGETS | facts.md, source_register.md | B2 |
| GENOMEWEB-CHINA-COMMENTARY | facts.md, business_model.md, bottleneck_map.md | B2 |

---

## SEC Access Limitation Note

SEC EDGAR direct HTML access returned HTTP 403 on the FIRST attempt for the FY2025 10-K document URL. Per this run's explicit robustness rule ("Cap fetches: at most 2 attempts per URL... never retry-loop"), NO second attempt was made against SEC EDGAR directly for either the 10-K or the subsequently-identified 10-Q — the run immediately pivoted to secondary sources after the first 403, consistent with the GEHC exemplar's identical limitation. Workaround sources used:
1. StockTitan.net structured filing mirrors (10-K) — reproduces primary SEC filing text, treated as A2-proxy tier
2. StockAnalysis.com aggregated financials/balance sheet (B1)
3. Official Thermo Fisher IR press releases (A1)
4. Multi-source earnings-call-transcript corroboration (Motley Fool, Investing.com, GenomeWeb, FierceBiotech, Yahoo Finance, Globe and Mail) — cross-checked across ≥4 independent outlets for Q1 2026 figures, a genuinely broader corroboration set than the GEHC exemplar used

Every load-bearing FY2025/Q1 2026 financial figure is cross-checked across ≥2 of the above. The China-specific exposure question (facts.md O2) could NOT be closed the way GEHC's equivalent question was closed (via the Bullfincher geographic-revenue aggregator) — TMO's own disclosure simply does not break out China separately from "Asia-Pacific," and this is flagged prominently as the single largest evidence gap in this dossier, distinct from a mere sourcing-access limitation.

---

## Robustness-Rule Compliance Check (per RUNNER instructions)

| Rule | Compliance |
|---|---|
| Write each file to disk immediately, not held in memory | PASS — facts.md written first (after raw/ extracts), followed incrementally by claim_ledger.csv, source_register.md, then each module in sequence through to this audit |
| Max 2 fetch attempts per URL | PASS — SEC EDGAR attempted once for the 10-K, immediately failed over to secondary sources; no retry-loop occurred anywhere in this run |
| DECISION_DRAFT ~65% target, not perfection | PASS — completeness assessed at ~65% in M1/decision_card.json; explicit OPEN items registered (O1-O10 in facts.md) rather than papered over |
| Career lens: life-science tools + China exposure surfaced | PASS — business_model.md, moat_map.md, bottleneck_map.md, ic_panel.md, and decision_card.md all explicitly develop the AI/China-instrument-competition theme as the central career-relevant open question |

---

## Audit Verdict

**CLEAN, DECISION_DRAFT (~65% complete).** No stale claims, no internal inconsistencies found across the file set, all one-offs registered, all sources traced to their usage. The dossier is fit for its stated purpose (a DECISION_DRAFT-grade primary-sourced dossier) but is explicitly NOT COMPLETE-grade — see facts.md OPEN items O1-O10 for the specific gaps, most importantly O2 (China-specific revenue/exposure cannot be precisely quantified — the single largest gap versus the GEHC exemplar's rigor), O3 (FY2025 FCF decline cause), O7 (AI revenue attribution, parallel to GEHC's equivalent gap), and O9 (no earnings call transcript fetched this run).
