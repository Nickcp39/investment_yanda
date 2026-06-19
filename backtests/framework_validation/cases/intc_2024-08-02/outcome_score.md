# Outcome Score — INTC (as of 2024-08-02)

> **Scoring pass.** Post-as-of data IS allowed here. The locked blind decision
> (`decision_card.json` / `decision_card.md`, locked 2026-06-17) is NOT modified.
> This file reconstructs the realized outcome and grades the decision against
> `PROTOCOL.md §6`, `METHODOLOGY.md §7`, and `WEIGHTING_HARNESS.md §7`.
>
> Pivotal case of the same-company discrimination pair (vs `intc_2021-04-23`).

---

## 1. Realized outcome (reconstructed from post-2024-08-02 data)

**As-of baseline:** $21.48 close (2024-08-02; −26.1% on the day; confirmed in the pack
and corroborated by CNBC "plunged 26% to $21.48"). **Dividend was suspended** with the
Aug 1 2024 release and stayed suspended through the entire window, so **price return ≈
total return** — no reinvestment adjustment needed.

### INTC price path

| Window | Date used | INTC close | Return from $21.48 | Source |
|---|---|---:|---:|---|
| As-of | 2024-08-02 | $21.48 | — | CNBC / pack (StatMuse raw $21.34) |
| +6 mo | 2025-02-03 | $19.38 | **−9.8%** | StatMuse |
| +12 mo | 2025-08-04 | $19.50 | **−9.2%** | StatMuse |
| +18 mo | 2026-02-02 | $48.81 | **+127.2%** | StatMuse (news corrob. "~$48 Feb 2026") |
| To-date | 2026-06-16 | $117.05 | **+444.9%** | StatMuse + stockanalysis.com (2 sources) |

Cross-check: StatMuse's own return engine reports +436.9% end-to-end off a slightly
higher base; all variants land ~+437% to +449% (a ~5.4× total). The to-date $117.05
is double-confirmed.

### Benchmarks (same windows, price-return; total-return ~0.6–1.5pt lower)

| Window | SPY | SOXX | INTC | INTC vs SPY | INTC vs SOXX |
|---|---:|---:|---:|---:|---:|
| +6 mo | +12.9% | +4.0% | −9.8% | **−22.7pt (lag)** | −13.8pt (lag) |
| +12 mo | +19.9% | +17.1% | −9.2% | **−29.1pt (lag)** | −26.3pt (lag) |
| +18 mo | +32.9% | +72.4% | +127.2% | +94.3pt (beat) | +54.8pt (beat) |
| To-date | +43.8% | +189.4% | **+444.9%** | **+401pt (beat)** | **+255pt (beat)** |

(SPY baseline $521.91 → $750.42; SOXX $204.41 → $591.57. Source: StatMuse, cross-checked
stockanalysis.com / Yahoo. SOXX 3-for-1 split was 2024-03-07, pre-baseline — no artifact.)

### Worst drawdown and recovery

- **Worst close: $18.13 on 2025-04-08 (−15.6%)**; intraday low $17.67 same day. The trough
  was the broad "Liberation Day" tariff sell-off (markets bottomed 2025-04-08, snapped back
  the 9th: INTC +19.15% on 2025-04-09). Source: StatMuse.
- **Note:** the realized floor was ~$18, NOT single digits — the pack's collector did not
  assume a deeper low, so this does not affect the grade.
- **Sharp recovery:** essentially the **entire** gain is post-bottom. INTC was ~flat-to-down
  for the first ~12 months, then ran +84% in calendar 2025 (Motley Fool) and ~3× again in H1
  2026 (~$37 at YE2025 → $117 by 2026-06-16) on a Q1-2026 earnings blowout (+24% on the print)
  and foundry-customer news. The to-date endpoint sits in a volatile stretch (−8.45% on
  2026-06-16 itself).

### Events that defined the realized path (characterization only)

- **2024-12-01:** CEO Pat Gelsinger "retires" (board-driven ouster); Zinsner + Holthaus interim.
- **2025-03 (announced ~Mar 12–13):** **Lip-Bu Tan appointed CEO** — new operator.
- **2025-04-08:** cycle bottom ~$18 (tariff sell-off), +19% next day.
- **2025-08-22:** **U.S. government takes ~9.9% equity stake** — $8.9B (433.3M sh @ $20.47),
  converting the remaining $5.7B CHIPS award + $3.2B DoD money to equity.
- **Aug 2025:** **SoftBank $2B** equity investment.
- **Sep–Dec 2025:** **Nvidia $5B** equity investment (~4.4%, 214.8M sh @ $23.28) + AI/x86
  collaboration. Combined US + Nvidia + SoftBank ≈ $15.9B new capital.
- **Late 2025 – H1 2026:** **18A / 18A-P node ramp on schedule**; foundry signed commitments
  rise past $15B; reports of external foundry customers amid TSMC capacity tightness.
- **~Q1 2026:** earnings blowout (~$13.6B rev, $0.29 EPS vs ~$0.01 est) → +24% day.

### Mechanical label

**WINNER.** Realized +444.9% to-date vs SPY +43.8% / SOXX +189.4% — a strong absolute gain
that beat BOTH benchmarks decisively (+401pt over SPY, +255pt over SOXX), and the thesis
validated: the foundry-cash binding constraint was resolved by external capital
(US/Nvidia/SoftBank ≈ $16B) + a new operator + on-schedule 18A — exactly the
turnaround-bottom the case hypothesized, not a structural-decline trap.

> Important path nuance: this is a **back-loaded** WINNER. For the first ~12 months it was a
> textbook falling knife — −9.8% at +6mo and −9.2% at +12mo, lagging SPY by 23–29pt, and it
> dipped to ~$18 (−15.6%) in April 2025. The avoid call "felt right" for a full year before the
> turn. But the rubric scores the realized outcome, and the realized outcome is a clear winner.

---

## 2. Grade of the locked decision

**Locked blind decision:** new money **WATCH** (0% real money; tracking ≤1%); existing
position **TRIM**; business verdict **bad**; context `structural_decline_trap`; explicit
avoid framing ("optical cheapness is the trap signature, not a margin of safety"; "do not
catch the falling knife").

### Axis-1 (size/direction) — **FAIL**

Per `PROTOCOL.md §6`, **Winner** row: a Winner scored **`WATCH / 0%` with avoid framing** is a
**FAIL** (Pass requires STARTER/CORE or an explicit structured starter; Partial requires WATCH
that names the correct key variable AND a clear buy/add trigger as a *tracking-to-buy* posture
— not an avoid posture).

The decision is borderline-Partial on paper because the card DID name the correct key variable
(foundry-loss trough + OCF-covers-capex + DCAI stabilization) and DID give an add trigger
(re-rate to STARTER on confirmation). Three things hold it at FAIL rather than Partial:

1. The framing is **avoid**, not watch-to-buy: business verdict "bad," existing-position **TRIM**
   (cut a holder toward zero), "do not catch the falling knife," 0% real money. PROTOCOL §6 puts
   "WATCH / 0% with avoid framing" explicitly in the **Fail** cell.
2. The named key variables are exactly the ones that resolved **favorably** — the kill criteria
   (operating losses trough, cash covers capex, leadership/strategic backing) all flipped the
   right way (new CEO, US/Nvidia/SoftBank capital, 18A on schedule), yet the posture was to stay
   out and trim, not to size in on the very confirmations it correctly enumerated.
3. The existing-position **TRIM** call would have forced a holder to sell into a ~$18–21 base that
   subsequently went to $117 — the largest possible miss for an existing holder.

So this is the canonical `missed_winner` failure that the harness was built to reduce
(WEIGHTING_HARNESS §0: "punish early asymmetric winners with WATCH / 0%").

### Reasoning score — **shallow** (direction defensible at as-of, but the structural-decline call was over-weighted)

`PROTOCOL.md §6`: sound = correct key variable + correct module dominance + no lookahead;
shallow = direction acceptable but mechanism weak; wrong_reason = right by accident.

- No lookahead — the run is clean (`material_audit.md` CLEAN; `runner_dissent` explicitly
  confirms no post-as-of info used). 
- The card correctly identified the binding constraint (foundry cash gap) and the right monitor
  variables — that part is sound.
- But it mechanically resolved a genuinely two-sided question to **0% / TRIM / "bad"** by treating
  M4 (−2) + M5 (−2) as a near-veto, when its OWN M5 finding conceded near-term survival was NOT in
  question (~$29B liquidity, self-funded reset *extends* runway) and its OWN dissent flagged the
  too-harsh edge. A genuinely two-sided, survivable, sub-book reset with a clean named key variable
  is the textbook **tracking-to-STARTER** setup, not an avoid/trim. The mechanism reasoning leaned
  on "structural_decline_trap" harder than the evidence supported — hence **shallow**, not sound.
  (Not `wrong_reason`: the diagnosis wasn't accidentally right; it was a reasonable-but-too-harsh
  read of a real risk.)

### Size-distance — **3** (opposite action)

`PROTOCOL.md §6`: 3 = opposite action (e.g., reject a winner). Correct band for a Winner is
**STARTER..CORE**; the decision delivered **0% (WATCH) + TRIM an existing holder**. Rejecting /
trimming a winner is the opposite action → **3**. (Even the 1% tracking-sliver cap does not pull
this back to a 2: a holder was told to TRIM, which is directionally opposite to STARTER+.)

### Veto

- `veto_fired`: **no** flat zero-REJECT hard veto fired (the card states this explicitly; it
  landed on WATCH, one notch above REJECT, because balance-sheet survival was not in question).
  But M4 + M5 (both −2) functioned as an **effective size-veto** that barred any STARTER-or-larger
  position — operationally a near-veto. Recorded as `veto_fired = no` (no hard zero), with the
  note that the effective near-veto is what produced the wrong size.
- `veto_expected`: **no.** Realized = WINNER → no veto should have fired. The expected posture was
  STARTER (tracking-to-buy), not a veto. → **veto mismatch: fired-effectively where none expected.**

### Dominant module — got **M4/M5**, expected **M2/M3**

- **Got:** the decision was driven by **M4 Financial Reality (−2)** and **M5 Inversion/Trap (−2)**
  — the card names M4 "the binding module" and M5 the effective size-veto.
- **Expected (for a realized WINNER turnaround):** **M2 (theme/mechanism)** + **M3 (profit pool /
  durability)** should have carried more weight — the live AI-compute + foundry-sovereignty theme
  was real (card's own M2), and the durability/operator question (M3) is what actually turned
  (new operator + sovereign/strategic capital de-risked the franchise). The pipeline correctly
  saw the as-of financial distress but let the warning modules dominate a name whose forward
  durability inflected. → **dominant-module mismatch.**

### Failure tags

- `too_small_missed_asymmetry` — primary. A WINNER taken to 0%/WATCH; the asymmetric
  recovery (self-funded reset + sub-book + named key variable + survivable balance sheet) was
  available at as-of and was declined.
- `inversion_veto_missed` — the M5 trap-test fired (as an effective near-veto) on a name that
  was NOT a trap; an inversion call that should have stayed a size-haircut became a de-facto
  avoid. (Mirror of the usual "missed a trap" — here the trap test produced a false positive.)
- `financial_reality_overweighted` *(maps to the spirit of `financial_reality_underweighted`'s
  opposite; tag retained verbatim where a registry tag exists)* — M4's as-of GAAP loss was
  real but transitional; weighting it as a −2 binding/near-veto over-anchored on trailing
  distress vs forward durability. Recorded in notes since the closed tag list has no exact
  "overweighted" twin.
- NOT `hindsight_leak` — the run is clean.

> Same-company pair note (vs `intc_2021-04-23`): this pair stress-tests whether the pipeline can
> tell the SAME company apart at two dates. The 2021 case (IDM 2.0, pre-write-down) is the sealed
> TRAP; the 2024 post-crash case is the realized WINNER. The pipeline applied the SAME
> structural-decline frame to both — correct (or near-correct) on 2021, but WRONG on 2024. The
> discrimination failure is that the −26% reset + dividend cut + sub-book + survivable balance
> sheet (the 2024 facts) are precisely what distinguishes a capitulation bottom from the 2021
> "expensive optimism" setup, and the pipeline did not let those facts move it off the trap label.

---

## 3. Verdict summary

| Field | Value |
|---|---|
| Mechanical label | **WINNER** (+444.9% to-date vs SPY +43.8% / SOXX +189.4%) |
| Axis-1 (size/direction) | **FAIL** (Winner taken to WATCH/0% + TRIM, avoid framing — PROTOCOL §6 Winner→Fail cell) |
| Reasoning score | **shallow** (clean, key variable named, but structural-decline frame over-weighted a survivable two-sided reset) |
| Size-distance | **3** (opposite action — rejected/trimmed a winner; correct band STARTER..CORE) |
| Veto fired / expected | no (hard) / no — but an **effective M4+M5 near-veto** mis-fired where none was warranted |
| Dominant module got / expected | **M4, M5** / **M2, M3** (mismatch) |
| Failure tags | `too_small_missed_asymmetry`, `inversion_veto_missed`, (financial_reality_overweighted — see notes) |
| Lookahead | none (CLEAN) |

**One-line:** The pipeline **missed a turnaround** — it correctly read the as-of financial
distress and named the right key variable, but resolved a survivable, sub-book, self-funded
reset to 0%/WATCH/TRIM as a "structural_decline_trap," and the name went on to ~5.4× and beat
both SPY and SOXX, with the very kill-criteria it listed (operator change, cash coverage, 18A)
all flipping favorably.

---

*Scored 2026-06-19 against the locked blind decision card. The decision card was not modified.*
