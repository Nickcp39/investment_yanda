# PBM Research — Search Log

> 每次 search 都在这里 append 一行：时间、query、目的、关键 URL 命中、key 摘录。
> 不省略 raw 数据，因为 chat 一压缩就丢。

---

## Phase 1A: 三家 PBM 母公司 10-K segment data

### 启动时间
2026-05-16

### 目的
拿到 CVS Caremark / Express Scripts (Evernorth) / OptumRx 三家 PBM 业务在母公司财报中的 **真实** segment 收入 + 营业利润 + EBITDA + 增速。

这是 PBM 立法 financial impact 模型的 baseline。

### 计划 query
1. CVS Health 2024 10-K Pharmacy Services Segment revenue operating income
2. Cigna Evernorth 2024 segment financials Express Scripts
3. UnitedHealth Optum Rx 2024 segment revenue earnings
4. CVS Caremark vs Express Scripts vs OptumRx 2024 EBITDA segment comparison

### 结果

#### 2026-05-16 Phase 1A Batch 1 (4 searches)
- ✅ CVS Pharmacy & Consumer Wellness（误，应找 Health Services） → 拿到 P&CW $124.5B
- ✅ Cigna Evernorth $111.8B PBS revenue
- ✅ UNH Optum total $253B, Optum Rx +15%
- ✅ Cross-comparison Drug Channels link 拿到
- raw 保存：`1A-pbm-母公司-10K-segment-batch1.md`
- 缺口：CVS Health Services 详细、Cigna Specialty 拆分、Optum Rx 绝对 $

#### 2026-05-16 Phase 1A Batch 2 (4 searches)
- ✅ CVS Health Services $173.6B (-7.1%), Adj OI $7.2B (-0.9%)
- ✅ Cigna Evernorth 拆分：Pharma Benefit $111.8B + Specialty $90.3B = $202.1B (+32%)
- ✅ Cigna Q4 单季 ESI $1.2B + Spec $948M operating income
- ✅ UNH Optum 拆三段：Health $105.4B + Rx ~$133B + Insight ~$15B = $253B
- ✅ CVS Health Services 4.15% margin confirmed
- raw 保存：`1A-pbm-母公司-10K-segment-batch2.md`

#### Phase 1A 总结
- 8 searches 完成
- 30+ 数据点收集
- 三家 PBM segment 财务 baseline 建立
- 仍缺：Optum Rx 绝对 revenue (推算 $130-133B); Evernorth 全年 OI (Q4 推算 $8-9B)
- 这些缺口可以用 WebFetch 直接拉 10-K PDF 补，留到 Phase 1F

---

## Phase 1B: FTC 2nd Interim Report deep extract

**计划时间**: 2026-05-16
**目的**: 从 FTC 2025-01 第二份报告里 extract 具体引文、数字、案例
**计划 query**:
1. FTC PBM second interim report specialty generic markup percentage Tadalafil
2. FTC PBM 2025 report key findings affiliated pharmacy reimbursement
3. FTC PBM report $7.3 billion specialty $1.4 billion spread pricing
4. WebFetch FTC PBM 2nd interim report PDF
