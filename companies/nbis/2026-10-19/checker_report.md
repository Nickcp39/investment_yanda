# NBIS Checker Report — as_of 2026-10-16, run 2026-10-19

**batch** nbis_nvda_selloff_rerun_2026-10-19 · **pipeline** lean-6module-v1.1

## Result: **CLEAN (self-checked)**

> ⚠️ **Role-isolation deviation.** `PROTOCOL.md §3` requires Checker != Runner. This batch was run by a
> single agent, so this report is a **self-check**, not an independent review. What IS independent:
> `verify_freshness.py` re-fetched the price from Yahoo without reference to the card and ran T1–T6; every
> number below was recomputed from the raw inputs (manifest + scenario CSV + 6-K exhibits) rather than read
> off the card. No card in this batch was cleared for entry, so the deviation had no decision consequence.

| # | Check | Status | Detail |
|---|---|---|---|
| C1 | freshness gate PASS | **PASS** | freshness_check.json status=PASS exit=0; refetched 165.47 (2026-10-16); T1–T6 all PASS |
| C2 | market cap = price × shares (recomputed) | **PASS** | 274.10M × 165.47 = $45,355,327,000 vs card $45,355,327,000 (0.000%); stockanalysis $45.36B |
| C3 | six modules, signals in [−2,+2] | **PASS** | n=6 signals=[0, 1, 1, 0, −2, 1] net=+1 (prior −1; only M6 moved) |
| C4 | distance-from-high recomputed vs stated | **PASS** | 165.47/299.86 − 1 = −44.82% vs stated −44.8% |
| C5 | buy_below gap recomputed | **PASS** | $180 gate is +8.8% above price → **price condition MET**; band floor $150 is −9.3% |
| C6 | verdict ceiling honoured | **PASS** | new_money_verdict=WATCH although price is inside band — justified: STARTER trigger condition (2) (active MW disclosed) is OPEN; `discipline.md` §3.1 requires verdict ≥ STARTER before BUY |
| C7 | decision_card.json ↔ decision_card.md consistent | **PASS** | price 165.47, verdict WATCH/HOLD, band [150,180], signals, K-G red, reds=1 all match |
| C8 | scenario model reconciles to card headline | **PASS** | EV basis A $37.3B: 45.36 − 14.78 + 6.73 = 37.31 ✓; EV/exit-ARR mid 37.3/8.0 = 4.66x ✓ (card 4.7x); EV/current 12.43x ✓ |
| C9 | runner_dissent present and substantive | **PASS** | 866 chars; argues both sides and names the T0 $500 cap |
| C10 | ≥1 primary (A1) source | **PASS** | 5 A1 of 9 total (four new 6-K exhibits + carried Q2 6-K) |
| C11 | convert arithmetic recomputed from Ex-99.1 | **PASS** | 3.45 + 2.30 = $5.75B ✓; conversion $313.46 = 1000/3.1902 ✓; $324.65 = 1000/3.0802 ✓; premiums 40.0%/45.0% on $223.90 ✓; net $5.68B with options ✓ |
| C12 | monitor rule applied correctly | **PASS** | reds: K-G only (K-VAL downgraded to green with price inside band) → 1 red → no trim; HOLD stands |

## Recomputed headline figures

| Item | Value |
|---|---:|
| as_of_price | **165.47** |
| distance from 52wk high (recomputed) | −44.8% |
| buy_below gate / floor | $180 / $150 |
| price vs gate (recomputed) | −8.1% (inside band) |
| net module signal | +1 |
| new money / existing | **WATCH** / HOLD |
| kill reds | 1 (K-G) |

## Completeness and ceiling

Completeness ~70%: no new financial statements (Q3'26 not yet released; date unannounced); residual
2029/2031 convert principal after the $800M exchange unverified; C110 / C-NEW-ATM unreconciled; the Oct-1
price-increase report is single-source and excluded. Ceiling: this card can be **WATCH** at most until the
Q3'26 6-K is read. **Action for the owner:** re-run on the Q3 release day; the price condition is already met,
so the whole decision sits on one document.
