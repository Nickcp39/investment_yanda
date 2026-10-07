# 交易通道批次 · 2026-10-06 — 运行计划 (PLAN)

**批次 ID** `trading_rails_2026-10-06` · **as_of** 2026-10-06（2026-10-07 09:45 EDT 盘中运行 → 锁定 10-06 收盘）· `lean-6module-v1.1` · weights `none` · 13 家均为首次建档（`companies/circle/` 原有一份 2026-05 的 dry-run 计划，未取数）

## 触发
用户 2026-10-07：美股要开始 23 小时交易，"类似 Robinhood、Coinbase 这种收中间手续费、有自己代币的公司会不会是下一个目标"；先确认交易需求是否真实上涨，再给公司名单和它们的"铲子公司"。随后："IBKR、HOOD、COIN、VIRT、CBOE、CME、FUTU，只看美股的，做 pipeline 骨架分析和买入评级，包括配套和做市商铲子公司。"

## 0. 选股：一条交易通道上的四类公司（只看美股上市）
| 类别 | 公司 | 文件夹 | 代码 | 在价值链里的位置 |
|---|---|---|---|---|
| 开店的（券商） | Interactive Brokers | `ibkr` | IBKR | 全球自动化券商 |
| | Robinhood | `hood` | HOOD | 零售一体化 App |
| | Coinbase | `coin` | COIN | 加密交易所 + USDC 分成 |
| | 富途 | `futu` | FUTU | 亚洲散户买美股（20-F / 6-K 申报） |
| 做市商（券商的上游） | Virtu | `virt` | VIRT | 付钱买订单流（Citadel、Jane Street、Susquehanna 未上市） |
| 交易所（收过路费） | Cboe | `cboe` | CBOE | 独家指数期权 |
| | CME | `cme` | CME | 期货 + 自有清算 |
| | ICE | `ice` | ICE | 纽交所 + 布伦特 + 数据 |
| | Nasdaq | `ndaq` | NDAQ | 23/5 发起者 + 金融科技 + 指数 |
| 配套 | Broadridge | `br` | BR | 券商与基金后台 |
| | Circle | `circle` | CRCL | USDC 发行方 |
| | BitGo | `btgo` | BTGO | 机构加密托管 |
| | Securitize | `secz` | SECZ | 代币化发行与过户 |

排除：清算公用设施 OCC / DTCC（不可投资）；Blue Ocean、Citadel Securities、Jane Street、Kalshi、Polymarket、Kraken（未上市）；Flow Traders（非美股）；MIAX、Webull、eToro、Bullish、Gemini、Galaxy（未在用户名单内，可后续补）。

## 1. A0 基准新鲜度门（INC-002）
`git fetch` → 落后 0 个提交；13 个 `<ticker>/2026-10-06/` 目录均不存在。

## 2. 本批特有的方法
1. **OE₀ = 正常化税后净利**：券商、交易所、做市商的经营现金流被客户资金和保证金扭曲，FCF 不可用；交易所与 BR 用公司"adjusted"口径（加回并购无形资产摊销）
2. **周期正常化**：13 家里 9 家的 TTM 处在交易量 / 利率高位（美股成交 2025 年 +44.6%，期权连续 6 年创纪录）→ base OE₀ 打在 TTM 之下（IBKR −12%、FUTU −20%、VIRT −33%、CBOE −8%）；COIN 用 10 个季度调整后 EBITDA 均值折算周期中位
3. **全部转换口径**：IBKR（A 类 + Holdings 持有的 LLC 单位 = 1,703.8M）、VIRT（Weighted Average Adjusted shares 159.9M）
4. **ramp 情景**：CRCL / BTGO / SECZ 盈利刚起步，用第 1 年与第 10 年 OE 两点插值；"8% 所需"改为解第 10 年 OE
5. **一手原文本地检索**：`fetch_filings.py` 新增表格逐行压平（交易所财报几乎全是表）
6. **第二价格源**：Nasdaq historical API（与石油批次相同）

## 3. 脚本
| 脚本 | 产物 |
|---|---|
| `fetch_data.py` | `data/snapshot_2026-10-06.json`（Yahoo + Nasdaq 价格、XBRL TTM） |
| `fetch_filings.py` | 各 dossier `raw/*.txt`（10-K / 20-F、10-Q、财报 8-K / 6-K） |
| `valuation_model.py` | `data/valuation_2026-10-06.*` |
| `make_freshness.py` | 各 dossier `freshness.json` |
| `dossier_content.py` + `make_dossiers.py` | 各 dossier 的 7 个 md + `decision_card.json` |
| `scripts/verify_freshness.py` | 各 dossier `freshness_check.json / .txt`（13/13 PASS） |

## 4. 进度
| 公司 | 完整度 | verdict | base IRR | buy_below | binding |
|---|---:|---|---:|---:|---|
| IBKR | 58% | WATCH | +4.5% | $65.37 | 价格 |
| HOOD | 57% | WATCH | +5.5% | $88.74 | 价格 + 周期 |
| COIN | 55% | WATCH | +6.2% | $156.94 | 价格 + 加密周期 |
| FUTU | 55% | WATCH | +12.1% | $160.38 | 完整度 + 中国监管 |
| VIRT | 54% | WATCH | +9.0% | $66.04 | 周期 + 完整度 |
| CBOE | 57% | WATCH | +10.0% | $327.38 | 完整度 |
| CME | 57% | WATCH | +9.9% | $313.98 | 完整度 |
| ICE | 56% | WATCH | +10.5% | $188.03 | 完整度 |
| NDAQ | 56% | WATCH | +9.2% | $102.24 | 完整度 |
| BR | 56% | WATCH | +11.4% | $207.68 | 完整度 + 替代叙事 |
| CRCL | 52% | WATCH | +4.8% | $62.08 | 价格 + 利率 |
| BTGO | 45% | WATCH | +5.9% | $5.91 | 价格 + 完整度 |
| SECZ | 35% | INFO-GAP | — | — | 完整度 |

结论见 [synthesis.md](synthesis.md)。
