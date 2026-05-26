# Phase 1A Batch 2: 补缺数据

> 搜索时间: 2026-05-16
> 状态: 主要缺口已补，仅 Optum Rx 绝对 revenue 仍需推算

---

## Search 5: CVS Health Services Segment 完整数据 ⭐

**Query**: `CVS Health Services Segment 2024 revenue operating income Caremark $186 billion annual`

**关键发现**：

| CVS Health Services Segment | 2023 | 2024 | YoY |
|---|---|---|---|
| Revenue | **$186.8B** | **$173.6B** | **-7.1%** |
| Adjusted Operating Income | ~$7.27B | **$7.2B** | **-0.9%** |

- **下降原因**：丢 Centene 大客户（2024-01 给 Express Scripts）+ pharmacy client price improvements
- Health Services 含：Caremark PBM + CVS Specialty + Oak Street + Signify + MinuteClinic
- **Operating margin**：7.2/173.6 = **4.15%**

**关键 URL**:
- CVS Q4 2024 press release: https://investors.cvshealth.com/news/news-details/2025/CVS-HEALTH-CORPORATION-REPORTS-FOURTH-QUARTER-AND-FULL-YEAR-2024-RESULTS/default.aspx
- Healthcare Dive Q4 2024 analysis: https://www.healthcaredive.com/news/cvs-q4-2024-earnings-medical-costs-profit-slashed/739959/
- CVS Health 2024 Annual Review: https://cvshealth2024inreview.com/

---

## Search 6: Cigna Evernorth 子段拆分 ⭐

**Query**: `Cigna Evernorth Specialty Care Services 2024 revenue Express Scripts operating income`

**关键发现**：

Cigna Total 2024 Revenue: **$247.1B (+27%)**

Evernorth 分两块：

| Evernorth 子段 | 2023 | 2024 | YoY |
|---|---|---|---|
| **Pharmacy Benefit Services** (= Express Scripts core) | $76.8B | **$111.8B** | **+46%** |
| **Specialty and Care Services** (= Accredo + eviCore 等) | $76.7B | **$90.3B** | **+18%** |
| **Evernorth Total Adj Revenue** | ~$153.5B | **~$202.1B** | **+32%** |

- **Evernorth 2024 adj income from operations: +9% YoY**（具体 $ 在 Q4 press release 但搜索 result 没显示）
- **Q4 2024 单季**：
  - Express Scripts adj operating income: **$1.2B**（单季）
  - Specialty and Care Services adj operating income: **$948M** (+27% YoY)
- **2025 guidance**: Evernorth adj operating income **≥$7.2B**

**用 Q4 数据估算全年**：
- 假设 Q4 是 ~25% 全年（季节性偏高），Express Scripts 全年 adj operating income ≈ $4.5-5B
- Specialty 全年 ≈ $3.5-4B
- **Evernorth 全年 ~$8-9B operating income (高于 2025 guidance $7.2B)**

⚠️ 这个数字需要从 10-K 原文 verify

**关键 URL**:
- Cigna Q4 2024 press release: https://newsroom.thecignagroup.com/2025-01-30-The-Cigna-Group-Reports-Fourth-Quarter-and-Full-Year-2024-Results
- Modern Healthcare Cigna earnings: https://www.modernhealthcare.com/insurance/mh-cigna-earnings-evernorth-health-express-scripts/
- Healthcare Dive Cigna Q4 2024: https://www.healthcaredive.com/news/cigna-express-scripts-plan-reform-q4-2024/738731/
- Substack Jeff Delverne analysis: https://jeffdelverne.substack.com/p/cignas-q4-2024-earnings-strong-growth

---

## Search 7: UnitedHealth Optum 拆分

**Query**: `UnitedHealth Optum Rx 2024 revenue absolute dollar amount Optum Health segment breakdown`

**关键发现**：

UnitedHealth 2024 Total Revenue: **$400.3B**

Optum 分三段：

| Optum 子段 | 2024 Revenue | YoY |
|---|---|---|
| **Optum Health** (医生集团 + ASC + Home health + Behavioral) | **$105.4B** | 增（具体 % 待补） |
| **Optum Rx** (PBM) | ~$130-133B（推算：去年 ~$116B × 1.15） | **+15%** |
| **Optum Insight** (数据 + Change Healthcare) | ~$18-20B（推算：Optum 总 $253B - Health $105 - Rx $133 = $15B） | 受 Change Healthcare 网络攻击影响 |
| **Optum Total** | **$253B** | **+12%** |

**Optum Operating Earnings**: $16.7B (adjusted $18.2B)
**Optum Rx**:
- 2024 scripts: **1.62B**（vs 1.54B 2023, +5.2%）
- 2024 managed pharma spend: **$178B** (含 $74B specialty = 41.6%)
- 2024 margin: **4.38%** (per earlier search)
- 2025: $188B managed, $87B specialty

**估算 Optum Rx 2024 operating income**:
- 用 4.38% margin × $133B revenue ≈ **$5.8B** operating income
- 但这是粗估，因为 Optum 总 operating earnings $16.7B 包括三段

**关键 URL**:
- Fierce Healthcare UNH Q4: https://www.fiercehealthcare.com/payers/unitedhealth-group-posts-144b-profit-4003b-revenue-2024
- Healthcare Finance News UNH 2024: https://www.healthcarefinancenews.com/news/unitedhealth-group-hits-4003-billion-revenue-credits-optumrx
- SEC UNH Q4 2024 8-K: https://www.sec.gov/Archives/edgar/data/731766/000073176625000022/a2024q4exhibit991.htm
- Statista Optum revenue by business: https://www.statista.com/statistics/622400/revenues-of-optum-by-business/
- Modern Healthcare UNH Q2 2025: https://www.modernhealthcare.com/insurance/mh-unitedhealth-group-earnings-optum-health/

---

## Search 8: 备份 - CVS Health Services Adjusted Operating Income

**Query**: `CVS Health 10-K 2024 Health Services Caremark adjusted operating income segment`

**Verify**：

- **2024 Health Services Adjusted Operating Income: $7.2B (-0.9%)** ✅ confirmed
- Operating margin = 7.2/173.6 = **4.15%**

**关键 URL**:
- Healthcare Dive analysis: https://www.healthcaredive.com/news/cvs-q4-2024-earnings-medical-costs-profit-slashed/739959/
- CVS 10-K filing direct: https://www.sec.gov/Archives/edgar/data/64803/000006480325000007/cvs-20241231.htm

---

## 总结：三家 PBM 母公司 2024 segment 数据

| | **CVS Health Services** | **Cigna Evernorth** | **UNH Optum Rx** |
|---|---|---|---|
| Revenue 2024 | $173.6B | $202.1B (Pharma $111.8B + Spec $90.3B) | ~$130-133B (估) |
| YoY Revenue | **-7.1%** | **+32%** | **+15%** |
| Adj Operating Income | **$7.2B** | ~$8-9B (Q4 推算) | ~$5.8B (margin 反推) |
| Operating Margin | 4.15% | ~4-4.5% | 4.38% |
| Scripts 2024 | 1.9B (-18%) | 1.9B (+40%) | 1.62B (+5%) |
| Market share | 27% | 30% | 23% |
| 母公司 Total Revenue | $372.8B | $247.1B | $400.3B |
| PBM segment 占母公司 % | 47% | 82% | 33% |
| 母公司市值（2026-05） | ~$90B | ~$90B | ~$330B |

**关键 inference**:
1. **PBM segment 占母公司 revenue % 排序**：Cigna (82%) >> CVS (47%) > UNH (33%)
2. **但市值占比不一样**：CI 估值低，UNH 高 → 资本市场给 UNH 多元化溢价
3. **PBM 改革 2027 利润悬崖最大暴露者：Cigna**
4. **CVS 已经在 2024 受丢 Centene 影响 (-7.1% revenue)，反而进入"已修复"状态**

---

## 仍缺数据

1. **Optum Rx 具体 revenue 绝对值**（10-K segment table 应有）
2. **Evernorth 2024 全年 adjusted operating income 实际数字**（搜到 Q4 但全年没拿）
3. **三家历史 5 年 segment trend**（2020-2024 做时间序列）
4. **PBM segment 内部 specialty vs core PBM 拆分**（用 specialty pharmacy 数据辅助）

---

## 下一步

Phase 1A 完成，进入 **Phase 1B: FTC 2nd Interim Report deep extract**。

Phase 1A 缺的 4 点可以在后续 Phase 1F (failure log / verification) 阶段用 WebFetch 直接拉 10-K PDF 补。
