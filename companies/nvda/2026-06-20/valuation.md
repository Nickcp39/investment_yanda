# NVDA Valuation (M6) — as_of 2026-06-20

价格 [S006]: **$210.69**（2026-06-18 收盘，≤ as_of；Yahoo + stockanalysis + websearch 三源一致，已过 `verify_freshness.py`）· 稀释股 24,391M · 市值 **~$5.139T**。模型见 `model/scenario_model.csv`。

> **CORRECTED**：本版改正 `../2026-06-19/`，那版把现价写成 **$145.48**（≈ 52 周最低 $142.03），导致 base IRR 被高估为 +13%、verdict 误判为"价格友好 STARTER"。真实价 $210.69 下结论翻为 **WATCH（无安全边际）**。见 `backtests/framework_validation/INCIDENTS.md` INC-001。

## 1. 倍数起点
- Trailing GAAP EPS (FY26) $4.90 → **P/E ~43x**（GAAP 含股权证券收益，偏高且为 FY26 旧口径）。
- Forward run-rate non-GAAP EPS ~$7.48（Q1 $1.87 ×4，且环比仍升）→ **forward P/E ~28.2x**。
- 起始 owner-earnings yield（经营 owner earnings 年化 ~$182B / $5.139T 市值）≈ **3.5%**（vs 错版误算的 5.1%；仍优于 GOOGL 1.45%，但已不便宜）。
- 现价距 52 周高 **−10.9%**、距 52 周低 **+48.3%** → **在区间上部，不在低位**（错版误称"贴 52 周低、−38%"）。

## 2. owner earnings 锚
- 经营性 owner earnings ≈ non-GAAP 净利 ≈ FCF（capex 极轻、R&D 费用化）→ run-rate **~$180–185B/年**（剔除 GAAP 净利中的 ~$30.2B 股权证券收益）。
- 与 GOOGL 关键差异: **不存在 capex 黑洞**，owner earnings 与 FCF 一致，估值不确定性**不在 owner earnings 桥**，而在 **run-rate 的可持续性 + 入场价**（错版只点了前者、漏了后者，因为它用了错价）。

## 3. 三情景 IRR（5 年，hurdle 8%）@ $210.69
| 情景 | OE 起点 | 5y CAGR | 退出 P/OE | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−17.6%** |
| Base | $182B | +12% | 20x | ~$266 | **+4.8%** |
| Bull | $185B | +22% | 24x | ~$495 | **+18.6%** |

- **base IRR +4.8% < 8% 门槛** → 现价**无安全边际**（与错版 +13% 截然不同；那 +13% 是 $142–145 低位区的收益率，被错当成今天的价）。
- 赔率: 上行 +18.6% / 基准 +4.8% / 下行 −17.6% → **不对称已不再偏向上行**:下行更深、基准不过门槛。
- 8%-hurdle 中性入场（base）: $266 / 1.08^5 ≈ **$181**。现价 $210.69 在其**上方** → 付的是溢价，不是折价。

## 4. 价格带（buy-below / size 锚）
| 档位 | 含义 | 价格 | vs $210.69 |
|---|---|---:|---:|
| No new money | 现价无 MOS | **现价 $210.69** | — |
| Starter 区 | base IRR 回到 8%+ | **~$155–181** | −12% 至 −26% |
| Add zone | base IRR ~12–14% | **~$142–155**（向 52 周低）| −26% 至 −33% |
| No-chase | 现价即是 | **> ~$181**，硬不追向 $236.54 | 现价已在内 |
| 下行保护参考 | bear 兑现 | ~$80（−62%）| 资产负债表存活 |

## 5. binding constraint
- **是估值（无 MOS），不是 run-rate**。在 $210.69：forward 28x、yield 3.5%、base IRR +4.8% < 8%、距高点仅 −11% → **价格是 go/no-go 卡点**。
- 与 2023 盲测案（卡点=估值 air-pocket，~198x）方向一致但程度温和:NVDA 只是**适度高于公允**（base 略低于 hurdle），非 GOOGL 那种 ~69x 深度无 MOS。
- run-rate 可持续性（pull-forward + custom-silicon 份额）仍是 **size 控制 + kill 监控**，但**次于价格**——价格先把新钱 verdict 压到 WATCH。

## 6. 与完整度的关系
- 完整度 ~65%（10-K 逐行、custom-silicon 定量份额、proxy 未取）→ verdict 上限本就封在 STARTER（60–80% 区间）。
- M6 价格门更严:现价无 MOS → 实际 verdict 封到 **WATCH / 0% 新钱**。镜像 GOOGL（同因子，被价格封）与 AAPL（exceptional 但 overpriced → WATCH）。
