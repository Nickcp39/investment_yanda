# TSLA Research Status

最后更新: 2026-06-19（Mega7 活体批次一遍跑通，冷启动）· as_of=2026-06-19 · pipeline_version=lean-6module-v1

Decision question: Tesla 是否是十年后仍值得拥有的高质量生意？$400.49 现价是否有安全边际？核心汽车收缩 + 利润率压缩、能源高增、robotaxi/Optimus/AI optionality 未兑现、Musk $1T 包稀释，如何改变 owner earnings 与耐久性？

Current stage: **9 完成（Decision Memo）→ 10 Monitor 已生效**

**Verdict = WATCH**（新钱 0%）· business_verdict **uncertain** · status **DECISION_DRAFT** · completeness ~55% · ceiling = WATCH（价格主导封顶 + 完整度 55%）

> **诚实标签**: 这是**决策草案（DECISION_DRAFT）**，不是 COMPLETE。一遍并行跑现实目标。**本案完整度（~55%）低于 NVDA（65%）**——SEC 10-Q/10-K 逐行（分部利润）WebFetch 403 未直取、robotaxi/Optimus 单位经济不可量化。OPEN gate 见下。

---

## Stage Checklist
| Stage | Artifact | Status |
|---|---|---|
| 0 Idea Intake | ../_mega7_2026-06-19/PLAN.md | ✅ |
| 1 Triage | step0_plan.md（thesis gate）| ✅ |
| 2 Plan | step0_plan.md | ✅ |
| 3 Evidence | raw/、facts.md、claim_ledger.csv、source_register.md（载荷数多源交叉；SEC 逐行 OPEN）| ⚠️ partial（SEC 403）|
| 4A Business | business_model.md | ✅ |
| 4B Financial Quality | financials/financial_quality.md + model/*.csv | ⚠️ partial（分部利润 OPEN）|
| 4C Value Chain | value_chain_map.md | ✅ |
| 4D Moat | moat_map.md | ✅ |
| 4E Bottleneck | bottleneck_map.md | ✅ |
| 4F Operator | operator_underwriting.md | ⚠️ partial（proxy 未取）|
| 4G Inversion | inversion_map.md | ✅ |
| 4H Valuation | valuation.md + model/scenario_model.csv | ✅ |
| 7 Audit | audit.md（completeness 55%, ceiling WATCH）| ✅ |
| 8 IC Panel | ic_panel.md（五票 REJECT + 段永平主审 WATCH）| ✅ |
| 9 Decision Memo | memo-v1.md（WATCH, 0%, buy <~$160）| ✅ |
| 10 Monitor | monitor.md（KPI + kill 三态 + 事件日历）| ✅ |
| 锁定卡 | decision_card.json + decision_card.md（版本戳）| ✅ |
| HTML 简报 | brief-v1.html | ✅ |
| 状态 | research_status.md + completion_checker.md | ✅ |

---

## Final Verdict 摘要
**WATCH · 新钱 0% · uncertain 生意 + 极端价格无 MOS + 故事驱动 + 核心利润池收缩。**

- Tesla 核心汽车在收缩（交付 −9%）、营业利润率连续三年腰斩（16.8%→4.6%）；能源储能 46.7GWh 翻倍（增长腿，利润率 OPEN）；robotaxi 已上线（小）、Optimus 产前（NARRATIVE）。
- DELIVERED owner earnings ~$5B（薄、被 capex 低谷美化），对 $1.41T 市值 → 起始 yield 0.35%、P/E 371x。
- 三情景 base 5y IRR **−17%**，**只有纯 NARRATIVE 的 moonshot 过 8% 门槛** → **价格对 DELIVERED 基本面无任何安全边际**。
- 资产负债表 fortress（净现金 $35.5B）→ **死不了，但死不了 ≠ 该买**。
- **binding constraint = 极端估值无 MOS（价格主导封顶）+ 核心利润池收缩 + Musk key-man/$1T 包 12% 稀释**（三重）。
- 非硬 veto（生意未破裂、前瞻不确定只 haircut）；价格 + 利润池收缩封 ceiling 在 WATCH。

## 升 verdict / 解封顶路径
①价格回到对 DELIVERED 基本面有 MOS 的区间（<~$200，向 52 周低 $288 以下并继续）；②robotaxi 披露正向单位经济 + 规模化 或 Optimus 真量产（NARRATIVE→DELIVERED）；③SEC 逐行（分部利润）+ proxy + robotaxi 单位经济补齐 → 完整度升（但价格无 MOS 仍封顶）。

## 与 NVDA 的对照价值
同一 pipeline + 同一五灵魂 + 同一段永平主审: NVDA → STARTER-开仓（价格友好、owner earnings 干净、瓶颈多季坐实），TSLA → WATCH-0%（价格极端 371x、owner earnings 薄且收缩、故事驱动）。差别全在客观事实（19x vs 371x、干净 OE vs 利润率塌、真瓶颈 vs narrative），证明框架既未被"robotaxi/AI 龙头"叙事或 $1.4T 市值带跑，也未对已上线 robotaxi/翻倍能源 over-veto（区别在价格不在故事）。

## Next Review
Q2 2026 财报（~2026-07）: 汽车利润率/交付方向（继续塌→封顶更紧/EXIT）、能源分部、robotaxi/FSD 运营、Optimus Fremont 是否真量产（NARRATIVE 验证）。价格触发: <~$200 才进入 STARTER 讨论。补齐: SEC 逐行（分部利润，O1 关键）+ proxy（O3）+ robotaxi 单位经济（O2）。
