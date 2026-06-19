# 00 Freeze Case — MU as of 2025-03-21

Status: `FROZEN` — blind Runner may begin.
Prepared: 2026-06-16 (orchestrator). Pipeline: lean 6-module (M1–M6) + 00/01/QA/SC.

## 1. Case Identity
- Ticker: MU
- Company: Micron Technology, Inc.
- Exchange / share class: NASDAQ: MU (common)
- Runner: blind subagent (only ≤ as-of evidence)
- Scorer: separate, later (holds sealed outcome)

## 2. Time Boundary
- As-of date: **2025-03-21** (Friday)
- Anchor event: **Q2 FY2025 earnings reported 2025-03-20 after close** (fiscal quarter ended 2025-02-27)
- Price date: 2025-03-21 close
- As-of price: **TO LOCK** by Runner from a historical price series (record source + date)
- Market cap: TO LOCK
- Share count: TO LOCK from latest filing ≤ as-of
- Currency: USD

## 3. Decision Question
- New money: at the 2025-03-21 price, should new money buy MU, and how much?
- Existing position: if already holding, HOLD / ADD / TRIM / EXIT?
- Expected output: business_verdict + new_money_verdict + existing_position_verdict + target size + price bands.

## 4. Allowed Evidence (public_date ≤ 2025-03-21)
| Evidence type | Cutoff rule | Notes |
|---|---|---|
| Filings (FY2024 10-K, Q1 FY2025 10-Q, 8-K) | ≤ as-of | SEC EDGAR |
| Q2 FY2025 earnings release / call (2025-03-20) | ≤ as-of | the anchor print |
| Price / volume / market cap | ≤ price date | historical series |
| Dated industry data (DRAM/NAND/HBM pricing, AI memory demand) | ≤ as-of | dated only; interpretation/lead |
| Sell-side / industry context | ≤ as-of | interpretation, not primary evidence |
| Local notes / video / KOL | ≤ as-of | topic lead / sentiment only |

## 5. Forbidden Evidence (hard — voids the case if used)
- MU stock price or performance after 2025-03-21.
- Any MU filing / release after 2025-03-21 (e.g., Q3 FY2025 ≈ June 2025 and later).
- Later memory-cycle / HBM / AI-capex outcomes after as-of.
- Later guru / fund / 13F actions.
- Any outcome-aware reasoning ("as we know it later …").

## 6. Sealed Outcome Label
SCORER ONLY — left blank at freeze. **Runner must not fill, read into, or infer this.**
- Outcome class:
- Measurement window:
- Realized return vs SOXX / SPY:
- Notes:

## 7. Freeze Checklist
- [x] As-of date fixed (2025-03-21)
- [x] Anchor event fixed (Q2 FY2025 print)
- [x] Allowed evidence listed
- [x] Forbidden evidence listed
- [x] Runner / Scorer separated
- [x] Case ready for Source Pack (01)
