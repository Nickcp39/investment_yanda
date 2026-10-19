# NBIS Decision Card — as_of 2026-10-16 close, run 2026-10-19 (SELLOFF RERUN + CONVERT FINANCING)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-10-19
**batch** nbis_nvda_selloff_rerun_2026-10-19 · **status** DECISION_DRAFT · **completeness** ~70%
**refresh_of** `companies/nbis/2026-09-05` · **context_label** `price_inside_band_for_the_first_time_proof_metric_still_open_leverage_leg_realised_peer_credit_stress`

> as_of is the **2026-10-16 Friday close**. The run was made on Monday 2026-10-19 during the session
> (NBIS traded ~$172 intraday at fetch time); an in-progress session is never used as as_of_price.

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **165.47** (2026-10-16 close; Yahoo + stockanalysis history, delta 0.00%) |
| market cap | ~$45.36B (274.10M shares) |
| vs prior card ($226.39, 2026-09-04) | **−26.9%** |
| distance from 52-week high $299.86 (intraday, 2026-06-22) | **−44.8%** |
| one week / one month | −25.2% / −24.1% (2026-10-16 single day −12.2%) |
| business_verdict | **good** (unchanged, four cards) |
| **new_money_verdict** | **WATCH (0%)** — fourth consecutive; **price condition of the STARTER trigger is now MET, evidence condition is not** |
| existing_position_verdict | **HOLD** (one kill flag red, not two; see monitor rule) |
| suggested initial / max size | **0% / 4%** |
| **buy_below** | **$150–180 UNCHANGED** (four cards). **Price is INSIDE the band: 8% below the $180 STARTER gate, 10% above the $150 floor** |
| **no_chase_zone** | ≥ $250 (carried) — 34% above price, irrelevant today |
| binding_constraint | **EVIDENCE, no longer price**: active MW undisclosed for four quarters; the fifth answer arrives with Q3'26 (date not announced; last year's Q3 came 11-11) |

## Six-module signals (net +1; prior −1) — baseline 09-05

| Module | Role | 08-12 | 09-05 | **10-19** | One line |
|---|---|---:|---:|---:|---|
| M1 Evidence Spine | confidence | −1 | 0 | **0** | Four primary 6-Ks since the last card (convert pricing/closing, AGM, Palantir, Inferize) all reached; **no new financial statements**; active MW still absent |
| M2 Theme / Mechanism | context | +1 | +1 | **+1** | Company-level evidence unchanged (5 GW contracted, RPO $33.6B); Palantir sovereign-stack partnership is primary but carries no dollar terms. Sector narrative took hits (OpenAI revenue shortfall report, Gartner neocloud warning) — scored in M5, not here |
| M3 Profit Pool / Durability | conviction | +1 | +1 | **+1** | No new transacted-price data. A reported Oct-1 list-price increase (H100 ~+17%, B300 ~+21%) is **secondary and unverified** — not credited |
| M4 Financial Reality | conviction | 0 | 0 | **0** | Liquidity up: $5.75B converts closed 08-24 (net ≈ $5.68B). Debt up by the same amount at 0.50% / 4.50%. Quarterly FCF still ≈ −$3.4B on the last reported quarter. Nets to zero until Q3 shows cash conversion |
| M5 Inversion / Trap | risk | −2 | −2 | **−2** | Leverage leg **realised, not just planned** ($3.75B plan → $5.75B done); conversion prices $313–325 are 90–96% above today's price, so the notes behave as debt. Peer CoreWeave bonds ~79c / CDS ~643bp; Gartner says most neoclouds will not survive independently; short interest 19.5% of float; Burry leveraged puts (secondary) |
| M6 Price / Position | price | −1 | −1 | **+1** | First card with price inside the band. EV/exit-2026-ARR mid ≈ **4.7x** (was 6.85x), EV/current ARR ≈ 12.5x (was 18.3x) |

## Kill criteria — status after this run

**K-A** active MW undisclosed — 🟡 **open, fourth quarter; Q3'26 is the fifth test** · **K-B** anchor risk — 🟢 (no anchor-contract news; RPO stands) · **K-C** prepayment → dilution — 🟡 **partly realised**: $800M of 2029/2031 notes exchanged for ~15.8M Class A shares (≈5.8% of shares out) on 08-24, on top of the $2.8B ATM at $223.6 avg recorded at 09-05 (C-NEW-ATM, still unreconciled to a primary line item) · **K-D** rev/MW declining — 🟢 · **K-E** capex without conversion — 🟢 (no new capex guide) · **K-F** concentration / ICFR — ⬜ · **K-G** leverage branch — 🔴 **TRIGGERED on quantity**: converts $5.75B vs the $3.75B plan the flag was written for; total convertible stock now ≈ $5.95B+ plus $775M ABF; peer credit stress is the market pricing this branch · **K-VAL** — 🟢 **downgraded from red**: price is inside the band.

**Monitor rule (2 reds → trim):** one red (K-G). **Not triggered.** Existing position stays HOLD.

## WATCH → STARTER trigger (restated, not changed)

**(1)** price below ~$180 — **MET at $165.47**. **(2)** active MW actually disclosed, with the ARR ramp test ($3.0B → $7–9B exit-2026) still on track at Q3 — **OPEN**. Condition (2) resolves on one dated document: the Q3'26 release. **Nothing in this run changes the verdict before that document.** If Q3 discloses active MW and ARR ≥ ~$5B with FY26 guidance intact, STARTER opens at ≤4% with price already inside the band; if Q3 again omits active MW, the card should ask why a fifth time and the band moves down, not the verdict up.

## Conflicts carried

- **C110** deferred-revenue basis (~$1.2B apart) — unresolved. **C111** net-debt basis — **superseded**: after the converts the company is unambiguously a net borrower on gross debt (~$6.7B+ debt vs ~$14.8B pro-forma cash before Q3 burn); EV shown on two bases in `model/`. **C-NEW-ATM** — unresolved; not used to fire K-C beyond "partly realised".

## runner_dissent

The honest case for moving today: EV at roughly 4.7x exit-2026 ARR against a $33.6B RPO and 5 GW contracted is a price this card has never seen, the drawdown is 45%, and waiting for a disclosure the company has withheld four times may mean never buying. The honest case against: the company itself set the equity reference at $223.90 when it priced $5.75B of converts eight weeks ago, the conversion prices are above $313, and the market has since repriced the whole neocloud credit stack, not just this name. The price got cheap because the leverage branch this card flagged in August is now being tested in public. The cost of waiting is bounded: Q3 is weeks away. One more constraint sits outside the card: under `trading-desk/risk_limits.md` the book is at **T0, single-name real-money cap $500**, so this entire question is, for now, a $500 question.
