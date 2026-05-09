# Circle (CRCL) Step 0 Search Plan

按 [frameworks/info_collection_pipeline.md](../../frameworks/info_collection_pipeline.md)
执行阶段 **Stage 1 输出** (本文件本身)，指导 Stage 2 (按 block 执行) 把每 block 产出落到
`companies/circle/raw/block<N>_<name>.md`，按 [_raw_block_template.md](../_raw_block_template.md)。

每项执行后回写 status。可跨会话恢复。

**Status 图例**: ⏸ pending · 🟡 in-progress · ✅ done · ⏭ skipped (acceptable gap) · ❌ blocked

最后更新: 2026-05-05

---

## 已确认的事实 (Block 1+2 部分跑出)

来源: 2026-05-05 WebSearch on "Circle Internet Group CRCL NYSE IPO" + "Circle SEC EDGAR CIK"

| 项 | 值 | Tier | Note |
|---|---|---|---|
| Legal name | Circle Internet Group, Inc. | A1 | EDGAR (CIK 1876042) |
| Ticker | CRCL | A1 | EDGAR + NYSE |
| Exchange | NYSE | A1 | EDGAR |
| IPO date | 2025-06-05 | A1 (公司 IR) / B2 (CNBC) | shares 首日交易 |
| IPO price | $31 / share | B2 | CNBC + Fortune |
| First day perf | +168% | B2 | CNBC (大幅 underpricing — Fortune 称十年第 7 大留钱 $1.72B) |
| CIK | 1876042 | A1 | EDGAR |
| 产品 | USDC (USD-pegged) + EURC (Euro-pegged) stablecoin | A1 | 公司 IR |
| Pre-IPO 实体名 | Circle Acquisition Public Ltd Co (S-1 April 2025 提交) | A1 | EDGAR |
| 最近一次 SEC filing | 2026-04-08 | A1 | EDGAR (具体 form type 待 Block 2 完成确认) |
| 首份季报 | Q2 2025 (2025-08-12 发布) | A1 | BusinessWire |
| EDGAR 入口 | https://www.sec.gov/edgar/browse/?CIK=1876042 | A1 | |
| 公司 IR 入口 | https://investor.circle.com/financials/sec-filings | A1 | |

**新发现 (dry-run 时漏的)**:
- **EURC** Euro-pegged 稳定币也是 Circle 产品 — 之前只提了 USDC
- 公司 IPO 严重 underpricing (首日 +168%) — 反身性 / 共识 角度有戏 (Marks lens 重要数据)
- Pre-IPO S-1 entity 名 "Circle Acquisition Public Ltd Co" 暗示有重组结构

---

## 完整 Plan (8 Block)

### Block 1: Anchor identity ✅
- [x] 确认 ticker / exchange / IPO 日期 / CIK — done
- 输出: 已确认事实写入本 plan 顶部 (Stage 0 Identify 不另起 raw file)

### Block 2: EDGAR locate 🟡

- [ ] 列出 EDGAR 所有 filing types + 日期 (10-K / 10-Q / S-1 / 8-K / DEF 14A / Form 4)
  - URL: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1876042&type=&dateb=&owner=include&count=40`
  - 输出: 每种 form 最新 1-2 份的具体 accession number 和日期
- [ ] 确认 latest 10-K (FY2025) accession number
- [ ] 确认 latest 10-Q accession number
- [ ] 确认 S-1 / S-1/A accession number
- [ ] 确认 latest DEF 14A accession number
- [ ] 扫 8-K title 列表 (最近 12 个月)，标记重要的 (M&A / 监管 / 高管变动 / 重大合同)

预计调用: 1 WebFetch (EDGAR 列表) · 输出: `raw/block02_edgar_filings.md`

---

### Block 3: 最近 10-Q 内容 ⏸

依赖 Block 2 拿到 URL。

- [ ] 拉最近 10-Q 财务概要 (current snapshot):
  - revenue / GM / OM / 净利润 / FCF / 经营现金流
  - debt / cash / 投资 / 优先股 / 普通股本
  - reserve interest revenue (核心收入项) — Circle 特有
  - Coinbase 50/50 分成数字 — Circle 特有
  - Risk factors 段重点 (3-5 条最重)
  - MD&A 季度 highlight

预计调用: 2-3 WebFetch (10-Q 不同段) · 输出: `raw/block03_latest_10q.md`

---

### Block 4: 10-K FY2025 + S-1 ⏸

依赖 Block 2 拿到 URL。

- [ ] 10-K FY2025:
  - business overview (业务模式描述 — 怎么挣钱)
  - 完整年度财务 (revenue/GM/OM/FCF FY2025 vs FY2024 同比)
  - 完整 risk factors 列表 (扫，标 3-5 条核心)
  - capital structure (股本 / debt / lock-up 安排)
  - related party (Coinbase 关系细节)
  - 监管历史段 (公司过往与 SEC / FinCEN / 各国监管的互动)

- [ ] S-1 / S-1/A (April 2025 提交版):
  - 3 年 audited pre-IPO 财务 (FY2022-2024)
  - founder 持股 + lock-up
  - 早期投资者持股 + 是否 IPO 套现
  - "use of proceeds"
  - 风险因素 (会列得比 10-K 更详尽)

预计调用: 4 WebFetch (各文档拆段) · 输出: `raw/block04_10k_s1.md`

---

### Block 5: 最近 call transcript ⏸

- [ ] 找最近一次 earnings call (Q4 2025 或 Q1 2026 if available):
  - 来源候选: Seeking Alpha / Tikr / 公司 IR webcast / Motley Fool transcript
  - 重点: CEO 开场 narrative / capital allocation 表态 / 分析师 Q&A 中关于 GENIUS Act / Tether 竞争 / reserve yield 下行的回答
  - 备份: 财报新闻稿 (BusinessWire / GlobeNewswire) + 任何媒体的 highlight 总结

预计调用: 1-2 WebSearch + 1-2 WebFetch · 输出: `raw/block05_calls.md`

---

### Block 6: 市场位置 + 竞争 ⏸

- [ ] DeFi Llama: USDC 总流通 / 链分布 / 历史曲线
  - URL 候选: `https://defillama.com/stablecoin/usd-coin`
- [ ] Coinbase (COIN) 最近一次财报中 USDC 提及 (持有量 + 收入分成数字)
- [ ] Tether (USDT) 最新 attestation (月度) + 行业 USDT/USDC 流通比例
- [ ] PayPal (PYPL) 最近一次财报 PYUSD 提及
- [ ] 链上 holder 集中度 (前 100 wallet 占比) — 可选

预计调用: 3-4 WebSearch + WebFetch · 输出: `raw/block06_market_position.md`

---

### Block 7: Sell-side + 专业新闻 ⏸

- [ ] Yahoo Finance CRCL Analyst tab — consensus EPS / Revenue / 目标价分布 + 评级
- [ ] 3 篇过去 6 个月专业报道 (Bloomberg/Reuters/WSJ/FT/The Block)，重点叙事:
  - GENIUS Act 通过对 Circle 的影响
  - Tether 竞争
  - Reserve yield 下行 (随 Fed 降息)
- [ ] 仓库本身 grep: `notes/videos/` 内是否有 Circle / CRCL / USDC / stablecoin 的 podcast notes
  - 这步**不调外网**，本地 grep

预计调用: 2-3 WebSearch + 1 Grep · 输出: `raw/block07_news_sellside.md`

---

### Block 8: 监管时间表 ⏸

- [ ] **GENIUS Act** (US):
  - 是否已通过？final 文本？
  - 关键条款: reserve composition 要求 / 利息分成 / 发行人资格 / 跨州牌照
- [ ] **MiCA** (EU):
  - Circle Europe SA 持牌状态 (法国)
  - EURC 在 MiCA 下的合规节奏
- [ ] **HK / SG / 日本** 稳定币立法对 Circle 的影响 — 简扫

预计调用: 2-3 WebSearch · 输出: `raw/block08_regulatory.md`

---

## 砍掉的 (接受信息缺口，进 Step 1 审计时降低 confidence)

- 历史每年 1 季 call transcript 抽样 (年轻公司 N/A)
- 8-K 全扫 (只标 Block 2 中重要的)
- proxy 详读 (DEF 14A 找到 URL 但不 deep dive，留待 L3 触发)
- Form 4 内部人交易历史 (只看 IPO 后大额抛售这一项)
- 13F 流向 (只看 top 5 holder snapshot，不做季度对比)
- scuttlebutt 5 类 (留 L3)
- 学术 / BIS / IMF 报告 (留 L3)

---

## 总预计调用

| Block | WebSearch | WebFetch | 时间 |
|---|---|---|---|
| 1 | 2 (done) | 0 | done |
| 2 | 0 | 1 | 5 min |
| 3 | 0 | 2-3 | 15 min |
| 4 | 0 | 4 | 30 min |
| 5 | 1-2 | 1-2 | 15 min |
| 6 | 3-4 | 1-2 | 20 min |
| 7 | 2-3 | 0 + 1 grep | 15 min |
| 8 | 2-3 | 0 | 15 min |
| **合计** | **~12** | **~10-12** | **~115 min ≈ 2 h** |

---

## 执行节奏建议

每个 block 单独执行一次，期间 stop 让用户审视产出。理由:
- 每个 block 完成后回写 EVIDENCE 区一段，避免 context 累积过满
- block 之间可能发现需要调整后续 block 范围 (例 Block 3 发现 reserve revenue 模式不是我想的，要调 Block 5/6 重点)
- 用户可在中途 redirect (例"先看 GENIUS Act，再回看财报")

下一步**等用户 confirm scope** 后从 Block 2 继续。
