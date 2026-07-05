# BSX Research Status

as_of: 2026-07-05 | run_date: 2026-07-05 | pipeline: lean-6module-v1.1

## Status: DECISION_DRAFT (~65-70%)

## Verdict: STARTER, small initial position (3-2 IC panel split after critique, zero unanimous)

## Blocking Issues for Upgrade
- Direct 10-K/10-Q text extraction (SEC 403 on both attempted endpoint types; per robustness rule, no retry — but the SEC submissions JSON API succeeded and materially strengthened the filing-calendar reconciliation)
- Product-level Watchman/Electrophysiology figures not confirmed from a primary 10-Q segment footnote (O2) — sourced from secondary earnings coverage
- China-specific revenue never separately disclosed by BSX anywhere found this run (O3) — bundled into "Emerging Markets," a material gap vs the GEHC exemplar's clean China disclosure
- Q1 2026 GAAP net income more-than-doubling YoY vs modest adjusted EPS growth — the underlying one-off item not identified (O5)
- Watchman standalone-vs-concomitant procedure split not numerically available (O7) — the single most important unresolved operating question
- Root cause of the ~2026-03-30 price gap not fully confirmed (smallest of the three gap events; does not change the overall narrative)

## What Changed / Was Newly Resolved This Run
- The ~58% price drawdown was fully investigated (not treated as a black-box endpoint check): three distinct, dated gap-down events (2026-02-04, ~2026-03-30, 2026-05-27) were identified and reconciled against specific SEC filing dates/accession numbers via the SEC submissions JSON API (which succeeded where direct document fetch did not), then corroborated by 3-5+ independent secondary sources per event.
- The central competitive/moat finding was precisely quantified: US PFA market share fell from ~100% (2023) to ~41% (early 2026), with Medtronic now LEADING at ~48% — the single most decisive, career-relevant fact in this dossier.
- A critical valuation reframe was independently derived: BSX's EV/EBITDA multiple compressed from an approximate 35x at the 52-week high to an approximate 16x currently — revealing the decline as substantially a multiple-correction story, not primarily an earnings-collapse story.
- Two material, previously-unknown risk factors were surfaced and properly registered: an active securities fraud class action naming 5 executives personally, and a pending $14.5B Penumbra acquisition (BSX's largest ever) committed just 3 weeks before the price decline began.

## Next Research Cycle Triggers
- **Q2 2026 earnings, 2026-07-29** (24 days from as_of): THE single highest-priority near-term trigger — confirms or falsifies whether the "three cuts and done" thesis holds (no fourth guidance cut) or continues.
- Q1 2026 and Q2 2026 earnings-call transcripts (not fetched this run, time/efficiency tradeoff): would likely resolve O2 (product-level figures), O5 (the GAAP/adjusted EPS divergence), and O7 (Watchman standalone-vs-concomitant split), plus provide qualitative color on the litigation and China exposure.
- Direct 10-K/10-Q MD&A + financial-statement footnote read if SEC EDGAR access improves: would resolve O1, and could resolve O3 (China revenue) via the geographic-revenue footnote if BSX discloses it there even without a headline breakout.
- OPAL HDx/FARAVIEW penetration data (currently ~33% of Farapulse accounts): the single most informative leading indicator for whether BSX's EP franchise stabilizes or continues eroding — track this explicitly each refresh.
- Securities litigation status: any settlement, dismissal, or substantive court ruling would be a major, thesis-relevant update in either direction.
- Penumbra deal closing (H2 2026 expected): re-assess ACTUAL (not guided) post-close leverage and integration progress once it happens.
