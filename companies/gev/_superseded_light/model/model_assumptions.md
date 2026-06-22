# Model Assumptions — GEV

Last updated: 2026-06-19

Purpose: document the drivers behind `../valuation.md`. Forward numbers are assumptions/guide, not facts; actuals cite `../facts.md`. ⚠️ Owner-earnings DCF is **not** usable (one-off-distorted base + cyclical equipment pricing) → scenarios are **normalized-EBITDA × EV/EBITDA**. See `scenario_model.csv`.

## Historical Period

- Start: FY2024 (first partial year post-spin, April 2024)
- End: Q1 2026 (latest reported)
- Currency: USD
- EV anchor: ~$292B at $1,109.73 (2026-06-19)

## Anchor actuals (clean reads — one-offs stripped)

| Metric | FY2024 | FY2025 | Q1'26 | claim_id |
|---|---:|---:|---:|---|
| Revenue | — | $38.07B (+9%) | $9.34B (+16%) | C002, C005 |
| Operating income | — | **$1.39B** (clean) | — | C002 |
| Net income (GAAP) | — | $4.9B ⚠️ (−$2.9B tax release) | $4.745B ⚠️ (−~$4.5B M&A) | C003, C006 |
| FCF | $1.7B | $3.7B | $4.8B ⚠️ (−~$5.3B advances) | C004, C007 |
| Segment EBITDA margin | — | inflecting | Power 16.3% / Elec 17.8% / Wind −$382M | C021 |
| Total RPO (equip/services) | — | — | $163.3B ($75.9B / $87.4B) | C012 |

## Forecast Drivers

| Driver | Bear | Base | Bull | Evidence / source_id |
|---|---:|---:|---:|---|
| **Normalized EBITDA** ($B) | ~5 | ~10 | 10+ | 2026 adj guide $5.7–6.4B (C010); 2028 target ~$10B+ on $52B @ ~20% (C023) |
| **EV/EBITDA multiple** | ~25x | ~30x | higher | Siemens ~39x; GEV premium today ~46–51x (C033) |
| Equipment pricing premium | fades (cyclical) | holds into 2028 | sustains + extends to 2030 | +10–20% 2026 (C016); demand-pull (C030) |
| Reservation→firm conversion | partial cancels | converts on plan | fully converts 2029–30 | 56 GW reservations vs 44 GW firm (C014) |
| Wind | drag persists / widens | 6% by 2028 on declining rev | break-even early | −$382M Q1; ~$400M FY26 loss (C028) |
| Hyperscaler capex slope (shared switch) | 2027 digestion | plateau-then-grow | keeps accelerating | ~$725B 2026 +77% (C030) |

## Key model drivers (why each is uncertain)

1. **Equipment-pricing durability** — the +10–20% premium is *cyclical* (demand-pull from hyperscaler capex). Bear has it fade; bull has it sustain. (C016, C030)
2. **Reservation→firm conversion** — 56 GW of the 100 GW is soft reservations; conversion proves durable rent vs a booking peak. (C014, C017)
3. **Normalized EBITDA** — the clean 2026 base (~$5.7–6.4B adj) vs the 2028 target (~$10B+) is the bridge; how much is structural vs cyclical is the question.
4. **Wind** — bear has it widening (kill b mildly triggered); base assumes the 6%/2028 path. (C028)
5. **ROIC as capacity lands 2027–28** — kill (c): does the $10B capex compress returns? Not yet visible. (C031)

## Assumption Discipline

- **Do not** value the cyclical equipment premium at a permanent-rent multiple — the central error the market is making.
- **Do not** use trailing GAAP / screener EV-EBITDA (one-off-distorted) — use the clean forward bridge.
- Bear (~$5B EBITDA × ~25x → ~$600–700) is *plausible* (2027 digestion + premium fade + Wind), not theatrical.
- Base (~$10B × ~30x → ~flat) assumes targets ~met — i.e., the price already embeds success.
- Bull ($1,400+) requires sold-out-through-2030 + SMR/Electrification 22% sustaining the re-rate.
- Treat the **services annuity ($87B RPO) as the durable, richly-valued layer** and the **equipment premium as the cyclical, modestly-valued layer** — don't blend them into one permanent multiple.
