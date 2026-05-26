# Phase 1A: 三家 PBM 母公司 10-K segment data — Batch 1

> 搜索时间: 2026-05-16
> 搜索次数: 4 次并发
> 状态: 部分完成（CVS 搜的是 Pharmacy & Consumer Wellness 而非 Health Services，需要 follow-up）

---

## Search 1: CVS Health 2024 10-K Pharmacy Services Segment

**Query**: `CVS Health 2024 10-K Pharmacy Services Segment revenue operating income annual report`

**关键发现**：
- 搜到的是 **Pharmacy & Consumer Wellness Segment**（实体药店），不是含 Caremark PBM 的 Health Services Segment
- P&CW 2024 revenue: **$124.5B** (+6.6%)
- P&CW 2024 adjusted operating income: **$5.8B** (-3.2%)
- 处方填充 +4% (30-day equivalent basis)
- Generic dispensing rate 88.9%

⚠️ **需要 follow-up**：CVS Health Services Segment（含 CVS Caremark PBM）的具体数字。**Modern Healthcare 提到 Health Services 2024 收入 $186.8B**。

**关键 URL**:
- SEC 10-K filing: https://www.sec.gov/Archives/edgar/data/64803/000006480325000007/cvs-20241231.htm
- CVS IR: https://investors.cvshealth.com/news/news-details/2025/CVS-HEALTH-CORPORATION-REPORTS-FOURTH-QUARTER-AND-FULL-YEAR-2024-RESULTS/default.aspx
- Q4 2024 Earnings Release PDF: https://www.cvshealth.com/content/dam/enterprise/cvs-enterprise/pdfs/2025/Q4-2024-Earnings-Release.pdf

---

## Search 2: Cigna 2024 10-K Evernorth Health Services Segment ⭐

**Query**: `Cigna 2024 10-K Evernorth Health Services segment revenue operating income annual report`

**关键发现**：
- **Pharmacy benefit services revenue: $111.8B (2024)，+46% from $76.8B (2023)** ⭐
- Total Cigna 2024 revenue +27% (Evernorth driven)
- Adjusted income from operations 2024 +4% YoY (Evernorth contribution strong)
- **2025 guidance: Evernorth adjusted income from operations ≥ $7.2B** ⭐
- Specialty & Care Services 增速尤其强

**关键 URL**:
- Cigna IR 2024 results: https://newsroom.thecignagroup.com/2025-01-30-The-Cigna-Group-Reports-Fourth-Quarter-and-Full-Year-2024-Results,-Establishes-2025-Outlook-and-Increases-Dividend
- Cigna 10-K PDF: https://s202.q4cdn.com/757723766/files/doc_earnings/2024/q4/filing/CI-10K-Q4-2024.pdf
- SEC filing: https://www.sec.gov/Archives/edgar/data/1739940/000114036125028099/ef20052574_ex99-1.htm

---

## Search 3: UnitedHealth 2024 10-K Optum Rx Segment ⭐

**Query**: `UnitedHealth Group 2024 10-K Optum Rx segment revenue earnings annual report`

**关键发现**：
- **Optum Rx revenue +15% in 2024** (具体绝对值需补搜)
- **Optum 全 division 2024 revenue: $253B**（+12% YoY，+$26.3B）
- **Optum 2024 operating earnings: $16.7B**（adjusted $18.2B）
- **2024 scripts: 1.62B** (vs 1.54B 2023，+5.2%)
- **2024 managed pharmaceutical spend: $178B**（其中 specialty $74B = 41.6%）
- **Optum Rx 2024 margin: 4.38%**
- **2025: $188B managed, $87B specialty**（增长 5.6% spend, 17.6% specialty）

**关键 URL**:
- SEC 10-K: https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm
- UNH 2024 results press release: https://www.businesswire.com/news/home/20250116305758/en/UnitedHealth-Group-Reports-2024-Results
- UNH 2025 outlook: https://www.unitedhealthgroup.com/content/dam/UHG/PDF/investors/2025/unh-reports-2025-results-and-issues-2026-outlook.pdf
- Segments disclosures: https://app.edgar.tools/companies/UNH/disclosures/segments

---

## Search 4: Cross-comparison (Drug Channels)

**Query**: `CVS Caremark Express Scripts OptumRx 2024 EBITDA segment profit comparison Drug Channels`

**关键发现**：
- **市场份额 2024**：Express Scripts 30%（+7pp，拿 Centene 20M 会员）；CVS Caremark 27%（-7pp）；OptumRx 23%；Top 3 = 80%
- **Express Scripts Centene 5-year deal 2024-01 开始**
- **Express Scripts 2024 retail Rx claims**：1.9B（2023 是 1.3B，+40% = +531M claims）
- **CVS Caremark 2024 30-day claims**：1.9B（2023 是 2.3B，-18.2%）
- **OptumRx 2025**：$188B managed, $87B (46%) specialty
- **Top 3 都在 2024 推出 cost-plus / transparent pricing 产品**

**关键 URL**:
- Drug Channels 2025 top PBMs: https://www.drugchannels.net/2025/03/the-top-pharmacy-benefit-managers-of.html
- Drug Channels 2026 top PBMs (2025 数据): https://www.drugchannels.net/2026/03/the-top-pharmacy-benefit-managers-of.html
- Modern Healthcare CVS Health Services: https://www.managedhealthcareexecutive.com/view/cvs-s-health-services-revenue-grew-to-186-8-billion
- IntuitionLabs Big 3 PBMs PDF: https://intuitionlabs.ai/pdfs/the-big-3-pbms-an-analysis-of-market-share-dominance.pdf

---

## 缺口（要 Batch 2 补）

1. **CVS Health Services segment 详细财务**（含 Caremark + Oak Street + Signify + MinuteClinic）：
   - 2024 revenue: $186.8B（要 verify）
   - 2024 operating income: ?
   - Caremark 单独 prescription revenue: ?

2. **Cigna Evernorth Specialty vs Pharmacy Benefit Services 拆分**：
   - Pharmacy benefit services revenue $111.8B 已 verify
   - Specialty and Care Services revenue: ?
   - Evernorth 2024 实际 operating income（vs 2025 guidance $7.2B）: ?

3. **OptumRx specific revenue 绝对值**：
   - 仅有 +15% growth，需绝对值
   - Optum Health 和 Optum Rx 拆分

4. **三家 5 年历史 segment 财务**（2020-2024）做 trend 分析

---

## 暂未保存的次级数据

- IntuitionLabs PDF 含 deeper analysis（PDF 较长，需要单独提取）
- SEC 10-K filings 实际原文（需要下载 PDF 然后 extract）

---

## 下一步

Batch 2:
- Search "CVS Health Services Segment 2024 revenue operating income Caremark"
- Search "Cigna Evernorth Specialty and Care Services 2024"
- Search "UnitedHealth Optum Rx 2024 revenue absolute dollars segment"
- Fetch UNH 10-K PDF for segment table extraction
- Fetch CVS 10-K PDF same
- Fetch Cigna 10-K PDF same
