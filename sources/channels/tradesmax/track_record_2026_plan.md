# TradesMax 2026 必买 14 只股 - 收益审计计划

最后更新: 2026-05-06 · 状态: PENDING USER CONFIRM

## 目的

验证用户的判断："他们整体全部都中了"。把 TradesMax 三集 2026
必买视频里点名的 14 只股票列出来, 拉<em>发布日 close</em> + <em>当前价
(2026-05-06)</em>, 算到今天为止的累计收益, 看 hit rate 与平均回报。

完成后落到 `sources/channels/tradesmax/track_record_2026.md` 作为
持久化审计记录, 同时为整体 source-tier 重评提供证据。

## 14 只标的清单 (从本地 transcript 提取)

### 上集 (发布 2025-12-31)
| # | Ticker | 公司 | 视频里给的入场参考 | 备注 |
|---|---|---|---|---|
| 1 | RMBS | Rambus | 未明确, 提到当前 PE 46x | 内存接口 IP |
| 2 | HROW | Harrow | 未明确 | 眼科药 |
| 3 | SANM | Sanmina | 未明确 | EMS / AI 基建 |
| 4 | ONDS | Ondas Holdings | VIP 介入 $7.60 | 国防无人机 |
| 5 | NVDA | Nvidia | 提到当前 Fwd PE 24.39x | AI GPU |

### 中集 (发布 2026-01-08)
| # | Ticker | 公司 | 视频里给的入场参考 | 备注 |
|---|---|---|---|---|
| 6 | AEP | American Electric Power | 未明确 | 电力 / AI 数据中心供电 |
| 7 | MU | Micron | 提到 2025 涨 240%, 2026 头 3 天再涨 20% | 存储 / HBM (二次推荐) |
| 8 | GLW | Corning | 未明确 | 光纤 / 显示 |
| 9 | RDW | Redwire | VIP 介入 $7.66, 录制日 +39% | 太空基建 |

### 下集 (发布 2026-01-15)
| # | Ticker | 公司 | 视频里给的入场参考 | 备注 |
|---|---|---|---|---|
| 10 | TTMI | TTM Technologies | <em>VIP 12-26 入场 $66.86</em>, 目标 $120 | 高端 PCB |
| 11 | INOD | Innodata | 合理入场 $60, 目标 $150 | AI 数据 (二次推荐) |
| 12 | PLAB | Photronics | 合理入场 $30, 目标 $53 | 掩模版 |
| 13 | NBIS | Nebius | 合理入场 $80, 目标 $200 | AI 云 (回收推荐) |
| 14 | SMR | NuScale Power | 合理入场 $18, 目标 $50 | 小型核电 |

## 数据采集计划

### 需要的数据点 (每只股 3 个)
1. **发布日 close** — 2025-12-31 / 2026-01-08 / 2026-01-15 当天收盘
2. **VIP 提到的入场价** — 上面表里有的 4 只 (ONDS, RDW, TTMI 直接给, 其它没给的就用发布日 close 替代)
3. **当前价** — 2026-05-06 (今天) 最新价

### 计算
- 收益 1: (今天价 - 发布日 close) / 发布日 close → 公平起点
- 收益 2: (今天价 - VIP 入场价) / VIP 入场价 → 他们自己声称的起点
- 区间最高价 / 最低价 (如果能拿到) → 验证"如果止盈"声明

### 工具
- WebSearch + WebFetch
- 优先 Yahoo Finance 历史 OHLC URL: `https://finance.yahoo.com/quote/<TICKER>/history/`
- 备选 Google Finance / Stockanalysis.com
- 当前价用 `<TICKER> stock price` 类查询

### 执行批次 (每批 ≤4 个并行 fetch, 之间停下回写状态)

| 批 | 标的 | 内容 | Status |
|---|---|---|---|
| B1 | NVDA, MU, NBIS | 当前价 + 发布日 close | pending |
| B2 | RMBS, HROW, SANM, ONDS | 当前价 + 发布日 close | pending |
| B3 | AEP, GLW, RDW | 当前价 + 发布日 close | pending |
| B4 | TTMI, INOD, PLAB, SMR | 当前价 + 发布日 close | pending |
| B5 | (汇总) | 计算收益, 写入 track_record_2026.md | pending |

## 输出格式 (track_record_2026.md 草稿)

```markdown
# TradesMax 2026 必买 14 只股 - 截至 2026-05-06 战绩

| # | Ticker | 发布日 close | VIP 入场 | 当前 (5/6) | 收益 vs 发布 | 收益 vs VIP |
|---|---|---|---|---|---|---|
| 1 | RMBS | $XX.XX | — | $YY.YY | +Z% | — |
...

汇总:
- 14 只里 N 只上涨 (hit rate XX%)
- 平均收益: XX%
- 中位数收益: XX%
- 最大涨幅: XX (Ticker), 最大跌幅: XX (Ticker)
- 同期 SPY: XX%, QQQ: XX%, SOX: XX%
- 跑赢大盘: 是/否, 跑赢 SOX: 是/否

结论: ...
```

## 已知盲点 / 注意

1. **没有验证 VIP 自报的 175% 2025 年回报** — 不在本次范围, 之后单独审计
2. **盘中价 vs close** — 当前价取最近一个 close 而非盘中
3. **股息再投资** — 不计 (短期为主, 影响小)
4. **拆股 / 分红事件** — 14 只里这段时间没记录到拆股, 但要 sanity check
5. **survivor bias 注意** — 这 14 只都是他们公开喊出来的, 我们没有他们 VIP 群里
   <em>没喊出来</em>但事后失败的标的可见性

## 等用户确认

要不要我按 B1→B5 顺序往下跑? 还是你想先调整范围 (比如先只跑下集那 5 只 +
明确给了入场价的几只, 信号最干净)?
