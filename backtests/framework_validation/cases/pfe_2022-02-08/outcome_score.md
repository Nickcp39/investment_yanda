# Outcome Scorecard — PFE (Pfizer Inc.), as-of 2022-02-08

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-as-of market data (allowed for the
> Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §7), and
> `WEIGHTING_HARNESS.md` §6/§7.

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | false_cheap_value_trap |
| Business verdict | uncertain |
| New-money verdict | **WATCH** (no new money at $51.70; explicit COVID-normalization + patent-cliff diagnosis) |
| Existing-position verdict | **TRIM** (toward tracking-only weight) |
| Suggested initial size | **0%** at the as-of setup |
| Suggested max size | **~1%** (tracking only, until thesis flips) |
| Buy-below / starter zone | **~$38** (~12–14x on ~$2.50–3.00 normalized ex-COVID EPS); revisit only on proof of ex-COVID base AND a normalized-earnings price — NOT the optical ~8x windfall multiple |
| Binding constraint | M4/M5 — strip the ~$54B Comirnaty+Paxlovid windfall → ex-COVID rev ~$46B, ex-COVID adj EPS ~$2.50–3.50 → **real fwd P/E ~15–21x** at $51.70 = market multiple, **no MOS**, on an ordinary ~6%-growth base facing a known mid-decade patent cliff; the optical ~8x is peak-windfall earnings, not value. (Reinforcing: windfall-deployment risk under a combined Chair+CEO with no allocation track record.) |
| Module signals | M1 0 / M2 −1 / M3 0 / M4 **−1** / M5 **−1** / M6 −1 |
| Hard veto | **None** fired. Soft veto / strong warning: caps size and blocks a STARTER, but explicitly NOT a hard zero or a short — balance sheet not at risk, ~3.1% dividend covered even on normalized earnings, COVID cash real-and-banked, downside survivable. |

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **PFE 2022-02-08.** Close **$51.70** (~$290B mkt cap; case_control). All
total-return figures below are StatMuse **total return** (dividend-inclusive) from the
2022-02-08 close — the same provider/basis used across the other Round-1 cases (NVDA, INTC,
AAPL). Internal consistency check: StatMuse reports the to-2026 *price* near $26.04 while
reporting a to-2026 *return* of −35.2%; from $51.70 a price of ~$26 is ~−50% on price alone,
so the −35.2% figure correctly adds back the (substantial, never-cut) dividend stream → it is
the total-return series, as intended.

| Window | Date used | PFE total return | SPY t.r. | PFE − SPY |
|---|---|---:|---:|---:|
| As-of | 2022-02-08 | — | — | — |
| +12mo | 2023-02-08 | **−10.2%** | −6.6% | **−3.6 pt** |
| +24mo | 2024-02-08 | **−40.8%** | +15.1% | **−55.9 pt** |
| +36mo | 2025-02-08 | **−41.3%** | +40.5% | **−81.8 pt** |
| ~today | 2026-06-16 | **−35.2%** | +78.1% | **−113.3 pt** |

### Price source(s)
StatMuse Money historical series (dividend-inclusive total-return endpoints per window;
plus a min-close query for the worst drawdown). The magnitudes at every 12/24/36-month
window and to-2026 are large enough that any provider rounding cannot flip the
classification. COVID-revenue collapse and dividend-history cross-checks below come from
SEC 8-K exhibits, Pfizer dividend press releases, and contemporaneous reporting.

### Worst drawdown along the path
Trough close **$19.80 on 2025-04-10** (April-2025 tariff-shock low) = **≈ −62%** from the
$51.70 as-of close on a price basis (deeper still intraday). The position was underwater at
every conventional window: roughly −10% (yr1), −41% (yr2), −41% (yr3), and still −35% on a
total-return basis 4.3 years out. Source: StatMuse min-close query 2022-02-08 → 2026-06-16
($19.80 @ 2025-04-10).

### Dividend status — this is a PRICE-impairment trap, NOT a yield/dividend trap (material)
The dividend leg of the card's "survivable, not a melting ice cube" read held exactly as
described — Pfizer **never cut or suspended** the dividend through the window. It **raised**
the quarterly payout to **$0.42** (first-quarter 2024) and **$0.43** (first-quarter 2025),
its **15th+ consecutive year** of increases and the **345th** consecutive quarterly dividend
(Pfizer dividend press releases, Dec-2023 / Dec-2024). So the realized loss was **all price**,
partially cushioned by a covered, rising yield — precisely the "value trap, balance sheet
fine, dividend covered, downside survivable" profile the card used to justify WATCH/TRIM
over a hard REJECT/EXIT. (Contrast INTC-2021, the structural-decline sibling, where the
dividend was cut 66% then suspended — PFE is the *false-cheap* trap variant, not the
melting-ice-cube variant, exactly as labeled.)

### The mechanism the card predicted is what realized
The card's load-bearing claim — that ~$54B of the 2022 guide was a one-time, high-margin
COVID windfall (Comirnaty + Paxlovid) that would normalize away, leaving an ordinary
~$46B ex-COVID base at a *real* ~15–21x — is exactly what happened:
- Comirnaty + Paxlovid combined revenue **$57B (2022) → ~$12.5B (2023) → ~$8B guided
  (2024)** (FiercePharma / SEC 8-K exhibits, 2023–2024). Q3'23 total revenue −41% op,
  Q4'23 −42% op, driven by the COVID line — i.e. the windfall the card said to strip out
  collapsed by ~78% in one year and ~86% in two.
- 2024 guidance ($58.5–61.5B) came in below the ~$63.2B consensus on "plummeting demand
  for COVID products," triggering further stock declines — the same normalize-the-windfall
  dynamic the card warned was unpriced in the optical ~8x.

### Mechanical label
**TRAP.** Decisive on the realized path actually available to a 2022 buyer:
- Lagged SPY by **~56 pt (+24mo), ~82 pt (+36mo), ~113 pt (to-2026)** — persistent, widening
  underperformance vs the index at every window past year 1.
- Suffered an **≈ −62% peak-to-trough drawdown** (close $19.80, 2025-04-10) and was a
  total-return loser (−35% to −41%) at every conventional window — the false-cheap signature:
  the optical ~8x was peak-windfall earnings, and the multiple re-rated as the windfall
  normalized, not as a mispriced compounder.
- This **confirms the orchestrator's sealed expectation** (PFE = TRAP, false_cheap_value_trap;
  "false-cheap peak-COVID-earnings"). The as-of $51.70 was a windfall-inflated entry into a
  multi-year COVID-normalization de-rate, cushioned only by a covered dividend.

Note for Synthesis: the loss is *less catastrophic* than INTC-2021's (no dividend cut, no
~66% terminal drawdown sustained, and a real cash-rich balance sheet) — which is exactly the
distinction the card drew when it chose WATCH/TRIM over EXIT. The trap classification is
unambiguous, but the card's *severity* read (survivable value trap, not melting ice cube) was
also correct, and there is no off-horizon terminal spike rescuing the number (unlike INTC).

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, **Trap row** (and the prompt's TRAP-row gate):
- PASS = `REJECT`, or `WATCH` **with a correct structural / normalization diagnosis** (here:
  it normalized the COVID windfall → real fwd P/E ~15–21x)
- PARTIAL = `WATCH` for a weak / incomplete reason
- FAIL = `STARTER` or `CORE`

Locked new-money verdict = **WATCH**, with **0% initial size**, explicit no-chase/avoid framing
at $51.70, **TRIM** for existing holders, and a diagnosis that names the exact realized
mechanism with worked arithmetic: strip ~$54B Comirnaty+Paxlovid → ex-COVID rev ~$46B →
ex-COVID adj EPS ~$2.50–3.50 → **real fwd P/E ~15–21x** = market multiple, no MOS, on an
ordinary ~6%-growth base facing a mid-decade patent cliff; the optical ~8x is a one-time
windfall artifact, not value. That is precisely the "WATCH with a correct
structural/normalization diagnosis" condition for a PASS, and it sits squarely inside the
sealed `REJECT..WATCH` correct band. The card did not merely land on the right verdict — it
pre-identified the exact variable (COVID windfall durability / ex-COVID earnings power) that
drove the realized −35% to −41% loss, and pre-named the inverse-confirmation kill-criterion
("COVID revenue normalizes hard with no BD backfill") that then fired.

**Axis-1 = PASS.**

### Size-distance (0–3)

Correct size band (sealed + PROTOCOL §7): **REJECT..WATCH / 0%.** Realized outcome = TRAP.
Locked sizing: initial **0%**, max **~1%** (tracking only), buy-below gated at **~$38** on
proof of the ex-COVID base.

- 0% initial new money is **dead-center in the correct band** for a realized trap → size-distance **0**.
- The ~1% ceiling is not an active position — it is a tracking-only sliver, and even that is
  gated on the thesis flipping (ex-COVID base proven AND price at normalized earnings). That is
  a correct WATCH-with-trigger structure, not a sizing into the trap. (The ~$38 buy-below was
  in fact reached and breached to the downside — the stock fell to ~$20 — so a holder who
  followed the gate would have *correctly* still not been triggered into a STARTER, because the
  ex-COVID-base-proof condition never cleanly resolved favorably.)

**Size-distance = 0** (within the correct band; 0% new money into a name that fell ~62% to
trough and lagged SPY by ~113 pt is exactly right).

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes, exactly. Sealed key variable = "COVID earnings
  normalization, patent cliff risk." The card's binding constraint is the COVID-windfall
  normalization (strip ~$54B → real ~15–21x) plus the mid-decade LOE wall — and the realized
  history confirms each leg: Comirnaty+Paxlovid collapsed $57B → ~$12.5B → ~$8B in two years,
  guidance was cut below consensus on COVID demand, and the multiple re-rated down. The card
  even pre-named the inverse-confirmation kill-criterion that fired.
- **Right module dominance?** Yes. **M4 (Financial Reality, −1)** carries the load-bearing
  normalization (the worked ex-COVID EPS / real-P/E arithmetic), and **M5 (Inversion/Trap
  Test, −1)** confirms the false-cheap-on-a-one-time-event kill path; M2 (context, −1) and M6
  (price, −1) reinforce that the low multiple is not MOS. That is exactly the WEIGHTING_HARNESS
  §4 emphasis for `false_cheap_value_trap` (M4, M5) and the §6 trap pattern (M4 normalized <<
  trailing + M5 false cheapness).
- **No lookahead?** Card draws only on pre-as-of evidence (Feb-8-2022 release/call, Q3'21 10-Q
  share count, dated Nov-2021 sell-side normalization context). The FY2021 10-K (filed
  2022-02-24) was correctly identified as post-as-of and excluded; the independent Lookahead
  Checker verdict on the pack was CLEAN (`material_audit.md`). On the face of the card, clean.
  (Full lookahead adjudication is the Auditor's job, out of Scorer scope.)

**Reasoning = sound.** Correct key variable, correct module dominance (M4 normalization-led,
M5 trap-confirming — the intended false-cheap pattern), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (a false_cheap_value_trap → M4/M5-led per WEIGHTING_HARNESS §4/§6; orchestrator
  reference for this case = **M4/M5**).
- **Got:** **M4 (Financial Reality, −1)** is the single most load-bearing module — it carries
  the explicit COVID-windfall normalization and the ~15–21x real-P/E conclusion that is the
  binding constraint — with **M5 (Inversion/Trap Test, −1)** co-dominant (the false-cheap kill
  path). M2 and M6 are supporting.

**dominant_module (got) = M4/M5; dominant_module_expected = M4/M5. Match** — the right
normalization-led / trap-confirming modules drove the call.

### Veto fired vs expected

- **veto_expected: no.** For a `false_cheap_value_trap`, WEIGHTING_HARNESS §6 *permits* a hard
  M4/M5 veto, but the orchestrator did not assert a mandatory hard veto for this case; the
  operative test is whether the framework drove size to 0 for the correct normalization reason.
- **veto_fired: no.** The card was explicit that M4/M5 were a **soft veto / strong warning**
  that capped size and blocked a STARTER — NOT a hard zero or a short — because the balance
  sheet was not at risk, the ~3.1% dividend was covered even on normalized earnings, and
  downside was survivable. Functionally this drove size to 0% new money / TRIM, which is the
  outcome a veto would have produced. The realized path **vindicates** the choice to express
  this as a size-to-0 warning rather than a solvency veto: PFE was a deep *price* loser but
  never a balance-sheet/dividend failure (dividend was raised, not cut), so a hard
  "melting-ice-cube" veto would have *over*-stated the danger and been the wrong mechanism. The
  soft-veto read was the precisely-calibrated one.

**veto_fired = no; veto_expected = no.**

### Failure tags (from WEIGHTING_HARNESS §7 list)

Candidate review:
- `inversion_veto_missed` — **NOT present.** The trap test fired (M5 −1) and confirmed the
  false-cheap kill path; the verdict avoided the trap.
- `trailing_accounting_trap` — **NOT present** (avoided). The card explicitly refused to treat
  the optical ~8x forward / ~11.7x trailing as MOS, correctly tagging it as peak-windfall
  earnings. This is exactly the trap WEIGHTING_HARNESS §6 was built to catch, and it was caught.
- `financial_reality_underweighted` — **NOT present.** M4 did the load-bearing normalization
  (strip the windfall → real ~15–21x) — the opposite of underweighted.
- `valuation_overweighted` / `valuation_underweighted` — **NOT present.** Price was correctly
  read as no-MOS and a windfall artifact (the correct posture for this context per §4).
- `too_large_for_uncertainty` — **NOT present** (0% initial; ~1% ceiling is tracking-only and
  thesis-gated).
- `too_small_missed_asymmetry` — **NOT present** (no asymmetry was missed; the realized path
  was a loss, so 0% was correct, not timid).
- `hold_winner_failed`, `no_add_rule`, `no_trim_rule` — **NOT present** (kill-criteria, the
  gated buy-below trigger, and the TRIM action are all explicit).

**failure_tags = none.** Clean false-cheap trap-avoidance with no failure mode triggered.

#### Calibration note for Synthesis (not a failure tag)
This is the **second clean trap-avoidance** in the set and the **mirror-correct counterpart**
to amzn_2023-02-03: in both, a headline-distorted financial picture was put through M4
normalization — but here the normalization correctly stripped a *windfall to expose
expensiveness* (false-cheap), whereas in AMZN it stripped a *non-cash mark to expose cheapness*
(real value). The pipeline applied M4 in opposite directions on opposite setups and got both
right — direct evidence the §4 context gate + §6 trap-veto design discriminates rather than
pattern-matching one way. It is also the **counterexample to intc_2024-08-02**: there M4/M5
over-fired into a near-veto on a survivable two-sided reset (a WINNER), producing a size-dist-3
FAIL; here M4/M5 fired on a genuine false-cheap trap and produced a size-dist-0 PASS. The
distinguishing fact in both is "survivable + two-sided vs structurally-impaired," and on PFE
the pipeline read it correctly (covered dividend + real cash + ordinary base = WATCH/TRIM, not
EXIT — and the dividend indeed was never cut). The card's two-sided dissent (bull: real cash +
rising dividend could make 8x asymmetric; hawk: EXIT not TRIM) bracketed the outcome well;
realized history landed nearer the spine (deep price loser, dividend-cushioned), validating the
chosen WATCH/TRIM midpoint.

---

## 3. Verdict

The lean 6-module pipeline **correctly avoided the Pfizer false-cheap value trap.** On a name
that screened optically cheap (~8x forward) only because ~$54B of the 2022 guide was a
one-time, high-margin COVID windfall, the framework's M4 normalization (strip the windfall →
ex-COVID adj EPS ~$2.50–3.50 → **real fwd P/E ~15–21x = no MOS**), confirmed by M5's false-cheap
kill path, produced a **WATCH with the precise COVID-normalization + patent-cliff diagnosis, 0%
new-money size, and a TRIM-toward-tracking existing-position action** — and pre-named the
inverse-confirmation kill-criterion that later fired. PFE then lost −10.2% / −40.8% / −41.3% /
−35.2% (total return) at +12/24/36mo and to-2026 while SPY returned −6.6% / +15.1% / +40.5% /
+78.1% — lagging the index by ~56 / ~82 / ~113 pt past year 1 — and drew down to a $19.80 close
(≈ −62%) on 2025-04-10, exactly as the Comirnaty+Paxlovid line collapsed $57B → ~$12.5B → ~$8B.
Critically, the card's *severity* read was also correct: this was a **price-impairment** value
trap, **not** a yield/dividend trap (the dividend was raised, never cut), validating the
soft-veto / WATCH-TRIM choice over a hard REJECT/EXIT. Axis-1 **PASS**, size-distance **0**,
reasoning **sound**, dominant module **M4/M5 (matches expected)**, **no failure tags**. A
textbook clean false-cheap trap-avoidance and a strong validation of the §4 context-gate /
§6 trap-veto design — and, paired with AMZN-2023, evidence the M4 normalization step
discriminates in both directions.

---

## 4. results.csv row (RETURNED to caller — not appended to results.csv per instructions)

```
lean-6module-v1,none,pfe_2022-02-08,false_cheap_value_trap,TRAP,0,WATCH,TRIM,REJECT..WATCH,0,no,no,M4/M5,M4/M5,sound,none,"TRAP: PFE t.r. -10.2%/-40.8%/-41.3%/-35.2% at +12/24/36mo & to-2026 vs SPY -6.6%/+15.1%/+40.5%/+78.1%; lagged SPY ~56pt(+24mo)/~82pt(+36mo)/~113pt(to-2026). Worst close $19.80 @2025-04-10 (~-62% from $51.70). Dividend NEVER cut - RAISED to $0.42(2024)/$0.43(2025), 15th+ consec yr / 345th consec qtr -> price-impairment value trap, NOT a yield/dividend trap (vindicates soft-veto WATCH/TRIM over EXIT). Mechanism realized as card predicted: Comirnaty+Paxlovid $57B(2022)->~$12.5B(2023)->~$8B(2024 guide), the ~$54B windfall normalized away exactly as M4 said; optical ~8x re-rated on ~$46B ordinary base. Axis-1 PASS (WATCH w/ correct COVID-normalization dx -> real fwd P/E ~15-21x + 0% size + TRIM); size-dist 0; reasoning sound; M4 normalization-led + M5 false-cheap kill path, M2/M6 support; no hard veto (soft size-to-0 warning, balance sheet fine, dividend covered = right). Mirror-correct vs AMZN-2023 (M4 stripped windfall to expose expensiveness vs stripped non-cash mark to expose value) & counterexample to INTC-2024 (M4/M5 fired correctly on a real trap here, no over-fire). Clean, no lookahead. Source: StatMuse total-return; SEC 8-K/FiercePharma for COVID-rev collapse, Pfizer dividend releases for the never-cut/raised dividend."
```
