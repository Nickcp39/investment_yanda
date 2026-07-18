# Valuation / Margin Of Safety — NBIS (LIGHT REFRESH, as_of 2026-07-10)

**Type**: LIGHT REFRESH of `../2026-06-18/valuation.md` — re-priced only; FILED financials carried forward unchanged (NBIS Q2 2026 6-K not yet out). Method carried: **EV/forward-sales triangulation + implied-expectations reverse check** — NOT an owner-earnings DCF (owner earnings are negative; FCF stays deeply negative through ≥FY2028).

Source base: market data (Yahoo chart API + websearch, 2 independent, 0.0% delta), financials (SRC-001/002, FILED, carried).

## What moved: PRICE

The canonical **as_of_price = $219.65** is the **last close ≤ 2026-07-10** (Yahoo chart re-fetch $219.65; websearch historical $219.65, +1.60% on the day; passes `verify_freshness.py`). Down **−23.4%** from the 06-18 close of $286.69. Path: peaked $276.17 (06-30), dropped on 07-01 after a Bloomberg "people familiar" report that Meta will sell excess compute via a cloud business (SENTIMENT/lead; the $27B Meta contract is intact), troughed intraday ~$195.19 (07-07), recovered to $219.65 (07-10). Price is now **−26.7% off the 52-week high $299.86** (mid-range, no longer "priced for perfection at the high") and +348% above the 52wk low $49.00.

## Current Setup (repriced @ $219.65)

| Item | 2026-06-18 | **2026-07-10** | claim_id |
|---|---:|---:|---|
| Share price (last close ≤ as_of) | $286.69 | **$219.65** (−23.4%) | C030R |
| Basic shares / diluted wtd-avg | 253.9M / 308.97M | 253.9M / 308.97M (FILED, carried) | C030 |
| Market cap (basic) | ~$72.79B | **~$55.77B** | C030R |
| Market cap (diluted) | ~$88.58B | ~$67.87B | C030R |
| Net cash (carrying) | ~+$0.85B | ~+$0.85B (FILED, carried) | C009 |
| **Enterprise value (basic)** | ~$71.9B | **~$54.92B** | C030R |
| Holder cost basis | ~$190–195 (+~50%) | ~$190–195 (now **+~13%**) | user |

## Multiples (EV ≈ $54.92B basic; was $71.9B)

| Multiple | 2026-06-18 | **2026-07-10** | Note |
|---|---:|---:|---|
| EV/Rev FY26E ($3.44B) | ~21x | **~16x** | |
| EV/ARR current ($1.9B) | ~38x | **~28.9x** | |
| EV/ARR on FY26-exit $7–9B | ~8–10x | **~6.1–7.8x** | now brackets *at/just-below* a mature multiple, no longer above it |
| EV/RPO (Q1'26 $33,585M) | ~2.2× | **~1.64×** | EV now < 2× the entire audited contracted book |

**Implied-expectations read**: at EV ≈ $54.9B, on EV/ARR the market pays ~6.1–7.8× the YE2026 $7–9B exit-ARR target. That is *at or just below* a mature neocloud multiple (CoreWeave ~7.7x fwd, hyperscalers ~9–10x) — i.e. the stock **no longer fully capitalizes the YE26 target as already-achieved-at-a-premium**. The "priced for perfection" flag of 06-18 has eased to "expensive but priced closer to base."

## Scenarios (EV/forward-sales triangulation, horizon ~end-2028 ≈ 2.48yr)

Target (implied) prices are horizon fair-value estimates and **do not change with today's price** — what changed is the **return from a lower entry**.

| Scenario | Implied price (horizon) | Total return from $219.65 | **IRR/yr** | 06-18 IRR/yr (from $286.69) |
|---|---:|---:|---:|---:|
| **Bear** | ~$120–140 | −45% to −36% | **−22% to −17%** | steeper (bear was ~−50%+) |
| **Base** | ~$330–400 | +50% to +82% | **+18% to +27%** | ~6–14% |
| **Bull** | ~$560–600 | +155% to +173% | **+46% to +50%** | ~+95% total |

**The base-case IRR now clears the ~12–15%/yr hurdle** (was below it at $286.69). Bull is very attractive; bear is a real −20%/yr. Skew has shifted from unfavorable toward roughly balanced-to-favorable **on the mechanical DCF-IRR**.

## Margin Of Safety — the disciplined read

| Required return | Buy below | Hold | Trim/No-chase above |
|---|---|---|---|
| ~12–15%/yr (high uncertainty, capital-intensive, controlled co., ~90% 2-customer concentration) | ≈ **<$150–180** (unchanged) | ~$180–260 | priced-for-perfection cleared; kill on criteria |

**At $219.65 the price is ~18% above the top of the buy-below band ($180) and ~32% above the bottom ($150).** The gap narrowed sharply (was −37%/−48% at $286.69) but is **not yet closed**. Two reasons the buy-below is held, not loosened, despite the base IRR clearing the hurdle:
1. **Elevated K-B (concentration) sentiment**: the Meta "sell excess compute" report spotlights the pre-existing ~90% two-customer concentration risk (a top-2 anchor potentially becoming a competing reseller). This argues the *required* MOS went up, not down.
2. **Capital-cycle PEAK-lean caution** (one-directional): neocloud rental is a **low-barrier** segment; a hyperscaler reselling surplus compute is exactly the supply-flooding signal the lens flags. This can only compress the verdict, never lift it.

Plus the completeness cap is unchanged: **active MW still withheld** (Q2'26 6-K not out), so the conversion-proof metric is still unaudited (~70% completeness).

## Conclusion

The −23.4% drop **materially improved the skew** and pulled new-money **much closer to a STARTER entry**, but it did **not reach the buy-below band ($150–180)**. New-money stays **WATCH (0%)**, now "warming." Existing holder **HOLD**. See `refresh_note.md` for old→new and the verdict-flip check.
