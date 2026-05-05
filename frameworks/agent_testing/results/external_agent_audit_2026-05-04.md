# 外部灵魂候选审计报告 (Phase A)

日期: 2026-05-04 · 审计者: souls pipeline
范围: 评估 hybrid_adoption_plan.md Phase A 中列出的外部候选

---

## TL;DR

- **buffett-perspective**: <strong>明显优于</strong>我们当前 Buffett 灵魂卡。
  应当直接 adopt (或 fork 后做小改)。
- **virattt/ai-hedge-fund**: 行业事实上的标杆项目, **43k 星 / 7.6k forks**。
  19 个 agent, 含 8 个我们没有的投资人 (Damodaran, Burry, Druckenmiller,
  Cathie Wood 等)。
- **action**: 优先 adopt buffett-perspective; 详查 ai-hedge-fund 仓库
  里的 Munger / Lynch / Fisher / Graham agent 文件作为 fork 参考。

---

## 候选 1: buffett-perspective (will2025btc)

### 元数据
- **平台**: Claude Code Skill (与我们同一平台)
- **License**: MIT (fork 友好)
- **活跃度**: 183 stars / 25 forks (中等)
- **语言**: 中文 + 英文双语
- **安装**: `git clone https://github.com/will2025btc/buffett-perspective.git
  ~/.claude/skills/buffett-perspective`
- **触发**: 中文"用巴菲特的视角"/"切换到巴菲特"; 英文"Buffett perspective"

### 内容评估

显著优于我们当前 `frameworks/investor_agents.md` 里的 Buffett 卡。具体:

| 维度 | 我们当前 Buffett 卡 | buffett-perspective |
| --- | --- | --- |
| 篇幅 | ~200 字 | ~5,000+ 字 (含示例) |
| 心智模型数量 | 5 (focus 列表) | <strong>6 (每个有原文引用 + 实际案例)</strong> |
| 决策启发式 | 0 (混在 focus 里) | <strong>8 (Safety Margin, Punch Card, Sweet Spot, Cockroach, 5-Minute, Newspaper, Too Hard 等)</strong> |
| 输出风格规范 | 无 | <strong>有 (句式结构, 词汇, 类比密度, 节奏, 确定性语调, 幽默风格)</strong> |
| 禁止元素清单 | 无 | <strong>有 ("synergies", 学术语言, 短期预测, 含糊措辞)</strong> |
| 内部矛盾承认 | 无 | <strong>有 (派生品使用, 富人税倡导 vs 避税, 公开节俭 vs 私人飞机)</strong> |
| 一手原文引用 | 0 | 多 (1965-2025 股东信范围) |
| 例子密度 | 0 个完整 case | 6+ 个完整 case (Coca-Cola 1988, IBM 2011, See's, Buy American 2008 等) |

### 对照我们 NBIS v5 输出

我们 v5 里 Buffett 灵魂的输出大概率被这个 Skill 升级 — 因为它有<em>具体
原话引用 + 显式输出格式约束 + 禁止 jargon 列表</em>。我们当前依赖模型
预训练记忆给"Buffett 风格的话"; Skill 用<em>具体源</em>约束。

### 决策

**Adopt + 小改**:
1. 安装到 `~/.claude/skills/buffett-perspective`
2. 跑一次 NBIS sanity check (跟我们 v5 对比)
3. 通过 → 修改 souls_workflow.md 第 2 步骤, Buffett 一档<em>不再
   主会话内套框架</em>, 而是 `/buffett-perspective` 调用
4. 不通过 (低概率) → 退回我们的 baseline, 但参考其 prompt 结构升级

---

## 候选 2: virattt/ai-hedge-fund

### 元数据
- **平台**: 本地 Python (Poetry), 多 LLM 支持
- **License**: MIT
- **活跃度**: <strong>43,000 stars / 7,600 forks</strong> (该领域<em>顶级</em>)
- **支持的 LLM**: OpenAI / Anthropic / Groq / DeepSeek / 本地 Ollama
- **安装**: `git clone` + `poetry install` + `.env` 设 API key

### 19 个 Agent 列表

**投资人 personas (13 个):**
1. Aswath Damodaran — 估值教父
2. Ben Graham — 价值投资祖父
3. Bill Ackman — 激进价值
4. Cathie Wood — 颠覆创新派
5. Charlie Munger — 反过来想
6. Michael Burry — Big Short 派 / 逆势深价
7. Mohnish Pabrai — Buffett 学徒
8. Nassim Taleb — 黑天鹅 / 反脆弱
9. Peter Lynch — Magellan 故事派
10. Phil Fisher — Scuttlebutt
11. Rakesh Jhunjhunwala — 印度沃伦巴菲特
12. Stanley Druckenmiller — 宏观大师
13. Warren Buffett

**功能 roles (6 个):**
14. Valuation Agent
15. Sentiment Agent
16. Fundamentals Agent
17. Technicals Agent
18. Risk Manager
19. Portfolio Manager

### 与我们 13 灵魂的对比

我们有但 ai-hedge-fund 没有 (4):
- 段永平 (中文圈, 不在英文项目正常)
- Li Lu (中文圈)
- Howard Marks
- Seth Klarman
- Terry Smith
- Joel Greenblatt
- Ray Dalio
- George Soros

ai-hedge-fund 有但我们没有 (8):
- **Aswath Damodaran** (估值方法论, 强烈建议补)
- **Bill Ackman** (激进价值)
- **Cathie Wood** (反向制衡 — 我们 panel 偏熊, 这位是 bullish 平衡)
- **Michael Burry** (深度逆势)
- **Mohnish Pabrai** (Buffett 学徒, 简化版)
- **Nassim Taleb** (黑天鹅 — 与 Klarman 互补)
- **Rakesh Jhunjhunwala** (印度市场, 暂不需)
- **Stanley Druckenmiller** (宏观, 比 Dalio 更交易)

**重要: 我们 panel 偏熊问题, ai-hedge-fund 已经解决** — Cathie Wood 是
显式 bullish 平衡。可以借鉴。

### 决策

**部分 fork 参考**, 不全盘采纳:
1. 浏览仓库 `src/agents/` 子目录, 看每个 agent 的 prompt 文件
2. 重点学:
   - Munger agent 的 prompt 设计 → 升级我们的 Munger 卡
   - Cathie Wood agent → 直接补到我们 panel (解决偏熊)
   - Druckenmiller agent → 与 Marks 对比, 决定要不要补
3. 不直接用整套, 因为它的 orchestration 是 Python 本地跑, 输出是
   trading signal, 与我们 HTML simbao + 主审制度不同

---

## 候选 3-5 (Phase A 后续)

| 项目 | 状态 | 优先级 |
| --- | --- | --- |
| [buffett-skills (agi-now)](https://github.com/agi-now/buffett-skills) | 未深查 | 中 — 可能与 buffett-perspective 重叠 |
| [Warren-Buffett-AI-Twin (jyana65)](https://github.com/jyana65/Warren-Buffett-AI-Twin) | 未深查 | 低 — 有 buffett-perspective 已足够 |
| ChatGPT Custom GPT marketplace 搜 Munger / Marks / Klarman | 未做 | 高 — 跨平台独立性的最佳路径 |

---

## 决策汇总 (Decision Matrix v1)

| 灵魂 | 当前 Tier | 路径决策 | 来源 | 优先级 |
| --- | --- | --- | --- | --- |
| Buffett | A | <strong>Adopt</strong> | buffett-perspective | P0 (立即) |
| Munger | B | Fork 参考 | ai-hedge-fund Munger agent | P1 |
| Howard Marks | A | 自建 (有 Oaktree 备忘录) 或找 GPT | — | P1 |
| Klarman | A | 自建 + 找 GPT | — | P1 |
| Greenblatt | A | 自建 (材料公开易获取) | — | P2 |
| Graham | 已逝 | Fork 参考 | ai-hedge-fund Ben Graham agent | P2 |
| Fisher | 已逝 | Fork 参考 | ai-hedge-fund Phil Fisher agent | P2 |
| Lynch | 退休 | Fork 参考 | ai-hedge-fund Peter Lynch agent | P2 |
| Terry Smith | B | 自建 (Fundsmith 年报公开) | — | P2 |
| 段永平 (主审) | C → 升 | <strong>必须自建</strong> | — | P0 (我们的核心特色) |
| Li Lu | C | 自建 | — | P3 |
| Soros | Hold | 维持框架套用 | — | P4 |
| Dalio | C | 维持框架套用 | — | P3 |
| <strong>Cathie Wood (新)</strong> | — | <strong>新增</strong> | ai-hedge-fund 或自建 | <strong>P1 (解决 panel 偏熊)</strong> |
| Aswath Damodaran (新) | — | 新增 (估值方法论强) | ai-hedge-fund 或自建 | P2 |
| Druckenmiller (新) | — | 评估 (有可能与 Marks 重叠) | — | P3 |

---

## 立即行动 (P0)

### 行动 1: 安装 buffett-perspective

```bash
# 在用户的电脑上执行
git clone https://github.com/will2025btc/buffett-perspective.git \
  ~/.claude/skills/buffett-perspective
```

安装后 Claude Code 应自动识别为可用 Skill, 触发 `/buffett-perspective`
或自然语言"用巴菲特的视角"。

### 行动 2: NBIS sanity check

安装完成后, 启动新对话:
- "用巴菲特的视角看一下 NBIS, 假设你只知道 2025-12-31 之前的信息"
- 把输出与 v5 简报里 Buffett 灵魂段落对比
- 评分维度: 来源忠实度, 框架理解, 案例应用, 边界声明, 可执行价值
  (即 rubric.md 5 项)

### 行动 3: 检查 ai-hedge-fund 关键 agent 文件

WebFetch 这些路径获取 prompt:
- `https://github.com/virattt/ai-hedge-fund/blob/main/src/agents/charlie_munger.py`
- `https://github.com/virattt/ai-hedge-fund/blob/main/src/agents/cathie_wood.py`
- `https://github.com/virattt/ai-hedge-fund/blob/main/src/agents/aswath_damodaran.py`

如果路径不准确, 浏览 `src/agents/` 目录找。

---

## 预期影响

如果 P0 三步都顺利:
- 节省 ~3 周自训 Buffett (直接采纳 buffett-perspective)
- 节省 ~2 周自训 Munger (fork ai-hedge-fund)
- 加 Cathie Wood 解决 panel 偏熊问题, 从 ai-hedge-fund 拿现成的
- 段永平和 Li Lu 仍要自建, 但因为是中文专属, 这反而是<em>我们的差异
  化优势</em>

总训练周期: 从 9-13 周压缩到 <strong>3-5 周</strong>。

---

## 风险提示

1. **buffett-perspective 可能在某些 NBIS-类型 case 上不及格** —
   它是通用 Buffett, 没针对 AI 基建场景优化。需要 Phase B sanity
   check 决定。
2. **ai-hedge-fund agent 是给 trading signal 用的**, 我们要的是
   investment memo lens — 输出格式不一致, 不能直接套用, 需要改。
3. **平台独立性目标在 P0 阶段还没解决** — 全在 Claude Code 里跑。
   ChatGPT/Gemini 端要等 Phase D。

---

下一步等用户确认是否安装 buffett-perspective 并启动 sanity check。
