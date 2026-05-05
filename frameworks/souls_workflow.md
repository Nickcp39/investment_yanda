# 灵魂 Pipeline (Souls Workflow)

公司 / 板块研究的标准流程。一次走完产出一份 HTML 简报 + 一个持久化的
memory 文件。下次回到同一标的, 不用从头再来。

设计参考: [TradingAgents](https://github.com/tauricresearch/tradingagents)
的 role 结构 + [FinMem](https://github.com/pipiku915/FinMem-LLM-StockTrading)
的 layered memory + [Du et al. Multi-Agent Debate](https://composable-models.github.io/llm_debate/)
的 critique 一轮。但精简到人脑能记住的程度。

---

## 核心 5 灵魂 (Core Panel)

每次都跑这 5 位。覆盖 5 个不可缺的视角:

| 灵魂 | Role 对应 | 一句话职责 |
| --- | --- | --- |
| **Warren Buffett** | Fundamentals | 业务质量 + 管理层 + owner earnings |
| **Howard Marks** | Cycle / Sentiment | 市场已经相信什么? 周期位置? 非对称? |
| **Charlie Munger** | Risk · Inversion | 反过来想 — 这事怎么会死? |
| **Seth Klarman** | Risk · Downside | 最坏情况亏多少? 安全边际? |
| **段永平 (Chair)** | Portfolio Manager | 综合 + 不为清单 + 100% 私有化测试 |

为什么是这 5 位:
- 都是<em>当下还活跃</em>的投资人 (Munger 2023 逝, 但 2024 前还在公开发言)
- 5 个独立维度, 角色不重叠
- 1 位主审避免 N 个独白没结论
- 5 位是人脑能记住的极限, 13 位会变噪音

## 扩展灵魂 (Extension Roster) — 按需触发

只在<em>核心 5 位指出特定缺口</em>时才请。否则不出场。

| 触发条件 | 召唤的灵魂 |
| --- | --- |
| Buffett 说"信息不够判断管理层" | **Li Lu** (信息完整性 70-80% 门槛) + **Fisher** (scuttlebutt 5 类) |
| Marks 说"高速增长不知是 alpha 还是 beta" | **Lynch** (fast grower 分类) + **Terry Smith** (quality compounder 三关) |
| Munger 说"反身性循环正在跑" | **Soros** (boom-bust 位相 + 退出规则) |
| 标的高度宏观敏感 (利率/汇率/regime) | **Dalio** (4 regime 矩阵) |
| 想做量化筛选起点 | **Greenblatt** (Magic Formula) |
| 标的破产边缘 / 净资产折扣 | **Graham** (跑道 + asset coverage) |
| 用户加入第一手观察 | 切换 Dialog 模式, 灵魂直接回应 |

## 6 步流程

```
Step 0: 资料归集 (10-30 min)
  ↓
Step 1: 信息完整度审计 (5 min)  ← Li Lu / Fisher 视角
  ↓
Step 2: 核心 5 灵魂初评 (15 min)
  ↓
Step 3: 一轮 critique (10 min)  ← 新增, 防止独白
  ↓
Step 4: 主审综合 + verdict (10 min)
  ↓
Step 5: 落盘 + memory 更新 (5 min)
```

总耗时: 一份完整简报 ~50-75 分钟。

### Step 0 — 资料归集

读: 仓库 `notes/videos/` 中所有提到该 ticker 的文件 + 必要的 1-3 次
WebSearch (优先一手 IR / SEC, 其次 B 级媒体, 最后 C 级评论)。

每条事实<em>必须</em>带 source tier 标签 (按 `sources/source_policy.md`):
- **A 级**: 公司一手 (10-K/Q, 8-K, 投资者 deck, 财报 transcript)
- **B 级**: 高质量二手 (Bloomberg / Reuters / WSJ / Moscow Times 全文)
- **C 级**: 市场评论 / 博主 / 论坛

输出: `companies/<ticker>/facts.md` (累积式, 每次研究都追加)。

### Step 1 — 信息完整度审计

请 Li Lu + Fisher 两位先发声 (不算入决策 panel)。他们只回答两个问题:

- **Li Lu**: 当前信息完整度 % (考虑非美国公司治理折扣需要 80%+)
- **Fisher**: scuttlebutt 5 类 (客户/供应/竞品/前员工/开发者) 各完成
多少?

如果完整度 <40% 或关键 scuttlebutt 类全缺, **回到 Step 0 补料**。
不要在低完整度上跑 panel 给伪 verdict。

### Step 2 — 核心 5 灵魂初评

每位灵魂出一段 ~150 字的<em>结构化</em>判断 (不是 v2-v5 那种长独白):

```
[Soul Name]
- Verdict: REJECT / WATCH / STARTER / CORE / SKIP / INFO-GAP
- 一句理由:
- 一条引用 (该灵魂 1-2 年内公开发言或具体行动) — 必须真实可考证
- 一条对该 ticker 的具体应用:
```

输出格式短促, 不是为了显得权威, 是为了让 Step 3 的 critique 能<em>具体
反驳</em>。

### Step 3 — 一轮 Critique (这是关键新增步骤)

Du et al. 论文的核心发现: 单 agent 各自独白 ≠ 协同推理, 必须有<em>显式
反驳</em>才能改善准确性。我们做<em>一</em>轮 (不多轮, 多轮收益递减):

```
Marks → critique Buffett:
  "你说的 owner earnings 维度市场已经定价了多少?"

Munger → critique Marks:
  "时机判断本身就是 Charlie 反复警告的事 — 你怎么避免变成 market timer?"

Klarman → critique Munger:
  "反过来想三大失败路径 OK, 但我管钱看价格 — 当前价位补偿了这些尾部
   风险吗?"

段永平 → critique all:
  "你们 4 位都假设懂这门生意 5-10 年。我先问 — 真懂吗?"
```

每位被反驳后给一段 50-100 字的回应, 可以坚持原立场或修订。Verdict 修订
带箭头标记 (↑/↓/→)。

### Step 4 — 主审综合

段永平作为 Chair:
- 综合 Step 2-3 的发声
- 套"不为清单" 4 项 + "100% 私有化测试" 4 个不能确信
- 给出 final verdict (REJECT / WATCH / STARTER 1-3% / CORE 5%+ / INFO-GAP)
- 列出 3-5 条 Kill Criteria + 监控触发器

注意: 段永平的最终 verdict 可以与多数票<em>不一致</em>。这是 Chair 制
设计意图 — 多数票噪音, 主审纪律。

### Step 5 — 落盘 + Memory

输出两份文件:

**简报 (HTML)**: `companies/<ticker>/brief-v<N>.html`
- 沿用 NBIS v3-v5 视觉风格 (chair banner / weight tier / verdict pills)
- 标记版本号 (vN), 不覆盖旧版本

**Memory (Markdown)**: `companies/<ticker>/memory.md`
- 这是 FinMem 风格的<em>分层记忆</em>, 下次研究同一标的从这里开始
- 结构见下方模板

```markdown
# <Ticker> Memory

最后更新: <date> · 简报版本: v<N> · 主审 verdict: <verdict>

## 长期 (变化慢)
- 创始人 / 管理层画像
- 业务模型本质
- 行业结构性 thesis

## 中期 (季度更新)
- 最新季报关键数字
- 已签合同 / 大客户名单
- 资产负债表节奏 (capex / 现金 / 稀释)

## 短期 (1-3 月)
- 最近一次股价 boom/bust 事件
- 最近一次叙事变化 (媒体口径)
- 当前 panel 立场分布

## Kill Criteria (跟踪状态)
- [ ] 触发 1: <描述> · 状态: 未发生 / 部分 / 已发生
- [ ] 触发 2: ...

## 监控源
- IR / 财报路径
- 关键媒体 (谁的报道值得追)
- 关键 X account / 雪球 ID
```

下次回到同一 ticker:
1. 读 `memory.md` (1 分钟)
2. 跑差量调研 (新季报 / 新事件)
3. 直接进 Step 2 跑 panel — 不重头再来

---

## 文件树

```
companies/
  <ticker>/
    facts.md         # 累积事实库 (source-tiered)
    memory.md        # 分层记忆 (覆盖更新)
    brief-v1.html    # 历次简报 (保留)
    brief-v2.html
    ...
```

旧的 `companies/_template.md` 仍保留用作单文件式简报的模板, 但<em>新
研究默认走 souls pipeline</em>。

---

## 何时<em>不</em>用这个 pipeline

- **快速看一眼**: 直接问灵魂中的某 1-2 位即可, 不必跑全流程。例如:
"用 Marks 视角看一下 BTC 当前周期位置" — 不开 panel。
- **明确不在能力圈**: 段永平直接说"不为", 不需要 5 灵魂背书。
- **板块 / 主题分析**: 这套是为<em>单标的</em>设计的。板块用另一套
(以后写)。

---

## 与文献 SOTA 的差距 (诚实)

我们做了什么 vs 没做什么:

| 维度 | 学术 SOTA | 我们做了 | 我们没做 |
| --- | --- | --- | --- |
| 角色划分 | TradingAgents 7 角色 | 核心 5 + 扩展 (角色 + 人格混合) | — |
| 多轮辩论 | Du et al. 多轮 | 1 轮 critique (够用) | 多轮迭代 |
| 分层记忆 | FinMem 模块 | `memory.md` 分长/中/短期 | 真正的 RAG 索引 |
| 工具独立 | 每 agent 专属工具 | 全 share 我提供的事实 | — |
| Agent 独立 | 不同上下文跑 | 全是一个作者 (我) | 这个根本问题不解决 |
| 基准测试 | 论文有 SHAR/IR/win rate | `agent_testing/` 已设计 | 还没真正跑过 |

最大的<em>方法论债务</em>: souls 全是我一个人写的, 共识是假的。这要等
接入外部 trained agent (ChatGPT GPTs / Claude Projects 训练好的"巴菲特")
才能根本解决。当前流程是<em>过渡形态</em>。

---

## 升级路径 (按优先级)

1. **当前 (v1)**: 5 步 + 5 灵魂 + 1 轮 critique + memory.md
2. **下一步 (v2)**: 把 `agent_testing/` benchmark 真正跑起来,
   在每次新研究前 sanity check 灵魂没漂移
3. **v3**: 接入 1-2 个外部 trained agent (例如 ChatGPT GPT 上有人
   做的 Buffett bot), 跑同一题, 看输出差异
4. **v4**: 板块 / 主题级 pipeline (多标的对比)
5. **v5**: 投资组合级 pipeline (跨 watchlist 综合)

---

## 例子: 用这个 pipeline 重做 NBIS 大概是什么样

如果今天从零开始, 不是 5 版迭代:

- **Step 0**: 1.5 小时通读 11 个视频 + 3 次 web 调研 → `companies/nbis/facts.md`
- **Step 1**: Li Lu 说完整度 60%, Fisher 说 scuttlebutt 完成 1.5/5
  → 信息够下初步 verdict 但不够 STARTER
- **Step 2**: 5 灵魂各 ~150 字: Buffett 拒绝 / Marks 观望 /
  Munger 观望 / Klarman 观望 / 段永平 (initial) WATCH
- **Step 3**: critique 一轮, Klarman 因 EBITDA 转正从拒绝降观望;
  其他坚持
- **Step 4**: 段永平: WATCH (个人 0%, panel 接受 STARTER 1-3% 边界);
  Kill Criteria 5 条
- **Step 5**: `companies/nbis/brief-v5.html` + `memory.md`

总时间: ~1.5-2 小时, 一次到位。当前的 v1-v5 演化是因为<em>没有这个
pipeline</em>导致的反复迭代。下一家公司应该 1 次走完。
