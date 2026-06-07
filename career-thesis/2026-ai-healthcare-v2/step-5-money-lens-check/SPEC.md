---
step: 5
title: Money-Lens Synthesis (HUMAN ONLY)
input_from: step-4-positions
output_to: 决策（不再传给下一步）
status: spec-only — to be executed by Nick personally, not by any AI thread
---

# Step 5 SPEC: Money-Lens Synthesis

## ⚠️ 重要

**本 step 必须由 Nick 本人完成。** 任何 AI thread 不允许产出 `final-synthesis.md`。AI 只能产 input 数据让 Nick 用。

理由:
- step 1-4 都是 "信息 → 信息" 的转换，可以 AI 做
- step 5 是 "信息 → 行动决策"，包含 Nick 的 risk preference / 家庭情况 / 人生 timing / 不可言传的"感觉"——这些任何 AI 都不完整持有
- 把这一步外包给 AI = 让 AI 替你做人生选择，这是 _methodology/process-overview.md 设计原则 §5 明确禁止的

## 1. Question

**根据 step 1-4 输出，Nick 接下来 12 / 36 / 120 个月的具体动作是什么？为什么？**

这 1 个 question 分 3 个时间窗:
- 12 月：接下来一年的具体动作（投递哪些公司 / 学什么 / 跟谁聊）
- 36 月：3 年的方向（已 commit 哪条主线 / Stage 2 准备）
- 120 月：10 年 thesis（终极目标 + 巨大不确定性 + 怎么应对）

## 2. Input

Nick 读:
- `step-1-macro-sizing/work/summary.md`
- `step-1-macro-sizing/work/segments-ranked.csv`
- `step-3-rent-capture-and-fit/work/nick-fit-overlay.csv` (按 final_priority 排序)
- `step-3-rent-capture-and-fit/work/insights.md`
- `step-4-positions/work/candidate-positions.csv`
- `step-4-positions/work/top-5-deep-dive/*.md`
- `_personal/nick-profile.md`（自己的）

可选参考:
- `step-2-value-chains/work/` 如果 Nick 想 zoom in 某条 chain
- `_methodology/` (回顾 process 设计)

## 3. Output

### 3.1 final-synthesis.md (Nick 写)

建议结构:
```markdown
---
synthesis_by: Nick
date: YYYY-MM-DD
process_input: step-1 to step-4 outputs as of YYYY-MM-DD
---

# Final Synthesis

## 我看完所有 input 后的 3 个最反直觉发现
1. ...
2. ...
3. ...

## 12-month plan
- 主线动作: ...
- 备选动作: ...
- 触发条件: 如果 X 发生就转向 Y

## 36-month plan
- 主线: ...
- 触发条件: ...

## 120-month thesis
- 终极目标: ...
- 主要不确定性: ...
- 怎么应对不确定性: ...

## money lens sanity check
- 我选的方向，谁在付钱给我？这个付钱方的预算在涨还是缩？
- 我是 follow money 还是 follow technology / hype / signal？

## 我决定不做的事 (explicit no-go)
- ...

## 下次 review 触发
- 下一次重读这份 synthesis 的 trigger（如：6 月后 / 某个 milestone hit / 某个外部信号）
```

### 3.2 决策不外包

Nick 完成 final-synthesis.md 后，**不**让任何 AI "review/optimize/critique" 它。
你可以让 AI 帮你 fact-check 某个数字、找 source、改 typo，但不让 AI 替你 second-guess 你的决策。

## 4. Method

### Nick 自己的内部 process
建议:
1. 一次性把 input 全看完（半天到一天）
2. 不直接动笔写 synthesis
3. 让自己离开几小时甚至一晚（生理 incubation period）
4. 第二天早上写第一版 synthesis
5. 1-2 周后再 review 一次（远距离决策 vs 当下决策对比）
6. 与 1-2 个 trusted friend / mentor 讨论 synthesis，但**不**让他们写你的 synthesis

### 段永平式提问
对每个备选方向，问自己 5 个问题（仿 frameworks/investor_agents.md 里的灵魂 panel）:

1. **段永平式**: 这个方向"做对的事"还是"把事做对"？我能不做这个吗？
2. **芒格式**: 这个方向的 inversion 是什么？什么会让它失败？我能接受失败结果吗？
3. **巴菲特式**: 10 年后回头看，这是不是一个"我一直 hold 的好资产"？
4. **段永平 part 2**: 我能 commit 5 年不动这个方向吗？
5. **Munger inversion**: 如果我不做这个，我会做什么？那个 alternative 更好吗？

## 5. Pruning
本 step 不再 prune segment / position（已在前 4 step 做完）。
本 step 唯一 "decision" 是 Nick 自己选 1 个 12 月主线 + 1-2 个备选。

## 6. Validation

Nick 自己问:
- [ ] final-synthesis.md 里的 12-month plan 是否具体到 "周末做 X"（不是 "考虑 Y"）
- [ ] money lens 那一段是否问过 5 个段永平式问题
- [ ] explicit no-go 是否包含至少 3 个具体方向（不是空话）
- [ ] 下次 review 触发是否有具体 trigger condition

## 7. Anti-patterns

- ❌ 让 AI 起草 final-synthesis.md 然后 Nick "润色"（这是变相外包）
- ❌ synthesis 拖延 > 2 周（input 会 stale）
- ❌ 一次写完不再 review（重要决策必须远距离视角再看一遍）
- ❌ 决定后立即向多人广播（先 silent commit 1-2 周自我观察 reaction）
- ❌ 决定基于 "感觉对" 而没经过段永平式 5 问

## 8. Money lens

整个 step 5 就是 money lens 的最后兑现。

具体 sanity check:
> "我选的 12-month 主线动作，付钱的人是谁？这个人 5 年后还在付钱吗？我能从'付钱方'的位置 inverse 思考'这个方向'吗？"

## 9. Effort hint

- 看完 step 1-4 input: 半天到一天
- incubation: 一天到一周（不主动想）
- 写第一版: 半天
- review: 1-2 周后半天
- 与 mentor 讨论: 数次半小时-1 小时对话
- 总 calendar: 2-4 周
- 总主动 thinking: ~3-5 天
