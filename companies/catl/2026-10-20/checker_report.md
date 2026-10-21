# CATL Checker Report — as_of 2026-10-20, run 2026-10-20 (FIRST CARD)

**batch** catl_battery_screen_2026-10-20 · **pipeline** lean-6module-v1.1 · **instrument** 3750.HK (HKD), A share 300750.SZ shown alongside

## Result: **CLEAN (self-checked)**

> ⚠️ **Role-isolation deviation.** `PROTOCOL.md §3` requires Checker != Runner. This card was run by a single
> agent, so this report is a **self-check**, not an independent review. What IS independent: `verify_freshness.py`
> re-fetched the H close from Yahoo without reference to the card and ran T1–T6; every number below was recomputed
> from the raw inputs (HKEX Q3 report, interim report, monthly return, manifest, scenario CSV) rather than read off
> the card. The card was not cleared for entry, so the deviation had no decision consequence.

| # | Check | Status | Detail |
|---|---|---|---|
| C1 | freshness gate PASS | **PASS** | freshness_check.json status=PASS exit=0; refetched 411.80 (2026-10-20); T1–T6 all PASS. T2 (+2.3% off the 52wk low) carries `low_high_hug_justified: true` — the low is the same session's intraday low, verified on two sources; the in-progress 10-21 session (new low ~370) is excluded by the as_of rule |
| C2 | market cap = price × shares (recomputed) | **PASS** | 4,627,249,686 × 411.80 = HKD 1,905,501,420,695 vs card 1,905,501,420,695 (0.000%); CNBC HKD 1.713T at the live 370.20 implies the same 4,627M count |
| C3 | six modules, signals in [−2,+2] | **PASS** | n=6 signals=[+1, +1, 0, 0, −1, −1] net=0 |
| C4 | distance-from-high recomputed vs stated | **PASS** | 411.80/794.50 − 1 = −48.17% vs stated −48.2% |
| C5 | buy_below gap recomputed | **PASS** | H: price is **+36.2% above the band top 302.3** and +65.4% above the floor 249.0 → price condition NOT met on H. A: 259.08 vs top 257.2 = +0.7% (at the top); live 10-21 ~231 inside |
| C6 | verdict ceiling honoured | **PASS** | new_money_verdict=WATCH, size 0%: on H the price condition fails (K-VAL triggered); on A the STARTER evidence conditions (Q4 GM, FY NP, rebate text, Oct share) are OPEN. `discipline.md` §3.1 requires verdict ≥ STARTER before BUY; completeness 60% caps at WATCH anyway |
| C7 | decision_card.json ↔ decision_card.md consistent | **PASS** | price 411.80 / A 259.08, premium 35.2%, mcap, band H [249.0, 302.3] and A [211.8, 257.2], signals, verdict WATCH 0% / max 3%, K-VAL triggered — all match |
| C8 | scenario model reconciles to card headline | **PASS** | Base: 85 × 1.08⁵ = 124.9B; × 14 = 1,748.5B; ÷ 4,627.25M = CNY 377.9 = HKD 444.3 (CSV 444.2, rounding); IRR@H (444.2/411.8)^⅕ − 1 = +1.5% ✓; IRR@A (377.9/259.08)^⅕ − 1 = +7.8% ✓; 8%-entry 377.9/1.4693 = CNY 257.2 = HKD 302.4 (CSV 302.3) ✓. Stress: 70 → 102.9 → 1,439.9 → CNY 311.2; entry 211.8 / HKD 249.0 ✓ |
| C9 | H/A premium and P/E recomputed | **PASS** | 411.80 × 0.8506 = CNY 350.3; ÷ 259.08 = +35.2% ✓. EPS 2026E 85B/4,627.25M = 18.37; P/E A 14.1x, H 19.1x ✓. FX cross-check 6.6783/7.8472 = 0.8510 vs 0.8506 (0.05%) ✓ |
| C10 | Q3 figures derived from primary 9M − H1 | **PASS** | Revenue 442.14 − 276.92 = 165.22 ✓; NP 64.53 − 43.28 = 21.25 ✓; Q3 GM from 9M cost 341.70 and H1 GM 23.93% → Q3 cost 131.05 → **20.7%** ✓; 9M GM 22.7% ✓. Consensus miss 21.25/26.2 − 1 = −18.9% (card "~−19%") ✓ |
| C11 | net cash recomputed from the Q3 balance sheet | **PASS** | 369.81 + 62.78 − 39.90 − 76.35 − 52.74 − 4.06 = **CNY 259.5B** ✓ (card ~260B). Note: notes payable 152.9B (trade) excluded by convention |
| C12 | runner_dissent present and substantive | **PASS** | ~900 chars; argues the bull case (14x on A, #1 share, net cash) against the H-premium problem and names the missing underwriting |
| C13 | ≥1 primary (A1) source | **PASS** | 3 A1 of 9 (Q3 report, interim report, monthly return); policy source is B1 (official announcement via Xinhua summary, text not fetched) and is flagged as such |
| C14 | as_of discipline | **PASS** | as_of = 10-20 close; the 10-21 in-progress session appears only as a labelled sensitivity column, never as as_of_price |

## Recomputed headline figures

| Item | Value |
|---|---:|
| as_of_price (H) | **411.80 HKD** |
| A share | 259.08 CNY |
| H premium over A | +35.2% |
| distance from 52wk high (recomputed) | −48.2% |
| buy_below band H / A | HKD 249–302 / CNY 212–257 |
| price vs H band top (recomputed) | +36.2% (above) |
| net module signal | 0 |
| new money / max | **WATCH 0%** / 3% |
| kill reds | 1 (K-VAL on H) |

## Completeness and ceiling

Completeness ~60%: first card, no operator underwriting, value-chain or moat map; Q3 segment margins and Q4
production guidance not obtained; the export-rebate change is reported with conflicting terms and is NOT in the
model (a CNY 70B stress scenario stands in for it); the "no US ADR" statement rests on two conflicting secondary
sources. Ceiling: **WATCH** until (a) the official rebate text is read and (b) FY2026 Q4 margin is known.
**Action for the owner:** nothing to execute; if A-share access exists, the price condition is already met and the
decision sits on the evidence list in the card.
