# ASML Research Status

Ticker: ASML | As-of: 2026-07-02 | Run: 2026-07-04 | Pipeline: lean-6module-v1.1 | Weights: none

## Honest status: **DECISION_DRAFT** (not COMPLETE)

One-pass LIVE run. Freshness gate: run after write (see freshness_check.json). Verdict is well-supported but completeness (~65%) and a few OPEN items (FY2025 net-income data conflict, dropped bookings disclosure, no direct 20-F extraction, market-cap source spread) cap it below COMPLETE. The PRICE verdict (WATCH) is robust regardless of those gaps — it is driven by mechanical IRR math on confirmed numbers (and is negative even on ASML's own 2030 targets).

## 11-stage checklist

| # | Stage | File | Status |
|---|---|---|---|
| 0 | Plan / thesis gate | step0_plan.md | DONE |
| 1 | Source register | source_register.md | DONE |
| 2 | Claim ledger | claim_ledger.csv | DONE |
| 3 | Facts (evidence spine, M1) | facts.md | DONE |
| 4 | Raw extracts | raw/ | DONE (light — release/6-K/aggregator based) |
| 5 | Business model + value chain + moat + bottleneck (M2/M3) | business_model.md, value_chain_map.md, moat_map.md, bottleneck_map.md | DONE |
| 6 | Financial reality (M4) | financials/financial_quality.md, model/*.csv | DONE |
| 7 | Operator underwriting (life-arc) | operator_underwriting.md | DONE |
| 8 | Inversion / trap (M5) | inversion_map.md | DONE |
| 9 | Valuation / price / position (M6) | valuation.md, model/scenario_model.csv | DONE |
| 10 | IC panel + decision card | ic_panel.md, decision_card.json/.md | DONE |
| 11 | Monitor + freshness | monitor.md, freshness_check.json | DONE after gate |

## Gates NOT yet passed (what would raise to COMPLETE)

- Direct SEC 20-F / full-filing extraction (currently official ASML releases + 6-K + aggregators).
- Resolve the FY2025 net-income data conflict vs the 20-F (O1) and the market-cap/share-count spread (O3).
- A clean normalized owner-earnings bridge across a full cycle (partially done — 2023 trough vs 2025 peak).
- Independent Checker pass (this is the Runner output; Checker not yet run).

## Final verdict summary

- Business: **exceptional** (arguably the best in the book — a 100% EUV monopoly). New money: **WATCH** (0%). Existing: N/A (not held) -> would be HOLD. Max size if/when cheap: ~10-12% (capped by deep cyclicality + AI-factor concentration in THIS book).
- Binding constraint: **PRICE on normalized earnings** (~62x trailing / ~48x EV/peak-FCF; base 5y IRR ~-5.7%/yr even on ASML's own 2030 midpoint). Secondary: does not diversify the book's AI factor. Not completeness, not quality.
- Buy-below STARTER **~$960**; CORE **~$821**. Top kill-criterion to monitor: **China export controls** (MATCH Act DUV ban + June'26 BIS/EUV enforcement risk).
