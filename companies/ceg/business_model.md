# Business Model — CEG

Last updated: 2026-06-19

Source base: business-model/value-chain raw, FY2025 (S1), Calpine close (S4). Facts: `facts.md` / `claim_ledger.csv`.

## One-Sentence Business

CEG is the **largest US merchant (non-rate-regulated) power producer** — it owns ~22 GW of carbon-free nuclear (running ~95% capacity factor at near-zero marginal cost) plus, post-Calpine, ~23 GW of dispatchable gas + Geysers geothermal and a large retail book, capturing margin by selling electrons into PJM/wholesale at gas-set clearing prices, with a fast-growing new lever: **bespoke long-dated PPAs to hyperscalers** that convert merchant volatility into contracted, §45U-PTC-floored annuity streams at a premium to wholesale.

## Who Pays?

| Customer | Product | Why they pay | Recurrence | Evidence |
|---|---|---|---|---|
| **Wholesale / PJM market** | electrons at clearing price | grid needs ~$0-fuel baseload to balance | continuous (merchant) | C020 |
| **Microsoft** | Crane (~835 MW) carbon-free output, matched to PJM datacenter load | needs 24/7 carbon-free power for AI; can't build nuclear | **20-yr PPA** (front-of-meter) | C013 |
| **Meta** | clean attributes of 1,092-MW Clinton from June 2027 | clean-energy matching for datacenters | multi-year | facts.md |
| **Retail customers** (post-Calpine) | electricity + energy services | integrated retail-plus-generation | recurring book | C012, C023 |
| **Future hyperscalers** (unsigned) | new bespoke PPAs | scarce carbon-free 24/7 power; capex accelerating | long-dated | C021, C025 |

## Revenue Engine

| Revenue stream | Pricing unit | Volume driver | Price driver | Main risk |
|---|---|---|---|---|
| **Merchant nuclear** (core) | $/MWh at PJM clearing | ~95% CF fleet | gas-set marginal price; **§45U ~$25/MWh floor** | power-price softening toward floor (C026) |
| **Hyperscaler PPAs** (new lever) | $/MWh contracted, 15–20yr | new deals signed | premium-to-wholesale; **MSFT price undisclosed** | Crane upside already capped to MSFT; next-PPA timing (C013) |
| **Calpine gas** | $/MWh dispatchable | ~23 GW gas + geo | spark spread; capacity payments | re-carbonizes purity; merchant gas volatility (C023) |
| **Retail (Calpine)** | customer margins | book size | competitive retail | churn; commodity pass-through |

**Revenue mix:** core economics are dominated by the nuclear inframarginal margin; the **strategic** value is the PPA lever (turns a commodity merchant into a contracted-annuity owner). Hedge ratios undisclosed → the open-vs-contracted split is the biggest near-term revenue-quality unknown.

## Ten-Year Existence Test

- **Problem in 10 years?** Yes — carbon-free 24/7 baseload demand is structurally growing (AI/datacenters + electrification), and the supply of it is effectively fixed.
- **Why CEG remains well-placed?** It **owns the scarce asset** (existing nuclear you can't build new), at scale, with a legislated PTC floor and a growing book of premium hyperscaler PPAs.
- **What changes the thesis?** Power curves collapsing toward the floor for years (compresses upside), Calpine deleverage stalling (balance-sheet impairment), or a hostile final FERC co-location definition (mostly an industry-BTM risk, minor for CEG's front-of-meter flagship). See `inversion_map.md`.

## Business Quality Scorecard

| Question | Answer | Evidence | Score (1–5) |
|---|---|---|---:|
| High willingness to pay? | **Yes** — hyperscalers pay a premium for scarce 24/7 carbon-free power; capex accelerating +77% | C021, C025 | 4 |
| Recurring / contracted? | Merchant base + growing 15–20yr PPAs + retail book; PTC-floored | C013, C026 | 4 |
| Does scale improve economics? | Yes — largest US producer; ~95% CF; near-zero marginal cost; **no capex treadmill** (fleet exists) | C004, C012, C018 | 4 |
| Reinvest at attractive returns? | Crane restart (DOE-funded), uprates, PPAs — high-return on existing asset; Calpine accretive-if-executed | C017, C014 | 4 |
| Inside circle of competence? | Power markets + nuclear ops + PJM/FERC regulation + Calpine integration — legible but specialized | step0_plan | 3 |

**Net:** a genuinely high-quality, contracted-and-floored franchise that owns the scarce input — structurally stronger than a typical merchant generator (and than NBIS's capital-treadmill model). The quality discount is **execution** (Calpine deleverage) and a **flagship whose upside is already sold** (Crane→MSFT), which is why the price — not the business — is what makes this a STARTER. See `valuation.md`.
