# GOOGL Refresh Note — as_of 2026-06-19

**Type**: LIGHT REFRESH (not a rebuild) of the existing v1/v2 dossier (as_of ~2026-06-16).
**Pipeline**: lean-6module-v1 · weights none · run_date 2026-06-19.
**Scope**: verify the 3-day delta (2026-06-16 → 2026-06-19), then produce/re-stamp `decision_card.json` + `decision_card.md`. The 40-file dossier is fresher than a one-pass rebuild and was left as-is.

## 1. Current price (last daily close ≤ as_of)
- **$368.03** — 2026-06-18 close (2026-06-19 intraday not used as freeze edge). Source: Yahoo chart API.
- Market cap ~**$4.46T** (12,116M diluted shares × $368.03; buybacks paused so share count is rising 12,088M → 12,116M).
- Cross-anchor unchanged: Berkshire June-2026 private placement priced A $351.81 / C $348.20 (~5% below market).

## 2. 3-day delta findings (06-16 → 06-18, the trading days inside the window)
| Date | Close |
|---|---:|
| 2026-06-16 | $373.25 |
| 2026-06-17 | $363.79 |
| 2026-06-18 | $368.03 |

- **Price**: 06-16 close $373.25 → 06-18 close $368.03 = **−1.4%**. Noise. Still ~69x base owner earnings, firmly in the avoid zone (>~$300). No move toward the ~$113 base anchor or even the ~$134 8%-threshold.
- **8-K / filings**: none new in the window. The most recent material filings (June 1–5: $80B+ / upsized $84.75B equity raise + Berkshire $10B private placement; depositary-shares offering closed June 5) were already in the v1/v2 dossier and `valuation.md`.
- **DOJ adtech remedy**: no ruling. Structural-remedy phase still pending (K-D stays yellow).
- **Earnings**: none. Q2 2026 report still expected ~late July 2026 (next major catalyst).
- **Other**: one C/D-tier talent item — Gemini engineer (Shazeer) moving to OpenAI, shares dipped near $362 mid-window. This is already covered by `monitor.md` supplementary watch ("DeepMind/Gemini 核心人才是否成批离职… C/D 级，仅线索"); a single departure is not structural and does not change the moat read.

## 3. Does the verdict hold?
**YES — material change: NO.** Verdict, size, ceiling, and buy-below all unchanged from memo-v1:
- new_money **WATCH** · existing **HOLD** · personal **0%** size · ceiling **WATCH**.
- binding_constraint unchanged = **price has no margin of safety** (base 10y IRR −3.0%, bull only +5.2%, both <8% hurdle; K-E is the active red constraint).
- buy_below **~$113** (base 10% anchor); reopen-panel ladder $134 / 113 / 95 / 48 unchanged.
- status label kept honest at **~75% / DECISION_DRAFT** (not COMPLETE) — the OPEN items (maintenance-vs-growth capex split, only-3-year filed series) that capped the ceiling are still open.

## 4. What was re-stamped vs left as-is
- **Re-stamped / produced this refresh**: `decision_card.json` + `decision_card.md` in the canonical lean-6module schema (matches `companies/nvda/`), stamped pipeline_version=lean-6module-v1, weights_version=none, run_date=2026-06-19, as_of=2026-06-19, as_of_price=$368.03, market cap ~$4.46T. Six module signals (M1 +1 / M2 +2 / M3 +1 / M4 −1 / M5 −1 / M6 −2) + runner_dissent derived directly from memo-v1.md and consistent with it. This refresh note.
- **Left as-is (still fresh, ~2026-06-16)**: the full dossier — `research_status.md`, `memo-v1.md`, `valuation.md`, `monitor.md`, `financials/`, `model/*.csv`, the 8 module maps, `ic_panel.md`, `audit.md`, `brief-v1.html`, `facts.md`, `claim_ledger.csv`, `source_register.md`, `raw/`. No re-run needed; the 3-day delta did not invalidate any of them.

*If Q2 2026 earnings or a DOJ adtech structural-remedy ruling lands, that is a re-open trigger (back to IC panel + memo v2), not a light refresh.*
