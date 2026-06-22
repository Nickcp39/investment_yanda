# Model Assumptions — NBIS

Last updated: 2026-06-18

Purpose: document the drivers behind `../valuation.md`. Forward numbers are assumptions, not facts; actuals cite `../facts.md`. Owner-earnings DCF is not usable (FCF negative through ≥2028) → scenarios are EV/forward-sales triangulation. See `scenario_model.csv`.

## Historical Period

Start year: 2024 (first meaningful AI-cloud revenue, post-relisting)
End year: Q1 2026 (latest reported)
Currency: USD (US GAAP)
Per-share basis: 253.9M basic / 308.97M diluted wtd-avg (C030)

## Anchor actuals

| Metric | FY2024 | FY2025 | Q1 2026 | claim_id |
|---|---:|---:|---:|---|
| Revenue | $117.5M orig | $529.8M | $399.0M | C001–C003 |
| ARR (exit) | $90M | $1.25B | $1.9B | C004 |
| Capex | $807.5M | $4,066M | $2,472.9M | C005–C006 |
| Adj. EBITDA (group) | −$226.3M | −$64.9M | +$129.5M | C007 |
| Contracted / active power | ~25MW / — | >2GW / ~170MW | >3.5GW / n/d | C018, C020 |

## Forecast Drivers

| Driver | Bear | Base | Bull | Evidence / source_id |
|---|---:|---:|---:|---|
| Revenue (FY2028, $B) | ~8 | ~15–17 | ~21+ | consensus span $4–11B FY27 (C031); mgmt $7–9B exit-ARR (C032) |
| Terminal EV/Sales | 4x | 5–6x | 7x | peers: CRWV ~7.7x fwd, hyperscalers ~9–10x (C031) |
| Capex / revenue | stays ~5–7x → dilution | falls toward 2–3x | falls fast, FCF inflects | C005 (now ~7.7x) |
| Adj. EBITDA margin (group) | <20% | ~35–40% | >40% | guide ~40% FY2026 (C032) |
| GPU useful life | ~3yr (impairment) | 5yr holds | 5yr conservative | C011 (just 4→5) |
| Share count | further dilution | modest | minimal | C038 (+27% to date) |

## Key model drivers (why each is uncertain)

1. **Active-power conversion** (contracted GW → live MW) — THE revenue driver; active MW undisclosed since YE2025. (C020)
2. **Realized price/MW** — strong now (sold out, raised prices), commoditizes if supply catches up / ASICs scale. (C029)
3. **Capex/revenue** — bull needs it to fall; bear has it perpetual → dilution.
4. **GPU residual value** — 5yr vs real ~3yr is the depreciation swing. (C011)
5. **Contract structure** — take-or-pay vs terminable unresolved (C014/C015) → durability under stress.

## Assumption Discipline

- Do **not** assume $7–9B exit-ARR converts 1:1 to recognized revenue (recognition lags energization).
- Do **not** use >7× terminal multiple to rescue the present — the stock already embeds a mature multiple **today** (implied-expectations check, `../valuation.md`).
- Bear is plausible (churn/commoditization/dilution), not theatrical. Bull does not require *everything* right but does require backlog conversion + held premium.
- Treat capex $ as a range until Q2 2026 6-K (~Aug 2026) confirms $20–25B vs $31–35B. (C032/C033)
