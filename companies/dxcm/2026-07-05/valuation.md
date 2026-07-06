# DXCM Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$71.25**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$71.25** | DXCM-SA-STATS — exact match to frozen as_of_price input |
| Shares outstanding | **385.87M** | DXCM-SA-STATS, cross-checked vs SEC 10-Q Q1 2026 balance sheet (385.9M) |
| Market cap | **~$27.49B** | derived: 385.87M x $71.25 — exact match to DXCM-SA-STATS |
| Net cash (FY2025, most current confirmed) | **~$758M (net CASH, not net debt)** | derived: cash $917.7M + short-term securities $1,081.0M − convertible notes $1,240.9M |
| Enterprise value | **~$26.74B** (BELOW market cap, since net cash) | derived |
| 52-wk range | **$54.11 - $89.98** | DXCM-SA-STATS |
| Position in range | **-20.8% off high, +31.7% above low** — mid-to-upper-middle of range | derived |

**Low/high-hug check**: Price sits meaningfully below its 52-week high and well above its low — comfortably outside the 3% hug band on both ends, so this is not a hug edge case. Unlike ABT/GEHC in this batch (both sitting closer to their 52-week lows, reflecting real, disclosed near-term headwinds), DXCM's price position reflects a stock that has ALREADY partially re-rated upward from its 2024-crisis lows and is trading in the healthier middle of its range — consistent with the genuinely positive Q1 2026 operating results and the constructive May 2026 Investor Day reception (facts.md E8, E71). This is NOT a "beaten-down, still-cheap" setup like GEHC's — it is closer to "recovering, and the market has already started paying up for the recovery."

---

## Why GAAP Multiples Require Care Here (a Different Distortion Pattern Than ABT/GEHC)

DexCom's GAAP figures are NOT distorted by one-off tax benefits or M&A financing costs (unlike ABT's FY2024 tax benefit or Q1 2026 Exact-Sciences-financing drag) — DexCom's earnings quality is genuinely clean (financials/financial_quality.md One-Off Registry). The care required here is different: **the trailing P/E (30.47x) and trailing EV/EBITDA (~22.4x, this dossier's own derived estimate) reflect a business in the MIDDLE of a sharp margin-expansion cycle**, meaning trailing multiples understate how much cheaper the stock looks on a forward basis if the expansion continues, but also mean the multiple is unusually sensitive to any deceleration in that expansion (i.e., a growth-and-margin-momentum stock, not a steady-state one).

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (GAAP) | **30.47x** (screener, TTM basis) | This dossier's own back-check using FY2025 GAAP EPS ($2.09): $71.25/$2.09 = 34.1x — somewhat higher than the TTM screener figure, consistent with TTM including the stronger, more-recent Q1 2026 quarter that the FY2025-only denominator doesn't capture |
| Forward P/E | **26.63x** (screener) | Reflects consensus expectation of continued EPS growth into FY2026 |
| Current EV / FY2025 actual EBITDA (this dossier's estimate) | ~$26.74B / ~$1,191.5M | **~22.4x** |
| Current EV / FY2026E adj EBITDA (company guide midpoint) | ~$26.74B / ~$1,627M | **~16.4x** — a meaningfully lower FORWARD multiple, reflecting the guided margin expansion |

**Peer/context anchor**: DexCom's closest direct peer for this specific comparison is Abbott's Diabetes Care/CGM sub-business (not all of Abbott — see the ABT dossier in this same batch), which does not trade as a standalone security, making a clean single-peer multiple comparison structurally impossible. Medtronic's Diabetes segment (MiniMed/Guardian/Simplera) is a smaller, less CGM-concentrated comparison. **Flagged as an OPEN item for the batch, same pattern as ABT's exemplar note**: once this batch's cross-dossier comparison table is built, DexCom's ~22.4x trailing / ~16.4x forward EV/EBITDA should be benchmarked against Abbott's implied Medical Devices multiple and Medtronic's Diabetes-segment-adjacent multiple specifically, not against either company's consolidated multiple.

**Conclusion**: DexCom trades at a genuine premium (trailing ~22.4x EV/EBITDA is richer than either ABT's ~19.2x or GEHC's ~9.7x in this same batch) — this is NOT a statistically cheap stock on an absolute basis. The premium reflects real, currently-materializing operating momentum (margin expansion accelerating, growth accelerating, a credible long-range plan just laid out), but it also means the investment case depends more heavily on that momentum CONTINUING (or the market's willingness to keep paying a premium for it) than on a valuation re-rating from a depressed starting point — the opposite return driver than GEHC's setup in this batch.

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the ABT/GEHC exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: Growth Stalls (GLP-1 Substitution + Abbott Global Squeeze) + a Third Distribution-Channel Incident + Multiple De-Rates Sharply

| Item | Assumption |
|---|---|
| Revenue CAGR | +4.0%/yr (Yr1-3), +3.0%/yr (Yr3-5) — GLP-1 substitution bites at the Stelo/non-insulin-T2D margin (facts.md E62, inversion_map.md Kill Path 2); Abbott's larger global distribution scale squeezes International expansion (Kill Path 1); a third channel-control incident (Kill Path 3) further dents growth |
| Exit adj EBITDA margin | 26.0% (Yr3) / 27.0% (Yr5) — well short of the FY2026 guide (31-31.5%), let alone the 2030 target (36-37%) |
| Exit multiple | 13.0x (Yr3) / 12.0x (Yr5) — sharp de-rate from today's ~22.4x, reflecting a "growth/margin-momentum thesis broken" repricing |
| Net cash terminal | $1.2B (Yr3) / $1.8B (Yr5) — weaker FCF generation still funds the $1B buyback but builds cash more slowly |
| **3-yr IRR** | **-11.7%** |
| **5-yr IRR** | **-6.8%** |

### Base Case: FY2026 Guidance Roughly Achieved, Growth/Margin Moderate Toward (Not Yet At) the 2030 Long-Range Plan, Multiple Normalizes From Today's Rich Level

| Item | Assumption |
|---|---|
| Revenue CAGR | +11.0%/yr (Yr1-3, tracking the FY2026 guide's 11-13% range), +10.0%/yr (Yr3-5, moderating toward but not yet at the 2030 ">10%" long-range target's lower bound) |
| Exit adj EBITDA margin | 28.0% (Yr3) / 31.0% (Yr5) — expanding meaningfully but tracking toward, not reaching, the 2030 36-37% target |
| Exit multiple | 18.0x (Yr3) / 16.0x (Yr5) — compresses from today's ~22.4x toward a more sustainable premium-growth-medtech level as the "post-crisis-recovery + fresh-Investor-Day" special-situation premium normalizes, even as the underlying business continues performing well |
| Net cash terminal | $1.5B (Yr3) / $2.5B (Yr5) |
| **3-yr IRR** | **+7.0%** |
| **5-yr IRR** | **+7.6%** (marginally BELOW the 8% hurdle) |

### Bull Case: 2030 Investor Day Targets Track Ahead of Schedule, GLP-1 Proves Genuinely Complementary, No Further Channel Incidents

| Item | Assumption |
|---|---|
| Revenue CAGR | +13.0%/yr (Yr1-3) / +12.0%/yr (Yr3-5) — near the upper end of what the Investor Day implied; G8 launches on/ahead of schedule, Stelo scales meaningfully |
| Exit adj EBITDA margin | 31.0% (Yr3) / 35.0% (Yr5) — approaching but not fully reaching the 2030 36-37% endpoint |
| Exit multiple | 20.0x (Yr3) / 19.0x (Yr5) — HOLDS near current levels rather than expanding further (deliberately conservative, consistent with the batch's discipline against assuming re-rating beyond an already-rich starting multiple) |
| Net cash terminal | $1.8B (Yr3) / $3.2B (Yr5) — strong FCF funds both the buyback and continued cash buildup |
| **3-yr IRR** | **+16.5%** |
| **5-yr IRR** | **+16.0%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | -11.7% | -6.8% | FAIL |
| Base | +7.0% | +7.6% | **FAIL at both horizons, but only marginally** (within ~1-1.3 percentage points) |
| Bull | +16.5% | +16.0% | PASS (both horizons) |

**Read**: This is a genuinely different, and slightly LESS favorable, shape than the ABT exemplar in this same batch — ABT's base case cleared the 8% hurdle (barely) at 5 years; DXCM's base case falls JUST short at BOTH horizons. The reason is almost entirely the multiple-compression assumption: DexCom's CURRENT price already embeds a rich ~22.4x trailing EV/EBITDA multiple (richer than ABT's ~19.2x or GEHC's ~9.7x), so even a genuinely constructive base case (double-digit growth continuing, real margin expansion toward the long-range plan) does not clear the hurdle unless the multiple simply HOLDS rather than normalizes even partially. **This is the single most important, sensitivity-worth-highlighting fact in this valuation**: if an investor believes DexCom's current premium multiple is durable (not a temporary post-Investor-Day enthusiasm premium), the base case would clear the hurdle comfortably; if the multiple normalizes even modestly toward a more typical premium-medtech level as this model assumes, the base case falls just short. The bear case is meaningfully worse than ABT's in relative-percentage terms (though similar in absolute IRR at 3yr), reflecting DexCom's single-category concentration risk (no segment diversification to cushion a growth/margin disappointment) — a genuinely higher-variance security than the diversified ABT/GEHC comparables in this batch, consistent with its 1.45 beta (vs ABT's 0.61).

---

## Buy-Below Analysis

| Target | Target IRR | Approx price | vs $71.25 | Rationale |
|---|---|---|---|---|
| No-chase (above this, base case 5yr IRR turns negative) | — | **~$103** | +45% | Base-case cushion is already thin at the current price; it would need to rise ~45% before the base case IRR turns negative — a wide gap, but this reflects the CURRENT price already being a genuine base-case-fails setup, not a comfortable one that only fails after a big rally |
| **Current price ($71.25)** | Base case FAILS marginally at both horizons (+7.0%/+7.6%) | — | — | Not yet a clean STARTER signal — the base case does not clear the hurdle, though the miss is narrow (within ~1 percentage point at 5yr) |
| **STARTER entry (test position)** | Base case clears the 8% hurdle with a real, not marginal, cushion | **~$60-65** | -9% to -16% | At this level, base-5yr IRR rises to ~9.6-11.4% (from the current 7.6%) — a genuine, not razor-thin, cushion, without requiring the bull-case Investor-Day-ahead-of-schedule catalysts to already be proven |
| **CORE entry (real margin of safety)** | Base case clears hurdle with a wide cushion at BOTH 3yr and 5yr horizons, closer to the bull case's territory | **~$50-52** | -27% to -30% | Would represent roughly the stock revisiting its 52-week-low-adjacent territory ($54.11) — plausible if a genuine growth/margin disappointment (echoing the 2024 crisis pattern) recurs, not merely a market-wide selloff |
| Deep value / max conviction | 15%+ even in a soft-bear-adjacent scenario | **~$48** | -33% | Would imply the market is pricing in something close to the bear case's growth/margin trajectory already — a significant re-set from current operating momentum |

**Binding constraint on price**: The current price does NOT offer a margin of safety in the base case at either horizon — this is a genuinely thinner setup than ABT's (which cleared the hurdle, if barely, at 5yr) or a name trading at a depressed multiple with a clear discount. DexCom's investment case at $71.25 currently rests on the BULL case materializing (2030 targets tracking ahead of schedule) or on the market's willingness to sustain today's premium multiple rather than let it normalize — a meaningfully more speculative, momentum-dependent setup than either ABT's "thin-but-positive base case" or GEHC's "ambiguous business, fair price" patterns in this same batch. **This is closer to "genuinely improving business, but the market has already priced in a good chunk of the improvement" than either ABT's "good business, real near-term cost, still-full price" or GEHC's "ambiguous business, roughly fair price" setups.**
