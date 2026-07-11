# NOVT Checker Report — mega7_2026-06-19 (ai_robotics batch, as_of 2026-07-10)

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT** (one full pipeline pass; NOT COMPLETE; completeness ~60%) — honest, matches research_status/audit/completion_checker.
verdict / size / ceiling: **new_money=WATCH (0%) / existing=HOLD / initial 0% / max 0%**; completeness ~60% → ceiling STARTER (60–80 band), price (no MOS) pulls to WATCH. ← 被完整度正确封顶: **是** (WATCH sits BELOW the STARTER ceiling — conservative, not exceeded).
数据新鲜度: **PASS** (freshness_check.json, exit_code 0, status==PASS). ← 无 PASS = 强制 FIX-NEEDED；此处有 PASS。
Gate 勾选: A✓ / B✓ / C⚠(Stage 7 operator PARTIAL, O3 OPEN — disclosed, caps completeness not a gate fail) / D⚠(owner-earnings bridge approximate O4, disclosed) / E✓ / F✓

## Freshness verification (§4 MECHANICAL gate)
- freshness_check.json present, `status=="PASS"`, `exit_code:0`, `pipeline_version:lean-6module-v1.1`, `validator_version:verify_freshness-v1`.
- Price $156.65 cross-checked by 3 independent sources (yahoo / stockanalysis / websearch) **to the cent**, max pairwise delta 0.0%. Validator re-fetched Yahoo = 156.6499… ≈ 156.65.
- Tripwires T1–T5 PASS (52wk band containment, low/high hug, mkt-cap identity, distance-from-high reconciliation, single-value-of-truth). **T6 = WARN only** (guidance source 2026-05-14 is 57d < as_of, >45d threshold) — a WARN, not a failure; overall gate remains PASS. Acceptable but noted below.
- Independent Checker re-fetch of live Yahoo was **blocked in this sandbox (no outbound network / future-dated)**; I therefore spot-**recomputed all price-derived numbers** instead, and every one ties: 37.76M×$156.65=**$5.915B** ✓, adj P/E **47.6x** ✓, FCF yield **0.91%** ✓, −8.8% off high ✓, +59.4% off low ✓. GAAP FY25-implied P/E 106.6x vs card "~107–111 LIVE" — reconciled (LIVE stockanalysis uses TTM-through-Q1'26 EPS, not FY25). No 45%-style INC-001 mispricing signature.

## Stamp & consistency
- decision_card.json/.md both stamped **lean-6module-v1.1 / weights none / run_date 2026-07-10**. ✓
- as_of_price **$156.65** identical across facts / valuation / decision_card.{json,md} / freshness.json / audit. Numbers tie out.
- Share-count spread (35.68M basic / 37.76M / 38.7M diluted) explicitly reconciled to Nov-2025 TEU dilution; mcap uses 37.76M. ✓

## Batch THESIS honesty check (the point of this batch)
- **robotics_revenue_pct**: ~15–25% "robotics-linked" (industrial R&A ~15–20% + a surgical-components slice), embodied-AI/humanoid **<1–2%**. Explicitly flagged **ESTIMATE / OPEN (O1)** — company discloses NO discrete robotics line; % built from disclosed growth-driver deltas (S007) + ATI franchise (S008). NOT hand-waved, honestly labeled as an estimate. ✓
- **demand REAL-vs-ANTICIPATION**: **MIXED**, evidence-backed. Industrial robotics = real cash but single-digit (Q1'26 R&A **rev +7%**, bookings **+50%**, AET book-to-bill 1.15 [S003]) with an honest **pull-forward caveat** (+37% total bookings includes full-year orders placed in Q1). Humanoid/embodied-AI = **anticipation** (Holoscan "prototype phase," meaningful 2027 per mgmt [S003]). No "demand-exploded-into-cash" NVDA moment. ✓
- **CAPITAL_CYCLE lens on the robotics segment**: applied (applicable=partial). Humanoid slice = **EARLY-ANTICIPATION** (visible/consensus/capital-attracting → naive-guard, don't pay up); industrial base = mid-cycle recovery; supply_barrier med-high for incumbent niche, low for the humanoid land-grab. ✓
- **real_bottleneck**: **PARTIAL** — real falsifiable moat (44% GM, vitality 27%, only servo-drive in NVIDIA Holoscan safety lab, multi-year qualification switching cost) **but component-level, not an NVDA-class chokepoint** ("a niche, not the toll bridge"); humanoid piece = concept/option today. Justified. ✓
- **option-value vs core-value split**: done (thesis §e) — price overwhelmingly buys the medical-53%/industrial-47% precision-components compounder; humanoid is a small embedded call; buying NOVT *for* humanoid = overpaying for a <2% pre-revenue sliver at 47x. ✓

## Source discipline
- No naked claims — every load-bearing figure carries a source_id or an explicit OPEN. KOL video S010 quarantined to SENTIMENT ("lead only, never evidence"), never supports the verdict. EDGAR 403 disclosed; faithful relays (S002/S007/StockTitan) used with dates+tiers. ✓

## 伪造引语/失配数字
- **None fabricated.** ic_panel header pre-labels ALL five investor views as 释义/lens (无一手出处不造引号). Numbers all reconcile (recomputed above).
- SOFT nit (non-blocking): despite the "no fabricated quote marks" disclaimer, the panel wraps famous aphorisms in quotation marks (Buffett "Wonderful business, but not at this price."; Klarman "No margin of safety = no purchase."). These are generic, attributable-to-known-philosophy paraphrases covered by the blanket 释义 label — compliant, but tidier to drop the quote marks or add "(释义)" inline.

## FIX 清单 (non-blocking — ruling stays CLEAN)
1. ic_panel.md — drop quotation marks on the paraphrased aphorisms or inline-tag them 释义 (cosmetic; blanket disclaimer already covers).
2. freshness T6 WARN — confirm Q1'26 call (2026-05-14) is still the latest authoritative guidance event before any size change (57d old; no Q2 print yet — expected, fine for now).
3. To move DECISION_DRAFT→COMPLETE (not required for WATCH): close O1 (independent robotics-revenue triangulation), O3 (proxy/operator), O2 (10-K line items/10-yr series), O4 (owner-earnings bridge).

## 一句话
诚实、内洽、不吹的一轮:价格/规模三源到分、机器人叙事被如实降级为"真但单位数的工业件 + <2% 人形期权、非 NVDA 收费站",verdict 被完整度与价格双重正确封到 WATCH,新鲜度机械门 PASS —— 可信到 DECISION_DRAFT/~60% 该有的程度,CLEAN。
