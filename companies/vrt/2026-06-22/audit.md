# VRT Audit / Quality Gate (pre-IC adversarial QA)

Last updated: **2026-06-22** (refreshed from 2026-06-19 seed)
Auditor stance: **对抗性找漏洞** (adversarial hole-punching). Independent quality gate between the analysis modules and the IC Panel. It does not add facts or pick a side; it tests whether the evidence is sound, modules are self-consistent, where the gaps are, and the highest allowable verdict.

Inputs audited: `facts.md`, `source_register.md` (S1–S11), `claim_ledger.csv` (35 rows), the 6-module artifacts (financial_quality / business_model / value_chain_map / moat_map / bottleneck_map / operator_underwriting / inversion_map / valuation), `model/{scenario_model.csv, model_assumptions.md}`, `memo-v1.md`, `monitor.md`, `freshness.json` + `freshness_check.json` (PASS).

---

## 0. One-line audit conclusion

Evidence engineering quality is **high**: 35 claims each carry a source_id, the core financials trace to primary A1/A2 (Q1'26 8-K/release S1, FY25 release S3, IC deck S4), the live market fields carry ≥2 independent sources cross-checked in `freshness.json` (and the mechanical gate **PASSES, exit 0**), and `scenario_model` arithmetic ties line by line at the new $345.05. **But one finding dominates + two secondary items remain**: ① the **"backlog silence"** — VRT withdrew headline quarterly orders / book-to-bill / backlog in Q1'26 after a +252%/2.9x Q4 and **has STILL not restored it as of as_of** (C012, UNVERIFIED); the cleanest demand gauge to underwrite kill (a) is missing exactly when it matters; ② valuation multiples + Street target are aggregator-sourced (`needs_audit`); ③ the point-estimate / range display gap (carried forward, harmless). **Ceiling = WATCH**, and the actionable lean is **one notch below the completeness band** — not because of missing modules, but because **the cleanest demand signal is off AND the price (~50-54x at $345) has no margin of safety** (worse than the seed's ~48x after the +3.6% move).

---

## 1. Source coverage

Every module's core claims trace to a facts.md source_id; no naked load-bearing claim. The live fields (price/mcap/52wk/shares/target) are the strongest-covered (≥2 independent + mechanical re-verify). The one soft spot: the full multiple set (C029) + Street target (C031) come from aggregators (S6, `needs_audit`) — not yet tied to a one-hand 10-Q balance sheet. Conclusion direction (priced for perfection) is robust at any basis. **Pass.**

## 2. No naked claims

No load-bearing claim lacks a source_id or evidence tag. The most sensitive item (C012, withheld orders) is handled as a textbook "known unknown" — **never used as EVIDENCE**, instead carried as the kill-(a) YELLOW trigger + the #1 open question across inversion/monitor/operator/financial_quality/research_status. Inferred items (C023 ~75% concentration, C024 cancellable backlog, C033 owns-integration/supplies-into-component) are tagged `inferred`. Aggregator multiples tagged `needs_audit`. **Pass.**

## 3. Cross-module consistency (refreshed numbers)

- **(a) backlog / orders description** — ✅ fully consistent: FY25 backlog $15.0B(+109%), Q4 B2B ~2.9x, Q4 orders +252%, and Q1'26 **WITHHELD (still dark at as_of)** are written identically everywhere; no module treats "orders up YoY" as ≥1.0 evidence.
- **(b) fwd P/E basis** — ⚠ display gap carried forward and now refreshed: **~50.5x** (stockanalysis / ~$6.8 adj-EPS denominator) vs **~54x** ($345.05 / FY26E $6.35 as-reported). Both say "priced for perfection." Noted in valuation.md + scenario_model.csv. Non-substantive.
- **(c) point estimate vs range** — ⚠ carried forward: base point $292 (static FY26E ×46) vs range $340–380 (FY27 EPS grown into 45–48x). Annotated in scenario_model.csv notes. Non-substantive.
- All organic-vs-total and adj-vs-GAAP conventions consistent.

## 4. Stale facts (the headline of THIS refresh)

This is the refresh's core check. **All LIVE data is current to as_of 2026-06-22** and mechanically verified:
- Price $333.05 (seed, 06-18) → **$345.05 (06-22)**; mcap ~$128B → ~$132.5B; 52wk $380/$110 → $379.94/$110.06; fwd P/E ~48x → ~50.5–54x; Street +13% → +9.6%. All re-pulled, ≥2 sources, gate PASS.
- Latest hard quarter correctly held at **Q1'26** (Q2'26 = 2026-07-29 not yet public) — the run does NOT fabricate a Q2 print. The T6 WARN (guidance 61d old) is **expected and correct**, not a staleness error: this IS the latest authoritative guidance.
- New events folded in: **ThermoKey closed 06-12** (C034), **$0.0625/qtr dividend** (C035) — both reflected in operator/business_model/financial_quality.
- **No stale price/quarter carried forward** — the explicit failure mode the user flagged (INC-001). The seed's $333.05 appears ONLY as a documented "what changed" delta, never as a current fact.

## 5. C-pollution

**Zero.** No KOL/video sources. S8 ("Backlog Silence," Seeking Alpha, B2) used only to corroborate that the withdrawal was independently noticed — never as the orders number. **Pass.**

## 6. Math / model (re-computed at $345.05)

| Check | Model value | Re-computed | Verdict |
|---|---|---|---|
| Bear = 6.50×28 | 182 | 182.0 | ✅ |
| Base = 6.35×46 | 292 | 292.1 | ✅ |
| Bull = 7.20×50 | 360 | 360.0 | ✅ |
| current fwd P/E = 345.05/6.35 | 54.3 | 54.3 | ✅ |
| Street upside = 378/345.05−1 | +9.5% | +9.5% | ✅ |
| Off low = 345.05/110.06−1 | +213% | +213.5% | ✅ |
| Off high = 345.05/379.94−1 | −9.2% | −9.2% | ✅ |
| Bear vs current = 182/345.05−1 | −47% | −47.3% | ✅ |
| mcap = 384.11M × 345.05 | $132.5B | $132.5B | ✅ |

All arithmetic ties; the freshness validator independently re-derived the market-cap identity (T3, 0.03%) and distance-from-high (T4, 0.0pt gap). **Pass.**

## 7. Missing primary sources

| Gap | Status | Impact |
|---|---|---|
| 🔴 Verified orders / book-to-bill / backlog (WITHHELD, still dark at as_of) | Company choice (C012) | **🔴 BINDING — the #1 gap.** Only resolution = Q2'26 (2026-07-29). |
| Multiples & Street target one-hand cross-check (C029/C031) | Aggregator S6, `needs_audit` | 🟠 direction stable, precision pending |
| Net-cash composition (gross cash vs debt) | S6 ~$0.76B | 🟡 EV≈mcap premise; confirm vs 10-Q (C028) |
| Segment split (power/thermal/services) | Not pulled | 🟡 content-per-rack decomposition (C016) |
| FY2025 10-K full text / full transcript series | Used release + single call | 🟠 full-year backlog, concentration, segment mix |

## 8. Management un-verified claims

Handled well; observable behaviors (actual revenue/margin/FCF, net cash, the closed ThermoKey deal, the declared dividend) rather than empty promises. The one forward claim (FY26 guide + 2030 targets) is verified to S1/S4 and credibility-weighted by the beat-raise record, with the operator correctly flagged as **un-stress-tested by a down-cycle**. The key "un-verified" is not a promise but the **withdrawn orders data series** — management chose not to disclose it and a quarter later still hasn't. **Pass.**

## 9. Valuation assumptions too aggressive / too loose

Assumptions are conservative and honest; the engine (EPS × forward P/E, because VRT is FCF-positive) is correctly chosen. base explicitly treats "~50x holds" as the risk, not a default; bear is plausible (de-rate to 28x on flat EPS → $182, no floor) not theatrical. **The refresh makes the price-side stricter, not looser:** the +3.6% move pushed price above the perfection line and shrank the Street upside to +9.6%. The real downside tail (signal-dark 2027 digestion) is still not fully pressed into the bear → true MOS only worse. **No "raise assumptions to manufacture a buy" anywhere.**

## 10. Risks not quantified

Identification complete (D/A/B/C paths + risk-type table); kill criteria are observable and thresholded. Three tail probabilities remain un-quantified (2027 capex digestion magnitude, signal-blackout delay cost, system-layer commoditization speed) — all entangled with C012 (the withheld signal). That entanglement is itself the core WATCH reason, not a blind spot.

## 11. Completeness % + Verdict Ceiling

### 11.1 Completeness weighting (fact / understanding / decision lines, conservative)

| Line | Weight | Score | Note |
|---|---:|---:|---|
| A. Fact line | 35% | 24/35 (69%) | core financials A1/A2 + live fields ≥2 src verified + gate PASS; **−** C012 withheld (structural), aggregator multiples needs_audit, segment not split |
| B. Understanding line | 35% | 27/35 (77%) | 5 modules complete & high-quality, LEAD answered; **−** design-authority/share metrics qualitative, operator un-stress-tested |
| C. Decision line | 30% | 19/30 (63%) | EPS×P/E ladder + 3 scenarios + MOS + monitor + freshness gate; **−** base point pinned on the unavailable orders variable, multiples needs_audit, single parallel pass |

**Weighted ≈ 24+27+19 = ~70/100.** (Slightly below the seed's 72 — this is a single parallel refresh pass, not a multi-pass independent build; held conservative per honesty rule.)

### 11.2 Verdict Ceiling

1. Completeness ~70% → **STARTER band** (60–80%).
2. Missing-module hard rules → **all cleared** (valuation/inversion/operator all present; zero C-pollution; business model understood).
3. Two substantive findings pull it down:
   - **(i) demand-signal blackout (C012)** — cleanest gauge off, still dark at as_of; on a no-floor/highest-beta name, bear can't be ruled out nor bull confirmed pre-Q2'26 → pushes the actionable lean below STARTER.
   - **(ii) ~50-54x, no margin of safety** — +213% off low, only +9.6% to Street; bull priced; M6 caps first. **The +3.6% move worsened this vs the seed.**
4. **Take the lower → Verdict Ceiling = `WATCH`.**

### Ceiling rationale

By completeness (~70%) this would be **STARTER**; the two substantive findings hold it at **WATCH** and push the lean a notch below STARTER. This is a *"research is solid, the conclusion is good-business-but-(i)-can't-see-demand-(ii)-too-expensive"* WATCH, not a *"not researched yet"* WATCH. STARTER unlocks on exactly two things: (a) Q2'26 clean re-disclosure of orders/B2B ≥1.0 at a non-perfection price, or (b) a pullback to ~$230–250. **Note vs the seed: the price-side constraint is now sharper (richer multiple, thinner Street upside).**

---

## Exposed gap list (priority) + reflow

| # | Gap | Priority | Action |
|---|---|---|---|
| G1 | 🔴 Orders / B2B / backlog (WITHHELD, C012) | P0 (binding, can't self-pull) | Wait for Q2'26 (2026-07-29) |
| G2 | Multiples & Street target one-hand audit (C029/C031) | P0 (fast) | Cross-check vs 10-Q balance sheet + clean consensus |
| G3 | scenario display alignment (point vs range, 50.5x vs 54x) | P1 (zero-cost) | Annotated in scenario_model notes |
| G4 | Net-cash composition (C028) | P1 | Confirm vs 10-Q |
| G5 | Segment split (C016) | P2 | Pull from 10-K/10-Q |
| G6 | FY25 10-K full + transcript series | P2 | Primary backlog/concentration/segment |
| G7 | 2027 capex digestion tail quantification (path D) | P2 | Press the bear downside tail |

## To IC — clears, but IC must address

Clears to IC Panel with verdict ceiling **WATCH**; IC may not exceed STARTER unless Q2'26 cleanly re-discloses orders/B2B ≥1.0 **or** price falls to ~$230–250. IC must address: ① signal-blackout (the hardest, still-dark a quarter later); ② price (~50-54x, +9.6% to Street — sharper than the seed); ③ A×D compounding; ④ moat protects share not cycle; ⑤ operator un-stress-tested + selective disclosure; ⑥ single-factor TIE with NBIS/CEG (portfolio-level concentration). Primary anchors: point estimates **$182/$292/$360 (+FY27E $430–480)**.
