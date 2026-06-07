---
step: 3
title: Rent Capture Points + Nick Fit Injection
input_from: step-2-value-chains + _personal/nick-profile.md
output_to: step-4-positions
status: spec-only — REQUIRES Nick sign-off of _personal/nick-profile.md before execution
---

# Step 3 SPEC: Rent Capture + Fit

## 1. Question

**(a) 每条 value chain 上，rent extraction 点在哪？为什么是那里（toll booth / IP / network / regulatory）？AI 是 amplify 还是 disrupt？**
**(b) Nick profile 在每个 rent capture 点的 unfair advantage / effort 各多少？**

注：(a) 和 (b) 是 两个 sub-deliverable，可由 1 个 thread 串行做，也可 2 个 thread 分工（a 先做完，b 拿 a 的输出加 profile 注入）。

## 2. Input

必读:
- `_methodology/process-overview.md`
- `_methodology/handoff-protocol.md`
- `step-1-macro-sizing/work/segments-ranked.csv` (knowing which segments survived)
- `step-2-value-chains/work/{us,cn}/*-valuechain.md` (所有 surviving 段双地理 chain)
- `step-2-value-chains/work/actors-master.csv`
- `_personal/nick-profile.md` ⚠️ **仅 (b) sub-step 读，(a) sub-step 不读**

禁读:
- step-4 / step-5 的 work/
- v1 elevator-map 类结论

## 3. Output

### 3.1 sub-deliverable (a) — `step-3-rent-capture-and-fit/work/rent-points-ranked.csv`

每个 rent extraction point 一行:
```
rent_point_id, segment_code, geography, layer, actor_type, actor_examples,
extraction_mechanism, mechanism_basis, ai_impact (amplify/disrupt/neutral),
leverage_score (1-10), leverage_basis, durability_years_estimate,
notes, sources
```

字段说明:
- `extraction_mechanism` enum: toll_booth / ip_moat / network_effect / regulatory_capture / scale / data_lock_in / brand
- `leverage_score`: 1-10 主观但需 `leverage_basis` 文本解释（例: "公司 ROIC > 30% × 段增长 25% × 进入门槛 high"）
- `durability_years_estimate`: 5 / 10 / 20 / >20 — 这个 rent extraction 多久会被打破

### 3.2 sub-deliverable (b) — `step-3-rent-capture-and-fit/work/nick-fit-overlay.csv`

继承 rent-points-ranked.csv 所有列 + 附加 profile-injected 列:
```
... (all from 3.1) ...,
unfair_advantage_score (1-10), advantage_basis,
effort_to_enter (low/med/high), effort_basis,
disqualifier_hit, preference_misalignment,
final_priority (high/med/low — 仅 thread 的 RAW 信号，不是 recommendation)
```

`final_priority` 计算规则:
- high: leverage_score ≥ 7 AND unfair_advantage_score ≥ 7 AND effort != high AND no disqualifier
- med: leverage_score ≥ 5 AND advantage_score ≥ 5 AND no disqualifier
- low: 其他

注：`final_priority` 是机械计算的标签，不是建议。建议在 step 5 by human。

### 3.3 配套 narrative: `step-3-rent-capture-and-fit/work/insights.md`

**≤ 2 页**。包含:
- 跨段 / 跨地理的 rent capture pattern（哪些 layer 最赚钱，是否 US/CN 一致）
- AI amplify vs disrupt 的分布
- profile 注入后的 surprising findings（不是建议，是 observation）

### 3.4 STATUS.md

## 4. Method

### (a) Rent capture identification
对每条 valuechain.md，按 6 层走一遍，问每个 actor:
1. 它能收钱主要靠什么 mechanism？
2. 该 mechanism 的护城河深度？（用 5 种 moat type 分类）
3. AI 5-10 年会 amplify 还是 disrupt？
4. ROIC / 利润率 / 议价权 数据 → leverage_score

### (b) Nick fit overlay
按 `_personal/nick-profile.md` §7 规则，逐 rent point 评分。
**严格**: thread 不能新增 capability / preference / 排除项。如果觉得 profile 不完整，写在 insights.md 让 Nick review，**不要私自补充**。

## 5. Pruning
本 step 不 prune segment（已在 step 1 done）。但 rent points 自身 `final_priority = low` 的不删，留着供 step 5 review。

## 6. Validation
- [ ] rent-points-ranked.csv 行数 ≥ surviving segments × geographies × 平均 2 个 rent points
- [ ] 每行 leverage_basis 有具体数字 / 来源（不是空话）
- [ ] nick-fit-overlay.csv 每行 advantage_basis 引用 nick-profile.md 中的具体 §
- [ ] insights.md ≤ 2 页
- [ ] STATUS.md = validated

## 7. Anti-patterns

- ❌ 给 "Nick 应该去 X" 建议（step 5 only）
- ❌ 在 insights.md 拓展超出 rent points 之外的话题
- ❌ 重写 nick-profile.md（read-only）
- ❌ (a) sub-step 引用 profile 让 leverage_score 被 profile 污染
- ❌ unfair_advantage_score 一律打 7-8（无差异化的 inflation）
- ❌ 自创 extraction_mechanism 枚举外的值

## 8. Money lens

> "我标的 high leverage 点真的是钱沉淀的地方，还是只是营业额大？高营业额低利润率（如 distribution）不是 rent extraction，是 commodity pipeline。"

## 9. Effort hint

- 假设 surviving 段 6 × 2 geo = 12 chains × 平均 3 rent points = 36 rent points
- (a) 部分: ~3-4 天
- (b) 部分: ~1-2 天（profile 注入相对快）
- 总: ~5-7 天 calendar，并行收益有限（需要跨 chain 对比）
