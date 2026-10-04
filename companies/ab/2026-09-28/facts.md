# AB — Facts / M1 证据脊柱（as_of 2026-09-28）

批次 `pelosi_book_2026-09-28` · 首次建档 · 标的 = **AllianceBernstein Holding L.P.（NYSE: AB，上市合伙企业单位）**

> ⚠️ **结构先说清**：交易的是 AB Holding 的单位。AB Holding 唯一的资产是经营实体 **AllianceBernstein L.P.（AB LP）31.3%** 的权益；
> Equitable Holdings 持 AB LP 68.0%，非关联方 0.7%（AB LP 10-Q）。**AB LP 必须分配全部"Available Cash Flow"**（GP 可酌情保留）。
> 所以 AB 单位 ≈ 一张按季浮动的分配凭证，本卡以**每单位分配**作 owner earnings。

## 0. 行情（LIVE，双源，见 `freshness.json`）
| | 值 | 源 |
|---|---:|---|
| 价格 | **$35.76** | Yahoo chart = Nasdaq historical（差 0.00%） |
| 52 周高 / 低 | $44.11 / $34.92 | Yahoo meta = Nasdaq summary |
| 位置 | −18.9% 距 52 周高点；+2.4% 距 52 周低点（T2 触发，已机械核验为真实收盘） | derived |
| 12 个月 | $37.90 → $35.76（−5.6%） | Yahoo |
| 单位数 | 93.08M（2026-06-30） | 10-Q 封面 |
| 市值 | **$3.33B**（Nasdaq $3.33B） | derived |

## 1. 分配（= owner earnings）
| 季度 | 每单位分配 | 源 |
|---|---:|---|
| Q3'25 | $0.86 | AB 8-K（经检索摘要读取，未重开原文） |
| Q4'25 | $0.96（含年末业绩费） | 同上 |
| Q1'26 | $0.83 | Q2'26 8-K 对比列（一手） |
| Q2'26 | $0.82 | Q2'26 8-K（一手） |
| **TTM** | **$3.47 → 分配率 9.70%** | derived |

按支付年口径（XBRL）：2023 $2.62 → 2024 $2.98 → 2025 $3.47。**2023 的 $2.62 是 2022 熊市的回声 —— 分配会随市场掉 20–30%，这是 bear 情景的先例。**

## 2. AB LP 经营（Q2'26 8-K，2026-07-28）
| | Q2'25 | Q2'26 | |
|---|---:|---:|---|
| 期末 AUM | $829.1B | $905.5B | +9.2%（8 月末 $919B，2026-09-10 8-K） |
| 平均 AUM | $799.5B | $881.2B | +10.2% |
| 调整后净收入 | $844.4M | $887.5M | +5.1% |
| 调整后营业利润 | $273.0M | $293.0M | +7.3% |
| 调整后营业利润率 | 32.3% | 33.0% | +70bp |
| 每单位调整后收益 = 分配 | $0.76 | $0.82 | +7.9% |
| 业绩费 | $38.7M | $46.6M | H1 $112.7M |

**费率在降**：调整后净收入 × 4 / 平均 AUM = 42.2bp（Q2'25）→ **40.3bp**（Q2'26），−1.9bp。收入增速（+5%）慢于 AUM（+10%）——被动占比上升所致。

**Q2 净流入 +$0.8B**（前四季均净流出）：主动 −$8.6B，被动 +$9.4B（含一笔 $9B 被动零售子顾问委托）；
主动股票约 −$11B、应税固收约 −$5B；免税（市政债）约 +$3B；另类/多资产约 +$4B（连续第 6 季正流入）。机构待入金管线 $25.8B。

**8 月末 AUM 结构**：股票 $364B（主动 273 / 被动 91）· 固收 $323B（应税 206 / 免税 99 / 被动 18）· **另类/多资产 $232B**。

## 3. 税务载体（一手，Q2'26 8-K 原文）
> "100% of AB Holding's distributions to foreign investors is attributable to income that is effectively connected with a United States trade or business … subject to federal income tax withholding at the highest applicable tax rate, 37%."

AB Holding 是上市合伙企业（PTP）：美国居民拿 K-1；**非居民：分配 37% 预扣**，出售时另有 §1446(f) 10% 总价预扣（后者为一般规则，未在 AB 文件中逐字核对）。

## 4. 其他
- **CEO 交接**：Seth Bernstein → Onur Erzan，2027-03-31 生效（8-K 2026-09-25）
- 种子资本 $383.1M；合并的公司发起基金投资 $431.1M（10-Q）
- 10-Q 未提私募信贷基金的赎回限制、gating 或减值

## 5. 佩洛西持仓（线索，不进估值）
AB Holding 单位买入，交易日 2026-01-16（当日收盘 $40.17），$1–5M（secondary）；持仓表写 25,000 单位。

## 6. 源登记
| ID | 类型 | 日期 | URL |
|---|---|---|---|
| AB-8K-Q2 | 8-K EX-99.01 | 2026-07-28 | https://www.sec.gov/Archives/edgar/data/1109448/000110944826000194/a2q26earningsrelease.htm |
| AB-10Q-Q2 | 10-Q（AB LP） | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/1109448/000110944826000197/ab-20260630.htm |
| AB-8K-AUM-AUG | 8-K | 2026-09-10 | https://www.sec.gov/Archives/edgar/data/1109448/000110944826000278/ex9901ab2026augustaumrelea.htm |
| AB-8K-CEO | 8-K | 2026-09-25 | https://www.sec.gov/Archives/edgar/data/1109448/000110944826000281/ex9901ableadershipchanges9.htm |
| ABH-XBRL | companyfacts（AB Holding） | 2026-09-28 | https://data.sec.gov/api/xbrl/companyfacts/CIK0000825313.json |
| AB-Q3Q4-25 | 8-K（检索摘要） | 2025-10 / 2026-02 | https://www.sec.gov/Archives/edgar/data/1109448/000110944825000069/a3q25earningsrelease.htm |

## 7. OPEN
- **O-AB1**：私募信贷 AUM 与其收费占比（10-Q 未拆分）—— 2026 年私募信贷负面新闻下的敞口大小
- O-AB2：分渠道费率走势
- **O-AB3**：用户专属：2026–27 居民期 K-1 申报 + 2028 起非居民预扣的实际净额（需 CPA）
- O-AB4：新 CEO 的战略延续性

**完整度 ~62%**。
