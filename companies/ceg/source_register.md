# Source Register — CEG (Constellation Energy)

Last updated: 2026-06-19

Purpose: assign stable source IDs before claims enter `claim_ledger.csv`. Mirrors the IDs already used in `facts.md` (S1–S9) and extends them (S10–S12) for sources surfaced in decomposition.

Tier scheme: **A1** = SEC primary filing (10-K / 10-Q / 8-K). **A2** = company primary (IR newsroom, earnings release, investor deck, official PR). **A3** = government/regulatory primary (FERC order, NRC notice, IRS notice, statute). **B1** = management commentary (earnings-call transcript). **B2** = independent analyst / financial press. **C** = KOL/video (narrative only, never a fact).

| source_id | Tier | Source | Date | URL / Local path | Supports (blocks / claims) |
|---|---|---|---|---|---|
| **S1** | A2 | CEG FY2025 earnings release | 2026-02-23 | constellationenergy.com/news/2026/02/...full-year-2025-results.html | FY2025 revenue/EPS/FCF, nuclear CF 94.7%, capital return — `financial_quality`, C001–C004, C020–C022 |
| **S2** | A1/A2 | CEG Q1 2026 8-K / earnings | 2026-05-11 | stocktitan.net/sec-filings/CEG/8-k...111d3b4cfb03 | Q1'26 (first Calpine-consolidated qtr) revenue/EPS, nuclear CF 92.3%, buyback raise — `financial_quality`, C005–C008, C023 |
| **S3** | A2 | CEG 2026 Business & Earnings Outlook deck | 2026-03-31 | investors.constellationenergy.com | FY2026 guide $11–12, 20%+ base-EPS CAGR to 2029, deleverage path — `financial_quality`, `valuation`, C009–C011 |
| **S4** | A2 | CEG–Calpine completion release | 2026-01-07 | constellationenergy.com/news/2026/01/...completes-calpine-transaction.html | Calpine close, ~55 GW combined, deal structure $26.6B — `business_model`, `operator_underwriting`, C012–C014, C024 |
| **S5** | A3 | FERC Order, Docket EL25-49 (193 FERC ¶61,217) | 2025-12-18 | FERC E-1-EL25-49-000 | 5-0 order directing PJM to enable co-located load; accept-in-part 2026-04-16 — `bottleneck_map`, `inversion_map`, C015–C016 |
| **S6** | A3 | NRC draft EA / FONSI (Crane restart) | 2026-06-08 | Federal Register via Justia | Crane restart on track 2027, comment to 2026-07-08 — `bottleneck_map`, C017–C018 |
| **S7** | A3 | IRS §45U credit page / Notice 2025-37; OBBBA P.L.119-21 §70510 | 2025-07 | irs.gov/credits-deductions/zero-emission-nuclear-power-production-credit; via Morgan Lewis / Clifford Chance | §45U PTC survived OBBBA; ~$15/MWh max, ~$25/MWh gross-receipts floor, sunset 2032, FEOC-only changes — `inversion_map`, `valuation`, C019, C026 |
| **S8** | B2 | Hyperscaler 2026 capex compilation (FT / CNBC) | 2026-02 | cnbc.com/2026/02/06/... | Hyperscaler 2026 capex ~$725B +77% (AMZN $200B / MSFT $190B / GOOGL $190B / META $115–135B) — `value_chain_map`, `inversion_map` (shared switch), C025 |
| **S9** | B2 | stockanalysis.com (CEG / VST / peer multiples) | 2026-06 | stockanalysis.com/stocks/ceg/ | Price, mkt cap, EV, fwd P/E, EV/EBITDA, peer multiples (VST/TLN/NRG) — `valuation`, C027–C028 |
| **S10** | A2 | CEG / DOE — Crane $1.0B loan guarantee close | 2025-11-18 | energy.gov LPO / CEG IR (referenced in pack) | $1.0B DOE loan backstops ~$1.6B Crane capex — `financial_quality`, C018 |
| **S11** | A2 | CEG–LS Power divestiture agreement | 2026-03-18 | CEG IR / LS Power PR (referenced in pack) | $5B / 4.4 GW asset sale signed (DOJ/FERC divestiture + deleverage) — `operator_underwriting`, C024 |
| **S12** | A2/B2 | Microsoft–Constellation Crane PPA (20-yr) | 2024-09 (orig); restated via S6 | constellationenergy.com newsroom; secondary press | 20-yr PPA exists; front-of-meter structure; **price undisclosed** — `business_model`, `bottleneck_map`, C013 (price = UNVERIFIED) |

## Notes on verification

- **Primary release URLs (S1, S2) returned HTTP 404/410 on automated fetch 2026-06-19** (link rot / anti-scraping on constellationenergy.com and stocktitan.net). The headline figures they support are nonetheless **pre-locked in `facts.md`** from the Block-1 research pass and are internally consistent; they are carried at the confidence the pack assigned (HIGH for reported financials). Re-confirm against the SEC-filed 10-K (FY2025) and 10-Q (Q1'26) at next review.
- **S12 (Microsoft PPA):** existence is HIGH-confidence; **pricing is UNDISCLOSED by CEG** → any economic sizing of Crane is inference, marked UNVERIFIED throughout.
- Tier rules align with the project `sources/source_policy.md` convention used in the NBIS case.
