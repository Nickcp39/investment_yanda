# Mega7 活体批次 — 运行计划 (PLAN)

**批次 ID**: `mega7_2026-06-19`
**as_of (冻结边沿)**: 2026-06-19
**pipeline_version**: `lean-6module-v1` · **weights_version**: `none`
**状态**: `PILOT PASS (NVDA+MSFT 双 CLEAN) — fan-out 剩 5 家 + 汇总进行中`
**主目录**: `D:\work\investment\financial-analysis-lab\companies\_mega7_2026-06-19\`

---

## 0. 目标

用**已固化、已回测验证(10-case 9 PASS/1 FAIL)** 的 `lean-6module-v1` pipeline,对当前 Mega7 七位做一次 **as_of=2026-06-19 的活体全档案研究**。每家公司跑成 GOOGL 那样的**完整 dossier**(11 stage,含 step 8 五灵魂 IC 面板),锁定一张 `decision_card.json`,过 `CHECKER.md` 完成度/质量门,最后汇总成**组合级排序 + 单因子集中度检查 + 自包含 HTML 看板**。

这是**活体运行,不是历史盲测**——今天就是冻结边沿,没有"未来"可泄漏,因此 `LOOKAHEAD_CHECKER.md` 那套**不适用**;改用 `CHECKER.md`(来源纪律 + 完整度 gate + 内部一致性 + 数据新鲜度)。

## 1. 七位 + 起步状态

| # | Ticker | 公司 | 起步状态 | 本批动作 |
|---|---|---|---|---|
| 1 | AAPL | Apple | 仅有 2016-05-12 历史盲测案;无现档案 | **全新全档案** (历史案做先验,数据用当前) |
| 2 | MSFT | Microsoft | 从未跑过 | **全新全档案** |
| 3 | GOOGL | Alphabet | `companies/googl/` 已有 v1/v2 全档案 (as_of ~2026-06-16, ~75%) | **刷新到 2026-06-19** (核对 3 天内无重大变化 + 重打版本戳;不重建) |
| 4 | AMZN | Amazon | 仅有 2023-02-03 历史盲测案;无现档案 | **全新全档案** |
| 5 | NVDA | Nvidia | 仅有 2023-05-25 历史盲测案;无现档案 | **全新全档案** |
| 6 | META | Meta | 仅有 2022-11-10 历史盲测案;无现档案 | **全新全档案** |
| 7 | TSLA | Tesla | 从未跑过 | **全新全档案** |

> 历史盲测案 (`backtests/framework_validation/cases/`) 仅作 thesis 先验/对照,**不得**把历史 as_of 的价格/事实当当前事实——所有载荷性事实必须重新取 2026-06-19 当下的一手来源。

## 2. 每家公司的产物(= GOOGL 标准 stage 清单)

输出落 `companies/<ticker>/`,文件集对齐 `companies/googl/`:

| Stage | Artifact | 模块映射 |
|---|---|---|
| 0 Idea Intake | (引用 `../../research_queue.md`) | — |
| 1 Triage | triage 短笺 | M2 入口 |
| 2 Plan | `step0_plan.md` (1 thesis gate + 证据块 + stop 条件) | — |
| 3 Evidence | `raw/`、`facts.md`、`claim_ledger.csv`、`source_register.md` | **M1 证据脊柱** |
| 4A Business | `business_model.md` | M2 |
| 4B Financial Quality | `financials/financial_quality.md` + `model/*.csv` | **M4 财务现实** |
| 4C Value Chain | `value_chain_map.md` | M3 |
| 4D Moat | `moat_map.md` | **M3 利润池/耐久** |
| 4E Bottleneck | `bottleneck_map.md` | M3 |
| 4F Operator | `operator_underwriting.md` (含创始人/核心团队 life-arc 评级) | M3 |
| 4G Inversion | `inversion_map.md` | **M5 反演/陷阱** |
| 4H Valuation | `valuation.md` + `model/scenario_model.csv` | **M6 定价/仓位** |
| 7 Audit | `audit.md` (completeness % + verdict ceiling) | 质量门 |
| 8 IC Panel | `ic_panel.md` (**五灵魂:段永平主审 + 巴菲特/芒格/Marks/Klarman**) | 决策 |
| 9 Decision Memo | `memo-v1.md` | 决策 |
| 10 Monitor | `monitor.md` (KPI + kill 三态 + 事件日历) | M6 监控 |
| — 锁定卡 | **`decision_card.json` + `decision_card.md`** (lean-6module 摘要,打版本戳) | M1-M6 汇总 |
| — 状态 | `research_status.md` (真实状态标签) + `completion_checker.md` | gate |
| — HTML | `brief-v1.html` (单页简报) | 呈现 |

**M1-M6 信号刻度**: `+2 强支持持有/加仓 / +1 弱支持 / 0 中性 / −1 警告 / −2 强警告或 veto 候选`。硬 veto 仅在 thesis 耐久性破裂或资产负债表无法存活时触发(M5),前瞻不确定性 = haircut 不是 veto。

## 3. 贯穿铁律(每家都查,CHECKER 强制)

- **来源纪律**: 每条载荷性 claim 带 (来源名 + 公开/取数日期 + link/path + tier);primary(10-K/10-Q/8-K/proxy/财报电话/官方统计) > 高质量 secondary > commentary(仅情绪) > 社媒/KOL(**仅线索,永不直接支撑 BUY**)。
- **verdict 上限 = 信息完整度**: `<40% INFO-GAP / 40-60% WATCH / 60-80% STARTER / >80% CORE`。完整度不够,verdict 必须被封顶。
- **size 跟已兑现信念走,不跟故事**(METHODOLOGY.md):Tracking 0.5-1% → Starter 3-5% → Confirmed 8-12% → Core 15-25%;天花板由**耐久性**定,不只由确认定;周期股封在 Confirmed 以下。
- **不造引语**: IC 面板里任何投资人引语必须有一手出处,否则标注为"释义/lens",不得伪造。
- **诚实标签**: 一遍并行跑出来现实目标是 `DECISION_DRAFT`(证据支撑的决策草案),**不得谎称 COMPLETE**;`research_status.md` 写真实状态标签;机械结论感觉不对时写 `runner_dissent`。

## 4. 执行三阶段

```
Phase 1 (并行) : 7 个 Runner agent,各建一家全 dossier → 锁 decision_card.json
Phase 2 (并行) : 每家一个 Checker agent,过 CHECKER.md → checker_report.md (CLEAN/FIX + 状态标签 + ceiling 核验)
Phase 3 (汇总) : 组合 synthesis — 7 张卡横向排序、单因子集中度检查、mega7_dashboard.html
```

执行载体: **多-agent workflow**(runner → checker 逐家 pipeline,末端 barrier 汇总)。每个 Runner 吃同一份 `RUNNER_BRIEF.md`,保证 7 家走完全相同的 pipeline、可横向比。

## 5. 交付物(全路径)

- 每家: `D:\work\investment\financial-analysis-lab\companies\<ticker>\` 全 dossier + `decision_card.json/md` + `checker_report.md`
- 批次汇总: `D:\work\investment\financial-analysis-lab\companies\_mega7_2026-06-19\mega7_synthesis.md`
- HTML 看板: `D:\work\investment\financial-analysis-lab\companies\_mega7_2026-06-19\mega7_dashboard.html`(7 名字 × verdict/size/ceiling/binding-constraint,排序,集中度旗标)

## 6. 组合级单因子检查(METHODOLOGY §5)

Mega7 七名几乎全骑 **"AI capex + 流动性"** 同一因子。汇总阶段必须显式回答:*若 AI capex 周期回撤 / 流动性收紧,这七名会不会一起跌?* —— 一句话判断,不做协方差。已持有 BTC/GOOGL/NBIS 也都在这条因子上(见 METHODOLOGY §5),新名字应分散因子而非加倍。

## 7. 批次进度跟踪

| Ticker | Runner | Checker | 状态标签 | verdict | size | ceiling | 备注 |
|---|---|---|---|---|---|---|---|
| AAPL | ⬜ | ⬜ | — | — | — | — | |
| MSFT | ✅ | ✅ CLEAN | DECISION_DRAFT | STARTER | 3-5%/max~9% | STARTER | base 5y IRR +9.5%; 价格有正 MOS(FV~$436); binding=完整度(OpenAI/capex 缺口) |
| GOOGL | ⬜ | ⬜ | — | — | — | — | 刷新非重建 |
| AMZN | ⬜ | ⬜ | — | — | — | — | |
| NVDA | ✅ | ✅ CLEAN | DECISION_DRAFT | STARTER | 3-5%/max~12% | STARTER | base 5y IRR +13%; 价格友好; binding=run-rate 可持续性 |
| META | ⬜ | ⬜ | — | — | — | — | |
| TSLA | ⬜ | ⬜ | — | — | — | — | |

> 现实预期: 一遍并行跑到 `DECISION_DRAFT`/~70% 级(GOOGL 用整天并行才到 ~75%)。打磨到 `COMPLETE` 是逐名 follow-up,不在本批一遍内承诺。
