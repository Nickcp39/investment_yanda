# Material Pack Audit (INDEPENDENT LOOKAHEAD_CHECKER) — SNDK 2025-06-16

Spec: [backtests/framework_validation/LOOKAHEAD_CHECKER.md](../../LOOKAHEAD_CHECKER.md). This is a MATERIAL-PACK audit (collector-only gate): the top-level pack must contain NO decision / verdict / thesis / valuation judgment / position size, and NO information dated after the as-of (**2025-06-16**).

最后更新: 2026-06-19

> **Independence note (the whole point of this gate, per `LOOKAHEAD_CHECKER.md`).** The original SNDK material/decision was a **NON-BLIND v0 self-run** (the orchestrator that collected it also decided it; `pipeline_version: lean_six_module_v0`, see `case_control.md` §1 and `VERSIONS.md`). That self-run is archived in `_v0/` and was **NOT read** for this audit or this v1 case. This audit re-derives the as-of integrity of the **top-level** material pack independently, with fresh web verification of the highest-risk and most-recent rows. Because the source pack was assembled by a non-blind hand, it is checked **hard**.

## 0. Audit Verdict

- **Verdict: CLEAN (top-level material pack).**
- As-of date (from `case_control.md` §2): **2025-06-16**. As-of price-of-record: **$44.21** close, ~$6.41B equity value on 145M shares.
- **0 load-bearing post-cutoff facts.** No outcome-aware language, and no decision / thesis / valuation judgment / position size in any of the four top-level material files. The pack is materially clean and test-ready for a blind Runner.
- Files audited (top-level only):
  - `case_control.md`
  - `sources_used.csv`
  - `raw_extracts.md`
  - `evidence_spine.md`
- **`_v0/` archive was NOT opened** (per the run instruction; the prior non-blind self-run must not contaminate this v1 pass). `operator_background.md`, `decision_card.*`, and this `material_audit.md` are v1 artifacts created in/after this audit, not part of the audited inbound pack.

### ⚠ Cleanliness concern raised (one — non-load-bearing to the material pack, but flag it LOUDLY)

- **The shared price data file `backtests/data/asof_2025_06_16_sndk_quotes.csv` contains a SECOND row dated 2026-06-16 with a post-as-of price ($1991.55), labeled "Current comparison anchor."** This is an **outcome anchor for the SCORER**, not a Runner input, and it lives in a shared data file rather than inside the material pack — but it is a live穿越 (look-ahead) hazard: a careless Runner reading that CSV could see the post-as-of price.
  - **Mitigation already in place / enforced here:** `sources_used.csv` row S009 cites this file specifically for "As-of price and market cap," and `raw_extracts.md` §S009 pins the as-of close to **$44.21** only. The blind Runner (this v1 run) used **only the 2025-06-16 row ($44.21)** and consciously excluded the 2026-06-16 row from all reasoning. The pack's own as-of price is correct.
  - **Recommendation (non-blocking):** the post-as-of row should be moved to a scorer-only file (e.g. an `outcome_*.csv`) so it cannot be seen by a blind Runner pointed at the price source. This does not void the pack; it is a hygiene fix for future runs.
- Beyond this, **no other cleanliness concern.** The material pack itself (the four top-level files) carries no post-cutoff fact and no decision.

## 1. Source Date Check (every `sources_used.csv` row: public_date ≤ 2025-06-16?)

| source_id | title | public_date | allowed? | issue / note |
|---|---|---|---|---|
| S001 | Nasdaq corporate-action alert (WDC/Sandisk spin-off) | 2025-02-24 | yes | trading mechanics; primary corporate action |
| S002 | Sandisk "celebrates Nasdaq listing" release | 2025-02-24 | yes | standalone setup; company release |
| S003 | WDC "completes planned separation" release | 2025-02-24 | yes | parent confirms Flash separated |
| S004 | Sandisk Q3 FY2025 results release | 2025-05-07 | yes | primary; Q3 financials + Q4 guide + CEO comments |
| S005 | Sandisk Form 10-Q (qtr ended 2025-03-28) | 2025-05-12 | yes | primary; balance sheet, Kioxia/Flash Ventures, risks |
| S006 | TrendForce "AI demand fuels enterprise SSD; 3Q25 NAND prices likely to rise" | 2025-05-26 | yes | **web-VERIFIED 2025-05-26** (see below); industry context |
| S007 | Sandisk **launches** secondary offering of WDC-owned shares | 2025-06-04 | yes | forced-seller setup; company release |
| S008 | Sandisk **prices** upsized secondary offering | 2025-06-06 | yes | **web-VERIFIED 2025-06-06** (see below); $38.50, 18.535M sh |
| S009 | Yahoo chart API SNDK 2025-06-16 close (local CSV) | 2025-06-16 | yes (with caveat) | = as-of; price-of-record **$44.21**. ⚠ the same CSV also holds a 2026-06-16 outcome row — see §0 concern; the **2025-06-16 row only** is used |
| S010 | Sandisk Form 10/A + information statement | 2025-01-31 | yes | pre-spin business/risk/pro-forma baseline |
| S011 | Sandisk S-1/A resale registration (WDC shares) | 2025-05-01 | yes | WDC 19.9% retained stake, resale overhang, debt-for-equity |
| S012 | Micron fiscal Q2 2025 results + prepared remarks | 2025-03-20 | yes | peer memory-cycle context |

All 12 rows have `public_date ≤ 2025-06-16`. **No source dated after the as-of.** The two rows closest to the cutoff (**S008** 2025-06-06; **S007** 2025-06-04) and the highest-narrative-risk row (**S006** TrendForce 2025-05-26) were independently web-confirmed.

**Web-verification detail (highest-risk / most-recent rows):**

| row | self-reported date | independent web check | verdict |
|---|---|---|---|
| **S008** Sandisk prices upsized secondary | 2025-06-06 | **Web-VERIFIED**: Sandisk IR + Nasdaq + Seeking Alpha all show **"Fri, 06/06/2025"**; 18,534,581 WDC-owned shares at **$38.50**; Sandisk receives no proceeds; pre-close debt-for-equity exchange via J.P. Morgan / BofA affiliates — exact match to `raw_extracts.md §S007/S008` | ✅ ≤ as-of |
| **S007** Sandisk launches secondary | 2025-06-04 | corroborated by the same IR/Investing.com cluster (launch precedes the 06-06 pricing); originally 17.0M shares proposed, upsized to 18.535M | ✅ ≤ as-of |
| **S006** TrendForce 3Q25 NAND note | 2025-05-26 | **Web-VERIFIED**: trendforce.com `/presscenter/news/20250526-12591.html` dated **2025-05-26**; content = *forecast* ("3Q25 NAND prices **likely to** rise," enterprise SSD "**likely to** shift toward undersupply," up to ~10% QoQ, low inventory) — a forward-looking as-of forecast, NOT a realized outcome | ✅ ≤ as-of |

> **URL-slug note (not a date problem):** the S007/S008 URLs in `sources_used.csv` contain the slug fragment `2025-05-06`, which does NOT match their `public_date` of 2025-06-04 / 2025-06-06. The web check confirms the **events and the press-release dates are 2025-06-04 (launch) and 2025-06-06 (pricing)**; the `-05-06-` in the slug is a CMS/slug artifact, not the publication date. The dates used in the pack are correct.

> **Web-search spillover I consciously DISCARDED (did not enter the pack or any reasoning):** the verification searches surfaced *post-as-of* outcome data — realized 3Q25 enterprise-SSD revenue (+16.5% QoQ), realized NAND price moves (+20–25%), December-2025 TrendForce notes, and a later large Sandisk secondary (Feb 2026). **None of this is in the material pack, none post-dates 2025-06-16 in the pack, and none was used.** The pack contains only the as-of *forecast*, which is correct.

## 2. Claim Traceability (load-bearing claims → allowed source_id)

| load-bearing claim | file(s) | source_id | traceable? |
|---|---|---|---|
| Standalone Nasdaq company Feb 2025; regular-way SNDK from 2025-02-24; 0.33333 ratio | case_control / raw_extracts / evidence_spine (C001–C002) | S001, S002, S003 | ✅ |
| Q3 FY2025 revenue $1.695B (−10% q/q, −1% y/y) | raw_extracts / evidence_spine (C003) | S004, S005 | ✅ |
| GAAP loss dominated by $1.83B goodwill impairment; non-GAAP EPS −$0.30; non-GAAP GM 22.7% | raw_extracts / evidence_spine (C004–C005) | S004 | ✅ |
| Q4 FY2025 guide: revenue $1.75–1.85B; non-GAAP GM 25.5–27.0% | raw_extracts / evidence_spine (C006) | S004 | ✅ |
| End-markets: Cloud $197M (+103% y/y, −21% q/q); Client $927M; Consumer $571M | raw_extracts / evidence_spine (C007) | S004 | ✅ |
| Cash $1.507B; LT debt $1.927B; total equity $9.161B; 145M shares (2025-03-28) | raw_extracts / evidence_spine (C008) | S005 | ✅ |
| Procures substantially all wafers from Kioxia Flash Ventures; ~$3.359B max loss exposure; ~50% fixed-cost / 49.9–50% capex obligation; $1.379B lease guarantees | raw_extracts / evidence_spine (C009) | S005 | ✅ |
| TrendForce AI/enterprise-SSD demand + possible Q3'25 undersupply / price rises | raw_extracts / evidence_spine (C010) | S006 | ✅ (web-verified) |
| WDC-owned shares sold in secondary at $38.50; Sandisk no proceeds | raw_extracts / evidence_spine (C011) | S007, S008 | ✅ (web-verified) |
| SNDK close $44.21 on 2025-06-16; ~$6.4B equity on 145M sh | case_control / raw_extracts / evidence_spine (C012) | S005, S009 | ✅ |
| Form 10/A pre-spin business/pro-forma/risk baseline | raw_extracts / evidence_spine (C013) | S010 | ✅ |
| WDC retained 19.9% (28,827,787 sh) registered for resale / debt exchange; 2025-04-30 close $32.11 | raw_extracts / evidence_spine (C014) | S011 | ✅ |
| Micron peer read: AI demand + NAND supply actions, but data-center NAND moderation + underutilization | raw_extracts / evidence_spine (C015) | S012 | ✅ |

No orphan / un-sourced load-bearing claim found.

## 3. Outcome-Aware Language Check

- Scanned all four pack files for hindsight phrasing ("later", "subsequently", "as we now know", "went on to", "rallied/collapsed to", "turned out") and for any post-as-of price.
- **None found in the material pack.** The pack consistently uses as-of framing. `evidence_spine.md` §0/§3 records the open questions (mid-cycle pause vs. new downturn; AI-demand strength; price-increase durability; Kioxia downside) **as unresolved**, never as a known outcome. The Q4 FY2025 *guide* is presented as company guidance, not as a realized result.
- The only post-as-of number anywhere in the case's orbit is the **2026-06-16 price row inside the shared `asof_2025_06_16_sndk_quotes.csv`** (the §0 concern) — it is the scorer's anchor and is **not referenced by any pack file's prose**; the pack's price-of-record is the 2025-06-16 $44.21 row only.

## 4. Post-Cutoff Fact Intrusion (per-case forbidden registry — each must be ABSENT)

`sndk_2025-06-16` is not in the LOOKAHEAD_CHECKER's printed registry table; the forbidden list is taken from `case_control.md` §5. Each checked ABSENT across the four pack files:

| forbidden item (case_control §5) | present in pack? |
|---|---|
| Fiscal Q4 2025 **results**, fiscal 2025 **10-K**, any later filings/releases | **ABSENT** (only the Q4 *guidance* given on 2025-05-07 appears — a pre-as-of forward statement, not a result) |
| Later Sandisk financial results, customer agreements, buybacks, index additions, analyst upgrades | **ABSENT** |
| Later NAND pricing (realized 3Q25+ NAND/enterprise-SSD price outcomes) | **ABSENT** (only the 2025-05-26 TrendForce *forecast* appears; realized 3Q25 data was found in web search and **excluded**) |
| Any SNDK stock performance after 2025-06-16 | **ABSENT from pack prose**; the 2026-06-16 price row in the shared CSV is the scorer anchor (§0) and is not used by the Runner |
| Any wording implying the runner already knows Sandisk became a large winner | **ABSENT** |

Additional traps specifically checked ABSENT: any reference to a post-as-of NAND up-cycle realization, any later WDC stake disposal beyond the 2025-06-06 secondary, any post-as-of Sandisk guidance raise — all ABSENT.

## 5. Evidence Misuse

| check | result |
|---|---|
| KOL / social / video used as core proof | **none** — no Twitter/YouTube/Reddit source anywhere in the pack |
| News / narrative used as lead vs. core proof | TrendForce (S006) and Micron (S012) are framed as **industry / peer context**, not as company-specific proof; `evidence_spine.md` C010/C015 mark them **medium** confidence and the §3 contradiction table explicitly uses them to argue *small sizing*, not a green light |
| Company optimistic framing stated as verified fact | **no** — management's "positioned to address AI opportunities," "price increases commenced," and "actions to reduce supply" (S002/S004) are presented as **management statements**; `evidence_spine.md` §2 "Sentiment / Narrative Only" explicitly says the AI-storage language "supports the thesis direction, but the core proof must come from supply discipline, pricing, margin, and enterprise SSD demand" |
| Peer print as industry context only | Micron (S012) used as a memory-cycle environment read, with its *bearish* side (data-center NAND moderation, underutilization) preserved — not cherry-picked |
| Goodwill-impairment / non-GAAP treatment | handled neutrally — the $1.83B impairment is flagged as the driver of the GAAP loss and the non-GAAP −$0.30 is shown alongside, without claiming either is "the real number"; left for the Runner's M4 to normalize |

No misuse.

## 6. Decision Absence (material-pack gate)

| check | result |
|---|---|
| Buy/sell verdict present in the four pack files | **NO** |
| `decision_card` present in the inbound pack | **NO** (the v1 `decision_card.*` are created by this run's Runner, after this audit; the prior v0 decision is sealed in `_v0/`, unread) |
| Thesis / valuation judgment / position size in the pack | **NO** — `evidence_spine.md` §2 frames the *question* ("priced like a weak cyclical while supply/demand is improving?") and explicitly says the evidence "supports an asymmetric setup, but **not** a high-confidence full position," which is a *neutral framing of the open question*, not a sized decision; the §4 Handoff hands the modules to a future Runner |
| Sealed outcome / scorer file in the audited top-level | **NO** |
| Decision question | recorded in `case_control.md` §3 and explicitly **deferred** (runner output separated from scorer output, §6) |

The decision is correctly deferred. No outcome is anywhere in the four top-level pack files.

---

## Decision

- **The top-level material pack is CLEAN and test-ready** for a blind Runner. All 12 sources are ≤ 2025-06-16 (the three highest-risk/most-recent web-verified), every load-bearing claim traces to an allowed source, no outcome-aware language, every forbidden-registry item ABSENT, no evidence misuse, no decision/thesis/size in the pack.
- **One cleanliness concern flagged loudly (non-load-bearing to the pack):** the shared price CSV `backtests/data/asof_2025_06_16_sndk_quotes.csv` carries a **post-as-of 2026-06-16 outcome price ($1991.55)** as a scorer anchor in the *same file* the Runner reads for the as-of price. It did not leak into the pack or this v1 run (the Runner used only the 2025-06-16 $44.21 row), but it should be relocated to a scorer-only file. **No fix is required to proceed; no LEAK.**
- **No `_v0/` material was read.** This audit and the v1 case are derived solely from the top-level as-of pack + framework docs.
