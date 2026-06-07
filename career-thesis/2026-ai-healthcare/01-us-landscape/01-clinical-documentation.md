---
title: S1 Clinical Documentation / AI Scribe — 段内 ranked list
segment: S1
created: 2026-05-16
status: draft-v1
companies_in_csv: 11
---

# S1: Clinical Documentation / AI Scribe

## 段级数据（2025 全年）

| 指标 | 数值 | 来源 |
|------|------|------|
| 段内总收入 | **$600M** | Menlo VC 2025 SoAH 报告 |
| YoY 增长 | **2.4x** | 同上 |
| 段内总融资 (2025 single year) | **~$1B+** | StatNews/TechCrunch 合并 |
| 段内 unicorn 数量 | ≥ 4 (Abridge, Ambience, Nabla?, +Nuance 已被收购) | 同上 |
| 段内 enterprise 渗透率 (大型 health system) | 35% (当前) → 40% (3 年预期) | Menlo VC |
| Startup 段内份额 vs 现存厂商 | **70% : 30%** | Menlo VC |

**关键洞察:** 这是 healthcare AI 的 **first breakout category**。商业化路径已经验证——医院按 per-MD 订阅付费（$2-4k/年），不靠保险报销，决策链短。Kaiser + Abridge 部署被称为"20 年来最快技术落地"。

但段内集中度极高——前 3 家（Nuance 33% + Abridge 30% + Ambience 13% = 76%）几乎吃掉所有市场。

## Ranked list（11 家）

### Tier 1: $1B+ 估值，绝对头部

| # | 公司 | 总融资 | 最新估值 | 最近一轮 | ARR | 客户 |
|---|------|--------|----------|----------|-----|------|
| 1 | **Abridge** | $800M+ | **$5.3B** | $300M Series E (2025-06) | **$100M** (2025-05, vs $60M EOY2024) | Kaiser (24.6k MD, 40 hospitals)、Mayo、Hopkins、Duke、UPMC、Yale |
| 2 | **Nuance DAX Copilot (Microsoft)** | — (acquired) | $19.7B (2022 acq.) | acquired 2022 | undisclosed | 77% of US hospitals (deployed base) |
| 3 | **Ambience Healthcare** | $243M+ | **$1.25B** | $243M Series C (2025-07) | undisclosed | health systems multi-specialty |

### Tier 2: 中位估值 $200M-$1B

| # | 公司 | 总融资 | 最新估值 | 最近一轮 | 备注 |
|---|------|--------|----------|----------|------|
| 4 | **Heidi Health** | ~$100M | $465M | $65M Series B (2025) | 全球扩张，APAC 强 |
| 5 | **Suki AI** | $165M | undisclosed | $70M Series D | 中小型 practice 为主 |
| 6 | **Nabla** | ~$95M+ | $180M (last disclosed 2024-01) | $70M Series C (2025-06) | 法国出身，agentic 扩张 |

### Tier 3: 小型 / 被收购 / 长尾

| # | 公司 | 总融资 | 状态 | 备注 |
|---|------|--------|------|------|
| 7 | **Augmedix** | $139M (acquired) | **acquired by Commure 2024** | 早期 Google Glass + human scribe 模式 |
| 8 | **DeepScribe** | ~$30M+ | private | 中等规模 |
| 9 | **Freed** | undisclosed | private | 专做 outpatient |
| 10 | **Eleos Health** | undisclosed | private (Menlo 投) | 行为/精神科 + post-acute |
| 11 | **Commure** | $200M+ growth round | private | 平台型；收购 Augmedix；做 scribe + RCM agent |

## 段内分析

### 商业模式比较

所有 S1 公司付费方都是 **医院/诊所** 直付，差异在：
- **Abridge / Nuance:** enterprise per-MD subscription（最大型 health system）
- **Heidi / Freed:** SMB SaaS（中小型 practice 自助开通）
- **Commure:** 平台 + 收购模式，向 RCM 横向扩
- **Nabla:** 从订阅向 outcome-based 转

### Moat 排序
1. **Nuance:** 距离 Epic / Cerner EHR 集成最深（Microsoft 资源），77% 医院已部署的 inertia
2. **Abridge:** Epic First-Class Integration、Kaiser deep deployment、ARR 增长最快
3. **Ambience:** 多模块（scribe + coding + RCM）的 horizontal stack
4. **Heidi:** 全球分布广（澳洲、欧洲、APAC 强），是唯一国际化做得好的 startup
5. **其他:** moat 弱，长期会被前 4 家吃掉

### 风险信号

- Abridge 的 $5.3B / $100M ARR = **53x revenue multiple** — 这是 SaaS 历史上最贵的一档。要么 ARR 继续 2-3x 增长 2 年才合理，要么会显著回调
- Nuance 仍占 33% 市场份额且增长稳定（背靠 MSFT），startup 段内的"30% × $600M = $180M"才是 2025 真实可分蛋糕，Abridge 一家就占了 ~$100M ARR，意味着其他 startup 加起来 ARR 只有 ~$80M——**赛道远没有融资数字看上去那么大**
- Switching cost：Menlo VC 调查显示 50% 大型 health system + 67% outpatient 表示愿意 switch ——头部公司护城河没大家想的深
- Ambient scribe 的天花板：Menlo 预测大型 health system 3 年后渗透率 40% 会 plateau，意味着 **段内增长 2027 后会显著放缓**

### 中国可映射性: **低**
- 中国医生不普遍 dictate（口述习惯没建立）
- 中国 EHR 标准化程度低于美国 Epic/Cerner
- 中国医院 IT 预算 < 美国 1/10
- **结论:** S1 的商业模式在中国短期内难复制。但**底层语音+LLM 技术**可以转向其他用途（如电话回访、远程会诊纪要）

## 数据补充建议

下一轮需要补的：
- Commure 详细估值（最近一轮）
- DeepScribe / Freed / Eleos 的融资数据
- ARR 数据除 Abridge 外几乎全缺，下次专门搜
- 段内"已死"案例（这一段似乎活的多死的少，但需要确认）

## 来源
- [TechCrunch - Abridge $5.3B](https://techcrunch.com/2025/06/24/in-just-4-months-ai-medical-scribe-abridge-doubles-valuation-to-5-3b/)
- [StatNews - Ambience $243M](https://www.statnews.com/2025/07/29/ambience-healthcare-ai-scribe-new-fundraise/)
- [StatNews - Nabla $70M Series C](https://www.statnews.com/2025/06/17/nabla-raises-70-million-ambient-market-heats-up/)
- [Sacra - Abridge $100M ARR](https://sacra.com/c/abridge/)
- [MobiHealthNews - Heidi Health $65M](https://www.mobihealthnews.com/news/heidi-health-raises-65m-expand-global-reach-its-ai-medical-scribe-platform)
- [Modern Healthcare - AI scribes 2025 VC](https://www.modernhealthcare.com/health-tech/ai/mh-ai-scribes-investment-vcs-pitchbook-2025/)
- [Menlo Ventures - 2025 State of AI in Healthcare](https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/)
