# TEM Valuation (M6)

Last updated: 2026-07-04 | as_of: 2026-07-04 | as_of_price: **$60.27**
See `model/scenario_model.csv` for IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (as_of 2026-07-04, last close 2026-07-02) | **$60.27** | Frozen input, cross-checked vs independent websearch ($60.04, 0.4% delta) |
| Shares outstanding | **179,404,620** | TEM-10Q-Q1-2026 (Class A 174,360,831 + Class B 5,043,789) |
| Market cap | **~$10,813M** | 179.405M × $60.27 |
| Net debt (post-May-2026-refinancing estimate) | **~$665M** | DERIVED — Q1 2026 10-Q balance sheet ($1,233M gross debt, $639M cash+marketable securities) adjusted for the May 12, 2026 $460M convertible-notes refinancing (facts.md E48-E53): +$441.9M net proceeds, −$307.7M credit-facility repayment, −$31.2M capped call, less ~2 months' operating burn since Q1-end |
| Enterprise value | **~$11,478M** | Market cap + net debt |
| 52-wk context | **−42% off 52wk high $104.32** | websearch cross-check |
| Price vs 52-wk low | **+44% above 52wk low $41.73** | websearch cross-check |

**High/low-hug check**: Price is NOT near either 52-week band edge (42% below high, 44% above low) — this is a mid-range price reflecting the stock's volatility over the past year, not a stale or extreme data point. No T2-tripwire concern.

---

## Why Trailing GAAP Multiples Are Meaningless (and Why We Use Revenue Multiples)

TEM has NEVER posted a full-year GAAP profit and is not expected to in FY2026 (adj EBITDA guide ~$65M, GAAP net income still negative). Unlike GEV (where the issue was one-off DISTORTIONS to an otherwise-real earnings base), TEM's issue is that there is, as yet, **no meaningful earnings base to distort** — P/E and EV/EBITDA (GAAP) are both undefined or nonsensical (negative denominators). This is a standard, disclosed characteristic of a growth-stage healthcare-AI company, not a red flag on its own, but it means the ONLY defensible near-term valuation anchor is a **revenue multiple**, disciplined by a path-to-profitability sanity check (does the implied revenue multiple, combined with the DISCLOSED margin trajectory, produce a plausible normalized-earnings multiple at maturity?).

| Metric | Value | Read |
|---|---|---|
| EV / FY2026E revenue ($1.59B guide) | **~7.2x** | The primary near-term multiple |
| EV / TTM revenue ($1.364B, Q2'25-Q1'26) | **~8.4x** | Trailing comp |
| Adj EBITDA margin FY2026 guide | ~4.1% | Thin, but the FIRST full-year positive guide in company history |
| Implied EV / FY2026E adj EBITDA (if achieved) | **~177x** | Meaningless as a standalone anchor at this margin level — included only to show why revenue multiple, not EBITDA multiple, is the correct near-term tool |

**Sanity check against peers**: Guardant Health (2025 revenue guide ~$915-925M, also not yet consistently GAAP-profitable) has historically traded in the mid-single-digit-to-high-single-digit EV/revenue range depending on growth/margin trajectory — TEM's ~7.2x on FY2026E revenue is NOT an obviously extreme multiple relative to comparable growth-stage genomic-testing/health-data names, though it does embed some "AI premium" versus a pure lab-testing comp given the Data/Applications segment's growth and pharma-deal signings.

---

## Five-Year Scenario Model (Revenue-Multiple + Margin-Trajectory Approach)

Methodology: project FY2031 (5-year horizon) revenue under three growth/execution scenarios tied directly to the qualitative kill-paths in `inversion_map.md`, apply a scenario-appropriate EXIT revenue multiple (reflecting whether the AI/data moat validates or the business de-rates to a mature-lab-testing comp), subtract projected net debt, divide by a scenario-appropriate DILUTED share count (reflecting the dilution kill-path), and back-solve the 5-year IRR from the current $60.27 price. Full detail in `model/scenario_model.csv`.

### Bear Case: Reimbursement Gap Persists, AI Moat Proves Narrow/Contestable

| Item | Assumption |
|---|---|
| Revenue CAGR (5yr) | ~18% (moderating from current 25-36%; reimbursement-gap drag on Diagnostics volume economics; Data/Applications growth slows as pharma deal renewals disappoint) |
| FY2031 revenue | ~$3,638M |
| Exit multiple | 3.5x EV/revenue (de-rates to a mature genomic-testing-lab comp, e.g., Guardant/Natera-style multiple, as the AI narrative fails to differentiate) |
| Share count 2031 | ~263.6M (+~8%/yr dilution — continued ATM + SBC + M&A stock, unmitigated by FCF turning positive) |
| Net debt 2031 | ~$865M (burn continues to require financing) |
| Price 2031 | **~$45.02** |
| **5-yr IRR (from $60.27)** | **−5.7%** |
| 3-yr IRR | **−10.7%** |
| Bear commentary | This is NOT a "business fails" scenario — revenue still more than doubles. It is a "the market stops paying an AI premium and the reimbursement drag compounds" scenario, consistent with Kill Paths F1+F2 in `inversion_map.md` triggering together. |

### Base Case: Partial Reimbursement Fix, Data Moat Holds for ~25% Segment

| Item | Assumption |
|---|---|
| Revenue CAGR (5yr) | ~22% (moderating gradually from current pace; MAC/reimbursement negotiations achieve partial success; Data/Applications continues at a healthy, not spectacular, clip) |
| FY2031 revenue | ~$4,297M |
| Exit multiple | 7.0x EV/revenue (holds near CURRENT multiple — a fair multiple for a 20%+ grower with a credibly improving margin structure, neither de-rated nor re-rated) |
| Share count 2031 | ~240.1M (+~6%/yr dilution — moderating as adj EBITDA turns durably positive and FCF reduces reliance on external financing) |
| Net debt 2031 | ~$400M (some paydown/conversion as FCF improves) |
| Price 2031 | **~$123.63** |
| **5-yr IRR (from $60.27)** | **+15.5%** |
| 3-yr IRR | **+18.0%** |
| Base commentary | This scenario assumes NEITHER full validation nor full failure of the AI/data thesis — a "the company executes reasonably well on both segments, dilution moderates as expected, multiple neither expands nor compresses" outcome. It CLEARS the 8% hurdle with real margin. |

### Bull Case: Reimbursement Gap Closes, AI/Data Moat Fully Validated

| Item | Assumption |
|---|---|
| Revenue CAGR (5yr) | ~28% (near current pace sustained; Algorithms segment scales meaningfully beyond 1.6% of revenue; reimbursement gap closes, boosting Diagnostics economics) |
| FY2031 revenue | ~$5,463M |
| Exit multiple | 11.0x EV/revenue (re-rates toward a validated "AI healthcare platform" comp — a genuine moat premium, analogous to how the market prices durable software/platform businesses) |
| Share count 2031 | ~218.3M (+~4%/yr dilution — meaningfully slowing as the company becomes FCF-generative and reduces capital-markets dependence) |
| Net debt 2031 | ~−$500M (net CASH positive — the company self-funds and delevers) |
| Price 2031 | **~$277.61** |
| **5-yr IRR (from $60.27)** | **+35.7%** |
| 3-yr IRR | **+40.0%** |
| Bull commentary | This requires ALL THREE compound-bet legs (reimbursement fix, moat validation, dilution deceleration) to resolve favorably — plausible, evidenced by real early data points (NRR 126%, pharma deal-signing), but not yet proven. |

### IRR Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | **−10.7%** | **−5.7%** | FAILS |
| Base | **+18.0%** | **+15.5%** | **PASSES with real margin** |
| Bull | **+40.0%** | **+35.7%** | PASSES strongly |

---

## Margin of Safety Analysis

**Buy-below at 8% hurdle rate (5-year, base case)**: **$84.14** — the price at which the BASE case exactly clears an 8% annualized return. Current price $60.27 is **28% BELOW** this buy-below level, meaning the base case already provides a genuine, quantified margin of safety at the as_of price — this is the single most important valuation finding in this dossier, and it is what separates TEM's verdict from GEV's (where even the BULL case barely cleared 8% and there was ZERO margin of safety).

**Buy-below for a "the worst case is still tolerable" CORE-style zone**: **~$45** — approximately where even the BEAR case (reimbursement gap persists, moat unproven) would deliver something close to breakeven-to-modest-positive real returns rather than a genuine capital-destruction outcome. TEM is currently ~34% ABOVE this deep-value floor, meaning there is real, non-trivial bear-case downside still embedded at $60.27 (bear 5yr IRR is −5.7%, a real if moderate loss) — this is NOT a "no possible downside" situation.

**MOS verdict**: TEM at $60.27 offers a genuinely different risk/reward shape than the GEV/MSFT exemplars:
- Unlike GEV (all three scenarios failed the 8% hurdle at 3yr; zero margin of safety at $1,109.73), TEM's BASE case clears the hurdle with real margin.
- Unlike MSFT (an established, profitable moat business with a POSITIVE margin of safety AND high completeness), TEM's positive-MOS finding comes bundled with (a) unresolved completeness gaps (exact pharma-deal contract terms, segment margin detail — facts.md O1-O3), (b) a genuine, non-trivial BEAR-case capital-loss scenario (unlike GEV/MSFT where the downside was "underperform," not "lose money"), and (c) the governance/dilution/related-party caution flags detailed in `operator_underwriting.md` and `inversion_map.md`.
- The verdict is therefore NOT a simple "price supports STARTER" like MSFT — it requires weighing a genuine positive numerical MOS against real, quantified, company-specific risks that are structurally different in kind (not just degree) from a mature moat business.

---

## Valuation Discipline

| Zone | Price | Rationale |
|---|---|---|
| Deep value / CORE-consideration | **≤ ~$45** | Even the bear case (reimbursement gap persists, moat unproven) is roughly tolerable; genuine floor-level pricing |
| STARTER zone | **≤ ~$60-65** | Base case clears 8% hurdle with real margin (buy-below $84.14); current $60.27 sits comfortably in this zone |
| Add-on-confirmation zone | **$65-84** | Base case still clears hurdle but with thinner margin; would want confirmation of reimbursement-gap progress or Data segment deal-signing momentum before adding here |
| No-chase / trim zone | **> ~$84** | Above the base-case buy-below; would require the BULL case (or better) to justify entry, i.e., betting on full moat validation |
| Avoid at any size | **> ~$189** | Even the BULL case fails the 8% hurdle above this level (bull buy-below) |

**Buy-below (STARTER): ≤$84** — current price $60.27 clears this with a 28% cushion.

---

## What Would Change This Verdict

- **Upgrade toward CORE**: (a) confirmed, SEC-primary (not trade-press) contract terms for the AstraZeneca/GSK/Merck deals showing genuine multi-year committed revenue, (b) evidence the MAC/Palmetto reimbursement approval has been won and commercial in-network rates have improved, (c) a slowdown in dilution rate (share count growth <5%/yr) confirming the FY2026 adj-EBITDA-positive trajectory is translating into reduced capital-markets dependence.
- **Downgrade toward WATCH/AVOID**: (a) reimbursement negotiations stall or a competitor (FMI/Guardant) wins a comparable multimodal-data deal with a major pharma customer, undermining the differentiation thesis, (b) a third convertible-note or dilutive ATM raise within the next 2-3 quarters signaling the FY2026 adj-EBITDA guide is not translating into reduced cash need, (c) any governance/related-party scrutiny event materializing (see `inversion_map.md` F4).
