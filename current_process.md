# 当前进度 (Current Process)

最后更新: 2026-05-06

## 这份文档的用途

快照式记录 lab 当前阶段、最近做完什么、下一步要做什么。每次阶段性
push 时刷新一次，避免回头时丢失上下文。

不是 changelog (那个看 git log)。是"我现在在哪一关"。

---

## 当前阶段

**Phase**: 灵魂训练 → 外部 Skill 采纳验证

从"我自己一个人在 Claude 会话里套用框架卡"升级到"使用经过验证的
外部 Skill 工具"。决策树见 `frameworks/agent_testing/hybrid_adoption_plan.md`：
**Adopt > Fork > Build**。

---

## 最近一轮工作 (2026-05-06)

### 测试结论：ai-hedge-fund 全部 agent 不采纳

跑了 ai-hedge-fund 仓库里的 investor personas (Munger / Cathie Wood /
Damodaran 等) 之后,结论:**水平整体不如我们自训的灵魂卡 +
buffett-perspective 的组合**。

观察到的问题:

- 输出形态是 trading signal (buy/sell/hold + confidence),**不是
  investment memo lens** — 用途不匹配
- prompt 偏短,一手原文引用少,内部矛盾声明基本没有
- 框架边界声明缺失,"灵魂感"弱,不像本人风格
- 5/4 audit 里"fork ai-hedge-fund Munger / Cathie Wood / Damodaran"
  的 P1 计划**撤销**

### 影响:外部 Skill 采纳通道收窄

之前 hybrid_adoption_plan 是 **Adopt > Fork > Build** 三档。今天测试
之后:

- **Adopt 档**:目前只有 buffett-perspective 一个真正过关
- **Fork 档**:基本作废 (ai-hedge-fund 是该领域 43k 星的标杆,它都不行,
  其他 fork 来源希望也低)
- **Build 档**:回到原计划——Marks / Klarman / 段永平 / Li Lu / Cathie Wood
  / Damodaran 全部走自建

也就是说:**hybrid plan 实际上退化成了 "Adopt(Buffett) + Build(其他全部)"
的两档**。Fork 这一档先放进 backlog,除非将来有新的高质量候选出现。

### 无代码改动

今天纯测试 + 决策修订,没动文件 (除了本文档)。

---

## 上一轮工作 (2026-05-05)

### 已落地

- `frameworks/agent_testing/hybrid_adoption_plan.md` v1 — Adopt vs Build
  决策框架
- `frameworks/agent_testing/training_plan.md` v1 — 长期训练目标 (L4 不
  够 → L2 最低门槛)
- `frameworks/agent_testing/results/sanity_check_buffett_2026-05-05.md` —
  buffett-perspective 的 prompt-内容 sanity check (NBIS 案例)
- `frameworks/agent_testing/results/external_agent_audit_2026-05-04.md` —
  外部灵魂 Skill 候选审计

### 真·会话验证 (本次 Claude Code session)

第一次在新会话里**真正调用 Skill**而不是手动套框架：

- `buffett-perspective` Skill on NBIS — Verdict: 太难篮子；6 个心智模型
  + 7 关全部走完，结论"直接进太难篮子，watch 都不该 watch"
- `buffett-perspective` Skill on Apple (正面对照) — Verdict: wonderful
  business 但当前不是 wonderful price；7 关对照 NBIS 表现差异显著
- `buffett-perspective` 的 candor 测试 (为啥巴菲特卖苹果) — 三层理由
  分解 (税 → 集中度 → 估值) + 主动承认"减早了"
- `expert-munger` Skill on NBIS — Verdict: too stupid 而非 too hard；
  Inversion + Incentive + Lollapalooza (七种 Cialdini) + 历史模式匹配
  (Cisco/Nortel/JDSU)

会话验证比 prompt-内容验证多了**真实 Skill 触发 + 工具调用 + 文件读取**
的完整路径，更接近正式使用形态。

---

## Skill 采纳状态

| 灵魂 | 候选 Skill | 状态 | 下一步 |
|---|---|---|---|
| Warren Buffett | `buffett-perspective` | prompt sanity check + 一次会话验证均通过 | 跑 benchmark_cases.jsonl 全量 |
| Charlie Munger | `expert-munger` | 一次会话验证通过 (NBIS) | 多场景 + 跑 benchmark |
| Howard Marks | 待找 | Build candidate | 收集 Oaktree 备忘录全集 |
| Seth Klarman | 待找 | Build candidate | 一手材料盘点 |
| 段永平 | 无 | **Build 必须** | 雪球 export pipeline |
| Li Lu | 无 | **Build 必须** | 一手材料盘点 |

⚠ "通过会话验证"≠ 正式采纳。正式采纳门槛仍然是 `rubric.md` ≥ 75
分跨 ≥ 3 案例。当前只是放行到 benchmark 阶段。

---

## 数据采集 Pipeline 状态

频道索引 + 元数据 + ASR 三层，已搭好基础设施：

- ✅ `scripts/channel_video_index.py` — Bilibili / YouTube 频道索引
- ✅ `scripts/bilibili_channel_queue.py` — Bilibili 元数据队列 (新)
- ✅ `scripts/youtube_asr_queue.py` — YouTube 无字幕兜底 ASR (新)

已收录频道：

- `tradesmax` (YouTube) — 美股投资网，AI 主题视频源
- `zhanguoshidai` (YouTube + ASR) — 战国时代频道
- `bilibili-1039025435` (Bilibili) — 段永平相关 (待确认归类)

⚠ audio/ 与 transcripts/ 全部 gitignore (zhanguoshidai/audio 已 725 MB)。

---

## 下一步 (按优先级)

1. **跑 buffett-perspective 全 benchmark** — `benchmark_cases.jsonl` 至少 5 个
   不同类型案例，rubric 5 项打分，过 75 分门槛即正式采纳
2. **跑 expert-munger 全 benchmark** — 同上
3. **Howard Marks Build 路径启动** — 收集 Oaktree memo 全集,自建灵魂卡
   (5/6 测试后已确认 Fork 档不可行,直接 Build)
4. **段永平雪球 export pipeline** — 中文专属，没人做过，必须自建
5. **将本次会话的两个验证记录化** — 把 NBIS Munger / Apple Buffett /
   Apple-sale candor 测试沉淀为 `results/` 下独立 sanity check 文件

---

## 已知风险

- Skill 验证目前只有"我手动跑 + 主观判断"一种方式，没有自动化 rubric
  打分流水线
- benchmark 案例数量可能不足以验证灵魂的泛化能力 (跨行业 / 跨周期)
- 上游 Skill 可能后续更新，需要锁定 commit / 版本号
- 会话状态 vs Skill 状态可能错位 — 同一 Claude 会话连续切换多个灵魂
  Skill 时存在隐性记忆污染

---

## 相关文档导航

- [souls_workflow.md](frameworks/souls_workflow.md) — 灵魂使用与 panel 编排规则
- [hybrid_adoption_plan.md](frameworks/agent_testing/hybrid_adoption_plan.md) — Adopt vs Build 决策
- [training_plan.md](frameworks/agent_testing/training_plan.md) — 长期训练目标
- [frameworks/agent_testing/README.md](frameworks/agent_testing/README.md) — 测试框架总览
- [companies/nbis.md](companies/nbis.md) — NBIS 简报 (本次主要测试案例)
