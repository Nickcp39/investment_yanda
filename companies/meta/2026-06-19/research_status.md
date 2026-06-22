# META Research Status

最后更新: 2026-06-19（Mega7 活体批次一遍跑通）· as_of=2026-06-19 · pipeline_version=lean-6module-v1

Decision question: META 是否是十年后仍值得拥有的高质量生意？$577.22 现价是否有安全边际？爆炸式 AI capex（FY26 $125–145B）+ 回购暂停 + 加杠杆 + 创始人控制如何改变 owner earnings 与 binding constraint？

Current stage: **9 完成（Decision Memo）→ 10 Monitor 已生效**

**Verdict = WATCH**（新钱 initial 0% / buy-below ~$480 / max ~5% if entered）· status **DECISION_DRAFT** · completeness ~62% · ceiling = STARTER（完整度封顶），价格压实际 verdict 到 WATCH

> **诚实标签**: 这是**决策草案（DECISION_DRAFT）**，不是 COMPLETE。一遍并行跑现实目标。OPEN gate 见下（O4 capex ROI 是 blocking 胜负手）。

---

## Stage Checklist
| Stage | Artifact | Status |
|---|---|---|
| 0 Idea Intake | ../_mega7_2026-06-19/PLAN.md | ✅ |
| 1 Triage | step0_plan.md（thesis gate）| ✅ |
| 2 Plan | step0_plan.md | ✅ |
| 3 Evidence | raw/、facts.md、claim_ledger.csv、source_register.md（载荷数全 A1）| ✅ |
| 4A Business | business_model.md | ✅ |
| 4B Financial Quality | financials/financial_quality.md + model/*.csv | ⚠️ partial（10-K 逐行 O1、capex 拆分 OPEN）|
| 4C Value Chain | value_chain_map.md | ✅ |
| 4D Moat | moat_map.md | ✅ |
| 4E Bottleneck | bottleneck_map.md | ✅ |
| 4F Operator | operator_underwriting.md | ⚠️ partial（proxy 精确数 O3 未重取）|
| 4G Inversion | inversion_map.md | ✅ |
| 4H Valuation | valuation.md + model/scenario_model.csv | ⚠️ partial（base IRR 依赖 owner-earnings 锚=O4）|
| 7 Audit | audit.md（completeness 62%, ceiling STARTER, 价格压到 WATCH）| ✅ |
| 8 IC Panel | ic_panel.md（五票一致 WATCH + 段永平主审）| ✅ |
| 9 Decision Memo | memo-v1.md（WATCH, 0%, buy ~$480）| ✅ |
| 10 Monitor | monitor.md（KPI + kill/升级三态 + 事件日历）| ✅ |
| 锁定卡 | decision_card.json + decision_card.md（版本戳）| ✅ |
| HTML 简报 | brief-v1.html | ✅ |
| 状态 | research_status.md + completion_checker.md | ✅ |

---

## Final Verdict 摘要
**WATCH · 新钱 initial 0% / buy-below ~$480 / max ~5% if entered · 好生意 + 偏贵价格 + owner-earnings 锚未决。**

- META 广告引擎满血：Q1 2026 营收 +33%、单价 +12%、量 +19%、DAP 3.56B、FoA 分部利润率 ~48% [S001]——**生意质量不是问题**。
- 但 owner earnings 被翻 3.5 倍的 capex 吃掉：经营 NI ~$75B 年化 vs FCF ~$49.6B 年化，FCF yield 仅 3.4%；停回购（Q1 $0）、加杠杆（LT debt $58.7B）、净现金变薄至 ~$22.4B。
- 现价 $577.22 forward ~19.8x、**base 5y IRR +4%（< 8% 门槛）**、高出保守公允价 ~21% → **价格是 binding constraint**（与 NVDA 相反）。
- binding constraint = 价格 + capex ROI 不确定性（O4 胜负手——锚选 FCF vs 经营 NI 把 base 从 ~0% 拉到 ~+10%）。
- 控制人 ~61% 投票 / ~14% 经济 + 提案全否 + 停回购全押 capex = 重资本无约束期激励错配（within-band haircut，非自动降级；2022 同结构验证为正）。
- 完整度 ~62% 封 ceiling 在 STARTER；价格把现价实际 verdict 压到 WATCH。

## 升 verdict / 解封顶路径
①价格回撤到 ~$480（base 8% 门槛）→ STARTER-eligible；②capex ROI 量化兑现（营业利润随 capex 复利）→ 上修锚、base ~+10% → STARTER-eligible（解 blocking O4）；③10-K 逐行 + proxy 补齐 → 完整度 >80%，配合价格可评更高 verdict。

## 与 NVDA / GOOGL 的对照价值
同一 pipeline + 五灵魂 + 段永平主审: NVDA → STARTER（价格友好 + owner earnings 干净），META → WATCH（价格偏贵 + owner earnings 被 capex 吃 + 控制人激励错配），GOOGL → WATCH（同型）。差别全在客观价格/owner-earnings 质量，证明框架未被"广告满血 + AI"叙事或高市值带跑；META 与 GOOGL 同型（广告双寡头 + capex 黑洞 + 价格封顶），META base +4% 略好于 GOOGL base −3%。

## Next Review
Q2 2026 财报（~2026-07 下旬）: 营收兑现 $58–61B 指引、单价/量持续性、capex 是否再上调、回购是否恢复、capex 与 OI 的复利关系（O4 早期信号）。价格触发: ~$480 建仓评估、>~$640 no-chase。补齐: 10-K 逐行(O1) + RL 全年(O2) + proxy(O3) + capex ROI 量化(O4)。
