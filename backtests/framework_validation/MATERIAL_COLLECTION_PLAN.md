# Material Collection Plan — As-of Backtest Cases

Batch: 2026-06-18 · Status doc (resumable). 本文件 = 这批 as-of 回测"材料收集"的执行计划 + 进度跟踪,保证大任务可断点续跑。

## Goal

Collect **as-of-CLEAN material packs (evidence only, NOT decisions)** for 5 new cases, so a blind decision test can be run later cleanly. The *decision* (decision_card etc.) is deliberately **deferred** to a separate future blind-Runner pass — this round only builds the materials.

## Scope — cases in this batch

| case_id | ticker | as-of | price date | anchor event |
|---|---|---|---|---|
| aapl_2016-05-12 | AAPL | 2016-05-12 | 2016-05-12 close | Q2 FY2016 (Apr 26 2016): first YoY revenue decline in 13 years; "is Apple ex-growth?" |
| intc_2024-08-02 | INTC | 2024-08-02 | 2024-08-02 close | Q2 2024 (Aug 1): big miss + ~15% layoffs + **dividend suspended** + weak guide; −26% day |
| dis_2021-11-11 | DIS | 2021-11-11 | 2021-11-11 close | Q4 FY2021 (Nov 10): Disney+ subscriber-growth miss; linear TV declining |
| pfe_2022-02-08 | PFE | 2022-02-08 | 2022-02-08 close | Q4/FY2021 (Feb 8): record COVID revenue; optically low P/E |
| pypl_2021-07-29 | PYPL | 2021-07-29 | 2021-07-29 close | Q2 2021 (Jul 28): near all-time high; eBay payment migration; rising competition |

(Already built: `sndk_2025-06-16`, `nbis_2026-01-01`. Legacy: `googl` 2024-06-16. See `cases/CASE_INDEX.md`.)

## Deliverable per case — the "material pack" (4 files in `cases/<case_id>/`)

| file | content |
|---|---|
| `case_control.md` | freeze: identity, as-of, price date, decision question, allowed/forbidden evidence (use `cases/sndk_2025-06-16/case_control.md` as format) |
| `sources_used.csv` | `source_id,title,public_date,url_or_path,type,used_for` — every row public_date ≤ as-of |
| `raw_extracts.md` | neutral excerpts/paraphrases from filings, releases, transcripts, dated news + the as-of price/market cap |
| `evidence_spine.md` | audited facts, open questions, source-quality / confidence grade |

**NOT in scope this round** (these are the future blind TEST): `thesis_mechanism.md`, `profit_pool_durability.md`, `financial_reality.md`, `inversion_trap_test.md`, `decision_card.md/.json`. Do not write a buy/sell verdict.

## Hard rules (every collector)

Self-apply `LOOKAHEAD_CHECKER.md` while collecting:
- **Only sources public ≤ the case's as-of date.** Neutral, as-of-framed extracts.
- **No outcome / no post-as-of facts / no later prices / no "later it…" language.**
- **No decision.** Materials only.
- **Do not read `companies/` folders** or any existing full-info analysis (contaminated).
- Min evidence mix (P1): 3–6 filings/releases · 1–3 transcripts · 1 price · 5–12 dated news · 1–4 peer/industry.

## Per-case capture spec (neutral — NO outcome)

- **AAPL 2016-05-12** — capture: FY2015 + Q2 FY2016 financials, iPhone unit trend, Services revenue line, cash pile + capital-return program, valuation (P/E), as-of close (near 2016 low). Decision Q (future test): *quality compounder mispriced as ex-growth, or a maturing-hardware value trap?* ⚠ as-of 5/12 **excludes** Berkshire's Q1'16 13F (filed ~5/16) — do not use it.
- **INTC 2024-08-02** — capture: Q2'24 results, Foundry segment losses, DCAI/CPU share trend vs AMD, balance sheet + capex, dividend suspension, as-of close (~post −26% day). Decision Q: *turnaround bottom, or structural-decline falling knife?*
- **DIS 2021-11-11** — capture: Disney+ subs + guidance, DTC operating losses, Parks recovery, Linear Networks trend, as-of close. Decision Q: *brand/IP compounder, or structural-decline trap (linear erosion + streaming losses)?*
- **PFE 2022-02-08** — capture: Comirnaty + Paxlovid revenue, 2022 COVID guidance, ex-COVID base, P/E, pipeline/patent-cliff context, as-of close. Decision Q: *cheap cash machine, or false-cheap peak-earnings trap?*
- **PYPL 2021-07-29** — capture: TPV, active accounts, take-rate, growth guide, eBay-migration disclosures, competition, valuation, as-of close (~ATH). Decision Q: *durable payments compounder, or expensive decelerating-growth de-rating trap?*

## Execution

5 **parallel background collector agents**, one per case. Each reads: its row here + `LOOKAHEAD_CHECKER.md` + `COMPANY_MATERIAL_TEMPLATE.md` + the SNDK case as a format example; then writes its 4-file pack.

## Downstream workflow

```
materials (this round)  ->  LOOKAHEAD_CHECKER per pack (CLEAN/LEAK)  ->  [future] blind Runner locks decision_card  ->  checker audit  ->  Scorer outcome_score
```

## Progress tracker (update as packs land)

| case | case_control | sources | raw_extracts | evidence_spine | checker | status |
|---|---|---|---|---|---|---|
| aapl_2016-05-12 | ☑ | ☑ | ☑ | ☑ | ☑ | test-ready (CLEAN-w-notes, fixed) |
| intc_2024-08-02 | ☑ | ☑ | ☑ | ☑ | ☑ | test-ready (CLEAN) |
| dis_2021-11-11 | ☑ | ☑ | ☑ | ☑ | ☑ | test-ready (CLEAN) |
| pfe_2022-02-08 | ☑ | ☑ | ☑ | ☑ | ☑ | test-ready (CLEAN) |
| pypl_2021-07-29 | ☑ | ☑ | ☑ | ☑ | ☑ | test-ready (CLEAN) |

## Completion criteria

All 5 packs present (4 files each) **and** each passes `LOOKAHEAD_CHECKER` = CLEAN (or CLEAN-WITH-NOTES). Then the batch is "test-ready."

## Resume protocol (if interrupted)

1. Re-read this tracker + list `cases/<case_id>/`.
2. Re-launch collectors **only for missing/incomplete packs**; do not re-collect completed ones.
3. Run the checker on any pack that hasn't been audited.
4. Mark each row done only after checker = CLEAN.

---

## Batch 2 (2026-06-17) — winners + INTC-2021 trap

Added to balance the set with the `planned` winners (META / AMZN / NVDA) and the INTC value-trap-near-top contrast to `intc_2024-08-02`. Same rules; materials only; self-applied `LOOKAHEAD_CHECKER`. 4 parallel collector agents.

| case | as-of close | mkt cap | sources | self-audit | status |
|---|---|---|---|---|---|
| meta_2022-11-10 | $111.00 ✓ | ~$294B | 11 | CLEAN-WITH-NOTES | test-ready |
| amzn_2023-02-03 | $103.39 ✓ | ~$1.06T | 15 | CLEAN-WITH-NOTES | test-ready |
| nvda_2023-05-25 | $379.80 ✓ (pre-split) | ~$938B | 14 | CLEAN-WITH-NOTES | test-ready |
| intc_2021-04-23 | $59.24 ✓ | ~$239B | 13 | CLEAN | test-ready |

All as-of closes VERIFIED; each pack = 5 files (4 material + `material_audit.md`). Notable look-ahead catches: NVDA Q1 FY24 10-Q (filed 2023-05-26, one day after as-of) excluded → numbers sourced from the 5/24 8-K; AMZN fenced a 2023-02-09 Motley Fool piece to narrative-only; INTC excluded the ~2021-05-09 Mercury Research share report.

Pre-blind-run TODO (not part of material collection): independent (separate-agent) look-ahead checker pass + add per-case rows to `LOOKAHEAD_CHECKER.md` forbidden registry (each `material_audit.md` provides a derived row).

---

## Operator / Founder background (added 2026-06-17) — now a required pack file

Founder/operator quality sets the **durability ceiling** (`METHODOLOGY.md`) and feeds M3. Every material pack now adds a **5th evidence file**:

- `operator_background.md` — follow `../../companies/_operator_underwriting_template.md`: People Map · Operator Scorecard (8 dims) · **Founder & Core Team Life-Arc** = the 2–4 people who actually decide the 10y outcome (not the org chart), **formation-first** (family / home / place-era / schooling / university / first job weighted most — the unchooseable, truest signal of formed values), a **required dark-arc / bear case for every person** (no hagiography), team cohesion + key-man + succession, → durability-ceiling grade 1–5.

As-of discipline: track record / tenure / capital-allocation / governance evidence must be public_date ≤ the case's as-of; **formation facts (childhood, schooling, early career) are timeless** — use them but cite. No post-as-of events/outcomes; evidence only; no unsupported psychological diagnosis. Min add: 3–6 dated operator sources (proxy / bios / interviews / shareholder letters / early-career records).

Backfill (2026-06-17): one collector per case writes `operator_background.md`. GOOGL is a full re-do (legacy stub → `googl_2024-06-14` proper pack incl. operator file).

| case | operator focus (verify) | status |
|---|---|---|
| googl_2024-06-14 | Pichai + Page/Brin (voting control) | full re-do |
| nvda_2023-05-25 | Jensen Huang (founder-CEO 1993–) | backfill |
| meta_2022-11-10 | Zuckerberg (founder control) | backfill |
| aapl_2016-05-12 | Cook (post-Jobs) | backfill |
| amzn_2023-02-03 | Jassy + Bezos | backfill |
| intc_2024-08-02 | Gelsinger (mid-turnaround) | backfill |
| intc_2021-04-23 | Gelsinger (brand-new CEO) | backfill |
| dis_2021-11-11 | Chapek + Iger | backfill |
| pfe_2022-02-08 | Bourla | backfill |
| pypl_2021-07-29 | Schulman | backfill |
