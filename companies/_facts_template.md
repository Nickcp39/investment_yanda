# &lt;Ticker&gt; — Facts (累积事实库)

按 [frameworks/info_collection_pipeline.md](../frameworks/info_collection_pipeline.md)
的 3×3+4+5stages 框架，**Stage 3 (Synthesize) 输出**。从 `raw/block<N>_*.md`
抽 claim 综合而成；下游灵魂只读 facts.md，不读 raw/。

每条事实 inline 标 source tier (`[A1]` 一手 / `[B2]` 高质二手 /
`[C3]` 市场评论 / `[D4]` 社交媒体)。每条 claim 应在 raw/ 里能找到出处。

**Snapshot**

- Company:
- Ticker:
- Exchange:
- 上市日期 / IPO date:
- Sector / 子行业:
- Last updated:
- Look-back 范围: __年 (default 10y / since IPO / since restructuring)

---

## L1 完成度自查

进 Step 1 panel 审计前，下面应全部勾选：

- [ ] 10 年 10-K 数字时间序列已拉 (revenue / GM / OM / FCF / ROIC / 股本 / debt / capex / 回购 / 股息)
- [ ] 管理层叙事 3 个采样点 (latest / 5y ago / 10y ago) 已读
- [ ] 最近 4 季 call transcripts verbatim 已读
- [ ] 历史每年 1 季 call transcript 抽样已扫
- [ ] 最近 1 份 10-Q 已读
- [ ] 最近 12 个月 8-K 已扫
- [ ] 最近 1-2 份 proxy (DEF 14A) 已读
- [ ] 资本结构当前快照已记录
- [ ] 大股东 top 5 + 内部人持仓 % 已记录
- [ ] 审计师 + 10 年 restatement / SEC 调查历史已查
- [ ] 关键事件年表 (M&A / 分拆 / 重组 / CEO 换人 / 重大诉讼) 已建

## L2 完成度自查

- [ ] Sell-side 一致预期 quick view (EPS / Revenue / 目标价分布)
- [ ] 13F 流向最近 4 季扫描
- [ ] 1-3 家直接竞品最近一次财报口径
- [ ] 3-5 篇高质量专业报道 (过去 6 个月)
- [ ] 行业专属 dashboard 1 项
- [ ] 监管 / 立法时间表 sweep

---

## EVIDENCE (事实区)

按主题分小节。每条 inline 标 tier，含 source / date retrieved / path / claim / reliability。

灵魂可直接引用此区作为 thesis 依据。

### 业务模式 / 收入结构

- [A1] _claim_
      Source:
      Date retrieved:
      Path:
      Reliability:

### 财务时间序列 (10 年)

- [A1] _10 年 revenue CAGR / GM 趋势 / FCF 趋势 / ROIC 中位数_

### 资本结构

- [A1]

### 管理层 / capital allocation 历史

- [A1]

### 大股东 + 内部人持仓

- [A1]

### 关键事件年表 (10 年)

- [A1] _YYYY-MM: <事件>_

### 行业 / 市场结构 / 竞争格局

- [A1]
- [B2]

### 监管 / 立法

- [A1]
- [B2]

### 行业专属 dashboard 数据

- [A1] / [B2]

---

## INTERPRETATION (解读区)

Sell-side 报告、专业媒体分析、研报观点。**灵魂可参考，但引用时必须复核到 EVIDENCE**。

### Sell-side 一致预期

- [B2] _consensus EPS / Revenue / 目标价范围 (date)_
      Source:
      Date retrieved:

### 专业媒体观点

- [B2] _<article title> argues <观点> based on <reasoning>_
      Source:
      Date retrieved:

### 我们仓库的播客 / 视频 notes (notes/videos/ grep 命中)

- [C3]
      Source: notes/videos/&lt;file&gt;.md
      Tier 注: 频道作者立场 + 是否有数据支撑

---

## SENTIMENT (情绪区)

不可作 thesis 依据。仅 Marks 等情绪敏感灵魂参考。

### Reddit / X / 论坛 vibe

- [D4] _<subreddit / X 话题> 过去 30 天 vibe summary_
      Polarity tag: BULLISH / NEUTRAL / BEARISH (估计 % 分布)
      最高赞贴大意: <一行>
      Date retrieved:
      Caveat: 仅 contrarian / 共识信号参考

### 短期价格 / 量 / 期权异常

- [D4] _<short interest %, days-to-cover, options skew, etc.>_
      Source:
      Date retrieved:

---

## OPEN QUESTIONS (信息缺口 / L3 触发候选)

哪些问题 L1+L2 无法回答，可能需要触发 L3：

- [ ] _<问题>_ → L3 候选: _<scuttlebutt / proxy 详读 / drawdown 计算 / etc.>_

---

## KILL CRITERIA (待 panel 后填)

Step 4 主审环节填入。每条要可证伪、有阈值。

- [ ]

---

## 修订记录

- YYYY-MM-DD: 首版 facts 收集完成 (L1+L2)，进 Step 1 审计
