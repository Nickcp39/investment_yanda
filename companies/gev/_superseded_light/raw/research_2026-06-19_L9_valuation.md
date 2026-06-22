# GEV Research Run — Layer 9: Valuation & the Clean-Multiple Bridge

- Run date: 2026-06-19
- Method: evidence-pack decomposition; market data S6 (stockanalysis.com 2026-06-18); forward anchors from S3 guide. All multiples derived from EV ≈ $292B and the 2026 *adjusted* guide.
- Status: ⚠️ UNAUDITED RESEARCH DIGEST. Not facts until promoted via `../claim_ledger.csv` → `../facts.md`.

---

## 1. THE SETUP

| Item | Value | Source |
|---|---:|---|
| Share price (2026-06-19) | **$1,109.73** | locked |
| Market cap | **~$298B** | S6 |
| Enterprise value | **~$292B** | S6 (small net cash; cash $10.17B offset by Prolec debt) |
| 52-wk context | ~−6% off ATH | S6 |

## 2. WHY SCREENER MULTIPLES ARE WRONG (carry the one-offs through)

[SECONDARY] S6 headline multiples are **distorted** by the same three one-offs flagged in L3-4 raw:
- **Trailing P/E ~32**, **EV/EBITDA ~85x**, **fwd P/E ~60** — all inflated by the **$2.9B FY2025 tax release + ~$4.5B Q1'26 Prolec/Proficy M&A gains** (and the EBITDA denominator is distorted by advance-payment timing).
- A screener reading TTM net income ~$9.4B is **double-counting** one-offs. **Discard trailing GAAP multiples entirely.**

## 3. THE CLEAN-MULTIPLE BRIDGE (the decision-relevant valuation)

Strip the one-offs; value on the **2026 adjusted guide**:

| Clean multiple | Calc | Value |
|---|---|---:|
| Adj EBITDA (2026 guide) | $44.5–45.5B × 12–14% | **≈ $5.7–6.4B** |
| **EV / fwd adj-EBITDA** | $292B ÷ $5.7–6.4B | **≈ 46–51x** |
| FCF (2026 guide) | given | $6.5–7.5B |
| **EV / FCF** | $292B ÷ $6.5–7.5B | **≈ 39–45x** |
| EV / **normalized** FCF | stripping advance-payment timing | **≈ 50x+** |

**Peer check:** Siemens Energy trades ~**39x** EV/EBITDA. **GEV carries a premium even after adjusting for one-offs.** The market is paying ~46–51x clean forward EBITDA — i.e., pricing **both** (a) the toll-booth as *permanent* **and** (b) the 2028 22%/22% segment margins as *landed*.

> **The valuation conclusion in one line:** at $1,109 GEV prices the cyclical equipment premium as permanent rent and the 2028 targets as already achieved, at a premium to a credible peer — leaving no margin of safety for the 2027-capex / Wind / cyclical risks.

## 4. SCENARIOS (triangulation → normalized EBITDA × EV/EBITDA → price)

Anchored on a *normalized* EBITDA × a cycle-appropriate multiple, vs current EV ~$292B / price $1,109.73. See `../model/scenario_model.csv`.

| Scenario | Path | Normalized EBITDA | Multiple | Implied value | vs $1,109 |
|---|---|---:|---:|---:|---:|
| **Bear** | 2027 capex digests, GT premium fades, Wind drags | ~$5B | ~25x | **~$600–700** | **−40%** |
| **Base** | targets ~met; 2028 rev $52B, ~20% EBITDA $10B+ | ~$10B | ~30x | **~flat** ($1,100-ish) | ~0% over 2–3 yr |
| **Bull** | sold-out-through-2030 + SMR/BWRX-300 + Electrification 22% sustains re-rate | $10B+ | higher | **$1,400+** | +25%+ |

## 5. MARGIN OF SAFETY

At ~−6% off ATH:
- **Bear ≈ −40%**, **Base ≈ flat**, **Bull ≈ +25%+.** The skew is **unfavorable** — thin margin of safety, full downside if 2027 capex digests.
- The **base case *requires* the bottleneck rent to be durable AND the 2028 margins to land** — both already in the price.
- **Buy discipline:** STARTER only **sub-~$950** (≈ 25x normalized, a level that pays you for the cyclical/Wind/2027 risk) **or** on confirmation that 2029–30 slots convert reservations → firm orders (durability proven, not just a booking peak).

---

## Analyst comments (NOT facts)

- The services annuity ($87B RPO) is the part worth paying *up* for; the equipment premium is not. The mistake the market is making (and the one to avoid) is paying a *permanent-rent* multiple for a *cyclical equipment peak*.
- Owner-earnings DCF is not the right primary tool here (heavy one-off distortion + cyclical equipment pricing) → scenarios use normalized-EBITDA × multiple, consistent with `../model/`.
- **Open gap:** a clean normalized-FCF bridge stripping advance-payment timing would tighten the EV/FCF read — flagged in `../facts.md`.
