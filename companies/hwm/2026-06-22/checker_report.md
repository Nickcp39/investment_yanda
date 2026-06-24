# HWM Checker Report — mega7_2026-06-19

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT** (correctly labeled; not falsely COMPLETE)
verdict / size / ceiling: new-money **WATCH** / existing **HOLD** / max size **~10%** (below the 15–25% Core tier) — **是否被完整度正确封顶: 是 (correctly capped).** PRICE (M6 −2) is the binding constraint and caps below the ~62%-completeness STARTER ceiling; size correctly held below Core by cyclicality + key-man/succession (O5).
数据新鲜度: **PASS (freshness_check.json, exit 0)** — re-run independently this audit, reproduced exit 0.
Gate 勾选: A ✓ / B ✓ / C ✓ / D ✓ / E ✓(w/ OPEN) / F ✓
FIX 清单: **none blocking.** Advisory only (see below).
伪造引语/失配数字: **无 (none).**
一句话: Among the most trustworthy dossiers in this corpus — every load-bearing number reproduced both arithmetically and against live web sources, the freshness gate genuinely re-runs to exit 0, and the status/verdict wording is disciplined and honest; the only gaps are the openly-flagged secondary spares figure and the absence of direct EDGAR full-text, neither of which touches the price-driven verdict.

---

## 1. Data-freshness — MECHANICAL HARD GATE → PASS

- `freshness_check.json` exists, `status=="PASS"`, `exit_code==0`. **I re-ran `python scripts/verify_freshness.py --dossier companies/hwm/2026-06-22` independently this audit → STATUS: PASS (exit 0)** with identical tripwire output. The PASS is a live result, not a stale cached artifact.
- **Price $280.36 spot-verified:** the script's own independent Yahoo re-fetch returned $280.3599853515625 (rounds to $280.36); 3 independent sources (Yahoo / stockanalysis / Google Finance) agree within 1% (max pairwise delta 0.0%). My own web check (2026-06) shows HWM ~$278–279, i.e. the as_of price is **not** stale-low — the stock has if anything drifted *down* since the 06-22 settled close, so there is no INC-001-style under-pricing risk.
- **Market-cap identity verified:** 400.31M × $280.36 = $112.23B = card `as_of_market_cap` 112,229,000,000 (0.00% delta). EV $112.23B + net debt $2.065B = $114.30B = card. ✓
- **as_of date alignment verified:** as_of 2026-06-22 = last fully-settled NYSE close; run_date 2026-06-23 was an active, unsettled session (~$275.1 intraday) at run time. Pinning as_of to the prior settled close is correct and is explicitly documented in freshness.json + raw extracts (daily-close ladder 06-15…06-22 provided). ✓
- **Two T6 WARN (non-blocking):** litigation + guidance sources are 46d old (newest 2026-05-07, the Q1 print) vs the >45d threshold. These are WARN not FAIL; the script still exits 0. The Runner's note that next authoritative event is Q2 earnings (~late-Jul/early-Aug) is correct — there is no newer settled filing to miss. Acceptable.

## 2. Completeness Gates A–F

| Gate | Result | Note |
|---|---|---|
| **A. Scope & Definition** | ✓ | ticker/as_of(2026-06-22)/purpose/horizon frozen in step0_plan + decision_card; completion criteria written; status label not stale. |
| **B. Evidence (M1 spine)** | ✓ | source_register has every load-bearing source w/ date+link+tier; raw/ has neutral extracts; claim_ledger.csv carries tier + verification + source_id; facts.md segregates EVIDENCE/INTERPRETATION/SENTIMENT/OPEN; no naked claims (each is tagged or explicitly OPEN). KOL/aggregator content kept as leads only. |
| **C. 11-stage / 6-module** | ✓ | M1–M6 all emit {signal, confidence, finding, drivers}; Stage-8 IC panel present with all five souls voting; **all quotes lens-labeled (see §5).** |
| **D. Model & Math** | ✓ (with E-class OPEN) | rev/margin scenario model + 10y trend tied to evidence; implied expectations reverse-engineered from current price; 3 scenarios reconcile to assumptions; **all formulas independently reproduced (see §6).** The one soft spot — no fully normalized owner-earnings bridge (O3) — is openly flagged, not hidden. |
| **E. Open Questions** | ✓ | O1–O5 enumerated; each correctly classed blocking-vs-non-blocking. All are non-blocking on the *verdict* (PRICE binds); they cap *completeness*. Rationale given. |
| **F. Audit & Consistency** | ✓ | audit.md + research_status reflect true state; number reconciliation holds across all 23 files; decision_card schema complete with version stamp `lean-6module-v1.1 / none / 2026-06-23`. Reports the true (lower) status. |

**Unmet gates: none.** E carries the documented OPEN items (spares-secondary, no direct EDGAR) but these are correctly disclosed as completeness gaps, not verdict gaps.

## 3. Honest status label → CORRECT

Label is **DECISION_DRAFT** uniformly across decision_card(.json/.md), research_status, completion_checker, audit, brief. Grep for "COMPLETE/完成/fully complete/彻底" returns **only negated/aspirational uses** ("not COMPLETE", "what would raise to COMPLETE", "toward COMPLETE", "One pass => DECISION_DRAFT, not COMPLETE"). **No overclaim.** The ~62% completeness and all four open items the Runner flagged (spares secondary-sourced, no direct EDGAR full-text, no normalized owner-earnings bridge, Plant succession opaque) are stated plainly in research_status, audit, facts (O1–O5), and the M1 finding. Wording is, if anything, conservative.

## 4. Verdict-ceiling check → CORRECTLY CAPPED (yes)

- Completeness ~62% → completeness ceiling = STARTER (60–80% band). **But M6 PRICE (signal −2) caps harder** → new-money **WATCH**. This is the documented intended behavior ("for a name with no price margin of safety, M6 caps before completeness") and matches the GEV precedent. ✓
- Negative base-case 5y IRR (−1.6%/yr) and bull only +4.2%/yr (both fail an 8% hurdle) fully justify WATCH over STARTER. ✓
- **Size correctly held BELOW Core:** suggested max **~10%**, explicitly capped below the 15–25% Core tier on two independent grounds — (a) cyclical/aero build-rate tilt, (b) key-man/succession ceiling (O5, operator grade 4/5 deliberately not 5). Existing = HOLD, no-add, no-chase >$300, trim >$330. All consistent and defensible. ✓

## 5. Fabricated IC-panel quotes → NONE

ic_panel.md opens with an explicit "No fabricated quotes — each voice is a LENS… no primary quote is attributed" disclaimer and labels every soul "(lens)". The investor lines used (Buffett "price is what you pay, value is what you get"; Munger "great business at a fair price… not worth an infinite price"; Marks "the most dangerous thing is paying a price that assumes everything goes right"; Klarman margin-of-safety) are **well-documented general investing principles**, not invented HWM-specific quotes. The one company-specific quote that *is* used — CEO "engine spares needs continue to increase… effect could be felt from the Iranian conflict" — traces to the primary release/IR page (HWM-Q1-2026-PR / HOWMET) and is reproduced in raw extracts. **Clean.**

## 6. Number consistency → ALL RECONCILE (independently reproduced)

Recomputed from first principles (price $280.36, 400.31M sh, TTM EPS $4.31, FY26E adj EPS $4.94, FY26E EBITDA $3,060M, net debt $2,065M):

| Metric | Card | My recompute | Match |
|---|---|---|---|
| Market cap | ~$112.2B | $112.23B | ✓ |
| EV | ~$114.3B | $114.30B | ✓ |
| Trailing P/E | ~65x | 65.0x | ✓ |
| Forward P/E | ~57x | 56.8x | ✓ |
| EV/FY26E adj EBITDA | ~37x | 37.4x | ✓ |
| P/TTM FCF | ~68x | 67.8x | ✓ |
| Bear/Base/Bull IRR | −13.8 / −1.6 / +4.2 %/yr | −13.8 / −1.6 / +4.2 | ✓ exact |
| Buy-below STARTER / CORE | ~$174 / ~$139 | $176 / $140 | ✓ |
| Off-high / off-low | −3.5% / +65% | −3.5% / +65.5% | ✓ |
| Rev CAGR / EPS CAGR (21→25) | +13% / +58% | 13.5% / 58.4% | ✓ |

`as_of_price`, market cap, P/E, EV/EBITDA, and IRR are identical across decision_card / valuation / scenario_model / facts / claim_ledger / brief. A stray-price scan found only $280.36 (×32), the 52wk high $290.63, buyback avg $230.43, the 06-23 intraday $275.20, and the legitimate daily-close ladder — **no inconsistent or stale price anywhere.**

**Independent web verification of the load-bearing claims (all CONFIRM):**
- Q1 2026 revenue **+19% to $2.31B** — confirmed (StockTitan, PRNewswire, Howmet IR, SEC 8-K).
- Adj EBITDA **$740M, margin 32.0% (+320bps)** — confirmed. (Note: the dossier correctly distinguishes the 32.0% *margin* from the coincidental "+32% YoY" EBITDA *growth*; both ≈32 but the card uses them correctly.)
- End markets **commercial +20% / defense +10% / gas turbines +39%** — confirmed.
- FY2026 guidance **rev $9.58–9.73B, adj EPS $4.88–5.00** — confirmed.
- Trailing P/E **~64–65x**, price **~$278–280** — confirmed.
- **Spares ~$520M, +36%, Engine Products $1.253B @ 36.6% EBITDA, +29% YoY** — independently **confirmed via Q1 earnings-call coverage.** The Runner's choice to keep this as OPEN/secondary (O1) is honest and arguably over-cautious; it does not affect the verdict.

## Advisory (non-blocking, for the path to COMPLETE)

These do NOT change the CLEAN ruling — they are the same items the Runner already flagged for a future pass:
1. **O1 / facts.md + claim_ledger.csv** — the spares figure ($520M/+36%/23%) is now independently corroborated by Q1 call coverage; a future pass can promote it from "OPEN_secondary_only" to verified once cross-checked against the 10-Q full text.
2. **O2 / source_register.md** — a primary EDGAR 8-K exhibit for Q1 2026 exists (sec.gov/Archives/edgar/data/0000004281/…); direct full-text extraction would close O2 and lift evidence scoring.
3. **O3 / financial_quality.md** — a normalized owner-earnings bridge (strip the $93M Savannah gain explicitly) would tighten M4.
4. **O5 / operator_underwriting.md** — Plant succession/bench remains the sharpest qualitative open item; already correctly capping the size ceiling.

None of (1)–(4) is blocking; the PRICE-driven WATCH verdict is robust to all of them.
