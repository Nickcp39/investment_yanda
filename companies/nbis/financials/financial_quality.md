# Financial Quality — NBIS

Last updated: 2026-06-18

Source base: FY2025 20-F (SRC-001), Q1 2026 6-K (SRC-002). Facts: see `../facts.md` / `../claim_ledger.csv`.

## One-line read

A genuine hyper-growth, hyper-capital-intensive story: revenue +479% FY2025 and segment-level economics turning real (~45% core-segment EBITDA margin Q1'26), **but** group FCF is deeply negative (~−$3.7B FY2025), the buildout is funded by ~$12.5B of dilutive financing + customer prepayments, and there are **material accounting-quality flags** (4→5yr depreciation extension, two-year adverse ICFR, a fixed-asset material weakness) landing in the same year.

## Accounting → Economics Bridge (FY2025, USD)

| Item | Reported | Economic interpretation | claim_id |
|---|---:|---|---|
| Revenue | $529.8M | Real, but ~half from 2 anchor contracts; ARR ($1.9B) is unaudited last-month×12 | C001, C004 |
| Pre-tax net income | +$13.8M | **Not economic** — entirely a +$598.9M non-cash ClickHouse mark; operations still loss-making | C008 |
| Adj. EBITDA (group) | −$64.9M | Turned +$15.0M in Q4'25, +$129.5M Q1'26; core segment +earlier. Real operating leverage emerging | C007 |
| D&A | $417.9M (FY25, from $77.1M FY24) | Will be understated ~$167.6M in FY2026 by the useful-life change | C011 |
| SBC | $83.2M | Real cost; growing; ties to share price not ROIC | C036 |
| Capex | $4,066M (~7.7× rev) | Overwhelmingly **growth** capex; maintenance capex small today but rises as fleet ages | C005 |
| Operating cash flow | +$401.9M | **Flattered** by ~$982.5M customer prepayments (deferred rev) | C010 |
| Implied FCF (OCF−capex) | ≈ −$3,664M | The real cash story: deeply negative, plugged by financing | C010 |
| Cash / debt | $9.3B / $8.45B converts | Carrying net cash ~+$0.85B; principal-basis net debt ~−$0.76B | C009 |

**Owner-earnings estimate: not meaningful yet.** Owner earnings are negative — the business consumes capital. The bull case is that *future* owner earnings emerge once active power scales and capex/revenue normalizes; that is a forecast, not a current fact. Modeled in `../model/`.

## Quality Questions

- **Is revenue recurring?** Largely **contracted** (multi-year MSFT/Meta take-or-pay-style; though take-or-pay vs terminable is disputed — C014/C015), plus growing self-service. Higher quality than spot, but concentrated.
- **Does growth require rising capital intensity?** **Yes, extreme** — capex ~7× revenue. This is the defining feature. Returns depend on utilization staying high and GPU residual values holding.
- **Are margins expanding from scale, accounting, pricing, or utilization?** A mix: genuine operating leverage (cost of revenue 49%→26% of rev YoY) **and** pricing power (raised prices, still sold out) **but** also a depreciation-policy tailwind (−$167.6M) that flatters FY2026.
- **Is SBC a real cost?** Yes ($83.2M, growing); compounds the ~27% dilution.
- **Buybacks?** None — the company is issuing, not retiring, shares.
- **Is reported FCF overstating owner earnings?** Reported OCF overstates it (prepayment-inflated); FCF itself is honestly negative.

## Red Flags (verified — these are the diligence priorities)

1. **🚩 Depreciation life 4→5 yrs, eff. Jan 1 2026** → −$167.6M FY2026 depreciation, into an accelerating GB300→Rubin cadence. Exactly the "earnings flattery" pattern bears (Burry/Chanos) flag on the sector. (C011)
2. **🚩 Adverse ICFR two years running**; open material weaknesses in **fixed assets/PP&E** (depreciation start dates, asset-count reconciliation) and **TripleTen rev-rec**. The PP&E weakness sits directly under the depreciation change. Auditor Reanda → Deloitte for FY2026. (C012)
3. **🚩 Net income flattered** by a $598.9M non-cash ClickHouse revaluation — do not read GAAP net income as operating performance. (C008)
4. **ARR is unaudited** and flattering during a steep ramp. (C004)
5. **Customer prepayments inflate OCF** and create a "significant financing component" → interest expense. (C010)
6. **Capex guidance is verbal-only** ($20–25B; $31–35B floated in secondary) — written materials guide on power, not capex $. (C032, C033)

## So what

The economics are improving and could become high-quality **if** active power scales and capex/revenue falls. But the combination of (a) extreme capital intensity, (b) negative FCF, (c) a depreciation tailwind, and (d) a PP&E control weakness means **reported profitability quality is currently low and must be re-underwritten each quarter**. This is the opposite of a Terry-Smith "clean compounder" today.
