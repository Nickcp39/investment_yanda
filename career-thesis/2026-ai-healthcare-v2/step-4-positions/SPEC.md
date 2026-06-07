---
step: 4
title: Positions — 高 fit rent point 对应的具体公司 × 角色
input_from: step-3-rent-capture-and-fit
output_to: step-5-money-lens-check
status: spec-only
---

# Step 4 SPEC: Positions

## 1. Question

**对 step 3 中 final_priority = high 或 med 的 rent point，具体哪些公司 × 角色是 Nick 可以投递 / 加入 / 创业 / 学习的入口？每个 entry path 的 effort 估计、12 月内 hiring 信号、典型薪酬范围、职业曲线？**

## 2. Input

必读:
- `_methodology/process-overview.md`
- `_methodology/handoff-protocol.md`
- `step-3-rent-capture-and-fit/work/nick-fit-overlay.csv` (筛 final_priority >= med 的 rent point)
- `step-3-rent-capture-and-fit/work/insights.md`
- `_personal/nick-profile.md`

参考:
- v1 (`../2026-ai-healthcare/data/companies.csv` + `china_companies.csv`) 已有 ~95 公司事实数据，可作为 candidate pool 起点 — **必须重新验证公司当前状态**（v1 数据 as of 2026-05-16，可能已 stale）

禁读:
- step-5 work/

## 3. Output

### 3.1 主 artifact: `step-4-positions/work/candidate-positions.csv`

每个 (公司 × 角色) 组合一行:
```
position_id, rent_point_id (from step 3), company_name, company_geography,
role_type, role_title_examples, role_seniority_range,
entry_path_description (free text),
effort_to_enter (low/med/high), effort_basis,
hiring_signal_2025_2026 (active/passive/none/unknown), hiring_signal_source,
salary_range_usd_or_rmb, salary_basis,
career_arc_3y, career_arc_10y,
disqualifier_hit, notes, sources
```

字段说明:
- `role_type` enum: engineer / research_scientist / clinical_app_specialist / clinical_PM / PM_general / BD / medical_affairs / regulatory_affairs / international_business / consultant / founder
- `entry_path_description`: 具体怎么进（"投联影智能国际业务部门，先做海外注册专员，2 年后转 international product manager"）
- `hiring_signal_2025_2026`: 公司过去 12 月该 role_type 是 hiring 还是冻结
- `career_arc_3y` / `career_arc_10y`: 从这个 position 出发，3 年/10 年典型路径

### 3.2 deep dive: `step-4-positions/work/top-5-deep-dive/{position_id}.md`

仅对 final_priority = high 且 step 4 thread 验证后 effort != high 的 top 5 position 做 deep dive。每份 ≤ 2 页:

```markdown
---
position_id: ...
company: ...
role_type: ...
---

# {position_id}: {company} - {role_type}

## 这个 position 是什么
## 为什么对 Nick high fit
## entry 具体动作（months 1-3, 3-12, 12-24）
## 风险信号 (red flags)
## exit options (3y, 10y)
## sources
```

### 3.3 STATUS.md

## 4. Method

### candidate 来源
1. step 3 中 final_priority = med / high 的 rent point → 对应 segment + actor type 已知
2. 在该 segment × actor type 内拉 top 公司清单（v1 数据 + 当前 LinkedIn/招聘网站 cross-check）
3. 对每家公司列 1-3 个 role_type 候选

### Hiring 信号验证
- LinkedIn jobs / 脉脉招聘 / 公司 careers 页
- 过去 12 月该 role_type 在该公司发了多少 JD
- 如该公司过去 12 月有裁员新闻 → hiring_signal = none

### Salary 数据
- US: levels.fyi / glassdoor / Blind
- China: 脉脉脉宝 / 看准网 / 同行交流
- 估计区间，不要单点。低 quality 标 estimate-only

### 不做 ranking
本 step 不给最终 "Nick 该选哪个" 排名（step 5 only）。本 step 仅产出 candidate list，按 step 3 的 final_priority 排序即可。

## 5. Pruning
本 step 不 prune segment（已在 step 1）。但允许 position 级标记:
- 触发 disqualifier (nick-profile.md §6) → 标 `disqualifier_hit` 但不删行
- effort = high 但 unfair_advantage low → 不删，让 step 5 review

## 6. Validation

- [ ] candidate-positions.csv 行数 ≥ step 3 中 final_priority>=med rent points × 平均 2 个 position
- [ ] top-5-deep-dive 数量 ∈ [3, 5]
- [ ] 每行 hiring_signal 有 source 或标 `unknown` 不瞎写
- [ ] 每行 salary 有 source 或标 `estimate-only`
- [ ] STATUS.md = validated

## 7. Anti-patterns

- ❌ 给出 "Nick 应该首先投 X 公司" 结论
- ❌ 写"5-15 年人生 roadmap"类 elevator-map（v1 已被否决，不重蹈）
- ❌ 列 > 5 个 deep dive（focus 是 step 4 的设计原则）
- ❌ 把 v1 的红旗清单 / PM 路径分析 / 个 case study 直接复制粘贴
- ❌ 提议新的 rent point（应该在 step 3 done）

## 8. Money lens

> "我列的 candidate position 的真实付费 source 是什么？这个 source 的预算是在涨还是缩？这个 position 是否在公司 strategic 重点上（公司投资增长方向 vs 维持运营）？"

如该 position 的所在 team 公司近期裁员或冻结预算 → 在 candidate-positions.csv notes 列 flag。

## 9. Effort hint

- 假设 step 3 给出 final_priority>=med 的 rent points ~10 个
- candidate-positions: 10 rent × 2 candidates × 1 role = 20 positions
- top-5 deep dive: 5 × 0.5 天 = 2.5 天
- candidate list: 20 × 0.5 小时 verification = 10 工时
- 总: ~1 周 calendar time
- 可并行 (subagent per rent point family)，~3-4 天
