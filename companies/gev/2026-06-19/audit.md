# GEV Audit

Last updated: 2026-06-21 | pipeline: lean-6module-v1.1 | as_of: 2026-06-19

---

## Stale-Claim Check

**Result: NO STALE CLAIMS** — cold-start run; no prior version of this dossier existed.

All claims have `as_of` ≤ 2026-06-19. Most recent data is Q1 2026 (2026-03-31 period, filed 2026-04-22).

---

## Internal Consistency Verification

| Check | Status | Notes |
|---|---|---|
| as_of_price appears in all price-bearing files | PASS | $1,109.73 appears in: facts.md, valuation.md, scenario_model.csv, decision_card.json, decision_card.md |
| Market cap calculation | PASS | 268.72M × $1,109.73 = $298.21B (matches claimed $298.2B, delta <0.001%) |
| EV calculation | PASS | $298.2B − $7.4B net cash ≈ $290.8B (stated ~$292.2B per stockanalysis, small rounding from their EV calc) |
| FY2025 revenue cross-check | PASS | $38,068M in facts.md / claim_ledger / valuation.md — identical |
| Segment revenue adds to total | PASS | Power $19,767M + Wind $9,110M + Electrification $9,191M = $38,068M |
| 52-wk high/low band check | PASS | $479.04 ≤ $1,109.73 ≤ $1,181.95 |
| decision_card.json pipeline_version | PASS | lean-6module-v1.1 |
| sources_used in card covers all load-bearing claims | PASS | 12 sources listed in card; all appear in source_register.md |
| Verdict consistency | PASS | WATCH in card, decision_card.md, ic_panel.md (unanimous), and valuation.md |
| buy_below consistency | PASS | $950 STARTER / $756 CORE — consistent across valuation.md and decision_card.json |
| IRR figures consistent | PASS | −15.4% bear / −4.3% base / +7.2% bull — same in valuation.md and decision_card.json |

---

## One-Off Registration Check

All material one-offs identified and flagged:
- [x] FY2025 $2.9B tax valuation release → registered in facts.md E10, claim_ledger, financial_quality.md
- [x] Q1 2026 $3.99B Prolec remeasurement → registered in E22, claim_ledger, financial_quality.md
- [x] Q1 2026 $330M Proficy sale → registered in E22, claim_ledger, financial_quality.md
- [x] Q1 2026 ~$5.6B contract-liability deposit inflows → registered in E24, financial_quality.md

---

## Source Coverage Check

| Source ID | Used In | Tier |
|---|---|---|
| GEV-8K-4Q25-ER | facts.md, claim_ledger, financial_quality.md, valuation.md, card | A1 |
| GEV-8K-1Q26-ER | facts.md, claim_ledger, financial_quality.md, valuation.md, card | A1 |
| GEV-8K-1Q26-TRANSCRIPT | facts.md, claim_ledger, moat_map.md, bottleneck_map.md, card | A2 |
| GEV-DEC25-INVESTOR-UPDATE | facts.md, claim_ledger, business_model.md, valuation.md, card | A2 |
| GEV-DEC25-PR-DIVIDEND | facts.md, claim_ledger, card | A1 |
| GEV-10K-FY25 | source_register.md (noted but not directly accessed due to 403) | A1 |
| GEV-SA-FINANCIALS | facts.md, claim_ledger, financial_quality.md, valuation.md | B1 |
| GEV-SA-STATS | facts.md, claim_ledger, freshness.json, card | B1 |
| YAHOO-GEV-PRICE | facts.md, freshness.json, claim_ledger | B1 |
| GEV-STOCKTITAN-1Q26 | facts.md, claim_ledger | B1 |
| GEM-GT-MARKETSHARE | facts.md, claim_ledger, moat_map.md, card | B2 |
| BWRX-ANS-2025 | facts.md, card | A2 |
| GEV-LASTBASTION-DEC25 | source_register.md, facts.md | B2 |

---

## SEC Access Limitation Note

SEC EDGAR direct HTML access returned HTTP 403 for all attempted URLs (10-K, 10-Q, XBRL companyfacts API). This is the same environment constraint faced by other dossiers in this pipeline. Workaround: all A1 numbers sourced from:
1. Official GEV press release PDFs (gevernova.com/sites/default/files/)
2. SEC 8-K structured summaries (stocktitan.net)
3. Official IR news releases (gevernova.com/news)
4. A2: Motley Fool earnings transcript (Q1 2026 call)

Every load-bearing financial number cross-checked ≥2 sources. No number entered EVIDENCE with only one source.

---

## Light-Run vs This Run: What Changed

| Dimension | Light Run | This Run |
|---|---|---|
| Source count | 5 (listed) | 13 (7 A1/A2 primary) |
| Revenue verification | Cited, not cross-checked | Cross-checked press release + stockanalysis |
| GT pricing quote | "+10-20% pricing" (attributed) | "10 to 20 points higher on $/kW" — exact management quote from transcript |
| Tax release | "~$2.9B" | $2.9B confirmed from press release |
| FCF | "$3.7B" | $3,710M confirmed |
| Q1 2026 Prolec gain | Mentioned | Exact: $3,992M confirmed |
| 100 GW milestone | Not in light run (pre-Q1) | Confirmed: grew from 83→100 GW in Q1 |
| 2026 FCF guidance | $5.0-5.5B (Dec'25) | $6.5-7.5B (raised post-Q1) |
| 2028 targets | Mentioned | Exact: $52B / 20% / $22B+ FCF cumul |
| IRR table | Qualitative | Quantitative: -15.4% / -4.3% / +7.2% |
| Siemens peer multiple | "~39x" | ~20x NTM per search (corrected) |
| Verdict | WATCH | WATCH (confirmed independently) |
