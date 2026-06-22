# MSFT Research Status

最后更新: 2026-06-19（cold-start,一遍并行跑通）

Decision question:
微软在 AI capex 大周期下是否仍是十年级别高质量复利机?$190B capex 恐慌 de-rate 后的当前价是否有足够安全边际可建仓?

Current stage: **9 完成（Decision Memo）→ 10 Monitor 已生效**

**真实状态标签: `DECISION_DRAFT`** · completeness **~65%** · ceiling = **STARTER**（完整度 + OpenAI/capex 信息缺口封顶,**非价格**)

**Verdict = STARTER**（new money;existing = ADD)· 建议初始 4% · 上限暂封 9%

> 诚实声明(铁律5 + research_completion_checker 语言规则):本轮**未达 COMPLETE**。一遍跑到证据支撑的决策草案。**不使用"完成/完整重跑完成/full research complete"语言。**

---

## Stage Checklist（cold-start 一遍跑通: 2026-06-19）

| Stage | Artifact | Status |
|---|---|---|
| 0 Idea Intake | ../../../research_queue.md (Mega7 批次) | ✅ |
| 1 Triage | (本批 RUNNER_BRIEF + PLAN) | ✅ |
| 2 Plan | step0_plan.md | ✅ |
| 3 Evidence | raw/extracts.md, facts.md, claim_ledger.csv（~30 A1/derived）, source_register.md | ✅ |
| 4A Business | business_model.md | ✅ |
| 4B Financial Quality | financials/financial_quality.md + model/*.csv | ✅ |
| 4C Value Chain | value_chain_map.md | ✅ |
| 4D Moat | moat_map.md | ✅ |
| 4E Bottleneck | bottleneck_map.md | ✅ |
| 4F Operator | operator_underwriting.md | ✅ |
| 4G Inversion | inversion_map.md | ✅ |
| 4H Valuation | valuation.md + model/scenario_model.csv | ✅ |
| 7 Audit | audit.md（completeness ~65%, ceiling STARTER） | ✅ |
| 8 IC Panel | ic_panel.md（五票 STARTER + 段永平主审） | ✅ |
| 9 Decision Memo | memo-v1.md（STARTER, 4%, buy-below ~$436, add ~$303） | ✅ |
| 10 Monitor | monitor.md（9 KPI + kill 五态 + 事件日历） | ✅ 已生效 |
| HTML 简报 | brief-v1.html | ✅ |
| 锁定卡 | decision_card.json + .md（版本戳） | ✅ locked |

---

## Final Verdict 摘要

**STARTER · 建议初始 4%(上限暂封 9%)· 好生意 + 这次价格也对,但研究没做完。**

- MSFT 是 exceptional 生意:FY25 营收 $281.7B、营业利润率 45.6%、净利 $101.8B;Q3 FY26 Azure +40%、Microsoft Cloud $54.5B、**RPO $627B(+99%)**、AI run-rate >$37B(+123%);净现金 ~$47B;一股一票。
- 现价 $379.40 ≈ 22.5× 净利、收益率 4.44%,**距 52 周高 −32%(capex 恐慌已 de-rate)**;base 公允价 ~$436 > 现价 → 正安全边际;三情景 IRR bear ~0%/base +9.5%/bull +15.2%。
- **与 GOOGL(同批,五票 WATCH)镜像对照**:同 AI-capex 因子,但 MSFT 价格 + 资产负债表 + 治理三方面更优 → STARTER 而非 WATCH。
- **唯一封顶 STARTER、堵 CORE 的是研究完整度(~65%)**:O3 OpenAI 经济学(Azure 增长隐藏依赖)+ O2 capex 维护/成长拆分(OE 区间 $73–125B)。

**上修 CORE 路径**:补 OpenAI 经济学(O3)+ capex ROI 框架(O2)+ 分部利润率(O4)→ 完整度上 80%。

## Kill Criteria（监控中,见 monitor.md）
K-A capex/OCF >70% 连两年(现 ~57% 🟡) · K-B Azure ≤+25% 连两季(现 +40% 🟢) · K-C OpenAI 经济学恶化(信息缺口 🟡) · K-D AI run-rate 塌(现 +123% 🟢) · K-E IRR <8%(>$436)(现 ~10% 🟢)

## 仍未过的 gate（why not COMPLETE）
- B 区:OpenAI 经济学(O3)、capex 拆分(O2)、分部利润率(O4)、8-K 2026-06 内容(O5)未一手提取。
- D 区:OE 区间宽未收敛(取决于 O2);base $112B 是假设。
- → 这些把 completeness 卡在 ~65%、verdict 封在 STARTER。

## Next Review
Q4 FY2026 财报(~2026-07 下旬):FY26 全年 capex 是否坐实 ~$190B、capex/OCF 全年、Azure FY27 指引、OpenAI 口径、维护/成长 capex 拆分。价格触发:>$436 no-chase、$303 加仓评 CORE。
