# Model Assumptions — VRT

Last updated: **2026-06-22** (refreshed from 2026-06-19 seed)

Purpose: document the drivers behind `../valuation.md`. Forward numbers are assumptions, not facts; actuals cite `../facts.md`. VRT is **FCF-positive**, so the engine is a **driver → EPS × P/E → price** ladder (not an owner-earnings DCF and not the EV/forward-sales triangulation used for NBIS). The swing variable is the **forward multiple** on a high-beta, no-floor capex-cycle name. See `scenario_model.csv`.

## Historical Period

Start year: FY2024 (pre-acceleration base)
End period: **Q1 2026 (latest reported; Q2'26 = 2026-07-29, not yet public)**
Currency: USD (US GAAP; "adjusted" = management non-GAAP)
Share base: market cap **~$132.5B at $345.05** (384.11M shares, C029)

## Anchor actuals

| Metric | FY2025 | Q1 2026 | Guide FY26 | claim_id |
|---|---:|---:|---:|---|
| Net sales | $10,229.9M (+26% org) | $2,650M (+23% org) | $13.5–14.0B (+29–31% org) | C001, C007, C014 |
| Adj operating margin | 20.4% | 20.8% (+430bps) | 22.8–23.8% | C002, C009, C014 |
| Adj EPS | — | $1.17 (+83%) | $6.30–6.40 | C010, C014 |
| Adj FCF | $1,887.4M | $653M (+147%) | $2.1–2.3B | C003, C011, C014 |
| Backlog | $15.0B (+109%) | **WITHHELD (still dark at as_of)** | — | C004, C012 |

## Forecast Drivers

| Driver | Bear | Base | Bull | Evidence / source_id |
|---|---:|---:|---:|---|
| EPS basis | ~flat ($6–7) | FY26 ~$6.35 → FY27 grows | FY27E up (2030 27%-margin path) | C014, C015 |
| **Forward P/E (the swing)** | **25–30x** (de-rate, no floor) | **45–48x** (multiple holds) | **~50x** (premium held) | C029 (now ~50.5–54x) |
| Organic growth | decelerates / air-pocket | +29–31% (FY26 guide) | beats; 20–22% CAGR to 2030 | C014, C015 |
| Adj op margin | misses / compresses | 22.8–23.8% (guide) | 27% (2030) validated | C014, C032, C015 |
| Book-to-bill | <1.0 (confirmed) | ~1.0+ (re-disclosed, stable) | re-accelerates | C012 (STILL withheld at as_of) |
| Hyperscaler capex slope | 2027 digestion | holds | steepens further | C025 |

## Key model drivers (why each is uncertain)

1. **Forward multiple** — the dominant swing. At ~50-54x there is no margin of safety (richer than the seed's ~48x); a de-rate to 25–30x (bear) on flat EPS *is* the entire downside. The multiple, not EPS, does the work. (C029)
2. **Book-to-bill / orders** — THE demand driver; **still withheld at as_of** (C012), next read Q2'26 (2026-07-29). Cannot be modeled as a value, only as a scenario branch (≥1.0 re-disclosed = base/bull; <1.0 = bear).
3. **Hyperscaler capex slope** — the shared switch; VRT is the most exposed name, no floor. A 2027 digestion is the bear trigger. SAME single factor as NBIS/CEG. (C025, C023)
4. **Margin path** — tracking ahead (FY26 22.8–23.8% vs 27% 2030); currently a *support*, not a risk. (C032)

## Assumption Discipline

- Do **not** assume the ~50x multiple holds — it *is* the risk; the base case requires it to hold (~45–48x), and that is not conservative. The rally to $345 widened the gap between price and any conservative anchor.
- Do **not** treat the $15B backlog as a floor — it converts ~12–18 months and is cancellable (C024). It is visibility, not an annuity.
- Bear is **plausible, not theatrical**: 2027 capex digestion + book-to-bill confirmed <1.0 + de-rate to 25–30x on flat EPS → ~$170–230 ($182 point), **with no floor** (the $110.06 low was ~one year ago, C030).
- Bull does not require everything right, but does require FY26 beaten + 27%-margin path validated + backlog re-accelerating + premium multiple held — and at $345 the near-term bull point ($360) is only +4%.
- Treat the orders/B2B branch as the **gating uncertainty**: until Q2'26 re-discloses, the bear branch cannot be ruled out *and* the bull cannot be confirmed.
- **Refresh delta:** none of the driver logic changed; only the live anchor (price/multiple) moved richer and the skew worsened.
