# GEV Decision Card — as_of 2026-09-05 (REFRESH + MODEL CORRECTION)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-09-05
**batch** memory_ai_refresh_2026-09-05 · **status** DECISION_DRAFT · **completeness** ~70%
**refresh_of** `companies/gev/2026-06-19` · **context_label** `oligopoly_services_annuity_price_trigger_fired_on_a_falsified_anchor`

> as_of is Saturday 2026-09-05; the last trading day is Friday 2026-09-04, so **as_of_price is the
> 2026-09-04 close**. Yahoo and stockanalysis cross-check to 0.00% on price for all five names in this batch.

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **941.95** (2026-09-04 close; 2 sources, delta 0.00%) |
| market cap | **~$250.87B** (266.33M shares) · EV $241.87B |
| vs prior card ($1,109.73, 2026-06-19) | **−15.1%** |
| distance from 52-week high $1,195.94 | **−21.2%** |
| business_verdict | **exceptional** (unchanged — highest business quality in this batch) |
| **new_money_verdict** | **WATCH (0%)** |
| existing_position_verdict | **HOLD** |
| suggested initial / max size | **0% / 7%** |
| **buy_below** | **~$786** — the prior **$950 STARTER line is RETIRED**, not met |
| binding_constraint | **PRICE — but for a different reason than in June** |

> ### The only entry trigger to fire in this batch — and it is not being honoured
> **941.95 is 0.85% BELOW the prior card's $950 STARTER line.** The $950 anchor was derived on 2026-06-19
> data and **Q2 2026 falsified a load-bearing input to it.** The correct action is to fix the anchor, not
> to buy against it.

## Six-module signals (net +3)

| Module | Role | Signal | Confidence | One line |
|---|---|---:|---|---|
| M1 Evidence Spine | confidence | **+1** | med | Q2 release + 10-Q cash-flow discussion primary-sourced; segment detail still thin (~70%) |
| M2 Theme / Mechanism | context+conviction | **+2** | high | **Strongest operating quarter in the batch on orders**: $24.2B, **+88% organic**; backlog $176B |
| M3 Profit Pool / Durability | conviction | **+2** | high | Gas oligopoly + services annuity. **The one business here whose durability is not the open question** |
| M4 Financial Reality | conviction/warning | **0** | high | **The leg that broke** — an accounting-quality issue, not a demand issue. See below |
| M5 Inversion / Trap | risk | **−1** | med | The trap is a cash-flow illusion, not solvency (cash $12.72B vs debt $3.72B) |
| M6 Price / Position | price+output | **−1** | med | On the corrected model, base IRR ≈ **−0.1%/yr**; 8%-hurdle entry ~$786 |

## The valuation correction — the core output of this refresh

**The error.** The 2026-06-19 base case computed 2028 equity value as *2028 EV + ~$18B of projected "net
cash"*, reaching ~$974/share.

**The evidence**, from the 2Q26 10-Q:

> H1-2026 cash from operating activities increased **$9.2B** YoY, driven primarily by an increase in
> **contract liabilities and current deferred income of $11.8B**, primarily due to higher **down payments
> on orders and slot reservation agreements** at Power, and higher down payments at Electrification.

**Why it matters.** That is customer float against **undelivered turbines**. Counting it as shareholder net
cash while also capitalising the future revenue it prepays **double-counts the same economics**.

**Independent arithmetic check.** FY26 revenue guide $45.5–46.5B at the Q2 adjusted EBITDA margin of 11.3%
implies roughly **$5.0–6.0B of adjusted EBITDA**, against an adjusted FCF guide of **$11.5–12.5B** — free
cash flow at about **2.2x EBITDA**, possible only through negative working capital. The headline **4.8% FCF
yield is a float yield**; on underlying earnings, EV $241.87B / $5.0–6.0B adj EBITDA ≈ **44x**. The June
objection at ~49x has **barely improved despite a 15.1% price fall**.

## Corrected scenarios — horizon end-2028 (2.32 years)

| Scenario | 2028 adj EBITDA | Exit EV/EBITDA | Free net cash (prior) | Value/share | IRR from 941.95 |
|---|---:|---:|---:|---:|---:|
| Bear | $6.5B | 25x | $5B ($12B) | ~$632 | **−15.9%/yr** |
| **Base** | **$8.5B** | **28x** | **$9B ($18B)** | **~$939** | **−0.1%/yr** |
| Bull | $10.4B | 32x | $14B ($22B) | ~$1,334 | **+16.0%/yr** |

8%-hurdle entry = $939 / 1.08^2.32 = **$786**. Price is about **20% above it**.

**Note the cross-check:** $786 lands close to the prior card's **$756 CORE** line, which was itself derived
on the 8% hurdle. **The two methods agree once the net-cash error is removed.** It was the looser **$950
STARTER** threshold — not the hurdle math — that was wrong.

## What is genuinely excellent, and must not be lost in the correction

Orders **$24.2B (+88% organic)** · backlog **$176B** · gas equipment backlog + slot reservations
**100 → 116 GW**, targeting **>=125 GW** by year-end · data centre orders **>$5B YTD**, more than double
all of 2025 · output path 20 GW (3Q26) → 24 GW (2028) → 30 GW (2030) · FY26 guidance **raised**.

`capital_cycle`: `applicable partial · stage mid · supply_barrier **high** · caution **NONE**` — unlike the
memory names, supply here **cannot** respond quickly because slots are booked years out.

**This is a valuation-anchor problem, not a business problem.** That distinction is why GEV stays at the top
of the watch list rather than being downgraded.

## WATCH → STARTER trigger

Either **(1) price into ~$786 or below**, or **(2)** adjusted EBITDA margin converging toward the ~20%
required by the 2028 path — **from 11.3% today** — with adjusted FCF sustained **after** contract-liability
growth normalises. Next test **2026-10-21**.

## Kill criteria

K-A gas turbine pricing negative YoY for two quarters · K-B slot cancellations without firm replacement ·
K-C Wind losses >$600M FY2026 with no credible recovery plan · K-D hyperscaler 2027 capex −30% with
Electrification orders −40% · K-E **NEW**: contract liabilities stop growing or reverse while reported FCF
stays in guide — the float is being consumed, not replenished · K-F **NEW**: adjusted EBITDA margin fails to
progress toward the 2028 path (11.3% today vs ~20% required).

## runner_dissent

**This is the call I am least comfortable with, and the discomfort runs bullish.** GEV posted 88% organic
order growth, took gas backlog 100 → 116 GW toward 125 GW, and has the highest business quality here by a
wide margin — and I am **declining a price trigger that mechanically fired**.

Two things could make that wrong. First, my 2028 EBITDA of $8.5B is carried from June and **may be too low**
given backlog growth since. Second, customer prepayments on a multi-year oligopoly backlog are arguably a
**durable structural float** rather than a one-off working-capital swing, and a business permanently prepaid
by its customers deserves some credit for it.

What I am **not** willing to do is buy against an anchor whose net-cash input the 10-Q has just contradicted.
The right sequence is to correct the model and let price come to the corrected number — not to honour a
trigger built on a falsified input. **If Q3 (2026-10-21) shows margin converging on the 2028 path, this
becomes the best STARTER candidate in the book and I would want to revisit immediately.**
