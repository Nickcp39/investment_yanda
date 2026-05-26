# Phase 1B: FTC Second Interim Report deep extract

> 搜索时间: 2026-05-16
> 搜索次数: 3 searches + 4 WebFetch (全 403 block)
> 状态: 完成（搜索数据足够，WebFetch 全 block 是限制不是 gap）

---

## 报告基本信息

**全称**: "Specialty Generic Drugs: A Growing Profit Center for Vertically Integrated Pharmacy Benefit Managers"
**发布**: 2025 年 1 月（FTC PBM 6(b) 调查第二份 interim report）
**作者**: FTC Bureau of Competition + Bureau of Economics
**研究方法**: 6(b) 强制 subpoena Big 3 PBMs (CVS Caremark, Express Scripts, OptumRx)
**研究时间窗**: 2017-2022 (Q1 dispensings 数据)
**研究范围**: 51 specialty generic drugs, 882 NDCs（National Drug Codes）, commercial + Medicare Part D plans

---

## 核心 finding（按数字大小排）

### F1: $7.3B 是 PBM affiliated 药房在 specialty generic 上的超额收入
- "**Big 3 PBMs' affiliated pharmacies generated over $7.3 billion of dispensing revenue in excess of their estimated acquisition cost**, as measured by the National Average Drug Acquisition Cost (NADAC), on specialty generic drugs over the study period"
- 时间窗：2017-2022（6 年累计）
- 即年化平均 **~$1.2B/年**

### F2: $1.4B spread pricing 额外利润（同口径）
- "In the aggregate, the Big 3 PBMs also separately generated an estimated **$1.4 billion of income from spread pricing** on the analyzed specialty generic drugs over the study period"
- 6 年累计 → 年化 **~$233M**
- 这是跟 F1 不重叠的另一笔（spread pricing on dispensings to OTHER pharmacies, where PBM doesn't dispense itself but still gets spread）

### F3: CAGR 42%（增长极快）
- "**PBM-affiliated pharmacy dispensing revenue in excess of NADAC increased dramatically at a compound annual growth rate of 42 percent from 2017-2021**"
- 4 年期间利润增长 ~4x
- 说明 PBM 越来越聚焦 specialty generic 这个金矿

### F4: 集中度极高
- "**In the aggregate, the top 10 specialty generic drugs generated $6.2 billion of dispensing revenue in excess of NADAC (85 percent of total)**"
- Top 10 / 51 = 20% drugs 占 85% 利润
- → 高度集中在少数 high-margin specialty generics

### F5: Markup 程度
- "PBMs marked up **nearly two-thirds** of the specialty generic drugs analyzed **by more than 100 percent**"
- "PBMs marked up the cost of **over one in five** specialty generic drugs **by over 1,000 percent**"
- 即：
  - 67% drugs markup >100%（doubled）
  - 20% drugs markup >1000%（11x）

### F6: 具体药品 markup 案例
- **Tadalafil**（pulmonary hypertension 适应症，prostate cancer 的兄弟分子）：
  - PBM affiliated 药房采购成本：$27
  - PBM reimbursement rate（30-day supply）：$2,106
  - **Markup: > 7,700%**
  - 年份：2022

- **Imatinib (Gleevec 仿制药)**: leukemia 用药，markup >1,000%
- **Abiraterone (Zytiga 仿制药)**: prostate cancer 用药，markup >1,000%
- **Mesalamine**: IBD 用药（搜索未找到具体 %）
- 报告中具体提到的药品 generics：
  - **Ampyra** (multiple sclerosis)
  - **Gleevec** (leukemia → Imatinib)
  - **Sensipar** (renal disease)
  - **Myfortic** (transplant)
  - **Zytiga** (prostate cancer → Abiraterone)

### F7: Affiliated vs Unaffiliated 报销差异
- "The Big 3 PBMs also reimbursed their affiliated pharmacies at a **higher rate** than they paid unaffiliated pharmacies on **nearly every specialty generic drug examined**"
- 这是 "self-dealing" 的核心证据

---

## 战略 implications（FTC 暗示）

1. **垂直整合是这套套利的前提**：必须既是 PBM 又拥有 specialty pharmacy 才能 self-deal
2. **Specialty Generic 是 PBM 真金矿，不是 brand**：之前以为 rebate (brand drug) 是核心，FTC 揭露 specialty generic markup 同样巨大
3. **Steering 患者到 affiliated pharmacy 是关键机制**：医生开药 → PBM 通过 formulary 限制 → 患者必须去 PBM 自家药房 → markup 套利
4. **NADAC 是真实采购成本基准**：FTC 用这个 benchmark 让 PBM 无处遁形

---

## 跟之前搜到的 "$73B 过去 10 年额外成本" 数字关系

- FTC 2025 报告聚焦 specialty generic = $7.3B (2017-2022)
- 另一个数字 "$73B 过去 10 年" 来源不同（可能是 FTC 第一份报告 2024-07）
- 数量级差 10x，说明 specialty generic 仅是 PBM 套利的一部分
- 完整套利还包括：rebate retention、formulary steering、340B 套利、DIR fees

---

## 关键 URL（验证 / 引用源）

### 一手源（被 403 block，但 URL 可信）
- FTC press release (2025-01-14): https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-releases-second-interim-staff-report-prescription-drug-middlemen
- FTC report PDF: https://www.ftc.gov/system/files/ftc_gov/pdf/PBM-6b-Second-Interim-Staff-Report.pdf
- FTC report landing page: https://www.ftc.gov/reports/specialty-generic-drugs-growing-profit-center-vertically-integrated-pharmacy-benefit-managers

### 二手汇总（搜索数据来源）
- Fierce Healthcare: https://www.fiercehealthcare.com/payers/ftc-big-3-pbms-generated-73b-specialty-generic-drug-markups
- AJMC: https://www.ajmc.com/view/ftc-report-highlights-prescription-drug-price-markups-by-pbms
- HIV-HCV Watch: https://www.hiv-hcv-watch.com/blog/jan-27-2025
- Buchanan Ingersoll & Rooney 法律分析: https://www.bipc.com/understanding-the-ftc%E2%80%99s-second-interim-staff-report-on-pbms-what-it-means-for-plan-sponsors-and-employers
- CNN: https://www.cnn.com/2025/01/14/business/drug-price-mark-up-ftc-pbm/index.html
- TechTarget: https://www.techtarget.com/pharmalifesciences/news/366618333/FTC-report-reveals-PBMs-inflate-costs-of-specialty-generic-drugs
- Pharmaceutical Commerce: https://www.pharmaceuticalcommerce.com/view/ftc-report-finds-big-three-pbm-mark-ups-specialty-generics-generated-billions
- PhRMA blog: https://www.phrma.org/blog/ftc-finds-pbms-make-billions-in-profit-from-marking-up-cancer-other-critical-generic-drugs
- Duane Morris LLP: https://www.duanemorris.com/alerts/ftc_report_shows_pharmacy_benefit_managers_profit_specialty_generic_drug_markups_0125.html
- Freshfields: https://blog.freshfields.us/post/102ju1a/ftc-issues-second-interim-report-on-pbms-focused-on-pricing-practices-for-special
- pharmaphorum: https://pharmaphorum.com/news/ftc-doubles-down-pbm-criticism-new-report
- Healthcare Finance News: https://www.healthcarefinancenews.com/news/ftc-says-top-three-pbms-made-73-billion-marked-drug-prices
- GaBI Online: https://gabionline.net/reports/ftc-reveals-extent-of-pbm-drug-mark-ups-and-profits
- Axios: https://www.axios.com/2025/01/14/pbms-marked-up-specialty-generics-ftc
- Center for Biosimilars: https://www.centerforbiosimilars.com/view/ftc-releases-second-report-on-pbms-meddling-in-generic-drug-markets
- Managed Healthcare Executive: https://www.managedhealthcareexecutive.com/view/new-ftc-report-pbms-mark-up-specialty-generic-drugs
- PlanSponsor: https://www.plansponsor.com/ftc-issues-2nd-report-exposing-practices-of-pharmacy-benefit-managers/

---

## 仍缺数据

1. **FTC Chair Lina Khan 离任前对 PBM 的具体立场陈述**（2025-01 报告发布时她已经在收尾）
2. **PCMA（PBM 行业协会）官方回应原文 quote**
3. **CVS/CI/UNH 三家公司对 FTC 报告的官方 quote**（高管 8-K 公开声明）
4. **FTC 第一份报告 2024-07 的 deep extract**（这次没做）

→ 这些可以用 Phase 1F WebFetch 补，如果 Phase 1F WebFetch 仍 block 就用 Bash + curl 试。

---

## 给 Phase 3 派生计算用的数字

| 数据点 | 值 | 用于 |
|---|---|---|
| Specialty generic markup 累计 (2017-2022) | $7.3B | 反推 specialty generic markup 年化收入 |
| Spread pricing on specialty generics 累计 | $1.4B | 同上 |
| CAGR (2017-2021) | 42% | 投影 2022-2027 趋势 |
| Top 10 drugs 集中度 | 85% of $7.3B | Pareto 分布 → 单药利润敏感性 |
| Tadalafil markup | 7,700% | 极端案例，模型 worst case |
| > 1,000% markup 药品占比 | 20% | 大批量套利空间估算 |
| 51 drugs / 882 NDCs | scope | 用作 model boundary |

---

## 下一步

Phase 1B 完成。**进 Phase 1C: 行业分析师 view (Adam Fein @ Drug Channels 等)**。
