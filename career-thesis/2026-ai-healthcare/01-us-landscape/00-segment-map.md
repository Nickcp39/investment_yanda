---
title: US AI Healthcare 子赛道地图（Phase 1 Block 1.0 输出）
created: 2026-05-16
status: draft-v1
sources_dated: 2025-Q4 to 2026-Q1
purpose: 在深挖单个子赛道之前，先把美国 AI 医疗 2025-2026 的整体资金流向和子赛道排序定下来
---

# US AI Healthcare 子赛道地图

## 一、市场总览（2025 全年数据）

| 指标 | 2025 | 2024 | YoY |
|------|------|------|-----|
| US digital health 总融资 | **$14.2B** | $10.5B | **+35%** |
| 总 deal 数 | 482 | — | — |
| AI-enabled 占总融资比例 | **54%** | 37% | +17pp |
| H1 2025 AI 占比 | **62%** | — | — |
| 平均 deal size | $29.3M | $20.7M | +42% |
| Mega rounds ($100M+) 占比 | 42% | ~22% | 接近翻倍 |
| 新 unicorns 数量 | 15 | 6 | +150% |
| Series C AI 溢价 | +61% deal size | — | — |

**核心叙事:** 钱不仅没少，反而创 2022 以来新高，但 **极度集中**——前 9 家拿掉就让总融资跌破 2024 水平。AI-native 公司在抢光所有大额份额，pandemic 一代非 AI 公司被困在 600+ 家"无 follow-on"的失业池里。

来源: [Rock Health 2025 year-end](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/)

---

## 二、子赛道分类（7 个 + 1 个观察项）

按 2025 资金流入和成熟度排，**热度从高到低**：

### 🔥 S1. Clinical Documentation / AI Scribe（最热）

**这是 healthcare AI 2025 的第一个 breakout category。**

- **段内 2025 收入估算:** ~**$600M**（行业总收入），YoY **2.4x**
- **代表公司:**
  | 公司 | 估值 | 总融资 | 核心客户 |
  |------|------|--------|----------|
  | Abridge | $5.3B | $800M+ | Kaiser (24.6k MD)、Mayo、Hopkins、Duke、UPMC、Yale |
  | Nabla | $5.3B | ~$316M | 中型医院系统 |
  | Ambience Healthcare | $1.04B | $243M (Series C) | health systems |
  | Suki AI | undisclosed | $165M | smaller practices |
  | Nuance DAX | (Microsoft) | acquired $19.7B | 全行业 |
  | DeepScribe / Augmedix / Heidi | smaller | — | 中小型 |
- **付费方:** 医院系统直接付费（per-MD 订阅，年均 $2–4k/MD），不靠保险
- **moat:** EHR 集成深度 + 大型 health system 数据/feedback flywheel
- **风险信号:** Abridge 50x ARR multiple，资本市场已定价 RCM 扩张（从 scribe 扩到 coding/billing/RCM），如果扩张不及预期会有显著回调

### 🔥 S2. Clinical Decision Support / Medical LLM

- **代表公司:**
  | 公司 | 估值 | 总融资 | 业务 |
  |------|------|--------|------|
  | OpenEvidence | **$12B** | ~$735M | 医生用的 AI medical search engine，capital efficiency 全段第一（16.3x）|
  | Hippocratic AI | $3.5B | $404M+ | patient-facing AI agents (scheduling, adherence) |
  | Glass Health | smaller | — | clinical reasoning copilot |
  | Pieces / Atropos | smaller | — | clinical evidence aggregation |
- **付费方:** 医生（B2C 订阅 / 医院 enterprise）+ pharma 共付
- **moat:** 临床证据库的质量、医生信任度、引用网络（OpenEvidence 用 NEJM 合作锁定 credibility）
- **特别说明:** OpenEvidence 的 16.3x funding-to-valuation 是整个 healthcare AI 最高，意味着市场对"医生入口"这件事的预期极高

### 🔥 S3. Precision Medicine / Diagnostics（最大单一公司）

- **代表公司:**
  | 公司 | 估值/市值 | 总融资 | 业务 |
  |------|------|--------|------|
  | **Tempus AI (TEM)** | **$14B 市值** | $1.05B | precision medicine 平台（genomics + clinical + RWE）|
  | Caris Life Sciences | (IPO 待定) | $2B+ | 分子分型 |
  | Foundation Medicine | (Roche 100% 持有) | — | comprehensive genomic profiling |
  | GRAIL (GH) | 公开市场 | — | 多癌种早筛 |
  | Guardant Health | 公开市场 | — | 液态活检 |
- **付费方:** 保险 + 药企（biopharma data deals）
- **moat:** 数据规模 + 实验室能力 + payer reimbursement codes
- **特别说明:** Tempus 是整个 list 单一最大公司（$14B 市值），数据是它的核心而不是模型

### 🔥 S4. Drug Discovery AI

- **代表公司:**
  | 公司 | 估值 | 总融资 | 业务 |
  |------|------|--------|------|
  | **Xaira Therapeutics** | $1B+ | $1B+ (Series A!) | AI-native drug discovery，史上最大 Series A 之一 |
  | Isomorphic Labs | (Alphabet 内部) | — | AlphaFold 商业化 |
  | Insilico Medicine | undisclosed | $100M Series E | AI-first pharma pipeline，首个 AI 发现药进临床 |
  | Recursion (RXRX) | 公开市场 | — | phenomic discovery |
  | Insitro | undisclosed | — | ML drug development |
  | Genesis Therapeutics | smaller | — | gen AI for small molecules |
- **付费方:** big pharma（partnership upfront + milestone）+ 自有 pipeline 退出
- **moat:** 数据闭环（湿实验 + 干实验）、AI/wet lab integration、IP
- **特别说明:** Xaira 的 $1B+ Series A 是 2024-2025 整个 AI 行业最大单轮之一，说明 LP 对 AI drug discovery 的下一波重新有信心（前一波 Recursion 等已被估值打回原形）

### 🌡️ S5. Medical Imaging AI（用户匹配度最高，但段热度中等）

- **代表公司:**
  | 公司 | 估值 | 总融资 | 业务 |
  |------|------|--------|------|
  | Aidoc | undisclosed | $150M Series E | 急诊放射 AI（卒中/PE/出血 triage）|
  | Rad AI | undisclosed | $60M Series C | 放射报告自动化 |
  | PathAI | undisclosed | $50M Series C ext. | AI 病理 |
  | HeartFlow | recently IPO'd | — | 心脏 CTA 分析 |
  | Cleerly | undisclosed | $223M+ | 冠脉 CTA AI |
  | Viz.ai | undisclosed | $250M+ | 卒中 workflow |
  | Annalise.ai | undisclosed | — | 多病种胸片 AI |
- **付费方:** 医院（per-study fee）+ 部分 CPT/AI codes（HeartFlow 是 reimbursement 标杆）
- **moat:** FDA 510(k)/De Novo 认证 + 医院部署集成 + 临床数据 partnership 锁定
- **重要观察:** **这一段的资金流入显著低于 S1-S4**，融资轮次普遍小于 $200M。原因不是技术不行，是 reimbursement 慢、医院 buyer 谨慎、数据访问门槛被存量玩家锁定（详见后续 deep dive）

### 🌡️ S6. Revenue Cycle / Admin AI（post-Olive 重建）

- **背景:** Olive AI ($4B 估值, $400M 融资) 2023 倒闭，整个 admin AI 段被重新估值
- **代表公司（活下来 + 新一代）:**
  | 公司 | 估值 | 总融资 | 业务 |
  |------|------|--------|------|
  | Innovaccer | undisclosed | $425M+ | healthcare data platform |
  | Cohere Health | undisclosed | $90M Series C | prior auth AI |
  | Commure | undisclosed | $200M growth | RCM agents |
  | Notable | undisclosed | — | patient access automation |
  | Akasa / Adonis / Anterior | smaller | — | 各种 RCM 细分 |
- **付费方:** 医院/health system 直付（per-task 或 per-claim）
- **moat:** EHR 集成 + payer 连接 + 临床流程理解
- **关键变化:** 商业模式从 SaaS 转向 **per-outcome / agentic（按结果或按任务付费）**，付费方 ROI 可量化才会买
- **特别说明:** 这是 Abridge 等 scribe 公司正在扩张进入的相邻段，未来 2 年会和 scribe 段发生融合

### ❄️ S7. Consumer / Virtual Care + AI（增长快但 moat 弱）

- **代表公司:**
  | 公司 | 估值/市值 | 业务 |
  |------|------|------|
  | Hims & Hers (HIMS) | $5–7B 市值（波动大）| D2C + GLP-1 + AI personalization |
  | Ro | private | D2C 处方 + GLP-1 |
  | Forward Health | **2024 已倒闭** | 曾估值 $1B+ |
  | K Health | private | AI primary care chatbot |
  | Spring Health | unicorn | 心理健康 AI matching |
  | Slingshot AI | smaller | $93M—mental health chatbot |
- **付费方:** 消费者直付 + 部分雇主福利
- **特别说明:** GLP-1 是这一段最大单一驱动，与 AI 关系不大；纯 AI 驱动的 Forward 已倒闭说明 consumer 端 moat 薄

### 👀 S8. 观察项 - Wearables / Longevity（不算 AI 医疗，但抢了资金）

- Oura $11B 估值（2025 单轮 $900M）
- Function Health $298M Series B
- Eight Sleep / Nourish 等
- 2025 这一段从第 8 跳到第 3，但**严格来说不是 AI 医疗**，只是用 AI 做个性化推荐。和用户的方向不直接相关。

---

## 三、跨子赛道排序（按"投资回报视角"）

### 按 2025 资金流入热度排：
1. S1 Clinical Documentation（最热，breakout 段）
2. S2 Clinical Decision Support（OpenEvidence 单家 $12B 估值）
3. S3 Precision Medicine（Tempus 单家 $14B 市值）
4. S4 Drug Discovery AI（Xaira $1B+ Series A 重启信心）
5. S6 Revenue Cycle / Admin（重建中，agentic 重塑）
6. S5 Medical Imaging AI（资金中等，临床确定性高）
7. S7 Consumer / Virtual Care（热度高但 moat 弱）

### 按"商业模式确定性"排：
1. S3 Precision Medicine（已有 payer reimbursement）
2. S5 Medical Imaging AI（FDA + CPT codes 已建立）
3. S1 Clinical Documentation（医院直付 per-MD，已 work）
4. S6 RCM Admin AI（per-outcome 模型建立中）
5. S2 Clinical Decision Support（B2C 模型还在摸索）
6. S4 Drug Discovery（长周期 milestone，10 年级别）
7. S7 Consumer Virtual Care（最不确定）

### 按"过渡到中国对应公司的可映射性"排（career 视角，本研究的核心）：
1. **S5 Medical Imaging AI** ← 联影智能、数坤、推想、Aidoc 中国版直接对应
2. **S3 Precision Medicine** ← 燃石、世和、贝瑞 etc.
3. **S1 Clinical Documentation** ← 中国市场不发达（医生 dictate 习惯没建立），映射弱
4. **S2 Clinical Decision Support** ← 春雨/丁香 + 大模型新一波在尝试
5. S4 Drug Discovery ← 晶泰、英矽智能、燧坤等（英矽就在两边都列）
6. S6 RCM ← 中国医疗付费结构完全不同，几乎不可映射
7. S7 Consumer ← 京东健康、阿里健康，但和 AI 关系弱

---

## 四、Phase 2 深挖候选（top 5 提议）

基于上面的双重排序，我建议 Phase 2 深挖的 top 5 候选是（**请用户确认或调整**）：

| # | 候选公司 | 段 | 选它的理由 | 用户 career 角度 |
|---|---------|----|----|----|
| 1 | **OpenEvidence** | S2 | $12B 估值 + 16.3x capital efficiency，整段最 sharp 的 idea | medical LLM 在中国正在被字节/阿里复制，未来 2 年关键赛道 |
| 2 | **Abridge** | S1 | breakout 段的第一名，50x ARR multiple 是否合理 | scribe 中国市场弱，但商业模式可复用到中国 RCM/coding |
| 3 | **Tempus AI** | S3 | 上市公司 + 单一最大、数据 moat 范本 | 中国对应公司（燃石/世和）正在出海，可能是用户切入点 |
| 4 | **Aidoc 或 HeartFlow**（二选一）| S5 | 用户 PA imaging 背景匹配度最高 | 中国版（联影智能/数坤）就是用户回国主线候选 |
| 5 | **Xaira Therapeutics 或 Insilico** | S4 | 重启信心的 AI drug discovery 旗舰 | 英矽中美双总部，可能是用户 dual-shore option |

**待确认问题:**
1. 第 4 名选 Aidoc（急诊 triage）还是 HeartFlow（心脏，已 IPO 是范本）？我建议 **HeartFlow，因为已 IPO 数据更全更适合做范本研究**
2. 第 5 名选 Xaira（最新最大）还是 Insilico（中美双总部，对你 career 直接相关）？我建议 **Insilico，因为它和你的"中国 AI 医疗出海"叙事直接重叠**

---

## 五、Block 1.0 完成状态

- ✅ 子赛道分类完成（7 主 + 1 观察）
- ✅ 每段代表公司 + 融资数字 + 商业模式 + moat
- ✅ 跨段排序（3 个 lens：资金热度、商业模式确定性、中国可映射性）
- ✅ Phase 2 top 5 候选提议

**下一步 (等用户确认):** 锁定 top 5 后启动 Phase 2 深挖。或者先按 Block 1.1-1.7 逐段做更细的 ranked list（这是原计划，但既然已经有了相对完整的公司清单，可以跳过部分子赛道直接进 Phase 2）。

## 来源

- [Rock Health 2025 year-end: A tale of two markets](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/)
- [AI Funding Tracker - Top 20 AI Healthcare Startups 2026](https://aifundingtracker.com/top-ai-healthcare-startups/)
- [Fierce Healthcare - Healthcare AI rakes in nearly $4B](https://www.fiercehealthcare.com/health-tech/healthcare-ai-rakes-nearly-4b-vc-funding-buoying-digital-health-market-2025)
- [Healthcare Dive - 2025 funding outpacing 2024](https://www.healthcaredive.com/news/digital-health-funding-2025-outpacing-2024-q3-rock-health/802330/)
- [New Market Pitch - Healthcare AI startup funding 2025-2026](https://newmarketpitch.com/blogs/news/healthcare-ai-funding-analysis)
