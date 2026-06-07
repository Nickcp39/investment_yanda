---
title: S4 Drug Discovery AI — 段内 ranked list
segment: S4
created: 2026-05-16
status: draft-v1
companies_in_csv: 10
key_insight: 私募估值高涨 vs 公开市场冷淡的极端 disconnect 段。Insilico HK IPO (2025-12) 是 Nick 出海叙事直接相关的标志性事件。
---

# S4: Drug Discovery AI

## 段级洞察先放前面

**这一段的核心矛盾:** 私募估值 + 融资 vs 公开市场 + clinical 兑现 = **巨大 disconnect**

- 私募端: Xaira $1B Series A、Eikon ~$1.5B、Isomorphic $600M 首轮 + $3B 大药企合作 → **资金狂热**
- 公开端: Recursion (RXRX) 2025 全年营收 $74.7M，亏损 **$644M**，5 年没新里程碑 → **市场冷淡**

中间唯一走通"私募→IPO→临床数据"完整循环的: **Insilico Medicine HK IPO 2025-12-30, $293M 募资, $2.7B 市值** —— 这是 Nick 出海叙事最直接相关的事件之一。Insilico 创始人 Alex Zhavoronkov 在中港双总部模式上跑通了 IPO，且 lead 药物 (rentosertib for IPF) 是 **唯一一个 AI 设计药物拿到 Phase 2 阳性数据** 的案例。

---

## 段级数据（2025-2026）

| 指标 | 数值 | 来源 |
|------|------|------|
| 段内累计私募融资 (since 2018) | **$10B+** | OnHealthcare Tech 2026 |
| 段内 2025 mega round 数 | 5+ rounds > $200M | OnHealthcare |
| 段内 IPO 标志 | Insilico HK IPO 2025-12 $293M (largest HK biotech IPO 2025) | HKEX |
| 公开市场最大公司营收 | Recursion $74.7M (2025) | 10-K |
| 公开市场最大公司亏损 | Recursion -$644M (2025) | 10-K |
| 公开市场最大公司 cash runway | Recursion $754M (EOY 2025) | 10-K |
| 段内 Phase 2 阳性 AI 设计药数 | 1（Insilico rentosertib for IPF）| PR |
| 段内 FDA 已批 AI 设计药数 | **0** | FDA |

**关键洞察:** 段内**还没有任何一款完全 AI 设计的药物拿到 FDA 批准**。所有估值都是 betting on 5-10 年后 pipeline 兑现。这是和 S1/S5 完全不同 risk profile 的段——**前者赌产品商业化，后者赌技术 R&D 兑现**。

---

## Ranked list（10 家）

### Tier 1: 大旗舰 ($500M+ raised) - 私募狂热

| # | 公司 | 国家 | 估值/市值 | 总融资 | 模型 lane | 关键事件 |
|---|------|------|----------|--------|-----------|----------|
| 1 | **Eikon Therapeutics** | US | ~$1.5B (incl. post-IPO) | $1.5B | live-cell phenomic + ML | IPO'd 2025 |
| 2 | **Xaira Therapeutics** | US | $1B+ | **$1.3B** ($1B Series A) | foundation model for biology (RFdiffusion + 多组学) | 史上最大 Series A 之一 (2024-04) |
| 3 | **Isomorphic Labs (Alphabet)** | US | (internal) | $600M (first external 2024) + $3B in Lilly/Novartis collab value | structure foundation model (AlphaFold 商业化) | 2024 首轮外部融资 |
| 4 | **insitro** | US | undisclosed | $643M | ML-driven biology + phenomics | Gilead/BMS collabs |
| 5 | **Valo Health** | US | undisclosed | $450M+ | Opal platform: human data → drug design | Novo Nordisk $4.6B milestone deal |

### Tier 2: 中型 + 已上市

| # | 公司 | 国家 | 估值/市值 | 总融资 | 状态 | 关键事件 |
|---|------|------|----------|--------|------|----------|
| 6 | **Insilico Medicine** | China/US (HK HQ) | **$2.7B** (HKD 20.7B 市值) | $500M private + $293M IPO | **PUBLIC HK 3696.HK Dec 2025** | 首个 HKEX Ch 8.05 AI biotech IPO; rentosertib Phase 2 阳性 (IPF) |
| 7 | **Recursion (RXRX)** | US | (NASDAQ) | public ($1B+ raised pre-IPO) | PUBLIC NASDAQ | 2025 营收 $74.7M (+27% YoY), 亏损 -$644M, cash $754M。曾合并 Exscientia |
| 8 | **Genesis Therapeutics** | US | undisclosed | $280M ($200M Series B) | private | gen chem + structure modeling |
| 9 | **AbCellera (ABCL)** | Canada | (NASDAQ) | public | PUBLIC NASDAQ | 抗体发现 AI；多个 partnership |
| 10 | **Cradle Bio** | Netherlands | undisclosed | $73M Series B | private | AI protein design (类似 RFdiffusion); 欧洲 |

---

## 段内深度分析

### 三大技术路线（"lane"）

按 OnHealthcare Tech 2026 分类，AI drug discovery 头部公司可分三个 lane：

| Lane | 描述 | 代表公司 |
|------|------|----------|
| **Structure foundation model** | 蛋白结构 → 设计分子 (类似 AlphaFold) | Isomorphic Labs, Chai Discovery, Cradle, Xaira (混合) |
| **Biology data + phenomics** | 大规模细胞实验 → ML 发现 phenotype | insitro, Recursion, Eikon |
| **Translational + generative chemistry** | 化学空间生成 + 临床转化 | Iambic, Genesis Therapeutics, Insilico |

每个 lane 有自己的 thesis 和风险，不能简单类比。**Insilico 是 lane 3 唯一走通 Phase 2 的**，因此其他 lane 的"5-10 年后能成"还是 hypothesis。

### 私募估值 vs 公开市场冷淡的解释

私募端为什么这么贵：
- LP（big pharma + sovereign + Tier 1 VC）赌的是 10-15 年后的"如果 AI drug discovery 成立，前 5 家拿走全部价值"，所以宁愿过付
- Big pharma 的 partnership 实质是变相 R&D outsourcing（Eli Lilly + Isomorphic $1.7B、Novartis + Isomorphic $1.2B）
- 退出预期不是 IPO 而是被大药企**整体收购**（类似 Genentech、Schrödinger 路径）

公开端为什么冷淡：
- Recursion 上市 4 年没新里程碑、亏损放大、cash burn rate 高
- 投资者对"how does AI fundamentally make drug discovery faster"的证据要求越来越严
- Pfizer / Merck 这种 incumbent 都开始内部建 AI 团队，外部 partnership 议价权下降

### Insilico HK IPO 是分水岭

**对全行业的含义:** 第一次有 AI biotech 通过"中国市场友好"的退出路径，且**lead asset 已有 Phase 2 数据**。
**对 Nick 的含义（特别重要）:**

- Insilico 是 **中港双总部 + AI + biotech** 模式 ← 和 Nick 想做的"中国 AI 医疗设备出海"高度同构（只不过 imaging 是 device，Insilico 是 biotech）
- Insilico 创始人 Alex Zhavoronkov 在俄罗斯出生、约翰霍普金斯 PhD、HK 长期生活 → 是 "全球化 AI 科学家"的典型 profile，可参考 path
- Insilico 上海 + 蒙特利尔 + 阿布扎比 + 波士顿 → multi-shore strategy 不是 idea 是 reality
- HK Ch 8.05 IPO 路径 → 给后续中国 AI medical 公司（包括 imaging）提供了 IPO 模板

### 风险信号

- **Recursion 这种已 IPO 但持续 burn 的公司可能成为 segment cautionary tale** — 如果未来 12 个月不出新里程碑，估值还会跌
- **AI drug discovery 整体 thesis 风险:** 如果 5 年内没有 ≥3 款 AI 设计药拿到 Phase 3 阳性，整个段融资会大幅收缩。当前只有 Insilico rentosertib Phase 2，是孤证
- **Big pharma 内部化威胁:** Pfizer / Merck / J&J / GSK 都在建内部 AI 团队，对外部 startup 议价权下降
- **AlphaFold + Med-Gemini 等开源 / 平台模型威胁:** structure prediction 这件事正在变成 commodity，模型 moat 在迅速消失。Isomorphic 这种基于 AlphaFold 商业化的公司护城河被自家亲戚（Google）冲刷

### 中国可映射性: **中-高**（不同子赛道差别大）

| 美国公司 | 中国对应 | 备注 |
|---------|----------|------|
| Insilico Medicine | 自己就是中国（HK） | **不需要 map，直接看 Insilico** |
| Recursion | 晶泰科技 (XtalPi, HK 上市) | 晶泰已 HK 上市 |
| Isomorphic Labs | 阿里达摩院/华深智药、深度智耀 | 不成熟 |
| Genesis Therapeutics | 燃石医药、英矽智能（与 Insilico 关联）| 部分重叠 |
| Xaira | 国内尚无对应规模玩家 | 资金体量差距大 |

**Nick entry paths (S4):**
1. **Insilico Medicine 上海/苏州团队** —— effort: 中。如果你想拿"中国 AI biotech 上市公司"的履历，这是最直接 entry。但你的 imaging 背景不是 perfect match，需要 reskill biology
2. **晶泰科技 (XtalPi)** —— effort: 中。HK 上市，深圳/上海团队，背景近似
3. **华深智药 / 深度智耀** —— effort: 低-中，但赛道较小
4. **加入西方 AI biotech 中国办公室**（如 Recursion 中国，如有）—— effort: 高，不确定是否存在
5. **建议:** S4 对 Nick **不是主线**。biology + AI 路径会让你放弃 imaging 积累 + 重新 reskill，机会成本太高。但 **Insilico 是值得 follow 的 case study**（你的中港双总部 + 出海叙事在 Insilico 身上已有验证）

---

## Nick 视角：S4 段对你职业决策的含义

**简短结论:** S4 不是 Nick 的主线（biology reskill 成本高），但 **Insilico Medicine 是 case study of choice** —— 它已经在 Nick 想做的事情上走通了一遍：
1. ✅ 中港双总部架构
2. ✅ AI + 医疗（虽然是 biotech 不是 device）
3. ✅ HK IPO 出海退出
4. ✅ 第一款 AI 产品拿到 Phase 2 数据

如果 Nick 未来要做"中国 AI 医疗设备出海 + IPO"，**Insilico 是 唯一一个 already done it 的范本**。Phase 4 elevator map 必须把 Insilico 作为锚点参照。

---

## 数据补充建议

- Insilico Alex Zhavoronkov 详细个人 path（俄罗斯 → JHU → HK）→ 可能作为 Nick 的 personal mentor mapping
- 晶泰科技 XtalPi HK IPO 数据
- Big pharma 内部 AI 团队规模（Pfizer / Merck）→ 用于 "外部 startup 议价权下降" thesis 量化
- 中国国内 AI biotech 二线：英矽智能不是中文名（Insilico 中文是英矽智能本人）、深度智耀、华深智药、星亢原

## 来源
- [OnHealthcare Tech - AI Drug Discovery Capital Stack 2026](https://www.onhealthcare.tech/p/the-ai-drug-discovery-capital-stack)
- [FierceBiotech - Xaira $1B funding](https://www.fiercebiotech.com/biotech/new-ai-drug-discovery-powerhouse-xaira-rises-1b-funding)
- [Insilico - Hong Kong IPO 2025-12-30](https://insilico.com/news/p010170up1-insilico-medicine-lists-on-hong-kong-sto)
- [Pharmaphorum - Insilico $293M HK IPO](https://pharmaphorum.com/news/insilico-ends-2025-293m-hong-kong-ipo)
- [Bloomberg - Insilico HK debut](https://www.bloomberg.com/news/articles/2025-12-30/ai-drug-firm-insilico-debuts-in-hong-kong-after-293-million-ipo)
- [Recursion - Q3 2025 financial results](https://ir.recursion.com/news-releases/news-release-details/recursion-reports-third-quarter-2025-financial-results-and)
- [stockanalysis - RXRX revenue history](https://stockanalysis.com/stocks/rxrx/revenue/)
- [Valo Health - Novo Nordisk expanded agreement](https://www.valohealth.com/press/valo-health-and-novo-nordisk-expand-collaboration-to-discover-and-develop-novel-treatments-for-cardiometabolic-diseases)
