# Materials Timeline-Accuracy Audit — 13 backtest cases (2026-06-21)

Content-level audit, **one layer deeper** than the mechanical freshness gate (`verify_freshness.py`).
The gate verifies the as_of **price** (nominal = raw × split) + every **source date ≤ as_of** (T7). This audit
verifies the **load-bearing FACTS themselves** — the anchor-quarter financials, guidance, and pivotal events the
verdict actually rests on — are (1) numerically **accurate** vs primary sources, (2) dated **≤ as_of**, and
(3) genuinely **as-of** (no post-as_of fact stated as known = content lookahead). 5 parallel read-only agents,
~80 load-bearing facts checked against primary/contemporaneous records (SEC EDGAR 403s automated fetches → numbers
corroborated via dated company releases + CNBC/Reuters/StatMuse/macrotrends).

## Result: 11/13 fully clean · 2 minor numerical slips (corrected) · 0 content lookahead

| case | anchor = latest ≤ as_of | content lookahead | numerical accuracy |
|---|---|---|---|
| nvda_2023-05-25 | ✅ Q1 FY24 | none | ✅ all exact |
| aapl_2016-05-12 | ✅ Q2 FY16 | none | ⚠ **corrected** (Services $6,056M→$5,991M) |
| googl_2024-06-14 | ✅ Q1'24 | none | ✅ all exact |
| meta_2022-11-10 | ✅ Q3'22 | none | ⚠ **corrected** ("first"→"second" YoY decline) |
| amzn_2023-02-03 | ✅ Q4'22 | none | ✅ all exact |
| intc_2021-04-23 | ✅ Q1'21 | none | ✅ all exact |
| intc_2024-08-02 | ✅ Q2'24 | none | ✅ all exact |
| pfe_2022-02-08 | ✅ Q4'21 | none | ✅ all exact |
| pypl_2021-07-29 | ✅ Q2'21 | none | ✅ all exact |
| dis_2021-11-11 | ✅ Q4 FY21 | none | ✅ all exact |
| mu_2025-03-21 | ✅ FQ2 FY25 | none | ✅ all exact |
| nbis_2026-01-01 | ✅ Q3'25 | none | ✅ all exact |
| sndk_2025-06-16 | ✅ Q3 FY25 | none | ✅ all exact |

## The 2 corrections (both as-of-knowable transcription/characterization errors — NOT lookahead, verdict-neutral)
1. **aapl_2016-05-12 — Services revenue $6,056M → $5,991M.** Root cause: `raw_extracts.md` transcribed the **Q1 FY16**
   column ($6,056M) into the Q2 FY16 anchor row; propagated to `evidence_spine.md` C005. True Q2 FY16 Services =
   $5,991M (+19.9% YoY). Thesis unaffected — still ~$6B, still +20%, still > Mac ($5,107M) and iPad ($4,413M).
   Fixed in `evidence_spine.md` + `raw_extracts.md`.
2. **meta_2022-11-10 — "first YoY revenue decline" → "second consecutive."** Q2'22 (-1%) was Meta's first-ever YoY
   revenue decline; Q3'22 (-4%) was the second. Fixed in `decision_card.md`, `evidence_spine.md` C001,
   `operator_background.md`. The load-bearing "first-ever **layoff**" framing was already correct.

## High-risk lookahead checks — all PASSED
- **googl_2024:** the DOJ search-monopoly ruling (issued **2024-08-05**, after as_of) is correctly treated as
  **PENDING** throughout — no ruling outcome used.
- **intc_2024:** dividend **suspension** correctly dated **2024-08-01 ≤ as_of 2024-08-02**; the post-as_of CEO exit
  (Gelsinger Dec'24) + CHIPS ~9.9% equity stake / Nvidia $5B (H2'25) are quarantined to the EXEMPT
  `outcome_score.md` / `counterfactual_catalyst_test.md` only.
- **amzn_2023:** the post-as_of source S013 (2023-02-09, already removed from `sources_used.csv`) drives **zero**
  load-bearing claims.
- **intc_2021:** the post-as_of Mercury Research server-share report (~2021-05) was correctly excluded.
- **Self-run cases (mu / nbis / sndk — highest leakage risk):** all clean. SNDK is the tell — a ~+500% FY2026
  outcome, yet framed cautiously ("uncertain", STARTER 3%) = no bullish outcome-leakage.

## Bottom line
The backtest materials are **timeline-accurate**: every case uses the correct anchor quarter, no post-as_of fact
leaks into any decision material, and load-bearing numbers tie to primary sources — with two now-corrected minor
slips that never touched a verdict. Combined with the mechanical gate (price + source-dates), all 13 cases are now
verified on the required timeline at both the data layer and the content layer.
