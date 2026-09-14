# SNDK Decision Card — as_of 2026-09-05 (REFRESH)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-09-05
**batch** memory_ai_refresh_2026-09-05 · **status** DECISION_DRAFT · **completeness** ~60%
**refresh_of** `companies/sndk/2026-06-22` · **context_label** `cyclical_inflection_company_claims_cycle_repealed_unproven`

> as_of is Saturday 2026-09-05; the last trading day is Friday 2026-09-04, so **as_of_price is the
> 2026-09-04 close**. Yahoo and stockanalysis cross-check to 0.00% on price for all five names in this batch.

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **1740.00** (2026-09-04 close; 2 sources, delta 0.00%) |
| market cap | **~$254.77B** (146.42M shares out) · EV $248.43B |
| vs prior card ($2,288.92, 2026-06-22) | **−24.0%** |
| distance from 52-week high $2,354.39 | **−26.1%** |
| business_verdict | **good** (unchanged — great cycle, fortress balance sheet, durability still cyclical) |
| **new_money_verdict** | **WATCH (0%)** |
| existing_position_verdict | **HOLD** — *softened from TRIM* |
| suggested initial / max size | **0% / 10%** (cyclical → never Core) |
| **buy_below** | **~$769** (prior card: $600) — **RAISED on evidence** |
| binding_constraint | **PRICE vs NORMALIZED earnings + an unfalsifiable 80% GM claim** |

> **Print-quality caveat.** The 2026-09-04 close was the **session high, +11.9% on the day** (prior close
> $1,554.99), on a BofA upgrade, a UBS note and Seagate's FQ4 beat — **no SanDisk disclosure**. The entry
> price being tested is a sentiment print.

## Six-module signals (net +1)

| Module | Role | Signal | Confidence | One line |
|---|---|---:|---|---|
| M1 Evidence Spine | confidence | **+2** | high | Q4 FY26 + FY26 + Investor Day all primary-sourced — best evidence quality in the batch |
| M2 Theme / Mechanism | context+conviction | **+2** | high | Q4 revenue $8.97B (+51% QoQ); ~1/3 volume, ~2/3 price; DC $2,977M (+103% QoQ), FY26 $5,153M (+437%) |
| M3 Profit Pool / Durability | conviction | **0** | low | **The whole case sits here, unresolved** — see below |
| M4 Financial Reality | conviction/warning | **+1** | med | FY26 EPS $73.76, FCF $11,494M, zero LT debt — but **capex $177M on $20,248M revenue (0.9%)** |
| M5 Inversion / Trap | risk | **−2** | high | Record margin + funded supply response + decelerating price momentum, simultaneously |
| M6 Price / Position | price+output | **−2** | high | 1.58x probability-weighted fair; bear-to-bull spread ~10x |

## Why M3 is 0 and not positive — the one table that decides this name

| FY | Revenue | Gross margin | Operating margin | Diluted EPS |
|---|---:|---:|---:|---:|
| FY2023 | $6,086M | 7.07% | −21.28% | **−$14.78** |
| FY2024 | $6,663M | 16.09% | −6.66% | **−$4.63** |
| FY2025 | $7,355M | 30.08% | 6.89% | **−$11.32** |
| FY2026 | $20,248M | **71.47%** | **61.58%** | **+$73.76** |

**Losses in three of the last four fiscal years. Gross margin was 30.08% twelve months ago.** At the
2026-08-13 Investor Day the company guided **~80% non-GAAP gross margin and ~75% operating margin
FY2028–FY2030**. NBM agreements now cover **8 customers, ~50% of FY2027 bits and ~2/3 of FY2028 bits** —
a genuine structural change. But a contract raises the **floor**; nothing yet shows it holds the **ceiling**
once pricing turns. Signal held at 0: not negative (NBM is real), not positive (proof requires a down quarter).

## Scenarios — FY2028 basis, all at 12x

| Scenario | Weight | Revenue | GM | OM | EPS | Fair | vs 1740.00 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bear — commodity reversion | 30% | $25.0B | 30% | 15% | $21.75 | **$261** | −85% |
| Base — NBM raises floor only | 45% | $35.0B | 50% | 35% | $71.05 | **$853** | −51% |
| Bull — Investor Day holds | 25% | $48.7B | 80% | 75% | $212.12 | **$2,545** | +46% |
| **Probability-weighted** | | | | | | **$1,098** | **−37%** |

**Price is 1.58x probability-weighted fair.** Bear-to-bull spread is ~10x on the same company at the same
price — that is a binary bet on whether the NAND cycle has been repealed, not a valuation disagreement.

## capital_cycle lens (one-way; caps only)

`applicable yes · stage late/peak · supply_barrier low-to-med · caution **PEAK**`

SK Hynix approved **$38B** of new fabs on 2026-08-07 and **fell 5% on its own announcement**. Samsung + SK
Hynix committing ~**$518B** to new Korean capacity. TrendForce DRAM contract momentum
**+90–95% → +58–63% → +13–18% → +3–8%** (1Q26 → 4Q26F); NAND +10–15% in 3Q26. Prices still rising, second
derivative turned, capacity financed. **The −26.1% drawdown does not switch this off.**

## WATCH → STARTER trigger — both required, in order

1. **Price into ~$769–900**, and
2. **Durability proof**: at least one quarter of flat-to-down industry NAND pricing in which SanDisk's
   gross margin still holds materially above its historical mid-cycle range.

Condition 2 is the entire thesis and **can only be produced in a down quarter**. Price alone does not open
a STARTER here.

## Kill criteria

K1 GM declines sequentially or misses the 83.0–84.9% Q1 FY27 guide · K2 NAND ASPs negative QoQ (4Q26F
already only +3–8%) · K3 NBM economics weaker than the 50%/67%-of-bits framing, or a customer walks ·
K4 capacity outruns demand (BiCS10, third Kitakami, Korean build-out) · K5 the $15.5B buyback executed
into the peak and the stock halves · K6 AI-capex pause cuts datacenter NAND · K7 **NEW**: FY2027 tracks the
Investor Day model on revenue but **not** on ~80% GM → durable-reset tail falsified, bull weight → 0.

## runner_dissent

Two honest scorekeeping notes **against my own prior card**.

**First**, the June card was right on price (−24%) and **wrong on the business**. It named "gross margin
rolls over" and "NAND ASPs turn negative" as what to watch; **both went the other way** — Q4 GM rose to
84.6% and two-thirds of sequential growth was price. Right direction for the wrong reason is not a win and
I am not recording it as one.

**Second**, my bear case may be too harsh. NBM take-or-pay across two-thirds of FY2028 bits is a real
structural change, and a pure 30%-GM commodity reversion may no longer be the right bear. I kept the 30%
weight anyway, because the alternative is crediting an unproven claim and the asymmetry of being wrong in
*that* direction is worse.
