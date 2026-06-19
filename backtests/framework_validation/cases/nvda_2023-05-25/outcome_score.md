# Outcome Scorecard — NVDA (NVIDIA), as-of 2023-05-25 (PRE-split)

> SCORER OUTPUT. The blind Runner decision in `decision_card.json` / `decision_card.md`
> is LOCKED and was NOT modified. This file uses post-2023-05-25 market data (allowed for
> the Scorer) to reconstruct the realized outcome and grade the decision per
> `PROTOCOL.md` §6, `METHODOLOGY.md` (position ladder + §7 "too small loses points"), and
> `WEIGHTING_HARNESS.md` §7. The 10:1 split (2024-06-07) is AFTER as-of; realized return is
> measured on a **split-adjusted total-return** basis (the as-of pre-split close $379.80 =
> split-adjusted 37.98).

---

## 0. Locked decision under test (recap, not re-litigated)

| Field | Locked value |
|---|---|
| Context label | `exceptional_bottleneck` |
| Business verdict | exceptional |
| New-money verdict | **STARTER** |
| Existing-position verdict | HOLD |
| Suggested initial size | **3%** (Starter tier) |
| Suggested max size | **12%** (Confirmed-tier ceiling) |
| Buy-below / starter zone | ~$379.80 at/around as-of; add into de-rate toward ~$300–340 (pre-print ~$305 zone) |
| Add zone | Scale 8–12% ONLY on confirmation: Q2 FY24 revenue near/above the $11.0B guide AND DC margin holding toward 70% non-GAAP AND demand broad/durable |
| Binding constraint | Demand durability vs pull-forward of the $11B Q2 guide → sizes the position; valuation only widens the band / caps initial size. Secondary cap: Huang key-man/succession |
| Module signals | M1 +1 / M2 +2 / M3 +2 / M4 +1 / M5 −1 / M6 +1 |
| Hard veto | None fired (exceptional_bottleneck gate: valuation = structured-entry modulator, not veto) |

---

## 1. Realized outcome (post-as-of, Scorer-allowed)

As-of anchor: **NVDA pre-split close $379.80 on 2023-05-25** (case_control.md §2; = split-adjusted
**37.98** per the as-of quote CSV `data/asof_2023_05_25_nvda_quotes.csv`, the post-print gap-up close).
All realized figures below are **split-adjusted** and anchored to 37.98, so the June-2024 10:1 split is
handled mechanically (no pre/post discontinuity). NVDA pays only a token dividend, so total return runs a
hair above price change.

| Window | Date used | NVDA close (split-adj) | NVDA return | SPY t.r. | SOXX t.r. | NVDA − SPY |
|---|---|---:|---:|---:|---:|---:|
| As-of | 2023-05-25 | 37.98 | — | — | — | — |
| +6mo | 2023-11-27 | $48.15 | **+26.8%** | ~ +13%* | ~ +20%* | ~ +14 pt |
| +12mo | 2024-05-24 | $106.29 | **+179.9%** | **+29.5%** | **+60%** | **+150 pt** |
| +18mo | 2024-11-25 | $135.81 | **+257.6%** | ~ +47%* | ~ +115%* | ~ +211 pt |
| ~today | 2026-06-16 | $207.41 | **+446.1%** (price); **~+448% t.r.** | **+88%** | **+302%** | **+360 pt** |

\* Intermediate SPY/SOXX points (+6mo, +18mo) are interpolated/approximate; the **+12mo** and
**to-2026** SPY/SOXX figures are direct StatMuse total-return reads. The two anchored benchmark windows
are decisive for classification — NVDA beat SOXX (the semiconductor index, the toughest comparator) at
**both** anchors (+179.9% vs +60% at +12mo; +448% vs +302% to-2026), so the win is NOT merely a semi-cycle
beta ride; intermediate benchmark points are directional only.

Source prices (direct StatMuse closing-price / total-return reads):
- NVDA (split-adj): 48.15 (2023-11-27), 106.29 (2024-05-24), 135.81 (2024-11-25), 207.41 (2026-06-16).
- NVDA total return since 2023-05-25 ≈ **+448%** (StatMuse; price leg +446.1% = 207.41/37.98 − 1).
- SPY total return: **+29.5%** (to 2024-05-24), **+88%** (to 2026-06-16; close $748.40).
- SOXX total return: **+60%** (to 2024-05-24), **+302%** (to 2026-06-16; close $591.24).

**Worst drawdown — the load-bearing path fact (opposite of GOOGL/INTC):**
The lowest close over the entire 2023-05-25 → 2026-06-16 window was **$37.40 on 2023-06-07** — i.e.
**−1.5% from the as-of entry of 37.98**, reached just **13 calendar days** after as-of. NVDA then never
revisited the entry. **A holder who bought the STARTER at $379.80 was essentially never underwater** —
the worst mark-to-market against entry was about one and a half percent.

The largest *interim peak-to-trough* decline was **−36.9%**, from the 2025-01-06 peak ($149.21) to the
2025-04-04 trough ($94.18) — the DeepSeek-scare + AI-capex-doubt + April-2025 tariff selloff (same shock
window that took GOOGL −18% and INTC −15.6% *below their entries*). But for NVDA that −37% drawdown
happened **far above the as-of anchor**: the $94.18 April-2025 trough was still **+148% above entry**.
Source: StatMuse min-close / max-close queries over the stated windows.

### Price source(s)
StatMuse Money historical series — the same provider used to verify the as-of price family (the CSV S007
series cross-checks to StatMuse) and the same provider used for the `googl_2024-06-14` and `intc` scored
cases (kept consistent for cross-case comparability). The magnitude (+446% price, beating even the semi
index by ~146 pts to-2026) is far too large for provider error to flip the label.

### Mechanical label
**WINNER.** Decisive and clean: **+446% price / ~+448% total return** vs SPY **+88%** (beat by ~360 pts)
and — the discriminating test — vs the SOXX semiconductor index **+302%** (beat by ~146 pts), with the
thesis not just intact but *over-delivered*. This confirms the orchestrator's sealed expectation: **NVDA =
WINNER, exceptional_bottleneck (the canonical AI-compute bottleneck)**. Unlike the two other scored
winners (GOOGL, INTC-2024), this win was **NOT back-loaded and carried essentially no drawdown vs entry** —
the asymmetry paid almost immediately (+27% by +6mo, +180% by +12mo) and monotonically.

### Did the binding constraint resolve, and which way?
The card's binding constraint was *"demand durability vs pull-forward of the $11B Q2 guide."* Realized:
the $11B Q2 FY24 guide was not pull-forward — Data Center demand **compounded for years** (the guide was,
if anything, conservative). Every kill-criterion the card listed (guide miss / DC roll-over / DC-margin
compression / CSP design-wins-away / inventory writedowns / Huang departure) **failed to trigger** through
the window. The one genuinely unresolved risk the card sized *down* for — pull-forward — was the risk that
**did not materialize**, which is exactly why the realized outcome is the +446% top-of-table winner.

---

## 2. Grading the locked decision

### Axis-1 — Direction (PASS / PARTIAL / FAIL)

PROTOCOL §6, Winner row:
- PASS = `STARTER` or `CORE` (or explicit structured starter)
- PARTIAL = `WATCH` but names the correct key variable + clear buy/add trigger
- FAIL = `REJECT`, or `WATCH / 0%` with avoid framing

Locked new-money verdict = **STARTER** (real 3% money at as-of, explicit confirmation-gated add path to
8–12%, buy-below ~$379.80 with a de-rate add zone). It avoided REJECT, avoided WATCH/0%, and reached a
real-ownership tier on a confirmed bottleneck.

**Axis-1 = PASS.**

This is the redesign working as intended. The textbook old-framework failure here would have been
WATCH/0% — "~198x trailing GAAP after +160% YTD and a 24% one-day spike → too expensive, wait for a
pullback" — which is precisely the `WEIGHTING_HARNESS §0` disease ("miss bottleneck winners when classic
valuation looked uncomfortable" / "punish early asymmetric winners with WATCH/0%"). The
exceptional_bottleneck gate correctly held valuation to a **structured-entry modulator, not a hard veto**,
and converted the optical multiple into a *size cap* rather than a *go/no-go veto*. On direction, the
pipeline got the single most important call of the round right.

### Size-distance (0–3)

Correct size band (sealed + PROTOCOL §7): **STARTER..CORE.** Realized outcome = the canonical
exceptional_bottleneck WINNER, **+446% price / ~5.5×**, with **no drawdown vs entry**.

Locked sizing: initial **3%** (bottom-middle of the 3–5% Starter band), max **12%** (Confirmed ceiling),
with an explicit confirmation-gated add path (Q2 FY24 revenue near/above the $11B guide + DC margin holding
+ broad/durable demand → 8–12%) and a stated 12% ceiling held "below Core until the guide converts."

Scoring against `METHODOLOGY.md §7` ("a winner identified only as a tiny STARTER is **not** full marks —
'right direction, too small' must lose points") and the durability ladder (§2: the 15–25% Core tier is for
businesses you'd hold 5–10 years; the **ceiling is set by durability, not just confirmation**):

- **Band:** the initial 3% sits **inside the correct STARTER..CORE band** → by the literal PROTOCOL §6
  size-distance scale, the entry is **0** (within band). The 12% **ceiling**, however, sits at the
  **Confirmed** tier and **never reaches the Core (15–25%) tier** that an exceptional_bottleneck winner of
  this durability warranted.
- **"Too small loses points" applies, and applies harder here than in GOOGL.** This is the one case in the
  round the framework itself names as the archetype the redesign exists to catch (`WEIGHTING_HARNESS §5`:
  *"meant to catch cases like SNDK 2025 or NVDA 2023 where a classic full-MOS process may be too slow"*).
  The name 5.5×'d. A 3% entry / 12% ceiling on THE bottleneck winner leaves very large asymmetry
  uncaptured if the plan is followed mechanically and never revised beyond the 12% Confirmed cap.
- **Crucially, the realized path does NOT vindicate the caution the way GOOGL's did.** GOOGL earned back
  its size-distance points because it was flat/lagging for 12 months and drew down −18% **below entry** —
  there, the timidity was substantially *justified by the path*. NVDA is the opposite: +180% by +12mo,
  worst-vs-entry drawdown ~**−1.5%**. The pull-forward risk the card sized down for **resolved within one
  quarter** in the bull's favor, and the confirmation trigger (Q2 FY24 landing well above the $11B guide)
  fired almost immediately — so the structured-add path, *if executed*, would have lifted the position
  toward the 12% ceiling early and cheaply. That makes the **12% ceiling itself the binding limitation**,
  not the 3% entry.
- **Mitigants that keep this a 1, not a 2:** (a) the entry **is** inside the correct band — this is genuine
  real-money ownership, not a WATCH dressed up; (b) the card carries an **explicit, well-specified
  confirmation-gated add path** to 12% — the methodology *wants* "start real, add on confirmation," and the
  realized Q2 print is exactly the confirmation that would have triggered the add; (c) the card correctly
  invokes the **exceptional_bottleneck context** and explicitly names the opposite risk
  (`too_small_missed_asymmetry`, "cf. SNDK") in its own dissent — it understood the trade-off it was making;
  (d) 12% (not 3%) is the operative ceiling, and 12% is a legitimate Confirmed-tier weight for a name with a
  live, unconfirmed pull-forward question at as-of.

Net: the **entry band is correct (0)**, but `METHODOLOGY §7` docks the **3% entry / 12%-Confirmed ceiling**
for the canonical Core-durability bottleneck winner that 5.5×'d with no drawdown — the ceiling is **one tier
too low** (Confirmed 12% vs the Core 15–25% the bottleneck warranted), and unlike GOOGL the path gave the
caution **no vindication**. The explicit add path + exceptional_bottleneck framing + the 12% (not 3%) ceiling
hold it at one notch, not two.

**Size-distance = 1** ("appropriately STARTER and inside band, but the 12% Confirmed ceiling skews one tier
small for the canonical exceptional_bottleneck winner; the explicit confirmation-gated add path and the
12% (not 3%) ceiling keep it from being a 2 — but, unlike GOOGL, the near-zero drawdown vs entry means the
timidity earned **no** path-vindication, so this is a firmer 1").

### Reasoning score (sound / shallow / wrong_reason)

- **Correct key variable named?** Yes, precisely. The card's binding constraint — *"demand durability vs
  pull-forward of the $11B Q2 guide; this, not the optical ~198x multiple, is what sizes the position"* —
  is the exact right variable, and it matches the sealed key variable ("AI compute bottleneck, pricing
  power, customer ROI"). The card identified the upside engine (full-stack accelerated-compute bottleneck:
  Hopper GPU + CUDA lock-in + NVLink/InfiniBand networking + HBM/packaging) **and** correctly isolated the
  one genuinely unresolved risk (pull-forward), tagging it as *unresolved at as-of* and sizing for it rather
  than pretending to resolve it. Realized history confirms the framing wholesale.
- **Right module dominance?** Yes. The **M2 (+2) / M3 (+2)** conviction stack — real dated demand shock +
  the bottleneck the industry must route through (M2), CUDA/full-stack profit-pool capture + operator 4/5 +
  clean governance (M3) — drove the STARTER, M4 (+1) confirmed the economics (margins/cash/operating
  leverage), M6 (+1) supported structured entry, and M5 (−1) sized down rather than killing it. That is
  exactly the intended dominance pattern for `exceptional_bottleneck` (`WEIGHTING_HARNESS §4`: positive
  emphasis M2/M3/M4; price = structured-entry modulator).
- **No lookahead?** The card draws only on pre-2023-05-25 evidence (Q1 FY24 8-K + CFO commentary + call,
  all 2023-05-24; FY23 10-K 2023-02-24; AMD MI300 CES-2023; DEF 14A 2023-05-08; as-of price series). It
  correctly excludes the Q1 FY24 10-Q (filed 2023-05-26, +1 day) and treats Q2 FY24 as a forward monitor
  event, not evidence. (Full lookahead adjudication is the Auditor's job and is out of Scorer scope; the
  checker status is CLEAN-WITH-NOTES; on the face of the card, clean.)

**Reasoning = sound.** Correct key variable, correct module dominance (M2/M3), no visible lookahead.

### Dominant module (got vs expected)

- **Expected** (sealed dominance + `WEIGHTING_HARNESS §4` for an exceptional_bottleneck → **M2/M3**, with
  M6 price as structured-entry modulator).
- **Got:** the call was carried by the **M2 (+2) / M3 (+2)** conviction stack — M2 establishing the dated
  AI-compute bottleneck (the *reason to own*) and M3 establishing durable profit-pool capture via the
  CUDA/full-stack moat + operator grade (the *durability that should have set the ceiling*), with M4
  confirming the economics and M6 setting structured entry. The two most load-bearing modules are
  **M2 and M3**, co-dominant.

**dominant_module (got) = M2/M3; dominant_module_expected = M2/M3. Match.** The right modules drove the
call. (Note: the one place the dominant modules *under-delivered* is the size ceiling — M3's strong
durability read (+2, operator 4/5) justified a **Core** ceiling, but the aggregation capped at Confirmed
12% on the unconfirmed-demand caveat; that is the size-distance-1 deduction, not a module-dominance miss.)

### Veto (fired vs expected)

- **veto_expected = no** (sealed; exceptional_bottleneck → valuation rarely a hard veto, downside controls
  size).
- **veto_fired = no.** No hard veto fired; valuation correctly acted as a structured-entry modulator + size
  cap. **Match** — and this is the correct behavior: a hard valuation veto here would have produced the
  WATCH/0% failure and missed a 5.5× winner.

### Failure tags (from `WEIGHTING_HARNESS §7` list)

Candidate review:
- `valuation_overweighted` — **NOT present** (the key success: the ~198x multiple was a size modulator, not
  a veto; the exceptional_bottleneck gate held).
- `confidence_used_as_veto` — **NOT present** (M1 +1; forward-EPS/share%/supply-conversion gaps were
  haircuts, not a WATCH).
- `bottleneck_underweighted` — **NOT present at the thesis level** (M2/M3 both +2 correctly named and
  weighted the bottleneck). *Arguably* present at the *sizing* level (the bottleneck's durability did not
  lift the ceiling into Core) — but that is more precisely captured by `too_small_missed_asymmetry`.
- `hold_winner_failed` — **NOT present** (existing-position HOLD on an intact, inflecting thesis is correct;
  the thesis over-delivered).
- `no_add_rule` / `no_trim_rule` — **NOT present** (both explicit and well-specified).
- `too_small_missed_asymmetry` — **PRESENT (primary, soft).** The name 5.5×'d with ~−1.5% worst drawdown
  vs entry; the 3% entry / 12%-Confirmed ceiling on the canonical exceptional_bottleneck winner left
  meaningful asymmetry uncaptured, and — unlike GOOGL — the path gave the caution no vindication. Tagged as
  the **primary** failure flag here (a firmer call than GOOGL's "soft/secondary"), because the realized path
  removes GOOGL's drawdown-justification mitigant. It remains a **size-distance 1, not 2**, only because the
  entry sat inside the correct band and the explicit confirmation-gated add path + 12% ceiling were present.

**failure_tags = too_small_missed_asymmetry.** No other failure tag; no veto/lookahead/hold-winner failure.

---

## 3. Verdict

The lean 6-module pipeline got the **single most important call of the round right on direction**: on the
textbook "priced-for-perfection near a top" setup (~198x trailing GAAP, +160% YTD, +24% one-day spike), it
returned a **STARTER with a real 3% entry and an explicit confirmation-gated add path** rather than the
old-framework WATCH/0% — Axis-1 **PASS**, reasoning **sound**, the M2/M3 bottleneck stack dominant (as
expected), **no valuation-as-veto and no confidence-as-veto** failure. That is exactly the disease
`WEIGHTING_HARNESS §0` / §5 was built to cure (it even names "NVDA 2023" as the archetype), and the redesign
cured it.

The one deduction is `METHODOLOGY §7`'s "too small loses points," and it bites **harder here than in
GOOGL**: NVDA is the canonical Core-durability bottleneck winner, it 5.5×'d, and — decisively — it carried
**no drawdown vs entry** (worst −1.5%, +180% by +12mo), so the **12% Confirmed ceiling (vs the Core 15–25%
the bottleneck warranted) earned no path-vindication** for its timidity. The structured-add path, the
exceptional_bottleneck framing, and the fact that 12% (not 3%) is the operative ceiling keep this a
**size-distance 1, not 2** — the entry was correctly inside the STARTER band; the **ceiling** is the one
tier too low. Net grade: a **strong, well-reasoned PASS** whose only flaw is a one-tier-timid ceiling on
THE bottleneck winner — the mirror image of GOOGL's "be braver at the ceiling, not the trigger."

---

## 4. results.csv row (DO NOT auto-append — returned to orchestrator)

```
lean-6module-v1,none,nvda_2023-05-25,exceptional_bottleneck,WINNER,3,STARTER,HOLD,STARTER..CORE,1,no,no,M2/M3,M2/M3,sound,too_small_missed_asymmetry,"WINNER +446% price/~+448% t.r. to 2026-06-16 from split-adj 37.98 ($379.80 pre-split) vs SPY +88%/SOXX +302%; beat SPY ~360pt and the SEMI index SOXX ~146pt. +6mo +26.8% ($48.15); +12mo +179.9% ($106.29) vs SPY +29.5%/SOXX +60% (beat both ~150/~120pt); +18mo +257.6% ($135.81). NOT back-loaded, NO drawdown vs entry: lowest close 37.40 @2023-06-07 = -1.5% from entry (13d post-as-of), never revisited; largest interim peak-to-trough -36.9% (Jan6'25 149.21->Apr4'25 94.18) but trough still +148% above entry. Binding constraint (pull-forward of $11B Q2 guide) resolved bull within 1 quarter; every kill-criterion failed to trigger. Axis-1 PASS (STARTER avoided old WATCH/0% valuation-veto); reasoning sound; M2/M3 bottleneck stack drove it (match); M5 -1 sized down no veto (correct for exceptional_bottleneck); valuation=structured-entry modulator not veto = the WEIGHTING_HARNESS §0/§5 fix working (names 'NVDA 2023' as archetype). size-dist 1: 3% entry inside band but 12% Confirmed ceiling one tier low vs Core 15-25% the canonical bottleneck warranted; unlike GOOGL the ~-1.5% worst-vs-entry drawdown gives the timidity NO path-vindication -> firmer 1; add-path+12%-ceiling keep it from 2. Source: StatMuse total-return (split-adjusted)."
```

---

*Scorer used post-2023-05-25 data (allowed). Locked decision_card NOT modified. Returns split-adjusted
total return per case_control.md pre-split convention. Version `lean-6module-v1` / `none` matches the card
(VERSIONS.md current ACTIVE).*
