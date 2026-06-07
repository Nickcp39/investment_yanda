# Micron (MU) Step 0 Search Plan

按 [frameworks/info_collection_pipeline.md](../../frameworks/info_collection_pipeline.md)
执行阶段 **Stage 1 输出** (本文件)，指导 Stage 2 (按 block 执行) 把每 block
产出落到 `companies/mu/raw/block<N>_<name>.md`，按
[_raw_block_template.md](../_raw_block_template.md)。

每项执行后回写 status。可跨会话恢复。

**Status 图例**: ⏸ pending · 🟡 in-progress · ✅ done · ⏭ skipped (acceptable gap) · ❌ blocked

最后更新: 2026-05-27

---

## 触发上下文

2026-05-27 用户提到 "mu 今天涨疯了" — 大幅单日上行，催化未知。
本简报启动直接驱动是这次价格事件，但研究框架按完整 8-block 推进，
**不只回答"今天为什么涨"，而是完成 L1+L2 该有的覆盖**。

催化拆解任务作为 **Block 7 优先子项** 提前执行，目的是把短期叙事跟
长期基本面分开归档。

---

## 已确认的事实 (Stage 0 Identify — 待单次 WebSearch 复核)

以下字段属于稳定公共信息，**先填上但标为待验证 (Tier B)**，
Stage 2 启动前用一次 WebSearch 在 EDGAR 上确认。

| 项 | 值 | Tier | Note |
|---|---|---|---|
| Legal name | Micron Technology, Inc. | B (待 EDGAR 确认) | |
| Ticker | MU | B | |
| Exchange | NASDAQ | B | |
| IPO date | 1984 | B | 历史悠久 |
| CIK | 待 Block 2 确认 | — | |
| Sector | 半导体 — 存储器 (DRAM / NAND / HBM) | A1 | 行业归属稳定 |
| 主营产品 | DRAM (含 HBM3e/HBM4), NAND Flash, SSD, managed NAND | A1 | |
| 财年截止 | 8 月底 (FY2026 = 2025-09 → 2026-08) | B | 跟其他半导体公司不同步，重要 |
| 最近 SEC filing | 待 Block 2 确认 | — | |
| EDGAR 入口 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=micron+technology&type=&dateb=&owner=include&count=40 | A1 | URL 模式 |
| 公司 IR 入口 | https://investors.micron.com | A1 | |
| 特殊情况 | 强周期性 (DRAM cycle) + 当前处于"AI 存储 supercycle"叙事中 + HBM 是 NVIDIA 链关键环节 | A1 | 直接决定调研 lens |

---

## 复杂度系数 + 时间预算

按 [info_collection_pipeline.md](../../frameworks/info_collection_pipeline.md)
复杂度系数：

- 普通公司: 1.0× → 2.5-4.5 h
- 强周期 + 当前赛道炒作: +20% (需多花时间区分"周期高位"vs"结构上行")
- 不是年轻公司, 不是跨境, 不是加密 → 无额外加成

本公司系数: **1.2× → 预计 L1+L2 约 3-5 h**

---

## 关联文档

- [macro/2026Q2_memory_supercycle_research.md](../../macro/2026Q2_memory_supercycle_research.md)
  — 同步推进。MU 是 supercycle 的三大主角之一 (与 SK Hynix / Samsung
  并列)，本简报的 Block 6 必须跟 macro 那份的 Block 1 (价格数据) +
  Block 3 (供给侧 capex/mix) 联动，避免重复 fetch。
- [companies/nbis.md](../nbis.md) — 上一份按视频起的简报，**反面参考**:
  全部基于二手视频导致"不可决策"，MU 这份要保证 Block 3/4 实际拉一手财报。

---

## 完整 Plan (8 Block)

### Block 1: Anchor identity ⏸
- [ ] 1 次 WebSearch 在 EDGAR 上确认 CIK + legal name + 最近 filing 日期
- [ ] 把上面 Stage 0 Identify 表里 Tier B 项升到 Tier A1

预计调用: 1 WebSearch · 5 min · 输出: 写回本 plan 顶部 (不另起 raw file)

---

### Block 2: EDGAR locate ⏸

- [ ] 列出 EDGAR 所有 filing types + 日期 (10-K / 10-Q / 8-K / DEF 14A / Form 4)
- [ ] 确认 latest 10-K (FY2025 = 截至 2025-08) accession number
- [ ] 确认 latest 10-Q (FY2026 Q1 或 Q2，取决于今天日期是否过 Q2 报) accession number
- [ ] 确认 latest DEF 14A accession number
- [ ] 扫 8-K title 列表 (最近 12 个月)，标记重要的 (重大合同 / HBM 客户 / 资本结构变动)
- [ ] **重点关注 2026-05-27 当天或前后是否有 8-K** — 触发今日涨幅的可能信源

预计调用: 1 WebFetch (EDGAR 列表页) · 5 min · 输出: `raw/block02_edgar_filings.md`

---

### Block 3: 最近 10-Q (FY2026 最近一季) ⏸

依赖 Block 2 拿到 URL。

- [ ] 财务概要 (current snapshot):
  - revenue / GM / OM / 净利润 / FCF / 经营现金流
  - debt / cash / capex 当季 + ytd / 股本
  - **存储行业特有指标**:
    - DRAM revenue 占比 / NAND revenue 占比
    - HBM revenue 单独披露 (若有) — supercycle 关键
    - inventory days (周期判断关键)
    - ASP YoY / bit shipment YoY (DRAM / NAND 各)
  - Risk factors 段重点 (3-5 条最重)
  - MD&A 季度 highlight — 特别是 management 对 cycle 阶段的措辞

预计调用: 2-3 WebFetch (10-Q 不同段) · 15 min · 输出: `raw/block03_latest_10q.md`

---

### Block 4: 10-K FY2025 ⏸

依赖 Block 2 拿到 URL。

- [ ] 10-K FY2025 (截至 2025-08):
  - business overview (DRAM/NAND/HBM 三段拆分)
  - 完整年度财务 (revenue/GM/OM/FCF FY2025 vs FY2024 同比) — 验证 cycle 上升轨迹
  - 完整 risk factors 列表 (扫，标 3-5 条核心):
    - 周期风险 / 客户集中度 / 中国地缘 / capex 强度 / HBM 竞争 (Samsung/Hynix)
  - capital structure (股本 / debt / 是否有可转债)
  - related party / 政府补贴 (CHIPS Act 资金条款细节)
  - 客户集中度披露 (是否有单一客户 >10% — NVIDIA/AMD 大概率)

预计调用: 3-4 WebFetch · 30 min · 输出: `raw/block04_10k.md`

---

### Block 5: 最近 call transcript ⏸

- [ ] 找最近一次 earnings call (FY2026 最近一季):
  - 来源候选: Seeking Alpha / Tikr / 公司 IR webcast / Motley Fool transcript
  - 重点:
    - CEO 开场叙事 (是否定调"supercycle")
    - HBM 量产 / 客户绑定 (NVIDIA HBM3e / HBM4 时间表)
    - DRAM/NAND ASP guidance
    - capex 节奏 (FY2026 / FY2027)
    - 分析师 Q&A 中关于"cycle 顶部还是中段"的回答
  - 备份: 财报新闻稿 (BusinessWire) + 任何媒体的 highlight 总结

预计调用: 1-2 WebSearch + 1-2 WebFetch · 15 min · 输出: `raw/block05_calls.md`

---

### Block 6: 市场位置 + 竞争 ⏸

- [ ] **三大厂对照** — 跟 macro/memory_supercycle 那份的 Block 3 共用:
  - SK Hynix 最近一次财报 (HBM 收入 / DRAM 价格 / capex)
  - Samsung 最近一次财报 半导体段拆 (HBM 客户认证状态 — NVIDIA 是否过认证)
  - 三家 2026 capex 合计 (供给响应速度判断)
- [ ] **NAND 厂对照** — 跟 lab 2025-10-02 视频 (WDC/SNDK/MU) 提到的"四大牛股"对比:
  - Western Digital (WDC) HDD/SSD 拆分后状态
  - Kioxia (KIOX) 最近一次披露
- [ ] **价格 dashboard**:
  - TrendForce / DRAMeXchange DRAM 合约价 2025 → 2026 走势
  - NAND 合约价
  - HBM 占 DRAM 产能比例

预计调用: 4-5 WebSearch + 2-3 WebFetch · 25 min · 输出: `raw/block06_market_position.md`

---

### Block 7: Sell-side + 专业新闻 + 仓库 grep + **5/27 催化拆解** ⏸ **(可优先执行)**

- [ ] **(优先) 2026-05-27 涨幅催化**:
  - WebSearch "Micron MU stock surge May 27 2026" + "Micron HBM" + "Micron earnings preview"
  - 候选触发因素清单 (待验证)：
    - [ ] 5/27 当天/前一日的 8-K (见 Block 2)
    - [ ] sell-side 上调 (大行评级 / 目标价 hike)
    - [ ] HBM4 量产 / NVIDIA 认证消息
    - [ ] DRAM/NAND 合约价新数据点 (TrendForce 月度)
    - [ ] 同业利好溢出 (SK Hynix / Samsung 财报指引上调)
    - [ ] 宏观面 (Fed 表态 / 关税 / capex 周期)
- [ ] Yahoo Finance MU Analyst tab — consensus EPS / Revenue / 目标价分布 + 评级变动
- [ ] 3 篇过去 6 个月专业报道 (Bloomberg/Reuters/WSJ/FT/EE Times)
- [ ] **仓库 grep** (本地，不调外网):
  - `notes/videos/` 内 MU / Micron 出现的 ~7 个视频已知 — 抽取每条的 thesis 与时间点
  - 重点比对 2024-03-28 (推 buy) / 2025-10-02 (四大牛股) 两条 — TradesMax 自身的 track record 测试

预计调用: 4-5 WebSearch + 2-3 WebFetch + 1 Grep · 25 min · 输出: `raw/block07_news_sellside.md`

---

### Block 8: 监管 / 立法 ⏸

- [ ] **CHIPS Act 资金条款细节** — MU 获批了多少补贴 / 配套义务 / clawback 条件
- [ ] **对华出口管制** — BIS 最新动作 (HBM 出口限制是否覆盖 MU)
- [ ] **关税** — 当前关税环境对 MU 客户终端 (服务器 / PC / 手机) 的影响传导
- [ ] **中国调查** — 2023 年 CAC 对 MU 的调查后续状态

预计调用: 2-3 WebSearch · 15 min · 输出: `raw/block08_regulatory.md`

---

## 砍掉的 (接受信息缺口，进 Stage 4 audit 决定是否触发 L3)

按 framework L3 触发表，以下默认砍掉，灵魂明确叫缺时再触发：

- 历史每年 1 季 call transcript 抽样 (老公司可选，本轮 L1+L2 不做)
- 8-K 全扫 (只标 Block 2 中重要的)
- proxy 详读 (只取 URL 不 deep dive)
- Form 4 全史 (只看最近 12 个月大额抛售)
- 13F 季度对比 (只看 top 5 holder snapshot)
- scuttlebutt 5 类 (留 L3 — Glassdoor / Blind / Reddit / HBM 客户口风)
- 学术 / BIS 报告 (留 L3)
- 历史 letter 全套 — MU 不写 owner letter，N/A
- 信用债 spread / drawdown 详算 (留 L3)

---

## 总预计调用

| Block | WebSearch | WebFetch | 时间 |
|---|---|---|---|
| 1 | 1 | 0 | 5 min |
| 2 | 0 | 1 | 5 min |
| 3 | 0 | 2-3 | 15 min |
| 4 | 0 | 3-4 | 30 min |
| 5 | 1-2 | 1-2 | 15 min |
| 6 | 4-5 | 2-3 | 25 min |
| 7 | 4-5 | 2-3 + 1 grep | 25 min |
| 8 | 2-3 | 0 | 15 min |
| **合计** | **~14** | **~12-14** | **~135 min ≈ 2.25 h** |

(含 1.2× 系数已计入 Block 6/7 的额外搜索量)

---

## 执行节奏

每个 block 单独执行一次，期间 stop 让用户审视产出 + 决定是否 redirect 后续 block。

**推荐起点**: 因为本次启动由 5/27 涨幅事件触发，建议执行顺序：

1. **Block 1** (Anchor identity — 1 次 search 复核) — 5 min
2. **Block 7 优先子项** (5/27 催化拆解 + lab grep) — 15 min
3. **Block 2** (EDGAR locate — 含检查 5/27 当天 8-K) — 5 min
4. 之后按 3 → 4 → 5 → 6 → 7 完整 → 8 顺序推进

这样能在 ~25 min 内回答"今天为什么涨"，剩下时间补完 L1+L2 基本盘。

下一步**等用户 confirm scope** 后从 Block 1 启动 Stage 2。
