# ABT Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$95.40**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$95.40** | YAHOO-ABT-PRICE (repo independent re-fetch) / ABT-SA-STATS (2 independent sources, exact match) |
| Shares outstanding | **1,741.8M** | MACROTRENDS-ABT-SHARES / ABT-SA-STATS |
| Market cap | **~$166.17B** | derived: 1,741.8M x $95.40 — exact match to ABT-SA-STATS |
| Net debt (Q1 2026, post-Exact-Sciences, most current) | **~$27.24B** | derived: debt $34.05B - cash $6.80B |
| Enterprise value | **~$193.41B** | derived |
| 52-wk range | **$82.56 - $134.65** (Yahoo close-basis) | YAHOO-ABT-PRICE; stockanalysis.com shows $81.97-$137.49 (likely intraday basis) |
| Position in range | **-29.2% off high, +15.6% above low** — lower-middle of range | derived |

**Low/high-hug check**: Price sits meaningfully below its 52-week high and moderately above its low — comfortably outside the 3% hug band on both ends, so this is not a hug edge case. The larger question (as with the GEHC exemplar) is whether the -29.2% drawdown from the high is JUSTIFIED by fundamentals or reflects an overreaction. **Read: PARTIALLY JUSTIFIED, PARTIALLY OPPORTUNITY.** The Q1 2026 GAAP EPS decline (-18.7% net income) is real but is substantially a mechanical consequence of financing a large, debt-funded acquisition (Exact Sciences) closed 2026-03-23 — not a core-business deterioration. Adjusted EPS continued growing (+5.5-6% Q1 2026), the core Medical Devices franchise grew +8.5% comparable, and Diagnostics' comparable growth actually INFLECTED POSITIVE (+1.8%) after a weak FY2025. This is a meaningfully different pattern than GEHC's multi-segment organic deterioration — the price decline here looks more like "market digesting a large leveraging acquisition + some genuine near-term EPS dilution" than "broad-based fundamental decay." This dossier independently re-verified the $95.40 price against 2 sources — not a stale or mis-keyed value.

---

## Why GAAP Multiples Require Care Here (Different Distortion Than Either GEV or GEHC Exemplars)

Unlike GEV (one-off-inflated GAAP earnings) or GEHC (reasonably clean GAAP-vs-adjusted correspondence), Abbott's GAAP figures are distorted in BOTH directions across recent periods: **FY2024's GAAP EPS ($7.64) was inflated by a one-off tax benefit** (not a clean comp), while **Q1 2026's GAAP EPS ($0.61, down from $0.76) is DEPRESSED by real-but-largely-transitional Exact Sciences financing/integration costs**. Neither the FY2024-vs-FY2025 GAAP comparison NOR the naive Q1 2025-vs-Q1 2026 GAAP comparison is a clean read. **Adjusted diluted EPS is the more decision-relevant metric this run**: FY2023 (implied ~$4.68 based on trailing multiple back-solve, not directly disclosed) -> FY2024 (not separately disclosed as "adjusted" in sources reviewed, OPEN) -> FY2025 $5.15 (+10% YoY, a clean, disclosed adjusted figure) -> Q1 2026 $1.15 (+5.5-6% YoY, also clean). This trajectory shows continued adjusted earnings growth throughout, even as GAAP figures swing on one-off items and acquisition financing costs.

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (GAAP) | **26.72x** | Elevated in absolute terms, and this run's own back-check (price/FY2025 GAAP EPS $3.72 = 25.65x) is reasonably close, confirming the screener figure is roughly TTM-consistent, not distorted by a stale EPS base |
| Forward P/E (FY2026E, adj EPS guide midpoint $5.48) | **17.04x** (screener) / **17.4x** (this run's derived check) | Reasonably consistent cross-check — good coherence |
| TTM revenue | ~$45.13B (Q1 2026 TTM basis per stockanalysis) | Growing |

---

## Clean Forward Multiple Analysis

**FY2025 operating income (stockanalysis basis)**: ~$8.05B at ~18.17% op margin. D&A is NOT separately disclosed in the official-PR sources reviewed this run (same limitation as GEHC's O2) — estimated at ~4.5% of revenue (a general diversified-healthcare-company approximation, NOT ABT-confirmed) giving **est. adj EBITDA ~$10.05B**.

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2025 adj EBITDA (est.) | $193.41B / $10.05B | **~19.2x** |
| Current EV / FY2026E adj EBITDA (est., guide midpoint growth) | ~$193.41B / ~$11.24B | **~17.2x** |
| Current P/E / FY2026E adj EPS (guide midpoint $5.48) | $95.40 / $5.48 | **~17.4x** |

**Peer/context anchor**: This dossier did not independently fetch a clean single-peer EV/EBITDA comparison this run (unlike the GEHC exemplar's Siemens Healthineers anchor) — Abbott's closest direct peers span multiple sub-industries (Medtronic/Stryker/Boston Scientific for Medical Devices, Danaher/Thermo Fisher for Diagnostics, none of which is a clean single-company match for Abbott's four-pillar diversified structure). **Flagged as an OPEN item for the batch**: once MDT, SYK, BSX, and other names in this same S&P 500 medical batch are completed, a cross-dossier peer-multiple comparison table should be built to properly benchmark Abbott's ~19.2x EV/EBITDA against its true device/diagnostics peer set. Directionally, ~19-20x EV/EBITDA is a PREMIUM multiple for the broader med-tech/diversified-healthcare universe (contrast with GEHC's ~9.7x), consistent with Abbott's generally higher perceived quality (Dividend King status, diversified 4-segment structure, CGM franchise leadership) — but this also means Abbott offers LESS of a "statistically cheap" argument than GEHC did, and more of the investment case rests on continued execution (Exact Sciences integration, NEC containment, China stabilization) rather than multiple re-rating from a depressed starting point.

**Conclusion**: Abbott is NOT statistically cheap on an absolute or (rough, unreconciled) peer-relative basis, despite sitting well off its 52-week high. The stock's discount to its own high partly reflects a genuine, disclosed EPS/leverage cost from the Exact Sciences deal (a real, quantifiable near-term drag) and partly reflects normal market digestion of a large acquisition — this is closer to "a good business paying a real, known short-term cost for an unproven long-term bet, at a still-full valuation" than either GEV's "exceptional business, wrong price" or GEHC's "ambiguous business, roughly fair price" patterns.

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the GEHC/GEV exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: Exact Sciences Thesis Fails + NEC Litigation Escalates + China Proves Structural

| Item | Assumption |
|---|---|
| Revenue CAGR | +2.0%/yr (Exact Sciences distribution-leverage upside fails to materialize; Nutrition keeps declining; China Diagnostics stays weak) |
| Exit adj EBITDA margin (Yr5) | 20.0% (modest expansion still occurs from Medical Devices mix-shift, but muted by NEC reserve charges and integration costs) |
| Exit multiple | 15.0x (de-rates from current ~19.2x, reflecting "big bet didn't pay off" re-rating, though still a premium multiple vs a true distressed name) |
| Net debt Yr5 | $26.0B (stated $3B/yr paydown plan under-delivers; NEC settlement/reserve costs consume cash that would otherwise delever) |
| **3-yr IRR** | **-12.7%** |
| **5-yr IRR** | **-4.2%** |

### Base Case: FY2026 Guidance Roughly Achieved, Exact Sciences Integration Proceeds as Planned (Not Yet Fully Proven), China/Nutrition Stabilize

| Item | Assumption |
|---|---|
| Revenue CAGR | +6.5%/yr (in line with the low end of FY2026 guided comparable growth 6.5-7.5%) |
| Exit adj EBITDA margin (Yr5) | 22.5% (steady expansion from current ~18-19% operating-margin-equivalent level as Exact Sciences integration synergies + Medical Devices mix continue) |
| Exit multiple | 17.8x (holds near-current-to-modestly-below-current level — growth thesis intact but not yet re-rated further pending proof points) |
| Net debt Yr5 | $16.0B (stated debt-paydown plan executes close to schedule, gliding down from $27.2B) |
| **3-yr IRR** | **+2.4%** |
| **5-yr IRR** | **+8.5%** (marginally clears the 8% hurdle) |

### Bull Case: Exact Sciences Distribution-Leverage Thesis Proves Out, NEC Resolves Favorably, CGM Defends Share, China Re-Accelerates

| Item | Assumption |
|---|---|
| Revenue CAGR | +9.0%/yr (genuine ex-US Cologuard/Cancerguard acceleration; CGM successfully defends vs Dexcom; China Core Lab re-accelerates) |
| Exit adj EBITDA margin (Yr5) | 24.5% (margin expansion past current levels, proven multi-franchise execution) |
| Exit multiple | 20.0x (re-rates modestly above current level, reflecting de-risked, proven execution across all four segments) |
| Net debt Yr5 | $10.0B (aggressive deleveraging beyond the stated plan, strong FCF generation) |
| **3-yr IRR** | **+12.9%** |
| **5-yr IRR** | **+16.3%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | -12.7% | -4.2% | FAIL |
| Base | +2.4% | +8.5% | FAIL (3yr) / PASS, marginally (5yr) |
| Bull | +12.9% | +16.3% | PASS (both horizons) |

**Read**: This is a MORE FAVORABLE shape than the GEHC exemplar (where the base case failed at BOTH horizons and was essentially flat even at 5yr). Here, the base case clears the 8% hurdle at 5 years, albeit only marginally (+8.5%, a thin cushion, not a deep margin of safety), while still failing at 3 years — meaning the investment case requires PATIENCE (a 5-year, not 3-year, holding horizon) even in the base case, and still depends on several things resolving constructively (Exact Sciences integration succeeding at least partially, NEC litigation not escalating materially, China/Nutrition stabilizing) rather than reversing. The bear case is a real, meaningful downside (though less severe than GEHC's bear case, reflecting ABT's more diversified and higher-quality underlying franchise mix). **The current price offers a thin, not absent, margin of safety in the base case at the 5-year horizon specifically — a more constructive setup than GEHC's, but still short of a clear "cheap, buy with confidence" signal.**

---

## Buy-Below Analysis

| Target | Target IRR | Approx price | vs $95.40 | Rationale |
|---|---|---|---|---|
| No-chase (above this, base case 5yr IRR turns negative) | — | **~$105-108** | +10-13% | Base case cushion erodes quickly above current levels given the already-full ~19x starting multiple |
| **STARTER entry (test position)** | Base case clears 8% hurdle at 5yr with a real (not marginal) cushion | **~$82-86** | -10% to -14% (near/at 52wk low $82.56) | At/near the 52-week low, the base-case 5yr IRR cushion would widen meaningfully (from the current thin +8.5% toward a more comfortable +13-15% range), while still not requiring the bull-case catalysts to already be proven |
| **CORE entry (real margin of safety)** | Base case clears hurdle with genuine cushion at BOTH 3yr and 5yr horizons | **~$70-75** | -22% to -27% | Would represent a further ~25% drawdown from here — roughly comparable in scale to a 2026-full-year guidance miss or a materially adverse NEC litigation development |
| Deep value / max conviction | 15%+ even in a soft-bear scenario | **~$60** | -37% | Would imply the market is pricing in a genuinely severe outcome (Exact Sciences largely written off + NEC crisis) — a significant dislocation from current fundamentals |

**Binding constraint on price**: The current price offers a THIN margin of safety in the base case (5yr IRR clears the hurdle by only ~0.5 percentage points) and NO margin of safety at the 3-year horizon. This is a "reasonably good business, still-full valuation, real but not yet resolved execution risk (Exact Sciences)" setup — meaningfully more constructive than GEHC's "roughly fair, no cushion at all" setup, but still short of a clear STARTER signal at the current price. **This is closer to "good business, fair-to-slightly-full price, patience required" than either GEV's "exceptional business, price kills it" or GEHC's "ambiguous business, fair price, unresolved questions" patterns** — Abbott's business quality is less ambiguous than GEHC's (Medical Devices/CGM is a genuinely strong, clearly-articulated moat), but the price does not yet offer a clear discount to compensate for the real, large, and recent (unproven) Exact Sciences leverage bet.
