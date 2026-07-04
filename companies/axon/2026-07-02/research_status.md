# AXON Research Status

Ticker: AXON | As-of: 2026-07-02 | Run: 2026-07-02 (LIVE) | Pipeline: lean-6module-v1.1 | Weights: none

## Honest status: **DECISION_DRAFT** (not COMPLETE)

One-pass LIVE run. Freshness gate PASS (price $597.04 confirmed across 3 independent sources). Verdict is well-supported but completeness (~70%) and a few OPEN items (no full-text 10-Q/10-K extraction, SBC-masked GAAP owner-earnings bridge, international-share confirmation, and the un-explained +46% melt-up) cap it below COMPLETE. The PRICE verdict (WATCH) is robust regardless of those gaps — it is driven by mechanical IRR math on confirmed adjusted numbers and a cross-check against management's own 2028 targets.

## 11-stage checklist

| # | Stage | File | Status |
|---|---|---|---|
| 0 | Plan / thesis gate | step0_plan.md | DONE |
| 1 | Source register | source_register.md | DONE |
| 2 | Claim ledger | claim_ledger.csv | DONE |
| 3 | Facts (evidence spine, M1) | facts.md | DONE |
| 4 | Raw extracts | raw/ | DONE (light — release-based; 8-K 403) |
| 5 | Business model + value chain + moat + bottleneck (M2/M3) | business_model.md, value_chain_map.md, moat_map.md, bottleneck_map.md | DONE |
| 6 | Financial reality (M4) | financials/financial_quality.md, model/*.csv | DONE |
| 7 | Operator underwriting (life-arc) | operator_underwriting.md | DONE |
| 8 | Inversion / trap (M5) | inversion_map.md | DONE |
| 9 | Valuation / price / position (M6) | valuation.md, model/scenario_model.csv | DONE |
| 10 | IC panel + memo + decision card | ic_panel.md, decision_card.json/.md | DONE |
| 11 | Monitor + freshness | monitor.md, freshness_check.json | DONE (freshness PASS) |

## Gates NOT yet passed (what would raise to COMPLETE)

- Direct SEC 10-Q/10-K/8-K full-text extraction (8-K returned 403; currently primary release + aggregators). (O2)
- Clean normalized owner-earnings bridge reconciling adj EBITDA ($710M) -> FCF ($155M) -> a defensible owner-earnings number net of real SBC dilution. (O1)
- Confirm international-revenue share (20%) and segment splits from the 10-Q. (O3)
- Diagnose the +46% 8-session melt-up (confirm no missed catalyst; likely momentum/index/sentiment). (O5)
- Independent Checker pass (this is the Runner output; Checker not yet run).

## Final verdict summary

- Business: **excellent**. Operator: **builder, 4.5/5**. New money: **WATCH** (0%). Existing: **HOLD** (trim into strength if large). Max size if/when cheap: ~12%. Buy-below STARTER ~$450 / CORE ~$370.
- Binding constraint: **PRICE (+ the parabola)** (~87x non-GAAP / ~70x EV/adj-EBITDA / 16.5x sales; base 5y IRR ~+1.9%). Not completeness, not quality, not the operator.
- Diversification: **YES** — de-correlates from the book's BTC/GOOGL/NBIS AI-capex/liquidity factor (demand = government budgets).
