# TEM Research Status

as_of: 2026-07-04 | run_date: 2026-07-04 | pipeline: lean-6module-v1.1

## Status: DECISION_DRAFT (~65%)

## Verdict: STARTER (small, 1.5% initial / 4% ceiling) — SPLIT IC panel (2 lean-STARTER-small, 3 WATCH)

## Blocking Issues for Upgrade (toward CORE)
- Exact SEC-primary contract terms for GSK/Merck/Gilead pharma data deals (currently trade-press-sourced; AstraZeneca ~$200M is cross-checked 2 independent trade outlets but still not an SEC-primary dollar figure) — O1
- Diagnostics segment margin / payer-mix breakdown to size the exact magnitude of the company-admitted reimbursement gap vs Foundation Medicine/Guardant Health — O2
- Pathos / SB Tempus related-party pricing terms (arm's-length basis) — governance/earnings-quality item, not currently detailed beyond headline dollar figures — O3
- Confirmed progress on the Palmetto MAC technical-assessment approval / commercial in-network reimbursement-rate negotiations

## Non-Blocking Open Items
- Full indenture/covenant terms of the May 2026 $460M convertible notes (standard unsecured zero-coupon terms cross-checked via secondary sources, not separately fetched from the full 8-K exhibit text)
- FY2026 guidance reiteration (vs any further revision) at Q1 2026 confirmed via ≥2 independent secondary sources, not re-derived from a fully re-fetched guidance paragraph in the Q1 2026 8-K text itself

## Next Research Cycle Triggers
- Q2 2026 results (expected ~August 2026): confirm dilution-rate trend, adj EBITDA trajectory toward the $65M FY2026 guide, and any MAC/reimbursement progress
- Any SEC 8-K disclosing exact GSK/Merck/Gilead contract terms
- Proxy statement (DEF 14A, next expected ~Q3/Q4 2026) for full Lefkofsky compensation structure and any Class B sunset-clause detail not currently confirmed
- Competitive moves: Foundation Medicine (Roche) or Guardant Health announcing a comparable multimodal (imaging+clinical+genomic) data product, which would directly test the `bottleneck_map.md` moat-durability thesis

## Robustness Note (this run)
This run was explicitly re-attempted after a PRIOR run stalled and produced zero output. Robustness measures applied successfully: (1) every file written to disk immediately upon completion, not held in memory; (2) SEC EDGAR WebFetch 403s were treated as an immediate fallback trigger (curl with proper headers), not a retry-loop — max 2 total attempts per URL, with the 2nd attempt routed through a different tool/method rather than blindly repeating the failing one; (3) a material LIVE post-quarter event (May 2026 convertible-notes refinancing) was actively searched for and found, rather than the run stopping at the most recently filed 10-Q. Total run produced 21 files across the full standard file set with no stalls.
