---
title: S2 Clinical Decision Support / Medical LLM — 段内 ranked list
segment: S2
created: 2026-05-16
status: draft-v1
companies_in_csv: 7
key_insight: OpenEvidence 是整个 healthcare AI 增长曲线最陡的公司（2024 → 2025 ARR 19x），可能是过去 5 年最重要的单一案例研究对象
---

# S2: Clinical Decision Support / Medical LLM

## 段级洞察先放前面

**OpenEvidence 是这一段、也可能是整个 healthcare AI 过去 5 年最重要的单一案例:**
- 2024 ARR: $7.9M
- **2025 ARR: $150M（YoY +1,803%, 即 19x）**
- 2026-01 估值: $12B (Series D $250M)
- **40% of US physicians 已注册使用**（760K 人）
- 18-20M clinical consultations / 月
- 90% 毛利率
- **商业模式: pharma + medtech 定向广告**, CPM $70-$1000+（社交媒体只 $5-15），ARPU ~$124

这是 software 历史上少有的增长曲线。同时也回答了一个 long-standing 问题：**医生愿意用 AI 做什么** —— 答案是"医疗参考查询和临床决策辅助"，而且**愿意用免费版**（OpenEvidence 对医生免费，靠 pharma 广告收钱）。

---

## 段级数据（2025-2026）

| 指标 | 数值 | 来源 |
|------|------|------|
| 段头部 OpenEvidence ARR | **$150M (2025)**, 19x YoY | Sacra |
| 段头部 OpenEvidence 估值 | **$12B** (Jan 2026 Series D) | CNBC, PitchBook |
| 段头部 Hippocratic AI 估值 | $3.5B (Nov 2025 Series C) | BusinessWire |
| 段头部 Hippocratic 累计客户 | 50+ health systems, 6 国, 1000+ use cases, 115M+ patient interactions | BusinessWire |
| US 医生总数 | ~1.1M (active) | AMA |
| OpenEvidence 渗透率 | **~40%** | CNBC interview Daniel Nadler |

**关键对比:** OpenEvidence 用 4 年 (founded 2022) 渗透到 40% US 医生，比 Abridge (2018 founded) 在大型 health system 35% 渗透率还快。两者都是 healthcare AI 史上最快的渗透曲线之一。

---

## Ranked list（7 家）

### Tier 1: $3B+ 估值 absolute 头部

| # | 公司 | 估值 | 总融资 | 业务 | 客户/用户 |
|---|------|------|--------|------|----------|
| 1 | **OpenEvidence** | **$12B** | $735M | "ChatGPT for doctors" — 临床证据问答 + 医疗参考 | 760K 注册 US 医生 (40% 全国), 18-20M/月 consults |
| 2 | **Hippocratic AI** | $3.5B | $404M | 非诊断 patient-facing AI agents (慢病管理、用药、出院随访) | 50+ health systems / 6 countries / 1000+ use cases / 115M+ interactions |

### Tier 2: 中型 / 长尾

| # | 公司 | 估值 | 总融资 | 业务 |
|---|------|------|--------|------|
| 3 | **Glass Health** | undisclosed | seed/A | AI 临床决策支持 + ambient scribe 混合。客户 Harvard / Stanford / Hopkins |
| 4 | **Atropos Health** | undisclosed | A | agentic real-world evidence。Stanford Health Care 部署。Microsoft Dragon Copilot 集成 |
| 5 | **Counsel Health** | undisclosed | seed | AI triage / patient routing |
| 6 | **Doctronic** | undisclosed | seed | AI triage / symptom assessment |
| 7 | **Pieces Technologies** | undisclosed | A | clinical evidence aggregation (smaller) |

---

## 段内深度分析

### OpenEvidence 商业模式 deep dive

**这是过去 5 年最值得研究的医疗 AI 商业模式之一**，原因：

| 维度 | 传统 SaaS | OpenEvidence |
|------|----------|-------------|
| 付费方 | 医院/医生（钱包薄+决策慢）| **Pharma / Medtech** (钱包厚+决策快) |
| ARPU | $2-4k/医生/年 (Abridge 类) | $124/医生/年 (隐含)，但增长无上限 |
| 触达 | 需医院 IT 部门 procurement | 医生**自助**注册，绕过 IT |
| 毛利 | 60-70%（SaaS 平均）| **90%** (广告模型) |
| 增长上限 | 医生数 × ARPU × NRR | 医生数 × pharma 广告 budget |
| 替代品 | Up-to-Date 这类静态参考 | Up-to-Date $4.6B 估值是上限标杆 |

**核心 insight:** OpenEvidence 把医疗 AI 从"卖软件给医院"变成"医生注意力的 marketplace"。前者是 healthcare 商业模式，后者是 **Google + Facebook 模式**。这就是为什么估值倍数 $12B / $150M = **80x ARR**，远超 SaaS 标准。

### 商业模式的中国可移植性 (Nick 关注)

**直接抄 OpenEvidence 模式在中国**：

| 因素 | 美国 | 中国 |
|------|------|------|
| 医生数量 | 1.1M | **4.5M+** (4x 美国) |
| 医生用 AI 工具的接受度 | 中高 | **极高**（中国医生短视频/微信学医习惯重）|
| Pharma 营销支出 | $30B/年 | ~$20B/年 |
| Pharma 营销监管 | 严，但允许付费医学教育 | **严，2024 后受 CSO 规整**，付费内容受限 |
| 类似产品 | OpenEvidence | 用药助手、丁香园、新青年麻醉论坛 (前数字时代版本) |
| 大模型基础设施 | OpenAI GPT-4/5 | DeepSeek / 字节 / 阿里 / 智谱 |

**中国可能的入局者:**
- 字节豆包医疗版 (内部产品，未独立)
- 阿里通义 + 阿里健康
- 腾讯觅影 + 腾讯医典
- DeepSeek 医疗版本（推测）
- 丁香园 (Dingxiangyuan, ChunYu) — 已有用户基础

**Nick 视角:** 这一段在中国本质上是 **LLM 大厂 vs 医疗内容老牌平台** 的对决，**不是新创业公司的赛道**。Nick 进入这一段最直接的路径不是加入 startup，而是加入字节/阿里/腾讯/DeepSeek 的医疗 AI 团队 — 但那是 LLM 工程岗，对 leetcode + system design 要求高，**Nick profile 不是 perfect match**。

### Hippocratic AI 模式

**和 OpenEvidence 不同的路径**：
- 不做医生入口，做 **patient-facing agents**（非诊断，自动化护理）
- 替代的是 nurse / social worker / nutritionist，不是 physician
- 商业模式: 按 health system enterprise 卖（per-agent / per-conversation）
- 风险：临床安全要求极高，agentic AI 出错的责任归属未明确

**对 Nick 的含义:** Hippocratic 模式在中国可移植性**更高**，因为中国基层医疗人手缺乏比美国还严重，AI 替代护士/营养师在政策上有支持（"分级诊疗"国家战略），落地阻力小。但创业窗口已经不在了 — 字节/阿里都在做。

### 风险信号

- **OpenEvidence pharma 广告依赖度:** 90% 毛利来自 pharma 广告。如果 FTC / FDA 收紧医疗 AI 中的 promotional content 监管，模式有风险。Daniel Nadler 是 Kensho 创始人（$700M+ 退给 S&P），他知道 PMF + 退出，是大概率事件。但 IPO 前估值已 $12B → IPO 想再翻倍很难
- **Hippocratic AI agentic safety risk:** 第一例临床事故（即便不是 agent 直接致死，相关）将引发监管大幅收紧
- **Glass Health 这种中型:** 在 OpenEvidence 和 Hippocratic 夹击下，很可能被边缘化或被收购
- **段 vs S1 的边界:** Glass Health 同时做 ambient scribe + CDS，类似 Ambience Healthcare。"horizontal" 公司可能在两个段都不是 #1。但 #1 玩家也可能反过来吃掉 horizontal 玩家 (Abridge 已在做 scribe + RCM)

### 中国可映射性: **中高**

| 美国公司 | 中国对应 | 备注 |
|---------|----------|------|
| OpenEvidence | 字节豆包医疗 / DeepSeek 医疗 / 丁香园 + 大模型 / 用药助手 | 没有 1 对 1 startup，是大厂内部赛道 |
| Hippocratic AI | 京东健康 / 平安好医生 + LLM / 腾讯医典 | 中国 patient-facing AI 由互联网医疗巨头做 |
| Glass Health | 大模型团队的医疗 vertical | 通常不是独立公司 |
| Atropos Health | 中国 RWE 工具市场较弱 | 因为中国 RWE 监管不完善 |

**Nick entry paths (S2):**
1. 字节豆包 / 阿里通义 / DeepSeek 医疗 vertical（如果他们做） — effort: 高（leetcode 关卡），但 profile match 不差
2. 京东健康 / 平安好医生 AI 部门 — effort: 中，但你的 PhD 价值被压低
3. 春雨医生 / 微医 + LLM 创业 — effort: 低，但赛道天花板低
4. 直接加入字节医疗或 DeepSeek 等内部团队 — effort: 高
5. **建议:** S2 不是 Nick 的主线，作为"如果 S5 出海路径不通的 plan B" — 但 leetcode 短板会成为 binding constraint

---

## Nick 视角：S2 段对你职业决策的含义

**简短结论:** S2 是 LLM 大厂的赛道，不是 Nick 这种 imaging + 硬件背景的赛道。

虽然 OpenEvidence 的故事极其性感（19x ARR 增长），但底层 capability 是 **medical LLM + 搜索算法 + 广告变现**，Nick 在这三件事上没有显著优势。强行进入 S2 等于在 LLM 工程师军备竞赛里跟字节/DeepSeek/OpenAI 直接竞争，battle 不在他主场。

**但 S2 段对 Nick 仍有 2 个间接价值:**

1. **作为投资视角的 thesis:** 如果你以后想给中国 LLM 大厂的 medical vertical 做职业判断（"字节医疗 vs 阿里医疗哪个会赢"），OpenEvidence 模式是必读的参照系
2. **作为 S5 (imaging) 的相邻威胁:** medical foundation model 未来可能侵蚀 narrow imaging AI 公司的市场（Annalise.ai 这种"100+ findings 综合 AI"和 medical LLM 重合度高）。理解 S2 帮助 Nick 评估 S5 公司哪些会被 LLM 冲击、哪些不会（HeartFlow 因为 hardware/CT-FFR 物理建模，不会；Aidoc 急诊 triage 部分可能被替代）

---

## 数据补充建议

- Daniel Nadler (OpenEvidence CEO) 详细背景 (Kensho 退出 + Harvard PhD) → 写入 founders_background
- Hippocratic AI 创始人 Munjal Shah 背景
- 中国 LLM 大厂的 medical vertical 估值/投入（Phase 3 详填）
- 美国 medical foundation model 玩家 (Med-Gemini, Med-PaLM, Anthropic medical) → 段内未覆盖，可能需要新增子段或列入 S2 Tier 1.5

## 来源
- [Sacra - OpenEvidence revenue & valuation](https://sacra.com/c/openevidence/)
- [CNBC - OpenEvidence $12B Series D 2026-01](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html)
- [TechCrunch - OpenEvidence $200M @ $6B 2025-10](https://techcrunch.com/2025/10/20/openevidence-the-chatgpt-for-doctors-raises-200m-at-6b-valuation/)
- [Fierce Healthcare - OpenEvidence $250M Series D](https://www.fiercehealthcare.com/ai-and-machine-learning/openevidence-clinches-250m-series-d-rapidly-growing-its-reach-doctors)
- [BusinessWire - Hippocratic AI Series C $126M @ $3.5B](https://www.businesswire.com/news/home/20251103432446/en/Hippocratic-AI-Raises-$126-Million-in-Series-C-at-$3.5-Billion-Valuation-Led-by-Avenir-Growth-to-Expand-Clinically-Safe-Generative-AI-Agents-Across-Healthcare)
- [Fierce - Hippocratic AI Series B $141M unicorn](https://www.fiercehealthcare.com/ai-and-machine-learning/hippocratic-ai-banks-141m-series-b-hits-unicorn-status-it-rolls-out-ai)
- [Fierce - Atropos Health Stanford agentic](https://www.fiercehealthcare.com/ai-and-machine-learning/atropos-health-launches-agentic-ai-clinical-evidence-stanford-health-care)
