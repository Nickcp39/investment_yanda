# BFLY Completion Checker (company-level A-F gate)

Last updated: 2026-07-04 · per `frameworks/research_completion_checker.md`

## Status Label: `DECISION_DRAFT` (completeness ~75-80%) -- **not COMPLETE**

## A. Scope And Definition
- [x] Scope frozen: BFLY, Class A common stock (NYSE: BFLY; dual-class structure with Class B super-voting held entirely by founder Rothberg), as_of 2026-07-04, decision = should new money open a position and at what size, horizon 5yr (shorter than the MSFT/GOOGL 10yr horizon in this batch, reflecting BFLY's much earlier stage and the absence of an earnings base to project a decade out).
- [x] Completion criteria stated before the final answer (this file + research_status.md).
- [x] Status label is not stale (cold-start, no prior version of this dossier).

## B. Evidence Engineering
- [x] source_register.md contains every source used by facts/model/modules.
- [x] Raw extracts: 8 primary SEC filings directly read (10-K FY2025, 10-Q Q1 2026, 6 material 8-Ks) -- genuinely deep extraction for a small-cap name, not just aggregated third-party data.
- [~] Full DEF 14A (2026 proxy) beneficial-ownership tables and executive-compensation detail referenced but not deep-extracted (O3 in facts.md) -- non-blocking for a WATCH-tier verdict at this size.
- [x] claim_ledger.csv contains tier/verification-status/source_id for ~80 claims.
- [x] facts.md updated only from verified or explicitly-labeled-derived claims; social/media commentary confined to SENTIMENT section.
- [x] memo/analysis files contain no bare claims (all tagged with source_id or flagged OPEN).
- [x] No stale prior-version claims (cold-start).

## C. Ten-Layer Research
- [x] 1 Direction · [x] 2 Business/quality gate · [x] 3 Evidence · [x] 4 Accounting trend · [x] 5 Value chain · [x] 6 Moat/bottleneck · [x] 7 Operator · [x] 8 Inversion · [x] 9 Valuation/MOS · [x] 10 Decision/monitor
  - Note: layers 6 (moat) and 9 (valuation) reach an explicit, well-evidenced NEGATIVE conclusion (moat is shallow/narrowing; no valuation margin of safety) -- this is a completed layer with an unfavorable finding, not an incomplete layer.

## D. Model And Math
- [x] Revenue drivers (product/software/Embedded-licensing split) tied to evidence.
- [x] Expense/cash-burn model: FY2023-FY2025 + Q1 2026 actuals, normalized bridge separating one-off items (E&O charge, litigation accruals, SBC, warrant FV changes) from recurring economics.
- [x] Runway analysis built from disclosed guidance (Adjusted EBITDA proxy, since no formal FY2026 FCF guide exists) -- flagged as a Runner-derived approximation (O5), directionally robust (>5yr) but not company-guided precisely.
- [x] Implied expectations/IRR rebuilt from current price using an EV/Revenue exit-multiple method (the correct framework given no near-term earnings base) -- 3 scenarios (bear/base/bull) plus one non-base sensitivity row.
- [x] Scenario outputs tied to sources/assumptions in model/scenario_model.csv, each row carrying an explicit rationale.
- [x] Key formulas auditable (scenario_model.csv + PowerShell verification of EV/Revenue arithmetic, matching the task brief's own "15.7-19.2x" framing exactly).

## E. Open Questions And Blockers
- [x] Each OPEN item classified: O1 (unnamed 11% customer) = non-blocking; O3 (DEF 14A detail) = non-blocking for WATCH; O4 (pre-FY2023 share counts) = non-blocking; O6 (next earnings date) = monitoring; Clarius architecture (bottleneck_map.md) = non-blocking for WATCH but would sharpen a future STARTER case; Embedded-partner conversion rate = the single most decision-relevant open item for a future upgrade.
- [x] No item is "blocking" in the sense of preventing a verdict -- the WATCH verdict itself is fully supported by the evidence gathered; the open items would refine, not enable, the analysis.
- [x] Evidence backlog captured in monitor triggers (ic_panel.md §3.5, decision_card.json kill_criteria).

## F. Audit And Consistency
- [x] Audit checked for stale self-description (none; cold-start).
- [x] File index/status reflects current state.
- [x] No prior-version markers (cold-start).
- [x] Content-consistency check: as_of_price $7.68 verified present verbatim in facts.md, valuation.md, model/scenario_model.csv, decision_card.md, decision_card.json (verify_freshness.py T5); market cap/shares/52wk band consistent across all files.
- [x] Final answer reports the true status (DECISION_DRAFT / WATCH), not a more favorable-sounding one.

## Mandatory Self-Check
1. Status label? **DECISION_DRAFT (~75-80%)**
2. Which gates are not fully passed? **B (DEF 14A full extraction), and a genuine substantive OPEN on Clarius's underlying architecture / Embedded-partner conversion rate** -- both non-blocking for the WATCH verdict reached.
3. What would be needed to reach COMPLETE? **Full DEF 14A extraction (O3) + independent resolution of Clarius's probe architecture + Embedded-partner conversion data beyond Midjourney + named identity of the ~11% customer (O1) + 2-3 more quarters of demonstrated profitability trajectory.**
4. Any stale files? **None (cold-start).**
5. Does the language match the actual status? **Yes -- WATCH/DECISION_DRAFT used throughout; no "complete" language used where it would overstate the work.**
