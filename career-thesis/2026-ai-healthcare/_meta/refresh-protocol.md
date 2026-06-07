---
title: Refresh Protocol - 6/12 个月后如何更新这份研究
purpose: 时间过去后哪些字段会过期、按什么顺序 refresh、如何 incremental 更新而不是从头重做
version: 1.0 (2026-05-16)
status: stable
---

# Refresh Protocol

## 字段衰减时间表

| 字段 | 衰减速度 | refresh 频率建议 | 信号 |
|------|----------|------------------|------|
| `latest_valuation_usd_m` | **快** (3-6 月) | 每季度 | 私募轮次 ≥ Series D 的公司，估值波动大 |
| `total_funding_usd_m` | 中 (6 月) | 每半年 | 看公司有没有新一轮 |
| `revenue_usd_m` | **快** (季度) | 每季度 | 上市公司每季度 10-Q；私募靠披露 |
| `revenue_yoy_pct` | 快 | 同上 | |
| `status` | 中 | 每半年 | 主要 catch 死亡 / 被收购 |
| `latest_round_date/type` | 中 | 每半年 | |
| `payer_type` | 慢 (年) | 每年 | 商业模式很少变 |
| `business_model` | 慢 | 每年 | |
| `moat_type` | 慢 | 每年 | |
| `founders_*` | 几乎不变 | 仅创始人离职 | |
| `tech_dna` | 慢 | 每年 | |
| `hardware_component` | 慢 | 每年 | |
| `china_counterpart*` | 中 | 每半年 | 中国对应公司也在变化 |
| `entry_paths` | 中 | 每半年 | 公司 hiring 节奏变化 |

## Refresh 流程（每半年一次）

### Step 1: 准备（10 min）

```
# 创建当日 snapshot
cp data/companies.csv data/snapshots/companies-YYYY-MM-DD.csv

# 读 decision-frame.md 确认 Nick 的 thesis 没变
# 如变了 → 走"重大变化"流程，可能要归档重做
```

### Step 2: 数字字段批量 refresh（30-60 min）

按字段 batch 处理，效率高于按公司 row by row：

1. **上市公司** (status=public): 直接读最新 10-K/10-Q。Tempus AI, HeartFlow, Recursion, Hims, GRAIL, Guardant 等
2. **大型私募** (latest_valuation >$1B): 查 "[name] funding 2026" + "[name] valuation"
3. **中型私募** ($200M-$1B): 同上但用 Sacra / CB Insights
4. **小型/长尾**: 只检查 status（还活着吗？）

每个字段更新后 `data_as_of` 同步更新到当日。

### Step 3: 状态变化 audit（15 min）

```python
# 找出 6 个月内可能死亡 / 被收购的公司
# 信号: 估值倒挂、裁员、停止 hiring、新闻沉默
```

特别关注：
- pandemic-era cohorts（2020-2021 成立但 2024-2026 无新轮）
- 创始团队大变动
- 主要客户流失

### Step 4: Universe update（30 min）

跑一次 discovery query 看有没有新公司进入 universe：

```
"healthcare AI startups 2026 funding"  
"medical AI new unicorns 2026"
```

新出现的公司 → 过资格筛（methodology.md）→ 入库。

### Step 5: 段级 narrative 更新（每段 15 min）

读每个 `0X-segment.md` 的"风险信号"和"数据补充建议"节，针对性更新。
不重写整篇，只更新过期段落 + 加 ## Update YYYY-MM 节追加新发现。

### Step 6: 统计 refresh（30 min）

重跑 `02-us-statistics/` 里的所有分析，比较 6 个月前 vs 现在的差异。
**主要看 delta，不看绝对值。** 例如：
- 哪个段中位估值涨了 / 跌了？
- 段内 mortality 增加了几家？
- capital efficiency 排名变化？

### Step 7: 重读 decision-frame.md 的"什么会让结论改变"表

走一遍 trigger list。任何一个 trigger 击中 → 在 `04-synthesis/elevator-map.md` 加 ## Refresh YYYY-MM 节，说明结论是否需要调整。

### Step 8: 写一份 refresh-log

```
_meta/refresh-log/YYYY-MM.md
```

记录：
- 触发本次 refresh 的原因（routine / Nick 主动 / trigger 击中）
- 改了哪些行 / 哪些字段
- 发现的重大变化
- 对 Nick 主线 thesis 的含义（如有）

## 重大变化流程

如果 decision-frame.md 的 trigger 列表击中 ≥ 1：

1. **暂停 routine refresh**
2. 把当前 CSV 复制到 snapshots/ 作为"重大变化前 baseline"
3. 重读 decision-frame.md，问 Nick：你的 thesis 还成立吗？
4. 等 Nick 回答后才继续

## Time budget

- Routine 半年 refresh：~3-4 小时 agent 工作 + Nick 半小时 review
- 不靠批量自动化（数据源都需要人脑判断 cross-validate）

## 不要做的事

- ❌ 直接覆盖 CSV——先 snapshot 再改
- ❌ 删 row（已死的公司也留着，标 status=dead）
- ❌ 改 schema 列名（要改必须升 schema.md 到新 version + retrofit 所有历史 snapshot）
- ❌ 一次性 refresh 所有 60+ 公司——分批，每段 batch
- ❌ 在 refresh 时引入新的 segment / 新的 column（这是单独的 task，不和 refresh 混）
