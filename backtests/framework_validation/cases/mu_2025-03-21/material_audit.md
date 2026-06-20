# Material Pack Lookahead Audit — MU 2025-03-21

Independent checker pass for the **`lean-6module-v1` re-run** of `mu_2025-03-21`. Different agent than the
original v0 collector; the prior v0 decision/analysis in `_v0/` was **NOT read** (contamination firewall).
As-of date: **2025-03-21**. Files audited (top-level only): `case_control.md`, `sources_used.csv`,
`raw_extracts.md`, `evidence_spine.md`.

> **Special caution flag (per re-run brief):** these materials were originally collected in a **NON-BLIND
> self-run** (the v0 pilot). A self-run is exactly where post-as-of facts leak in unnoticed, so every row
> and every load-bearing claim was checked against the as-of boundary with extra suspicion, and the
> single highest-risk row (S4, a 10-Q dated *exactly* on the as-of date) was scrutinized specifically.

## 0. Audit Verdict

- **Verdict: CLEAN-WITH-NOTES.**
- No load-bearing post-cutoff fact is present; no decision / thesis / valuation / position size is present
  in the top-level material pack. The pack is test-ready for the blind v1 Runner.
- The "NOTES" are **as-of-cleanliness / methodology** observations, none of which is a leak:
  1. **S4 (Q2 FY2025 10-Q) is dated 2025-03-21 — the as-of date itself** (boundary-touching, not over). It is
     used only to cross-confirm balance-sheet line items already in the S1 press release (2025-03-20). Admissible
     (`public_date ≤ as_of`), but flagged because boundary-day filings are the classic place a self-run drifts.
  2. **S5 price is self-described single-source** ("independent corroboration of the exact tick not separately
     obtained — treated as VERIFIED-single-source"). This checker obtained an **independent second source**
     (statmuse: 2025-03-21 close $94.37, down ~8% on the day) that **corroborates the magnitude** ($94.4–94.7,
     ~8% post-print drop). Minor ~$0.35 tick difference across vendors; non-load-bearing. Upgraded from
     single-source to two-source-corroborated.
  3. **No dated third-party DRAM/HBM price index** is in the pack (evidence_spine open-question #4 admits this).
     Not a leak — it is a *gap*, correctly disclosed. Industry-pricing direction rests on Micron's own ASP
     commentary, which the Runner must treat as a management lead, not independent evidence.
  4. The forward-looking content (FQ3-25 guidance; "record revenue in fiscal 2025"; 1-gamma DRAM launch) was
     all **stated in the 2025-03-20 release / as-of filings** — as-of-knowable forward guidance, NOT realized
     post-cutoff outcomes. Admissible, but must be quarantined by the Runner as management claim.

## 1. Source-Date Check

Every `sources_used.csv` row checked; the boundary-touching and price rows web-verified (do not trust the
CSV's self-reported date on a self-run).

| source_id | title (short) | public_date | ≤ as_of (2025-03-21)? | verified this pass | issue |
|---|---|---|---|---|---|
| S1 | Q2 FY2025 press release (8-K EX-99.1) | 2025-03-20 | yes | accession `0000723125-25-000006` consistent w/ EDGAR pattern; figures internally self-consistent | none |
| S2 | Q1 FY2025 press release (8-K EX-99.1) | 2024-12-18 | yes | date plausible (FQ1 ended 2024-11-28; ~3-wk lag standard) | none |
| S3 | FY2024 10-K (FY ended 2024-08-29) | 2024-10-04 | yes | standard ~5-wk post-FY filing lag | none |
| S4 | **Q2 FY2025 10-Q (qtr ended 2025-02-27)** | **2025-03-21** | **yes (= as_of)** | **boundary day — see Note 1; used only to cross-confirm S1 balance sheet** | **flagged, admissible** |
| S5 | Daily price history (stockanalysis.com) | 2025-03-21 | yes (= as_of) | **independent 2nd source obtained (statmuse $94.37 close, ~8% drop) — corroborates S5 $94.72** | none (upgraded to 2-source) |

All 5 rows dated on or before 2025-03-21. **0 source-date violations.** (Web search incidentally surfaced
stray POST-as-of MU items — later-2025 quarters, a much higher later price — these were **NOT opened and NOT
used**; their appearance is logged only as a discipline check. The current 2026 quote was glimpsed while
verifying the price endpoint and is **firewalled — it plays zero role in any module.**)

## 2. Claim Traceability

Every load-bearing claim in `raw_extracts.md` / `evidence_spine.md` traces to an allowed `source_id ≤ as_of`:

| key claim | source_id | traceable? |
|---|---|---|
| FQ2-25 rev $8,053M; GAAP GM 36.8% / non-GAAP 37.9%; GAAP EPS $1.41 / non-GAAP $1.56 | S1 (cross-conf S4) | yes |
| OCF $3.94B; net capex $3.085B; adj FCF $857M | S1 | yes |
| Cash+investments $9.60B; total debt ≈$14.36B; inventory $9,007M; equity $48,633M; ~1,123M dil sh | S1, S4 | yes |
| HBM revenue crossed $1B in the quarter; data center DRAM record; DC tripled YoY | S1 | yes (as mgmt claim) |
| DC revenue surpassed 50% of total; +400% YoY / +40% QoQ (FQ1) | S2 | yes (as mgmt claim) |
| FQ3-25 guide: rev $8.80B record; non-GAAP GM 36.5%; non-GAAP EPS $1.57 | S1 | yes (forward guidance) |
| Full-cycle: FY22 NI $8,687M → FY23 net LOSS −$5,833M (w/ $1,831M NRV write-down) → FY24 NI $778M | S3 | yes |
| Revenue $30,758M → $15,540M → $25,111M; DRAM ~70% / NAND ~29%; 4 BUs (CNBU 38% …) | S3 | yes |
| Cyclicality / underutilization / top-10 customers ~½ rev / CHIPS-Act capex language | S3 | yes |
| As-of close $94.72, down ~8%, mkt cap ≈$105.6B | S5 | yes (2-source) |

No dangling references; no claim resting on an out-of-window source. **PASS.**

## 3. Outcome-Aware Language Check

Independent scan of all four pack files for hindsight tokens ("later", "subsequently", "went on to", "as we
now know", "rallied/collapsed to", "in hindsight", "turned out"): **0 load-bearing matches.** The strings of
that kind appear only inside the **forbidden-evidence list in `case_control.md`** (correctly *naming* what is
excluded) and inside explicit **quarantine notes** ("Treated as a sentiment lead, not evidence"; "modeled
range, not a disclosed figure"). The FQ3 guidance and "record fiscal 2025" framing are forward statements
made on 2025-03-20, explicitly tagged as guidance — not realized outcomes. **No post-as-of price anywhere**
in the analysis (the only prices are the as-of close and trailing mid-March daily closes). **PASS.**

## 4. Post-Cutoff Fact Intrusion (per forbidden registry, `mu_2025-03-21` row)

| forbidden item | status | note |
|---|---|---|
| post-as-of HBM-ramp **outcome** | **ABSENT** | only the as-of fact "HBM crossed $1B in FQ2" + the FQ3 *guidance*; whether HBM ramps further is left as the open thesis question, not an outcome |
| the run / drawdown after 2025-03-21 | **ABSENT** | only as-of close $94.72 + trailing mid-March closes (S5); post-date move named only in the case_control forbidden list |
| Q3 FY2025+ results (≈ June 2025 and later) | **ABSENT** | raw_extracts §"Conflicts/notes" explicitly states FQ3/FQ4-FY25 & FY2026 filings surfaced in search were *deliberately excluded* |
| any 2025-H2 / 2026 development | **ABSENT** | no realized post-as-of development used; 2025 references are as-of forward guidance |

All registry items absent. **PASS.**

## 5. Evidence Misuse

- **No KOL / social / video sources** in this pack (the "Local notes / video / KOL" evidence row in
  case_control is allowed-in-principle but unused). Nothing to misuse.
- **Company optimistic framing correctly quarantined:** evidence_spine grades the HBM/data-center narrative
  and the ~8% drop as "Sentiment / narrative (lowest reliability — lead only)"; the management "record
  fiscal 2025" line is held as a claim, not verified fact. Management ASP-direction commentary is flagged
  (open-question #4) as the *only* pricing signal, not independent evidence.
- The single price series (S5) was self-flagged as single-source and is now independently corroborated
  (§1, §0 Note 2). **PASS.**

## 6. Materials-Only Check (no decision / no outcome in the pack)

Independent token scan for decision / valuation content (REJECT / WATCH / STARTER / CORE, buy / sell,
target_size, decision_card, "fair value", "we should own"): **0 matches in the top-level pack.** The four
files are neutral evidence assembly. Note `evidence_spine.md` carries an M1 **signal (+1) and confidence
(high)** and some interpretation (normalized-EPS range, HBM durability) — this is the M1 module's own
confidence read, **not** a buy/sell verdict, and is the expected content of `evidence_spine.md` under the
template. The sealed-outcome block in `case_control.md` §6 is **blank** (as required). No `decision_card`,
no sizing, no business verdict present. **PASS.**

> **Firewall note:** the prior v0 decision + analysis files live in `_v0/`. They were **NOT opened** during
> this audit or the subsequent v1 run. The v1 Runner reasons only from the four top-level evidence files
> + the newly built `operator_background.md`.

## 7. Decision

The pack is **CLEAN-WITH-NOTES** and clears the pre-decision gate. No load-bearing post-cutoff fact, no
outcome-aware phrasing, no decision present; forward guidance correctly admitted as as-of-knowable. The
notes (boundary-day 10-Q used only for cross-confirmation; price upgraded to two-source; no dated industry
price index = disclosed gap; forward guidance must stay quarantined as management claim) are methodology
flags, not leaks. **The blind v1 Runner may proceed.**

---

## 8. Addendum — `operator_background.md` added (this v1 run, 2026-06-19)

- **Added:** `operator_background.md` (the v0 case lacked an operator dossier) underwriting the 2–4 MU
  deciders — CEO Sanjay Mehrotra, CFO Mark Murphy, CBO Sumit Sadana, EVP Global Ops Manish Bhatia, and
  CTPO Scott DeBoer — with formation-first life-arcs, per-person dark-arcs, and a team-durability grade.
  Operator sources **O01–O06** appended to `sources_used.csv`.
- **As-of discipline:** every track-record claim is `public_date ≤ 2025-03-21`; formation facts are timeless
  but cited. Newest dated *event used* = the May-8-2017 Micron-CEO appointment + the as-of filings already
  in pack. Mehrotra's role is "CEO since 2017," not anything later.
- **Self-audit verdict: CLEAN.** No post-as-of MU outcome, no later price, no later HBM result; public bios /
  the Computer History Museum oral history are character-pattern / formation tier, never promoted to
  EVIDENCE-tier hard claims. Materials only — NO buy/sell verdict, NO valuation, NO size. The investment
  call is deferred to the blind decision pass.
