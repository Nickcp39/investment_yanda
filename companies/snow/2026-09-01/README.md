# SNOW · 2026-09-01

**Snowflake Inc.** — 本库首个 consumption 计费标的。

> **裁决：WATCH 0%，buy_below ~$173（距现价 −48%）。状态 DECISION_DRAFT，非 COMPLETE。**

## 先读这三个
1. [`decision_card.md`](decision_card.md) — 裁决与六模块
2. [`prediction_2026-09-02.md`](prediction_2026-09-02.md) — **本库第一张事前预测卡**
3. [`financial_quality.md`](financial_quality.md) — 三锚 owner earnings，本卡的核心

## ⚠️ 两条必须知道的限制
- **claim_ledger 37 条，verified = 0。** 全部行情源与 SEC.gov 在本环境
  EGRESS_BLOCKED，`verify_freshness.py` 跑不了（批次 PLAN §2 INC-004）。**本卡不得标 CLEAN。**
- **用户点名 SNOW 的前提「跌得很凶」对今天不成立。**
  2026 最大回撤 −56%（底 2026-04-10），但已收复并创新高，**YTD +50%**。

## 文件
| 文件 | 内容 |
|---|---|
| `step0_plan.md` | 研究计划 |
| `facts.md` / `claim_ledger.csv` / `source_register.md` | 证据层 |
| `raw/websearch_notes.md` | 原始抽取 |
| `business_model.md` | consumption 模型；**增长越快毛利越薄** |
| `moat_map.md` | BSX 式检验：只有「跨云中立」是结构性锁定 |
| `financial_quality.md` | **三锚：98x / 负数 / 310x** |
| `valuation.md` | 三情景 IRR + 价格阶梯 |
| `inversion_map.md` | 6 条 kill criteria |
| `decision_card.md` / `.json` | 卡 |
| `monitor.md` | 触发式监控 |
| `ic_panel.md` | 五灵魂：5 反对 0 支持 |
| `audit.md` | 自审 + 敏感性 |
| `completion_checker.md` | 完整度 45%，封顶 WATCH |
| `memo-v1.md` | IC memo |
