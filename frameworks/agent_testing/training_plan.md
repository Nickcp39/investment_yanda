# 灵魂训练计划 (Souls Training Plan)

版本: v1 · 起草日期: 2026-05-04

---

## 目标

把当前 13 位虚拟灵魂从"<em>我一个人在 Claude 会话里套用框架</em>"升级到
"<em>独立运行 + 源材料锚定 + 通过 benchmark 验证</em>"的状态。

成功标准: 任意核心灵魂能在<strong>不依赖主对话上下文</strong>的情况下,
回答 `benchmark_cases.jsonl` 题目, 并通过 `rubric.md` 打分:

- 总分 ≥ 80/100
- 来源忠实度 ≥ 18/25
- 0 严重失败项 (编造语录 / 编造书籍 / 把观点说反)
- 至少 3 个不同类型案例通过

## 为什么 L4 (改 prompt) 不够

仅改 `frameworks/investor_agents.md` 卡片里的描述, 解决不了 5 个根本问题:

1. <strong>没有源材料锚定</strong>: 灵魂引用 Buffett 股东信时, 全靠模型
   预训练记忆。无法保证不编造 (rubric 严重失败项)。
2. <strong>没有上下文隔离</strong>: 13 位灵魂全在同一 Claude 会话里回答,
   共享前文记忆 → 隐性收敛。
3. <strong>没有验证循环</strong>: prompt 改完不知道是否更好。
4. <strong>没有版本控制</strong>: 改 prompt 等于覆盖, 看不到演化。
5. <strong>没有性能基线</strong>: 不知道当前灵魂在 rubric 上得多少分。

L2 (Custom GPT / Claude Project per 灵魂) 是<strong>最低可接受门槛</strong>。
L3 (RAG) 和 L1 (微调) 是后续选项。

## 范围

### 必须训练 — 核心 5 位

按 souls_workflow.md 定义的核心 panel:

| 灵魂 | 一手源材料 (必备) | 估计语料量 |
| --- | --- | --- |
| Warren Buffett | 1965-2024 Berkshire 股东信 + 年报 + 股东大会 Q&A 文字版 | ~3,000 页 |
| Howard Marks | 1990-2025 Oaktree 备忘录全集 + 两本书 (*The Most Important Thing*, *Mastering the Market Cycle*) | ~2,500 页 |
| Charlie Munger | *Poor Charlie's Almanack* + Daily Journal 2014-2023 transcripts + Berkshire 股东会问答 | ~2,000 页 |
| Seth Klarman | *Margin of Safety* + Baupost 公开信 (有限) + 公开访谈 transcripts | ~800 页 |
| 段永平 | 雪球 @大道无形我有型 全部帖子 (export) + Stanford Q&A + 主要采访 | ~1,500 页 |

### 第二批 — 扩展 4 位

| 灵魂 | 一手源材料 |
| --- | --- |
| Terry Smith | Fundsmith 年报全集 (2010-2025) + *Investing for Growth* + Accounting for Growth |
| Philip Fisher | *Common Stocks and Uncommon Profits* + *Conservative Investors Sleep Well* |
| Peter Lynch | *One Up on Wall Street* + *Beating the Street* + Magellan-era 演讲 |
| Joel Greenblatt | *The Little Book That Beats the Market* + *You Can Be a Stock Market Genius* + 哥伦比亚课程 |

### 第三批 — 视情况

| 灵魂 | 备注 |
| --- | --- |
| Li Lu | 公开材料有限 — 需谨慎处理来源真实性 |
| Ray Dalio | LinkedIn 帖 + *Principles* + *Big Debt Crises* |
| George Soros | *The Alchemy of Finance* — 反身性框架专门用 |
| Benjamin Graham | *Security Analysis* + *The Intelligent Investor* — 已逝, 但框架经典 |

## 训练 6 阶段

```
Phase 0: 基线测试 (1 周)
  ↓
Phase 1: 一手源材料归集 (3-4 周, 可并行)
  ↓
Phase 2: 每位灵魂的 Custom GPT / Claude Project 搭建 (1-2 周)
  ↓
Phase 3: Benchmark 第一轮 + Scorecard (1 周)
  ↓
Phase 4: 失败模式修复迭代 (2-3 周)
  ↓
Phase 5: Approved 名单更新 + RAG 升级评估 (1 周)
```

总周期: <strong>9-13 周 (~3 个月) 完成核心 5 位</strong>。每周投入 ~5
小时即可。

### Phase 0 — 基线测试 (Baseline)

**目标**: 在改任何东西<em>之前</em>, 先量化当前灵魂的水平。

**步骤**:
1. 选 `benchmark_cases.md` 中 3 道不同类型题目 (compounder / 估值 /
   宏观)
2. 让当前 13 位灵魂 (在主 Claude 会话里) 答一遍
3. 用 `rubric.md` 打分, 填 `scorecard_template.md`
4. 输出 `results/baseline_2026-05.md`

**成功标准**: 有量化数据。一般预期当前灵魂 60-70/100, 来源忠实度
12-15/25 (因为没有源材料锚定)。

**为什么先做这步**: 不知道起点就不知道改进幅度。

### Phase 1 — 一手源材料归集

**目标**: 给每位核心灵魂建一个 source pack。

**目录结构**:
```
frameworks/<soul-folder>/
  source_pack/
    primary/         # A 级一手 (本人书籍/股东信/原始演讲)
      buffett_letter_1977.pdf
      buffett_letter_1978.pdf
      ...
    secondary/       # B 级 (高质量转录, 比如 CNBC 大会 Q&A 整理)
    excluded/        # 看过但拒绝纳入的 (比如来源不清的语录合集)
    SOURCES.md       # 每条素材登记: 来源 / 日期 / 页数 / 真实性确认
```

**关键纪律 (来自 source_grounding_matrix.md)**:
- A 级 PDF 必须是<em>原始扫描或官方电子版</em>, 不接受第三方编纂
- B 级转录必须有原始视频 / 录音 URL
- 任何"语录合集"、"金句汇编"放 `excluded/`, 不进 source pack
- `SOURCES.md` 每条带 retrieval date 和真实性确认

**优先级**: Buffett (源材料最齐) → Marks → Munger → 段永平 → Klarman。

**估计耗时**: 每位灵魂 5-15 小时归集 + 验真。Buffett 因 Berkshire 网站
集中, 最快 (5 小时); 段永平最慢 (雪球 export 需要工具)。

### Phase 2 — Custom GPT / Claude Project 搭建

**目标**: 让每位灵魂在<strong>独立会话</strong>运行, 不与主 Claude 上下文
混合。

**两种平台对比**:

| 选项 | 优势 | 劣势 |
| --- | --- | --- |
| **ChatGPT Custom GPT** | 上传文件多 (20 个), 大众分享, market 已有先例 | OpenAI 模型, 与 Claude 不同, 跨平台输出格式整合麻烦 |
| **Claude Project** | 与主对话同生态, 项目内文件持久化 | 单文件 30MB 上限, 知识库管理较手动 |

**推荐**: 先用 <strong>Claude Project</strong> (与主仓库集成顺), 之后
也可在 ChatGPT 复刻一份做对照实验。

**每个 Project 的标准化设置**:
- 系统 prompt = `frameworks/investor_agents.md` 中该灵魂卡 + 显式的
  "禁止编造直接语录, 不确定来源时主动声明"
- 项目文件 = `source_pack/primary/` 全部 + `source_pack/secondary/`
  精选
- 项目说明里嵌入 `rubric.md` 5 项打分维度, 让灵魂知道自己被怎么评估

**输出**: 每位灵魂一个 Claude Project 链接, 登记到 `approved_agents.md`
新增一列 "External Project URL"。

### Phase 3 — Benchmark 第一轮

**目标**: 量化训练后的灵魂水平。

**步骤**:
1. 从 `benchmark_cases.jsonl` 选 5 道题, 每道至少覆盖 3 位灵魂
2. 在每位灵魂的 Project 中独立答题 (复制题目, 不带主会话上下文)
3. 把每个答案保存到 `results/<soul>/case_<id>.md`
4. 人工 (或第二个 Claude) 用 rubric 打分
5. 输出 `results/phase3_scorecard_<date>.md`

**成功标准**:
- 总分均值 ≥ 75/100 (从 baseline 60-70 提升 ≥ 8 分)
- 来源忠实度均值 ≥ 18/25 (核心改善点, 因为现在有 primary source)
- 严重失败项 ≤ 1 (编造语录率从 baseline 应该大幅下降)

### Phase 4 — 失败模式修复

**目标**: 把没达标的灵魂打到能用。

**典型失败模式 + 修复策略**:

| 失败 | 根因 | 修复 |
| --- | --- | --- |
| 编造直接引用 | 模型预训练记忆错配 | 系统 prompt 加: "引用必须从上传的 source_pack 检索, 否则说 '此处无源' " |
| 框架边界模糊 | 卡片描述不够具体 | 卡片里加 3 个"该回答"和 3 个"该拒答"的范例 |
| 输出泛泛 | 缺少强制结构 | 系统 prompt 加 5 字段输出模板 (引用 / verdict / 理由 / kill criteria / 信心) |
| 多灵魂收敛 | 卡片描述同质化 | 加各灵魂的<em>反差点</em> — Buffett vs Munger 在某题上的预期分歧 |

**迭代规则**:
- 每次修改 system prompt 或源材料后, <em>重跑同一组题</em>
- 分数下降的修改回滚
- 通过 80 分阈值的灵魂登记到 approved 列表 (附 "approved as of date")

**预期**: 5 位核心灵魂里 3-4 位能在 2-3 次迭代后过 80 分。1 位
(可能段永平, 因雪球材料散) 可能要更多轮。

### Phase 5 — Approved 名单更新 + RAG 评估

**目标**: 决定哪些进入正式生产使用, 哪些需要进 L3 升级。

**Approved 名单维护**:
- `approved_agents.md` 新增列: External Project URL · Last benchmark score · Last evaluated date
- 每月自动重测 1 道随机题, 防止漂移
- 分数低于 75 的自动降级回 Tier B

**RAG 评估**:
- 对得分 ≥ 90 的灵魂, 评估是否升级到 RAG (向量索引整个 source_pack)
- 对得分 75-90 的灵魂, 保持 Custom Project 状态
- 对反复无法过 75 的灵魂, 暂停训练, 转回 Tier C 仅作 supporting lens

## 资源需求

| 项 | 数量 / 成本 |
| --- | --- |
| Claude Pro / ChatGPT Plus | 必需 (用于 Project / Custom GPT) |
| 时间投入 | 每周 5-10 小时, 持续 ~3 个月 |
| 一手 PDF / transcript 获取 | 大部分免费 (Berkshire / Oaktree 官网公开) |
| 雪球 export 工具 | 段永平 unique, 需脚本或第三方工具 |
| 评分人力 | 自评为主; 偶尔交叉用第二个 Claude 评 |
| 新增依赖 (RAG 阶段) | OpenAI Embeddings API 或 sentence-transformers, $20-50 |

**不需要**: GPU, 微调成本, 专门 ML 知识。整个流程是<em>系统性 prompt
+ source 工程</em>, 不是模型训练。

## 风险 + 缓解

| 风险 | 概率 | 缓解 |
| --- | --- | --- |
| 段永平雪球 export 困难 | 高 | Plan B: 手动收集精选 200-300 帖, 不追求全集 |
| Custom GPT/Project 上传文件大小限制 | 中 | 把每位灵魂的 source pack 切成"必读" + "可选", 必读放 Project |
| 灵魂训练后仍编造引用 | 中 | 加显式"无源拒答"指令, 在系统 prompt 末尾重复强调 |
| 验证人力不足 | 高 | 接入第二个 LLM 当 judge, 但<em>抽样人审</em>10% |
| 训练完成但与主 pipeline 集成失败 | 低 | Phase 2 设计时就规定输出 schema, 提前对齐 souls_workflow.md |

## 时间表 (假设每周 7 小时)

```
Week 1:    Phase 0 基线测试
Week 2-5:  Phase 1 源材料归集 (Buffett → Marks → Munger → 段永平 → Klarman)
Week 6-7:  Phase 2 Project 搭建
Week 8:    Phase 3 第一轮 benchmark
Week 9-11: Phase 4 失败模式修复迭代
Week 12:   Phase 5 Approved 名单更新
Week 13+:  扩展 4 位 (Terry Smith / Fisher / Lynch / Greenblatt)
```

## 验收标准 (DoD — Definition of Done)

阶段一(核心 5 位)完成的判定:

- [ ] 5 位核心灵魂均有独立 Claude Project + source_pack
- [ ] 每位灵魂在 phase 3 benchmark 上 ≥ 75 分, 至少 3 位 ≥ 80 分
- [ ] 0 位有"严重失败项 = 编造引用"
- [ ] approved_agents.md 更新, 列出每位灵魂的 Project URL + 最近测试分
- [ ] souls_workflow.md 第 2 步骤已经接通: panel 调用<em>外部 Project</em>
      而不是主会话内套框架
- [ ] 一份 NBIS 简报用<em>外部灵魂</em>从零跑一遍, 与 v5 (主会话版本)
      做<em>差异分析</em> — 确认外部版本至少在 source 引用维度严格更优

## 与 souls_workflow.md 的对接

souls_workflow.md 当前 Step 2 (核心 5 灵魂初评) 是"在主会话里套框架"。
训练完成后 Step 2 改为:

```
Step 2 (升级版):
  对核心 5 位中的每一位 — 调用其外部 Project / Custom GPT
  传入: 当前 ticker + facts.md + 题目模板
  得到: 该灵魂的独立 verdict (在隔离上下文中产生)
  汇总到 panel 表格
```

这才真正解决"souls = 我一个人"那个根本问题。

---

## 启动条件

要正式启动这份训练计划, 用户需要确认:

1. 时间投入愿景: 每周 5-10 小时 × 3 个月 (核心 5 位)
2. Claude Pro 或 ChatGPT Plus 订阅就位
3. 同意先做 Phase 0 基线测试再开始 Phase 1, 不跳过

如果以上都同意, 下一步就是<strong>启动 Phase 0</strong>: 我从
benchmark_cases 里选 3 道题, 让当前的 13 位灵魂答一遍, 打个分, 拿到
我们的 baseline。

---

## 不在本计划范围

- 微调 (L1) — 性价比不足, 推后讨论
- 板块 / 主题 panel 训练 — 单独立项
- 外部已训练投资人 agent (例如 ChatGPT marketplace 上他人的 "Buffett
  GPT") 接入 — 单独立项, 也需要过 benchmark
