---
title: 数据采集方法论
purpose: 资格筛规则、source 优先级、cross-validation 准则、查询模板。Fresh agent 加数据之前先读这里。
version: 1.0 (2026-05-16)
status: stable
---

# 数据采集方法论

## 资格筛（universe 候选 → 进库）

候选公司池从行业报告 + 段头部清单中收集，估计 universe 约 150 家。
进入 `companies.csv` 必须满足**以下任一条**：

✅ **INCLUDE if any:**
1. 有公开披露的 revenue / ARR / 用户量
2. Series B 或更晚轮次
3. 上市公司
4. 显著被收购（acquisition price > $50M）
5. 显著死亡 / 破产 / 解散（作为存活率统计样本和 cautionary tale）
6. 创立 < 3 年但累计融资 ≥ $50M（rising star）

❌ **EXCLUDE if:**
- 完全 stealth，没有任何公开信息
- 累计融资 < $5M 且创立 > 5 年（failed-to-launch）
- 纯消费 wellness 且无 AI/ML 核心（如 Oura 之类）
- 横跨多个非 AI 段且 AI 只是营销标签

❗ **不能 EXCLUDE 的理由（重要）:**
- ❌ "Nick 难进" / "太大公司了进不去" → 这是 entry_paths 字段要描述的，不是筛选条件
- ❌ "中国没有对应公司" → 这是 china_counterpart 字段要记录的，不是筛选条件
- ❌ "估值过低不值得 Nick 关注" → 反例：Forward Health 已死，但是 cautionary tale 必须收录

理由：详见 `_meta/decision-frame.md` "不靠成功率思考"。

## 目标样本量

按 segment 配 ~10 家，总计 60-70 家。每段内部分层：

- Tier 1 (头部，>$1B 估值或 $500M 累计融资): ~3 家
- Tier 2 (中部，$200M-$1B 估值): ~4 家
- Tier 3 (新兴 / 已死 / 长尾): ~3 家

允许小幅倾斜：S5 Medical Imaging（Nick 背景对口）可以加到 12-15 家。

## Source 优先级（沿用 sources/source_policy.md）

| Tier | 类型 | 用于 |
|------|------|------|
| 1 | SEC 10-K/10-Q/S-1（上市公司）+ 公司官方公告 | 永远优先；不需要 cross-validate |
| 2 | Rock Health / CB Insights / Pitchbook / Menlo VC / Sacra | 主要数据源；推荐 cross-validate |
| 3 | TechCrunch / StatNews / Fierce Healthcare / Healthcare Dive / Modern Healthcare / Forbes / WSJ / Bloomberg | 必须 cross-validate；带日期 |
| 4 | 行业 newsletter / HIT Consultant / MobiHealthNews | OK 用于 sanity check |
| 5 | aifundingtracker / newmarketpitch / 类似聚合器 | **不可信**！发现 Nabla 估值被错报为 $5.3B（实际 $180M）。仅作 candidate discovery，数据必须再去 Tier 1-3 验证 |
| 6 | Twitter / Reddit / blog | 不入库；仅作信号 |

## Cross-validation 规则

每个 `latest_valuation_usd_m` / `total_funding_usd_m` / `revenue_usd_m` 数据点：

- **High confidence:** Tier 1 直接披露，或 ≥ 2 个 Tier 2-3 独立来源一致
- **Med confidence:** 单一 Tier 2 来源，或多个 Tier 3 一致
- **Low confidence:** Tier 4-5 单一来源，或 Tier 2-3 之间冲突且无法 resolve

冲突时优先：Tier 1 > Tier 2 > Tier 3 一致多数 > Tier 3 单一 > Tier 5 排除。

任何 Low confidence 数据点：在 notes 字段标 `[LOW CONFIDENCE]`。

## 时效

- 所有数字必须带日期（`latest_round_date` 或 notes 中标注 "as of YYYY-MM"）
- 任何超过 12 个月的估值数据，在 notes 标 `[STALE >12mo]`
- 公司状态（private/dead）每次 refresh 必须重核

## 查询模板（可复用）

### Discovery 阶段（找候选公司）

```
"top [SEGMENT] AI healthcare startups 2025 funding list"
"[SEGMENT] AI companies revenue ranking 2025"
"Rock Health [SEGMENT] 2025 report"
"Menlo Ventures state of AI healthcare 2025"
```

### Fill 阶段（补单家公司数据）

```
"[COMPANY NAME] valuation funding 2025"
"[COMPANY NAME] Series [X] round"
"[COMPANY NAME] revenue ARR disclosed"
"[COMPANY NAME] CB Insights Sacra"   # 这两家有结构化页面
```

### Cross-validate 阶段

- StatNews: 临床/医疗 newsletter，记者跑会议消息源
- Sacra: 私募估值/ARR 估算（标注是估算）
- 公司官网 + LinkedIn Crunchbase profile

## 反 anti-pattern

- ❌ 不要一次 batch 8 个段并行。先 1 段，校准 schema 再推进
- ❌ 不要把"aifundingtracker 列表"当 source of truth，那是 candidate pool 不是 fact
- ❌ 不要在 md 里直接写 "Abridge 估值 $5.3B"，要写 "估值 $5.3B（[StatNews 2025-06](url)）"
- ❌ 不要为了凑 60 家忽略 IBM Watson Health 这种"死过来回的"——这种正是 survival analysis 的关键样本
