# HWM Audit — Completeness & Verdict Ceiling

As-of: 2026-06-22 | Run: 2026-06-23

## Completeness scoring

| Dimension | Weight | Score | Note |
|---|---:|---:|---|
| Evidence / sourcing (M1) | 20% | 12/20 | Load-bearing numbers corroborated >=2 sources; but no direct EDGAR full-text; spares secondary |
| Theme/mechanism (M2) | 15% | 14/15 | Aero up-cycle + spares annuity well-evidenced (Q1 end-market growth) |
| Profit pool/durability + operator (M3) | 20% | 15/20 | Moat clear; operator strong; succession + spares precision OPEN |
| Financial reality (M4) | 15% | 13/15 | 10y trend + Q1 confirmed; owner-earnings bridge not fully normalized |
| Inversion/trap (M5) | 10% | 9/10 | Valuation/cycle trap well-characterized; no veto |
| Price/position (M6) | 20% | 18/20 | IRR math complete and decisive |
| **Total** | 100% | **~62%** | |

## Verdict ceiling rule (per RUNNER_BRIEF iron rule 2)

`<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`

- Completeness ~62% -> ceiling = **STARTER** (just into the band).
- **But M6 PRICE caps harder:** with a negative base-case 5y IRR and zero margin of safety, the price constraint binds below the completeness ceiling -> **WATCH**.
- This is the intended behavior: "for a name with no price margin of safety, M6 caps before completeness."

## Verdict

- New-money: **WATCH** (price-capped, not completeness-capped).
- Existing: **HOLD**.
- Status: **DECISION_DRAFT**.
- Freshness: **PASS** (freshness_check.json, exit 0).

## What would move the ceiling

- To COMPLETE/STARTER-eligible: direct 10-Q/10-K extraction + spares confirmation + owner-earnings bridge + Checker pass.
- To an actual STARTER *position*: price < ~$174 (margin of safety), independent of completeness.
