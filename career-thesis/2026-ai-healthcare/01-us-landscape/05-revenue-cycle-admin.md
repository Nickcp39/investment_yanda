---
title: S6 Revenue Cycle / Admin AI — 段内 ranked list（含死亡公司）
segment: S6
created: 2026-05-16
status: draft-v1
companies_in_csv: 13 (incl 2 dead, 2 acquired, 2 incumbents)
---

# S6: Revenue Cycle / Admin AI

## 段级数据（2025）

| 指标 | 数值 | 来源 |
|------|------|------|
| Prior auth AI spending | **$100M+** (2025), 10x YoY | Menlo VC |
| Patient engagement AI spending | $100M+, 20x YoY | Menlo VC |
| Payer ops AI spending | $50M+, 5x YoY | Menlo VC |
| Back-office RCM 整体 TAM（含传统 IT） | **$18.8B** | Menlo VC |
| Medical documentation 整体 TAM | $19.6B | Menlo VC |
| 大型 health system AI 采购周期 | 6.6 月（vs 传统 8 月，缩短 18%）| Menlo VC |
| Payer AI 采购周期 | 11.3 月（vs 9.4 月，**延长 20%**）| Menlo VC |

**关键洞察:** 增长率最炸（prior auth 10x、patient engagement 20x），但绝对盘子还很小（百万级，不是十亿级）。
**这是"高增速 + 低基数 + 高失败率"的典型段** —— Olive、Babylon 死亡是规律不是例外。

---

## Ranked list（13 家，含 2 死 + 2 acquired + 2 incumbents）

### Tier 0: 已死 / cautionary tales（最重要的样本）

| # | 公司 | 死法 | 鼎盛估值 | 总融资 | 死因 |
|---|------|------|----------|--------|------|
| 1 | **Olive AI** ⚰️ | 2023-10 关门，资产卖给 Waystar (clearinghouse) + Humata (prior auth) | $4B (2021) | $400M (Series H 2021) | "过度承诺 + 缺乏聚焦 + 客户支持烂 + 透明度差"。CEO Sean Lane 原话: "fast-paced growth and lack of focus"。被 KLAS 报告爆"5x 成本节省"是估算不是数据。**钱来得太容易反而不被尊重** |
| 2 | **Babylon Health** ⚰️ | 2023 破产，资产卖给 eMed | $4B (IPO 2021) | $550M | 英国出身，过度依赖 NHS 单一 buyer + SPAC IPO 透支故事 + AI 实际能力低于宣传 |

**这两家死亡共同教训（对评估其他 RCM 公司的红旗清单）:**
1. 单一 metric 不可证伪的 ROI 承诺（如 "5x cost saving"）→ 红旗
2. 产品线扩张过快，每条线都浅 → 红旗
3. 客户 NPS 低但保留率靠"长合约 +客户成功救火"撑着 → 红旗
4. CEO 公开演讲过度 vs 客户案例文档极少 → 红旗
5. pre-IPO 通过 SPAC（捷径）而不是 traditional IPO → 红旗

### Tier 1: 头部 unicorn+

| # | 公司 | 估值 | 总融资 | 最近一轮 | 业务 |
|---|------|------|--------|----------|------|
| 3 | **Innovaccer** | **$3.45B** | $700M+ | $275M Series F (2025-01) | 数据平台 + AI co-pilots（医生 scribe + prior auth + 拒付申诉），多模块 |
| 4 | **Commure** | ~$6B (est) | $1B+ | $200M growth (2025-06) | full-stack AI 平台（RCM + scribe + practice mgmt），AI agent 处理 denials/prior auth/EOB/患者短信 |

### Tier 2: 中型

| # | 公司 | 估值 | 总融资 | 最近一轮 | 业务 |
|---|------|------|--------|----------|------|
| 5 | **Cohere Health** | undisclosed | $106M | $50M equity (2025-02) | prior auth 专做；和 Ensemble 合作做 RCM-native LLM |
| 6 | **AKASA** | undisclosed | ~$200M | Series D (2022) | GenAI for RCM（preauth + coding + claims）|
| 7 | **Notable** | undisclosed | ~$120M+ | Series B+ | patient access automation |

### Tier 3: 新兴 / 长尾

| # | 公司 | 估值 | 总融资 | 业务 |
|---|------|------|--------|------|
| 8 | **Tennr** | undisclosed | ~$60M | patient intake + prior auth via OCR/document AI |
| 9 | **Develop Health** | undisclosed | $17.6M | $14.3M Series A (2025) | benefits verification + prior auth（新一代）|
| 10 | **Humata Health** | undisclosed | n/a | acquired Olive's prior auth biz; 独立运营 |
| 11 | **Anterior** | undisclosed | seed | payer ops |

### Tier 4: Incumbents（不是 startup 但段内不可忽视）

| # | 公司 | 状态 | 业务 | 关键事件 |
|---|------|------|------|----------|
| 12 | **Waystar (WAY)** | public NASDAQ | clearinghouse + RCM 工作流 | 收购了 Olive 的 clearinghouse 业务（2023）|
| 13 | **R1 RCM** | public NYSE | 老牌 RCM 外包 | 被 PE 私有化 ~ $9B（2024）|

---

## 段内深度分析

### 商业模式演化

Olive 死亡之后整个段的 pricing 模型发生了关键变化：

**Pre-Olive (2020-2022):** SaaS 订阅，按 seat 或按医院规模收费，承诺 ROI 但不挂钩
**Post-Olive (2023-now):** **per-outcome / per-claim / per-prior-auth pricing**，把 AI 厂商和 ROI 硬绑定。这种模型对厂商风险更高但对医院信任度更高，是 Commure / Cohere 的核心打法

### 谁是真买方？

S6 段是 healthcare AI 里**买方最复杂**的一段：
- **Hospital RCM team:** 关心 collections 改善（直接付费方）
- **Payer ops team:** 关心 admin cost 降低（另一种买方）
- **第三方 RCM outsourcer (R1, Ensemble):** 关心毛利提升（间接买方，会自建或合作）

不同买方决定不同的 GTM，混在一起的公司容易死。Olive 同时卖 hospital + payer + clearinghouse，**三个市场都没做深** 是它失败的根因之一。

### Moat 分析

| Moat 类型 | 例 | 强度 |
|----------|---|------|
| EHR 集成深度 | Commure (Epic/Cerner 深) | 强 |
| Payer 网络 | Cohere（200+ payer 接口）| 强 |
| 数据 + RCM-native LLM | Cohere x Ensemble | 中 |
| Brand + 早期客户 | Akasa | 弱 |
| 平台收购整合 | Commure（已购 Augmedix）| 强 |

### 风险信号

- **AKASA 类型公司:** Series D 已 3 年没新轮（2022 至今），可能是下一批被淘汰
- **Innovaccer 估值 $3.45B 但收入未披露:** 多模块平台型常见现象——增长靠新 module 上线而非现有客户深耕。值得关注 NRR
- **Tennr / Develop Health 这种"新一代":** 单一痛点（document AI / benefits 验证）+ 小融资。会不会被 Cohere/Commure 直接打掉？还是被收购？很难独立长大
- **Olive 资产被 Waystar / Humata 接走:** 说明传统 RCM incumbents（不是 startup）才是 prior auth 的终极赢家可能性。这对所有 RCM startup 都是结构性威胁

### 中国可映射性: **极低**

S6 在中国几乎无法直接对应，因为：
- **付费方根本不同**：中国医疗主要 payer 是医保局（政府）+ 自费，没有美国那种商业 payer + provider 博弈
- **RCM 业务本身少**：中国医院 RCM 高度集成在 HIS 系统里（卫宁、东软、创业慧康），AI 化主要靠这些 EHR 厂商自身
- **Prior auth 不是 bottleneck**：中国 prior auth 主要在医保审核环节（政府部门），不是商业 payer
- **结论:** S6 的商业模式在中国无法直接复制。但**底层 LLM + agentic workflow 技术**可以转向其他用途（如医保智能审核、医院财务自动化）

**对 Nick 的 entry_paths 含义:** S6 在 Nick 的"中国医疗设备出海"主线里**几乎没位置**。除非他想做反向（中国公司学美国 RCM AI 模式做国内医保 IT），否则这一段对他主要价值是 **看清死亡模式，避免在其他段重蹈覆辙**

---

## Nick 视角：S6 段对你职业决策的含义

虽然 S6 不在你的主线，但从 Olive 的死亡可以提炼对你**评估任何 AI healthcare 公司**的红旗清单（见上方"两家死亡共同教训"）。这套清单可以用来评估你后面看到的：
- 中国医疗 AI 公司（数坤、推想等）：估值倒挂 + 频繁裁员 + 客户案例少 = 同类信号
- 任何你考虑加入的 startup：CEO 演讲 vs 客户案例文档比例

**实用建议:** 拿到一家 AI healthcare 公司 offer 之前，至少看 5 篇客户案例的具体可量化结果。如果只能找到 PR 稿不能找到客户工程师的视频/访谈，警惕。

---

## 数据补充建议（下一轮）

- AKASA 准确融资 + 客户数
- Innovaccer revenue 数据
- Notable / Tennr / Anterior 详细融资
- 段内未来 12 个月预期死亡名单（哪些公司"看上去像 Olive 2021"）

## 来源
- [Healthcare Dive - Olive AI shuts down](https://www.healthcaredive.com/news/olive-ai-shuts-down/698455/)
- [Modern Healthcare - Olive AI downfall: what's next](https://www.modernhealthcare.com/digital-health/olive-ai-shutting-down-digital-health-investors-waystar-humata/)
- [Becker's - Rise and fall of Olive AI timeline](https://www.beckershospitalreview.com/healthcare-information-technology/digital-health/the-rise-and-fall-of-olive-ai-a-timeline/)
- [TechCrunch - Innovaccer $275M Series F](https://techcrunch.com/2025/01/09/innovaccer-aims-to-become-healthcares-ai-powerhouse-with-275m-series-f/)
- [Commure - $200M growth round press release](https://www.commure.com/press-releases/commure-raises-200m-in-growth-financing-from-general-catalysts-cvf-to-accelerate-ai-powered-rcm-platform)
- [MedCity News - Develop Health $14.3M](https://medcitynews.com/2025/08/develop-health-prior-authorization-funding/)
- [Modern Healthcare - Prior auth companies vs insurers](https://www.modernhealthcare.com/health-tech/ai/mh-prior-authorization-companies-cohere-health-eliseai/)
- [Menlo Ventures - 2025 State of AI in Healthcare](https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/)
