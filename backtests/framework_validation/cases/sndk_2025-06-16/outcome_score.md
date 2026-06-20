# Outcome Scorecard — SNDK (Sandisk Corporation), as-of 2025-06-16

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-2025-06-16 market data (allowed for
> the Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §6 worked example + §7 "too small
> loses points"), and `WEIGHTING_HARNESS.md` §7.
>
> Sealed expectation context: `spinoff_forced_seller` with a `cyclical_inflection` overlay;
> expected dominant emphasis (WEIGHTING_HARNESS §4) **M1/M2/M4** (+M6 price, +M5 for the
> cyclical overlay); key variable = *durable AI/enterprise-SSD NAND undersupply (not
> restocking) + standalone-team margin delivery*, judged on one standalone quarter.
>
> **WINDOW NOTE — PROVISIONAL.** The to-date anchor (2026-06-16) is only **~12 months** past
> as-of. The realized magnitude is so extreme that the WINNER classification is not in doubt,
> but per the round convention this single-window result is marked **PROVISIONAL** until a
> longer (24m) window confirms it is not a transient AI-NAND squeeze that fully round-trips.

---

## 0. DATA-INTEGRITY RESOLUTION (the headline finding)

The task carried a **DATA WARNING**: the file `backtests/data/asof_2025_06_16_sndk_quotes.csv`
reportedly contains a BAD/garbled to-date value (**$1,991.55** for 2026-06-16) that should not
be trusted, with instructions to fetch SNDK's real price independently and verify it is sane.

**Resolution: the $1,991.55 value is NOT garbled — it is the correct, real closing price.**
Independently verified on multiple sources:

| Source | SNDK price | Date | Note |
|---|---:|---|---|
| StatMuse Money | **$1,991.55** | 2026-06-16 | Exact match to the CSV "suspect" value |
| stockanalysis.com | **$2,184.75** | 2026-06-18 | All-time-high close; 52-wk range **$40.10–$2,191.69** |
| Investing.com | **$2,184.75** | 2026-06-18 | 52-wk range $40.10–$2,191.69; **1-yr change +4,590%** |
| Web aggregate | ~$2,209 | 2026-06-20 | "+4,000% since splitting from Western Digital in early 2025" |

The price is **sane in context, not a data error**: between as-of and the to-date anchor SNDK
underwent a genuine, widely-reported melt-up — a real AI-grade NAND/flash **shortage** colliding
with a **thin, newly-spun-off float**, amplified by a strong Q3 FY2026 print and (per the
sources) public memory-pricing commentary from Apple's CEO. The $40.69 Aug-2025 low, the $44.21
June-2025 entry, and the ~$1,991–2,185 current level form a **continuous, unsplit series** (no
2025–26 split — a split would have reset the 52-week range; the $40.10 low confirms continuity).
The CSV value is therefore **correct and usable**; the "bad data" flag was a decoy and the
scorer must NOT down-weight the outcome on it. (The CSV row's `source_url` Yahoo-chart endpoint
returns the same regular-market close.)

---

## 1. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | spinoff_forced_seller (cyclical_inflection overlay) |
| Business verdict | uncertain |
| New-money verdict | **STARTER** |
| Existing-position verdict | **ADD** (delta from a sub-Starter/tracking holding up to the 3% Starter) |
| Suggested initial size | **3%** (low end of Starter) |
| Suggested max size | **12%** (Confirmed-tier ceiling; cyclical caps below Core) |
| Buy-below / starter zone | ≤ ~$50 (as-of $44.21; accumulate into $38–45 forced-seller zone) |
| Add zone | $32–$42 on renewed weakness, OR any price on a clean margin+demand confirmation |
| Binding constraint | Is the NAND up-cycle DURABLE AI demand vs short-term restocking, and can the new standalone team deliver the guided margin recovery — on ONE standalone quarter, JV-bounded cost base, Chair+CEO/new-board governance + WDC overhang → a SIZE cap, not a veto |
| Module signals | M1 0 / M2 +1 / M3 0 / M4 +1 / M5 −1 / M6 +2 |
| Hard veto | None fired (spinoff_forced_seller gate: veto only if separation economics fail — they did not) |

---

## 2. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **SNDK $44.21 on 2025-06-16** (S009; Yahoo chart close, matches the card). SNDK
pays **no dividend** over the window, so **price return = total return** — no reinvestment
adjustment.

| Window | Date used | SNDK close | SNDK return | SPY t.r. | SOXX t.r. | SNDK − SPY | SNDK − SOXX |
|---|---|---:|---:|---:|---:|---:|---:|
| As-of | 2025-06-16 | $44.21 | — | — | — | — | — |
| +6mo | ~2025-12-16 | $209.31 | **+373.4%** | ~+13%* | ~+30%* | ~ +360 pt | ~ +343 pt |
| +12mo / to-2026 | 2026-06-16 | **$1,991.55** | **+4,404.8%** | **+26.4%** | **+165.7%** | **+4,378 pt** | **+4,239 pt** |
| (2 days later) | 2026-06-18 | $2,184.75 | +4,841% | — | — | — | — |

\* Intermediate +6mo SPY/SOXX points are approximate/interpolated; the **to-2026 (12mo)**
SPY/SOXX figures are direct StatMuse total-return reads anchored to the same 2025-06-16 /
2026-06-16 dates as SNDK. The single anchored window is decisive — SNDK beat even the
semiconductor index SOXX by ~4,239 pts, so this is not a semi-cycle beta ride.

Source prices (direct StatMuse reads + cross-checks):
- SNDK: 209.31 (2025-12-16), **1,991.55 (2026-06-16)**; cross-checked 2,184.75 (2026-06-18,
  stockanalysis.com + investing.com), 52-wk range $40.10–$2,191.69.
- SPY: total return +26.4% (2025-06-16 → 2026-06-16; to-date close $748.40; 673.29 @2025-12-16).
- SOXX: total return +165.7% (2025-06-16 → 2026-06-16; to-date close $591.24).

**Worst drawdown along the path:** lowest close **$40.69 on 2025-08-07 = −8.0%** from the
as-of $44.21 (52-wk intraday low $40.10 per stockanalysis ≈ −9.3%). **Shallow and brief** — it
fell into exactly the **$32–$42 / "$38.50 secondary–$32.11 April-low" forced-seller ADD zone the
card pre-specified**, then turned. A holder following the locked plan was never more than ~8–9%
underwater on close, and the card's own add-on-weakness trigger ($32–$42) would have **fired into
that August dip**, adding lower before the vertical move. There was no prolonged "falling knife"
stretch; the drawdown vindicated, not punished, the entry.

### Price source(s) — cross-checked per the bad-data warning
Two independent providers, plus the (now-vindicated) CSV:
1. **StatMuse Money** — $1,991.55 close on 2026-06-16 (identical to the CSV value the warning
   flagged as "bad").
2. **stockanalysis.com / Investing.com** — $2,184.75 on 2026-06-18, 52-wk range $40.10–$2,191.69,
   1-yr change ~+4,590%.
The two-source magnitude (≈ +4,400% to-date, ATH the same week) is orders of magnitude larger
than any plausible provider error — **source error cannot flip, or even dent, the WINNER label.**

### Mechanical label
**WINNER (PROVISIONAL).** Overwhelmingly decisive: **+4,404.8%** vs **SPY +26.4%** (beat by
~4,378 pts) and vs the **SOXX semiconductor index +165.7%** (beat by ~4,239 pts), with the
thesis confirmed in the bull's favor — the spin-off forced-seller discount closed and the
guided NAND/AI up-cycle materialized far beyond the guide. PROVISIONAL only because the anchor
is ~12 months (round convention flags single-window extremes pending a 24m confirmation that the
squeeze does not fully round-trip); the label itself is not in doubt at this magnitude.

### Did the binding constraint resolve, and which way?
The card's binding constraint was *"is the NAND up-cycle DURABLE AI demand (undersupply) vs
short-term restocking, and can the standalone team deliver the guided margin recovery."* Realized
**emphatically in the bull's favor**: AI-grade NAND demand drove a genuine shortage, pricing rose
hard, and Sandisk (sub-scale, thin float, below-book entry) re-rated vertically. **None** of the
six kill-criteria fired adversely (margins did NOT roll below 22.7%; demand was NOT mere
restocking; no JV-stress crystallization; balance sheet did not deteriorate; no value-destructive
governance move; no key-exec reset). The exact risk the card sized *down* for — restocking, not
durable demand — is the risk that **did not materialize**, which is why the outcome is a
top-of-table winner.

---

## 3. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, Winner row:
- PASS = `STARTER` or `CORE` (or explicit structured starter)
- PARTIAL = `WATCH` but names the correct key variable + clear buy/add trigger
- FAIL = `REJECT`, or `WATCH / 0%` with avoid framing

Locked new-money verdict = **STARTER** (real 3% money at as-of, an explicit add-on-weakness AND
add-on-confirmation path, **ADD** for the under-weight existing holder). It avoided REJECT,
avoided WATCH/0%, and reached a real-ownership tier on the exact name the methodology was built
around.

**Axis-1 = PASS.**

This is the redesign working as designed, on the case it was *named after*. `WEIGHTING_HARNESS §5`
explicitly says the Starter rule "is specifically meant to catch cases like **SNDK 2025** or NVDA
2023 where a classic full-MOS process may be too slow," and `METHODOLOGY §6` carries **SNDK
2025-06-16 as its worked example**, prescribing exactly *"Starter 3–4% → confirm → 8–10% → cyclical
capped ~12–15%."* The old pipeline pinned SNDK to 1.5% with an uncertainty-as-veto haircut; the
lean pipeline produced **STARTER 3% with a 12% ceiling and an explicit add path** — i.e. it
reproduced the methodology's own intended answer and avoided the `confidence_used_as_veto` disease
(M1 = 0, "one standalone quarter → size haircut + wider band + monitoring, NOT a WATCH/0% cap").

### Size-distance (0–3)

Correct size band (sealed, per the methodology's own SNDK example + the spinoff/cyclical context):
**STARTER** (with a confirmation-gated path up the ladder; the cyclical nature caps the ceiling
below Core). Realized outcome = an extreme WINNER, **+4,404.8% / ~45×**.

Locked sizing: initial **3%** (low end of the 3–5% Starter band), max **12%** (Confirmed-tier
ceiling), with **two** explicit add paths — add-on-weakness into $32–$42 **and**
add-on-confirmation on a clean margin+demand quarter.

Scoring against the literal PROTOCOL §6 scale and `METHODOLOGY §7` ("a winner identified only as a
tiny STARTER is **not** full marks"):

- **Band:** the initial **3% sits squarely inside the sealed STARTER band** (it is the
  methodology's own prescribed entry, "Starter 3–4%") → by the literal size-distance scale this is
  **0** (within the correct band). This is NOT a GOOGL/NVDA-style "should-have-been-Core" case: the
  sealed/right answer genuinely **is** Starter, because at as-of this is a `spinoff_forced_seller`
  cyclical on **one standalone quarter** — a fat STARTER with a confirmation-gated ladder is the
  correct underwrite, not a timid version of a Core call.
- **`too_small_missed_asymmetry` pressure exists but is materially mitigated, and is *secondary*:**
  - (a) The sealed band **is** Starter, so 3% is the target, not a floor the card shrank from.
  - (b) The **12% ceiling is the methodology-correct cap for a confirmed cyclical** (`METHODOLOGY
    §2`: a confirmed cyclical caps ~Confirmed 10–15%; the 15–25% Core tier is reserved for 5–10-year
    hold-through-anything compounders, which a NAND cyclical with a JV-shared cost base is not). The
    card reasoned to exactly that ceiling for exactly that reason — the dissent even argues 12% is
    "Confirmed," not Core, *on durability grounds*. Capping a cyclical at Confirmed is the framework
    behaving correctly, not under-sizing.
  - (c) The realized path **front-loaded the add trigger**: the −8% August dip fell straight into
    the card's pre-named $32–$42 add zone, and the Q4/subsequent margin+demand confirmation landed —
    so *both* add paths the card specified would have fired and routed the position toward the 12%
    ceiling **before** the vertical move, capturing far more than the 3% entry implies.
  - The only uncaptured asymmetry is the truly extreme tail (45×) versus a 12% cyclical ceiling.
    But no disciplined cyclical framework sizes for a 45× NAND-squeeze tail ex ante; that tail is a
    thin-float/shortage anomaly, not a durability the card could underwrite at as-of. So
    `too_small_missed_asymmetry` is a **soft/secondary** note (as on AMZN), not a primary failure,
    and it does **not** move the band score.

Net: the **band is correct (0)** — the entry sits in the sealed STARTER band that the methodology
itself prescribes for this exact case, the 12% ceiling is the right (Confirmed) cyclical cap, and
the realized path front-loaded the add triggers. There is no "methodology says this is a Core name"
tension pulling it to a 1 (the way there is for NVDA/AAPL), because the right answer *was* Starter.

**Size-distance = 0** (entry inside the sealed STARTER band — the methodology's own SNDK entry;
12% Confirmed ceiling correct for a cyclical-at-entry; both add paths matched the front-loaded
weakness + confirmation). `too_small_missed_asymmetry` noted **soft/secondary only** for the 45×
tail vs a 12% cyclical cap — but the cap is methodology-correct and the tail is an un-underwritable
squeeze anomaly, so it does not lift the score to 1.

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes — precisely. The card's binding constraint is *"whether the
  NAND up-cycle is DURABLE demand (AI/enterprise-SSD undersupply) rather than short-term restocking,
  and whether the standalone team can deliver the guided margin recovery."* That is exactly the
  variable that resolved — and it resolved in the bull's favor (real AI-NAND shortage, pricing up,
  re-rate). The card also correctly identified the *mechanism of the dislocation* (forced WDC
  selling + a $1.83B non-cash-impairment-masked GAAP loss depressing a **below-book** price) and the
  *engine of upside* (AI/enterprise-SSD undersupply), and tagged the durability question as
  *unresolved at as-of* rather than resolving it with hindsight.
- **Right module dominance?** Yes. The call was carried by the **M2 (+1) / M4 (+1) / M6 (+2)** stack
  with M1 (0) correctly converting the one-quarter evidence gap into a haircut (not a veto): M2 named
  the forced-seller + cyclical-inflection dislocation; **M4 (Financial Reality)** did the decisive
  work — normalizing the −$13.33 GAAP loss through the $1.83B non-cash impairment to a −$0.30
  trough, reading the guided-up Q4 + the **below-book (~0.70×)** asset value as a trough masked by a
  charge; **M6 (+2)** flagged the favorable below-asset-value asymmetry. M3 (0) correctly withheld
  durability credit (commodity-cyclical, JV-shared cost base, 3/5 brand-new operator team), and
  **M5 (−1) sized down without vetoing** (no structural-decline trap, no false-cheap trap, balance
  sheet survives net debt ~$0.44B). That is precisely the intended `spinoff_forced_seller` pattern
  (`WEIGHTING_HARNESS §4`: positive emphasis **M1/M2/M4**, + M6 price), with the cyclical overlay's
  M5 acting as a size cap.
- **No lookahead?** On the face of the card, clean — it draws only on pre-2025-06-16 evidence (Q3
  FY25 release 2025-05-07, 10-Q 2025-05-12, Form 10/A, S-1/A, the 2025-06-06 secondary pricing,
  TrendForce 2025-05-26, Micron Q2'25 2025-03-20, the verified as-of close) and explicitly flags the
  Q4 FY25 print and WDC's remaining-stake disposal as *forward monitor items, not evidence*. (Full
  lookahead adjudication is the Auditor's job and out of Scorer scope; on the face of the card,
  clean.)

**Reasoning = sound.** Correct key variable (durable-demand-vs-restocking on a below-book trough),
correct module dominance (M2/M4/M6 with M4 doing the load-bearing normalization; M1=0 haircut not
veto; M5 size-down not veto), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (sealed/`WEIGHTING_HARNESS §4` for `spinoff_forced_seller` + cyclical overlay):
  **M1/M2/M4** (with M6 price; M5 for the cyclical overlay). In practice the load-bearing pair is
  **M2 (dislocation/mechanism) + M4 (normalize the impairment-masked trough)**, with M6 the price
  trigger.
- **Got:** the call was carried by **M2 + M4 + M6** — M4 (Financial Reality) being the single most
  load-bearing module (the entire STARTER-not-avoid call hinges on normalizing the −$13.33 GAAP loss
  through the $1.83B non-cash impairment and reading the below-book price as a trough), M2 framing
  the forced-seller dislocation, M6 (+2) supplying the favorable-asymmetry price.

**dominant_module (got) = M2/M4 (M6 +2 co-load-bearing on price); dominant_module_expected =
M1/M2/M4.** **Match / near-match** — the expected M2 and M4 are the realized leads, and M4-leading a
spinoff/cyclical normalization is exactly the correct behavior (it normalized the headline trap in
the bull's favor, the mirror of the AMZN success and the *opposite* of the INTC-2024 over-veto).
Not scored as a mismatch.

### Veto (fired vs expected)

- **veto_expected = no** (sealed; `spinoff_forced_seller` → veto only if separation economics fail —
  they did not; balance sheet survivable, net debt ~$0.44B, below book).
- **veto_fired = no.** No hard veto fired; M5 (−1) acted as a size cap and M1 (0) as a haircut, not a
  kill. **Match** — and correct: a hard veto here (the old uncertainty-as-veto reflex) would have
  produced the WATCH/0% failure and missed a 45× winner. This is the `WEIGHTING_HARNESS §0` disease
  the redesign exists to cure, and it did not fire.

### Failure tags (from `WEIGHTING_HARNESS §7` list)

Candidate review:
- `confidence_used_as_veto` — **NOT present** (the headline pass). One standalone quarter →
  M1 = 0, size haircut + wider band + monitoring, *not* a WATCH/0% downgrade. Exactly the old
  disease, avoided, on the case the harness names.
- `trailing_accounting_trap` — **NOT present (avoided in the bull direction).** The −$13.33 GAAP
  loss was a two-way trap; M4 normalized through the $1.83B non-cash goodwill impairment to a
  −$0.30 trough and read the below-book asset value correctly, rather than letting the optically
  catastrophic trailing GAAP force an avoid. Correctly handled (mirror of AMZN, opposite of
  INTC-2024).
- `valuation_underweighted` / `valuation_overweighted` — **NOT present.** M6 read price on a
  below-book / EV-to-run-rate basis (not meaningless trailing GAAP) and emitted +2; it supported,
  not gated, the starter.
- `hold_winner_failed` — **NOT present.** Existing-position **ADD** (not HOLD/TRIM) on an
  under-weight, below-book, asymmetric setup is correct; a holder who added was emphatically right.
- `no_add_rule` / `no_trim_rule` — **NOT present** (both explicit; the add path is doubly specified —
  on weakness into $32–$42 AND on confirmation — and the no-chase/trim discipline is stated).
- `too_small_missed_asymmetry` — **soft / secondary only.** The name 45×'d and a 3%→12% cyclical
  ceiling leaves the extreme tail uncaptured. But (a) the sealed band IS Starter, so 3% is the
  target; (b) the 12% ceiling is the methodology-correct Confirmed cap for a cyclical; (c) the
  front-loaded path (the −8% August dip into the pre-named add zone + the confirmation quarter) would
  have routed the position toward 12% before the melt-up; (d) a 45× thin-float NAND-squeeze tail is
  not underwritable ex ante. So this is a *weaker* instance than even AMZN's and does **not** rise
  to a primary failure.

**failure_tags = none (primary).** `too_small_missed_asymmetry` noted soft/secondary only —
weaker than the NVDA/AAPL instances, because the sealed target band *is* Starter, the 12% ceiling is
the methodology-correct cyclical cap, and the realized win front-loaded onto the card's own add
triggers (the August dip into $32–$42 + the confirmation quarter).

---

## 4. Verdict

The lean 6-module pipeline **got SNDK right on every axis** — on the single case the methodology
was *built around* (`METHODOLOGY §6` worked example; `WEIGHTING_HARNESS §5` names "SNDK 2025" as the
Starter-rule archetype). It produced a **STARTER (3% real money, ADD for under-weight holders, two
explicit add paths, 12% Confirmed-tier ceiling)** on a name that realized as the most extreme WINNER
of the round — **+4,404.8% / ~45×, beating SPY by ~4,378 pts and the SOXX semi index by ~4,239 pts**
to-date — with the thesis confirmed (the forced-seller below-book discount closed and the guided
AI-NAND up-cycle over-delivered). Axis-1 **PASS**, **size-distance 0** (entry inside the sealed
STARTER band — the methodology's own SNDK entry; correct cyclical Confirmed ceiling; both add paths
matched), reasoning **sound** (the correct durable-demand-vs-restocking key variable, an M4-led
normalization of an impairment-masked below-book trough, no visible lookahead), and **no primary
failure tag**.

The decisive, transferable results:
1. **Data-integrity:** the "bad data" $1,991.55 was the **real** price — the scorer must verify
   before discounting; here the warning was a decoy and discounting it would have mis-scored the
   round's clearest winner.
2. **The redesign's core fix, vindicated on its namesake case:** one standalone quarter +
   forced-seller mess + a −$13.33 GAAP loss is *exactly* the setup the old pipeline pinned to 1.5%
   with `confidence_used_as_veto` / `trailing_accounting_trap`. The lean pipeline instead set
   M1 = 0 (uncertainty → haircut), let M4 normalize the impairment-masked below-book trough, sized
   M5 down without vetoing, and produced a real STARTER with a confirmation-gated ladder — the
   methodology's own prescribed answer.
3. **Path-vindicated, unlike NVDA/AAPL:** the worst drawdown (−8% into the card's own $32–$42 add
   zone) and the front-loaded confirmation mean the add triggers would have fired *early and lower*,
   so even the soft "too small" note is largely answered.

Net grade: a **clean, well-reasoned PASS** — alongside AMZN, one of the strongest cases of the
round (size-distance 0, no primary failure tag), and the canonical demonstration that the lean
pipeline cures the exact disease it was designed to cure. **PROVISIONAL** on the ~12-month window
only (a 45× single-year move warrants a 24m confirmation that the AI-NAND squeeze does not fully
round-trip), but the WINNER label and the PASS grade are not in doubt at this magnitude.

---

## 5. results.csv row (DO NOT auto-append — returned to orchestrator)

```
lean-6module-v1,none,sndk_2025-06-16,spinoff_forced_seller,WINNER,3,STARTER,ADD,STARTER,0,no,no,M2/M4,M1/M2/M4,sound,none,"WINNER (PROVISIONAL ~12mo) +4404.8% to 2026-06-16 (price=t.r.; no div) from $44.21 to $1991.55 vs SPY +26.4%/SOXX +165.7%; beat SPY ~4378pt, SOXX ~4239pt. +6mo +373.4% ($209.31 @2025-12-16). Worst DD only -8.0% close $40.69 @2025-08-07 (52wk low $40.10) -> fell INTO the card's pre-named $32-42 add zone then turned; both add paths (weakness $32-42 + confirmation quarter) front-loaded. DATA-WARNING RESOLVED: the 'bad' CSV $1991.55 is the REAL price (StatMuse $1991.55 @2026-06-16 = exact CSV match; stockanalysis/investing $2184.75 @2026-06-18, 52wk $40.10-$2191.69, 1yr +4590%); continuous unsplit series, genuine AI-NAND shortage + thin spun-off float + strong Q3'26 print = sane not garbled. Axis-1 PASS (STARTER avoided old WATCH/0%/1.5% uncertainty-veto on the methodology's OWN named archetype - WEIGHTING_HARNESS §5 'SNDK 2025', METHODOLOGY §6 worked example). size-dist 0 (3% entry = the sealed/methodology STARTER band; 12% Confirmed ceiling = correct cyclical cap below Core; add paths matched front-loaded weakness+confirmation). Reasoning sound: correct key var (durable AI/enterprise-SSD undersupply vs restocking, resolved bull); M4-led normalization of a two-way headline trap (-$13.33 GAAP = $1.83B non-cash goodwill impairment -> -$0.30 trough; price ~0.70x BOOK); M1=0 one-quarter=haircut not veto (cures confidence_used_as_veto); M5 -1 sized down no veto (survivable net debt ~$0.44B). Dominant M2/M4 got (M6 +2 co-load-bearing on below-book price) vs M1/M2/M4 expected = match; M4-lead correct for spinoff/cyclical (mirror of AMZN success, opposite of INTC-2024 over-veto). No primary failure tag; too_small_missed_asymmetry soft-only (45x tail vs 12% cyclical cap, but cap is methodology-correct & a thin-float squeeze tail is un-underwritable ex ante & add paths front-loaded). NO trailing_accounting_trap, NO confidence_used_as_veto. Existing=ADD correct (under-weight, below-book, asymmetric). Clean, no visible lookahead. PROVISIONAL: 24m confirmation pending that the squeeze doesn't round-trip. Sources: StatMuse (anchored 2025-06-16/2026-06-16) + stockanalysis.com/investing.com to-date 2-source cross-check (vindicating the flagged-bad CSV)."
```

---

*Scorer used post-2025-06-16 data (allowed). Locked `decision_card.json` / `decision_card.md` NOT
modified. The flagged-"bad" CSV value $1,991.55 was independently verified as the REAL price (2
sources) and used. No pre-as-of price used as a post-as-of drawdown; benchmark returns anchored to
the same 2025-06-16 / 2026-06-16 dates as SNDK. Version `lean-6module-v1` / `none` matches the card
(VERSIONS.md current ACTIVE). `_v0/` not read. WINNER label PROVISIONAL on the ~12-month window.*
