# Outcome Scorecard — GOOGL (Alphabet Class A), as-of 2024-06-14

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-as-of market data (allowed for the
> Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §7), and
> `WEIGHTING_HARNESS.md` §7.

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | quality_compounder |
| Business verdict | good |
| New-money verdict | **STARTER** |
| Existing-position verdict | HOLD |
| Suggested initial size | **4%** (Starter tier) |
| Suggested max size | **12%** (Confirmed-tier ceiling) |
| Buy-below / starter zone | ≤ ~$182 (as-of $175.44) |
| Add zone | $150–$170 on weakness, OR any price on a clean forward confirmation |
| Binding constraint | Forward durability of Search profit pool under gen-AI + capex-into-unproven-returns under disengaged founder control → a SIZE cap, not a veto |
| Module signals | M1 0 / M2 +1 / M3 +1 / M4 +1 / M5 −1 / M6 +1 |
| Hard veto | None fired |

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **GOOGL Class A $175.44 on 2024-06-14** (matches case_control.md; StatMuse S005).

All figures below are StatMuse **total return** (dividend-inclusive) from the 2024-06-14 close,
with the corresponding close price for reference. GOOGL began paying its first dividend in
2024, so total return runs slightly above raw price change.

| Window | Date used | GOOGL close | GOOGL total return | SPY t.r. | QQQ t.r. | GOOGL − SPY |
|---|---|---:|---:|---:|---:|---:|
| As-of | 2024-06-14 | $175.44 | — | — | — | — |
| +6mo | 2024-12-13 | $188.83 | **+9.2%** | ~ +14%* | ~ +15%* | ~ −5 pt |
| +12mo | 2025-06-13 | $174.17 | **+0.7%** | **+11.8%** | **+11.3%** | **−11.1 pt** |
| +18mo | 2025-12-12 | $308.89 | **+78.7%** | ~ +30%* | ~ +40%* | ~ +49 pt |
| +24mo | 2026-06-12 | $359.68 | **~+105%** | ~ +42%* | ~ +54%* | ~ +63 pt |
| ~today | 2026-06-16 | $373.39 | **+115.9%** | **+42.1%** | **+54.8%** | **+73.8 pt** |

\* Intermediate SPY/QQQ points (+6mo, +18mo, +24mo) are interpolated/approximate; the
+12mo and to-2026 SPY/QQQ figures are direct StatMuse total-return reads. The two anchored
benchmark windows are sufficient to classify the outcome; intermediate benchmark points are
directional only.

Source prices (direct StatMuse closing-price reads):
- GOOGL: 188.83 (2024-12-13), 174.17 (2025-06-13), 308.89 (2025-12-12), 359.68 (2026-06-12), 373.39 (2026-06-16).
- SPY: 529.88 (2024-06-14), 588.71 (2025-06-13), ~748 (wk 2026-06-15).
- QQQ: 524.42 (2025-06-13), ~730 (wk 2026-06-15).

**Worst drawdown along the path:** close **$144.11 on 2025-04-08** = **−17.9%** from the
as-of $175.44 (the April-2025 tariff-shock selloff). Trough-to-recovery: GOOGL printed its
low ~10 months after as-of, was still roughly flat at the +12mo mark, then re-rated ~+115%
off the as-of over the following ~12 months. Source: StatMuse min-close query 2024-06-14→2026-06-16.

### Price source(s)
StatMuse Money historical series — the same provider the case used to verify the as-of
price (S005). Queried per-date closing price and per-window total-return endpoints.
Cross-internal-consistency: derived price changes match StatMuse's own total-return
figures (e.g. 174.17/175.44 − 1 = −0.7% ≈ reported +0.7% t.r. with the dividend add-back;
373.39/175.44 − 1 = +112.8% price vs +115.9% t.r.). No second provider was needed for
classification, but the magnitude is large enough that provider error cannot flip the label.

### Mechanical label
**WINNER.** Decisive: +115.9% total return vs SPY +42.1% (**beat SPY by ~73.8 pts**) and
QQQ +54.8% over ~24 months, with the thesis intact and compounding (Cloud scaled, Search
ad pool held and AI-monetized, FCF/capital-return continued). Strong absolute gain + wide
benchmark beat = WINNER under the PROTOCOL §6 threshold. Confirms the orchestrator's sealed
expectation (GOOGL = WINNER, quality_compounder).

**Path caveat (load-bearing for grading size):** the win was **back-loaded**. At +12mo the
position was **flat (+0.7%) and LAGGING SPY by ~11 pts**, and it had drawn down ~18% along
the way. An investor following the locked plan held a 4% starter through a year of
underperformance before the +13→+24mo re-rate delivered the asymmetry. This is exactly the
profile where "right direction, too small" costs the most: the eventual move was very large
(roughly a double), so under-sizing left a lot on the table — but the year-one lag plus the
−18% drawdown means an aggressive day-one core would have been sitting on a loss/flat for 12
months on an unresolved thesis. Both facts matter for the size grade below.

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, Winner row:
- PASS = `STARTER` or `CORE` (or explicit structured starter)
- PARTIAL = `WATCH` but names the correct key variable + clear buy/add trigger
- FAIL = `REJECT`, or `WATCH / 0%` with avoid framing

Locked new-money verdict = **STARTER** (4% real money, explicit add-on-confirmation path,
buy-below $182). It avoided REJECT and avoided WATCH/0%, and reached a real-ownership tier.

**Axis-1 = PASS.**

This is the headline result for the redesign: the *old* GOOGL backtest failed this exact
case with a WATCH/0% "more-research-more-doubt" downgrade of a winner. The lean 6-module
pipeline explicitly converted the two forward unknowns (AI-Search monetization, capex
returns) into a **size haircut, not a confidence veto** (M1 signal 0 / "high evidence
quality, forward uncertainty → haircut"), which is precisely the disease WEIGHTING_HARNESS
§0 was built to cure. The redesign fixed the failure on direction.

### Size-distance (0–3)

Correct size band (sealed + METHODOLOGY): **STARTER..CORE.** Realized outcome = WINNER that
delivered ~+116% / ~2x.

Locked sizing: initial **4%** (top of the 3–5% Starter band), max **12%** (Confirmed
ceiling), with an **explicit add-on-confirmation path** ($150–170 weakness OR a clean
fundamental confirmation quarter) and a stated 12% governance-capped ceiling.

Scoring against METHODOLOGY §7 ("a winner sized only as a tiny STARTER is NOT full marks")
and the durability ladder:

- The initial 4% sits **inside the correct STARTER..CORE band** → not a band miss. By the
  literal PROTOCOL §6 size-distance scale this is **0** (within the correct band).
- METHODOLOGY's "too small loses points" pressure applies to the *initial* number for a
  name the same doc explicitly tags as belonging in the **15–25% Core tier** ("BTC, GOOGL
  belong here"). A compounder that ~doubled was entered at 4% and capped at 12% — the plan,
  if followed mechanically and never revised upward beyond confirmation, **never reaches the
  Core tier its own durability warranted**, leaving meaningful asymmetry uncaptured.
- **Mitigants that earn back the points:** (a) the explicit, well-specified add path means
  the 4% was a genuine *starter*, not a terminal size — the methodology *wants* "start real,
  add on confirmation," and the card delivered that structure; (b) the realized path
  **vindicates the caution**: the thesis stayed genuinely unresolved for ~12 months (flat,
  lagging, −18% drawdown), and the qualifying confirmation (the post-as-of prints showing AI
  Overviews/Search holding + Cloud margin scaling) is exactly what would have triggered the
  add into the +18mo re-rate; (c) the 12% ceiling, not a 4% cap, is the operative max, and
  12% is a legitimate Confirmed-tier weight for a name with a live disruption question and a
  hard governance cap.

Net: the *band* is correct (0), but METHODOLOGY §7 docks the initial 4%/12%-ceiling for a
Core-durability name that doubled. Calling it a clean 0 would ignore the doc's explicit
"GOOGL belongs in Core" + "too small loses points"; calling it a 1 reflects that the
entry+ceiling skews to the **timid** end of the correct band for the realized asymmetry,
while still crediting the add path and the 12% (not 4%) ceiling.

**Size-distance = 1** ("appropriately STARTER, but entry+ceiling skew one notch small for a
Core-durability compounder that ~doubled; the explicit add-on-confirmation path and 12%
ceiling keep it from being a 2"). The year-one lag + drawdown is the reason this is a 1 and
not a harsher mark — full day-one core sizing would have been *wrong on timing* even though
right on destination.

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes. The card's binding constraint is "forward durability
  of the Search profit pool under generative-AI disruption + capex-into-unproven-returns
  under disengaged founder control." The sealed key variable was "commercial-intent Search
  gateway + Cloud inflection + heavy FCF, AI-Search risk unproven at as-of." These match
  precisely — the card identified *both* the upside engine (Search gateway + Cloud inflection
  + FCF/capital-return turn) and the one genuinely unresolved risk (AI-Search monetization),
  and correctly tagged that risk as **unresolved at as-of** rather than pretending to resolve
  it. Realized history confirms the framing: Search/ad held and re-accelerated, Cloud margin
  scaled, FCF/capital-return continued — the upside engine fired and the disruption fear did
  not (yet) materialize, which is the +116% outcome.
- **Right module dominance?** Yes. The conviction stack M2/M3/M4 (each +1) drove the
  STARTER, M6 (+1) supported entry at price, and M5 (−1, no veto) sized it down rather than
  killing it. That is the intended dominance pattern for a quality_compounder
  (WEIGHTING_HARNESS §4: positive emphasis M2/M3/M4).
- **No lookahead?** The decision card draws only on pre-2024-06-14 evidence (Q1'24 8-K, FY23
  10-K/proxy, May-2024 AI Overviews launch + criticism, DOJ closing args, peer prints). It
  explicitly flags the DOJ ruling, Q2 print, and CFO handoff as *forward monitor items, not
  evidence*. (Full lookahead adjudication is the Auditor's job and is out of Scorer scope;
  on the face of the card, clean.)

**Reasoning = sound.** Correct key variable, correct module dominance, no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (sealed `dominant_modules: M2, M3, M6`; orchestrator note + METHODOLOGY for a
  quality compounder → **M2/M3**, with M6 price support).
- **Got:** the call was driven by the M2/M3/M4 conviction stack (theme/mechanism +
  profit-pool/durability + financial-reality confirmation), with M6 setting entry. The single
  most load-bearing module is **M3 (Profit Pool / Durability)** — it carried the operator
  grade (4/5), the Cloud-inflection durability read, and the governance cap that set the 12%
  ceiling. M2 (the AI-era gateway thesis) is co-dominant.

**dominant_module (got) = M3** (with M2 co-dominant); **dominant_module_expected = M2/M3.**
**Match.** The right modules drove the call.

### Failure tags (from WEIGHTING_HARNESS §7 list)

Candidate review:
- `confidence_used_as_veto` — **NOT present** (the explicit fix: M1=0 forward-uncertainty →
  haircut, not WATCH). This is the old failure the redesign avoided.
- `valuation_overweighted` — **NOT present** (M6 read price as fair/mildly-attractive and
  supported a starter; it did not gate the name to 0 on "not optically cheap").
- `hold_winner_failed` — **NOT present** (existing-position verdict HOLD with no thesis-break
  trigger is correct; the thesis was intact).
- `no_add_rule` / `no_trim_rule` — **NOT present** (both explicit and well-specified).
- `too_small_missed_asymmetry` — **PARTIAL / borderline.** The name ~doubled; the initial 4%
  + 12% ceiling on a Core-durability compounder leaves asymmetry on the table per
  METHODOLOGY §7. Tagged as a **soft/secondary** flag, not a primary failure, because (a) the
  size sat inside the correct band, (b) the realized year-one lag + −18% drawdown means the
  caution was substantially *justified*, not merely timid, and (c) the explicit add path was
  the designed route to capture the back-loaded move.

**failure_tags = too_small_missed_asymmetry (soft / secondary).** No primary failure tag.

---

## 3. Verdict

The lean 6-module pipeline **fixed the old GOOGL WATCH/0% failure.** On the same anchor that
the prior framework fumbled (downgrading a winner to "watch / avoid" on
more-research-more-doubt), the redesign produced a **STARTER with a real 4% entry, a clean
add-on-confirmation path, and a 12% durability-capped ceiling** — Axis-1 **PASS**, reasoning
**sound**, right modules (M2/M3) dominant, and **no confidence-as-veto** failure. The only
deduction is METHODOLOGY's "too small loses points": for a name the methodology itself files
under Core (15–25%), a 4% entry / 12% ceiling skews one notch toward timid given the realized
~2x — but the explicit add path, the 12% (not 4%) ceiling, and the genuinely back-loaded,
−18%-drawdown realized path (flat and lagging at +12mo) keep this a **size-distance 1**, not a
miss. Net grade: a strong, well-reasoned PASS with a minor, defensible under-sizing lean.

---

## 4. results.csv row (appended)

```
lean-6module-v1,none,googl_2024-06-14,quality_compounder,WINNER,4,STARTER,HOLD,STARTER..CORE,1,no,no,M3,M2/M3,sound,too_small_missed_asymmetry,"WINNER +115.9% t.r. vs SPY +42.1%/QQQ +54.8% to 2026-06-16; beat SPY ~74pt. +12mo only +0.7% (lagged SPY ~11pt); worst DD -17.9% @2025-04-08 $144.11. Win back-loaded (+13-24mo). Axis-1 PASS (STARTER avoided old WATCH/0%); reasoning sound; M2/M3 conviction stack drove it; M5 -1 sized down no veto; M1=0 forward-uncertainty=haircut not veto (fixed old disease). size-dist 1: 4% entry/12% ceiling timid-end for a Core-durability name that ~2x, but add-path+12%-ceiling+yr1 lag/DD justify caution. Source: StatMuse total-return."
```

---

## 5. Addendum (2026-06-19) — business-reality proof + the "braver?" verdict

### 5a. Did the two forward unknowns (and the governance cap) actually break — and which way?

Every risk that held this name **below Core** resolved in the bull's favor. Dated proof (Alphabet
releases Q2'24→Q1'26; DOJ remedies opinion 2025-09-02):

| As-of fear (drove the haircut / cap) | What actually happened, 2024-06 → 2026-06 | Direction |
|---|---|---|
| GenAI erodes the Search profit pool | Search & other revenue **accelerated**: +13.8% YoY (Q2'24) → **+19% YoY (Q1'26)**; AI Overviews ~1.5B MAU monetizing at ~conventional rates; AI Mode 75M+ DAU; Gemini App 750M MAU; **Gemini 3 retook frontier leadership** (late 2025) | **Bear thesis BROKE** |
| +91% capex = empire-spend | Capex $52.5B (FY24) → $91.4B (FY25) → **$180–190B guide (FY26)**, but **Cloud op margin 11.3% → 32.9%**, Cloud growth re-accelerated to **+63%**, backlog **>$460B** | **VALIDATED** (caveat: TTM FCF compressing $73B→$64B) |
| DOJ breaks Search distribution | **2025-09-02 remedy: NO Chrome divestiture; default-placement economics survive**; only *exclusive* contracts barred | **MILDER than feared** |
| Founder control destroys minority value | Backed the exact capex that re-rated the stock 2.1×; **raised the dividend**, **$45.7B buyback (FY25)**; no self-dealing | **BENIGN-to-positive** |

All four resolved bullish → **+109.8% price / +115.9% total return, beat SPY by ~68–74 pts.**

### 5b. Was 4% / 12% too timid — "should have been braver"?

**Yes — at the CEILING, not at the ENTRY.** These are two different errors, and only one is real:

- **Entry (4% starter): correct — do not change.** The thesis was genuinely unresolved at as-of, and the
  realized path *vindicated* caution — flat for 12 months (lagging SPY ~11 pts), then **−18% at the April-2025
  trough ($144.11)** before the re-rate. A reckless full-size Core buy at $175 would have sat underwater on an
  unproven thesis for a year. The staged "starter + add on $150–170 weakness" was the **better** path, and the
  add zone was actually hit.
- **Ceiling (12% Confirmed): one tier too low — the real miss.** `METHODOLOGY.md §2` *already lists GOOGL as a
  Core (15–25%) name*. The blind Runner docked it a full tier to Confirmed **because of the founder-governance
  discount** — the single assumption that proved **value-irrelevant**. That discount is exactly where the
  bravery was owed.

**One-line lesson:** *Be braver at the ceiling, not the trigger.* A governance/control discount on a franchise
compounder whose economics + operators are already Core-grade should **shave the Core ceiling (25% → ~15%),
not delete the Core tier (→ 12% Confirmed).**

### 5c. Weighting hypothesis (HYPOTHESIS ONLY — do not tune on one case, per §9)

> For a `quality_compounder` carrying a founder/control-governance discount **and** operator life-arc ≥ 4/5,
> a growing profit pool, and an unfailable balance sheet: apply the governance discount **within** the Core band
> (lower the ceiling toward ~15%), **not** as a **tier demotion** to Confirmed. Test against META (control 3/5)
> and DIS (operator 2.5/5) before any weight change — confirm the discount is **operator-grade-conditioned**,
> not flat. Separately, keep watching the **FCF-compression** strand (TTM $73B→$64B) before declaring the capex
> thesis fully closed.
