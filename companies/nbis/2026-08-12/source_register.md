# Source Register — NBIS 2026-08-12

⚠️ **本次全部为二手聚合源。** 一手源（SEC EDGAR、nebius.com、businesswire）
在本运行环境下均返回 `EGRESS_BLOCKED`，无法取得。

| source_id | 类型 | 说明 | 一手/二手 |
|---|---|---|---|
| SRC-Q2A | 财经媒体 | TradingKey / Investing.com / Crypto Briefing —— Q2 损益数字 | 二手 |
| SRC-Q2B | 财经媒体 | ts2.tech / 24-7 Wall St / MarketScreener —— 现金流与资产负债表 | 二手 |
| SRC-Q2C | 财经媒体 | Seeking Alpha news / StockTwits / GuruFocus —— 产能、定价、融资 | 二手 |
| SRC-BLOCKED-1 | **一手（未取得）** | SEC EDGAR Form 6-K FY2026 | ❌ EGRESS_BLOCKED |
| SRC-BLOCKED-2 | **一手（未取得）** | nebius.com/investor-hub 股东信 | ❌ EGRESS_BLOCKED |
| SRC-BLOCKED-3 | **一手（未取得）** | BusinessWire 原始新闻稿 20260812963359 | ❌ EGRESS_BLOCKED |

## 用户可自行取得一手源的路径

1. SEC EDGAR：`sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001513845&type=6-K`
2. Nebius Investor Hub：`nebius.com/investor-hub`（股东信 PDF）
3. 电话会转录：Seeking Alpha / Motley Fool / stockanalysis.com

**取得后需回填 `claim_ledger.csv` 的 status 栏，并解决 C110 / C111 两处冲突。**
