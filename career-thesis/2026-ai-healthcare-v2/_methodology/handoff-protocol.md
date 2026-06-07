---
title: 多 thread handoff 协议
purpose: 让多个 Claude Code thread / subagent 并行工作时不互相覆盖、不互相依赖 conversation context
created: 2026-05-17
---

# Handoff Protocol

## 核心约定

1. **每个 step 是独立 unit**: thread A 跑 step 1 后退出 conversation；thread B 启动 step 2 时只读文件，不读 thread A 的对话
2. **文件是唯一 truth**: 任何 thread 的"我记得 X"都是不可信的。只信文件
3. **scope 边界严格**: thread 拿到 step X 的 SPEC，只产出 step X 的 output，不顺手做 step X+1
4. **`work/` 是工作区，root 是产出区**: thread 在 `step-X/work/` 里 draft、迭代；定稿的 artifact 移到 `step-X/` 根目录

## STATUS.md 协议

每个 `step-X/work/` 第一个文件是 `STATUS.md`：

```markdown
---
step: X
status: draft | in-progress | validated | blocked
started: YYYY-MM-DD by thread Y
last-updated: YYYY-MM-DD
---

# Status notes
- [date] thread Y started, currently working on Z
- [date] thread Y validated output, ready for downstream
- [date] blocked because of W, awaiting human decision
```

下游 thread 启动时**第一件事**是 `cat ../step-(X-1)/work/STATUS.md`。如果 status != validated → 不要开始，去和 Nick 确认。

## Output artifact 格式

按优先级：

1. **CSV** — 结构化数据，schema 必须文档化（schema 行 + 数据行）
2. **决策表 markdown** — 表格 + 每行有明确 column meaning
3. **流程图 ASCII / mermaid** — value chain / data flow
4. **narrative md** — 仅当 CSV / 表无法表达的 qualitative reasoning（cap 1 页/file）

❌ 不允许：超过 2 页的 narrative 作为主 output；任何嵌入式 hyperlink 数组；非 ascii art 的 PDF/PNG（必须可被下游 thread parse）

## Context pack（下游 thread 启动 brief）

每个 thread 启动时给的 prompt 应该包含：

```
你是 step X thread。

必读文件:
- _methodology/process-overview.md
- _methodology/handoff-protocol.md
- _methodology/pruning-rules.md  (如果你的 step 涉及 prune)
- step-X/SPEC.md (你的任务规格)
- step-(X-1)/work/STATUS.md (上游状态)
- step-(X-1)/work/* (上游产出，按 SPEC 中 Input 部分指定的 path)
- (step 3 only) _personal/nick-profile.md

不要读:
- 其他 step 的 work/ 目录
- ../2026-ai-healthcare/ (v1 老版本)，除非 SPEC 明确允许引用某个文件
- 任何 _archive/ 内容

任务：按 step-X/SPEC.md 跑这一步。产出到 step-X/work/。
完成后更新 step-X/work/STATUS.md 为 validated。
不要跨步。
```

## Subagent 使用

当一个 step 内部有多个 parallel 子任务（如 step 2 的 N 个段），主 thread 用 Claude Code 的 `Agent` tool spawn subagent：

- 每个 subagent 拿到独立子任务（"做 step 2 的 S3 段 value chain"）
- subagent 不需要看其他 subagent 输出
- 主 thread 汇总所有 subagent 输出后更新 `STATUS.md`

## Worktree 使用

如果同一 step 需要更深隔离（如 thread 想试验性 rewrite），用 git worktree spawn 独立 worktree。但**只在需要时用**，默认所有 thread 共享同一 worktree（同一文件系统状态）。

## 冲突处理

如果两个 thread 同时 edit 同一文件 → 后写覆盖前写。要避免冲突：

- 每个 step 由 1 个主 thread 负责（不并行）
- step 内部的 subagent 各写各的子文件夹
- 通过 STATUS.md 的 lock 模式申明 "我在 edit X，30 分钟内别人不要碰"

## 给人类（Nick）的接口

人类不直接 edit step-X/work/ 里的文件。人类只做：

1. 决定每个 step 启动哪个 thread
2. 看 STATUS.md 判断 step 是否 done
3. step 5 写 final-synthesis.md
4. 修改 `_methodology/` 或 `_personal/` 时 review 设计是否还成立

## 例外：紧急 stop

任何 thread 看到 "scope creep" 信号（输出超出 SPEC、跨步、加新 segment 名词）→ **立即停**，在 STATUS.md 写 `blocked: scope creep risk`，等人类决策。
