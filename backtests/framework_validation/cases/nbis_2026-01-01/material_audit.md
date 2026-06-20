# Material Pack Lookahead Audit — NBIS 2026-01-01

Spec: [backtests/framework_validation/LOOKAHEAD_CHECKER.md](../../LOOKAHEAD_CHECKER.md).
Independent checker pass for the **lean-6module-v1 clean re-run**. As-of date: **2026-01-01**.
Files audited (top-level only): `case_control.md`, `sources_used.csv`, `raw_extracts.md`, `evidence_spine.md`.

> Context for this audit: the prior `_v0` pilot ran NON-BLIND (self-run). These top-level materials were
> carried forward for the v1 blind re-run, so they are re-audited **hard** for any post-as-of leakage that a
> self-run could have admitted. **The `_v0/` archive was NOT read** (per case control + the re-run brief). I did
> not collect this pack and did not consult `companies/nbis/`.
>
> Special hazard flagged in the brief: the as-of (2026-01-01) is **recent** — only ~5–6 months before the audit
> date (2026-06). The most dangerous leaks are therefore the *very next* events: Q4'25 / FY2025 results and the
> Q4'25 shareholder letter (reported/filed Feb 2026), any 2026 financing/contract, the Goldman PT raise to ~$205
> on the ~$27B Meta expansion (2026), and any post-2025-12-31 price. Each is checked ABSENT below.

## 0. Audit Verdict

- **Verdict: CLEAN.**
- **0 load-bearing post-cutoff facts.** No outcome-aware language. No decision / thesis / valuation judgment /
  position size present in any of the four material files (correct for a material pack).
- The pack contains heavy **forward-looking** content — the $7–9B FY2026 ARR target, the ~2.5GW CYE2026 contracted-
  power guidance, the 800MW–1GW CYE2026 connected-power guidance, the three-pronged 2026 financing plan, the ATM
  authorization, and the Microsoft tranche schedule through 2031. These are all **management guidance/targets
  stated on or before the as-of date** (the Q3'25 release + CEO letter, both 2025-11-11), not realized post-cutoff
  outcomes → correctly admissible as as-of-knowable.
- One genuine self-flag is handled correctly inside the pack (not a leak): the Q3 letter **cover graphic** shows
  "$4.3B ARR at year-end 2026," which contradicts the $7–9B target stated twice in the letter body. The runner
  treats the body figure ($7–9B) as the stated target and flags the cover number as a likely design artifact
  (raw_extracts §H). This is a correct as-of disambiguation, not a hindsight intrusion.

## 1. Source-Date Check (every `sources_used.csv` row: public_date ≤ 2026-01-01?)

WEB-VERIFIED this pass (highest-risk / most-recent / load-bearing rows):
- **S012/S013 (Q3'25 release + CEO letter, 2025-11-11):** CONFIRMED via Nasdaq/Businesswire/Yahoo/Nebius newsroom
  — release dated **2025-11-11**; Meta deal "~$3 billion over 5 years"; ATM "up to 25 million Class A shares" with
  a prospectus supplement planned **2025-11-12**. All match the pack.
- **S007/S008 (Microsoft deal, 2025-09-08):** CONFIRMED via SEC 6-K listing — "$17.4 billion through 2031,"
  expandable to "$19.4 billion," Vineland NJ, 5-year term, tranches during 2025–2026. Verbatim match.
- **S021 (Nasdaq-100 reconstitution, 2025-12-13, eff. 2025-12-22):** CONFIRMED — the six adds are ALNY, FER, INSM,
  MPWR, STX, WDC; **NBIS is not among them.** The pack's "NBIS NOT added → no index tailwind" is correct.
- **S022 (Benzinga short interest, 2025-12-30):** CONFIRMED to the decimal — 33.07M shares short, **15.47% of
  float**, **2.76 days** to cover, as of 2025-12-30.
- **Goldman target headline (raw_extracts §L):** CONFIRMED the $155 Buy target was a **November 2025** action
  (analyst A. Duval). [The later raise to ~$205 on the ~$27B Meta expansion is a **2026** event — POST-as-of,
  NOT in the pack, NOT used. See §4.]

| source_id | public_date | ≤ as_of? | web-verified this pass | issue |
|---|---|---|---|---|
| S001 FY2024 Q4 release (6-K Ex-99.1) | 2025-02-20 | yes | — (primary; internally consistent) | none |
| S002 FY2024 20-F | 2025-04-30 | yes | — | none |
| S003 Q1'25 release | 2025-05-20 | yes | — | none |
| S004 Q1'25 shareholder letter | 2025-05-20 | yes | — | none |
| S005 Q2'25 release | 2025-08-07 | yes | — | none |
| S006 Q2'25 shareholder letter | 2025-08-07 | yes | — | none |
| S007 Microsoft deal release | 2025-09-08 | yes | **yes** (terms verbatim) | none |
| S008 Microsoft deal 6-K | 2025-09-08 | yes | **yes** | none |
| S009 $2.75B convertible notes pricing | 2025-09-10 | yes | — (consistent w/ S010/S011) | none |
| S010 $1.0B equity offering pricing | 2025-09-10 | yes | — | none |
| S011 offerings closing (~$4.2B) | 2025-09-15 | yes | — | none |
| S012 Q3'25 release | 2025-11-11 | yes | **yes** (date, Meta, ATM) | none |
| S013 Q3'25 CEO shareholder letter | 2025-11-11 | yes | **yes** | none |
| S014 as-of price CSV (Yahoo chart API) | 2025-12-31 | yes (= last trade ≤ as-of) | method-verified (see note) | none |
| S015 Dec-2024 $700M raise (NVIDIA/Accel/Orbis) | 2024-12-02 | yes | — | none |
| S016 Nasdaq relisting investor update | 2024-10-17 | yes | — | none |
| S017 Yandex Russia divestiture (6-K) | 2024-02-05 | yes | — | none |
| S018 CoreWeave IPO pricing | 2025-03-27 | yes | — | none |
| S019 CoreWeave Q3'25 results | 2025-11-10 | yes | — | none |
| S020 IEA Energy and AI report | 2025-04-10 | yes | — | none |
| S021 Nasdaq-100 reconstitution | 2025-12-13 | yes | **yes** (NBIS excluded) | none |
| S022 Benzinga short interest | 2025-12-30 | yes | **yes** (15.47% float) | none |
| S023 Avride/Uber + Toloka/ClickHouse | 2025-10-01 | yes | — | none |

All 23 `sources_used.csv` rows have `public_date ≤ 2026-01-01`. **0 source-date issues.**

**As-of price note (S014):** the price-of-record is the **2025-12-31 close $83.71** from a locally-saved Yahoo
chart-API series (the project's standard price method; Stooq is dead per memory). The saved late-Dec OHLC is
internally consistent (a smooth $93→$84 drift into year-end) and 2025-12-31 is correctly the last trading day on or
before the as-of. Live quote sites now only return June-2026 prices, so the historical point cannot be re-pulled
live; the saved series is accepted as the price-of-record and **no post-2025-12-31 price appears anywhere** in the
pack. (Web search incidentally surfaced current ~June-2026 quotes — NOT opened/used.)

## 2. Claim Traceability (load-bearing claims → allowed source_id)

| key claim | source_id(s) | traceable? |
|---|---|---|
| As-of price $83.71 (12/31/25); mkt cap ~$21.1B (251.8M sh × close) | S014, S012 | yes |
| FY2024 baseline: rev $117.5M (+462%), adj EBITDA loss −$266.4M, cash $2,449.6M, MarchARR ≥$220M | S001 | yes |
| ARR ramp $220M → $249M(Q1) → $430M(Q2) → ~$551M(Q3) | S001, S004, S006, S013 | yes |
| Q3'25 rev $146.1M (+355% YoY / +39% QoQ); core ~90% of rev; group adj EBITDA −$5.2M; net loss −$119.6M | S012, S013 | yes |
| Core adj-EBITDA positive (~19% margin Q3'25) | S005, S013 | yes |
| Q2'25 GAAP +$502.5M was a Toloka revaluation gain, not operations; adj net loss −$91.5M | S005 | yes |
| Balance sheet 9/30/25: cash $4,794.8M, non-current debt $4,090.8M → ~net-cash at quarter end | S012 | yes |
| Capex ramp H1'25 $1,054.5M; Q3'25 $955.5M; 9M PP&E −$2,010.0M; 9M op cash −$432.4M | S005, S012 | yes |
| Microsoft ~$17.4B→$19.4B through 2031, 5-yr, Vineland NJ, tranches 2025–26 | S007, S008 | yes |
| Meta ~$3B over 5 yr (capacity-limited), announced 2025-11-11 | S012, S013 | yes |
| Contracted power → ~2.5GW CYE2026 (from 1GW); 800MW–1GW connected CYE2026; 220MW/100MW CYE2025 | S013 | yes |
| FY2026 ARR target $7–9B (stated twice in CEO letter) | S013 | yes |
| Sept-2025 raise: $2.75B converts (2030/2032; 1.00%/2.75%; conv ~$138.75) + $1.0B equity @ $92.50; ATM ≤25M Cl A | S009, S010, S011, S012 | yes |
| NVIDIA+Accel+Orbis $700M @ $21.00 (Dec 2024); relisted Oct 2024; Russia divested ~$5.4B mid-2024 | S015, S016, S017 | yes |
| NBIS NOT in Nasdaq-100 (Dec 2025); short interest ~15.5% of float | S021, S022 | yes |
| CoreWeave comp: ~$23B IPO EV; 2024 rev $1.9B; MSFT 62% of 2024 rev; Q3'25 rev $1.36B | S018, S019 | yes |
| IEA: data-center power ~945 TWh by 2030; ~20% of projects at delay risk | S020 | yes |

No orphan / un-sourced load-bearing claim. Every claim traces to a source dated ≤ as-of.

## 3. Outcome-Aware Language Check

Scanned all four files for hindsight tokens ("later", "subsequently", "as we now know", "went on to",
"rallied/collapsed to", "in hindsight", "turned out") and for any post-as-of price.
- **0 load-bearing matches.** The forward 2026/2027/2031 figures are explicitly as-of **guidance/targets**
  (CEO letter, Microsoft contract schedule), not realized results.
- The open questions in `evidence_spine.md` §2 (deal margins, financing/dilution path, capacity→revenue
  conversion, customer concentration, ARR definition, governance) are recorded as **unresolved** — never as a known
  outcome.
- No post-2025-12-31 price anywhere; the only price is the as-of $83.71 plus the trailing late-Dec daily closes.

## 4. Post-Cutoff Fact Intrusion (NBIS-specific forbidden registry — not yet in LOOKAHEAD_CHECKER.md; each ABSENT)

> Proposed registry row to add to `LOOKAHEAD_CHECKER.md`:
> `nbis_2026-01-01 | 2026-01-01 | forbid anything after 2026-01-01 | traps below`.

| forbidden item (post-2026-01-01) | status | note |
|---|---|---|
| Q4'25 / FY2025 results + the **Q4'25 shareholder letter** (released ~2026-02-12) and the FY2025 20-F | **ABSENT** | the pack stops at the Q3'25 release/letter (2025-11-11); search surfaced the 2026-02-12 Q4 letter — NOT opened/used |
| Any **2026** ARR print or the actual FY2026 ARR vs the $7–9B target | **ABSENT** | only the as-of $7–9B *target* appears; "will it be hit?" is left as open question Q5 |
| Any **2026** financing (new debt/equity/asset-backed close) beyond the Sept-2025 raise + the as-of ATM authorization | **ABSENT** | only Sept-2025 closings + the ATM *authorization* (≤25M Cl A) are used; no 2026 draw |
| Any **2026** contract/expansion — esp. the **~$27B Meta expansion** and any new hyperscaler deal | **ABSENT** | only the as-of Microsoft ($17.4–19.4B) + Meta (~$3B) deals appear |
| **Goldman PT raise to ~$205** (on the 2026 Meta expansion) / any 2026 analyst action | **ABSENT** | only the Nov-2025 $155 Buy target is referenced (as a dated secondary headline); the $205/2026 action is excluded |
| Any **NBIS price/market-cap after 2025-12-31** (run-up or drawdown) | **ABSENT** | price-of-record is the 2025-12-31 close only |
| Index inclusion **after** Dec 2025 (a later Nasdaq-100 / S&P add) | **ABSENT** | recorded only as NOT-included as of the Dec-2025 reconstitution |
| Any 2026 capacity/connected-power *actuals* vs the CYE2025/CYE2026 guidance | **ABSENT** | only as-of targets; conversion is flagged as the key execution risk (open question Q3) |

All registry items **ABSENT**. (Discipline note: web verification incidentally surfaced several post-as-of items
— the 2026-02-12 Q4'25 letter, the Goldman $205 / ~$27B Meta 2026 raise, a June-2026 "stock surging" Benzinga item,
and current June-2026 quotes. **None were opened; none entered this audit or the pack.** Their appearance in result
lists is logged here only as the cutoff-boundary discipline check the brief asked for.)

## 5. Evidence Misuse

- **KOL / social / video:** none used as core proof. No Twitter/YouTube/Reddit/local-note source is load-bearing
  (the pack's evidence_spine §3 confirms "No KOL/social/video material was load-bearing").
- **News / narrative as lead, not proof:** the Benzinga short-interest (S022) and the Goldman target headline are
  used for **positioning/sentiment context only**, explicitly secondary, and the short-interest magnitude is a
  factual exchange-reported figure (independently confirmed). CoreWeave (S018/S019) and IEA (S020) are **industry
  context**, not proof NBIS must win.
- **Company optimistic framing labeled as framing:** the CEO's "sold out of capacity," "outstanding 2026," and
  "top AI cloud businesses globally" are quoted as **management framing**, and the GAAP profitability picture is
  correctly de-flattered (Q2 GAAP gain attributed to the Toloka revaluation, not operations; raw_extracts §C). The
  $7–9B ARR target is presented as a *target*, with the cover-graphic $4.3B discrepancy flagged rather than
  silently adopted.

## 6. Materials-Only Check (no decision / no outcome)

Token scan for decision/valuation content (REJECT/WATCH/STARTER/CORE, buy/sell, target_size, decision_card,
"fair value", "we should own"): **0 matches in the material pack.**
- `evidence_spine.md` §0 emits a neutral **module signal (0)** with a confidence read but **no portfolio action**,
  no size, no price target — that is module scaffolding for the future blind run, not a decision.
- `case_control.md` §3 records the decision question and explicitly **defers** it to the Runner; §7 separates Runner
  / Auditor / Scorer roles.
- No `decision_card`, no buy/sell verdict, no valuation judgment, no position size anywhere. Multiples/market cap
  appear only as **neutral arithmetic** (≈$21.1B = 251.8M × $83.71). No sealed-outcome / scorer file is present in
  the top-level folder (correct).

## 7. Decision

The material pack is **CLEAN** and clears the pre-decision gate. No load-bearing post-cutoff fact, no outcome-aware
language, no decision/thesis/size present; the abundant forward content is correctly admitted as as-of-knowable
management guidance. The brief's specific worry — that a non-blind self-run might have leaked the imminent Q4'25 /
FY2025 print, a 2026 financing, the ~$27B Meta expansion, the Goldman $205 raise, or a post-as-of price — is checked
and **none is present**. The blind Runner may proceed on these materials.

**Cleanliness concern (non-blocking):** the single thing to keep honest during the blind run is the **$4.3B vs
$7–9B ARR-target discrepancy** on the Q3 letter (cover graphic vs body). It is correctly flagged in the materials,
but because $4.3B ≈ the Sept-2025 cash raised, a careless reader could anchor to the wrong number. The Runner should
treat **$7–9B** as the stated CYE2026 ARR target and carry the ambiguity as model risk, not resolve it with any
post-as-of knowledge.
