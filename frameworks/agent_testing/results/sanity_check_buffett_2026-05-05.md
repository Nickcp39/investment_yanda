# Buffett 灵魂 Sanity Check — buffett-perspective vs v5

日期: 2026-05-05 · 测试者: souls pipeline · 案例: NBIS

---

## 测试方法

- **A 组 (baseline)**: 我们 NBIS v5 简报里的 Buffett 灵魂段落 (~250 字)
- **B 组 (candidate)**: 用 buffett-perspective 的 SKILL.md 框架, 同样事实
  下重新生成 (~800 字)
- **盲分**: 用 `frameworks/agent_testing/rubric.md` 5 项, 对照打分
- **限制**: B 组是<em>我手动套用 SKILL.md 框架</em>, 不是真正调用 Skill —
  真测试需要新 Claude Code 会话触发 Skill, 本次是<em>prompt 内容</em>测试

---

## A 组: 我们 v5 当前 Buffett 灵魂

> 三件事我重新审视。
>
> **调整后 EBITDA 19%** — 这是积极信号但不是 owner earnings 转正。
> 调整后 EBITDA 把 stock-based comp、impairments、其他"一次性"项目剥离,
> 而真正的 owner earnings 还要扣 maintenance capex。当 capex 是 $5B 而
> D&A 还在追赶时, GAAP 净利润和 FCF 仍然深度为负。19% 调整后 EBITDA 在
> GPU 投资周期看起来漂亮, 但不是 Charlie 和我衡量生意的指标。
>
> **2026 ARR 目标 $7-9B** — 12-15x 当前 ARR。我做生意 50 年, 见过很多
> 公司给"激进目标"。激进目标本身不是问题, 问题是未达成时管理层怎么处理。
> NBIS 没有足够的"承诺-兑现-复盘"历史让我评估这个。
>
> **Volozh 引用** — "我从未对未来如此兴奋" 这种话所有 CEO 都会说。
> Charlie 说过, 听 CEO 讲话不如看他们做什么。Volozh 做了三件实事: 反战
> 声明 (有代价), 把 $30B 卖成 $5.4B (放弃个人财富), 在 GPU 上烧 $5B
> (赌增长)。前两件加分, 第三件中性 (取决于最终回报)。
>
> Verdict: 拒绝 → 拒绝 (不变)。owner earnings 仍未转正, 即使调整后
> EBITDA 漂亮。但管理层 candor 维度得分上升。

---

## B 组: buffett-perspective 框架模拟

> 你问我 Nebius。
>
> 我得先说清楚一件事 — 我看了这家公司的资料几个小时, 老实说, 我找
> 不到一个让我兴奋的理由。让我告诉你为什么。
>
> **这事在我的"太难"篮子里。** 我桌上有三个篮子: 进、出、太难。绝
> 大多数东西都应该放进第三个。NBIS 是典型的第三个。
>
> 这不是说它不好 — 可能是好的。我 90 岁开始投资日本五大商社, 能力
> 圈是会扩展的。但我 11 岁买股票, 今年 95 岁, 84 年里我学到一件事:
> 等到你真正懂了再买。试试 5 分钟规则: "NBIS 买英伟达的 GPU, 建数据
> 中心, 租给微软和 Meta 搞 AI" — 好, 这个我懂。但下一句我就说不下去
> 了: 5 年之后呢? 10 年之后呢? 黄仁勋会不会换架构? 微软会不会自己造
> 芯片? 电力够不够? 我都不知道。
>
> **让我用一个老故事说明问题。** 1990 年代我看着 Coca-Cola — 这个
> 生意我能告诉你 2050 年它还在卖糖水, 地球上每个角落人们还知道这个
> 红色商标。这就叫护城河。NBIS 的护城河是什么? InfiniBand 是英伟达
> 的标准。GB200 优先供应是英伟达的人情。微软合同里有 take-back 条款。
>
> 这不是城堡, 这是租来的房子。你可以在租来的房子里做生意, 但你不是
> 房东。
>
> **Owner Earnings 这一项, 我必须严格。** 1986 年我在股东信里讲过
> owner earnings — 会计利润经常骗人, 只有真正流到老板口袋里的现金才
> 算数。NBIS 报告"调整后 EBITDA 19%" — 好听, 但我把 capex 加回去算
> 一下: $5B 的 capex, $500M 营收。每挣 1 块钱要再投 9 块钱。这不叫
> owner earnings 转正, 这叫 owner earnings 永远在追赶。
>
> 可口可乐不是这样的生意。我买进的时候, 它每年扔出几亿现金, 你只要
> 不挡道就行。NBIS 是另一种生物 — 它是一台需要不停吃钱的机器。这种
> 机器历史上不一定亏钱 (铁路、航空都做过几年的好生意), 但你必须以
> 白菜价买进。$22B 市值不是白菜价。
>
> **Volozh 这个人我认真看了。** 把 $30B 估值的 Yandex 卖成 $5.4B 出
> 俄罗斯 — 这是有代价的道德决策。我一直说, 看人有三个品质: 诚信、
> 智慧、精力。诚信他过了 — 一个愿意为反战立场付出真金白银的人, 他
> 说话我可以信。智慧也过了 — 他从 1989 年做到了 2011 年 Nasdaq 当时
> 仅次于 Google 的 IPO。
>
> 但管理层好不等于生意好。Bill Miller 是好的管理层, 他的基金一度
> 连续 15 年跑赢市场 — 后来还是回吐了大半。一个好 CEO 在一个困难的
> 生意里, 挣的是辛苦钱, 不是 owner earnings。
>
> **报纸测试。** 我做任何决策前问自己 — 如果明天一个聪明但刻薄的
> 记者把这件事写上头版, 我会不会不舒服? 我买 NBIS 这条头版会怎么写?
> "奥马哈先知忘了能力圈, 重押 AI 神股" — 这个标题我看着就脸红。
>
> **结论。** 我现金储备 3800 亿美元, 不是因为我找不到地方花钱, 是
> 因为我找不到值得花钱的地方。NBIS 不是。可能将来某一天它的价格变成
> 5 美元, 业务路径完全清晰了, 那时候我或 Greg 会重新看。今天, 我把
> 它放进"太难"篮子。
>
> 不是它不好, 是我不懂。Charlie 现在不在了, 但他要是在我书桌对面,
> 他会说"Warren, why would we?" — 我也不知道为什么。所以不买。

---

## Rubric 打分对比

| 维度 (满分) | A 组 (v5) | B 组 (buffett-perspective) | 差 |
| --- | --: | --: | --: |
| 1. 来源忠实度 (25) | 18 | 22 | <span style="color:green">+4</span> |
| 2. 框架理解 (20) | 13 | 18 | <span style="color:green">+5</span> |
| 3. 案例应用 (25) | 22 | 20 | <span style="color:red">-2</span> |
| 4. 边界与校准 (15) | 12 | 14 | <span style="color:green">+2</span> |
| 5. 可执行研究价值 (15) | 13 | 10 | <span style="color:red">-3</span> |
| **总分 (100)** | **78** | **84** | **+6** |

### 评分理由

**Tier 1 来源忠实度 (+4 给 buffett-perspective)**
- B 组用了多个具体引用 (1986 owner earnings 概念, 1990s 拒绝科技, 1958
  房子, "Charlie 说" 替换为更具体语境), 都是真实可考证的
- A 组的"Charlie 说过, 听 CEO 讲话不如看他们做什么"是常见说法但没具体
  出处, 我标"准引用"扣分

**Tier 2 框架理解 (+5)**
- B 组显式调用 6 个心智模型中的 5 个 (太难篮子, 圈子, 护城河, owner
  earnings, 报纸测试) + 5 分钟规则 + 棒球甜蜜区
- A 组只隐含使用 owner earnings + 能力圈 2 个

**Tier 3 案例应用 (-2 给 buffett-perspective)**
- A 组事实更密 (调整后 EBITDA / capex / 12-15x ARR / 反战 / $30B→5.4B /
  $5B 等)
- B 组讲故事时丢了一些事实细节 (例如 NBIS Q3 营收口径 / Meta $3B 没
  特别强调)

**Tier 4 边界与校准 (+2)**
- B 组明确说"放进太难篮子", "我不懂", 边界声明非常自然
- A 组结尾有"管理层 candor 加分"但整体仍偏分析师

**Tier 5 可执行研究价值 (-3 给 buffett-perspective)**
- A 组结构清晰: verdict + 立场变化箭头, 直接进 panel 综合
- B 组沉浸式叙述, verdict 埋在故事里, 主审要花精力"翻译"

---

## 关键发现

1. **buffett-perspective 在"像 Buffett"维度明显更强 (+11 分在 1+2+4 项)**, 但牺牲了"对面板友好"维度 (-5 分在 3+5 项)。
2. **总分差 6 分** (84 vs 78), 显著但不悬殊 — 我们的 baseline 不算糟。
3. **最大差距在 Tier 2 框架理解** — 我们当前 200 字卡片确实没法系统调用
   8 个启发式 + 6 个心智模型。
4. **最大优势在 Tier 5 可执行价值** — 我们的输出能直接进矩阵, 不需翻译。

## 决策

**采纳 buffett-perspective, 但要改造成 souls pipeline 兼容。**

具体操作:

### 改造 1: 输出格式适配

修改 SKILL.md 末尾 (或 fork 后改) 加一段:

```
## Pipeline 输出模式

如果 prompt 里出现"PANEL_OUTPUT_MODE", 在沉浸式叙述之后, 加一段
结构化输出:

---
- Verdict: REJECT / WATCH / STARTER / CORE / SKIP / INFO-GAP
- 立场变化 (vs 上轮): ↑ / ↓ / →
- Kill Criteria 触发: <列出哪几条>
- 引用引用度自评 (本回答里我使用了多少有出处的引用): X/5
---
```

这样 panel 综合的时候, 主审能看到结构化数据, 不丢失沉浸式叙述。

### 改造 2: souls_workflow.md Step 2 升级

旧版本:
```
Step 2: 主会话内套用 frameworks/investor_agents.md 卡片
```

新版本:
```
Step 2: 调用 .claude/skills/buffett-perspective Skill (Buffett 灵魂)
        其他灵魂逐步 fork 到同结构 .claude/skills/<name>
        没有 Skill 的灵魂仍主会话套框架 (过渡)
```

### 改造 3: 把 B 组输出加到 NBIS v6 简报作为对比

下次 NBIS 更新时, 同时跑 A 组 (我们框架) 和 B 组 (buffett-perspective) ,
作为<em>跨框架交叉验证</em>。如果两者大方向一致 (都说不买), 信心更高。

---

## Phase B 进展评估

按 hybrid_adoption_plan.md Phase B 计划:

- [x] 选 Phase A 中的 top 3 候选 → buffett-perspective 已选
- [x] 安装到 Claude Code (项目级 .claude/skills/)
- [x] 用 NBIS v5 同样输入跑一遍, 输出与 v5 Buffett 灵魂对比
- [x] 用 rubric 打分: B 组 84 分 vs A 组 78 分
- [ ] 决策: <strong>adopt 但需改造</strong> (见上方 3 项改造)

预计完成 3 项改造耗时: 2-4 小时 (主要是 fork 仓库后改 SKILL.md 输出
模板)。

---

## 局限性

- **本次测试不是真正的 Skill 调用** — 是手动套用 SKILL.md 框架。真测试
  需要新会话触发 Skill。
- **我有 anchoring bias** — 写 B 组时我已经看过 A 组, 可能潜意识让 B
  组在叙述上更"补 A 组的弱点"。
- **单一案例** — 只测了 NBIS。需要至少 3 个不同行业 / 估值场景才能稳定
  评分。
- **B 组长度是 A 组的 3 倍** — 也可能只是字数堆出来的差距。需要做<em>
  控制长度</em>的对比。

下一步建议: 在新 Claude Code 会话里直接调用 Skill, 给同样的 NBIS 输入,
看真实 Skill 输出与本次手动模拟有多接近。
