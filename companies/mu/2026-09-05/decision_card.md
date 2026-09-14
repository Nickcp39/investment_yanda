# MU Decision Card — as_of 2026-09-05 (RE-PRICE ONLY)

**pipeline_version** lean-6module-v1.1 · **weights_version** none · **run_date** 2026-09-05
**batch** memory_ai_refresh_2026-09-05 · **status** DECISION_DRAFT · **completeness** ~60%
**refresh_of** `companies/mu/2026-07-10` · **context_label** `cyclical_inflection_at_cycle_peak_no_margin_of_safety`

> as_of is Saturday 2026-09-05; the last trading day is Friday 2026-09-04, so **as_of_price is the
> 2026-09-04 close**. Yahoo and stockanalysis cross-check to 0.00% on price for all five names in this batch.

## Locked conclusion

| Field | Value |
|---|---|
| as_of price | **1016.59** (2026-09-04 close; 2 sources, delta 0.00%) |
| market cap | **~$1.149T** (1,130M shares) · EV $1.12T |
| vs prior card ($979.30, 2026-07-10) | **+3.8%** |
| distance from 52-week high $1,255.00 | **−19.0%** |
| business_verdict | **exceptional** (unchanged) |
| **new_money_verdict** | **WATCH (0%)** |
| existing_position_verdict | **HOLD** |
| suggested initial / max size | **0% / 12%** (cyclical → capped below Core) |
| **buy_below** | **$650 — UNCHANGED, deliberately** |
| binding_constraint | **PRICE vs normalized cycle earnings. No new information since 2026-07-10.** |

> **This is a RE-PRICE ONLY.** Latest reported quarter is still Q3 FY2026 (2026-06-24). **Q4 FY2026 lands
> 2026-09-30**, after this as_of. The T6 guidance-recency warning fires at 73 days on this dossier and
> **that warning is correct, not a defect** — it is the pipeline saying "this name has no fresh evidence".

## Six-module signals (net 0)

| Module | Role | Signal | Confidence | One line |
|---|---|---:|---|---|
| M1 Evidence Spine | confidence | **0** | high | No new company evidence. Everything carried from `../2026-07-10/` |
| M2 Theme / Mechanism | context+conviction | **+2** | high | Corroborated externally (SNDK Q4 blowout, STX FQ4 +48.5% YoY) — but read-across, not Micron's numbers |
| M3 Profit Pool / Durability | conviction | **0** | med | HBM genuinely high-barrier; commodity DRAM majority is not. 16 SCAs = real but partial offset |
| M4 Financial Reality | conviction | **+2** | high | Q3 FY26 carried: rev $41.46B, non-GAAP GM 84.9%, EPS $25.11, adj FCF $18.3B. Not disconfirmed — just not updated |
| M5 Inversion / Trap | risk | **−2** | high | **The only leg that moved on evidence — and it moved down.** See below |
| M6 Price / Position | price+output | **−2** | high | Moved the wrong way: 2.31x base fair (was 2.23x), 1.07x bull fair (was 1.03x) |

## Why M5 worsened: the supply response is no longer a forecast

In July it was anticipated. It is now **board-approved and financed**:

- **SK Hynix approved $38B** of new memory fabs on 2026-08-07 — and its stock **fell 5% on its own
  announcement**, which is the market pricing the glut it implies.
- **Samsung + SK Hynix ~800 trillion won (~$518B)** to new Korean fabs, plus ~81 trillion won for packaging.
- **Micron's own FY2027 capex guided above $10B every quarter** (FY2026 tracking ~$27B).

Meanwhile TrendForce has conventional DRAM contract-price momentum decelerating
**+90–95% QoQ (1Q26) → +58–63% (2Q26) → +13–18% (3Q26F) → +3–8% (4Q26F)**.

**Capacity being funded into decelerating price momentum is the textbook late-cycle configuration.**

## The price moved the wrong way against the carried band

| Scenario | Normalized EPS | Exit P/E | Fair | 07-10 price/fair | **09-05 price/fair** |
|---|---:|---:|---:|---:|---:|
| Bear | $11 | 15x | $165 | — | 6.16x |
| **Base** | **$22** | **20x** | **$440** | 2.23x | **2.31x** |
| Bull | $38 | 25x | $950 | 1.03x | **1.07x** |

In July the stock sat roughly **at** the honest bull case. It is now **above** it.

## The forward-multiple trap, and the drawdown calibration

Forward P/E **7.07x**, trailing **22.94x**. Memory prints its lowest multiples on peak EPS — that is what a
top looks like from the inside. Micron's own record: **FY2022 EPS $7.75 → FY2023 EPS −$5.34** (−169%).
At 1016.59 the market is implicitly paying for normalized EPS of roughly **$85 at 12x** — about **11x** the
FY2022 prior-peak EPS.

**Own-history drawdown calibration:** −89.7%, −73.8%, −50.6%, −48.4%, −54.0%. **Median −54.0%.** Current is
**−19.0%** (deepest −39.1% on 2026-07-29, since retraced). By this stock's own history a 19% drawdown has
never marked a cycle low.

## Why buy_below is UNCHANGED at $650

Micron has not reported. There is no company-specific evidence on which to move the line. **Re-rating an
entry price on sector sentiment and peer read-across is exactly the error this pipeline exists to prevent.**
2026-09-30 earns a change — in either direction. Price needs a further **−36.1%** to reach $650.

## Kill criteria

K1 Q4 FY26 (2026-09-30) misses $50.0B / ~86% / $31.00, or guides Q1 FY27 down · K2 non-GAAP GM declines
sequentially (**the first true cycle-turn signal**) · K3 DRAM contract pricing negative QoQ · K4 Korean
capacity lands ahead of demand · K5 SCAs prove renegotiable under price pressure · K6 price above buy-below
with no evidenced upgrade to normalized earnings — **CURRENTLY TRIGGERED**.

## runner_dissent

I want to flag a tension in the carried band rather than quietly fix it. **Normalized base EPS of $22/year
sits against a current quarterly run-rate of $25–31** — it assumes roughly a **93% decline** in earnings
power. That was defensible mid-cycle reversion before HBM and before 16 multi-year SCAs; it may now be too
harsh, and if it is, base fair of $440 is too low and the $650 entry is unreachably strict.

But the evidence that would justify raising it **can only be generated in a down-pricing quarter**, and none
has occurred. So: **flagged, not changed.** If Q4 FY26 on 2026-09-30 comes with a Q1 FY27 guide that holds
margin against decelerating contract prices, that is the first real datapoint for re-basing the band upward.
