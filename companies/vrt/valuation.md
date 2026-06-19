# Valuation / Margin Of Safety — VRT

Last updated: 2026-06-19

Source base: market data (S6, aggregator, `needs_audit`), FY26 guide (S1), 2030 targets (S4). All prices as of 2026-06-19, **volatile**. Engine = **EPS × forward P/E** ladder (VRT is FCF-positive; the swing variable is the forward multiple) — see `model/scenario_model.csv` / `model/model_assumptions.md`.

## Current Setup (at $333.05)

| Item | Value | claim_id |
|---|---|---|
| Share price | $333.05 | pack |
| Market cap | ~$128B | C029 |
| Net cash | ~$0.76B | C028 |
| **Enterprise value** | **~$128B** (net cash → EV ≈ mkt cap) | C029 |
| 52-wk high / low | $380 / $110 | C030 |
| Position vs high / low | **−12% off high / +203% off low** | C030 |

## Multiples (EV ≈ $128B; FY26E EPS $6.35)

| Multiple | Value | Note | claim_id |
|---|---:|---|---|
| **Forward P/E** | **~48–49x** | on FY26E EPS $6.35 — the anchor | C029 |
| Trailing P/E | ~84x | earnings still catching up to price | C029 |
| EV/EBITDA | ~54x | | C029 |
| P/FCF | ~56x | | C029 |
| P/S | ~11.8x | | C029 |
| **PEG** | **~1.5** | fast growth, but not cheap relative to it | C029 |

**Read: priced for perfection.** ~48–49x forward earnings on a hardware-heavy industrial is only justified by sustained 20%+ organic growth *and* the margin march to 27% (2030). **The bull case is already in the price.** (C029, C015)

## Why an EPS × P/E ladder (not a DCF)

VRT is **solidly FCF-positive** (~$1.9B FY25 → ~$2.2B FY26E), so — unlike NBIS (negative FCF → EV/forward-sales triangulation) — the defensible engine is **EPS × forward multiple**. The whole bear case is a **de-rate** (48x → 25–30x) on roughly flat EPS: the *multiple* does the work on a high-beta, no-floor capex-cycle name. That is the single most important valuation fact.

## Scenarios (EPS × P/E → price)

Anchored on near-term EPS × a forward multiple, vs current price $333. See `model/scenario_model.csv`.

| Scenario | Path | EPS basis | P/E | Value | vs $333 |
|---|---|---|---:|---|---:|
| **Bear** | 2027 capex digestion + book-to-bill confirmed <1.0; de-rate ~25–30x on **flat** EPS; **no floor** | ~$6–7 | 25–30x | **~$170–230** | **−31% to −49%** |
| **Base** | In-line FY26 execution; multiple holds ~45–48x | ~$6.35 → FY27 grows | 45–48x | **~$340–380** | **+2% to +14%** |
| **Bull** | FY26 beaten, 2030 27%-margin validated, backlog re-accelerates; ~50x FY27E EPS | FY27E up | ~50x | **~$430–480** | **+29% to +44%** |

\* Bear has **no floor** — the $110 52-wk low was one year ago. The skew is unfavorable for new capital: base ≈ flat-to-+14%, bull ≈ +29–44%, **bear ≈ −31 to −49%**.

## The Street (limited upside already priced)

- **Analyst mean target ~$377–378** (Strong Buy, ~27 analysts, high $500) ≈ **+13%** upside. (C031)
- After **+203% off the low**, even the Street sees only ~+13% to the mean — i.e., much of the bull case is *consensus*, not edge.

## Margin Of Safety

| Required return | Buy below | Hold/Watch | Trim/Avoid above |
|---|---|---|---|
| ~12–15%/yr (high-beta, no floor, priced-for-perfection) | ≈ **<$230–250** (restores MOS; ~bear + cushion) | ~$250–340 | **>~$340** (priced for perfection — at/above now) |

**At $333 the stock sits at/above the "priced for perfection" line.** This is not "sell" (no position is held); it is **"no margin of safety for new capital."** Combined with the withheld orders/B2B (binding gap, C012), it caps the actionable lean at **WATCH**. Re-rates toward STARTER on (a) clean orders/B2B re-disclosure ≥1.0, or (b) a pullback toward ~$230–250.

## Valuation discipline notes

- A great franchise can still be a poor *forward* investment at ~48x with **no contracted floor** under a cyclical demand base.
- The forward multiple is doing all the work — do not assume ~48x holds; the base case *requires* it, and that is not conservative.
- Uncertainty is asymmetric and *informational*: the orders/B2B gauge is withheld (C012), so the bear branch cannot be ruled out nor the bull confirmed until Q2'26 re-discloses → required MOS rises, and there is none at $333.

→ Position implication is written in `memo-v1.md` (WATCH; STARTER on pullback / re-disclosure) and `monitor.md` (triggers).
