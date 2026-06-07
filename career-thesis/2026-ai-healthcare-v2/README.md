---
title: AI Healthcare 职业研究 v2
owner: Nick
created: 2026-05-17
status: design-phase — methodology spec only, no research executed yet
supersedes: ../2026-ai-healthcare/ (老版本，已 PAUSED，作为 reference 数据保留)
---

# AI Healthcare 职业研究 v2

## 这个目录是什么

v1（`../2026-ai-healthcare/`）从公司清单倒推 Nick fit，方向错了。
v2 从宏观钱流开始，**5 步流程**走到底，最后才注入 Nick fit。

设计 process 优先于跑 process。这个目录现在只有 **methodology + 文件夹骨架**，没有真研究输出。

## 关键设计决策（user 2026-05-17 锁定）

| 维度 | 决策 |
|------|------|
| scope | AI healthcare only（不是 all sectors）|
| geography | US + China parallel |
| horizon | 10 年 (2026 → 2036) |
| pruning | 10y CAGR < 15% OR 当前段 < $500M OR 10y 预测 < $5B → drop |
| 个人 fit 注入点 | step 3 (中场)，不在 step 1 前注入 |
| 协作模式 | Claude Code 多 thread / subagent，文件 handoff |

## 5 步流程（详情见 `_methodology/process-overview.md`）

```
step-1-macro-sizing          → US + China AI healthcare 子赛道大小 + 10y 增长
   ↓ pruning
step-2-value-chains           → 每个 surviving 子赛道画 sponsor→payer→service→product→infra→user
   ↓
step-3-rent-capture-and-fit   → 找 rent extraction 点 + 注入 Nick profile 评分
   ↓
step-4-positions              → 具体 position 候选（公司 × 角色）
   ↓
step-5-money-lens-check       → 人工最终 synthesis（不能外包给 AI）
```

## 文件夹结构

```
2026-ai-healthcare-v2/
├── README.md                                  ← 你正在读
├── _methodology/                              ← process 设计文档
│   ├── process-overview.md
│   ├── handoff-protocol.md
│   └── pruning-rules.md
├── _personal/
│   └── nick-profile.md                        ← step 3 注入的 canonical 档案
├── step-1-macro-sizing/
│   ├── SPEC.md                                ← input/output/method/validation
│   └── work/                                  ← 执行 thread 工作区
├── step-2-value-chains/
│   ├── SPEC.md
│   └── work/
├── step-3-rent-capture-and-fit/
│   ├── SPEC.md
│   └── work/
├── step-4-positions/
│   ├── SPEC.md
│   └── work/
├── step-5-money-lens-check/                   ← human-only
│   └── SPEC.md
└── shared/
    ├── data/                                  ← cross-step 引用数据（可从 v1 _archive 摘）
    └── sources/                               ← 全部 citation 集中
```

## 怎么用这个目录

### 如果你是 fresh thread 接手某个 step：
1. 读 `_methodology/process-overview.md` 理解整体
2. 读 `_methodology/handoff-protocol.md` 理解 thread 间约定
3. 读你要做的 `step-X/SPEC.md` 找具体任务
4. 读 `step-(X-1)/work/` 看上游输出
5. 在 `step-X/work/` 输出，按 SPEC 要求的格式
6. 不要跨步操作（做 step 2 时不要顺便做 step 3）

### 如果你是 Nick 自己：
1. 看 `_methodology/process-overview.md` 确认 process 没歪
2. 看每个 step 的 `work/` 看进度
3. step 5 必须你自己写——任何 AI 都不能写最终 synthesis

## 重要 anti-pattern

- ❌ 跨步骤一口气推 (跑完 step 1 直接出 step 4 结果)
- ❌ 把 Nick fit 注入到 step 1 之前 (会让 macro 分析被 profile 污染)
- ❌ 在 step 2/3 跑路里加 step 5 的 "所以你应该做 X" 结论
- ❌ 自创新 segment 或 capture point 名词 (复用 step 1/2 已经命名的)
- ❌ 复用 v1（`../2026-ai-healthcare/`）的 elevator-map 类结论作为 anchor (v1 已被否决)
