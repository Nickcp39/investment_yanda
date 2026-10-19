# NVDA Checker Report — as_of 2026-10-16, run 2026-10-19

**batch** nbis_nvda_selloff_rerun_2026-10-19 · **pipeline** lean-6module-v1.1

## Result: **CLEAN (self-checked)**

> ⚠️ **Role-isolation deviation.** `PROTOCOL.md §3` requires Checker != Runner. Single-agent batch, so this
> is a **self-check**. Independent elements: `verify_freshness.py` re-fetched the price and ran T1–T6; the
> cash-flow bridge was pulled from SEC XBRL companyfacts (machine-readable), not transcribed from the card;
> IRRs were recomputed from `model/scenario_model.csv`. No card in this batch was cleared for entry.

| # | Check | Status | Detail |
|---|---|---|---|
| C1 | freshness gate PASS | **PASS** | freshness_check.json status=PASS exit=0; refetched 214.13 (2026-10-16); T1–T5 PASS; **T6 WARN** (guidance source 2026-08-26 is 51d old) — accepted: the 08-26 8-K is still the latest authoritative guidance; Q3 FY27 print ~11-18 |
| C2 | market cap = price × shares (recomputed) | **PASS** | 24,264M × 214.13 = $5,195,650,320,000 vs card $5,195,650,320,000 (0.000%); stockanalysis basic-share basis $5.171T (0.47%) |
| C3 | six modules, signals in [−2,+2] | **PASS** | n=6 signals=[2, 1, 2, −1, −2, 0] net=+2 (prior +3) |
| C4 | distance-from-high recomputed vs stated | **PASS** | 214.13/243.37 − 1 = −12.01% vs stated −12.0% |
| C5 | buy_below gap recomputed | **PASS** | band top $222.44 is +3.9% above price → **price inside band**; floor $148.30 is −30.7% |
| C6 | verdict ceiling honoured | **PASS** | new_money_verdict=WATCH although price ≤ band top — justified: the 09-05 card's STEP 1 (10-Q closes the OCF bridge) is only half-met; STEP 2 entry is gated on STEP 1 by that card's own sequencing |
| C7 | decision_card.json ↔ decision_card.md consistent | **PASS** | price, band, signals, net +2, verdicts, STEP 1 status, K7 all match |
| C8 | scenario model reconciles to card headline | **PASS** | recomputed IRRs at 214.13: bear −19.29%, base **+8.83%**, bull +24.02%, haircut +0.35% — match csv; 8%-neutral entries from y5 values: 326.84/1.08⁵ = $222.44 ✓, 217.9/1.08⁵ = $148.30 ✓ |
| C9 | runner_dissent present and substantive | **PASS** | 905 chars; states the bull case in its strongest form before answering it |
| C10 | ≥1 primary (A1) source | **PASS** | 4 A1 of 8 total (XBRL companyfacts, 10-Q, 8-K 09-03, carried 8-K 08-26) |
| C11 | cash-flow bridge arithmetic | **PASS** | H1 OCF 74,421 − Q1 OCF 50,344 = Q2 24,077 ✓; Q2 NI 118,010 − 58,321 = 59,689 ✓ (card 59,688, rounding); AR: 63,059 − 40,710 = +22,349 ✓; equity gains H1 23,707 − Q1 15,936 = 7,771 ✓ |
| C12 | module moves tied to evidence tier | **PASS** | M4 and M5 moved on A1 evidence (10-Q); M2 moved one notch on C1 secondary evidence (flagged as such); M6 moved on price only |

## Recomputed headline figures

| Item | Value |
|---|---:|
| as_of_price | **214.13** |
| distance from 52wk high (recomputed) | −12.0% |
| band | $148.30 – $222.44 |
| price vs band top (recomputed) | −3.7% (inside) |
| base 5y IRR (recomputed) | +8.83% |
| net module signal | +2 |
| new money / existing | **WATCH** / HOLD |

## Completeness and ceiling

Completeness ~70%: 10-Q customer-revenue concentration and China/export sections read only via secondary
summaries; the $400M H200 charge not located in the 10-Q text; names behind the five ≥10%-of-AR customers
undisclosed; OpenAI-revenue report is secondary (CNBC 403 to the fetcher). Ceiling: **WATCH** until the Q3
FY27 cash-flow statement (~2026-11-18) answers the re-specified STEP 1. **Action for the owner:** re-run on
the Q3 release; the entry price condition is already met, so the decision sits on OCF/NI and AR/revenue.
