# 投资名人 Agent 测试体系

这个目录用于测试基于投资名人公开发言、书籍、股东信、访谈和已训练 agent
集合出来的分析角色。

目标不是让 agent 模仿真人语气，而是验证它是否真正掌握了一个投资框架：

- 是否忠实于来源。
- 是否知道自己的适用边界。
- 是否能在真实公司案例中稳定应用。
- 是否能承认不知道。
- 是否能和其他 agent 形成有效分歧，而不是统一输出漂亮废话。

## 测试对象

每个待测 agent 都要登记为一个版本：

```text
Agent name:
Version:
Builder / source:
Underlying model:
Source pack:
Last evaluated:
Evaluator:
Status: draft / testing / approved / rejected / retired
```

不要把“名人名字”直接等同于能力。一个叫 Buffett Agent 的模型，只有通过
Buffett 来源忠实度和公司分析测试后，才可以进入实际研究流程。

## 五层测试

1. 来源忠实度测试

   给 agent 一组来源摘录或来源摘要，要求它只基于材料总结原则。它不能编造
   书名、年份、语录、案例或持仓。

2. 框架边界测试

   给它不适合该框架的问题，看它会不会乱答。例如让 Graham Agent 评估一家
   无盈利 SaaS 的远期 TAM，或者让 Dalio Agent 对单家公司产品护城河做确定
   判断。合格 agent 应该主动说明边界。

3. 案例应用测试

   给自包含案例包，让 agent 输出判断、证据、反证和 kill criteria。案例包
   必须包含足够事实，避免 agent 靠实时搜索或幻觉补全。

4. 反诱导测试

   故意加入错误归因、伪造语录、热门叙事、短期股价诱惑，看 agent 是否纠正
   或降权处理。

5. 交叉辩论测试

   同一家公司交给多个 agent。合格结果不是所有人一致，而是能形成可解释分歧：
   Buffett 可能喜欢商业质量，Klarman 可能拒绝价格，Marks 可能提醒周期位置。

## 最低通过线

一个 agent 至少需要：

- 总分 >= 80/100。
- 来源忠实度 >= 18/25。
- 没有严重失败项。
- 在至少 3 个不同类型案例中通过。

严重失败项包括：

- 编造直接语录或来源。
- 把某位投资人的观点说反。
- 对明显超出能力圈的问题装作确定。
- 不看价格就建议买入。
- 不看资产负债表就评价高杠杆公司安全。
- 把短期价格走势当作核心投资理由。

## 实际使用流程

1. 先给每个 agent 准备 `source pack`。
2. 用 `benchmark_cases.md` 中的题目盲测。
3. 如果要批量跑测试，用 `benchmark_cases.jsonl` 作为机器可读题库。
4. 用 `rubric.md` 打分。
5. 把结果写入 `scorecard_template.md`。
6. 只有 approved agent 可以用于正式公司 memo。

## 当前筛选结果

当前可用名单见 `approved_agents.md`。

初筛报告见 `results/initial_screening_2026-05-05.md`。这份报告筛选的是当前
repo 内的 agent 卡片，而不是外部已训练 agent 的真实输出。外部 agent 接入后
仍需要单独跑题库和打分。

## 推荐输出格式

每次测试输出都应该包含：

```text
Agent:
Case:
Verdict:
Score:
Strengths:
Failures:
Source fidelity notes:
Boundary notes:
Retest needed:
```
