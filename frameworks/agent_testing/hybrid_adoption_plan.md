# 混合采纳计划 (Hybrid Adoption Plan)

版本: v1 · 起草: 2026-05-04

---

## 核心策略

**Adopt > Fork > Build**

不要从零自训。优先级:
1. **Adopt (直接用)** — 现成的 Claude Skill / Custom GPT / 开源项目, 通过验证后直接接入
2. **Fork (微调)** — 现成的有但不完美, fork 一份按我们 pipeline 改
3. **Build (自建)** — 没现成的或现成的全部不及格, 才自建

**纪律**: 无论来源, 都必须过 `frameworks/agent_testing/rubric.md` ≥ 75 分
才能用于正式 memo。来路不重要, benchmark 表现才重要。

---

## 每位灵魂的初步分类

| 灵魂 | 候选来源 | 决策 | 理由 |
| --- | --- | --- | --- |
| Warren Buffett | [buffett-perspective Skill](https://github.com/will2025btc/buffett-perspective), AI Hedge Fund Buffett agent, ChatGPT Buffett GPT, [40K Meta-Prompt](https://x.com/rohanpaul_ai/status/1947412958885384410) | **Adopt 候选** | 候选最多 |
| Charlie Munger | AI Hedge Fund Munger agent, ChatGPT Munger GPT (待找) | **Fork 候选** | 公开 Skill 较少 |
| Howard Marks | AI Hedge Fund 不一定有 (Marks 较冷门), 自建 | **Build 候选** | Oaktree 备忘录公开易获取 |
| Seth Klarman | Custom GPT (待找), 自建 | **Build 候选** | 一手材料稀缺 |
| 段永平 | 无 | **Build 必须** | 中文专属, 没人做过 |
| Li Lu | 无 | **Build 必须** | 公开材料少 |
| Terry Smith | Custom GPT (待找) | 待评估 | 第二批 |
| Philip Fisher | 待找 | 待评估 | 第二批 |
| Peter Lynch | 待找 | 待评估 | 第二批 |
| Joel Greenblatt | 待找 | 待评估 | 第二批 |

---

## 验证门槛 (Adoption Gate)

任何外部灵魂被采纳前, 跑这套 sanity check:

### 必须通过 (硬指标)
- **来源忠实度 ≥ 18/25**: 喂它一道有原文的题, 看引用是否真实
- **框架理解 ≥ 14/20**: 给它边界外的问题, 看会不会装懂
- **0 严重失败**: 不编造直接语录, 不把投资人观点说反
- **NBIS 简报输出与我们 v5 的 Buffett 灵魂 head-to-head 不显著差**

### 软指标
- 中文支持 (因为我们 pipeline 是中英混)
- 能输出结构化 JSON / Markdown (能整合到 HTML pipeline)
- 不依赖外部 API key (除非愿意接入)

---

## 平台独立性策略

终极目标是<em>跨基础模型</em>分布灵魂, 不是全压在 Claude 上:

| 平台 | 推荐分配 | 基础模型 |
| --- | --- | --- |
| **Claude Code Skill** | 段永平 (主审), Li Lu, 中文专属 | Anthropic Claude |
| **ChatGPT Custom GPT** | Buffett, Munger, Klarman | OpenAI GPT-4o/5 |
| **Gemini Gem** | Marks, Smith, Lynch | Google Gemini |
| **本地 / API** | 备用 | Llama / Mistral / Qwen |

输出汇总到我们的 HTML pipeline。<em>这是真正解决"souls = 一个底层模型"
的根本路径</em>。

现阶段: 不强求三平台齐备, 但<em>架构上</em>要支持。先把 Claude 端做完整,
再扩平台。

---

## 4 阶段执行计划

### Phase A: 评估现有 (1 周)

- [ ] 拉 [buffett-perspective](https://github.com/will2025btc/buffett-perspective)
      README + 主要 Skill 文件, 评估 prompt 质量
- [ ] 浏览 [AI Hedge Fund](https://github.com/) 仓库 (具体 URL 待找),
      看 12 个 agent 的 prompt 设计
- [ ] 浏览 [buffett-skills (agi-now)](https://github.com/agi-now/buffett-skills)
- [ ] 检查 [Warren-Buffett-AI-Twin (jyana65)](https://github.com/jyana65/Warren-Buffett-AI-Twin)
- [ ] 搜索 ChatGPT GPTs marketplace 的 Munger / Marks / Klarman / Smith GPT
- [ ] 输出: `frameworks/agent_testing/results/external_agent_audit_<date>.md`
      记录每个候选的初步评分

**Phase A 不是要测试它们, 是要看它们的"原料"质量。**测试在 Phase C。

### Phase B: 候选者 sanity check (1 周)

- [ ] 选 Phase A 中的 top 3 候选 (例如 buffett-perspective)
- [ ] 安装到 Claude Code 或 ChatGPT
- [ ] 用 NBIS v5 同样的输入跑一遍, 输出与我们 v5 Buffett 灵魂对比
- [ ] 用 `rubric.md` 双盲打分 (我们的 + 外部的, 不知哪是哪)
- [ ] 决策: 谁能 adopt, 谁要 fork, 谁不行

### Phase C: 自建段永平 + Li Lu (2-3 周)

- [ ] 段永平 source pack: 雪球 export 工具 + 精选 200-300 帖
- [ ] Li Lu source pack: 北大 / Columbia 公开演讲 transcripts
- [ ] 写 system prompt (目标 5,000+ 字, 不是当前 200 字)
- [ ] 在 Claude Project 搭建 (Claude 端, 因为中文)
- [ ] 跑 benchmark, 通过 80 分阈值

### Phase D: 集成 + 平台扩展 (2-3 周)

- [ ] 修改 `souls_workflow.md` 第 2 步骤:
      panel 调用<em>外部 Skill / Project</em>而不是主会话内套框架
- [ ] 设计输出 schema: 每位灵魂 verdict 结构标准化, 跨平台一致
- [ ] (可选) ChatGPT 端搭建 Buffett/Munger Custom GPT
- [ ] (可选) Gemini Gem 端搭建 Marks
- [ ] 用 Tier 5a holdout 测试 (你之前提的 2026 数据切割) 跑全 panel

---

## 时间表对照

| 路径 | 总周期 | 投入 |
| --- | --- | --- |
| 原始 training_plan (从零自训) | 9-13 周 | 每周 5-10 小时 |
| 混合采纳 (本计划) | 5-7 周 | 每周 4-7 小时 |
| **节省** | **~4-6 周** | **~1/3 工作量** |

主要节省来自<em>不重复造 Buffett / Munger / Marks 这些已有人做过的</em>。

---

## 与 training_plan.md 的关系

| training_plan.md | hybrid_adoption_plan.md (本文) |
| --- | --- |
| 假设全部自训 | 优先采纳现有 |
| 9-13 周完成核心 5 位 | 5-7 周 |
| Phase 1 = 源材料归集 | Phase A = 评估外部候选 |
| Phase 2 = 自搭 Project | Phase B = 测试外部 + Phase C 自建少数 |

**关系**: hybrid_adoption_plan 是<strong>主路径</strong>; training_plan 是
<em>fallback</em> (当 Phase B 测试发现外部全不行时, 退回自训)。

---

## 第一步立刻执行

Phase A 第 1 项: 拉 buffett-perspective README + 主要 Skill 文件,
评估其 prompt 质量。

预期输出:
- buffett-perspective 的<em>实际安装方式</em> (Claude Code 直接装 / 复制
  prompt / fork repo)
- prompt 质量初步判断 (跟我们的 200 字卡比, 高几个量级)
- 是否包含我们没有的元素 (源材料 / 例子 / 边界声明)

如果 buffett-perspective 让人惊艳 → 全计划朝"采纳为主"调整
如果 buffett-perspective 一般 → 我们的 baseline 不算糟, 加快自训

接下来启动这一步。
