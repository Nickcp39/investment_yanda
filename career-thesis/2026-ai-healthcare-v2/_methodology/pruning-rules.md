---
title: Pruning Rules
purpose: 决定哪些子赛道在 step 1 后被 drop（不进 step 2-4）
created: 2026-05-17
version: v1 default
---

# Pruning Rules

## 触发时机

**只在 step 1 末尾执行一次。** 下游 step 不重新 prune（避免决策分散在多处不可审计）。

## 子赛道 keep / drop 规则

子赛道被 **drop** 如果满足 **任一**：

| 规则 | 阈值 | 理由 |
|------|------|------|
| 增长慢 | 10y forward CAGR < **15%** | healthcare AI overall ~30% CAGR。慢于平均一半 = 不在快电梯上 |
| 当前 market 太小 | 段当前营收 < **$500M** | 全段不到一家 unicorn 营收，10y 内不可能撑起 Nick 的 career platform |
| 10y forecast 太小 | 段 10y 预测营收 < **$5B** | 即使现在小但 10y 还不到 $5B，TAM 不够 |

**注意:** OR not AND。任一为真即 drop。

## 例外规则（escape valves）

下游 step 不能用，但 step 1 thread 可以 flag 例外，等 Nick 决策：

| 例外 | 说明 |
|------|------|
| 战略性小段 | 段虽小但是其他大段的 enabling layer（如 health data interop） |
| 早期 wildcard | 段当前几乎 0 营收但有 strong technical / regulatory catalyst（如 AI agent 在医院 ops） |
| Nick 已 commit 段 | 即使 fail 阈值，Nick 已有强 entry 网络的段（这种"个人 reason" 不应该参与 step 1 prune，但 flag 出来供后续讨论）|

例外段不进入 step 2 主线，但在 step 1 output 的 `segments-ranked.csv` 里 column `escape_valve_reason` 标记原因，让 Nick review 时可见。

## Pruning 不做的事

❌ **不按 Nick fit prune** — 即使 Nick profile 完全不 match 也保留（profile 注入是 step 3）
❌ **不按 geography prune** — US + China 都保留（geographic prune 是更后期的事）
❌ **不按"难进" prune** — 这是 entry path 描述问题，不是 segment 存活问题
❌ **不引入新的标准（如 moral / political / ESG）** — 只看钱

## 数据要求

step 1 thread 必须给每个段提供:
- `current_market_size_usd_m` (current annual revenue/spending in the segment)
- `forward_10y_cagr_pct` (10-year forward CAGR estimate)
- `forecast_2036_market_size_usd_b` (10-year forecast market size)
- `data_quality` (high / med / low / estimate-only)
- `sources` (URLs to primary data)

如果某个段数字找不到 high/med quality 数据：
- 标 `data_quality = low` 或 `estimate-only`
- 不要随便编。在 STATUS.md 标 `blocked: missing data for segment X`，等 Nick 决策

## 默认 segment list 起点

step 1 thread 可以从这些 candidate segment 开始，但不限于这个 list（可以加新段，必须给出加的理由）：

- S1 Clinical Documentation / AI Scribe
- S2 Clinical Decision Support / Medical LLM
- S3 Precision Medicine / Diagnostics
- S4 Drug Discovery AI
- S5 Medical Imaging AI
- S6 Revenue Cycle / Admin AI
- S7 Consumer / Virtual Care AI
- S8 Hospital Operations AI（v1 之前没单列，但 Menlo 报告里有）
- S9 Health Data Cloud / Agent Infrastructure
- S10 Physician Evidence Search
- S11 Patient Access / Navigation Agents

注：这 11 个直接来自用户另一个 AI thread 产出的 `D:\work\investment\career-thesis\2026-ai-healthcare\outputs\us_healthcare_industry_structure.md` 里的 D01-D11 分类。如果 step 1 thread 重命名 / 拆分 / 合并段，需要在 output 里明确 mapping。

## Rule 修订

如果 step 1 跑下来发现 default 阈值太严（survival 太少）或太松（太多 noise），在 STATUS.md 写 `blocked: pruning rules need revision`，等 Nick 调整本文件后再继续。**不要在 step 1 跑过程中私改阈值。**
