# NVDA Decision Card — as_of 2026-09-05 (LIGHT REFRESH)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-09-05
**batch** memory_ai_refresh_2026-09-05 · **status** DECISION_DRAFT · **completeness** ~65%
**refresh_of** `companies/nvda/2026-07-10` · **context_label** `exceptional_bottleneck_price_at_line_owner_earnings_bridge_unverified`

> as_of is Saturday 2026-09-05; the last trading day is Friday 2026-09-04, so **as_of_price is the
> 2026-09-04 close**. Yahoo and stockanalysis cross-check to 0.00% on price for all five names in this batch.

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **230.36** (2026-09-04 close; 2 sources, delta 0.00%) |
| market cap | **~$5.589T** (24,264M diluted x 230.36) |
| vs prior card ($210.96, 2026-07-10) | **+9.2%** |
| distance from 52-week high $236.54 | **−2.6%** |
| business_verdict | **exceptional** |
| **new_money_verdict** | **WATCH (0%)** |
| existing_position_verdict | **HOLD** |
| suggested initial / max size | **0% / 0%** |
| **buy_below** | **a BAND: $148.30 – $222.44** (prior card: $181) |
| binding_constraint | **PRICE (above the band) + OWNER-EARNINGS QUALITY (bridge unverified)** |

## Six-module signals (net +3)

| Module | Role | Signal | vs 07-10 | Confidence | One line |
|---|---|---:|---:|---|---|
| M1 Evidence Spine | confidence | **+1** | +2 → +1 | med | 8-K folded in, but no cash-flow statement and no 10-Q → cannot close the OE bridge |
| M2 Theme / Mechanism | context+conviction | **+2** | = | high | Revenue $96.221B (+106%), DC $89.0B (+117%) ≈92%, Q3 guided ~$108.0B |
| M3 Profit Pool / Durability | conviction | **+2** | = | med | 75.0% GM held; ~$26.0B returned in Q2; ~$99.0B authorisation left |
| M4 Financial Reality | conviction/warning | **0** | **+2 → 0** | low | **The changed leg.** OCF $24,077M = 40% of GAAP NI $59,688M; FCF 36%; inventory $31,575M |
| M5 Inversion / Trap | risk | **−1** | = | med | No structural break; China DC excluded from guide = uncounted optionality; GM guided 75.0% → 74.0% |
| M6 Price / Position | price+output | **−1** | = | med | Base 5y IRR **+7.25%**, just under the 8% hurdle; forward multiple compressed 28x → 19.10x |

## The finding that matters

The prior card rested on a clean bridge: **capex-light, FCF = owner earnings ~$182B**. Q2 FY27 breaks it.

- GAAP net income **$59,688M** but operating cash flow only **$24,077M** (40%) and FCF **$21,341M** (36%).
- **GAAP EPS $2.46 EXCEEDS non-GAAP $2.22** — backwards for this company. Most plausibly non-cash
  mark-to-market gains on the **$42,783M** equity-securities book.

Both point the same way: reported GAAP earnings currently overstate cash owner earnings. **Neither can be
resolved from the 8-K.** M4 drops from +2 to 0 on *unverified*, not on proven deterioration.

## Price band

| Basis | OE start | 8%-neutral entry |
|---|---:|---:|
| Accounting OE (Q2 annualised ~$215.5B; Q3 guide implies ~$241B) | $225B | **$222.44** |
| Cash-haircut OE (toward demonstrated FCF ~$85B annualised) | $150B | **$148.30** |

**230.36 is above the top of the band either way** — but the distance closed sharply, from −14% below the
old $181 line to +3.6% above the $222 line.

## Scenarios (5y, hurdle 8%)

| Scenario | OE start | CAGR | Exit P/OE | y5 per share | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $180B | −8% | 15x | ~$73 | **−20.5%** |
| **Base** | **$225B** | **+12%** | **20x** | **~$327** | **+7.25%** |
| Bull | $235B | +22% | 24x | ~$628 | **+22.2%** |
| *Base, cash-haircut* | *$150B* | *+12%* | *20x* | *~$218* | ***−1.1%*** |

## WATCH → STARTER trigger (sequenced — order matters)

**STEP 1.** The Q2 FY27 **10-Q** closes the OE bridge: operating cash flow converges toward non-GAAP net
income, and the GAAP-over-non-GAAP inversion is confirmed as investment gains rather than operating.
**STEP 2.** Only then does ~$222 become a live entry, and a pullback into it opens a 3–5% STARTER.

Skipping step 1 means sizing on an earnings number the cash flow statement does not yet support.

## Kill criteria

K1 revenue materially misses the ~$108B Q3 guide, or DC declines sequentially, or GM < 65% ·
K2 large-scale custom-silicon migration structurally erodes DC share (**only escalation to veto**) ·
K3 large inventory-commitment write-down ($4.5B H20 precedent; inventory now $31,575M and rising) ·
K4 price persistently above the band with no evidenced OE upgrade → stay WATCH — **CURRENTLY TRIGGERED** ·
K5 **NEW**: the 10-Q shows the OCF/net-income gap is structural → re-underwrite M3/M4, do not widen the band ·
K6 Huang key-man.

## runner_dissent

The mechanical output (WATCH) matches July, but **the reason inverted** and this is the most interesting
name in the batch. In July the stock was expensive against a clean earnings base. Today it is roughly **at
a fair price against an earnings base I cannot yet verify.** Those are very different situations, and the
second resolves on a single dated document. If the 10-Q closes the bridge, NVDA is the first STARTER
candidate this book has had in this complex — and note the forward multiple **compressed from ~28x to
~19.10x while the price rose 9.2%**, because earnings outran price. I am deliberately not pre-crediting that.
