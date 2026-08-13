# Audit — IREN Full Run

as_of: 2026-08-12 · Stage I

```
Source coverage:            ⚠️ 差。SEC/IR/BusinessWire 全部 EGRESS_BLOCKED，
                            100% 二手聚合源
Key claims without source_id: 0
Conflicting numbers:        2 处
                            - 股价 $34.83 vs $39.75（日期不同，需行情源）
                            - 单 MW 定价 vs NBIS 差 2.4-5.4×（跨标的，未解）
Stale facts:                最新财报是 Q3 FY26（3月季），**已 5 个月**；
                            Q4 财报 15 天后发布
D1/C2 contamination:        已隔离 —— 分析师目标价 $81.73 标 SENTIMENT 未进 facts；
                            $21.1B 缺口为第三方估算，标 SENTIMENT
Math/model errors:          衍生值全部标注（29.8×、46%/月、26% 稀释、106× 市值/AI年化、
                            三情景股价）。⚠️ 三情景假设为自建，非公司指引
Missing primary sources:    Q3 FY26 8-K 全文、投资者演示、电话会转录、20-F
Management claims not verified: $4B ARR 目标、"85% 已签约"、3GW grid-connected 定义
Valuation assumptions too aggressive: 否 —— 反而刻意保守：
                            bear 情景假设股数 +72%，base 隐含 −17%
Risks not quantified:       Childress 改造的具体资本开支与工期未取得
Verdict ceiling:            **WATCH**
```

## Verdict ceiling

完整度估计 **~45%** → 落 40–60% 档 → **最高 WATCH**。

理由：一手源 0 条；3 项 blocking OPEN；**最新财报已 5 个月且 15 天后就出新的**。

## 自欺检查

- **有没有因为"跌了 60%"而看多？** —— 没有。M6 明确给 −1，base 情景隐含 −17%，
  且在卡上写死"跌幅不是估值"作为禁止理由
- **有没有被 $9.7B / $4B 这类大数字带跑？** —— 没有。全 pipeline 的核心动作
  就是把分母（$134.4M）挖出来，**这是开题阶段漏掉的**
- **有没有把 adj EBITDA 当盈利？** —— 没有。H2 明确指出 adj EBITDA 与 GAAP
  差 $307M/季，且折旧在此是真实经济成本
- **有没有因为"是 NBIS 同业"就套用 NBIS 的结论？** —— 没有。
  反而发现两者**融资模式是镜像**（客户出钱 vs 股东出钱），这是判别式不是相似点

## 结论
**审计通过，封顶 WATCH，不建仓。**
解除条件：8/27 财报 + 一手源 + 解决 3 项 blocking OPEN。
