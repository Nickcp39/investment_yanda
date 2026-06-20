# Outcome Scorecard — MU (Micron Technology, Inc.), as-of 2025-03-21

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-2025-03-21 market data (allowed for
> the Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §7 "too small loses points"), and
> `WEIGHTING_HARNESS.md` §7. The `_v0/` subfolder (archived old run) was ignored.
>
> Sealed/derived expectation: **WINNER** (PROVISIONAL — short window), context
> `cyclical_inflection` (memory up-leg + secular HBM/AI-memory overlay), key variable
> *HBM / AI-memory durability + cycle position*, **expected band STARTER..CORE**.
>
> **Window caveat (read first):** realized window is only **~15 months** (2025-03-21 →
> 2026-06-16), shorter than the 24–36mo most cases run. For a *cyclical*, 15mo does not
> complete a full memory cycle, so the WINNER label is marked **PROVISIONAL** — it captures
> direction and magnitude with very high confidence (a ~10.8× run that beat even the semi
> index by ~4×), but it does NOT yet prove the through-cycle-margin-floor thesis is *durable*
> across a down-leg. The provisional flag is about cycle-completeness/durability, not about
> the direction of the call, which is unambiguous.

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | `cyclical_inflection` (memory up-leg + secular HBM/AI-memory overlay) |
| Business verdict | good |
| New-money verdict | **STARTER** |
| Existing-position verdict | HOLD |
| Suggested initial size | **4%** (Starter tier) |
| Suggested max size | **12%** (Confirmed-tier ceiling) |
| Buy-below / starter zone | ≤ ~$95 (as-of $94.72, post ~8% FQ2-print drop) |
| Add zone | $70–$85 on weakness (~1.6–1.8× book), OR any price on a clean forward confirmation (HBM + DC-DRAM revenue still growing AND blended GM holds/re-expands AND inventory not ballooning) → toward the ~10–15% Confirmed tier |
| Binding constraint | M4/M5 cycle-position + M3 HBM-durability: buying a majority-commodity cyclical on a confirmed MID-CYCLE up-leg at a FULL normalized multiple (~27× on ~$3.5 normalized EPS; ~15× run-rate is on flattered up-leg earnings) on the unproven thesis that HBM/AI-memory permanently raises the through-cycle margin floor → a SIZE + cycle-timing cap, not a veto |
| Module signals | M1 +1 / M2 +1 / M3 +1 / M4 +1 / M5 −1 / M6 +1 |
| Hard veto | None fired |

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **MU $94.72 on 2025-03-21** (the first full session after the FQ2 FY25 print
of 2025-03-20 after close; matches the locked card's two-source as-of). MU pays only a token
dividend, so **price return ≈ total return** (the Yahoo adjusted-close series differs from raw
close by <0.5% over the window; figures below are the adjusted/total-return leg).

| Window | Date used | MU close | MU t.r. | SPY t.r. | SOXX t.r. | MU − SPY | MU − SOXX |
|---|---|---:|---:|---:|---:|---:|---:|
| As-of | 2025-03-21 | $94.72 | — | — | — | — | — |
| +6mo | 2025-09-22 | $164.62 | **+74.2%** | **+18.9%** | **+35.9%** | **+55 pt** | **+38 pt** |
| +12mo | 2026-03-23 | $404.35 | **+328.3%** | **+17.5%** | **+69.9%** | **+311 pt** | **+258 pt** |
| ~today | 2026-06-16 | $1,020.76 | **+981.6%** | **+34.6%** | **+198.6%** | **+947 pt** | **+783 pt** |

(+12mo uses 2026-03-23, the first session ≥ the 2026-03-21 anniversary, which fell on a
Saturday.)

**Source prices (two-source, the same dual-source convention as the prior scored cases):**
- **Yahoo Finance** chart API (the project's canonical price source per `memory/price_data_source.md`):
  MU 164.62 (2025-09-22), 404.35 (2026-03-23), 1,020.76 (2026-06-16); live MU $1,133.99 on
  2026-06-18 with a 52-wk range $103.38–$1,149.43 and **no splits** in the series.
- **stockanalysis.com** cross-check: MU $1,043.19 (2026-06-17), $1,133.99 (2026-06-18) — matches
  Yahoo to the cent. The ~10.8× move is therefore double-confirmed and far too large for any
  provider/split artifact to flip the label.
- **Benchmarks (to-2026, direct reads, internally consistent with the other scorecards in this
  round):** SPY t.r. **+34.6%** (adj close $748.40, 2026-06-16) — same figure the AMZN/NVDA cards
  use; SOXX t.r. **+198.6%** (close $591.24, 2026-06-16) — same figure the AMZN card uses. Anchoring
  the benchmarks to the identical 2025-03-21 / 2026-06-16 dates as MU.

**Worst drawdown along the path (load-bearing for grading size):** lowest close **$64.72 on
2025-04-04 = −31.7%** from the as-of $94.72 — the early-April-2025 "Liberation Day" tariff
selloff (the *same* macro shock window that took GOOGL −18%, INTC −15.6%, and NVDA's interim peak
−37% *below/around* their entries). It was **sharp but brief and macro-driven, not thesis-driven**:
April 4 $64.72 (trough), April 9 $77.87, and MU closed **back above the $94.72 entry by 2025-05-13**
($96.93) — i.e. the whole drawdown was a ~7-week macro dip, after which MU never closed below entry
again (post-May-1 low $77.77 on 2025-05-01). So a holder who bought the STARTER at $94.72 sat on a
worst mark of about −32% for a few weeks, was back to even inside ~2 months, and was +74% by +6mo.
Source: Yahoo per-date min-close over 2025-03-21 → 2026-06-18.

### Mechanical label
**WINNER (PROVISIONAL — short ~15mo window).** Decisive and clean on every comparator:
**+981.6% total return vs SPY +34.6% (beat ~947 pt) and — the discriminating test — vs the SOXX
semiconductor index +198.6% (beat ~783 pt).** Even at +12mo it had already beaten SPY by ~311 pt
and the semi index by ~258 pt (+328% vs +69.9%), so this is emphatically **NOT a semi-cycle beta
ride** — MU outran its own sector index by ~4× to-2026. The card's open thesis question — does HBM /
AI-memory permanently re-weight the mix and lift the through-cycle margin floor — resolved
**overwhelmingly in the bull's favor** within the window: the cyclical re-rated *and* the secular
HBM overlay re-rated on top of it. **PROVISIONAL** only because 15mo does not complete a memory
down-leg, so the *durability* leg of the thesis (does the higher margin floor survive the next
trough) is not yet proven — but the direction and magnitude of the call are unambiguous.

### Did the binding constraint resolve, and which way?
The card's binding constraint was the cycle-position + HBM-durability risk: *"you are buying a
majority-commodity cyclical on a confirmed MID-CYCLE up-leg at a full normalized multiple on the
unproven thesis that HBM/AI-memory permanently raises the through-cycle margin floor."* Realized:
the up-leg did **not** roll over — the GM step-down the card flagged as the key early-warning signal
was a mix blip, not a cycle top; HBM + data-center DRAM kept compounding through the AI build-out;
and the stock re-rated ~10.8×. Of the five named kill-criteria (cyclical rollover / HBM
differentiation fails / capex destroys FCF / inventory glut / normalized-margin thesis breaks),
**none triggered** through the window — the GM step-down reversed and the mix shifted further toward
the higher-margin HBM pool, exactly the bull path. The one genuinely unresolved risk the card sized
*down* for (the cycle rolling at a full normalized multiple) is the risk that **did not
materialize**, which is precisely why the realized outcome is a top-of-table winner.

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, Winner row:
- PASS = `STARTER` or `CORE` (or explicit structured starter)
- PARTIAL = `WATCH` but names the correct key variable + clear buy/add trigger
- FAIL = `REJECT`, or `WATCH / 0%` with avoid framing

Locked new-money verdict = **STARTER** (real 4% money at as-of, HOLD for existing holders, an
explicit confirmation-gated add path to the ~12% Confirmed tier). It avoided REJECT and avoided
WATCH/0%, and reached a real-ownership tier.

**Axis-1 = PASS.**

This is the redesign working as intended. The textbook old-framework failure here would have been
**WATCH/0% with avoid framing** — "not trough-cheap (~2.17× book, memory bottoms near ~1× book),
~27× on normalized ~$3.5 EPS, the optically cheap ~15× run-rate is on flattered up-leg earnings,
wait for the ~$70–85 / ~1.6–1.8× book entry" — which is exactly the `WEIGHTING_HARNESS §0` disease
("reward cheapness too much … walk toward / away on the multiple … punish asymmetric setups").
The card's own `runner_dissent` even surfaces this temptation explicitly ("a disciplined cyclical
investor could legitimately run this as a 1–2% tracking sliver here and wait for a cheaper price")
and then **correctly rejects it**, holding a real 4% starter on the dislocation + HBM optionality +
survivable downside. The `cyclical_inflection` gate held price to a normalized-economics *size
modulator*, not a hard veto, and the M1 +1 evidence-confidence read converted the forward HBM-
durability uncertainty into a **haircut + wider/lower add band, not a confidence veto**. On
direction, the pipeline got the call right.

### Size-distance (0–3)

Correct size band (derived expectation + PROTOCOL §7 logic for a `cyclical_inflection` with a
secular overlay): **STARTER..CORE.** Realized outcome = a ~10.8× WINNER that beat the semi index
by ~4×, with the worst drawdown a brief −31.7% macro dip fully recovered in ~7 weeks.

Locked sizing: initial **4%** (top of the 3–5% Starter band), max **12%** (Confirmed-tier ceiling),
with an explicit confirmation-gated add path (HBM + DC-DRAM revenue still growing AND blended GM
holding/re-expanding AND inventory not ballooning → add toward ~10–15% Confirmed) and a stated
rationale that a *cyclical* caps at Confirmed, not Core, until HBM durability proves out.

Scoring against the literal PROTOCOL §6 scale and `METHODOLOGY §7` ("a winner identified only as a
tiny STARTER is **not** full marks — 'right direction, too small' must lose points") + the
durability ladder (§2: the 15–25% Core tier is for businesses you'd hold 5–10 years; the **ceiling
is set by durability, not just confirmation**):

- **Band:** the initial **4% sits inside the correct STARTER..CORE band** → by the literal scale the
  entry is **0** (within band). The **12% ceiling**, however, sits at the **Confirmed** tier and
  never reaches the **Core (15–25%)** tier that the realized ~10.8× outcome — with the secular HBM
  overlay re-rating on top of the cyclical — would in hindsight have warranted.
- **"Too small loses points" applies, and the path gives the caution NO vindication** (the NVDA
  pattern, not the GOOGL pattern). MU was **already +74% by +6mo and +328% by +12mo**, and its only
  meaningful drawdown was a ~7-week macro dip that reversed by mid-May-2025. The add trigger the card
  specified (HBM + DC-DRAM growth with blended GM holding) was being confirmed within ~1–2 quarters,
  so the structured add path — *if executed* — would have routed the position toward the 12% ceiling
  early and well below the eventual level. That makes the **12% Confirmed ceiling itself the binding
  limitation**, not the 4% entry. Unlike GOOGL (which lagged for ~12mo and drew −18% below entry,
  partially *justifying* the caution), MU gave the timidity nothing to hide behind.
- **Mitigants that hold this at a 1, not a 2:** (a) the entry **is** inside the correct band — real
  ownership, not a dressed-up WATCH; (b) the card carries an **explicit, well-specified
  confirmation-gated add path** to ~12% — the methodology *wants* "start real, add on confirmation,"
  and the realized HBM/DC-DRAM prints are exactly that confirmation; (c) **12% (not 4%) is the
  operative ceiling**, and at as-of, capping a *majority-commodity cyclical entered mid-up-leg at a
  full normalized multiple* at the Confirmed tier was the **methodology-correct** call — the Core
  tier is for proven 5–10yr durables, and HBM through-cycle durability was the explicit *open
  question*, not an as-of fact. The card was disciplined, not timid, on the evidence it had; the ~11×
  is what *resolved* the open question, which it correctly could not assume.

This is the **NVDA-twin** sizing outcome (entry inside band, ceiling one tier low for what became a
Core-magnitude winner, no path-vindication for the caution → size-distance 1), and it is graded a
**firmer 1, not a 0**: it is one notch *worse* than AMZN's size-distance-0 (whose sealed band was
STARTER-singular, so 12% was the literal target ceiling) because MU's expected band explicitly
includes **CORE**, so the 12% cap *does* leave Core-tier asymmetry on the table; and it is one notch
*better* than a 2 because the entry sat in-band with a real, confirmation-triggered add path to 12%.

**Size-distance = 1** (entry correctly inside the STARTER band; the 12% Confirmed ceiling is one
tier below the Core 15–25% the ~10.8× realized winner warranted; the explicit add path + the 12%
(not 4%) operative ceiling keep it from a 2 — but, like NVDA and unlike GOOGL, the near-immediate
+74%/+328% with only a brief macro drawdown means the timidity earned **no** path-vindication, so it
is a firm 1).

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes — precisely. The card's binding constraint is the cycle-
  position + HBM-durability axis (*"buying a majority-commodity cyclical on a confirmed mid-cycle
  up-leg at a full normalized multiple on the unproven thesis that HBM/AI-memory permanently raises
  the through-cycle margin floor … the QoQ revenue dip + guided GM step-down + consumer softness are
  the early signals to watch"*). That is the **exact** axis that decided the outcome — the GM
  step-down reverted (mix blip, not cycle top), HBM/DC-DRAM compounded, and the through-cycle thesis
  re-rated the stock. The card isolated the right upside engine (HBM/AI-memory as a scarce, contracted
  higher-margin pool re-weighting the mix) **and** the right single risk (commodity ASP tailwind
  maturing into a glut) and correctly tagged the risk as *unresolved at as-of* rather than resolving
  it with hindsight.
- **Right module dominance?** Yes, for a `cyclical_inflection`. The conviction stack **M2 +1 / M3 +1
  / M4 +1** drove the STARTER — M2 (AI creating a new scarce HBM bottleneck on a confirmed up-leg,
  Micron 1-of-3), M3 (the **bifurcated-pool** read: Half-A HBM = the only structural-ceiling lifter
  but unproven across a cycle, Half-B commodity = cyclical-not-eroding; operator team 4/5 lifting
  conviction *within* the cyclical band but explicitly NOT above it), M4 (accounting confirms the
  up-leg, but **size off NORMALIZED, not flattered run-rate, economics**) — with **M5 −1** running the
  trap test and **correctly declining to fire** (impairment cyclical/recoverable, not structural;
  balance sheet survives a cycle; no bankruptcy path), and **M6 +1** supporting a starter on the ~8%
  dislocation. That is exactly the intended dominance pattern for `cyclical_inflection`
  (`WEIGHTING_HARNESS §4`: positive emphasis **M2/M4/M5**; price = normalized-economics modulator).
  The M4-led "size off normalized" discipline + the M5 "this is a size cap, not a kill" call are the
  two most load-bearing reads, and both were correct.
- **No lookahead?** On the face of the card, clean — it draws only on pre-2025-03-21 evidence (the
  FQ2 FY25 release of 2025-03-20 + the 10-Q, the FQ1 release, the FY24 10-K, the as-of price series)
  and explicitly flags the FQ3 print (guided to record $8.80B revenue), forward HBM/margin trajectory,
  and any dated third-party DRAM/HBM pricing as *forward monitor items, not evidence*. (Full lookahead
  adjudication is the Auditor's job and out of Scorer scope; on the face of the card, clean.)

**Reasoning = sound.** Correct key variable (the HBM-durability / cycle-position axis that actually
decided it), correct module dominance for a cyclical_inflection (M2/M4 conviction + M5 risk, with the
M4 "size off normalized" + M5 "cap-not-kill" reads doing the decisive work), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (`WEIGHTING_HARNESS §4` for a `cyclical_inflection` → positive emphasis **M2/M4/M5**;
  the binding constraint the card itself names is **M4/M5 cycle-position + M3 HBM-durability**).
- **Got:** the call was carried by the **M2/M3/M4 conviction stack** with **M5 −1** as the decisive
  *non-veto* risk read. The single most load-bearing modules are **M4** (normalize the up-leg, size
  off ~$3.5 normalized EPS not the flattered ~$6.2 run-rate — the discipline that made a *measured*
  STARTER rather than a chase) and **M3/M5** (M3's bifurcated-pool "HBM is the only ceiling-lifter,
  and it's unproven" framing; M5 correctly classifying the risk as a recoverable cyclical drawdown,
  not a structural trap). M2 frames the theme; M6 sets the entry.

**dominant_module (got) = M2/M3/M4** (conviction stack; **M4/M5** most load-bearing);
**dominant_module_expected = M2/M4** (with M5). This is a **near-match / acceptable** — the realized
dominance leans exactly to the M4 (normalized-economics) + M5 (cap-not-kill) reads that
`cyclical_inflection` weights, and M3's HBM-durability call is the third pillar the card's own binding
constraint names. Not scored as a mismatch.

### Veto (fired vs expected)

- **veto_expected = no** (`cyclical_inflection` gate: veto only if the balance sheet cannot survive
  the cycle — and it plainly could: cash+inv $9.60B, equity $48.6B, FY23 −$5.8B loss absorbed without
  distress, no bankruptcy path).
- **veto_fired = no.** No hard veto fired; M5 −1 correctly acted as a *size cap, not a kill*.
  **Match** — and it is the correct behavior: a hard veto here (treating the "full normalized multiple
  on up-leg earnings" as a false_cheap trap) would have produced the WATCH/0% failure and missed a
  ~10.8× winner. The card explicitly distinguished a *recoverable cyclical* impairment from a
  *permanent structural* one (contrast INTC-DCG / PYPL / DIS, where structural decline justified the
  size-to-0), which is precisely the discrimination the redesign needed.

### Failure tags (from `WEIGHTING_HARNESS §7` list)

Candidate review:
- `valuation_overweighted` — **NOT present** (the key save: the ~27× normalized / 2.17× book "not
  trough-cheap" read was a *size modulator*, not a veto; the `cyclical_inflection` price-as-modulator
  gate held, and the card resisted its own dissent's "wait for ~$70–85" temptation).
- `confidence_used_as_veto` — **NOT present** (M1 +1; the forward HBM-durability / next-quarter-margin
  unknowns + the disclosed no-dated-DRAM/HBM-index gap + the modeled normalized-EPS input were
  expressed as a haircut + wider/lower add band, not a WATCH).
- `false_cheap_value_trap` / `trailing_accounting_trap` — **NOT present (avoided in the bull
  direction).** The card *did* flag the up-cycle-EPS "false cheap" risk (the ~15× run-rate is on
  flattered earnings) but correctly graded it a PARTIAL/survivable size cap, not a full trap, because
  structural-decline and balance-sheet-death were both absent — exactly right.
- `hold_winner_failed` — **NOT present** (existing-position **HOLD** on an intact, inflecting thesis
  was correct; the thesis over-delivered and a holder who held was emphatically right).
- `no_add_rule` / `no_trim_rule` — **NOT present** (both explicit and well-specified; the add path is
  gated on the exact HBM/DC-DRAM/GM confirmations that subsequently landed).
- `too_small_missed_asymmetry` — **PRESENT (primary, soft-to-firm).** The name ~10.8×'d (beating even
  the semi index by ~4×) with only a brief macro drawdown, and the 4% entry / **12%-Confirmed ceiling**
  left meaningful Core-tier asymmetry uncaptured; unlike GOOGL, the front-loaded path gave the caution
  no vindication. Tagged as the **primary** flag (the NVDA-twin pattern). It remains a **size-distance
  1, not 2**, only because the entry sat inside the correct band and the explicit confirmation-gated
  add path + the 12% (not 4%) operative ceiling were present, *and* because capping a majority-
  commodity cyclical at Confirmed was the methodology-correct call on as-of evidence.

**failure_tags = too_small_missed_asymmetry** (primary). No veto-missed, no hold-winner-failed, no
confidence-as-veto, no valuation-overweighted; add/trim rules both present.

---

## 3. Verdict

The lean 6-module pipeline **got MU right on direction and reasoning.** On a setup the old framework
would very likely have killed as WATCH/0% ("not trough-cheap, ~27× on normalized EPS, ~2.17× book,
wait for the ~$70–85 entry"), it returned a **STARTER with a real 4% entry, HOLD for holders, and an
explicit confirmation-gated add path** — Axis-1 **PASS**, reasoning **sound**, dominant modules the
M2/M3/M4 conviction stack with the decisive work done by M4's "size off normalized economics" and
M5's "recoverable cyclical, not structural trap → cap not kill" reads (as expected for a
`cyclical_inflection`), **no valuation-as-veto and no confidence-as-veto**. The card even surfaced the
old-framework temptation in its own dissent and correctly overrode it. That is exactly the
`WEIGHTING_HARNESS §0` disease (reward-cheapness / uncertainty-as-veto / walk-away-on-the-multiple),
and the redesign cured it. It also correctly *discriminated* a recoverable cyclical (size cap) from a
structural-decline trap (size-to-0) — the mirror-correct call vs INTC-DCG/PYPL/DIS.

The one deduction is `METHODOLOGY §7`'s "too small loses points," the **NVDA pattern**: MU realized as
a ~10.8× winner that beat its own sector index ~4× and gave the caution **no path-vindication**
(already +74% by +6mo, +328% by +12mo, only a brief −31.7% macro dip that reversed in ~7 weeks), yet
the **12% Confirmed ceiling sits one tier below the Core 15–25%** that outcome warranted. The entry was
correctly in-band and the add path was explicit and confirmation-gated, and — importantly — capping a
*majority-commodity cyclical entered mid-up-leg at a full normalized multiple* at Confirmed was the
**methodology-correct** call on as-of evidence (the HBM through-cycle durability that would justify Core
was the explicit *open question*, which the ~11× is what *resolved*). So this is **size-distance 1**
(firm, NVDA-twin: entry in band, ceiling one tier timid, no path-vindication) — not a 0 (MU's expected
band includes Core, so the cap *does* leave asymmetry on the table, unlike AMZN's Starter-singular
band) and not a 2 (in-band entry + real add path). Net grade: a **strong, well-reasoned PASS** whose
only flaw is a one-tier-timid ceiling on a Core-magnitude winner — "be braver at the ceiling, not the
trigger." **Label PROVISIONAL** on the short ~15mo window: direction/magnitude are unambiguous, but the
through-cycle-durability leg of the thesis is not yet proven across a memory down-leg.

---

## 4. results.csv row (DO NOT auto-append — returned to orchestrator)

```
lean-6module-v1,none,mu_2025-03-21,cyclical_inflection,WINNER,4,STARTER,HOLD,STARTER..CORE,1,no,no,M2/M3/M4,M2/M4,sound,too_small_missed_asymmetry,"WINNER (PROVISIONAL, ~15mo window) +981.6% t.r. to 2026-06-16 from $94.72 vs SPY +34.6%/SOXX +198.6%; beat SPY ~947pt and the SEMI index SOXX ~783pt (NOT a beta ride). +6mo +74.2% ($164.62); +12mo +328.3% ($404.35; 2026-03-23) vs SPY +17.5%/SOXX +69.9% (beat both ~311/~258pt). Worst DD -31.7% @2025-04-04 $64.72 (Apr-2025 'Liberation Day' tariff selloff, same macro window as GOOGL/INTC/NVDA), brief+macro not thesis, back >entry by 2025-05-13; post-May low $77.77. Binding constraint (cycle rolling at full normalized multiple while HBM-durability unproven) resolved bull: GM step-down was a mix blip not a cycle top, HBM/DC-DRAM compounded, ~10.8x re-rate; all 5 kill-criteria failed to trigger. Axis-1 PASS (STARTER avoided old WATCH/0% 'not trough-cheap/~27x normalized' veto - card overrode its OWN dissent's wait-for-$70-85 temptation); reasoning sound; dominant M2/M3/M4 conviction stack w/ decisive work by M4 'size off normalized not run-rate' + M5 'recoverable cyclical=cap-not-kill' (got vs M2/M4 expected = near-match for cyclical_inflection); M5 -1 sized down no veto (correct: BS survives cycle, no bankruptcy, impairment cyclical not structural) - mirror-correct discrimination vs INTC-DCG/PYPL/DIS structural traps; M1 +1 forward HBM-durability uncertainty=haircut not veto; price=normalized-economics modulator not veto = WEIGHTING_HARNESS fix working. size-dist 1 (NVDA-twin): 4% entry inside band but 12% Confirmed ceiling one tier low vs Core 15-25% the ~10.8x winner warranted; like NVDA & unlike GOOGL the +74%@6mo/+328%@12mo path gave caution NO vindication -> firm 1; add-path + 12%(not 4%) ceiling + methodology-correct cyclical-Confirmed cap keep it from 2; one notch worse than AMZN sd0 (MU band includes Core). failure_tag too_small_missed_asymmetry (primary). Clean, no visible lookahead. PROVISIONAL: 15mo doesn't complete a memory down-leg so through-cycle-margin-floor DURABILITY unproven, but direction/magnitude unambiguous. Source: Yahoo Finance (anchored 2025-03-21/2026-06-16, no splits) + stockanalysis.com to-date cross-check ($1,133.99 2026-06-18)."
```

---

*Scored 2026-06-20 against the locked blind decision card. The decision card was NOT modified.
`_v0/` ignored. Post-2025-03-21 data used (allowed for the Scorer). Benchmark returns anchored to
the same 2025-03-21 / 2026-06-16 dates as MU; SPY/SOXX to-2026 figures cross-consistent with the
AMZN/NVDA scorecards in this round. Price source Yahoo Finance per `memory/price_data_source.md`,
double-confirmed on stockanalysis.com. Version `lean-6module-v1` / `none` matches the card (VERSIONS.md
current ACTIVE).*
