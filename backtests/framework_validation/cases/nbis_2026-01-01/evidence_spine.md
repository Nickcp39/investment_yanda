# M1 Evidence Spine - NBIS 2026-01-01

## 0. Module Verdict

- Role: confidence
- M1 signal: **0** (neutral — adequate primary evidence; one structural blind spot caps it from going positive)
- Confidence: **medium-high** on reported facts; **low** on the unwritten variables (deal economics, March 2026 capex/financing plan, contracted-capacity conversion risk)

## 1. Audited / High-Confidence Facts (primary-sourced, dated <= 2026-01-01)

| # | Fact | Source | Quality |
|---|---|---|---|
| 1 | As-of price $83.71 (2025-12-31 close); as-of market cap ~$21.1B (251.8M sh) | S014 | High (exchange data) |
| 2 | Q3'25 group revenue $146.1M (+355% YoY, +39% QoQ); core ~90% of revenue | S012, S013 | High (6-K) |
| 3 | Core AI infra ARR ~$551M end-Sept 2025; trajectory ~$220M -> $249M -> $430M -> $551M across FY24 exit to Q3'25 | S001, S004, S006, S013 | High (releases) |
| 4 | Core business adjusted-EBITDA positive (~19% margin Q3'25); group adj EBITDA loss narrowed to -$5.2M | S005, S013 | High (6-K) |
| 5 | GAAP still loss-making: Q3'25 net loss -$119.6M; Q2'25 GAAP profit was a Toloka revaluation gain, not operations | S012, S005 | High (6-K) |
| 6 | Balance sheet 9/30/25: cash $4,794.8M, debt ~$4,106.8M -> roughly net-cash at quarter end | S012 | High (6-K) |
| 7 | Capex ramp: H1'25 $1,054.5M; Q3'25 $955.5M; 9M PP&E purchases $2,010.0M | S005, S012 | High (6-K) |
| 8 | Microsoft deal: ~$17.4B through 2031, expandable to ~$19.4B, tranches 2025-2026, Vineland NJ, 5-yr | S007, S008 | High (6-K) |
| 9 | Meta deal: ~$3B over 5 years, announced 2025-11-11 (pre-cutoff); capacity-limited | S012, S013 | High (release) |
| 10 | Contracted power guidance raised to ~2.5GW by CYE2026 (from 1GW); 800MW-1GW connected by CYE2026; 220MW connected/100MW active by CYE2025 | S013 | High (CEO letter) |
| 11 | 2026 ARR target $7-9B by year-end 2026 (stated twice in CEO letter) | S013 | High (CEO letter) |
| 12 | Sept 2025 raise ~$4.2-4.3B: $2.75B converts (2030/2032; 1.00%/2.75%; conv ~$138.75) + $1.0B equity at $92.50; ATM up to 25M Class A shares (Nov) | S009-S012 | High (releases) |
| 13 | NVIDIA + Accel + Orbis invested $700M at $21.00/sh (Dec 2024); relisted Oct 2024; Russian ops divested ~$5.4B mid-2024 | S015-S017 | High; NVIDIA stake size undisclosed |
| 14 | NBIS NOT in Nasdaq-100 as of Dec 2025; short interest ~15.5% of float (late Dec 2025) | S021, S022 | High / med (1 secondary) |
| 15 | Closest public comp CoreWeave: ~$23B IPO EV (Mar 2025), 2024 rev $1.9B, MSFT 62% of revenue; Q3'25 rev $1.36B | S018, S019 | High (filings) |

## 2. Open Questions (knowable list; not resolvable from public data at as-of)

| # | Open question | Why it matters | Best available proxy |
|---|---|---|---|
| Q1 | What is the gross/EBIT margin and cash-on-cash return on the Microsoft and Meta contracts? | Determines whether large-deal ARR is value-accretive or capex-dilutive | Mgmt calls "economics attractive"; core 19% adj EBITDA margin; no contract-level disclosure |
| Q2 | How much incremental equity/debt will fund the ~2.5GW build, and at what dilution? | The entire thesis hinges on financing the build without crushing per-share value | Sept raise + ATM signal heavy reliance on capital markets; asset-backed debt is unproven |
| Q3 | How firm is "contracted power" -> connected -> active -> revenue conversion? | A gigawatt of contracted land is not revenue; conversion lag is the execution risk | CoreWeave's own data-center delays (S019) show the industry-wide hazard |
| Q4 | Customer concentration: how dependent is the 2026 ARR on Microsoft + Meta? | Concentration is the neocloud failure mode (cf. CoreWeave/MSFT 62%) | Two named mega-deals plus a diversified core base; mix not disclosed |
| Q5 | Will the $7-9B ARR target be hit, and how is it defined (last-month x12 can spike on a single tranche)? | ARR is a run-rate, not realized revenue; the metric can flatter a lumpy ramp | Definition disclosed (S013); 2026 realized revenue not yet guided in writing |
| Q6 | Governance: dual-class (Class B) control by founder; legacy ex-Yandex overhang | Affects minority-holder protection and any forced-seller dynamics | Class A/B split disclosed (S012); founder-led |

## 3. Source Quality Assessment

- **Tier 1 (filings/official releases):** S001-S013, S015-S017 — Nebius 6-Ks, the audited FY2024 20-F, and dated company press releases. The financial spine is essentially fully primary-sourced.
- **Tier 1 (exchange data):** S014 — Yahoo chart API daily close, saved locally; standard market-data quality.
- **Tier 1 (peer filings):** S018-S019 — CoreWeave IPO/earnings; S020 — IEA; S021 — Nasdaq.
- **Tier 2 (dated news):** S022 short interest (Benzinga); the Goldman target headline. Used for narrative/positioning only, not as core proof.
- **Not used:** No KOL/social/video material was load-bearing. The existing repo `companies/nbis/` folder was NOT read (post-cutoff per case control).

## 4. Confidence Grade and Sizing Implication

- The **reported business facts are high-confidence**: this is a real, audited, fast-scaling AI-cloud business with two named blue-chip contracts and a (briefly) net-cash balance sheet at 9/30/25.
- The **forward economics are low-confidence**: deal margins, the financing path for ~2.5GW, and capacity-to-revenue conversion are all undisclosed and are exactly the variables that decide whether this is a winner or a capital trap.
- M1 therefore emits **0**: evidence completeness is adequate to act, but the unresolved economics justify a confidence haircut on size rather than a free pass to CORE. Per the template, uncertainty becomes a smaller size and explicit kill gates, not an automatic WATCH/0%.
