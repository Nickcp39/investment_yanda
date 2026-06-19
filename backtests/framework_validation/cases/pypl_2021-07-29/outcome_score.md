# Outcome Score — PYPL (PayPal Holdings), as-of 2021-07-29

> SCORER output. Uses post-2021-07-29 realized data (allowed for scoring only). The locked
> blind Runner `decision_card.json` / `decision_card.md` were NOT modified. Grades against
> `PROTOCOL.md §6` (TRAP row) + `WEIGHTING_HARNESS.md §7`.
>
> Sealed expectation (verified): **TRAP** — `false_cheap_value_trap` anchor (key var: take-rate
> decline / competition / eBay migration), expected band `REJECT..WATCH`, expected dominant
> `M4/M5`, `veto_expected = false` (per Round-1 matrix the matrix does not pre-commit a hard veto;
> the trap is priced via M4/M5/M6, not a structural-decline kill).

---

## 1. Realized outcome (entry $283.17, 2021-07-29)

PayPal paid **no dividend** over the entire window, so PYPL price return = total return. SPY/QQQ
figures use adjusted close (dividends reinvested) where both endpoints were available; the
to-2026 SPY/QQQ figures use raw current close vs as-of raw close and therefore *understate* the
benchmark total return by the few % of dividends collected since — which does not change any
conclusion.

| Horizon | Date | PYPL close | PYPL TR | SPY TR | QQQ TR | PYPL − SPY | PYPL − QQQ |
|---|---|---:|---:|---:|---:|---:|---:|
| Entry | 2021-07-29 | **$283.17** | — | — | — | — | — |
| +12mo | 2022-07-29 | $86.53 | **−69.4%** | −5.2% | −13.4% | **−64 pp** | **−56 pp** |
| +24mo | 2023-07-28 | $73.98 | **−73.9%** | +6.9% | +6.0% | **−81 pp** | **−80 pp** |
| +36mo | 2024-07-29 | $58.29 | **−79.4%** | +29.1% | +28.8% | **−108 pp** | **−108 pp** |
| to ~now | 2026-06-18 | ~$42.51 | **−85.0%** | ~+70% (px) / ~+80% TR | ~+102% (px) / ~+108% TR | **~−155 pp** | **~−190 pp** |

**Worst drawdown:** entry $283.17 → trailing-52-week / cycle low **$38.46** (reached within the
past year, i.e. 2025→early-2026) = **−86.4%**. Measured from the July-2021 all-time high (~$308–310
close) the peak-to-trough was **~−87%**. PYPL never recovered: it broke the 2022 lows ($66), the
2023 lows ($50s), the 2024 lows, and kept grinding to the high-$30s; current ~$42 is still **−85%**
from the as-of price and ~5.4× below entry.

Sources: Yahoo Finance daily chart API (PYPL/SPY/QQQ closes & adj-closes at each anchor date);
stockanalysis.com/stocks/pypl (current $42.51 on 2026-06-18; 52-week range $38.46–$79.50);
corroborating web quotes for current SPY ~$746.74 / QQQ ~$740.62 (2026-06-18). As-of price $283.17
matches the case `asof_2021-07-29_pypl_quotes.csv`.

**Mechanical label (realized): `TRAP` — confirmed, severe.** Expensive decelerating-growth
de-rating exactly as sealed. PYPL lost ~85% while both broad benchmarks roughly doubled; the gap
to the index (~150–190 pp) is among the widest in the Round-1 matrix. This is a textbook
overpay-at-the-high / multiple-collapse trap (the ~60x-forward, ~$333B cap compressed as growth
normalized toward the high-teens and below, the eBay roll-off and competition pressured the
take-rate, and the 750M-account / 2025 targets were later abandoned — all the M4/M5 kill-criteria
fired).

---

## 2. Grade vs PROTOCOL §6 (TRAP row)

PROTOCOL §6 TRAP row: **PASS** = `REJECT`, or `WATCH` with correct structural-decline diagnosis.
Per the task instruction, because the Runner *relabeled* the mechanism (expensive-quality-compounder
**de-rating**, not false-cheap), the test is whether **the de-rating/overpay mechanism it named was
the correct one** — and it was, precisely.

### Axis 1 — Outcome/size grade: **PASS**

- New-money verdict **WATCH / 0%**, existing **TRIM**, max-size ceiling **5%**, buy-below **$200**.
- Against a realized −85% TRAP, WATCH/0% new money is the correct protective call, and it is **not**
  the "WATCH / 0% with avoid-framing that is actually right by accident" failure — the Runner
  carried an explicit, mechanism-correct buy plan (initiate only ≤~$200 **and** growth stabilizing).
  Even the buy-below $200 would have been hit within months and kept falling, but the *gate* (price
  compression **plus** ex-eBay growth stabilizing) was never jointly satisfied on the way down, so a
  disciplined reader following this card does not catch a falling knife. This clears PASS for a TRAP.
- It is materially stronger than a bare WATCH: the existing-holder **TRIM-toward-≤5%** instruction
  protected incumbents from the bulk of the −85%, and the kill-criteria list pre-named every actual
  failure (ex-eBay decel through the high-teens; take-rate compression; margin contraction + weak FCF
  conversion; further premium M&A; NNA/engagement deterioration; multiple getting more stretched).

### Mechanism / relabel credit: **correct, full credit**

- Sealed anchor was `false_cheap_value_trap`. The Runner explicitly rejected that label as an
  ill-fit ("PYPL at ~60x is the opposite of optically CHEAP") and substituted
  `expensive_quality_compounder_derating_risk`, routing the trap through **M5 −2 (de-rating /
  overpay cap)** + **M6 −1 (no MOS at near-ATH)** + **M4 −1 (flattered EPS, contracting non-GAAP
  margin, −33% FCF, decel)** rather than a fake structural-decline veto. **This is the correct
  mechanism** — the realized loss was a multiple de-rate + growth-quality normalization on an
  overpriced compounder, *not* a low-P/E false-cheap trap and *not* (in 2021-2024) a bankruptcy /
  structural-decline death. The relabel improved the diagnosis over the sealed anchor and still
  landed the protective size. Full mechanism credit.

### Dominant module: got **M5 (−2) + M6 (−1) + M4 (−1)** · expected **M4 / M5** → **match**

- The binding constraint was explicitly **PRICE** (M6) enforced by the **M5 −2 de-rating cap**, with
  **M4 −1** supplying the growth-quality erosion evidence. Expected dominant per matrix = M4/M5.
  The card's dominant trio = M5 + M6(price) + M4 → **matches the expected M4/M5 emphasis** (M6-price
  is the correct co-driver for an overpay trap). No dominance error.

### Veto: fired **none (hard)** · expected **none (hard)** → **match**

- `veto_expected = false`: the Round-1 matrix prices this trap via M4/M5/M6, not via a hard
  structural-decline kill. The Runner fired **no hard veto** and was explicit about why (TPV +40%, net
  cash, survivable — the WEIGHTING_HARNESS §6 veto conditions were genuinely not met as of 2021-07-29).
  Instead it used a **strong −2 soft cap on NEW money**. This is exactly right and well-reasoned: a
  hard structural-decline veto in mid-2021 would have been a *lookahead* (the structural decline
  thesis only became defensible in 2022+). **Match — no false veto, no missed veto.**

### Size-distance: **0** (within correct band)

- Correct band for a TRAP = `REJECT..WATCH`. Card = **WATCH / 0% new money** → squarely inside the
  band. `size_distance_error = 0`.

### Reasoning score: **sound**

- Correct key variable (price/de-rating on decelerating growth; ex-eBay roll-off; take-rate vs
  Square/Cash App/Apple Pay/BNPL competition — i.e. the matrix's own key variables), correct module
  dominance (M4/M5/M6-price), no lookahead. The dissent honestly flags the label substitution and
  states the falsifier (ex-eBay growth decelerating below the high-teens) — which is precisely what
  happened. `reasoning = sound`.

### Failure tags: **none**

No `valuation_underweighted` (it was the binding constraint), no `confidence_used_as_veto` (M1 = 0;
WATCH driven by price, not by uncertainty — exactly the disease WEIGHTING_HARNESS warns against, and
the card explicitly avoids it), no `inversion_veto_missed` (no hard veto was expected and the soft
−2 cap did the work), no `too_small_missed_asymmetry` / `too_large_for_uncertainty`. The card even
carries an explicit **trim rule** and **add/initiate rule**, so no `no_trim_rule` / `no_add_rule`.
Clean.

---

## 3. Verdict

**PASS (clean).** This is a model TRAP catch: the pipeline refused new money at the near-ATH price
(WATCH/0%), trimmed incumbents toward a ≤5% target, named the exact de-rating mechanism and every
kill-criterion that subsequently fired, and did so **without** an unjustified lookahead hard veto —
all while the stock proceeded to lose ~85% versus benchmarks that roughly doubled. The Runner's
mechanism relabel (`expensive_quality_compounder_derating_risk` over the sealed
`false_cheap_value_trap`) was the *more correct* read and is credited in full. Size-distance 0,
reasoning sound, dominant module and veto both matching expectation, zero failure tags.

*Locked decision card not modified. Post-as-of data used for scoring only.*
