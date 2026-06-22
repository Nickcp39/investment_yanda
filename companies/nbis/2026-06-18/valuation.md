# Valuation / Margin Of Safety — NBIS

Last updated: 2026-06-18

Source base: market data (SRC-018), financials (SRC-001/002). The canonical **as_of_price = $286.69** is the **last close ≤ 2026-06-18** (Yahoo adjusted close, independently re-verified vs stockanalysis + websearch at 0.0% delta — the prior "~$287.73" was an intraday read; ~$288 was rounding). Still a **fresh ATH region** (intraday 52wk high $298.80 / $298.61; price is only −4.0% off it) ahead of Nasdaq-100 inclusion 6/22. Numbers are EV/forward-sales triangulation + implied-expectations reverse check — **not** a 10-yr owner-earnings DCF (the business is too early; owner earnings are negative — see `financials/financial_quality.md`).

## Current Setup

| Item | Value | claim_id |
|---|---|---|
| **Share price (as_of close 2026-06-18)** | **$286.69** (intraday ATH $298.61 / $298.80) | C030 |
| Basic shares / diluted wtd-avg | 253.9M / 308.97M | C030 |
| Market cap | ~$72.79B basic / ~$88.58B diluted | C030 |
| Net cash | ~+$0.85B carrying (~−$0.76B principal) | C009 |
| **Enterprise value** | **~$71.9B basic / ~$87.9B diluted** | C030 |
| Holder cost basis | ~$190–195 (entry ~May 2026), +~50% | user |

## Why not owner-earnings DCF

Owner earnings are **negative** (capex ~7× revenue, FCF ≈ −$3.7B FY2025, C010). Consensus shows FCF deeply negative through ≥FY2028 (≈ −$17B to −$20B/yr). So valuation hangs entirely on **future** revenue scale and a **terminal multiple** — which means it is a bet on execution + multiple, with little present margin of safety. That fact alone is the most important valuation conclusion.

## Multiples (EV ≈ $72.5B)

| Multiple | Value | Note |
|---|---:|---|
| EV/Rev FY25 actual | ~136x | noise at this growth |
| EV/Rev TTM | ~82x | noise |
| EV/Rev FY26E ($3.44B) | ~21x | |
| EV/Rev FY27E (~$11.2B, wide range $4–11B) | ~6.4x | **FY27 is the swing — consensus itself spans $4–11B** |
| EV/ARR current ($1.9B) | ~38x | |
| EV/ARR on FY26-exit $7–9B | ~8–10x | brackets a *mature* multiple — i.e., priced as if exit-ARR already achieved |
| **EV/RPO (Q1'26 RPO $33.6B)** | **~2.2×** | RPO = audited contracted revenue; EV ≈ 2× the *entire* contracted book. Note "$46–50B backlog" is deal ceilings, not RPO (C044/C045) |

## Implied Expectations (the key check)

At EV ≈ $72.5B, applying a *mature* neocloud multiple (~5–7x EV/sales; CoreWeave ~7.7x fwd, hyperscalers ~9–10x) **today**, the market is paying for **~$10–14B of steady-state revenue** — a level NBIS doesn't reach until ~2027–28. On EV/ARR, $72.5B at 8–10x = **$7–9B ARR**, exactly management's YE2026 exit-ARR guide. 

**Translation: the stock already capitalizes the YE2026 ARR target (a ~540% jump in one year) as if achieved, at a mature multiple. It is priced for near-flawless execution of the Meta/Microsoft backlog.** There is little room for slippage and essentially no margin of safety at $288.

## Scenarios (EV/forward-sales triangulation, horizon ~end-2028)

Rough, assumption-driven. Anchored on FY2028 revenue × terminal EV/sales, vs current EV $72.5B (price ~$288).

| Scenario | FY2028 rev | Terminal EV/Sales | Implied EV | Implied price* | vs $288 | Drivers |
|---|---:|---:|---:|---:|---:|---|
| **Bear** | ~$8B | 4x | ~$32B | ~$120–140 | **−50% to −58%** | churn/clawback (path B), commoditization, capex air-pocket forces dilution; FY27 conversion at low end |
| **Base** | ~$15–17B | 5–6x | ~$85–100B | ~$330–400 | **+15% to +40%** (~6–14%/yr) | backlog converts on plan; demand breadth improves; capex/rev starts normalizing |
| **Bull** | ~$21B+ | 7x | ~$150B | ~$560–600 | **~+95%+** | flawless execution, holds premium multiple, 3rd anchor signs, FCF inflects sooner |

\* Price ≈ implied EV ÷ ~255–260M shares, ignoring further dilution (which would lower bear/base more). Heavily simplified.

## Margin Of Safety

| Required return | Buy below | Hold | Trim/Avoid above |
|---|---|---|---|
| ~12–15%/yr (high uncertainty, capital-intensive, controlled co.) | ≈ <$150 (≈ bear EV with cushion) | ~$150–250 | **>~$280** (priced for perfection) |

**At $288 the stock sits above the "priced for perfection" line.** The skew is unfavorable: bear ≈ −50%+, base ≈ low-teens %/yr, and the base case *requires* the backlog to convert without the inversion paths firing. This does not mean "sell" — it means new capital has no margin of safety, and the asymmetric downside the old brief flagged has, if anything, grown with the price.

## Valuation discipline notes

- A great buildout story can still be a poor *forward* investment at 8–10x exit-ARR with negative FCF.
- The terminal multiple is doing all the work — do not let a 7x "mature" assumption rescue the present.
- Uncertainty is high (FY27 revenue consensus spans $4–11B; take-or-pay vs terminable unresolved) → required MOS rises, and there is none at $288.

→ Position implication for the holder is written in `memo-v1.md` (hold/trim/add) and `monitor.md` (triggers).
