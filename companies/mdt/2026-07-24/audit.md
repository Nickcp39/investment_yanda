# MDT Audit — REFRESH

Last updated: 2026-07-24 | pipeline: lean-6module-v1.1 | as_of: 2026-07-24 | prior: `../2026-07-05/audit.md`

---

## 1. Internal Consistency Checks (all PASS)

| # | Check | Result |
|---|---|---|
| 1 | as_of_price $83.21 identical across decision_card.json/md, facts.md, valuation.md, model/scenario_model.csv | PASS (T5 tripwire confirms) |
| 2 | Market cap = 1.28B × $83.21 = $106.51B vs card $106.509B | PASS (T3: 0.00%) |
| 3 | Net debt $18.74B (10-K: debt $27.96B − cash $9.22B) + $0.65B SPR = ~$19.4B | PASS |
| 4 | EV = $106.51B + $19.4B = $125.9B | PASS |
| 5 | EV/EBITDA = $125.9B / $11.60B est. = ~10.85x ≈ 10.9x | PASS |
| 6 | Forward P/E = $83.21 / $5.95 = 13.99x (matches screener) | PASS |
| 7 | 52wk position: +13.5% off low ($73.31), −21.7% off high ($106.33) | PASS (T2/T4) |
| 8 | Net signal M1(0)+M2(+1)+M3(+1)+M4(+1)+M5(+1)+M6(+1) = +5/0 | PASS |
| 9 | Prior +4/0 → new +5/0 (M5 0→+1) consistent across json/md/comparison | PASS |
| 10 | FY2026 non-GAAP EPS $5.53 lands inside the lowered $5.50-5.54 post-MiniMed guide | PASS |
| 11 | MiniMed IPO 28M × $20 = $560M; ~90.03% retained | PASS |
| 12 | Dividend yield $2.88 / $83.21 = 3.46% | PASS |
| 13 | D/E = $27.96B / $50.07B = 55.8% | PASS |
| 14 | FCF/NI = $5.426B / $4.801B = 1.13x | PASS |
| 15 | Litigation count (15 suits / 55 people) identical across facts/inversion/freshness/comparison | PASS |

## 2. Stale-Claim Check

| Claim class | Date | Freshness |
|---|---|---|
| Price / 52wk band / shares / mcap | 2026-07-24 (re-fetched) | FRESH — re-verified 2 ways at as_of |
| FY2026 actuals (revenue, EPS, FCF, segments) | 2026-06-03 | CURRENT — no new print until Q1 FY2027 (2026-09-01); carried forward, not stale |
| Balance sheet (net debt, equity) | 2026-04-24 (FY2026 10-K) | CURRENT — most recent filed |
| SPR completion | 2026-07-16 | FRESH (within window) |
| Touch Surgery Aide / Hugo AI | 2026-07-21 | FRESH (within window) |
| MiniMed IPO + deconsolidation | 2026-03-06 / 2026-03-25 | CURRENT (within window; deconsolidation ongoing) |
| MiniMed litigation count | 2026-06-08 (FY2026 10-K) | CURRENT |
| China VBP commentary | 2026-06-04 (Q4 call) | CURRENT (on-record; hard % still a gap — O2) |
| Guidance (FY2027) | 2026-06-03 | CURRENT but 50d old → freshness WARN (annual guide; next update 2026-09-01) — flagged, not a failure |
| S&P 'A' rating | 2024-08-23 | STALE (>18mo) — flagged O8, treated as most-recent-known, not current-confirmed |

## 3. Data-Integrity / Discipline Compliance

- **LIVE data re-fetched independently**: price via the repo Yahoo fetcher AND stockanalysis history — exact $83.21 match; freshness gate PASS (exit 0). No conflicting-price artifact this run.
- **≥2 sources on load-bearing numbers**: price (2), MiniMed IPO terms (3+), SPR (3), litigation count (10-K + tracker), Hugo AI (PR + transcript + trade), China (transcript + aggregator). Met.
- **Primary filings used where possible**: MDT newsroom PRs (A1), MiniMed S-1 (A1), FY2026 10-K + EDGAR metadata (A1), earnings-call transcript (A2). SEC 10-K document-body not read verbatim (bot-block) — flagged O5/O8.
- **KOL/analyst ratings = leads only**: BTIG/Evercore/TD Cowen/Jefferies targets are logged as SENTIMENT leads, NOT standalone thesis support; explicitly noted that targets were mostly TRIMMED (honest, not cherry-picked to the bullish side).
- **No fabrication**: Hugo revenue is stated as UNDISCLOSED (not estimated); the ~7% China figure is labeled FY2024-vintage (not presented as current); the "2,175 injuries" figure is explicitly corrected as FDA MAUDE reports vs the actual 15 lawsuits.
- **No fabricated quotes**: the ic_panel 5-soul reasonings are stylized synthesis in each investor's known framework/voice (a deliberate panel device), NOT presented as verbatim quotations from real individuals. The only quoted management language (CFO Piéton on including full-year Diabetes; CEO Martha on China) is sourced to the earnings-call transcript.
- **Honest signal discipline**: the one signal upgrade (M5 0→+1) is justified with specific evidence AND explicitly capped at +1 with the counter-risks (Hugo unresolved, TAVR/PFA competition) on the record — not an unqualified bullish drift.

## 4. Robustness-Rule Compliance

- SEC EDGAR document-body historically bot-blocked; did not retry-loop — used MDT's own A1 newsroom + the metadata API + a legal tracker quoting the 10-K. Consistent with the max-2-attempts rule.
- Price cross-check caught no anomaly; the 08-05 intraday ($85.50) was correctly treated as a later, different-date read, NOT as the as_of price.

## 5. Audit Verdict

**PASS.** The refresh is internally consistent (15/15 checks), freshness-gated (PASS), and discipline-compliant. The one upgrade (M5) is evidence-based and honestly bounded. Residual gaps (Hugo revenue, hard China %, SEC body read, China-robotics competitors) are explicitly registered, not papered over. The dossier honestly reports a MODEST STRENGTHENING that holds the STARTER verdict rather than manufacturing a bigger move than the evidence supports.
