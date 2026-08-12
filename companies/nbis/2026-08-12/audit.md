# Audit — NBIS Q2'26 Rerun

as_of: 2026-08-12 · Stage I

## 审计清单

```
Source coverage:            ⚠️ 差。一手源(SEC EDGAR / nebius.com / businesswire)
                            全部被本环境出口代理拦截(EGRESS_BLOCKED)。
                            全部 Q2 claim 依赖二手聚合源。
Key claims without source_id: 0（每条 claim 都有 source_id 或标 OPEN）
Conflicting numbers:        ⚠️ 2 处未解
                            - C110 递延收入：$4,778.1M vs ~$5.98B，差约 $1.2B
                            - C111 净负债：名义净现金 +$0.6B vs "已转净负债"
Stale facts:                价格 ~$215-220 为二手源估计，未经行情源确认
D1/C2 contamination:        1 处已隔离 —— C124「现在就能卖光 2027 产能」
                            是管理层口头声明，已标 SENTIMENT，未进 facts
Math/model errors:          衍生值已标注（EBITDA margin 40.6%、成本占比 22.9%、
                            单季 FCF -$3.41B、capex/营收 ~7.0x、Trim zone 推导）
Missing primary sources:    Q2 6-K 全文、股东信、电话会转录 —— 均未取得
Management claims not verified: C124；以及"四笔 >$1B 合同"的对手方未披露
Valuation assumptions too aggressive: 否。base 目标沿用 07-10 的 $330-400，
                            本次未上修（尽管 ARR 指引 $7-9B 支持上修）——
                            保守处理，因源质量不足以支撑上修
Risks not quantified:       杠杆分支：非流动负债一季 $4.10B→$8.50B 已量化；
                            但利息覆盖、担保条款细节未取得
Verdict ceiling:            **WATCH**
```

## Verdict ceiling 判定

| 信息完整度 | 最高结论 |
|---|---|
| < 40% | INFO-GAP |
| **40%-60%** | **WATCH** ← 本卡落此档 |
| 60%-80% | STARTER |
| > 80% | CORE 可讨论 |

**完整度估计 ~50%（低于 07-10 的 ~70%）**，因为：
- 一手源 0 条（07-10 版有 20-F/6-K 原文支撑的历史 claim）
- 2 处数值冲突未解
- active MW 连续第三季 OPEN

**⚠️ 这意味着：本次 WATCH 裁决是"规则封顶"的结果，不是"分析后认为该 WATCH"。**
即使基本面读数偏正面（M3/M4 双升级），也不能据此上调裁决。

## 自欺检查

- **有没有被"大涨"带跑？** —— 检查通过。M3/M4 确实升级，但 M1 降级、
  M6 未改善、K-VAL 更紧。**净效果是完整度下降 + 价格更贵。**
- **有没有把管理层指引当事实？** —— C118/C119/C120/C124 全部标 `guidance`/`plan`，
  未进 facts 层。
- **有没有用涨价证伪 capital cycle？** —— 见 decision_card 的 capital_cycle 一节，
  已明确写出"涨价是周期的第一步而非反面"，caution 维持。
  **这是本次最容易犯的错误，已显式挡住。**

## 结论

**审计通过，但强制封顶 WATCH。**
解除条件：取得 6-K 一手源 + 解决 2 处冲突 + active MW 披露。
