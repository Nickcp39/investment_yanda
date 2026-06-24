# HWM Research Status

Ticker: HWM | As-of: 2026-06-22 | Run: 2026-06-23 | Pipeline: lean-6module-v1.1 | Weights: none

## Honest status: **DECISION_DRAFT** (not COMPLETE)

One-pass live run. Freshness gate PASS. Verdict is well-supported but completeness (~62%) and a few OPEN items (spares precision, direct 10-Q/10-K extraction, owner-earnings bridge, succession) cap it below COMPLETE. The PRICE verdict (WATCH) is robust regardless of those gaps — it is driven by mechanical IRR math on confirmed numbers.

## 11-stage checklist

| # | Stage | File | Status |
|---|---|---|---|
| 0 | Plan / thesis gate | step0_plan.md | DONE |
| 1 | Source register | source_register.md | DONE |
| 2 | Claim ledger | claim_ledger.csv | DONE |
| 3 | Facts (evidence spine, M1) | facts.md | DONE |
| 4 | Raw extracts | raw/ | DONE (light — release-based) |
| 5 | Business model + value chain + moat + bottleneck (M2/M3) | business_model.md, value_chain_map.md, moat_map.md, bottleneck_map.md | DONE |
| 6 | Financial reality (M4) | financials/financial_quality.md, model/*.csv | DONE |
| 7 | Operator underwriting (life-arc) | operator_underwriting.md | DONE |
| 8 | Inversion / trap (M5) | inversion_map.md | DONE |
| 9 | Valuation / price / position (M6) | valuation.md, model/scenario_model.csv | DONE |
| 10 | IC panel + memo + decision card | ic_panel.md, decision_card.json/.md | DONE |
| 11 | Monitor + completeness + freshness | monitor.md, audit.md, completion_checker.md, freshness_check.json | DONE (freshness PASS) |

## Gates NOT yet passed (what would raise to COMPLETE)

- Direct SEC 10-Q/10-K full-text extraction (currently release + aggregators).
- Confirm spares $/% from the 10-Q (O1).
- Clean normalized owner-earnings bridge (O3).
- Plant succession / bench depth disclosure (O5).
- Independent Checker pass (this is the Runner output; Checker not yet run).

## Final verdict summary

- Business: **exceptional**. New money: **WATCH** (0%). Existing: **HOLD**. Max size if/when cheap: ~10%. Buy-below STARTER ~$174.
- Binding constraint: **PRICE** (65x trailing / 57x fwd; negative base 5y IRR). Not completeness, not quality.
