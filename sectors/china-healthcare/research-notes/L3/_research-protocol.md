# L3 流通与零售 — 真研究 protocol

> 创建：2026-05-16
> 标准：像财报分析师做行业调研一样，不是直觉综合
> 标的：sectors/china-healthcare/各层工作机会矩阵.md 的 L3 章节

## 4 phase 流程

### Phase 1 收集（Collect，30-50 searches 分 6 批）

每次搜索的 raw 结果**全部**保存到 `raw-searches/{topic}-{seq}.md`，包含：
- query 原文
- 搜索时间
- 返回的所有 URL
- 关键摘录原文（不综合）

| 批 | 主题 | 搜索数 |
|---|---|---|
| 1A | 流通巨头（国药/上药/华润/九州通）员工 + 营收 + 业务结构 | 8 |
| 1B | 4 大连锁（大参林/益丰/老百姓/一心堂）员工 + 门店 + 财务 | 6 |
| 1C | 互联网医药（京东健康/阿里健康/拼多多）员工 + GMV + 业务 | 6 |
| 1D | DTP + 双通道 + 思派/镁信/圆心 财务详细 | 6 |
| 1E | 智慧供应链 / 物流 AI 真实项目 + 投入 | 4 |
| 1F | 真实 JD + 知乎/小红书 insider quotes | 8-10 |

### Phase 2 提取（Extract）

把所有数据点入 `data/sources.csv` 增加 L3.* 行：
- block / data_point / value / unit / as_of / source_type / source_url / note
- source_type: P1_annual_report / P2_industry_report / P3_news / P4_insider / P5_estimate
- 一个数字一行；冲突源也都入库

### Phase 3 派生计算（Analyze）

`data/analysis/` 下分别建：

| 文件 | 内容 |
|---|---|
| `L3-DTP-CAGR-reconciliation.csv` | DTP 2019=345 → 2024=872 实际 CAGR = X%，行业宣称 2028=5000 隐含 Y% CAGR，两者差距分析 |
| `L3-productivity-comparison.csv` | 京东健康 vs 阿里健康 vs 拼多多 单人产出比 + 行业含义 |
| `L3-margin-trajectory.csv` | 行业利润率 2010 → 2023 + 4 大流通商单独 trajectory + 投影 |
| `L3-employment-bottoms-up.csv` | 4 流通 + 4 连锁 + 互联网 + DTP + 物流 真实员工数加总 → L3 总就业 真值 |
| `L3-salary-real-vs-estimated.csv` | 真实 JD 抓取的薪资带 vs 我之前估算 |
| `L3-channel-shift-projection.csv` | 处方外流：医院 → 药店 / DTP / 互联网 流量分配 + 2028 投影 |

### Phase 4 综合（Synthesize）

重写 `各层工作机会矩阵.md` L3 章节：
- 每个 claim 标 source id（如 [L3.A.05] 指向 sources.csv 的具体行）
- 把"估算"和"实证"分开标
- 真实 JD 直接 quote 原文
- insider voice 直接 quote 知乎/小红书 原文（带帖子链接）
- 派生计算放在新的 3.12 节

## 不做的事

- 不在 Phase 1 综合
- 不让 P5_estimate 数字流到结论
- 不引用没保存原文的源
- 不写"~XX 万"如果不能用 bottoms-up 加出来

## 进度跟踪

更新本文件 + TodoWrite
