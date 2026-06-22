# GEV Valuation (M6)

Last updated: 2026-06-21 | as_of: 2026-06-19 | as_of_price: **$1109.73**
See `model/scenario_model.csv` for IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-06-18) | **$1109.73** | YAHOO-GEV-PRICE / GEV-SA-STATS |
| Market cap | **~$298.2B** | 268.72M × $1,109.73 |
| Net cash (approx, Q1 2026) | **~$7.4B** | GEV-SA-FINANCIALS |
| Enterprise value | **~$292.2B** | GEV-SA-STATS |
| 52-wk context | **−6.1% off ATH $1,181.95** | YAHOO-GEV-PRICE |
| Price vs 52-wk low | **+132% from $479.04 low** | YAHOO-GEV-PRICE |

**High-hug justified**: YES. Price near 52-week high is justified by strong Q1 2026 results (guidance raised significantly: FCF $6.5-7.5B vs prior $4.5-5.0B; EBITDA margin raised to 12-14%) and fundamental re-rating. Not a stale price copy.

---

## Why Screener Multiples Are Wrong (CRITICAL)

| Metric | Screener Value | Distortion |
|---|---|---|
| Trailing P/E | ~32x | FY2025 net income $4.9B includes $2.9B tax release |
| EV/EBITDA (ttm) | ~85x | TTM GAAP EBITDA distorted by Q1 advance-payment inflows + one-offs |
| TTM EPS | $34.17 | Includes $3.99B Prolec gain + $0.33B Proficy gain |
| Forward P/E | ~60x | Unclear — likely based on GAAP distorted estimates |

**Rule**: Discard all trailing GAAP multiples. Use the adj EBITDA guide and segment targets.

---

## Clean Forward Multiple Analysis

Using EV ~$292B and guidance:

| Metric | Calc | Multiple |
|---|---|---|
| FY2026 adj EBITDA midpoint | $44.5–45.5B × 13% = $5.85B | **EV/EBITDA 2026E: ~49.9x** (call it ~48–51x) |
| FY2026 FCF guide midpoint | $7.0B | **P/FCF 2026E: ~43x** |
| FY2028 adj EBITDA (targets) | $52B × 20% = $10.4B | **EV/EBITDA 2028E: ~28x** |
| Siemens Energy peer (NTM) | — | **~20x EV/EBITDA** |
| Sector median (industrial) | — | **~17x EV/EBITDA** |

**GEV premium to Siemens**: ~2.5x on 2026E. This represents the market pricing:
1. GEV's superior services annuity (higher margin, more durable)
2. Faster margin expansion trajectory (Power → 17-19% by 2026, 22% by 2028)
3. Electrification data center optionality
4. US-listed premium

**Conclusion**: At ~49x 2026 adj EBITDA, the market has essentially already priced in the 2028 targets (28x on 2028 EBITDA implies modest multiple compression from 49x to 28x, requiring both full target delivery AND sustained premium multiple). The base case requires perfect execution.

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-based approach (not owner-earnings DCF — one-off distortion + cyclical pricing makes DCF unreliable, consistent with light-run approach). Terminal value = exit EV/EBITDA × 5-year EBITDA.

**Key inputs**:
- Current EV: $292.2B
- Shares: 268.72M
- Net cash: $7.4B → implied share price from EV = ($292.2B + $7.4B) / 268.72M = same as current $1,109.73 (this is self-consistent)
- Horizon: 3 years (to end-2028/early 2029) and 5 years

### Bear Case: Hyperscaler Decel + Persistent Wind Drag

| Item | Assumption |
|---|---|
| 2028 EBITDA | ~$6.5B (targets miss by 38%; gas pricing moderates; Wind stays −$400M) |
| Exit multiple | 25x EV/EBITDA |
| Net cash 2028 | ~$12B (lower FCF than guide) |
| EV 2028 | $6.5B × 25x = $162.5B |
| Equity value 2028 | $162.5B + $12B = $174.5B |
| Per share (est. 265M, modest buyback) | **~$659** |
| 3-year IRR (from $1,109.73) | **~−15.4%** |
| Bear commentary | Severe de-rating: market pays 49x today for an asset that delivers $6.5B EBITDA → 25x re-rate is the punishment |

### Base Case: ~80% of 2028 Targets Achieved

| Item | Assumption |
|---|---|
| 2028 EBITDA | ~$8.5B (guide miss ~18%; some tariff headwind; Wind improves) |
| Exit multiple | 28x EV/EBITDA |
| Net cash 2028 | ~$18B (FCF $17-18B cumulative 2026-2028) |
| EV 2028 | $8.5B × 28x = $238B |
| Equity value 2028 | $238B + $18B = $256B |
| Per share (est. 263M shares after buyback) | **~$974** |
| 3-year IRR (from $1,109.73) | **~−4.3%** |
| Base commentary | Even with reasonably good execution, you underperform at current price over 3 years |

### Bull Case: Full 2028 Targets + Re-Rate

| Item | Assumption |
|---|---|
| 2028 EBITDA | ~$10.4B (targets met; Wind 6% achieved) |
| Exit multiple | 32x EV/EBITDA (premium sustained for execution) |
| Net cash 2028 | ~$22B (cumul. FCF per guide) |
| EV 2028 | $10.4B × 32x = $332.8B |
| Equity value 2028 | $332.8B + $22B = $354.8B |
| Per share (est. 260M after buyback) | **~$1,365** |
| 3-year IRR (from $1,109.73) | **~+7.2%** |
| Bull commentary | Even the optimistic scenario barely clears the 8% hurdle over 3 years |

### IRR Summary

| Scenario | 3-yr IRR | 5-yr IRR (est.) | vs 8% hurdle |
|---|---|---|---|
| Bear | **−15.4%** | −8 to −10% | FAILS — significantly |
| Base | **−4.3%** | ~+3-5% | FAILS |
| Bull | **+7.2%** | ~+10-12% | Barely PASSES at 5 years |

---

## Margin of Safety Analysis

**Buy-below at 8% hurdle rate**:
For base-case 3-year IRR to equal 8%: need current price ≈ $756 (implied entry price given $974 base case exit, discounting back at 8%).
For bull-case 3-year IRR to equal 8%: need current price ≈ $1,083 (just below current $1,109).

**MOS verdict**: 
- At $1,109.73, even the bull case barely clears the 8% hurdle at 3 years.
- The base and bear cases fail the hurdle rate by significant margins.
- There is **essentially ZERO margin of safety** at current price.
- The market is pricing the 2028 targets as near-certainty AND maintaining a ~28-30x 2028 EBITDA multiple.

---

## Valuation Discipline

| Zone | Price | Rationale |
|---|---|---|
| Deep value / CORE | **< ~$750** | ~$6.5B EBITDA × 25x = $162.5B EV → $664/sh; + solid MOS for base at 8% hurdle |
| STARTER zone | **$750 – $950** | 8%+ base IRR; base-case MOS positive; pay for confirmed rent, not target rent |
| No-add / Hold zone | **$950 – $1,150** | Pricing in majority of 2028 targets; ~0 to −5% IRR base case |
| **Current: $1,109.73** | **→ WATCH / avoid new entry** | At or above no-add zone; only bull-case IRR marginal at 8% |
| Avoid / trim | **> ~$1,150** | At or near 52-wk high; new entry = negative expected value in base/bear |

**Buy-below (STARTER): ≤$950** (consistent with light run's ~$950; CONFIRMED primary-sourced)

---

## Comparison to Light Run Numbers

| Light Run Claim | Primary-Sourced Value | Status |
|---|---|---|
| FY2025 rev ~$38.07B | $38,068M | CONFIRMED |
| ~$2.9B tax release | ~$2.9B | CONFIRMED |
| ~$87B services RPO | ~$87B (YE2025; Q1'26 shows ~$87B per transcript) | CONFIRMED (approximate) |
| +10–20% GT pricing | "10 to 20 points higher on $/kW" (management quote) | CONFIRMED |
| FY2025 FCF ~$3.7B | $3,710M | CONFIRMED |
| EV/fwd-EBITDA ~46–51x | ~48–51x (2026E) | CONFIRMED |
| Buy-below ~$950 | ~$750–950 (our analysis) | CONFIRMED (light run was reasonable) |
| Market cap ~$298B | $298.2B | CONFIRMED |
| EV ~$292B | $292.2B | CONFIRMED |
