# ABT Audit

Last updated: 2026-07-05 | pipeline: lean-6module-v1.1 | as_of: 2026-07-05

---

## Stale-Claim Check

**Result: NO STALE CLAIMS** — cold-start run; no prior version of this dossier existed at `companies/abt/`.

All claims carry `as_of` <= 2026-07-05. Most recent filed data is Q1 2026 (period ended 2026-03-31, 10-Q filed ~2026-04-29). Most recent LIVE data (price) is 2026-07-02 close. Q2 2026 earnings are scheduled 2026-07-16 (11 days after as_of) — the next mandatory refresh trigger.

---

## Internal Consistency Verification

| Check | Status | Notes |
|---|---|---|
| as_of_price appears in all price-bearing files | PASS | $95.40 appears identically in: facts.md, valuation.md, decision_card.json, decision_card.md, brief-v1.html, freshness.json (verified mechanically by verify_freshness.py T5) |
| Market cap calculation | PASS | 1,741.8M x $95.40 = $166.17B (matches ABT-SA-STATS exactly; verified mechanically by verify_freshness.py T3, 0.00% delta) |
| 52-wk high/low band check | PASS | $82.56 <= $95.40 <= $134.65 (verify_freshness.py T1) |
| Distance-from-high reconciliation | PASS | Narrative -29.2% vs card-implied -29.1% (verify_freshness.py T4, 0.1pt gap — rounding only) |
| FY2025 revenue cross-check | PASS | $44,328M in facts.md / claim_ledger.csv / business_model.md / financial_quality.md / valuation.md — identical across all files |
| Q1 2026 segment revenue detail | PASS | Medical Devices $5,539M / Diagnostics $2,180M / Established Pharma $1,426M / Nutrition $2,017M — identical in facts.md, claim_ledger.csv, business_model.md, financial_quality.md |
| Exact Sciences deal terms | PASS | $20.6-21B price, 2026-03-23 close, $20.0B debt issuance — consistent across facts.md, business_model.md, moat_map.md, financial_quality.md, inversion_map.md, valuation.md, decision_card.json |
| Net debt figures | PASS | FY2025 ~$4.41B / Q1 2026 ~$27.24B — identical across facts.md, financial_quality.md, valuation.md, model/scenario_model.csv, decision_card.json |
| China revenue figures | PASS | FY2025 $1.91B/−9.75% YoY — consistent across facts.md, business_model.md, moat_map.md, bottleneck_map.md, inversion_map.md, decision_card.json (with the O4 reconciliation caveat noted consistently everywhere it appears) |
| NEC litigation figures | PASS | $70M jury verdict (2026-04-13), $53M compensatory + $17M punitive — identical across facts.md, moat_map.md, operator_underwriting.md, inversion_map.md, freshness.json, decision_card.json |
| decision_card.json pipeline_version | PASS | lean-6module-v1.1 |
| sources_used in card covers all load-bearing claims | PASS | 15 sources listed in card (subset of the 23 in source_register.md, selected for the highest-load-bearing claims) |
| Verdict consistency | PASS | WATCH (new money) / HOLD (existing) consistent across decision_card.json, decision_card.md, ic_panel.md (unanimous 5/5), valuation.md, brief-v1.html |
| buy_below consistency | PASS | $82-86 STARTER / $70-75 CORE — consistent across valuation.md, decision_card.json, decision_card.md, brief-v1.html |
| IRR figures consistent | PASS | Bear −12.7%/−4.2%, Base +2.4%/+8.5%, Bull +12.9%/+16.3% (3yr/5yr) — identical in valuation.md, model/scenario_model.csv, decision_card.json, decision_card.md, brief-v1.html, ic_panel.md |
| freshness_check.json status | PASS | Mechanically verified via `verify_freshness.py` — exit code 0, all 5 hard tripwires PASS, 1 soft WARN (T6, guidance freshness — see below) |

---

## T6 WARN Disposition (Not a Blocking Issue)

`verify_freshness.py` flagged T6 (LIVE-qualitative freshness for the `guidance` field) as a WARN: the newest guidance source is dated 2026-04-29, which is 67 days before this dossier's as_of date (2026-07-05), exceeding the validator's 45-day freshness heuristic. **This is expected and correct, not a data-quality gap**: Abbott's next earnings report (Q2 2026) is confirmed for **2026-07-16**, which is 11 days AFTER this as_of date — i.e., no newer guidance exists yet to fetch. This is the accurate, most-current-available state of the world, not a missed refresh. Flagged explicitly here per the audit discipline (do not silently pass over a WARN) — this WARN should auto-resolve on the next refresh once Q2 2026 results are available, and it is registered as the top monitoring trigger in research_status.md.

---

## One-Off / Non-Recurring Registration Check

All material one-offs identified and flagged:
- [x] FY2024 one-off tax benefit (inflated GAAP net income to $13,402M / diluted EPS to $7.64 — NOT a clean YoY comp base) → registered in facts.md E20/E22/I5, financial_quality.md
- [x] Exact Sciences acquisition financing costs (Q1 2026 GAAP EPS drag, $0.20 FY2026 guided dilution) → registered in facts.md E30/E36, financial_quality.md, operator_underwriting.md, inversion_map.md
- [x] Weak respiratory season (Q1 2026 rapid/POC diagnostics headwind) → registered in facts.md E30, financial_quality.md
- [x] Nutrition segment cited contract loss (Q4 2025) → registered in facts.md E24, financial_quality.md, moat_map.md

**Note vs GEHC exemplar pattern**: Similar to GEHC, ABT's identified one-offs this run are predominantly on the COST/financing side (Exact Sciences financing, respiratory season) rather than earnings-inflating (except the FY2024 tax benefit, which inflated a PRIOR-period comp, not the current period) — a modestly constructive feature meaning current reported figures are not artificially flattered.

---

## Source Coverage Check

| Source ID | Used In | Tier |
|---|---|---|
| SEC-10K-FY25 | source_register.md, raw/10k_fy2025_extract.md (noted but not directly accessed — SEC 403) | A1 |
| SEC-10Q-1Q26 | source_register.md, raw/q1_2026_earnings_extract.md (noted but not directly accessed — SEC 403 expected pattern) | A1 |
| ABT-Q4FY25-PR | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, valuation.md, raw/10k_fy2025_extract.md, card | A1 |
| ABT-8K-1Q26-STOCKTITAN | facts.md, claim_ledger.csv, business_model.md, financial_quality.md, raw/q1_2026_earnings_extract.md, card | A2 (proxy) |
| MEDTECHDIVE-EXACTSCIENCES | facts.md, claim_ledger.csv, business_model.md, moat_map.md, inversion_map.md, card | B1 |
| ABT-SA-STATS | facts.md, claim_ledger.csv, freshness.json, valuation.md, card | B1 |
| ABT-SA-FINANCIALS | facts.md, claim_ledger.csv, financial_quality.md, valuation.md, card | B1 |
| ABT-SA-BALANCESHEET | facts.md, claim_ledger.csv, financial_quality.md, valuation.md | B1 |
| YAHOO-ABT-PRICE | facts.md, freshness.json, claim_ledger.csv, card | B1 |
| KAVOUT-CGM-SEARCH | facts.md, claim_ledger.csv, moat_map.md, bottleneck_map.md, decision_card.json, card | B2 |
| MORDOR-CGM-MARKET-SEARCH | facts.md, claim_ledger.csv, moat_map.md, decision_card.json, card | B2 |
| INSURANCEJOURNAL-NEC-VERDICT | facts.md, claim_ledger.csv, moat_map.md, operator_underwriting.md, inversion_map.md, freshness.json, decision_card.json, card | B1 |

---

## Robustness-Rule Compliance Check

- [x] Every URL capped at 2 attempts before fallback (SEC EDGAR 403'd on first attempt for both 10-K and 10-Q; immediately pivoted to official Abbott IR press release + stocktitan.net + stockanalysis.com — no retry-loop)
- [x] Each file written to disk immediately upon completion (facts.md first, then claim_ledger.csv/source_register.md, then each subsequent module in sequence) — no hold-in-memory
- [x] `verify_freshness.py` run and achieved PASS status on first attempt
- [x] Completeness target ~65% (DECISION_DRAFT) — met, not over- or under-shot (see completion_checker.md)
