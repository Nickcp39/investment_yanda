# Mega7 活体批次 — Runner 执行指令 (RUNNER_BRIEF)

每个 Runner agent 负责**一个 ticker**,据此把 `lean-6module-v1` pipeline 端到端跑成 `companies/<ticker>/` 全 dossier,as_of=2026-06-19。7 个 Runner 吃同一份本文件,保证一致可比。

---

## 你的角色

你是某一个 ticker 的 **Runner**。产出 P1 全 dossier + 锁定 `decision_card.json`。你**不**给自己打分(Checker 另做)。机械结论感觉不对就写 `runner_dissent`。

## 输入与取数

- **一手优先**: SEC EDGAR(10-K / 10-Q / 8-K / proxy)、官方财报与电话会 transcript、官方统计。用 WebSearch/WebFetch 取**当下(≤2026-06-19)最新**披露。
- **股价/市值**: 走 Yahoo chart API(repo 既定来源,Stooq 已失效)。
- **KOL/美股投资网/社媒**: 只作线索或情绪,**未经一手验证不得进 `facts.md`、永不直接支撑 BUY**。
- 若该 ticker 在 `backtests/framework_validation/cases/` 有历史盲测案:可读作 thesis 先验/对照,但**历史 as_of 的价格与事实不得当当前事实**,全部重新取当下来源。

## 必产文件(对齐 `companies/googl/`)

```
companies/<ticker>/
  research_status.md          ← 11-stage 勾选 + 真实状态标签 + Final Verdict 摘要
  step0_plan.md               ← 1 thesis gate + 证据块 + stop 条件
  source_register.md          ← 每来源: 名+日期+link/path+tier
  claim_ledger.csv            ← 每 claim: source_id, value, unit, as_of, tier, 验证状态, destination
  facts.md                    ← EVIDENCE / INTERPRETATION / SENTIMENT / OPEN / Contradictions
  raw/                        ← 一手摘录(按 block: 10-K/10-Q/proxy/13F/电话会)
  business_model.md           ← 一句话生意 + 营收引擎 + 10 年测试 + 质量记分卡
  financials/financial_quality.md + model/*.csv  ← 10 年趋势 + owner earnings 桥 + 三情景
  value_chain_map.md / moat_map.md / bottleneck_map.md
  operator_underwriting.md    ← 创始人/CEO/董事会 + 核心团队 life-arc 评级 + 激励
  inversion_map.md            ← 失败路径 + 永久减值 + kill 标准
  valuation.md + model/scenario_model.csv  ← MOS + 估值带 + 价格区间
  audit.md                    ← completeness % + verdict ceiling 规则
  ic_panel.md                 ← 五灵魂(段永平主审 + 巴菲特/芒格/Marks/Klarman)
  memo-v1.md                  ← 决策 memo
  monitor.md                  ← KPI + kill 三态 + 事件日历
  brief-v1.html               ← 自包含单页简报
  completion_checker.md       ← 公司级 A-F gate 勾选
  decision_card.json + decision_card.md   ← 锁定卡(见下 schema)
```

## 六模块映射 + 信号刻度

M1 证据脊柱(信心)· M2 主题/机制(语境+信念)· M3 利润池/耐久(信念,含 operator)· M4 财务现实(信念或警告)· M5 反演/陷阱(风险或 veto)· M6 定价/仓位/监控(价格+输出)。

`+2 强支持 / +1 弱支持 / 0 中性 / −1 警告 / −2 强警告或 veto 候选`。**硬 veto 仅在 thesis 耐久性破裂或资产负债表无法存活时触发**;前瞻不确定性 = haircut 不是 veto(这是修好的老病,别复发)。

## decision_card.json schema(必填,打版本戳)

```json
{
  "ticker": "", "as_of": "2026-06-19",
  "pipeline_version": "lean-6module-v1", "weights_version": "none", "run_date": "2026-06-19",
  "context_label": "",
  "as_of_price": 0, "as_of_market_cap": 0,
  "module_signals": [
    {"module": "M1 Evidence Spine", "role": "confidence", "signal": 0, "confidence": "low|med|high", "finding": "", "drivers": ["source_id"]}
    // M2..M6 同
  ],
  "business_verdict": "bad|uncertain|good|exceptional",
  "new_money_verdict": "REJECT|WATCH|STARTER|CORE",
  "existing_position_verdict": "EXIT|TRIM|HOLD|ADD",
  "suggested_initial_size_pct": 0, "suggested_max_size_pct": 0,
  "buy_below_price": 0, "starter_zone": "", "add_zone": "", "trim_or_no_chase_zone": "",
  "binding_constraint": "", "kill_criteria": [""], "runner_dissent": "",
  "sources_used": [{"source_id": "", "public_date": "", "url_or_path": ""}]
}
```

## 贯穿铁律

1. **来源纪律**: 每条载荷性 claim 带来源名+日期+link/path+tier;primary>secondary>commentary>社媒。
2. **verdict 上限 = 完整度**: `<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE`。完整度不够就封顶,别被"净利大涨"带跑。
3. **size 跟已兑现信念**: Tracking 0.5-1 / Starter 3-5 / Confirmed 8-12 / Core 15-25;天花板由耐久性(含 operator life-arc)定;周期股封在 Confirmed 以下。M6 只输出吸引力+不对称+stage+风险,**不设硬性 size 天花板**。
4. **不造引语**: IC 面板任何投资人引语必须有一手出处,否则标"释义/lens"。
5. **诚实**: 一遍跑现实目标 = `DECISION_DRAFT`;**禁谎称 COMPLETE**;`research_status.md` 写真实标签;不确定写 `runner_dissent`、写 OPEN。

## 完成自检(交卡前)

① 当前状态标签是什么?② 哪些 gate 还没过?③ 什么证据能升到 COMPLETE?④ 有没有 stale 文件标了不同状态?⑤ 措辞是否匹配真实状态?— 任一不清楚 = 未完成。
