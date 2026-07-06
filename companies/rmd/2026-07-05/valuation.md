# RMD Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$209.63**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$209.63** | STOCKANALYSIS-RMD-STATS / WEBSEARCH-YAHOO-RMD-PRICE (2 independent sources, exact match) |
| Shares outstanding | **144.24M** | STOCKANALYSIS-RMD-STATS |
| Market cap | **~$30.24B** | derived: 144.24M × $209.63 |
| Net cash (Q3 FY2026, most current) | **~$0.82B NET CASH** (opposite sign from a leveraged company) | derived: cash $1.66B − debt $843.17M |
| Enterprise value | **~$29.42B** (below market cap, since net cash) | derived |
| 52-wk range | **$180.27 – $293.81** | STOCKANALYSIS-RMD-STATS |
| Position in range | **−28.7% off high, +16.3% above low** — recovering from a deep drawdown | derived |

**Low-hug check (inverse of the GEV/MSFT high-hug tripwire)**: Price sits well below its 52-week high but is NOT at the low either (comfortably outside the 3% hug band on both ends). Is the −28.7%-off-high positioning justified by genuine fundamentals, or a mispriced overreaction? **Evidence points toward OVERREACTION, not justified deterioration** — unlike GEHC (where the equivalent low-range positioning tracked a real, multi-data-point deterioration), RMD's fundamentals through Q3 FY2026 show margin EXPANSION, durable double-digit revenue growth, and a strengthening balance sheet (financial_quality.md) — the SAME period over which the stock fell 33% peak-to-trough. The decline is attributable to GLP-1 narrative fear, a modest (~1.4%) revenue miss vs. consensus, and compound noise from a CFO transition + M&A announcement landing in the same earnings release — not to any evidenced fundamental breakdown. This dossier independently re-verified $209.63 against 2 sources, both dated to the same 2026-07-02 close (up 4.24% that day on a Goldman Sachs APAC Conviction List addition) — not a stale or mis-keyed value.

---

## Why Trailing Multiples Are Trustworthy Here

Trailing P/E is internally consistent: TTM diluted EPS $10.37 × trailing P/E 20.21x = $209.58, matching the actual price $209.63 almost exactly [facts.md E49-E50] — confirming screener data coherence, similar to the GEHC exemplar's equivalent sanity check.

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (TTM) | **20.21x** | Meaningfully richer than GEHC's 15.72x — reflects RMD's structurally higher margins and net-cash balance sheet, but is NOT a "statistically cheap" multiple in isolation |
| TTM revenue | $5.538B (+~7.6%) | |
| TTM net income | $1.520B | |
| TTM diluted EPS | $10.37 | |

---

## Clean Forward Multiple Analysis

**FY2025 operating income**: $5,146.3M × 32.75% = **$1,685M**. D&A is NOT separately disclosed in any source reviewed this run (OPEN item, consistent with GEHC's equivalent O2 gap) — estimated at ~3.5% of revenue (same convention used in the GEHC dossier, NOT RMD-confirmed) giving **est. FY2025 EBITDA ~$1.866B** (36.2% margin).

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2025 est. EBITDA | $29.42B / $1.866B | **~15.8x** |
| Current EV / TTM est. EBITDA (using TTM revenue $5.538B × similar margin) | ~$29.42B / ~$2.01B | **~14.6x** |
| Current P/E (TTM) | $209.63 / $10.37 | **20.21x** |

**RMD vs. the GEHC comparison point**: RMD trades at roughly a **60-65% PREMIUM** to GEHC's ~9.7x EV/EBITDA (and an even larger premium to the Siemens Healthineers peer anchor of ~7.9x used in that dossier). This is NOT an apples-to-apples comp (different sub-sectors of med-tech — imaging capital equipment vs. respiratory/sleep devices — with different growth/margin/moat profiles), but it establishes that **RMD is priced as a premium, high-quality compounder, not as a distressed or statistically cheap name** — consistent with the fundamentally stronger financial_quality.md and moat_map.md findings versus the GEHC exemplar. The valuation question for RMD is therefore NOT "is this cheap regardless of risk" but "does this premium multiple appropriately price the GLP-1 uncertainty."

**Conclusion**: RMD is not statistically cheap on an absolute or GEHC-relative EV/EBITDA basis, despite trading 28.7% below its 52-week high. The multiple already reflects a business quality premium; whether it ALSO appropriately reflects the GLP-1 risk discount the market has been applying (33% peak-to-trough decline) is the central question the scenario model below addresses.

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the GEHC/GEV/MSFT exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: GLP-1 New-Patient Funnel Shrinks + Multiple De-Rates on Growth Scare

| Item | Assumption |
|---|---|
| Revenue CAGR | **−2%/yr** (GLP-1-driven funnel shrinkage materializes per inversion_map.md Kill Path 1 — device/mask volume growth reverses) |
| Exit EBITDA margin (Yr5) | 28% (compression from ~36% as fixed costs deleverage on a shrinking revenue base) |
| Exit multiple | 11.0x (de-rates sharply — a "growth story broken" repricing, though still above GEHC's exit-bear multiple of 8.0x, reflecting RMD's stronger starting balance sheet/moat even in a bad scenario) |
| Net cash Yr5 | ~$0 (depleted by continued buybacks against a weakening business) |
| **3-yr IRR** | **−15.1%** |
| **5-yr IRR** | **−12.7%** |

### Base Case: GLP-1 Nets Roughly Neutral, Growth Moderates to High-Single-Digit, Multiple Holds

| Item | Assumption |
|---|---|
| Revenue CAGR | +7%/yr (moderation from the current +9-11% pace; diagnosis-funnel expansion per company data roughly offsets any funnel-narrowing effect; category growth + international expansion continue) |
| Exit EBITDA margin (Yr5) | 34% (holds near current ~36% level, modest normalization) |
| Exit multiple | 15.8x (HOLDS CONSTANT at entry level — no re-rate assumed in either direction, consistent with the disciplined exemplar convention) |
| Net cash Yr5 | ~$3.2B (continued FCF generation net of buybacks/dividends/bolt-on M&A) |
| **3-yr IRR** | **+6.0%** |
| **5-yr IRR** | **+7.9%** |

### Bull Case: GLP-1 Proves a Genuine Tailwind (Per CEO Framing), AI Layer Monetizes, Re-Rate

| Item | Assumption |
|---|---|
| Revenue CAGR | +11%/yr (GLP-1 "demand gen" thesis materializes per CEO Farrell's framing and the company's own resupply/adherence data; Smart Comfort/AirView AI layer proves monetizable via improved mix/ASP) |
| Exit EBITDA margin (Yr5) | 36% (further expansion past current levels) |
| Exit multiple | 20.0x (re-rates up, reflecting confirmed AI differentiation + durable double-digit growth + net-cash optionality) |
| Net cash Yr5 | ~$4.5B |
| **3-yr IRR** | **+18.4%** |
| **5-yr IRR** | **+18.4%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −15.1% | −12.7% | FAIL |
| Base | +6.0% | +7.9% | **FAIL (narrowly, both horizons)** |
| Bull | +18.4% | +18.4% | PASS (both horizons) |

**Read**: This is a materially DIFFERENT shape than the GEHC exemplar (base case ~flat/slightly negative) and closer to, but still distinct from, a genuine "base case clears the hurdle" setup. RMD's base case is POSITIVE at both horizons and comes CLOSE to the 8% hurdle (particularly at 5yr: +7.9%, just 10bps under the bar) — meaning a small, plausible improvement in any single input (slightly higher sustained growth, a modest multiple re-rate, or simply the net-cash build compounding a bit faster) would tip the base case over the line. **This is the closest of any dossier reviewed this run to a genuine "coin-flip on the base case" setup** — the investment decision hinges on whether the bear case (GLP-1 funnel genuinely shrinks) is a low-probability tail risk (in which case the probability-weighted expected IRR clears 8%) or a real, material-probability risk (in which case it does not).

---

## Buy-Below Analysis

| Target | Target IRR (5yr base case) | Approx price | vs $209.63 | Rationale |
|---|---|---|---|---|
| No-chase (above this, base case IRR would fall meaningfully below hurdle) | — | **~$225–230** | +7% to +10% | Base case already offers minimal cushion at current price; do not average up without a fundamentals upgrade |
| Base case JUST clears 8% hurdle (zero cushion) | ~8% | **~$209** | ~flat (essentially current price) | Base case IRR crosses the 8% line almost exactly at today's price — this is the single most decision-relevant number in this dossier |
| **STARTER entry (modest real cushion)** | ~10% | **~$190** | **−9.4%** | A ~9-10% pullback restores a genuine, if modest, margin of safety in the base case without requiring the bull-case catalysts to already be proven |
| **CORE entry (real margin of safety)** | ~12% | **~$174–178** | **−15% to −17%** | Requires the base case (not bull) to clear the hurdle with genuine cushion — would represent a further meaningful drawdown from here, roughly back toward the 2026 mid-year trading range |
| Deep value / max conviction | 15%+ even if bear-adjacent inputs partially materialize | **~$155–160** | −24% to −26% | Near the actual 2026 trading trough — would require the market to be pricing in something close to the bear case already |

**Binding constraint on price**: Unlike GEHC (base case clearly fails the hurdle at the current price, decision hinges on unproven bull-case catalysts) or a genuinely cheap setup (base case clears with real cushion today), **RMD sits almost exactly AT the base-case break-even line for the 8% hurdle** — the current price offers essentially zero, not negative, but also not meaningfully positive, margin of safety in the base case. This is a genuine "close call" that depends heavily on (a) how much probability weight one assigns to the bear case (GLP-1 funnel genuinely shrinking) vs. treating it as a well-evidenced-against-but-not-fully-refuted tail risk, and (b) whether one wants ANY cushion before committing capital, even to an otherwise well-run, financially strong business. A modest pullback (~9-10%, to the ~$190 area) would meaningfully improve the risk/reward without requiring heroic assumptions.
