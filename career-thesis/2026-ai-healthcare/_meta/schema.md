---
title: companies.csv schema 定义
purpose: 每列的定义、枚举值、抓取规范、空值处理。改 CSV 之前先读这里。
version: 2.0 (2026-05-16)
status: stable
---

# CSV Schema v2.0

`data/companies.csv` 是本研究的 single source of truth。所有 md 分析都基于这个 CSV 派生。

## 23 列定义

### 标识 (4 列)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | ✅ | 公司名（官方名，不用 ticker）|
| `segment` | enum | ✅ | S1-S7（见下方枚举）|
| `subsegment` | string | 选填 | 段内细分（自由字符串，建议复用现有值）|
| `founded_year` | int | ✅ | 创立年份 |

### 地理 + 状态 (3 列)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `hq_country` | enum | ✅ | US / China / Israel / UK / France / Australia / Canada / Other |
| `hq_city` | string | 选填 | SF, Boston, NYC, Beijing, Shanghai... 用于"jobs concentrated where" |
| `status` | enum | ✅ | private / public / acquired / dead |

### 资本 (5 列)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `latest_valuation_usd_m` | float | 选填 | 私募 = 最近一轮 post-money；上市 = 市值；空 = 未披露 |
| `total_funding_usd_m` | float | ✅ | 累计私募融资。上市后的 follow-on 不算 |
| `latest_round_date` | YYYY-MM | ✅ | 最近一次融资 / IPO / 收购的日期 |
| `latest_round_type` | enum | ✅ | Seed / A / B / C / D / E+ / IPO / Acquired / Dead |
| `revenue_usd_m` | float | 选填 | ARR 优先；如是年营收，在 notes 标 "annual" |

### 商业 (4 列)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `revenue_yoy_pct` | float | 选填 | YoY 增长率（%），如 100 表示 2x |
| `payer_type` | enum | ✅ | hospital / insurer / pharma / patient / employer / govt / mix |
| `business_model` | string | ✅ | 自由文本但优先用：per_user_subscription, per_outcome, data_licensing, smb_saas, enterprise_subscription, platform_per_outcome |
| `moat_type` | enum | ✅ | data / regulatory / integration / brand / network / IP / hardware / scale |

### Career 信号 (5 列 v2 新增 + 2 列 v2.1 新增)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `founders_phd_count` | int | 选填 | 创始团队中博士数量。"未知" 留空 |
| `founders_background` | string | 选填 | 短 tag。例: "Stanford CS PhD + ex-Google" / "MD + serial entrepreneur" / "ex-Epic engineer + MD" |
| `tech_dna` | enum | 选填 | algorithm / data / hardware / clinical / hybrid |
| `hardware_component` | enum | 选填 | none / paired_device / embedded_in_device |
| `nick_notes` | string | 选填 | 任何对 Nick 决策有价值的备注 |
| `entry_role_paths` | string | 选填 (v2.1) | 这家公司对 Nick 可能的 entry role 列表，按 effort 由低到高排。格式: 逗号分隔短 tag。例: `"clinical_PM, engineer, BD"` / `"engineer, research_scientist"` / `"clinical_app_specialist, PM"`。tag 词汇集见下方 |
| `pm_demand_signal` | enum | 选填 (v2.1) | 该公司近 12 个月 PM 招聘活跃度：`high` (active hiring) / `med` / `low` / `unknown`。优先看 LinkedIn jobs 或脉脉 |

**`entry_role_paths` tag 词汇集（请复用，不要发明新词）:**
- `engineer` — ML / SWE / 算法工程师
- `research_scientist` — 研究科学家（PhD 偏 research 岗）
- `clinical_app_specialist` — 临床应用专家
- `clinical_PM` — 医疗产品经理
- `PM` — 通用产品经理（非医疗特化）
- `BD` — 商务拓展 / 客户成功
- `medical_affairs` — 医学事务（biotech 特有）
- `regulatory_affairs` — 法规事务
- `international_business` — 国际业务（出海岗）

### 中国映射 (3 列，Phase 3 填)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `china_counterpart` | string | 选填 | 中国对应公司名（可能多家，逗号分隔）|
| `china_counterpart_overseas_status` | enum | 选填 | none / planning / active / na |
| `entry_paths` | string | 选填 | 自由文本：可能进入这家/这个段的路径列表（"China R&D 上海" / "via 联影出海" / "academic spinout 路径"...）|

### 元数据 (1 列)

| 列名 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `data_as_of` | YYYY-MM-DD | ✅ | 这一行数据最后一次更新的日期 |

## Segment 枚举（稳定）

| Code | Name |
|------|------|
| S1 | Clinical Documentation / AI Scribe |
| S2 | Clinical Decision Support / Medical LLM |
| S3 | Precision Medicine / Diagnostics |
| S4 | Drug Discovery AI |
| S5 | Medical Imaging AI |
| S6 | Revenue Cycle / Admin AI（含 prior auth, RCM, patient access）|
| S7 | Consumer / Virtual Care AI |

横跨多个段的公司：写 `S1+S6` 这种格式（按主段排前）。

## 空值规则

- **数字字段:** 空 = 未披露。不要填 0、N/A、unknown。
- **enum 字段:** 空 = 未调研。`na` = 已确认不适用。
- **必填字段为空:** 整行需要标 review

## sources.csv

每个非空数据点都要在 `data/sources.csv` 记一行：

| 列 | 说明 |
|---|---|
| `company` | 对应 companies.csv 的 name |
| `field` | 字段名 |
| `value` | 数据值 |
| `source_url` | 引用 URL |
| `source_title` | 文章标题 |
| `fetched_date` | YYYY-MM-DD |
| `confidence` | high / med / low（cross-validated = high，单一二级源 = med，自媒体 = low）|

只记关键字段：`latest_valuation_usd_m`, `total_funding_usd_m`, `revenue_usd_m`, `latest_round_date`。其他字段可以从对应段 md 文件追溯。

## 版本控制

每次 CSV 有 ≥ 5 行修改 / 添加，运行：

```
cp data/companies.csv data/snapshots/companies-YYYY-MM-DD.csv
```

保留全部历史 snapshot，不覆盖。
