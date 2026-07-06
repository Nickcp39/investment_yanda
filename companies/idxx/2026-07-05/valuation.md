# IDXX Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$557.80**

---

## Current Multiple Snapshot

| Metric | IDXX | Notes |
|---|---|---|
| Price | $557.80 | Last close 2026-07-02, confirmed 2 sources |
| Market cap | $44.00B | 78.88M shares × $557.80 |
| 52wk range | $506.91 - $769.98 | Price is −27.6% off high, +10.0% above low [facts.md E2] |
| Trailing P/E | 41.03× | [E52] |
| Forward P/E | 37.01× | [E52] |
| EV/EBITDA (est.) | ~29.1-30.1× | Screener 29.05x [E53]; this model's derived 30.06x — strong internal consistency |
| P/FCF | 40.61× | [E53] |
| Price/Sales | 9.90× | [E53] |
| Dividend yield | 0% (no dividend) | [E7] |

---

## Peer Context: Zoetis (ZTS) — the Closest Public Animal-Health Comp

Zoetis is the most direct large-cap animal-health public comp, though it is NOT a clean pure-play match
(Zoetis is predominantly a pharmaceutical/vaccine company with a smaller diagnostics division, whereas
IDXX is a pure diagnostics/instruments company — the comp is directionally useful, not a precise
apples-to-apples multiple reference).

- Zoetis trades at a WIDE range depending on source/date: ~9.7-15x EV/EBITDA (various aggregators, mid-2026)
  and ~18.6-21x P/E (also varying by source and whether trailing/forward) — roughly **1.5-3x cheaper** than
  IDXX on an EV/EBITDA basis and roughly **2x cheaper** on a P/E basis, using the more conservative
  (higher) end of each range for Zoetis.
- Notably, Zoetis itself is reported facing "slower 2026 guidance and weakness in the companion animal
  market" — meaning the broader animal-health sector is NOT uniformly re-rating higher; IDXX's premium
  multiple appears to be a **company-specific** quality/growth premium (accelerating growth, expanding
  margins, raised guidance — financial_quality.md), not an industry-wide bull market in animal-health
  stocks.
- **Reading**: IDXX's premium over Zoetis is directionally JUSTIFIED by fundamentals (IDXX's growth is
  accelerating while Zoetis's is reportedly decelerating; IDXX's business mix is ~79% recurring
  high-margin diagnostics/consumables vs Zoetis's broader, lower-margin pharma/vaccine mix) — but the
  MAGNITUDE of the premium (1.5-3x on EV/EBITDA) leaves very little room for IDXX's growth advantage over
  Zoetis to narrow even slightly before the relative-value case erodes.

---

## Sell-Side / Market Context

- 15 analysts rate IDXX "Buy" (one broader count cites 17, with roughly 2/3 Buy, 1/3 Hold, zero Sell)
  [facts.md E6]; average price target **$709.14**, implying **+27.1% upside** from $557.80 [E52]. Street
  consensus is firmly constructive DESPITE the already-rich multiple — this is not a case where the Street
  is bearish and price alone offers a contrarian opportunity; it's closer to "everyone agrees this is a
  great business," which is itself a reason for caution about how much of the good news is already priced.

---

## Historical Multiple Context (important caveat)

IDXX has historically traded at premium, growth-compounder multiples for much of its public history
(various general/secondary sources reference historical P/E ranges in the 30-45x band across recent years
— not independently re-verified against a specific historical time series this run, flagged as an OPEN
item for a future refresh). This means the CURRENT ~41x trailing / ~37x forward P/E is not obviously an
outlier VERSUS IDXX'S OWN HISTORY — it may simply be "IDXX trading at its normal premium," which is a
materially different framing than "IDXX has newly become expensive." This caveat matters for the
scenario_model.csv exit-multiple assumptions: the base case's 24x EV/EBITDA exit (a moderate compression
from today's ~30x) already assumes some de-rating even under a "good, not perfect" execution scenario —
if IDXX's historically normal multiple band is genuinely closer to today's level than to a generic
med-tech average, the base case may be somewhat conservative rather than aggressive. Not resolved with
high confidence this run.

---

## 3-Scenario IRR (see model/scenario_model.csv for full methodology)

| Scenario | 3yr IRR | 5yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear (vet-visit decline accelerates + diagnostic-intensity plateau + AI-competition erosion) | −11.9% | −4.9% | FAIL |
| **Base (guidance achieved, growth normalizes to ~9-10% CAGR, modest multiple compression)** | **+2.8%** | **+5.6%** | **FAIL (both horizons)** |
| Bull (AI-flywheel edge proven durable, growth sustains mid-teens, multiple holds) | +16.5% | +15.2% | PASS |

**Key finding**: Even the BASE case (which assumes management's own strong current guidance is
essentially achieved and the growth algorithm continues working, just moderating from its current
acceleration) does not clear an 8% hurdle at either 3 or 5 years, under a moderate (30x → 24x EV/EBITDA)
multiple-compression assumption. This means the investment case is **not** "the business might disappoint"
(the evidence in this dossier says the business is currently executing exceptionally well) but rather
**"the price already assumes a continuation of exceptional, not just good, execution."** This is
structurally the GEV-exemplar pattern (great business, price is the binding constraint) — not the GEHC
pattern (business quality itself carries unresolved questions).

---

## Buy-Below / Price Band Analysis

| Band | Price | vs $557.80 | Rationale |
|---|---|---|---|
| No-chase ceiling | ~$650 | +16.5% | Above this, even the bull case offers a thinning margin of safety; would require the AI-flywheel durability question to already be resolved favorably |
| Current price | $557.80 | — | Base case FAILS 8% hurdle at both horizons; only bull case clears |
| **STARTER zone** | **$480-510** (near/at 52wk low $506.91) | **−14%~−9%** | Base case begins to clear or approach the 8% hurdle at this level without requiring bull-case AI/Mars-network questions to already be resolved |
| Add toward CORE | $420-450 | −25%~−19% | Base case clears the hurdle with genuine margin of safety; would likely require either a broader growth-stock de-rating cycle or an IDXX-specific growth deceleration to reach |
| Deep value | ~$380 (near bear-case 3yr terminal) | −32% | Would require the bear case's specific mechanism (visit decline + intensity plateau + AI erosion, simultaneously) to be actively unfolding — not the current situation |

**Recommended buy_below for new-money STARTER consideration: ~$500** (approximately at the current 52-week
low), consistent with the base case beginning to offer a real, if still modest, cushion against the primary
risk (valuation de-rating) without requiring the bull-case catalysts to already be proven.

---

## Binding Constraint

**PRICE, not business quality.** Every business-quality module in this dossier (moat_map.md,
financial_quality.md, operator_underwriting.md) supports a verdict at or near the top of this project's
S&P 500 medical batch reviewed to date: accelerating growth, expanding margins, raised guidance, clean
balance sheet, disciplined capital allocation, a genuinely evidenced (if not fully proven) AI-diagnostics
flywheel, and a thoughtfully-executed CEO succession that explicitly signals continuity in the highest-
priority growth vector. The constraint on this investment is that the market has already recognized all of
this — the stock trades at a ~1.5-3x EV/EBITDA premium to the closest animal-health peer and a multiple
that requires continued NEAR-BEST-CASE execution just to clear a modest 8% hurdle. This is a "wonderful
business, full price" case, not a "flawed business at any price" case.
