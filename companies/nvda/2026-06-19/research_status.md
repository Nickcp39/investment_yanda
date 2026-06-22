# NVDA Research Status

最后更新: 2026-06-19（Mega7 活体批次一遍跑通）· as_of=2026-06-19 · pipeline_version=lean-6module-v1

Decision question: NVIDIA 是否是十年后仍值得拥有的高质量生意？$145.48 现价是否有安全边际？AI capex 周期、China 管制、custom-silicon 竞争如何改变 owner earnings？

Current stage: **9 完成（Decision Memo）→ 10 Monitor 已生效**

**Verdict = STARTER**（新钱 initial 3–5% / max ~12%）· status **DECISION_DRAFT** · completeness ~65% · ceiling = STARTER（完整度封顶）

> **诚实标签**: 这是**决策草案（DECISION_DRAFT）**，不是 COMPLETE。一遍并行跑现实目标。OPEN gate 见下。

---

## Stage Checklist
| Stage | Artifact | Status |
|---|---|---|
| 0 Idea Intake | ../_mega7_2026-06-19/PLAN.md | ✅ |
| 1 Triage | step0_plan.md（thesis gate）| ✅ |
| 2 Plan | step0_plan.md | ✅ |
| 3 Evidence | raw/、facts.md、claim_ledger.csv、source_register.md（载荷数全 A1/A2）| ✅ |
| 4A Business | business_model.md | ✅ |
| 4B Financial Quality | financials/financial_quality.md + model/*.csv | ⚠️ partial（10-K 逐行 OPEN）|
| 4C Value Chain | value_chain_map.md | ✅ |
| 4D Moat | moat_map.md | ✅ |
| 4E Bottleneck | bottleneck_map.md | ✅ |
| 4F Operator | operator_underwriting.md | ⚠️ partial（proxy 未重取）|
| 4G Inversion | inversion_map.md | ✅ |
| 4H Valuation | valuation.md + model/scenario_model.csv | ✅ |
| 7 Audit | audit.md（completeness 65%, ceiling STARTER）| ✅ |
| 8 IC Panel | ic_panel.md（五票 STARTER + 段永平主审）| ✅ |
| 9 Decision Memo | memo-v1.md（STARTER, 3–5%, buy ~$150）| ✅ |
| 10 Monitor | monitor.md（9 KPI + kill 三态 + 事件日历）| ✅ |
| 锁定卡 | decision_card.json + decision_card.md（版本戳）| ✅ |
| HTML 简报 | brief-v1.html | ✅ |
| 状态 | research_status.md + completion_checker.md | ✅ |

---

## Final Verdict 摘要
**STARTER · 新钱 initial 3–5% / max ~12% · 好生意 + 价格友好 + 前瞻不确定。**

- NVDA 是 AI 全栈算力瓶颈，多季一手坐实（Q1 FY27 营收 $81.6B/+85%、DC $75.2B/+92%、网络 +199%、Q2 指引 $91B）。
- owner earnings 异常干净（capex-light，FCF≈OE≈$182B run-rate）、净现金 ~$72B、低位回购 + 提股息——**无 GOOGL 式 capex 黑洞**。
- 现价 $145.48 forward ~19x、起始 OE yield 5.1%、base 5y IRR +13%（>8% 门槛）、贴 52 周低 → **价格不是卡点**（与 GOOGL 相反）。
- **binding constraint = run-rate 可持续性（pull-forward + custom-silicon 份额）**，按修好的规则控制 size、不否决（M5 无硬 veto）。
- 完整度 ~65% 封 ceiling 在 STARTER；周期性封 size 在 Confirmed 以下。

## 升 verdict / 解封顶路径
①custom-silicon 份额定量披露且 NVDA 守住（解 blocking O4）；②连续 2–3 季营收兑现指引（pull-forward 证伪）；③10-K 逐行 + proxy 补齐 → 完整度 >80% 可评 CORE candidate（仍受周期 size 封顶）。

## 与 GOOGL pilot 的对照价值
同一 pipeline + 同一五灵魂 + 同一段永平主审: GOOGL → WATCH-0%（价格封顶），NVDA → STARTER-开仓（完整度封顶、价格友好）。差别全在客观事实（估值起点 19x vs 69x P/OE、owner earnings 干净 vs capex 黑洞），证明框架未被"AI 龙头"叙事或高市值带跑。

## Next Review
Q2 FY27 财报（~2026-08 下旬，最重要节点）: 营收是否兑现 $91B 指引（pull-forward 证伪/坐实）、DC 环比/毛利率、网络持续性、custom-silicon 进展。价格触发: ~$110–130 加、>~$200 no-chase。补齐: 10-K 逐行 + proxy + custom-silicon 份额。
