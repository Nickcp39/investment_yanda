# Outcome Scorecard — AAPL (Apple Inc.), as-of 2016-05-12

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-as-of market data (allowed for the
> Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §7), and
> `WEIGHTING_HARNESS.md` §7.

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | quality_compounder (mispriced as ex-growth) |
| Business verdict | good |
| New-money verdict | **STARTER** |
| Existing-position verdict | HOLD |
| Suggested initial size | **4%** (Starter tier) |
| Suggested max size | **11%** (Confirmed-tier ceiling; explicitly capped below full Core) |
| Buy-below / starter zone | ≤ ~$95 (~10.5x trailing / ~7x EV-earnings); at-the-money ~$90.34 |
| Add zone | $80–92 on confirmation the iPhone decline is the 6s-vs-6 cyclical compare + Services keeps compounding |
| Binding constraint | iPhone trajectory — cyclical supercycle compare (→ installed-base + Services annuity bridges maturity) vs structural saturation (→ slow melt dragging normalized earnings); China secondary |
| Module signals | M1 +1 / M2 +1 / M3 +1 / M4 +1 / M5 −1 / M6 +1 |
| Hard veto | None fired (M5 −1 = size haircut, not a veto; structural_decline / false_cheap_value_trap labels tested and rejected) |

As-of close confirmed from the pack (`case_control.md` §2 + `asof_2016-05-12_aapl_quotes.csv` S008):
**$90.34 as-traded** on 2016-05-12 (intraday low $89.47 — first sub-$90 since 2014; ~$494.9B
market cap), on the **pre-2020 4:1-split basis** (the Jun-2014 7:1 split is already in this
as-traded basis; only the Aug-2020 4:1 split is removed, x4 vs the modern split line). On a
split-AND-dividend-adjusted basis the same close is ~$20.57 (StatMuse's adjusted series).

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **AAPL $90.34 (as-traded) on 2016-05-12.** All figures below are StatMuse
**total return** (dividend-inclusive) from the 2016-05-12 close. Total return is basis-invariant
(unaffected by the 2020 4:1 split), so it is the correct yardstick; raw split-adjusted closes are
shown only to characterize the path.

| Window | Date used | AAPL total return | SPY t.r. | QQQ t.r. | AAPL − SPY |
|---|---|---:|---:|---:|---:|
| As-of | 2016-05-12 | — | — | — | — |
| +12mo | 2017-05-12 | **+71.6%** | +17.7% | +31.3% | **+53.9 pt** |
| +24mo | 2018-05-12 | **+110.5%** | +36.9% | +61.9% | **+73.6 pt** |
| +36mo | 2019-05-13 | **+110.5%** | ~+44%* | ~+72%* | ~ +67 pt |
| ~today | 2026-06-16 | **+1,317.7%** | **+326.1%** | **+635.4%** | **+991.6 pt** |

\* SPY/QQQ +36mo are interpolated between the +24mo and to-2026 anchored reads (directional
only). The +12mo, +24mo, and to-2026 SPY/QQQ figures are direct StatMuse total-return reads;
those three anchored windows are more than sufficient to classify the outcome.

Reference split-adjusted closes (direct StatMuse reads, dividend-adjusted basis): $20.57
(2016-05-12, also the **lowest** adjusted close in the entire 2016→2026 window), $25.10
(2016-12-05), $54.87 (2018-10-03 pre-warning high), ~$33.74 (week of 2018-12-31 / 2019-01-03
trough), $299.24 (2026-06-16).

**Worst drawdown along the path (from the as-of entry): ≈ 0% — essentially never underwater.**
StatMuse reports the lowest closing price across the full 2016-05-12 → 2026-06-16 window as
**$20.57 on 2016-05-12 itself** — i.e. AAPL never closed below its as-of level again on a
total-return-adjusted basis. The as-of $90.34 (intraday low $89.47, a multi-year low) was within
a whisker of the absolute bottom; by 2016-12-31 the position was already +26.2% total return.
The only material *peak-to-trough* scare along the multi-year path was the Q4'18→Q1'19 selloff
(the Nov-2018 guide cut + the 2019-01-02 China revenue warning — the very binding-constraint risk
the card named): the adjusted close fell ~$54.87 (2018-10-03) → ~$33.74 (2019-01-03) = **−38.5%
peak-to-trough**, but even that trough was still **+59.8% total return above the as-of entry**. A
2016-05-12 buyer was never sitting on a loss. Source: StatMuse min-close + per-date queries
2016-05-12 → 2026-06-16.

### Price source(s)
StatMuse Money historical series — the same provider used to score the GOOGL and INTC cases,
and consistent with the case's own as-of verification (S008 cross-checks the as-traded $90.34;
StatMuse's $20.57 is that same close on a split+dividend-adjusted basis, x4 split + dividend
add-back). Queried per-window total-return endpoints + per-date closing-price and min-close
queries for AAPL, SPY, QQQ. The +1,317.7% magnitude is far too large for provider error to flip
the WINNER classification.

### Mechanical label
**WINNER — decisively, and one of the cleanest in the set.** AAPL returned **+1,317.7% total
return vs SPY +326.1% (beat SPY by ~992 pts) and QQQ +635.4% (beat QQQ by ~682 pts)** over ~10
years, **beat SPY at every measured window** (+54pt at +12mo, +74pt at +24mo), and — the
distinctive feature — **was essentially never below the as-of entry at any point.** The thesis
the card identified compounded exactly as framed: the iPhone decline proved cyclical (the 6s-vs-6
supercycle compare, as the card argued), the 1B+ installed base + Services annuity carried and
then re-accelerated, capital return retired a huge share of the float, and the franchise re-rated
from ~10x to a premium multiple. This **confirms the orchestrator's sealed expectation** (AAPL =
WINNER, a durable quality_compounder mispriced as ex-growth at the 2016 low). The as-of ~$90 /
~6.7x EV-earnings on ~$153B net cash was, in fact, a generational entry.

**Path note (load-bearing for the size grade):** unlike the back-loaded GOOGL win, the AAPL win
was **front-loaded and monotonic from the entry** — +72% by year 1, +110% by year 2, never
underwater, with the asymmetry visible early. This makes the under-sizing critique *stronger*, not
weaker: there was no year-one lag or drawdown to vindicate caution. The one moment the binding
constraint actually bit (the Q1'19 China warning) still left the position up ~60%, and the
card's pre-named add zone / kill-criteria would have read it correctly (cyclical, not structural).

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, **Winner row**:
- PASS = `STARTER` or `CORE` (or explicit structured starter)
- PARTIAL = `WATCH` but names the correct key variable + clear buy/add trigger
- FAIL = `REJECT`, or `WATCH / 0%` with avoid framing

Locked new-money verdict = **STARTER** (4% real money, explicit add-on-confirmation path,
buy-below ~$95, HOLD for existing). It avoided REJECT, avoided WATCH/0%, and reached a
real-ownership tier on a name that returned ~14x.

**Axis-1 = PASS.**

This is the *exact* failure the redesign was built to fix, run on the textbook example: a durable
compounder, optically "ex-growth" after its first revenue decline in 13 years, that the old
"more-research-more-doubt / avoid because the optic looks bad" process would have sent to WATCH/0%.
The lean pipeline instead converted the genuine maturity uncertainty into a **size haircut, not a
confidence veto** (M5 −1, no hard veto; M1 +1) and bought a starter. Direction: correct.

### Size-distance (0–3)

Correct size band (sealed + METHODOLOGY): **STARTER..CORE.** Realized outcome = a WINNER that
compounded **~14x over the decade**, beat SPY by ~992 points, and was never underwater — the
single best realized outcome in the case set, and precisely the "businesses you would hold 5–10
years" Core archetype `METHODOLOGY.md §2` describes (it is the doc's own canonical Core example:
"Duan let Apple run to ~60%").

Locked sizing: initial **4%** (top of the 3–5% Starter band), max **11%** (Confirmed-tier
ceiling, explicitly capped *below* full Core), with an explicit add-on-confirmation path.

Scoring against METHODOLOGY §7 ("a winner sized only as a tiny STARTER is NOT full marks") and
the durability ladder:

- The initial 4% sits **inside the correct STARTER..CORE band** → by the literal PROTOCOL §6
  size-distance scale this is **not a band miss (a strict-literal 0).**
- But METHODOLOGY §7's "too small loses points" pressure bites **harder here than on GOOGL**, for
  three reasons that all cut the same way:
  1. **The ceiling is capped below Core by design.** The card's max is **11% (Confirmed tier)**,
     explicitly "capped below full Core," on the grounds that the post-Jobs *new-category / growth*
     line is unproven (Ive stepping back, no proven new-category author). Realized history shows
     the **cash-machine / installed-base annuity alone** — the exact line the card graded as the
     durable, Core-grade strength (M3: "raises the floor") — compounded ~14x **without needing a
     new category**. The growth-ceiling caveat was real but was the *wrong variable to cap total
     size on*: the durability that warranted Core was already present and already sufficient.
  2. **The win was front-loaded and never underwater**, so — unlike GOOGL — there is **no
     year-one lag or drawdown to earn back the timidity**. A day-one larger position would have
     been *right on both destination and timing*. The mitigant that softened GOOGL's grade is
     absent here.
  3. This is the methodology's **named Core exemplar** entered at 4% / capped at 11%; followed
     mechanically, the plan **never reaches the Core tier its own durability + realized outcome
     warranted.**
- **Mitigants that keep it from a 2:** (a) 4% is a *genuine, well-structured starter* with an
  explicit add path (the methodology *wants* "start real, add on confirmation"), not a terminal
  size; (b) the *band* is correct — this was real ownership of the winner, not a reject/0%; (c) at
  as-of the iPhone cyclical-vs-structural question was genuinely unresolved, so a sub-Core *entry*
  was defensible even though the *ceiling* was not.

Net: the *entry band* is correct, but the **11% Confirmed ceiling on the methodology's flagship
Core (15–25%) compounder, with no path-caution to redeem it, is one notch too timid for a ~14x
realized winner.** Same structural lean as GOOGL (timid at the ceiling, not the trigger), and the
absence of any vindicating drawdown makes it at least as deserving of the deduction.

**Size-distance = 1** ("appropriately STARTER, correct band, but the 11% Confirmed ceiling skews
one notch small for the methodology's own Core-durability exemplar that compounded ~14x and was
never underwater; the explicit add path keeps it from a 2, but unlike GOOGL there is no year-one
lag/drawdown to earn the timidity back").

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes, precisely. The card's binding constraint is the
  iPhone-trajectory question — "**cyclical** iPhone-6-supercycle comparison (→ maturity bridged by
  the 1B installed base + Services annuity) **vs structural** saturation (→ slow melt dragging
  normalized earnings)," with China secondary. Realized history resolved it **exactly the bullish
  way the card laid out**: the decline was the cyclical compare, units stabilized/re-grew, the
  installed base + Services compounded and carried the franchise, and the one time the structural
  fear flared (Q1'19 China warning) it proved transitory — the position stayed up ~60% and went on
  to ~14x. The card identified both the upside engine (installed-base annuity + Services + buyback
  + fortress balance sheet at ~6.7x EV-earnings) and the single genuinely unresolved risk, and
  correctly tagged the risk as *unresolved at as-of* rather than pretending to resolve it.
- **Right module dominance?** Yes. The conviction stack **M2 +1 / M3 +1 / M4 +1** (theme/mechanism
  + profit-pool/durability + financial-reality) drove the STARTER, M6 (+1) supported entry at a
  clearly attractive price, and M5 (−1, no veto) **correctly sized down rather than killing** — the
  intended quality_compounder dominance pattern (WEIGHTING_HARNESS §4: positive emphasis M2/M3/M4;
  price a modulator not a veto). The M5 trap test did real work: it explicitly ran the
  structural_decline / false_cheap_value_trap labels and **rejected them for the right reasons**
  (moat intact, normalized earnings only modestly below trailing, fortress net cash, survivable) —
  the mirror-image of the correct *positive* call to the INTC trap-rejection.
- **No lookahead?** The card draws only on pre-2016-05-12 evidence (FY15 10-K, Q2'16 8-K/10-Q +
  transcript, Strategy Analytics/IDC Q1'16 industry data, dated 2016 news). `case_control.md` §5
  explicitly excludes the forbidden post-as-of facts — notably **Berkshire's Apple stake** (first
  disclosed in the 13F filed ~2016-05-16, *after* the as-of) and any later iPhone/AirPods/Services
  boom. On the face of the card, clean. (Full lookahead adjudication is the Auditor's job, out of
  Scorer scope.)

**Reasoning = sound.** Correct key variable (resolved exactly as framed), correct module dominance
(M2/M3/M4 conviction stack led; M5 sized down without a false veto), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (quality_compounder → WEIGHTING_HARNESS §4 positive emphasis **M2/M3/M4**, price a
  modulator; aligns with the GOOGL sibling's M2/M3 conviction-stack pattern).
- **Got:** the call was driven by the **M2/M3/M4 conviction stack**, with M6 setting entry and M5
  sizing down. The single most load-bearing module is **M3 (Profit Pool / Durability)** — it
  carried the premium-tier profit-pool capture, the wide ecosystem/brand moat + 1B installed base,
  and the operator grade (post-Jobs team 4/5, owner-minded, low governance risk) that set the
  *floor* (the part that actually compounded ~14x). **M2** (the durable-franchise-mispriced-as-
  ex-growth thesis) is co-dominant.

**dominant_module (got) = M3** (with M2 co-dominant); **dominant_module_expected = M2/M3.**
**Match.** The right modules drove the call.

### Veto fired vs expected

- **veto_expected:** No. For a quality_compounder, WEIGHTING_HARNESS §4 fires a veto "only if
  thesis durability breaks" — which it did not. Sealed/orchestrator expectation: no veto.
- **veto_fired:** **No.** M5 fired a −1 size-haircut warning and explicitly declined a hard veto
  (the structural_decline / false_cheap_value_trap labels were tested and rejected: moat intact,
  normalized earnings only modestly below trailing, fortress net cash, survivable downside). This
  is exactly correct and is the **mirror image of the redesign's central fix** — the old process
  would have let "the optic looks bad / forward demand is uncertain" act as a de-facto veto and
  produced WATCH/0%; the lean pipeline correctly held it to a size haircut.

**veto_fired = no; veto_expected = no.** Correct.

### Failure tags (from WEIGHTING_HARNESS §7 list)

Candidate review:
- `confidence_used_as_veto` — **NOT present** (the explicit fix: M1 +1 / M5 −1 forward-maturity
  uncertainty → size haircut, not WATCH). This is the old failure the redesign avoided, on the
  canonical example.
- `valuation_overweighted` — **NOT present** (M6 read ~10x / ~6.7x EV-earnings as clearly
  attractive and supported a starter; price did not gate the name down).
- `inversion_veto_missed` — **NOT present** (the trap test correctly ran *and rejected* the
  structural-decline / false-cheap labels for sound reasons; no false-positive veto, unlike the
  intc_2024 sibling).
- `hold_winner_failed` — **NOT present** (existing-position HOLD with no thesis-break trigger is
  correct; the thesis was intact and compounding).
- `no_add_rule` / `no_trim_rule` — **NOT present** (both explicit; add zone $80–92 on cyclical
  confirmation, trim only on broken thesis).
- `too_small_missed_asymmetry` — **PRESENT (primary, stronger than GOOGL's).** A ~14x winner, the
  methodology's own Core (15–25%) exemplar, entered at 4% and **capped at 11% (Confirmed, below
  Core) by design** on a growth-ceiling caveat that proved value-irrelevant — the durable
  cash-machine line alone delivered the ~14x. Per METHODOLOGY §7 this leaves very large asymmetry
  uncaptured. Tagged **primary** here (vs soft/secondary for GOOGL) because there was **no
  year-one lag or drawdown to justify the caution** — the win was front-loaded and never
  underwater, so the timid ceiling has no path-vindication.

**failure_tags = too_small_missed_asymmetry.** (Primary. The size *band* is correct and the entry
is a defensible starter, so this is the only tag — but it is a real one, not a soft flag: the
sub-Core ceiling on the flagship Core compounder is the one genuine miss.)

---

## 3. Verdict

The lean 6-module pipeline **nailed the direction on the canonical "avoid because the optic looks
bad" compounder** — the exact case the old framework was built to stop fumbling. Apple at ~$90 /
~6.7x EV-earnings on ~$153B net cash, "ex-growth" after its first revenue decline in 13 years, got
a **STARTER (4% real money, HOLD for holders, explicit add path)** instead of the legacy WATCH/0%,
because the pipeline turned genuine iPhone-maturity uncertainty into a **size haircut, not a
confidence veto** (M2/M3/M4 +1 conviction stack; M5 −1 ran the trap test and *correctly rejected*
the structural-decline / false-cheap labels; M1 +1). Realized outcome: **+1,317.7% total return vs
SPY +326.1% / QQQ +635.4% to 2026-06-16 (beat SPY by ~992 pts), never underwater from the entry,
≈14x** — a decisive WINNER and the cleanest in the set, confirming the sealed expectation.

Axis-1 **PASS**, reasoning **sound**, dominant module **M3 (with M2 co-dominant; matches M2/M3
expected)**, **no veto fired or expected** (correct), and the right modules drove it. The sole
deduction is METHODOLOGY §7's "too small loses points," and it bites **harder than on GOOGL**: the
**11% Confirmed ceiling — capped below Core by design, on a new-category/growth caveat that proved
value-irrelevant** (the cash-machine annuity alone compounded ~14x) — left large asymmetry on the
table, and **unlike GOOGL there was no year-one lag or drawdown to earn the timidity back** (the
win was front-loaded and monotonic). Net grade: a strong, well-reasoned **PASS** with a genuine
**size-distance 1** under-sizing lean (`too_small_missed_asymmetry`, primary) — *be braver at the
ceiling, not the trigger.* The same lesson the GOOGL scorecard logged, here in its purest form: a
growth-ceiling caveat should shave the *growth* sleeve, not cap *total* size below Core on a
franchise whose durable economics + operators were already Core-grade.

---

## 4. results.csv row (RETURNED to orchestrator — not written to results.csv by Scorer)

```
lean-6module-v1,none,aapl_2016-05-12,quality_compounder,WINNER,4,STARTER,HOLD,STARTER..CORE,1,no,no,M3,M2/M3,sound,too_small_missed_asymmetry,"WINNER +1317.7% t.r. to 2026-06-16 vs SPY +326.1%/QQQ +635.4%; beat SPY ~992pt. +12mo +71.6% (SPY +17.7%/+54pt), +24mo +110.5% (SPY +36.9%/QQQ +61.9%/+74pt). Worst DD ~0% from entry: as-of 2016-05-12 ($90.34 as-traded / $20.57 adj) was the LOWEST close in the whole 2016->2026 window (never underwater); only path scare Q4'18->Q1'19 China-warning -38.5% peak-to-trough but still +59.8% above entry. Win front-loaded+monotonic (vs GOOGL back-loaded). Axis-1 PASS (STARTER avoided old WATCH/0%); reasoning sound; M2/M3/M4 conviction stack drove it; M5 -1 ran trap test + CORRECTLY rejected structural-decline/false-cheap labels (mirror of redesign fix), no veto=right. iPhone cyclical-vs-structural key var resolved exactly bullish as framed; Berkshire 13F correctly excluded (post-as-of). size-dist 1: 4% entry/11% Confirmed ceiling capped below Core by a growth/new-category caveat that proved value-irrelevant -- cash-machine annuity alone did ~14x; methodology's OWN Core exemplar (Duan let AAPL run ~60%). Harder miss than GOOGL: NO yr1 lag/drawdown to redeem the timid ceiling. Be braver at the ceiling not the trigger. Source: StatMuse total-return; as-of from case S008."
```
