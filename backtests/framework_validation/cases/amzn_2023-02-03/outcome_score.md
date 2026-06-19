# Outcome Scorecard — AMZN (Amazon.com, Inc.), as-of 2023-02-03

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-as-of market data (allowed for the
> Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` §7 (position ladder), and
> `WEIGHTING_HARNESS.md` §7.
>
> Sealed expectation (Runner never saw it): **WINNER**, context
> `quality_compounder / cyclical_inflection`, key variables *retail margin trough /
> AWS durability / cost discipline*, **expected band STARTER** (PROTOCOL §7 row 4).

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | cyclical_inflection (quality_compounder underlay) |
| Business verdict | good |
| New-money verdict | **STARTER** |
| Existing-position verdict | HOLD |
| Suggested initial size | **4%** (Starter tier) |
| Suggested max size | **12%** (Confirmed-tier ceiling) |
| Buy-below / starter zone | ≤ ~$110 (as-of $103.39) |
| Add zone | ~$80–$95 on weakness, OR any price on a clean forward confirmation (retail-margin recovery + capex moderating/FCF turning + AWS-growth stabilizing) |
| Binding constraint | Whether FY22 retail losses + ~$2.7B charges + AWS decel are a normalizable cost/margin TROUGH or a structural step-down, compounded by FY22 FCF −$11.6B that only normalizes IF capex moderates → a SIZE cap, not a veto |
| Module signals | M1 0 / M2 +1 / M3 +1 / M4 +1 / M5 −1 / M6 +1 |
| Hard veto | None fired |

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **AMZN $103.39 on 2023-02-03** (post 20-for-1 split; matches `case_control.md`).
AMZN paid **no dividend** over the window, so **price return = total return** — no
reinvestment adjustment needed.

| Window | Date used | AMZN close | AMZN return | SPY (price) | QQQ (price) | AMZN − SPY | AMZN − QQQ |
|---|---|---:|---:|---:|---:|---:|---:|
| As-of | 2023-02-03 | $103.39 | — | $395.29 | $300.38 | — | — |
| +6mo | 2023-08-03 | $128.91 | **+24.7%** | ~+13%* | ~+10%* | ~ +12 pt | ~ +15 pt |
| +12mo | 2024-02-02 | $171.81 | **+66.2%** | **+21.7%** | **+41.1%** | **+44.5 pt** | **+25.1 pt** |
| +18mo | 2024-08-02 | $167.90 | **+62.4%** | ~+33%* | ~+45%* | ~ +29 pt | ~ +17 pt |
| ~today | 2026-06-16 | $246.00 | **+137.9%** | **+89.8%** | **+143.0%** | **+48.1 pt** | **−5.1 pt** |

\* Intermediate SPY/QQQ points (+6mo, +18mo) are interpolated/approximate; the **+12mo and
to-2026** SPY/QQQ figures are direct StatMuse closing-price reads, anchored to the same
2023-02-03 / 2026-06-16 dates as AMZN. The two anchored windows are sufficient to classify.

**Benchmark note (total return).** The table uses **price-only** benchmark returns computed
from anchored closing prices. Adding dividends: SPY (~1.4%/yr) → t.r. ≈ **~+95%** to-date;
QQQ (~0.6%/yr) → t.r. ≈ **~+146%** to-date. AMZN pays no dividend, so its +137.9% is already a
total return. Net: AMZN **beat SPY by ~43–48 pts** and finished **roughly in-line-to-slightly-
behind QQQ** (≈ +138% vs ≈ +143–146%) over ~3.4 years.

Source closing prices (direct StatMuse reads, the same provider the case used to verify the
as-of price, S008):
- AMZN: 128.91 (2023-08-03), 171.81 (2024-02-02), 167.90 (2024-08-02), 246.00 (2026-06-16).
  To-date double-confirmed: stockanalysis.com shows $244.39 on 2026-06-18 — same ~$244–246 level.
- SPY: 395.29 (2023-02-03), 481.10 (2024-02-02), 750.42 (2026-06-16).
- QQQ: 300.38 (2023-02-03), 423.79 (2024-02-02), 729.89 (2026-06-16).

**Worst drawdown along the path:** close **$90.73 on 2023-03-10 = −12.3%** from the as-of
$103.39 — the mid-March-2023 SVB / regional-banking selloff. Shallow and short: March 9 $92.25,
March 10 $90.73 (trough), March 13 $92.43; **recovered back above the $103.39 entry by late
April 2023** ($104.98 on 2023-04-26), i.e. the entire drawdown was a ~7-week dip. (The
2023-01-05 low of $83.12 is **PRE-as-of** and excluded. The broad April-2025 "Liberation Day"
selloff that troughed GOOGL/INTC **never touched the entry** for AMZN — AMZN's 2025 low was
$167.32 on 2025-04-21, **+61.8% ABOVE** the $103.39 base.) Source: StatMuse per-date closes.

### Price source(s)
StatMuse Money historical series (provider used for the as-of verification, S008); per-date
closing-price endpoints, anchored precisely to 2023-02-03 and 2026-06-16 for both AMZN and the
benchmarks. To-date AMZN cross-checked against stockanalysis.com ($244.39, 2026-06-18). The
~+138% magnitude is far larger than any plausible provider error, so source error cannot flip
the WINNER label.

### Mechanical label
**WINNER.** Decisive: **+137.9% vs SPY +89.8% (t.r. ~+95%)** — **beat SPY by ~43–48 pts** over
~3.4 years — with the thesis confirmed (margin trough normalized, AWS stayed durable, FCF turned
strongly positive). vs QQQ it finished roughly in-line-to-slightly-behind (≈ +138% vs ≈ +143–146%
t.r.), but a strong absolute gain + a wide S&P beat + a confirmed thesis is a clear WINNER under
the PROTOCOL §6 threshold. **Confirms the sealed expectation** (AMZN = WINNER,
quality_compounder / cyclical_inflection).

**Path note (load-bearing for grading size — and the key contrast with the GOOGL/INTC cases):**
this win was **FRONT-loaded**, not back-loaded. AMZN was **already +66.2% at +12mo and BEATING
SPY by ~44 pts and QQQ by ~25 pts at that mark**, and its worst drawdown from entry was a shallow
−12.3% that fully reversed inside ~7 weeks. The trough-vs-structural question the card flagged as
binding resolved **favorably and fast**: the cost cuts + capex shift restored retail margin, AWS
growth stabilized then re-accelerated, and FY22's −$11.6B FCF swung to large positive FCF. The
investor following the locked plan was in profit and ahead of the index within the first year and
never sat on a meaningful loss — there was no year-long "did I catch a falling knife" stretch.

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, Winner row:
- PASS = `STARTER` or `CORE` (or explicit structured starter)
- PARTIAL = `WATCH` but names the correct key variable + clear buy/add trigger
- FAIL = `REJECT`, or `WATCH / 0%` with avoid framing

Locked new-money verdict = **STARTER** (4% real money, explicit add-on-confirmation path, HOLD
for existing holders). It avoided REJECT and avoided WATCH/0%, and reached a real-ownership tier.

**Axis-1 = PASS.**

This is the redesign working as intended. The card explicitly converted the binding
trough-vs-structural / FCF-normalization uncertainty into a **size haircut + wider add band, NOT a
confidence veto** (M1 signal **0**, "high evidence quality, forward-interpretive uncertainty →
haircut"), and explicitly normalized through the non-cash −$12.7B Rivian mark + the ~$2.7B charges
instead of letting the headline net LOSS trigger an avoid. That is precisely the
`confidence_used_as_veto` / `trailing_accounting_trap` disease WEIGHTING_HARNESS §0 was built to
cure, and the pipeline did not fall into it.

### Size-distance (0–3)

Correct size band (sealed, PROTOCOL §7 row 4): **STARTER** (singular — narrower than GOOGL's
STARTER..CORE; the sealed sheet caps AMZN's expected entry at Starter precisely because at as-of
this is underwritten as a *cyclical_inflection* whose normalization is unconfirmed). Realized
outcome = WINNER, +137.9% / ~2.4×.

Locked sizing: initial **4%** (the top half of the 3–5% Starter band), max **12%** (Confirmed-tier
ceiling), with an **explicit, well-specified add-on-confirmation path** (~$80–$95 on weakness OR a
clean quarter confirming retail-margin recovery + FCF turning positive + AWS-growth stabilizing).

Scoring against the literal scale and METHODOLOGY §7:

- The initial **4% sits exactly in the sealed STARTER band** → not a band miss. By the literal
  PROTOCOL §6 size-distance scale this is **0** (within the correct band). Unlike GOOGL — where the
  methodology itself files the name in the **Core (15–25%)** tier and a 4%/12% entry therefore
  skews timid (→ size-distance 1) — the sealed sheet here says the *correct* answer **is** Starter,
  so 4% is not under-sized relative to what the case was supposed to produce.
- METHODOLOGY §7's "a winner sized only as a tiny STARTER is NOT full marks" pressure is **much
  weaker here than for GOOGL**, for three reasons: (a) the sealed band is STARTER, so Starter is the
  target, not a timid floor; (b) the **12% Confirmed ceiling was the right ceiling** — a *cyclical*
  recovery caps around Confirmed (~10–15%) per METHODOLOGY §2 until durability is proven, and the
  card reasoned to exactly that ceiling for exactly that reason; (c) the realized path was
  **front-loaded** — the add trigger (a clean confirmation quarter) would have fired within ~2–3
  quarters as retail margin recovered and FCF turned, routing the position up toward the 12% ceiling
  *while* the stock was still well below its eventual level.
- The only residual asymmetry left uncaptured: AMZN ultimately ~2.4×'d, and a 4%→12% cyclical
  ceiling is, with hindsight, below what a "quality_compounder underlay that proved durable" could
  have justified. But that is the *quality_compounder-graduates-to-Core* upgrade question, which the
  card explicitly flagged ("the quality_compounder underlay could justify a higher ceiling IF the
  retail trough proves cyclical and AWS growth stabilizes") and correctly **gated on a forward
  confirmation it could not have at as-of**. Holding a cyclical at a Confirmed ceiling until
  durability is proven is the methodology behaving correctly, not a sizing error.

Net: the **band is correct (0)** and, unlike GOOGL, there is no "methodology says this is a Core
name" tension pulling it to a 1 — the sealed target *was* Starter and the card delivered Starter
with the right (Confirmed) ceiling and an add path that the front-loaded realized fundamentals
would have triggered.

**Size-distance = 0** (entry inside the sealed STARTER band; 12% Confirmed ceiling correct for a
cyclical-at-entry; explicit add path matches the front-loaded confirmation). A soft, secondary
`too_small_missed_asymmetry` note still applies for the ultimate ~2.4× vs a 12% cap, but it does
not move the band score.

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes — precisely. The card's binding constraint is "whether the
  FY22 retail-segment operating losses + ~$2.7B charges + AWS deceleration are a normalizable cost/
  margin **TROUGH** or a structural step-down, compounded by FY22 FCF −$11.6B that only normalizes
  IF capex moderates." The sealed key variables are "retail margin trough / AWS durability / cost
  discipline." These **match exactly**. Realized history confirms the framing in the bull's favor:
  the retail margin recovered off the trough, AWS durability held (decel was an optimization pause,
  not share loss — peers also bottomed then re-accelerated), the cost cuts + build→optimize capex
  shift landed, and FY22's −$11.6B FCF swung strongly positive. The card identified the right
  upside engine (AWS + ad high-margin pools) AND the one genuinely unresolved risk
  (trough-vs-structural) and correctly tagged the risk as *unresolved at as-of* rather than
  resolving it with hindsight.
- **Right module dominance?** Yes. The conviction stack **M2 +1 / M3 +1 / M4 +1** drove the
  STARTER (theme = margin-trough franchise; profit-pool/durability = AWS annuity + ad + scaled
  retail moat with operator grade 4/5; financial-reality = normalize through the non-cash mark, op
  income still +$12.2B, OCF intact). **M4 (Financial Reality)** is the single most load-bearing
  module — the entire call hinges on *normalizing* the headline net loss (the −$12.7B Rivian mark)
  and reading the charges + retail losses as trough rather than steady-state, which is M4's job and
  is exactly what the redesign needed to get right. **M6 +1** supported entry at price; **M5 −1
  (no veto)** correctly sized it down rather than killing it. That is the intended dominance pattern
  for a cyclical_inflection (WEIGHTING_HARNESS §4: positive emphasis M2/M4/M5).
- **No lookahead?** On the face of the card, clean — it draws only on pre-2023-02-03 evidence
  (Q4'22 release tables, FY22 10-K filed 2023-02-03, the 2023-02-02 call, the Jan-2023 layoff
  message, MSFT/GOOGL peer prints) and explicitly flags Q1'23+ results, the March-2023 additional
  layoffs, and any AWS re-acceleration as *forbidden / forward monitor items*. (Full lookahead
  adjudication is the Auditor's job and out of Scorer scope; on the face of the card, clean.)

**Reasoning = sound.** Correct key variable, correct module dominance (M4-led conviction stack,
which is the harder, more valuable read here), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (sealed key variables + METHODOLOGY for a quality_compounder/cyclical_inflection):
  **M2/M3** (theme + profit-pool/durability), with M4 financial-reality confirmation.
- **Got:** the call was carried by the **M2/M3/M4 conviction stack**, with the single most
  load-bearing module being **M4 (Financial Reality)** — the normalization through the non-cash mark
  + the trough-not-steady-state read of the charges/retail losses is what made a STARTER (rather
  than an avoid) defensible, and is also what `cyclical_inflection` weights heavily. M3 (AWS
  durability + ad pool + operator 4/5) is co-dominant; M2 (margin-trough-franchise theme) frames it.

**dominant_module (got) = M4** (with M3 co-dominant); **dominant_module_expected = M2/M3.**
This is a **near-match / acceptable**: the *expected* M3 is co-dominant and the realized
dominance leans to **M4**, which is the correct lead module for a `cyclical_inflection`
(WEIGHTING_HARNESS §4) and is the module that actually did the decisive work (normalizing the
headline trap in both directions). Not scored as a mismatch — M4-leading a cyclical-inflection
normalization is the right behavior, and it confirmed rather than fought the M2/M3 thesis.

### Failure tags (from WEIGHTING_HARNESS §7 list)

Candidate review:
- `confidence_used_as_veto` — **NOT present.** The explicit fix: M1=0, forward-interpretive
  uncertainty → size haircut + wider band, *not* a WATCH/0% downgrade. This is the old disease the
  redesign avoided, and avoiding it is the headline pass.
- `trailing_accounting_trap` — **NOT present (avoided in the bull direction).** The headline FY22
  net LOSS was a two-way trap; the card normalized through the −$12.7B non-cash Rivian mark and read
  operating income (+$12.2B) and OCF ($46.8B) correctly, rather than letting the optically broken
  trailing metrics force an avoid. Correctly handled.
- `valuation_overweighted` — **NOT present.** M6 read price on a *normalized sum-of-pools* basis
  (explicitly NOT trailing earnings, which were meaningless here) and supported a starter; it did
  not gate the name on "not optically cheap."
- `hold_winner_failed` — **NOT present.** Existing-position **HOLD** with no thesis-break trigger
  is correct; the thesis was intact and compounding (price = total return +137.9%). A holder who
  held was right.
- `no_add_rule` / `no_trim_rule` — **NOT present** (both explicit and well-specified; the add path
  is gated on the exact confirmations that subsequently landed).
- `too_small_missed_asymmetry` — **soft / secondary only.** The name ~2.4×'d and a 4%→12% cyclical
  ceiling leaves some terminal asymmetry uncaptured. But (a) the sealed band IS Starter, so 4% is
  the *target*, not timid; (b) the 12% ceiling is the methodology-correct Confirmed cap for a
  cyclical-at-entry; (c) the front-loaded path would have routed the position up toward 12% on the
  early confirmation. So this is a *much weaker* version of the GOOGL flag and does not rise to a
  primary failure.

**failure_tags = none (primary).** `too_small_missed_asymmetry` noted as soft/secondary only,
weaker than the GOOGL instance because the sealed target band is Starter and the realized win was
front-loaded onto the card's own add trigger.

---

## 3. Verdict

The lean 6-module pipeline **got AMZN right on every axis.** It produced a **STARTER (4% real
money, HOLD for holders, explicit add-on-confirmation path, 12% Confirmed-tier ceiling)** on a name
that realized as a clear **WINNER (+137.9%, beating SPY by ~43–48 pts and finishing in-line with
QQQ)** — Axis-1 **PASS**, **size-distance 0** (entry inside the sealed STARTER band, correct
cyclical Confirmed ceiling), reasoning **sound** (the correct trough-vs-structural key variable,
an M4-led normalization of a two-way headline trap, no visible lookahead), and **no failure tag**.

The decisive, transferable result: this is the case where the pipeline had to **normalize through
an optically catastrophic headline** (a reported net LOSS that was a non-cash Rivian mark, both
retail segments in operating loss, −$11.6B FCF, four straight quarters of AWS deceleration) and
**not** let any of those trigger a `trailing_accounting_trap` / `confidence_used_as_veto` avoid —
exactly the failure it committed on INTC-2024 (where it over-weighted M4/M5 into a near-veto on a
survivable reset). Here it did the opposite and correct thing: M1=0 (uncertainty→haircut), M4
normalized the trap in both directions, M5 −1 sized down without vetoing, and the name was sized as
a real Starter with a confirmation-gated path to Confirmed. The win was **front-loaded** (+66% and
beating both indices by +12mo, worst drawdown only −12.3% for ~7 weeks), which means even the soft
"too small" asymmetry note is largely answered by the add path firing early. Net grade: a **clean,
well-reasoned PASS — the strongest of the scored cases** (cf. GOOGL PASS/size-dist-1, INTC-2024
FAIL/size-dist-3).

---

## 4. results.csv row (to append)

```
lean-6module-v1,none,amzn_2023-02-03,cyclical_inflection,WINNER,4,STARTER,HOLD,STARTER,0,no,no,M4,M2/M3,sound,none,"WINNER +137.9% to 2026-06-16 (price=t.r.; no div) from $103.39 vs SPY +89.8%(t.r.~+95%)/QQQ +143.0%(t.r.~+146%); beat SPY ~43-48pt, ~in-line-to-slightly-behind QQQ. FRONT-loaded (unlike GOOGL/INTC): +6mo +24.7%, +12mo +66.2% already BEATING SPY ~44pt & QQQ ~25pt; +18mo +62.4%. Worst DD only -12.3% @2023-03-10 $90.73 (SVB dip), recovered >entry by late Apr-2023 ~7wk; 2025 tariff trough never touched entry (2025 low $167.32=+62%). Axis-1 PASS (STARTER avoided WATCH/0%); size-dist 0 (entry in sealed STARTER band; 12% Confirmed ceiling correct for cyclical-at-entry; add path matched front-loaded confirmation). Reasoning sound: correct trough-vs-structural key var; M4-led normalization of a two-way headline trap (net LOSS=non-cash Rivian mark, op income +$12.2B/OCF intact, FY22 FCF -$11.6B->later strongly positive); M1=0 uncertainty=haircut not veto; M5 -1 sized down no veto. Dominant M4 got (M3 co-dom) vs M2/M3 expected = near-match, M4-lead correct for cyclical_inflection. No primary failure tag; too_small_missed_asymmetry soft-only (name ~2.4x vs 12% cap, but sealed band IS Starter & win front-loaded onto add trigger). Mirror-correct vs INTC-2024 (there over-weighted M4/M5 into near-veto on survivable reset; here normalized correctly). Clean, no visible lookahead. Source: StatMuse (anchored 2023-02-03/2026-06-16) + stockanalysis.com to-date cross-check."
```

---

*Scored 2026-06-19 against the locked blind decision card. The decision card was NOT modified.
No pre-as-of price (2023-01-05 $83.12 low) used as a post-as-of drawdown; benchmark returns
anchored to the same 2023-02-03 / 2026-06-16 dates as AMZN.*
