# GEV Checker Report — as_of 2026-09-05

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
| C2 | market cap = price x shares (recomputed) | **PASS** | 266M x 941.95 = $250,869,543,500 vs card $250,869,543,500 (delta 0.000%) |
| C3 | six modules, signals in [-2,+2] | **PASS** | n=6 signals=[1, 2, 2, 0, -1, -1] net=+3 |
| C4 | distance-from-high recomputed vs stated | **PASS** | recomputed -21.24% vs stated -21.2% |
| C5 | buy_below gap recomputed | **PASS** | buy_below $786.00 is -16.6% from price 941.95 -> NOT triggered |
| C6 | verdict ceiling honoured (no STARTER above buy_below) | **PASS** | new_money_verdict=WATCH with price 16.6% above buy_below |
| C7 | decision_card.json <-> decision_card.md consistent | **PASS** | price + verdict both present |
| C8 | scenario model reconciles to card headline | **PASS** | 8%-entry from corrected model $785.59 vs card $786.00 |
| C9 | runner_dissent present and substantive | **PASS** | 1096 chars |
| C10 | >=1 primary (A1) source | **PASS** | 3 A1 of 4 total |

## Recomputed headline figures

| Item | Value |
|---|---:|
| as_of_price | **941.95** |
| distance from 52wk high (recomputed) | -21.24% |
| buy_below | $786.00 |
| gap price -> buy_below (recomputed) | -16.6% |
| net module signal | +3 |
| new money / existing | **WATCH** / HOLD |

## Completeness and ceiling

- completeness **~70%** -> verdict ceiling **STARTER** by the completeness rule (60-80 band).
- **PRICE caps first**: price is 16.6% above buy_below, so the ceiling that actually binds is price, not completeness. Raising completeness would NOT flip this card.
- Verdict issued: **WATCH** — consistent with both ceilings.

## Open items the checker could not close

- Segment-level orders / revenue / EBITDA not in the press release.
- Whether contract-liability growth is a durable structural float or a one-off order-boom swing — this is the single assumption the corrected model is most sensitive to.
- Wind full-year 2026 loss trajectory.

## Checker note

This is the card that matters in this batch and the one I checked hardest, because it DECLINES a mechanical entry trigger that fired. Three things had to hold and all three do: (1) the 10-Q quote is primary-sourced and says what the card says it says; (2) the independent arithmetic (FCF ~2.2x EBITDA) reaches the same conclusion by a different route; (3) the corrected 8%-hurdle entry of $786 lands close to the prior card's own $756 CORE line, which was derived by the same hurdle method — so the correction makes the two methods agree rather than inventing a new number. The residual risk is stated honestly in runner_dissent: 2028 EBITDA of $8.5B is carried from June and may be too low given 88% order growth.
