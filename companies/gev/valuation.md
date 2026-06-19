# Valuation / Margin Of Safety — GEV

Last updated: 2026-06-19

Source base: L9 raw, S6 (market data 2026-06-18), S3 (2026 guide). ⚠️ Headline screener multiples are **distorted by one-offs** — this analysis uses the **clean forward bridge** (see `financials/financial_quality.md`). Scenarios are **normalized-EBITDA × EV/EBITDA**, not an owner-earnings DCF (heavy one-off distortion + cyclical equipment pricing make a clean DCF unreliable).

## Current Setup

| Item | Value | claim_id |
|---|---|---|
| Share price (2026-06-19) | **$1,109.73** | locked |
| Market cap | ~$298B | C032 |
| Net cash / debt | small net cash (cash $10.17B offset by Prolec debt) | C009 |
| **Enterprise value** | **~$292B** | C032 |
| 52-wk context | ~−6% off ATH | C032 |

## ⚠️ Why screener multiples are wrong

| Headline (S6) | Value | Distortion |
|---|---:|---|
| Trailing P/E | ~32 | inflated by $2.9B tax release + ~$4.5B M&A gains |
| **EV/EBITDA** | **~85x** | EBITDA distorted by advance-payment timing + one-offs |
| Fwd P/E | ~60 | same one-off base |

Screener TTM net income ~$9.4B **double-counts** the one-offs (C008). **Discard trailing GAAP.** Use the clean forward bridge below.

## The Clean-Multiple Bridge (the decision-relevant valuation)

Value on the **2026 adjusted guide** (C010):

| Clean multiple | Calc | Value |
|---|---|---:|
| Adj EBITDA (2026 guide) | $44.5–45.5B × 12–14% | **≈ $5.7–6.4B** |
| **EV / fwd adj-EBITDA** | $292B ÷ $5.7–6.4B | **≈ 46–51x** |
| EV / FCF (2026 guide) | $292B ÷ $6.5–7.5B | **≈ 39–45x** |
| EV / **normalized** FCF | stripping advance-payment timing | **≈ 50x+** |
| **Peer: Siemens Energy** | — | **~39x EV/EBITDA** |

**GEV carries a premium to Siemens even after adjusting one-offs.** At ~46–51x clean forward EBITDA the market prices **both** (a) the toll-booth as *permanent* **and** (b) the 2028 22%/22% segment margins as *already landed*. (C033)

## Owner Earnings Bridge (why it's not the primary tool)

| Item | Note |
|---|---|
| FY2025 net income | $4.9B — **not usable** (~$2.9B tax release) |
| FY2025 operating income | $1.39B — cleaner, but pre-ramp |
| Q1'26 FCF | $4.8B — **flattered** ~$5.3B by advances |
| Maintenance vs growth capex | within $10B 2025–28 program; mostly growth |
| **Owner earnings** | **not cleanly estimable today** — one-off distortion + cyclical equipment pricing → use normalized-EBITDA scenarios instead |

## Scenarios (normalized EBITDA × EV/EBITDA → price)

Anchored on a *normalized* EBITDA × a cycle-appropriate multiple, vs current ~$292B EV / $1,109.73. See `model/scenario_model.csv`.

| Scenario | Path | Norm. EBITDA | Multiple | Implied price | vs $1,109 |
|---|---|---:|---:|---:|---:|
| **Bear** | 2027 capex digests, GT premium fades, Wind drags | ~$5B | ~25x | **~$600–700** | **−40%** |
| **Base** | targets ~met; 2028 rev $52B, ~20% EBITDA $10B+ | ~$10B | ~30x | **~flat** (~$1,100) | ~0% / 2–3 yr |
| **Bull** | sold-out-through-2030 + SMR/BWRX-300 + Electrification 22% sustains re-rate | $10B+ | higher | **$1,400+** | +25%+ |

## Margin Of Safety

| Required return | Buy below (STARTER) | Hold / no-add | Avoid / overpay above |
|---|---|---|---|
| ~10–12%/yr (cyclical industrial w/ moat) | **≈ <$950** (~25x normalized — pays you for cyclical/Wind/2027 risk) | ~$950–1,150 | **>~$1,150** (priced for permanent rent) |

**At $1,109 (~−6% off ATH) the skew is unfavorable:** bear ≈ −40%, base ≈ flat, bull ≈ +25%+. Thin margin of safety; **full downside if the 2027 capex cycle digests.** The base case *requires* the bottleneck rent to be durable **and** the 2028 margins to land — both already in the price. This is **not "avoid forever"** — the durable core (oligopoly + services annuity) is worth owning at the right price; the current price overpays for the cyclical equipment layer.

## Valuation Discipline

- **The services annuity ($87B RPO) is worth paying *up* for; the equipment premium is not.** The market's error is paying a *permanent-rent* multiple for a *cyclical equipment peak*.
- Do not let business quality (genuinely among the best in industrials) rescue a full entry price — *a great company is not a great investment at any price.*
- Uncertainty (cyclical pricing + Wind + one-off-distorted base) raises the required margin of safety → there is none at $1,109.
- **Buy discipline:** STARTER only **sub-~$950**, or on **2029–30 slots converting reservations → firm orders** (durability proven, not a booking peak).

→ Position implication in `memo-v1.md`; triggers in `monitor.md`.
