# NBIS Checker Report — as_of 2026-09-05

**batch** memory_ai_refresh_2026-09-05 · **pipeline** lean-6module-v1.1

## Result: **CLEAN (self-checked)**

> ⚠️ **Role-isolation deviation.** `PROTOCOL.md §3` requires Checker != Runner. This batch was
> run by a single agent, so this report is a **self-check**, not an independent review — it cannot
> catch the runner's own systematic bias. What IS independent: `verify_freshness.py` mechanically
> re-fetched the price and ran T1–T6 without reference to the runner's judgement, and every number
> below was **recomputed from the raw inputs** (manifest + scenario CSV) rather than read off the
> card. The verdict label is therefore `CLEAN (self-checked)`, which is weaker than a mega7-batch
> `CLEAN`. No card in this batch was cleared for entry, so the deviation had no decision consequence.

| # | Check | Status | Detail |
|---|---|---|---|
| C1 | freshness gate PASS | **PASS** | freshness_check.json status=PASS exit=0 |
| C2 | market cap = price x shares (recomputed) | **PASS** | 274M x 226.39 = $62,053,499,000 vs card $62,053,499,000 (delta 0.000%) |
| C3 | six modules, signals in [-2,+2] | **PASS** | n=6 signals=[0, 1, 1, 0, -2, -1] net=-1 |
| C4 | distance-from-high recomputed vs stated | **PASS** | recomputed -24.50% vs stated -24.5% |
| C5 | buy_below gap recomputed | **PASS** | buy_below $180.00 is -20.5% from price 226.39 -> NOT triggered |
| C6 | verdict ceiling honoured (no STARTER above buy_below) | **PASS** | new_money_verdict=WATCH with price 20.5% above buy_below |
| C7 | decision_card.json <-> decision_card.md consistent | **PASS** | price + verdict both present |
| C8 | scenario model reconciles to card headline | **PASS** | EV/exit-ARR mid 6.85x; buy_below band carried [150.0, 180.0] |
| C9 | runner_dissent present and substantive | **PASS** | 1065 chars |
| C10 | >=1 primary (A1) source | **PASS** | 4 A1 of 6 total |

## Recomputed headline figures

| Item | Value |
|---|---:|
| as_of_price | **226.39** |
| distance from 52wk high (recomputed) | -24.50% |
| buy_below | $180.00 |
| gap price -> buy_below (recomputed) | -20.5% |
| net module signal | -1 |
| new money / existing | **WATCH** / HOLD |

## Completeness and ceiling

- completeness **~70%** -> verdict ceiling **STARTER** by the completeness rule (60-80 band).
- **PRICE caps first**: price is 20.5% above buy_below, so the ceiling that actually binds is price, not completeness. Raising completeness would NOT flip this card.
- Verdict issued: **WATCH** — consistent with both ceilings.

## Open items the checker could not close

- ACTIVE MW still not disclosed after a second consecutive quarter (K-A).
- Customer concentration not disclosed in the Q2 filing.
- FY2026 ICFR opinion outstanding.

## Checker note

This card downgrades its own language (withdraws 'warming') in a quarter where the operating numbers clearly improved. I checked that this is not over-correction: the July flag was explicitly conditional on the Q2 filing closing the active-MW gap, that condition failed, and K-C partially fired on the $2.8B ATM at $223.6 — essentially the current price. The downgrade is condition-driven, not sentiment-driven.
