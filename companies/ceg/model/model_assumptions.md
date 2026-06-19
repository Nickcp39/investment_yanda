# Model Assumptions — CEG

Last updated: 2026-06-19

Purpose: document the drivers behind `../valuation.md`. Forward numbers are assumptions, not facts; actuals cite `../facts.md`. Owner-earnings DCF is not used (combined-entity FCF not cleanly reported post-Calpine; hedge ratios undisclosed) → scenarios are **forward adj-EPS × a terminal multiple**, bracketed by merchant peers and the franchise premium, cross-checked against Street targets. See `scenario_model.csv`.

## Historical Period

Start: FY2025 (latest full year, standalone)
Latest reported: Q1 2026 (first Calpine-consolidated quarter)
Currency: USD (US GAAP)
KPI basis: **adjusted operating EPS** (the franchise/Street metric; GAAP swings on commodity marks)

## Anchor actuals

| Metric | FY2025 | Q1 2026 | claim_id |
|---|---:|---:|---|
| Revenue | $25.5B (+8%) | $11.1B (+64%, Calpine artifact) | C001, C005 |
| Adj operating EPS | $9.39 (beat) | $2.74 (beat $2.59) | C002, C006 |
| GAAP EPS | $7.40 | $4.49 | C002, C006 |
| Nuclear capacity factor | 94.7% | 92.3% | C004, C007 |
| FCF | ~$1.3B | n/d (combined) | C003 |
| Net debt / leverage | ~$5.3B / ~0.9x standalone | ~$21.6B / ~3.8x post-Calpine (est.) | C011 |

## Forecast Drivers

| Driver | Bear | Base | Bull | Evidence / source_id |
|---|---:|---:|---:|---|
| Adj EPS basis ($) | ~12.0 (near guide-mid) | ~13.0 (fwd) | ~13.8 (fwd) | FY26 guide $11–12 (C009); base/bull flex on Crane + Calpine + PPAs |
| Terminal P/E (x) | ~18 (merchant peer) | ~25 (premium holds) | ~30 (re-rate) | peers VST 16x / TLN 17–18x / NRG 18x (C028); franchise premium 24–30x |
| Crane (2027) | delayed/contested | **on track 2027** | on track + 2nd restart | C017 |
| Calpine | deleverage **stalls** | accretes + deleverages → ~2.0x | clean → ~2.0x | C014, C011, C024 |
| New hyperscaler PPA | none | 1–2 signed | multiple | C013, C021 (none confirmed yet) |
| Power price (open years) | toward ~$25 floor | ~$34/MWh holds | firm/up | C026 |

## Key model drivers (why each is uncertain)

1. **New hyperscaler PPA** — the swing for the *equity* re-rate (Crane's upside is already to MSFT). None confirmed today → the catalyst, not a base fact. (C013)
2. **Calpine deleverage** — ~3.8x → ~2.0x by 2027 is a forecast (LS Power $5B signed, cash not yet in). A stall re-rates the entity toward a merchant-gas multiple. (C011, C024)
3. **Terminal multiple** — the bear/base gap is mostly *multiple* (18x vs 25x) on a similar EPS, because the franchise is intact in both; the question is whether the premium-to-peers holds.
4. **Power-price level** — floored by §45U (~$25/MWh to 2032), so the downside is bounded; open years priced ~$34. (C026)
5. **MSFT PPA price** — undisclosed → Crane annuity not directly sizeable; affects how much base/bull EPS upside is real vs capped. (C013)

## Assumption Discipline

- Implied prices in `scenario_model.csv` are **reconciled to land inside the locked `../memo-v1.md` ranges** (bear $200–230 / base $300–340 / bull $400+). Do not let the EPS×multiple math drift outside those ranges.
- Do **not** use a >30x terminal multiple to rescue the present — ~24x already embeds a premium to 16–18x peers (C027/C028).
- Bear is plausible (deleverage stall + no PPA + multiple compression), **not** an earnings collapse — the §45U floor makes the bear shallow. Bull does not require everything right, but does require a new PPA + clean deleverage.
- Treat post-Calpine leverage and combined FCF as **estimates** until the Q1'26 10-Q. (C011)
