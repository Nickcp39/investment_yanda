# SNDK Checker Report — as_of 2026-09-05

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
| C2 | market cap = price x shares (recomputed) | **PASS** | 146M x 1740.0 = $254,770,800,000 vs card $254,770,800,000 (delta 0.000%) |
| C3 | six modules, signals in [-2,+2] | **PASS** | n=6 signals=[2, 2, 0, 1, -2, -2] net=+1 |
| C4 | distance-from-high recomputed vs stated | **PASS** | recomputed -26.10% vs stated -26.1% |
| C5 | buy_below gap recomputed | **PASS** | buy_below $769.00 is -55.8% from price 1740.0 -> NOT triggered |
| C6 | verdict ceiling honoured (no STARTER above buy_below) | **PASS** | new_money_verdict=WATCH with price 55.8% above buy_below |
| C7 | decision_card.json <-> decision_card.md consistent | **PASS** | price + verdict both present |
| C8 | scenario model reconciles to card headline | **PASS** | 30% MOS on prob-weighted $1098.49 = $768.94 vs card $769.00 |
| C9 | runner_dissent present and substantive | **PASS** | 794 chars |
| C10 | >=1 primary (A1) source | **PASS** | 3 A1 of 8 total |

## Recomputed headline figures

| Item | Value |
|---|---:|
| as_of_price | **1740.00** |
| distance from 52wk high (recomputed) | -26.10% |
| buy_below | $769.00 |
| gap price -> buy_below (recomputed) | -55.8% |
| net module signal | +1 |
| new money / existing | **WATCH** / HOLD |

## Completeness and ceiling

- completeness **~60%** -> verdict ceiling **STARTER** by the completeness rule (60-80 band).
- **PRICE caps first**: price is 55.8% above buy_below, so the ceiling that actually binds is price, not completeness. Raising completeness would NOT flip this card.
- Verdict issued: **WATCH** — consistent with both ceilings.

## Open items the checker could not close

- Flash Ventures JV funding mechanics unverified -> the 0.9%-of-revenue capex figure is reported but not economically explained.
- Whether NBM contracts are take-or-pay on price as well as volume.
- The ~80% gross-margin claim is untestable until a down-pricing quarter occurs.

## Checker note

buy_below was RAISED $600 -> $769. I re-derived it independently (30% MOS on the probability-weighted $1,098) and it reconciles. A raised entry line on a name that just fell 24% deserves scrutiny for anchoring-to-price; it survives, because the raise is driven by FY26 *actual* EPS of $73.76 which the June card could not model, and the new line is still 55.8% below the market. The 30/45/25 weighting is the softest input in the batch — it is a judgement, it is stated explicitly, and it is falsifiable via K7.
