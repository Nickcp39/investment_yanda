# Information Collection Pipeline

公司研究 Step 0 (资料归集) 的真正定义。这份文档展开 [souls_workflow.md](souls_workflow.md)
里那句"读 notes + 1-3 次 WebSearch"——把"收集"做成可执行 + 可审计的 pipeline。

对接 [sources/source_policy.md](../sources/source_policy.md) 已经定义的 4 级
source hierarchy (一手 / 高质二手 / 市场评论 / 社交媒体)；本文档只增补**收集投入分层**、
**信息类型分流**、**多年处理**、**行业 overlay**、**停止条件**、**plan-first 执行**
这 6 件事。

---

## 核心心智 shift

业余 → 专业的差别不是"收集得更全"，是 4 件事：

1. **分层**: 必读 / 应读 / 按需，三层投入差 5 倍
2. **类型分流**: 事实 / 解读 / 情绪 不混用
3. **假设驱动停止**: 不按"读了多少篇"停，按"每个灵魂能不能开口"停
4. **Plan-first 执行**: 先写搜索计划 md，再调工具——不批量、可暂停、可跨会话恢复

---

## 框架: 3 × 3 + 4

- 维度 A: 3 个收集层级 (L1/L2/L3) — 决定**何时**收集
- 维度 B: 3 种信息类型 (Fact/Signal/Sentiment) — 决定**如何**使用
- 4 条横切原则: look-back / 行业 overlay / 停止条件 / **plan-first 执行**

---

## 维度 A: 3 个收集层级

### L1 — 必读 (Mandatory)

**100% 完成，没读完不允许跑灵魂**。

| 项目 | 来源 | 备注 |
|---|---|---|
| 10 年 10-K (年度报告) | SEC EDGAR | 数字时间序列全拉，叙事采样 3 个 (latest / 5y ago / 10y ago) |
| 最近 1 份 10-Q | SEC EDGAR | current snapshot |
| 最近 12 个月 8-K | SEC EDGAR | material events |
| 最近 1-2 份 DEF 14A (proxy) | SEC EDGAR | 治理 + 高管薪酬 |
| 最近 4 季 call transcript verbatim + 历史每年 1 季抽样 | 公司 IR / Seeking Alpha / Tikr | 共 ~14-18 份 |
| 资本结构当前快照 | 最新 10-Q | debt / cash / 股本 / 优先股 |
| 大股东 + 内部人持仓 | 13G / Form 4 / proxy | top 5 holder + 内部人持股 % |
| 审计师 + 重述历史 | 10-K (audit opinion) + SEC 调查 / restatement 历史 | 10 年范围 |
| 关键事件年表 | 8-K + 公司 press release | M&A / 分拆 / 重组 / CEO 换人 / 重大诉讼 |

**例外处理 (Look-back 不够 10 年)**:
- 年轻公司 (post-IPO < 5 年): 拉 S-1 历史 exhibits 补 pre-IPO 3-5 年财务
- spinoff: 母公司历史按"前世" tier 处理，灵魂明确**降低 confidence**
- 重组 / 反向并购: 重新计时，前史不可直接外推

### L2 — 应读 (Standard pro)

**代表性采样，不追全**。

| 项目 | 数量门槛 | 来源 |
|---|---|---|
| Sell-side 一致预期 | 1 次 quick view | Yahoo Finance / TipRanks (免费) |
| 13F 流向 | 最近 4 季 | EDGAR / WhaleWisdom |
| 近期 8-K + Form 4 | 最近 12 个月 | EDGAR (与 L1 部分重叠，重点看趋势) |
| 1-3 家直接竞品最近一次财报口径 | 1-3 家 × 1 季 | 各家 IR |
| 高质量专业报道 | **3-5 篇**，过去 6 个月 | Bloomberg / Reuters / WSJ / FT / 行业专门 (The Block / Stat / Endpoints 等按行业) |
| 行业专属 dashboard | **1 项** (按行业，见下方 overlay) | 见下方表 |
| 监管 / 立法时间表 | 1 次 sweep | SEC press release / Fed / Congress 议案追踪 / 各国监管官网 |

### L3 — 按需 (Lens-triggered only)

**Step 1 审计或 Step 2/3 灵魂明确叫缺时才拉。不在默认清单**。

| 资源 | 触发 lens | 触发条件 |
|---|---|---|
| Scuttlebutt 5 类 (客户/供应/竞品/前员工/开发者) | Fisher | "客户口碑没数据" |
| 专家网络访谈 (Tegus / AlphaSense / Third Bridge) | Fisher / Munger / Buffett | 信息缺口 + 预算允许 (付费) |
| 历史 letter 详读 (10 年范围全部) | Buffett / Munger | "管理层 capital allocation 模式不清楚" |
| Proxy 详读 + 关联交易 | Munger | "激励结构异常" |
| 信用债 spread / 历史 drawdown / 压力情景 | Klarman | "下行情景没量化" |
| 诉讼深挖 / 监管执法历史 | Klarman / Munger | "尾部风险无量化" |
| 4 regime 矩阵 (利率/汇率/通胀/政策) | Dalio | "宏观敏感且 panel 没人覆盖" |
| 反身性循环 + 融资条件 + 衍生品仓位 | Soros | "boom-bust 可能在跑" |
| Magic Formula 量化扫描 | Greenblatt | "想做 idea generation 起点" |
| Liquidation / asset-cover 详算 | Graham | "破产边缘 / 净资产折扣场景" |
| Alternative data (信用卡 / 卫星 / 招聘 / app 数据) | 视行业 | 业务模式需要直接客户行为数据 |
| 学术 / BIS / IMF / FSB 报告 | 系统性主题 | 涉及系统性风险 / 监管哲学 |

---

## 维度 B: 3 种信息类型

facts.md 拆 3 个区，**严禁混用**。这是 amateur 简报最常见的硬伤——把分析师观点当事实、把情绪当信号。

| 类型 | 例子 | facts.md 区 | 灵魂能否引用 |
|---|---|---|---|
| **事实 (Fact)** | 财报数字 / SEC 一手披露 / 监管原文 / 一手 attestation | EVIDENCE 区 | ✅ 可作 thesis 直接依据 |
| **解读 (Signal)** | sell-side 评级 / 行业研报观点 / 专业新闻分析师 take | INTERPRETATION 区 | ⚠ 仅参考，引用时必须复核到事实 |
| **情绪 (Sentiment)** | Reddit / X / 散户论坛 vibe | SENTIMENT 区 | ❌ 不可作 thesis；Marks 等情绪敏感灵魂可看作 contrarian / 共识信号 |

---

## 横切原则 1: Look-back (多年)

### 默认 10 年

覆盖一个完整周期 (大概率经历过一次衰退)，让 Buffett / Klarman / Marks / 段永平
等需要"长期" 视角的灵魂能开口。

### 地板规则

- **Floor**: since IPO / since major restructuring (取较晚)
- **Pre-public**: S-1 历史 exhibits 一般含 3-5 年 pre-IPO 财务，纳入
- **Spinoff**: 母公司"前世"历史按降级 tier 标注，**不可直接当 successor 历史外推**

### 多年 ≠ 全部读完，三种粒度

| 数据形态 | 处理方式 | 工作量 |
|---|---|---|
| **数字时间序列** | 10 年 revenue / GM / OM / FCF / ROIC / 股本 / debt / capex / 回购 / 股息 拉成表 | 自动化为主 |
| **管理层叙事** | latest annual letter + 5 年前 + 10 年前 (3 个采样点) 看 strategy 演化 | 30-60 min |
| **财报电话会** | 最近 4 季 verbatim + 历史每年 1 季抽样 (~14-18 份) | 60-120 min (最重) |

3 种粒度组合是 affordable 多年的关键。

---

## 横切原则 2: 行业 dashboard overlay

L2 只额外加**一项**行业专属 dashboard，避免清单膨胀。

| 行业 | dashboard | 来源举例 |
|---|---|---|
| 加密 / 稳定币 / DeFi | 链上数据 (供应 / 持仓 / 转账 / 链分布) | Dune Analytics / DeFi Llama / Nansen (部分付费) |
| SaaS / 互联网 | Web traffic / app downloads / 客户留存 / NPS | SimilarWeb / Sensor Tower / G2 (部分付费) |
| 零售 / 消费 | 信用卡 spending / 客流 / 同店销售 | YipitData / Placer.ai (付费) / 公司披露 |
| 制药 / 生物科技 | FDA approvals / clinical trial / 处方数据 | clinicaltrials.gov / IQVIA (付费) / FDA 官网 |
| 工业 / 周期 | 商品价格 / capex 周期 / 库存 | LME / EIA / 行业协会 |
| 银行 / 金融 | 利率敏感度 / NPL / capital ratio | 公司披露 + Fed H.8 + 监管 call report |
| AI 基础设施 | GPU 出货 / hyperscaler capex / 电力价 | NVIDIA 财报 / hyperscaler capex 公布 / EIA |
| 半导体 | 行业出货 / lead time / capex cycle | SIA / WSTS / 各家 capex |
| 能源 | 商品价格 / 钻井数 / 库存 | EIA / Baker Hughes |

**只加一项**。多于一项要明确 justify。

---

## 横切原则 3: 停止条件 (灵魂能否开口)

不按"读了多少篇" 停，按**每位灵魂的最低开口门槛**停。

| 灵魂 | 最低开口门槛 |
|---|---|
| Buffett | 最近 1 份 10-K + 10 年 ROIC 时间序列 + 管理层 capital allocation 模式可描述 |
| Marks | 至少 3 篇 B 级新闻交叉看 consensus + sentiment vibe tag 已打 + sell-side 一致预期已 sweep |
| Munger | 财报 risk factors 已读 + 关键 incentive 结构 (proxy 高管薪酬 / 大股东) 已查 |
| Klarman | 资产负债表 + asset coverage + 至少一次历史下行场景的 drawdown 数字 |
| 段永平 (Chair) | 业务模式可用 2 句中文讲清 + "10 年是否还在做这事" 能给非空答案 + 不为清单 4 项已过 |

**任一灵魂的门槛没过 → Step 1 (Li Lu/Fisher 审计) 应触发回 Step 0 补料**。

这是 souls_workflow.md 里 Step 1 那个 <40% 阈值的真正含义——不是简单按页数。

---

## 横切原则 4: Plan-first 执行

**先写搜索计划 md，再调工具**。不批量、不一次性、可暂停、可跨会话恢复。

业余的做法: 拿到公司就一口气调 10 个 WebSearch / WebFetch，结果一团乱无法审计、出错无法回退、跨会话从头来。

专业的做法: **先把"要搜什么 / 从哪搜 / 大致输出什么 / 砍了什么" 写进一个 md plan 文件**，
等用户 confirm scope 后按 plan 一次推进 1 个 block，每 block 完成后回写 plan status，
产出落到独立 raw md 文件——这样 plan + raw md 就是可持久化的执行轨迹。

详见下方"执行阶段"。

---

## 执行阶段 (Execution Stages)

Step 0 资料归集本身是一个 **5 阶段子 pipeline**。每个阶段有明确的 input / activity /
output artifact / success criteria / hand-off trigger。stage 之间靠 md 文件传递状态——
跨会话可恢复、出错可回退、产出可审计。

### 文件夹结构

```
companies/<ticker>/
  step0_plan.md       # Stage 1 输出：搜索计划（block 列表 + status + 砍掉项）
  raw/                # Stage 2 输出：每个 block 一份 verbatim/close 抓取
    block01_identity.md
    block02_edgar_filings.md
    block03_latest_10q.md
    block04_10k_s1.md
    block05_calls.md
    block06_market_position.md
    block07_news_sellside.md
    block08_regulatory.md
  facts.md            # Stage 3 输出：从 raw/ 综合而成（EVIDENCE/INTERPRETATION/SENTIMENT）
  memory.md           # Stage 5+ (panel 跑完后)
  brief-v1.html       # Stage 5+ (panel 跑完后)
```

### Stage 0 — Identify (识别)

| 项 | 内容 |
|---|---|
| **Input** | 公司名 / ticker / 模糊描述 |
| **Activity** | 1-2 次 WebSearch 确认基础事实 (ticker / exchange / IPO date / CIK / 主营) |
| **Output** | 写进 step0_plan.md 顶部的 "已确认事实" section (不单独成文件) |
| **Success criteria** | 公司唯一可识别 + EDGAR / IR 入口 URL 已知 |
| **Hand-off trigger** | 进 Stage 1 写完整 plan |

### Stage 1 — Plan (写搜索计划)

| 项 | 内容 |
|---|---|
| **Input** | Stage 0 identity + framework (本文档) + [companies/_step0_plan_template.md](../companies/_step0_plan_template.md) |
| **Activity** | 列 8 个 block (或按行业 / 公司情况调整)，每 block 写 target / 来源 URL / 预计调用 / 预计产出 / 砍掉的项 |
| **Output** | `companies/<ticker>/step0_plan.md` |
| **Success criteria** | 每 block 有可执行的 query / URL；总调用数 + 时间预估清晰；砍掉项有 justify |
| **Hand-off trigger** | **必须 stop**，等用户 confirm scope。用户可调整范围 / 顺序 / 砍掉项 |

### Stage 2 — Execute by block (按 block 执行)

| 项 | 内容 |
|---|---|
| **Input** | step0_plan.md 当前 pending block |
| **Activity** | 一次推进 1 block (或多个紧密耦合的 block 并行)。WebSearch / WebFetch / Grep |
| **Output** | `companies/<ticker>/raw/block<N>_<name>.md` (按 [companies/_raw_block_template.md](../companies/_raw_block_template.md))。同时回写 step0_plan.md 把该 block status 改 ✅ |
| **Success criteria** | block 的 target 全部回答 (或明确标 ❌ blocked / ⏭ skipped)；raw md 里 verbatim 段 + 提取 claim 段都填了 |
| **Hand-off trigger** | block stop——可暂停（用户审视产出 + redirect 后续 block）或继续下一 block |

**这是 iterative 阶段**。所有 block 跑完才进 Stage 3。

### Stage 3 — Synthesize (综合写 facts.md)

| 项 | 内容 |
|---|---|
| **Input** | `companies/<ticker>/raw/*.md` 全部 |
| **Activity** | 从各 raw md 的 "提取 claim" 段抽出事实，按主题分组合并 (跨 block 去重 / 交叉验证 / 标矛盾)，写入 facts.md 的 EVIDENCE / INTERPRETATION / SENTIMENT 三区。每条 claim 保留来源到具体 raw md 文件 |
| **Output** | `companies/<ticker>/facts.md` (按 [companies/_facts_template.md](../companies/_facts_template.md)) |
| **Success criteria** | facts.md 的 L1 + L2 自查 checkbox 全勾 (或对每个未勾项标"该 block 砍/blocked，进 OPEN QUESTIONS") |
| **Hand-off trigger** | 进 Stage 4 audit |

### Stage 4 — Audit (灵魂可开口性自查)

| 项 | 内容 |
|---|---|
| **Input** | facts.md + 横切原则 3 的 5 条灵魂最低开口门槛 |
| **Activity** | 逐灵魂对照门槛——能不能开口？ 哪条信息缺？ |
| **Output** | facts.md 末尾的 "灵魂开口度自查" section (新加)；如果有缺，写进 OPEN QUESTIONS + 决定是否触发 L3 (回到 Stage 2 加 block) |
| **Success criteria** | 5 灵魂全部能开口 (或明确接受 N 个降低 confidence / 排除某灵魂) |
| **Hand-off trigger** | 进 souls_workflow.md Step 1 (Li Lu/Fisher 审计 + 5 灵魂初评) |

### Stage 5+ — souls_workflow.md 接管

Step 0 子 pipeline 到此结束。后续 Step 1-5 (审计 / 初评 / critique / 主审 / 落盘) 见
[souls_workflow.md](souls_workflow.md)。

### 跨会话恢复

每次会话开始时，读 `companies/<ticker>/step0_plan.md` 确定**当前 stage + 当前 block**，
从 status 标 ⏸ pending 的下一项继续即可。所有产出都落盘，不依赖 conversation context。

### 错误 / 中断处理

- WebFetch 失败 → 该 block 标 ❌ blocked，记原因，进下一个 block
- 信息源已死 (URL 404 / paywall) → 该项标 ⏭ skipped，写 substitute 来源候选 OR 接受缺口进 OPEN QUESTIONS
- Block 部分完成 → 标 🟡 in-progress，写已做了什么，下次接续

---

## 总工作量估算

不算 L3 (按需触发):

| 阶段 | 时间 |
|---|---|
| L1 数字时间序列 (10y financial pull) | 20-30 min (借工具) |
| L1 管理层叙事 (3 个 letter 采样) | 30-60 min |
| L1 call transcripts (~16 份) | 60-120 min |
| L1 其他 (proxy / Form 4 / 大股东 / 重述) | 20-30 min |
| L2 sell-side / 13F / 竞品 / 新闻 / 行业 dashboard / 监管 | 30-45 min |
| **L1+L2 合计** | **2.5-4.5 小时** |

souls_workflow.md 里"Step 0: 10-30 min"是**不切实际**的——专业级 Step 0 至少 2-3 小时。
要么调整时间预期，要么明确接受"Step 0 跨多次会话累积"。

**建议**: Step 0 不在单次 50-75 min 简报会话里完成。它是**前置工作**，
完成后再进 Step 1-5 panel pipeline (~ 50-75 min)。

---

## L3 触发示例 (实操)

```
Step 1 审计触发:
  Li Lu: "完整度 35% — 缺管理层 10 年公开声明的连续性证据"
    → L3: 拉历史 letter 详读

Step 2 灵魂叫缺触发:
  Buffett: "ROIC 10 年是高，但 capital allocation 5-10 年前的 M&A 没看清"
    → L3: 重读 5-10 年前 letter + 当时的 10-K M&A 段
  Munger: "薪酬结构里有期权 reload 条款，可能引发短视行为"
    → L3: proxy 详读 + 关联交易段
  Klarman: "FCF 看起来稳，但没看过 2008 / 2020 这种衰退里的下行幅度"
    → L3: 拉 2008-2009 / 2020 当年 10-K + drawdown 数字

Step 3 critique 触发:
  Marks → Buffett: "你的 ROIC 论点市场已经定价了多少?"
    → 若 sell-side 一致预期已涵盖 → 用 L2 数据回应
    → 若没涵盖 → L3 拉 sell-side 详细 model 假设
```

---

## 与 source_policy.md 的映射

| 本文档 | source_policy.md tier |
|---|---|
| L1 + L2 行业 dashboard 一手部分 | Tier 1 (一手) |
| L2 高质量专业报道 + sell-side 部分 | Tier 2 (高质二手) |
| 我们仓库 notes/videos/ 节选 | Tier 3 (市场评论) |
| L3 sentiment / Reddit / X | Tier 4 (社交媒体) |

每条事实 inline 标 Tier (`[A1]` / `[B2]` / `[C3]` / `[D4]`)，按 [companies/_facts_template.md](../companies/_facts_template.md) 的 schema。

---

## 工具 / 自动化路线图

当前手工。按使用频率优先级，未来可写脚本：

1. **SEC EDGAR fetcher** (10-K/Q/8-K + Form 4 自动拉到 `sources/sec/<ticker>/`) — 最高优先
2. **财务时间序列 puller** (借 SEC XBRL / yfinance 拉 10y revenue/margin/FCF/ROIC) — 次优先
3. **13F holder tracker** (季度对比，flagged 显著加仓减仓) — 中优先
4. **earnings transcript fetcher** (Seeking Alpha / Tikr 通常需要登录，复杂) — 低优先
5. **行业 dashboard scraper** (Dune / DeFi Llama 公开 API；其他付费跳过) — 低优先

Premature 之前先手工跑 2-3 家公司，找出真痛点再自动化。

---

## 修订记录

- 2026-05-05 v1: 首发，3×3+3 框架 + 多年处理 + 行业 overlay + 停止条件
- 2026-05-05 v2: 加 Plan-first 第 4 原则 + 5 阶段执行子 pipeline (Identify / Plan / Execute by block / Synthesize / Audit) + 文件夹结构 + 跨会话恢复规则。框架升级 3×3+3 → 3×3+4+5stages
