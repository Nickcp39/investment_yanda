# Outcome Scorecard — NBIS (Nebius Group), as-of 2026-01-01

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-2026-01-01 market data (allowed for
> the Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §7 "too small loses points"), and
> `WEIGHTING_HARNESS.md` §7. The `_v0/` pilot archive was NOT used.
>
> **WINDOW CAVEAT (load-bearing): the realized window is only ~5.5 months (2025-12-31 →
> 2026-06-16). This is far too short for a durable verdict. The mechanical label below is
> classified but marked STRONGLY PROVISIONAL — a 5.5-month read on a reflexive, thin-float,
> story-driven AI-infra name can reverse hard. It is recorded as a directional data point,
> not a settled outcome.**

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | `exceptional_bottleneck` |
| Business verdict | good |
| New-money verdict | **STARTER** |
| Existing-position verdict | HOLD |
| Suggested initial size | **~3%** (low end of Starter, deliberate) |
| Suggested max size | **~10%** (Confirmed-tier ceiling — explicitly NOT Core 15–25%) |
| Buy-below / starter zone | ≤ ~$92.50 (Sept-2025 equity print); as-of $83.71 qualifies |
| Add zone | Scale toward ~10% ONLY on confirmation: connected-MW on the 220MW CYE2025 / 800MW–1GW CYE2026 guide AND realized ARR on the $7–9B path AND non-dilutive financing |
| Binding constraint | Reflexive financing dependence (fund the ≥2.5GW build cheaply without crushing per-share value) AND convert contracted power into connected, revenue-producing capacity; co-binding: Microsoft/Meta concentration + undisclosed contract spread |
| Module signals | M1 0 / M2 +2 / M3 +1 / M4 0 / M5 −1 / M6 +1 |
| Hard veto | None fired (exceptional_bottleneck gate: valuation/financing = size cap + kill-gates, not hard veto; net-cash at 9/30/25, no near maturities) |

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **NBIS close $83.71 on 2025-12-31** (decision_card §as_of_price; = `data/asof_2025_12_31_nbis_quotes.csv`
last row, Yahoo chart API v8). NBIS pays **no dividend**, so price return = total return. SPY/SOXX returns are
**total return** (adjusted close, dividends reinvested).

| Window | Date used | NBIS close | NBIS t.r. | SPY t.r. | SOXX t.r. | NBIS − SPY | NBIS − SOXX |
|---|---|---:|---:|---:|---:|---:|---:|
| As-of | 2025-12-31 | $83.71 | — | — | — | — | — |
| +1mo | 2026-02-02 | $88.20 | **+5.3%** | +2.0% | +17.1% | +3 pt | −12 pt |
| +2mo | 2026-03-02 | $91.00 | **+8.7%** | +0.7% | +16.9% | +8 pt | −8 pt |
| +3mo | 2026-03-31 | $103.80 | **+24.0%** | −4.4% | +9.2% | +28 pt | +15 pt |
| +4mo | 2026-04-30 | $138.20 | **+65.1%** | +5.7% | +53.3% | +59 pt | +12 pt |
| +5mo | 2026-06-01 | $264.50 | **+216.0%** | +11.5% | +90.0% | +204 pt | +126 pt |
| **~to-2026** | **2026-06-16** | **$265.10** | **+216.7%** | **+10.3%** | **+96.5%** | **+206 pt** | **+120 pt** |

(For reference only, last available 2026-06-18 close $286.69 = +242.5%; the +216.7% to-2026-06-16 figure is the
scoring anchor.)

Source prices (Yahoo Finance chart API v8, `query1.finance.yahoo.com`, the project's canonical price source per
`memory/price_data_source.md`; SPY/SOXX use adjusted close for total return):
- NBIS: $88.20 (2026-02-02), $103.80 (2026-03-02), $103.80 (2026-03-31), $138.20 (2026-04-30), $265.10 (2026-06-16).
- SPY t.r. **+10.3%** to 2026-06-16 (close $750.33; adj $748.40) — cross-checks to the same $748.40 used in the
  `nvda_2023-05-25` and `intc_2024-08-02` scored cases (provider-consistent).
- SOXX t.r. **+96.5%** to 2026-06-16 (close $591.24) — likewise the identical $591.24 anchor as the NVDA case.

### Worst drawdown — the load-bearing path fact

The **lowest close** over the entire 2025-12-31 → 2026-06-16 window was **$73.87 on 2026-02-05 = −11.7% vs the
as-of entry of $83.71.** NBIS closed below its entry on only **2 days** (2026-02-04 $82.39, 2026-02-05 $73.87) and
never again. A holder who bought the ~3% STARTER at $83.71 was underwater only briefly and at most ~12%.

The largest **interim peak-to-trough** decline was **−32.1%**, from the 2026-01-16 peak ($108.73) to that same
2026-02-05 trough ($73.87) — but because the run-up that created the peak happened *after* entry, the −32% trough
was still only **−11.7% below the as-of anchor**. Source: Yahoo chart API min-close / running-peak computation over
the stated window.

### Shape of the win — BACK-LOADED

Unlike NVDA-2023 (immediate, monotonic) or META-2022 (front-loaded), this win was **back-loaded**: NBIS was only
**+5% to +9% through the first two months**, dipped to **−11.7% in early February**, then inflected — +24% by
end-March, +65% by end-April, first close above +100% on 2026-05-04 ($176.42), and the explosive leg in May (+216%
by 2026-06-01). The first ~4 months barely beat SPY and *trailed* SOXX; the entire excess return arrived in a single
~6-week window (late-April → early-June 2026). This matters for grading: the structured confirmation-gated add path,
if executed, would have been adding *into* the late-April/May proof — well-positioned — but the **10% ceiling caps a
name that nearly 3.2×'d**.

### Did the binding constraint resolve, and which way? (Scorer-allowed post-as-of facts)

The card's binding constraint was **reflexive financing dependence + capacity-to-ARR conversion**, with the dominant
M5 kill path being *"a financing wobble makes the ATM/raises dilutive or unavailable, slowing the build."* Realized,
**both legs resolved decisively in the bull's favor:**

1. **Q4'25 / FY2025 print (2026-02-12):** group revenue **$227.7M (+547% YoY, +56% QoQ)**; **YE2025 ARR $1.25B —
   ABOVE the $900M–1.1B guide** the card flagged; group adj-EBITDA **turned positive**; 2026 guide revenue
   **$3.0–3.4B** with the **$7–9B ARR target reaffirmed**, and >1GW power being secured for CYE2026. The forcing
   metric (connected MW + realized ARR vs the $7–9B path) tracked **ahead of guide** — the opposite of the card's
   kill-criteria #1 (MW lag) and #5 (ARR undershoot). Note: the Q3-letter "$4.3B-vs-$7–9B ARR cover discrepancy"
   the dissent carried as model risk resolved benignly (ARR beat its near-term guide).
2. **The financing kill-gate — the card's #1 binding constraint — resolved FAVORABLY.** The May re-rating was
   explicitly attributed (Foreign Policy Journal / Barchart, 2026-05) to NBIS **funding 2026 capex without requiring
   further equity dilution** — i.e. the exact reflexive-dilution risk M5 sized *down* for **did not materialize.**
3. **Concentration / contract-scale unknown resolved UP:** a **~$27B Meta deal** (next-gen NVIDIA Vera Rubin) plus
   an **Eigen AI acquisition (~$643M)** and analyst upgrades drove +13% on 2026-05-04 and a sustained breakout to
   all-time highs — anchor demand expanded rather than paused/in-sourced (kill-criterion #4 did not fire).

**Every one of the card's six kill-criteria failed to trigger within the window**, and the two co-binding unknowns
(financing-without-dilution, anchor-contract scale) both broke bullish. The mechanism the Runner named — a real
power/capacity bottleneck rented to creditworthy payers, gated on non-dilutive financing — is the mechanism that
played out. (Mechanism is sound; the magnitude is still only a ~5.5-month read — see window caveat.)

### Mechanical label

**WINNER — STRONGLY PROVISIONAL (~5.5mo window).** NBIS **+216.7%** (price = total return) vs SPY **+10.3%** (beat
by **~206 pts**) and — the discriminating test that rules out a pure AI/semis-beta ride — vs the **SOXX semiconductor
index +96.5%** (beat by **~120 pts**). The thesis over-delivered on its own forcing metric (ARR beat guide) and its
dominant kill path (dilutive financing) reversed favorably. This is consistent with what the orchestrator would seal
for an `exceptional_bottleneck` (the AI-power/capacity bottleneck). **The PROVISIONAL flag is not a formality:** the
window is ~5.5 months, the win is concentrated in a single ~6-week story-driven leg (Meta $27B + "no dilution"
narrative), and the name is exactly the reflexive, thin-float, sentiment-sensitive structure the card itself warned
can *permanently impair per share via dilution if markets tighten* — a future tightening could still validate that
risk. Recorded as a strong directional data point, not a settled durable outcome.

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, Winner row: PASS = `STARTER` or `CORE` (or explicit structured starter); PARTIAL = `WATCH` + correct
key variable + clear buy/add trigger; FAIL = `REJECT`, or `WATCH / 0%` with avoid framing.

Locked new-money verdict = **STARTER** (real ~3% money at as-of $83.71, explicit confirmation-gated add path to
~10%, buy-below ~$92.50). It avoided REJECT, avoided WATCH/0%, and reached a real-ownership tier on a confirmed
bottleneck. **Axis-1 = PASS.**

This is the redesign working as designed. The textbook old-framework failure here was the obvious one: NBIS at as-of
was *optically grotesque* on trailing revenue (~$21B cap on ~$146M quarterly revenue), a thin-float, 15.5%-short,
no-index-bid neocloud burning ~$2.0B of 9M PP&E and openly dependent on an ATM — the `WEIGHTING_HARNESS §0` disease
("miss bottleneck winners when classic valuation looked uncomfortable" / "treat uncertainty as a veto") would have
returned WATCH/0% with avoid framing. The `exceptional_bottleneck` gate correctly held both the optical multiple and
the financing uncertainty to a **size cap + explicit kill-gates, not a hard veto**, and the card explicitly named the
context's signature trap — *under-sizing the starter on optics* — as the thing to avoid. On direction, the pipeline
got the call right.

### Size-distance (0–3)

Correct size band (PROTOCOL §6 + sealed expectation for an `exceptional_bottleneck` WINNER): **STARTER..CORE.**
Realized outcome = a ~3.2× in ~5.5 months with a max −11.7% draw vs entry.

Locked sizing: initial **~3%** (low end of the 3–5% Starter band), max **~10%** (Confirmed ceiling), with an
explicit confirmation-gated add path (connected-MW on guide AND ARR on the $7–9B path AND non-dilutive financing →
toward ~10%) and a stated ceiling held *below Core* "until financing-without-dilution and connected-MW/ARR are
proven."

- **Band:** the ~3% initial sits **inside the correct STARTER..CORE band** → by the literal PROTOCOL §6 size-distance
  scale, the entry is **0** (within band). The ~10% **ceiling**, however, sits at the **Confirmed** tier and
  **never reaches the Core (15–25%) tier**.
- **`METHODOLOGY §7` "too small loses points" applies.** The name ~3.2×'d. A ~3% entry / ~10% ceiling on a winner
  this size leaves very large asymmetry uncaptured if the plan is followed mechanically and never revised beyond the
  ~10% Confirmed cap.
- **Two genuine mitigants keep this a 1, not a 2, and arguably soften the 1:**
  (a) **The path partly vindicated the caution — more than NVDA, less than GOOGL.** Unlike NVDA (which never drew
  down and inflected within one quarter), NBIS spent ~4 months going roughly sideways-to-down (−11.7% in early Feb,
  only +5–9% through February), so a deliberate **low-end-of-Starter ~3% entry with proof-gated adds was the
  *correct* posture for a reflexive name whose deciding facts (margins, dilution path, conversion) were all
  undisclosed at as-of.** The realized confirmation (Q4'25 ARR beat 2026-02-12; non-dilutive-financing narrative +
  Meta $27B late-Apr/May) arrived *exactly* as the add-path required, and the stock did its work *after* that proof —
  so the structured-add design was well-matched to the realized sequence.
  (b) The card carries an **explicit, well-specified confirmation-gated add path**, and ~10% (not ~3%) is the
  operative ceiling — a legitimate Confirmed-tier weight for a name with a live, unresolved *reflexive-financing*
  question at as-of.
- **Why it is still not a 0:** the durability ladder (`METHODOLOGY §2`) sets the ceiling by durability, and the
  realized financing resolution (capex funded *without* dilution) + ARR beat is precisely the proof that, in
  hindsight, would have unlocked a higher tier — yet the card's ~10% cap structurally forecloses Core even on full
  confirmation. For a ~3.2× winner whose dominant risk reversed favorably, the **~10% Confirmed ceiling is one tier
  too low** vs the Core band a fully-confirmed bottleneck warrants.

Net: entry band correct (0), but the **~3% entry / ~10%-Confirmed ceiling** is docked one notch for a ~3.2× winner —
the **ceiling is one tier too low** (Confirmed ~10% vs Core 15–25%). The explicit add path, the ~10% (not ~3%)
ceiling, **and the genuinely back-loaded path that rewarded the proof-gated caution** hold it firmly at one notch,
not two. **Size-distance = 1.** (Lighter than NVDA's "firm 1": there, near-zero drawdown gave the timidity no
vindication; here the −11.7% dip + 4-month flat stretch + proof-then-rip sequence give the cautious entry real
path-justification — the deduction is the *ceiling*, not the entry, and it is the softest 1 in the winner set.)

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes, precisely. The card's binding constraint — *reflexive financing dependence
  (fund the build cheaply without dilution) AND convert contracted power into connected revenue-producing capacity,
  with Microsoft/Meta concentration + undisclosed spread as co-binding* — is the exact axis the outcome turned on.
  The single fact that drove the May re-rating (**capex funded without further equity dilution**) is the precise
  resolution of the card's #1 named risk; the ARR-beat resolved the conversion leg; the **$27B Meta** deal resolved
  the concentration/scale unknown upward. The Runner isolated the deciding variables and **sized for them rather than
  pretending to resolve them** (held the initial to the low end, capped below Core).
- **Right module dominance?** Yes. The **M2 (+2)** mechanism/bottleneck signal (real power/capacity bottleneck,
  "sold out," Microsoft+Meta anchors, forcing metric = connected MW + ARR) was the dominant driver, supported by
  **M3 (+1)** profit-pool/durability and the **M6 (+1)** structured-entry read, with **M5 (−1)** correctly sizing
  *down* for reflexive financing rather than vetoing, and **M1 0 / M4 0** treating forward-economics uncertainty and
  the funding warning as a **size cap + kill-gate, not a WATCH** (the explicit cure for the old "more questions →
  downgrade to 0%" disease). That is the intended dominance pattern for `exceptional_bottleneck`
  (`WEIGHTING_HARNESS §4`: positive emphasis M2/M3/M4; price/financing = modulator + gate).
- **No lookahead?** On the face of the card, evidence is all dated ≤ 2026-01-01 (FY2024 20-F; Q1–Q3 2025 6-Ks /
  shareholder letter through 2025-11-11; Microsoft 2025-09-08; Sept-2025 equity + convertible prints; CoreWeave/IEA
  comps; 2025-12-31 quote; short-interest 2025-12-30; Nasdaq-100 change 2025-12-13). Full lookahead adjudication is
  the Auditor's job (out of Scorer scope); on the face of the card, clean.

**Reasoning = sound.** Correct key variable (and it is the variable the outcome turned on), correct module dominance
(M2-led, M3 support), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (sealed dominance + `WEIGHTING_HARNESS §4` for an `exceptional_bottleneck` → **M2/M3**, with
  M6/price/financing as structured-entry modulator and M5 as the sizing risk).
- **Got:** carried by **M2 (+2)** establishing the dated power/capacity bottleneck (the *reason to own*), with
  **M3 (+1)** profit-pool/durability and **M6 (+1)** structured entry in support, and **M5 (−1)** sizing down the
  reflexive-financing risk. Most load-bearing = **M2/M3.**

**dominant_module (got) = M2/M3; dominant_module_expected = M2/M3. Match.** The one place the dominant modules
under-delivered is the ceiling — M2's +2 bottleneck and M3's durability did not lift the cap into Core (the
size-distance-1 deduction), but that is a sizing limitation, not a dominance miss. (Honest note: M3 was held to +1,
not +2, by governance/key-man + undisclosed-spread discounts; the realized window does not yet adjudicate durability,
so the +1 is not faulted here.)

### Veto (fired vs expected)

- **veto_expected = no** (sealed; `exceptional_bottleneck` → valuation/financing rarely a hard veto, downside +
  kill-gates control size).
- **veto_fired = no.** No hard veto; financing/valuation correctly acted as a size cap + explicit kill-gates (net-cash
  at 9/30/25, no near maturities, blue-chip receivables → survivable, not a bankruptcy case). **Match** — and correct:
  a hard veto here would have produced the WATCH/0% failure and missed a ~3.2× move. M5's −1 was the *right* posture
  (size down, gate, don't kill).

### Failure tags (from `WEIGHTING_HARNESS §7` list)

- `valuation_overweighted` — **NOT present** (the optical trailing multiple was a size modulator, not a veto; the
  gate held — the key success).
- `confidence_used_as_veto` — **NOT present** (M1 0; the undisclosed forward economics were a size haircut, not a
  WATCH — the explicit redesign fix).
- `bottleneck_underweighted` / `mechanism_missed` / `theme_missed` — **NOT present** (M2 +2 correctly named and led
  with the power/capacity bottleneck; the forcing metric was specified).
- `financial_reality_underweighted` — **NOT present** (M4 0 correctly split operating-confirm vs funding-warn and
  routed the funding risk to a kill-gate, not a veto; the funding risk then resolved favorably).
- `inversion_veto_missed` — **NOT present** (no veto warranted; survivable, and the inversion path it named was the
  one that *reversed*).
- `hold_winner_failed` / `no_add_rule` / `no_trim_rule` — **NOT present** (existing-position HOLD correct on an intact
  inflecting thesis; add and trim/kill rules both explicit and well-specified).
- `too_small_missed_asymmetry` — **PRESENT (primary, soft).** The name ~3.2×'d; the ~3% entry / ~10%-Confirmed ceiling
  left meaningful asymmetry uncaptured. Tagged **soft** (softer than NVDA's "firm"): the back-loaded path (−11.7% dip
  + 4-month flat stretch, with the run arriving only *after* the proof the add-path required) genuinely vindicated the
  cautious *entry* — the deduction is squarely the *ceiling*, and it stays a size-distance **1**.

**failure_tags = too_small_missed_asymmetry.** No veto / lookahead / hold-winner / valuation-overweight /
confidence-as-veto failure.

---

## 3. Verdict

The lean 6-module pipeline got the call right on the round's hardest *optics* setup: NBIS at as-of looked like the
canonical thing the old framework reflexively killed — a thin-float, heavily-shorted, no-index-bid neocloud at a
grotesque trailing multiple, openly dependent on an ATM and a still-unproven asset-backed-debt plan. The pipeline
returned a **STARTER with a real ~3% entry and an explicit confirmation-gated add path** rather than WATCH/0% —
Axis-1 **PASS**, reasoning **sound**, the **M2/M3 bottleneck stack dominant (as expected)**, **no valuation-as-veto
and no confidence-as-veto**, and an M5 −1 that correctly *sized down for* (rather than vetoed) the exact
reflexive-financing risk that then **reversed in the bull's favor** (capex funded without dilution; ARR beat guide;
$27B Meta deal). That is precisely the `WEIGHTING_HARNESS §0` disease the redesign exists to cure, and the redesign
cured it.

The one deduction is `METHODOLOGY §7`'s "too small loses points," and it is the **softest 1 in the winner set**: the
~3% entry sat inside the correct STARTER band, the genuinely **back-loaded path** (−11.7% dip, ~4 months flat, the
entire excess arriving in a single late-April→May leg *after* the add-path's proof landed) means the cautious entry
was *vindicated by the path* in a way NVDA's never was, so the limitation is the **~10% Confirmed ceiling (vs the
Core 15–25% a fully-confirmed bottleneck warrants), not the entry**. Net grade: a **strong, well-reasoned PASS** whose
only flaw is a one-tier-timid ceiling — "be braver at the ceiling, not the trigger."

**Overriding caveat:** all of the above is a **~5.5-month** read. The mechanical WINNER label is **STRONGLY
PROVISIONAL** — the win is concentrated in one ~6-week story-driven leg, and the name remains the reflexive,
sentiment-sensitive, dilution-exposed structure the card itself flagged as capable of permanent per-share impairment
if markets tighten. This case should carry low weight in any cross-case synthesis until a longer window (12m+) is
observed; treat it as a strong directional signal that the `exceptional_bottleneck` gate fired correctly, not as a
settled durable outcome.

---

## 4. results.csv row (DO NOT auto-append — returned to orchestrator)

```
lean-6module-v1,none,nbis_2026-01-01,exceptional_bottleneck,WINNER,3,STARTER,HOLD,STARTER..CORE,1,no,no,M2/M3,M2/M3,sound,too_small_missed_asymmetry,"PROVISIONAL ~5.5mo window (2025-12-31->2026-06-16; too short for durable verdict). WINNER +216.7% price=t.r. from 83.71 to 265.10 vs SPY +10.3%(748.40)/SOXX +96.5%(591.24); beat SPY ~206pt and the SEMI index SOXX ~120pt (not pure AI/semis beta). BACK-LOADED: +5.3% @+1mo, dipped to -11.7% @2026-02-05 (lowest close 73.87; only 2 closes below entry), +24% @3mo, +65% @4mo, first +100% 2026-05-04, +216% by 2026-06-01; largest interim peak-to-trough -32.1% (108.73 1/16->73.87 2/5) but trough still only -11.7% vs entry. Binding constraint (reflexive financing + capacity->ARR conversion) RESOLVED BULL: Q4'25 print 2026-02-12 rev 227.7M +547%YoY, YE25 ARR 1.25B ABOVE 0.9-1.1B guide, adj-EBITDA positive, $7-9B ARR reaffirmed; May re-rate explicitly on capex funded WITHOUT equity dilution + $27B Meta deal + Eigen AI; all 6 kill-criteria failed to trigger. Axis-1 PASS (STARTER avoided old WATCH/0% on grotesque optics + financing fear); reasoning sound (named the deciding var = financing-without-dilution, which is exactly what re-rated it); M2/M3 bottleneck stack drove it (match); M5 -1 sized down the reflexive-financing risk that then reversed favorably, no veto = correct; valuation+financing = size-cap+kill-gates not veto = WEIGHTING_HARNESS fix working. size-dist 1 (SOFTEST in winner set): ~3% entry inside band but ~10% Confirmed ceiling one tier low vs Core 15-25% for a ~3.2x winner; UNLIKE NVDA the back-loaded path (-11.7% dip + ~4mo flat, run only AFTER proof landed) VINDICATED the low-end-Starter+proof-gated-add entry -> deduction is the ceiling not the entry. Source: Yahoo Finance chart API v8 (memory/price_data_source.md); SPY/SOXX adj-close t.r., cross-check 748.40/591.24 = same anchors as nvda/intc cases; Q4'25+catalyst via SEC 6-K + Investing.com/ForeignPolicyJournal/Barchart 2026-02/05."
```

---

*Scorer used post-2026-01-01 data (allowed). Locked decision_card NOT modified. NBIS pays no dividend (price =
total return); SPY/SOXX use adjusted-close total return. Version `lean-6module-v1` / `none` matches the card.
WINDOW ~5.5mo → label STRONGLY PROVISIONAL; treat as low-weight directional signal in synthesis.*
