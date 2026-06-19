# VRT Research Run — Layer 9: Valuation & Market

- Run date: 2026-06-19
- Method: decomposition of the deep buy-side pack; anchors = stockanalysis.com statistics (S6), FY26 guide (S1), 2030 targets (S4). All prices as of 2026-06-19, **volatile**.
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Multiples are aggregator-sourced (S6, `needs_audit`); not promoted to facts until through `../claim_ledger.csv`.
- Mapped claims: C014, C015, C029–C031

---

# Vertiv — Valuation (priced for perfection)

## 1. CURRENT SETUP (at $333.05, 2026-06-19)

| Item | Value | claim_id |
|---|---|---|
| Share price | **$333.05** | pack |
| Market cap | **~$128B** | C029 |
| Net cash | ~$0.76B | C028 |
| **Enterprise value** | **~$128B** (net cash → EV ≈ mkt cap) | C029 |
| 52-wk high / low | **$380 / $110** | C030 |
| Position vs high / low | **−12% off high / +203% off low** | C030 |

## 2. MULTIPLES (EV ≈ $128B; FY26E EPS $6.35)

| Multiple | Value | Note | claim_id |
|---|---:|---|---|
| **Forward P/E** | **~48–49x** | on FY26E EPS $6.35 — the anchor | C029 |
| Trailing P/E | ~84x | high — earnings still catching up to price | C029 |
| EV/EBITDA | ~54x | | C029 |
| P/FCF | ~56x | | C029 |
| P/S | ~11.8x | | C029 |
| **PEG** | **~1.5** | growth is fast but not cheap relative to it | C029 |

**Read:** ~48–49x forward earnings on a hardware-heavy industrial is **priced for perfection** — only justified by sustained 20%+ organic growth *and* the margin march to 27% (2030). **The bull case is already in the price.** (C029, C015)

## 3. WHY NOT AN OWNER-EARNINGS DCF (and what we use instead)

Unlike NBIS (negative FCF → EV/forward-sales triangulation), VRT is **solidly FCF-positive** (~$1.9B FY25 → ~$2.2B FY26E). So the defensible engine is a **driver → EPS × P/E → price** scenario ladder: the swing variable is the **forward multiple** the market is willing to pay on a high-beta, no-floor capex-cycle name. A 48x → 25–30x de-rate (with flat EPS) is the whole bear case; the multiple is doing the work. See `../model/scenario_model.csv`.

## 4. SCENARIOS (EPS × P/E → price)

| Scenario | Path | EPS basis | P/E | Value | claim_id |
|---|---|---|---:|---|---|
| **Bear** | 2027 capex digestion + book-to-bill confirmed <1.0; de-rate to ~25–30x on **flat** EPS; **no floor** | ~flat ($6–7) | 25–30x | **~$170–230** | C023, C030 |
| **Base** | In-line execution; multiple holds ~45–48x | FY26 ~$6.35 → FY27 grows | 45–48x | **~$340–380** | C014 |
| **Bull** | FY26 beaten, 2030 27%-margin validated, backlog re-accelerates; ~50x FY27E EPS | FY27E up | ~50x | **~$430–480** | C015 |

**The skew is unfavorable from here:** base ≈ flat-to-+14%, bull ≈ +29% to +44%, **bear ≈ −31% to −49%** — and the bear has **no floor** (the $110 low was one year ago). The asymmetry is *against* new capital at $333.

## 5. THE STREET (limited upside already priced)

- **Analyst mean target ~$377–378** (Strong Buy, ~27 analysts, high $500) ≈ **+13%** upside. (C031)
- After **+203% off the low**, the Street itself sees only ~+13% to the mean — i.e., much of the bull case is consensus, not edge.

## 6. MARGIN OF SAFETY

| Required return | Buy below | Hold/Watch | Trim/Avoid above |
|---|---|---|---|
| ~12–15%/yr (high-beta, no floor, priced-for-perfection) | ≈ **<$230–250** (restores MOS; ~bear+cushion) | ~$250–340 | **>~$340** (priced for perfection — at/above now) |

**At $333 the stock sits at/above the "priced for perfection" line.** This is not "sell" (no position is held); it is **"no margin of safety for new capital"** — which, combined with the withheld orders/B2B (binding gap, C012), caps the actionable lean at WATCH. Re-rates toward STARTER on (a) clean orders/B2B re-disclosure ≥1.0, or (b) a pullback toward ~$230–250.

---

**Bottom line for the memo:** At $333 (~$128B EV), VRT trades at **~48–49x forward / ~54x EV-EBITDA / ~56x P-FCF / PEG ~1.5** — **the bull case is already in the price**. −12% off the high but **+203% off the low**, with the Street mean (~$377) implying only **~+13%**. The scenario ladder (EPS × P/E) skews unfavorably: base flat-to-+14%, bull +29–44%, **bear −31–49% with no floor**. Valuation alone blocks a buy; the withheld orders/B2B (C012) blocks the *upgrade*. (cross-ref `../valuation.md`, `../model/`)
