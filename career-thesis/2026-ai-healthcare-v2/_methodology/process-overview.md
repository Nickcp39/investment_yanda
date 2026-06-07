---
title: 5 步流程 overview
purpose: 整个研究 process 的 master 文档。每个 step 的 SPEC.md 是细化版，本文是总览。
created: 2026-05-17
---

# 5 步流程 Overview

## 设计原则

1. **每步回答 1 个 narrow question**，不是 "做这个 sector 的分析"
2. **每步的 output 是下一步的 input**，纯文件 handoff，不靠 conversation context
3. **pruning 在 step 1 一次性发生**，下游步骤不再 prune（pruning 决策应集中可审计）
4. **Nick fit 注入仅在 step 3**，前后不污染
5. **step 5 必须人做**，AI 只能产 input，不能产 final synthesis
6. **money lens 是 cross-cutting**，每步 SPEC 末尾都有一个 "money sanity check" 问题

## 5 步速览

| step | 1 个 narrow question | input | output (artifact) | thread 类型 |
|------|---------------------|-------|---|------------|
| 1 macro-sizing | "US + China AI healthcare 各子赛道当前营收 + 10y CAGR 各多少？" | scope + pruning rules | `step-1/work/segments-ranked.csv` (含 dropped 列) | research thread |
| 2 value-chains | "对每个 surviving 子赛道，钱从 sponsor 到 user 经过哪些 actor？" | `step-1/work/segments-ranked.csv` | `step-2/work/{segment}-valuechain.md` × N | research thread |
| 3 rent-capture + Nick fit | "每条 value chain 里，rent extraction 点在哪？Nick profile 在每个点的 unfair advantage 多少？" | step-2 outputs + `_personal/nick-profile.md` | `step-3/work/rent-points-ranked.csv` + `nick-fit-overlay.csv` | research thread |
| 4 positions | "每个高 fit rent point 对应什么具体公司 × 角色？" | step-3 outputs + 招聘市场数据 | `step-4/work/candidate-positions.csv` + `top-5-deep-dive/{position}.md` | research thread |
| 5 money-lens synthesis | "follow 这些 candidate 真的是 follow money 而不是 follow technology 吗？" | step-4 outputs | `step-5/final-synthesis.md` | **human only** |

## 每步的标准 SPEC 字段（每个 step-X/SPEC.md 都遵循这个格式）

```
1. Question     — 这一步回答的 1 个 narrow question
2. Input        — 必须 consume 的文件路径 list
3. Output       — 必须产出的文件路径 + schema/format
4. Method       — 用什么数据源、什么分析方法
5. Pruning      — 这一步保留 / 丢弃的规则
6. Validation   — 怎么判断 output 是 "good enough to feed downstream"
7. Anti-patterns— 这一步常见 over-reach
8. Money lens   — 这一步的 sanity check question
9. Effort hint  — 大致工作量估计
```

## handoff 设计

详见 `handoff-protocol.md`。要点：

- 每个 step 的 `work/` 目录开头放 `STATUS.md`，记录 draft / validated / blocked
- output 优先 CSV / 结构化表，叙述性 md 仅作辅助
- 下游 thread 启动时只读 `_methodology/`、自己的 `SPEC.md`、上游 `work/` 目录——**不读其他 step 的 work/**

## 整体时间预算

| step | 单 thread 估计 | 并行可压缩到 |
|------|---------------|-------------|
| 1 | 3-5 天 | 2 天（US/CN 分开两 thread）|
| 2 | 1-2 周（per surviving segment 1-2 天 × ~5-8 段）| 4-7 天（每段一 thread）|
| 3 | 3-5 天 | 不易并行（需要跨 chain 比较）|
| 4 | 1 周 | 可按 position 类型分 thread |
| 5 | 1-2 天（人工 synthesis）| 不能并行 |

总：**3-5 周 calendar time**，如果 parallel thread 多。

## 与 v1 的关系

v1 (`../2026-ai-healthcare/`) 产生的事实数据可能 useful：
- `data/companies.csv` — 70 美国 AI healthcare 公司事实库
- `data/china_companies.csv` — 25 中国对应公司事实库
- `01-us-landscape/` — 段级分析（事实摘要部分可用，结论部分忽略）

v2 不自动复用 v1 输出。**如果某个 step 需要 v1 数据，由该 thread 显式 copy 到 `shared/data/` 并标注来源**。
