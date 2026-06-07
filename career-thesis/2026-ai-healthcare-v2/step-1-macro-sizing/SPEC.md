---
step: 1
title: Macro Sizing — US + China AI healthcare 各子赛道当前营收 + 10y CAGR
input_from: none (起点)
output_to: step-2-value-chains
status: spec-only (no thread has executed)
---

# Step 1 SPEC: Macro Sizing

## 1. Question

**US + China AI healthcare 各子赛道，当前营收多少？10 年 CAGR 多少？10 年预测多少？哪些子赛道按 pruning 规则被 drop？**

## 2. Input

必读:
- `_methodology/process-overview.md`
- `_methodology/handoff-protocol.md`
- `_methodology/pruning-rules.md`

参考（可选）:
- v1 (`../2026-ai-healthcare/01-us-landscape/00-segment-map.md`)的市场数据可作为起点，但必须**重新验证**所有数字（v1 数据 quality 标签 inconsistent）

禁读:
- v1 的 elevator-map / pm-pathways / 任何 synthesis 类文件
- `_personal/nick-profile.md`（profile 不应污染 macro 分析）

## 3. Output

### 3.1 主 artifact: `step-1-macro-sizing/work/segments-ranked.csv`

schema:
```
segment_code, segment_name_en, segment_name_zh,
us_current_market_usd_m, us_10y_cagr_pct, us_forecast_2036_usd_b, us_data_quality, us_sources,
cn_current_market_usd_m, cn_10y_cagr_pct, cn_forecast_2036_usd_b, cn_data_quality, cn_sources,
keep_or_drop, drop_reason, escape_valve_reason, notes
```

字段说明:
- `segment_code`: S1, S2, ... S11+ (复用 v1 命名，新段从 S12 起)
- `keep_or_drop`: keep / drop / escape (escape = 触发 pruning 但 flag 例外)
- `drop_reason`: 如果 drop，写哪条 pruning rule 触发（如 "us_10y_cagr < 15%"）
- `escape_valve_reason`: 如果 escape，写 pruning-rules.md §例外规则 中的哪条
- `data_quality`: high (>=2 primary sources agree) / med (1 primary or 2 secondary) / low (single secondary or older than 12mo) / estimate-only (no source, qualitative估计)

### 3.2 配套 artifact: `step-1-macro-sizing/work/sources.csv`

每个 data point 一行，schema:
```
segment_code, geography, field, value, source_url, source_title, fetched_date, confidence
```

### 3.3 STATUS.md: `step-1-macro-sizing/work/STATUS.md`

按 handoff-protocol §STATUS.md 格式。

### 3.4 narrative 总结: `step-1-macro-sizing/work/summary.md`

**≤ 1 页**。仅包含:
- 段共看了多少个
- keep N 个 / drop N 个 / escape N 个
- 数据质量分布
- 任何 step 1 thread 觉得 Nick 应该知道的 anomaly（不要给 recommendation）

## 4. Method

### 数据源优先级
1. 一级（primary）: 公司 10-K / 招股书 / 公司公告
2. 一级: 政府数据 (CMS NHE, FDA databases, 国家统计局, 国家医保局)
3. 二级 (secondary): Rock Health, CB Insights, Pitchbook, Menlo VC, McKinsey, Frost & Sullivan, 灰盒报告
4. 三级 (tertiary): TechCrunch, StatNews, Fierce Healthcare 等行业新闻（仅作交叉验证）
5. 四级（不推荐）: aifundingtracker, newmarketpitch 等 aggregator — v1 已发现这类源有错（Nabla val 错报）

### 推荐分析方法
- 对每个 segment：先找 segment-level market sizing report（McKinsey / Frost / Grand View / Mordor / 灰盒），再 cross-check top 3-5 公司营收
- 10y CAGR：优先用 sector report 的 forecast；如无，用过去 3-5 年实际增长 extrapolate（标 `data_quality: estimate-only`）
- China 数据通常 underreported，预期 70% 段 China 数据为 med 或 low quality

### Pruning 执行
按 `_methodology/pruning-rules.md` 执行。drop 一律打 `drop_reason`，escape 一律打 `escape_valve_reason`。

## 5. Pruning

仅本 step 执行 pruning（见 SPEC §3.1 `keep_or_drop` 列）。
**Pruning 规则不在本 SPEC 重复，唯一 source of truth 是 `_methodology/pruning-rules.md`。**

## 6. Validation

step 1 output 可以传给 step 2 的判据：

- [ ] `segments-ranked.csv` 每行 schema 完整
- [ ] 每个 keep / escape 段至少 1 个 primary 或 high-quality secondary 源
- [ ] `sources.csv` 行数 ≥ `segments-ranked.csv` 中 keep+escape 段数 × 4（min 4 sources per surviving segment）
- [ ] `summary.md` ≤ 1 页
- [ ] STATUS.md = validated

如果以上有 X 不达标 → STATUS.md = blocked，写明哪条不达标。

## 7. Anti-patterns

- ❌ 给出 "S5 最值得 Nick 关注" 类结论（Nick fit 是 step 3，本 step 不动）
- ❌ 列具体公司清单（公司层在 step 2 / 4）
- ❌ 分析 business model（这是 step 2 / 3 的事）
- ❌ 自创新 segment 但不在 STATUS.md 标注 + 给出加入理由
- ❌ 用 v1 的结论作为 "现成 anchor"（v1 已被否决，事实数据可参考但结论一律不复用）
- ❌ 单源数据被 keep（必须至少 cross-check 1 次，否则 data_quality = low）

## 8. Money lens

完成本 step 末尾问：

> "我有没有把 'AI 公司融资额' 和 'AI 公司营收' 混在一起？哪些段我报的是融资数字（资本流入）而不是真实付费方付的钱（市场规模）？"

如果发现混淆，标 `data_quality: low` + 在 sources.csv 加 confidence: low。

## 9. Effort hint

- 单 thread 顺序跑: ~3-5 天 calendar time
- 并行 (US thread + China thread): ~2 天 + 0.5 天 merge
- 11 段 × 平均 4 sources × 平均 30 分钟搜索/验证 ≈ 22 工时
