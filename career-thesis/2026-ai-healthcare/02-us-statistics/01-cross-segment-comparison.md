---
title: 跨段比较 — 中位估值 / 中位融资 / 中位营收
generated: 2026-05-16
source: scripts/ai_healthcare_stats.py
---

# Phase 2.1 跨段比较表

| 段 | 公司数 | 累计融资 ($B) | 累计营收 ($B) | 中位融资 ($M) | 中位估值 ($M) | 中位营收 ($M) | 上市数 | 死亡数 |
|----|--------|---------------|---------------|---------------|---------------|---------------|--------|--------|
| S1 Clinical Documentation | 11 | $2.63 | $0.10 | 165.0 | 1,250.0 | 100.0 | 0 | 0 |
| S2 Clinical Decision Support | 6 | $1.22 | $0.15 | 30.0 | 7,750.0 | 150.0 | 0 | 0 |
| S3 Precision Medicine | 9 | $1.50 | $7.48 | 750.0 | 5,300.0 | 982.0 | 7 | 0 |
| S4 Drug Discovery AI | 10 | $7.35 | $0.07 | 621.5 | 1,500.0 | 74.7 | 4 | 0 |
| S5 Medical Imaging AI | 16 | $3.16 | $0.14 | 175.5 | 1,520.0 | 136.0 | 2 | 0 |
| S6 Revenue Cycle / Admin AI | 10 | $1.60 | $0.00 | 120.0 | 4,000.0 | — | 1 | 1 |
| S7 Consumer / Virtual Care | 8 | $3.45 | $2.40 | 460.0 | 3,300.0 | 2,400.0 | 1 | 3 |

## 排序分析

### 按累计营收排（商业化成熟度）
1. **S3 Precision Medicine**: $7.48B
2. **S7 Consumer / Virtual Care**: $2.40B
3. **S2 Clinical Decision Support**: $0.15B
4. **S5 Medical Imaging AI**: $0.14B
5. **S1 Clinical Documentation**: $0.10B
6. **S4 Drug Discovery AI**: $0.07B
7. **S6 Revenue Cycle / Admin AI**: $0.00B

### 按累计融资排（资本注入热度）
1. **S4 Drug Discovery AI**: $7.35B
2. **S7 Consumer / Virtual Care**: $3.45B
3. **S5 Medical Imaging AI**: $3.16B
4. **S1 Clinical Documentation**: $2.63B
5. **S6 Revenue Cycle / Admin AI**: $1.60B
6. **S3 Precision Medicine**: $1.50B
7. **S2 Clinical Decision Support**: $1.22B

### 按累计估值排（市场预期总和）
1. **S3 Precision Medicine**: $66.50B
2. **S1 Clinical Documentation**: $33.03B
3. **S7 Consumer / Virtual Care**: $24.40B
4. **S6 Revenue Cycle / Admin AI**: $16.45B
5. **S2 Clinical Decision Support**: $15.50B
6. **S4 Drug Discovery AI**: $5.20B
7. **S5 Medical Imaging AI**: $4.94B

## Nick 视角关键发现

- **S3 (Precision Medicine) 商业化最成立**: 累计营收 > 所有其他段加起来
- **S5 (Imaging AI) 资本与营收均衡**: 不是融资最多但有 IPO 范本 (HeartFlow)
- **S2 (CDS/LLM) 估值/营收差距最大**: 高估值多靠预期（OpenEvidence 80x ARR）
- **S6 + S7 是死亡冠军段**: 累计死亡资本 ~$2B