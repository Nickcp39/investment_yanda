# &lt;Ticker&gt; Step 0 Search Plan

按 [frameworks/info_collection_pipeline.md](../frameworks/info_collection_pipeline.md)
执行阶段 Stage 1 产出。指导 Stage 2 (按 block 执行) 收集到 `raw/` 文件夹。

每项执行后回写 status。可跨会话恢复。

**Status 图例**: ⏸ pending · 🟡 in-progress · ✅ done · ⏭ skipped (acceptable gap) · ❌ blocked

最后更新: YYYY-MM-DD

---

## 已确认的事实 (Stage 0 Identify 输出)

来源: YYYY-MM-DD WebSearch on "..."

| 项 | 值 | Tier | Note |
|---|---|---|---|
| Legal name | | A1 | |
| Ticker | | A1 | |
| Exchange | | A1 | |
| IPO date | | A1 | |
| CIK | | A1 | |
| Sector / 子行业 | | A1 | |
| 主营产品 / 业务 | | A1 | |
| EDGAR 入口 | | A1 | |
| 公司 IR 入口 | | A1 | |
| 最近 SEC filing 日期 | | A1 | |
| 看出来的特殊情况 | | | 例: 年轻公司 / spinoff / 加密 / 跨境 / 重组 |

---

## 复杂度系数 + 时间预算

按 [info_collection_pipeline.md](../frameworks/info_collection_pipeline.md) 复杂度系数:
- 普通公司: 1.0× → 2.5-4.5 h
- 年轻 (< 5 年公开): +30%
- 加密 / 高度监管 / 跨境: +50%
- 双叠加: ~7-8 h

本公司系数: __ × → 预计 L1+L2 约 __ h

---

## 完整 Plan (Block 列表)

每个 block 完成后产出落到 `raw/block<N>_<name>.md`，按
[_raw_block_template.md](_raw_block_template.md) 结构。

### Block 1: Anchor identity ⏸
- [ ] 确认 ticker / exchange / IPO date / CIK / 主营业务

预计调用: 1-2 WebSearch · 5 min · 输出: `raw/block01_identity.md`
(若 Stage 0 已搞定可直接 ✅，identity 不另起 file)

### Block 2: EDGAR locate ⏸
- [ ] 列出 EDGAR 所有 filing types + 日期 (10-K / 10-Q / S-1 / 8-K / DEF 14A / Form 4)
- [ ] 确认 latest 10-K accession number
- [ ] 确认 latest 10-Q accession number
- [ ] 确认 (年轻公司) S-1 / S-1/A accession number
- [ ] 确认 latest DEF 14A accession number
- [ ] 扫 8-K title 列表 (最近 12 个月)，标记重要的

预计调用: 1 WebFetch · 5 min · 输出: `raw/block02_edgar_filings.md`

### Block 3: 最近 10-Q ⏸
- [ ] 财务概要 (revenue/GM/OM/FCF/cash/debt/股本)
- [ ] Risk factors 段重点 (3-5 条最重)
- [ ] MD&A 季度 highlight
- [ ] (行业专属指标，按业务模式)

预计调用: 2-3 WebFetch · 15 min · 输出: `raw/block03_latest_10q.md`

### Block 4: 10-K + (年轻公司) S-1 ⏸
- [ ] 10-K business overview / 完整年度财务 / risk factors / capital structure / related party
- [ ] (若适用) S-1 历史 audited financials (3 年 pre-IPO) / founder + 早期投资者持股 / use of proceeds

预计调用: 4 WebFetch · 30 min · 输出: `raw/block04_10k_s1.md`

### Block 5: 最近 call transcript ⏸
- [ ] 找最近 1 次 earnings call
- [ ] CEO 开场 / 分析师 Q&A 中关于核心问题的回答

预计调用: 1-2 WebSearch + 1-2 WebFetch · 15 min · 输出: `raw/block05_calls.md`

### Block 6: 市场位置 + 竞争 ⏸
- [ ] 行业 dashboard (按 info_collection_pipeline.md 行业 overlay 表)
- [ ] 1-3 家直接竞品最近一次财报口径

预计调用: 3-4 WebSearch + WebFetch · 20 min · 输出: `raw/block06_market_position.md`

### Block 7: Sell-side + 专业新闻 + 仓库 grep ⏸
- [ ] Yahoo Finance 一致预期 (consensus EPS / Revenue / 目标价)
- [ ] 3 篇过去 6 个月专业报道 (Bloomberg/Reuters/WSJ/FT/行业专门)
- [ ] 本仓库 grep: `notes/videos/` 内是否有该 ticker / 关键词 podcast notes

预计调用: 2-3 WebSearch + 1 Grep · 15 min · 输出: `raw/block07_news_sellside.md`

### Block 8: 监管 / 立法 ⏸
- [ ] 适用法规 + 立法时间表 (按行业)

预计调用: 2-3 WebSearch · 15 min · 输出: `raw/block08_regulatory.md`

---

## 砍掉的 (接受信息缺口，进 OPEN QUESTIONS / Stage 4 audit 决定是否触发 L3)

按 framework L3 触发表，以下默认砍掉，灵魂明确叫缺时再触发：

- 历史每年 1 季 call transcript 抽样 (年轻公司 N/A)
- 8-K 全扫 (只标 Block 2 中重要的)
- proxy 详读 (只取 URL 不 deep dive)
- Form 4 全史 (只看 IPO 后大额抛售)
- 13F 季度对比 (只看 top 5 holder snapshot)
- scuttlebutt 5 类 (留 L3)
- 学术 / BIS / IMF 报告 (留 L3)
- 历史 letter 全套 (留 L3)
- proxy 关联交易段详读 (留 L3)
- 信用债 spread / drawdown 详算 (留 L3)

---

## 总预计调用

| Block | WebSearch | WebFetch | 时间 |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |
| **合计** |  |  | **~__ h** |

---

## 执行节奏

每个 block 单独执行一次，期间 stop 让用户审视产出 + 决定是否 redirect 后续 block。

下一步: Stage 1 完成后 **stop**，等用户 confirm scope，再从 Block 1 (或下一个 ⏸) 启动 Stage 2。
