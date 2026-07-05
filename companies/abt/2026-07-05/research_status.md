# ABT Research Status

as_of: 2026-07-05 | run_date: 2026-07-05 | pipeline: lean-6module-v1.1

## Status: DECISION_DRAFT (~65%)

## Verdict: WATCH (unanimous 5/5 IC panel, zero change after critique) — a shallower WATCH than the GEHC precedent in this same batch

## Freshness Gate: PASS

`verify_freshness.py --dossier companies/abt/2026-07-05` → **STATUS: PASS (exit 0)**. Price $95.40 confirmed via 3 independent sources (repo Yahoo re-fetch, stockanalysis.com, validator's own re-fetch), all 5 hard tripwires (T1-T5) PASS. One soft WARN (T6, guidance freshness — expected, since Q2 2026 earnings are scheduled 2026-07-16, 11 days after this as_of date; no newer guidance exists yet to fetch — see audit.md for full disposition).

## Blocking Issues for Upgrade
- Direct 10-K/10-Q text extraction (SEC 403 on the 10-K first attempt; per robustness rule, no retry — immediately used the official Abbott IR press release + A2-proxy structured mirrors, cross-checked >=2 sources)
- Gross margin discrepancy between official PR (52.6%) and a secondary aggregator (56.42%) unreconciled (O2)
- Post-Exact-Sciences leverage ratio (D/E) not directly disclosed — the ~0.65x estimate is derived, not confirmed (O3)
- China % of total ABT revenue not cleanly reconciled — a possible double-counting artifact in one secondary source (O4)
- FY2025/Q1 2026 free cash flow not independently confirmed (O5) — a real gap given the scale of the Exact Sciences financing event
- Abbott-specific NEC litigation financial exposure not quantified anywhere found (O6) — only a single $70M jury verdict and an industry-wide (not Abbott-specific) ~$4B estimate exist

## What Changed / Was Newly Resolved This Run
- N/A — cold-start run, first dossier for ABT in this repo.
- Key NEW finding vs the immediately-preceding GEHC dossier in this same batch: Abbott's FreeStyle Libre CGM franchise is assessed as the single deepest consumables-annuity moat identified across the S&P 500 medical batch to date (deeper prescription/brand lock-in than GEHC's OEM-agnostic PDx model, though narrower in addressable scope and genuinely contested by Dexcom).
- The Exact Sciences acquisition ($20.6-21B, closed 2026-03-23) is a materially larger relative leverage event (net debt ~6x'd in one quarter) than GEHC's Intelerad deal, and is entirely unproven as of this as_of date (only ~3.5 months post-close).
- NEC infant-formula litigation is a real, already-quantified legal tail-risk ($70M jury verdict, April 2026) with no clean parallel in the GEHC exemplar — CEO Robert Ford's public posture (fight, don't settle) is a genuinely high-conviction, unresolved bet.
- Diagnostics segment shows an early, partially-realized positive inflection (Q1 2026 comparable growth +1.8%, vs FY2025's -4.5% organic) — a more favorable early signal than GEHC had at an equivalent point in its own evidence timeline for the parallel China/VBP-affected segment.

## Next Research Cycle Triggers
- **Q2 2026 results (2026-07-16, confirmed and imminent — 11 days after this as_of date)**: Highest-priority trigger. Will resolve the T6 guidance-freshness WARN, test whether the Diagnostics/China comparable-growth inflection (Q1 2026's +1.8%) is durable or a one-quarter blip, and provide the first management commentary on Exact Sciences integration progress since close.
- Direct 10-K/10-Q MD&A + footnote read if SEC EDGAR access improves: Would resolve O1, O2 (gross margin reconciliation), O3 (confirmed post-deal D/E), and O4 (clean China geographic revenue %).
- Any subsequent NEC litigation development (settlement, further jury verdicts, Congressional-shield legislative progress): Would meaningfully update the M5/inversion risk assessment in either direction.
- Any confirmed ex-US Cologuard/Cancerguard revenue-acceleration disclosure: Would be the single most thesis-moving piece of new evidence for the Exact Sciences bull case.
- FY2025/Q1 2026 free cash flow statement detail (O5): Needed to build a clean owner-earnings bridge post-Exact-Sciences financing.
