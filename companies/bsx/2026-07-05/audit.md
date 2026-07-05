# BSX Audit

Last updated: 2026-07-05 | pipeline: lean-6module-v1.1 | as_of: 2026-07-05

---

## Stale-Claim Check

**Result: NO STALE CLAIMS** — cold-start run; no prior version of this dossier existed at `companies/bsx/`.

All claims carry `as_of` ≤ 2026-07-05. Most recent filed data is Q1 2026 (period ended 2026-03-31, 10-Q filed 2026-05-01). Most recent LIVE data (price) is 2026-07-02 close. Most recent qualitative LIVE data (guidance) is the 2026-05-27 Bernstein conference second cut.

---

## Internal Consistency Verification

| Check | Status | Notes |
|---|---|---|
| as_of_price appears in all price-bearing files | PASS | $45.14 appears identically in: facts.md, valuation.md, decision_card.json, decision_card.md, brief-v1.html, freshness.json, model/scenario_model.csv (base setup notes) |
| Market cap calculation | PASS | 1,490M × $45.14 = $67.26B (matches claimed ~$67.09-67.26B across sources, delta <0.3%) |
| 52wk high/low band check | PASS | $42.68 ≤ $45.14 ≤ $108.14 (price correctly within stated Yahoo-basis range); minor basis difference vs stockanalysis.com ($42.25/$109.50) explicitly noted in freshness.json |
| EV calculation | PASS | Market cap $67.26B + net debt ~$9.54B (Q1 2026, pre-Penumbra-close basis) ≈ $76.79B, used consistently in valuation.md and model/scenario_model.csv |
| FY2025 revenue cross-check | PASS | $20,074M in facts.md / claim_ledger.csv / business_model.md / financial_quality.md — identical across all files |
| Q1 2026 segment revenue detail | PASS | MedSurg $1,701M / Cardiovascular $3,503M — identical in facts.md, claim_ledger.csv, business_model.md, raw/earnings_extracts.md |
| Three-guidance-cut timeline | PASS | Feb 4 (10.5-11.5%/$3.43-3.49) → Apr 22 (7.0-8.5%/$3.34-3.41) → May 27 (6.5-8.0% organic) — identical across facts.md, business_model.md, ic_panel.md, decision_card.json, freshness.json |
| PFA share figures (100%→41%, Medtronic 48%) | PASS | Identical across facts.md, moat_map.md, bottleneck_map.md, decision_card.json, decision_card.md, freshness.json |
| decision_card.json pipeline_version | PASS | lean-6module-v1.1 |
| sources_used in card covers all load-bearing claims | PASS | 15 sources listed in card (subset of the 24 in source_register.md, selected for the highest-load-bearing claims) |
| Verdict consistency | PASS | STARTER (2% initial) / HOLD (existing) consistent across decision_card.json, decision_card.md, ic_panel.md (3-2 post-critique), valuation.md, brief-v1.html |
| buy_below / starter_zone consistency | PASS | $42-45 STARTER / $52-58 no-chase ceiling — consistent across valuation.md, decision_card.json, decision_card.md, brief-v1.html |
| IRR figures consistent | PASS | Bear −30.8%/−15.4%, Base −10.6%/+0.1%, Bull +9.7%/+14.3% (3yr/5yr) — identical in valuation.md, model/scenario_model.csv, decision_card.json, decision_card.md, brief-v1.html |
| 35x→16x EV/EBITDA de-rating figure consistency | PASS | Cited identically in valuation.md, model/scenario_model.csv methodology notes, decision_card.json, decision_card.md, brief-v1.html |
| IC panel vote count (3-2) consistency | PASS | Identical across ic_panel.md, decision_card.json runner_dissent, decision_card.md |

---

## One-Off / Non-Recurring Registration Check

All material one-offs and unresolved items identified and flagged:
- [x] Q1 2026 GAAP net income more-than-doubling YoY vs modest adjusted EPS growth (unidentified one-off) → registered in facts.md E26/O5, financial_quality.md
- [x] Three sequential FY2026 guidance cuts (Feb 4 initial, Apr 22 first cut, May 27 second cut) → registered in facts.md E7, business_model.md, raw/earnings_extracts.md, operator_underwriting.md
- [x] Active securities fraud class action (unresolved, material) → registered in facts.md E14, freshness.json (LIVE-qualitative), ic_panel.md, inversion_map.md, decision_card.json
- [x] Pending $14.5B Penumbra acquisition (not yet closed, debt-funded) → registered in facts.md, business_model.md, financial_quality.md, freshness.json, inversion_map.md
- [x] $2B accelerated share repurchase (opportunistic buyback amid the crash) → registered in facts.md E33/C77, operator_underwriting.md, raw/earnings_extracts.md

**Note vs GEHC exemplar pattern**: Unlike GEHC (cost-side one-offs depressing earnings) and unlike a hypothetical earnings-inflating one-off pattern, BSX's most significant flagged item this run (the Q1 2026 GAAP/adjusted EPS divergence) is UNIDENTIFIED as to cause — this is itself an honestly-registered completeness gap, not a judgment call on whether it is benign or concerning. Valuation work throughout this dossier deliberately uses the ADJUSTED EPS basis to sidestep building conclusions on this unconfirmed item.

---

## Source Coverage Check

| Source ID | Used In | Tier |
|---|---|---|
| BSX-10K-FY25 | source_register.md, raw/filing_calendar.md (existence/date confirmed via submissions JSON, content not directly fetched) | A1 |
| BSX-10Q-1Q26 | source_register.md, raw/filing_calendar.md (same) | A1 |
| BSX-SUBMISSIONS-JSON | raw/filing_calendar.md, source_register.md, decision_card.json | A1 |
| BSX-STOCKTITAN-10Q | facts.md, claim_ledger.csv, raw/earnings_extracts.md, financial_quality.md, card | A2 (proxy) |
| BSX-Q4FY25-PR | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, raw/earnings_extracts.md, card | A1 |
| BSX-Q1-2026-PR | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, raw/earnings_extracts.md, card | A1 |
| BSX-PENUMBRA-8K | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, raw/earnings_extracts.md, inversion_map.md, card | A1 |
| BSX-SA-STATS | facts.md, claim_ledger.csv, freshness.json, valuation.md, card | B1 |
| BSX-SA-FINANCIALS | facts.md, claim_ledger.csv, financial_quality.md, valuation.md, card | B1 |
| YAHOO-BSX-PRICE | facts.md, freshness.json, claim_ledger.csv, card | B1 |
| QSIGHT-GUIDEPOINT-PFA2026 | facts.md, claim_ledger.csv, moat_map.md, bottleneck_map.md, decision_card.json, freshness.json, card | B2 |
| BSX-INVESTOR-DAY-2025 | facts.md, claim_ledger.csv, moat_map.md, business_model.md, card | A2 |
| ZLK-CLASSACTION | facts.md, claim_ledger.csv, ic_panel.md, inversion_map.md, freshness.json, card | B1 (legal notice) |
| MORNINGSTAR-PRNEWSWIRE-INVESTORALERT | facts.md (corroborating), freshness.json | B1 (legal notice) |
| MASSDEVICE-APR22 | facts.md, claim_ledger.csv, raw/earnings_extracts.md, card | B1 |
| TRADINGPEDIA-MAY27 | facts.md, claim_ledger.csv, raw/earnings_extracts.md, card | B2 |
| STOCKTWITS-BERNSTEIN | facts.md (corroborating) | B2 |
| MOTLEYFOOL-FEB4 | facts.md, claim_ledger.csv, card | B1 |
| FORBES-FEB5 | facts.md (corroborating) | B1 |
| MEDTECHDIVE-PFARACE | facts.md, raw/competitive_landscape_extract.md (corroborating) | B1 |
| TIKR-MISPRICING | facts.md S3 (sentiment only) | B2 |
| WALLSTREETZEN-OWNERSHIP / GURUFOCUS-MAHONEY | facts.md, claim_ledger.csv, operator_underwriting.md | C1/B2 |
| MEDICALDESIGN-CEOPAY | facts.md, claim_ledger.csv, operator_underwriting.md | B1 |
| SP-MOODYS-CREDITRATING | facts.md, claim_ledger.csv, financial_quality.md | B1 |
| BSX-OPALHDX-PRODUCTPAGE / PRNEWSWIRE-OPAL-LAUNCH | facts.md, moat_map.md, bottleneck_map.md, raw/competitive_landscape_extract.md, card | A2/A1 |

---

## SEC Access Limitation Note

SEC EDGAR direct HTML access returned HTTP 403 Forbidden on the attempts made (cgi-bin/browse-edgar company search AND direct .htm 10-K/10-Q document URLs — 2 total attempts across both endpoint types). Per this run's explicit robustness rule ("Cap fetches at 2 attempts/URL... never retry-loop"), NO further retry was made against SEC EDGAR direct document access — the run immediately pivoted to fallback sources. NOTABLY, unlike the GEHC exemplar, this run discovered that **SEC's own `data.sec.gov/submissions/{CIK}.json` API succeeded (HTTP 200)** even while the traditional browse-edgar/direct-document paths were blocked — this materially strengthened the evidence spine by providing an AUTHORITATIVE (not proxy-sourced) filing calendar with exact accession numbers and item codes, which was used to precisely reconcile each of the three price-gap events against specific, dated corporate disclosures (raw/filing_calendar.md). Workaround sources used for financial line-item content:
1. Official Boston Scientific press releases (news.bostonscientific.com, prnewswire.com) — A1 tier, company-issued
2. StockTitan.net structured 10-Q filing mirror — A2 proxy tier
3. StockAnalysis.com aggregated financials — B1
4. Web search corroboration across multiple independent secondary sources (MassDevice, MedTech Dive, Motley Fool, Forbes, Tradingpedia, law-firm investor alerts)

Every load-bearing FY2025/Q1 2026 financial figure is cross-checked across ≥2 of the above. The three-event price-drawdown narrative (facts.md E7) is corroborated by 3-5+ independent secondary sources per event. The securities litigation (E14) is corroborated across 3+ independent law-firm investor-alert releases.

---

## Robustness-Rule Compliance Check (per RUNNER instructions)

| Rule | Compliance |
|---|---|
| Write each file to disk immediately, not held in memory | PASS — facts.md written first (with an initial critical-finding flag on the drawdown), updated incrementally after research, followed by raw/ extracts, source_register.md, claim_ledger.csv, then each module in sequence |
| Max 2 fetch attempts per URL | PASS — SEC EDGAR direct-document endpoints (2 distinct URL types) each attempted at most twice total; no retry-loop occurred anywhere in this run; fell back fast to the SEC submissions JSON API (which worked) and secondary sources |
| DECISION_DRAFT ~65% target, not perfection | PASS — completeness assessed at ~65-70% in M1/decision_card.json; explicit OPEN items registered rather than papered over (O1-O10 in facts.md) |

---

## Audit Verdict

**CLEAN, DECISION_DRAFT (~65-70% complete).** No stale claims (cold-start run), no internal inconsistencies found across 19 files, all one-offs and unresolved items registered, all sources traced to their usage. The dossier is fit for its stated purpose (a DECISION_DRAFT-grade primary-sourced dossier) but is explicitly NOT COMPLETE-grade — see facts.md OPEN items O1-O10 for the specific gaps, most importantly O2 (product-level Watchman/EP figures not confirmed from a primary financial-statement table), O3 (China revenue never separately disclosed by BSX), O5 (Q1 2026 GAAP/adjusted EPS divergence source unidentified), O7 (Watchman standalone-vs-concomitant numeric split), and the unresolved Mar 30 2026 price-gap root cause (raw/filing_calendar.md).
