# NVDA Valuation (M6) — as_of 2026-07-10 (REFRESH)

价格 [S106]: **$210.96**（2026-07-10 收盘，≤ as_of；Yahoo 再抓 + stockanalysis 两源一致，已过 `verify_freshness.py`）· 稀释股 24,391M · 市值 **~$5.145T**。模型见 `model/scenario_model.csv`。

> **REFRESH of 2026-06-20**：价格由 $210.69 → **$210.96**（+0.13%，实质持平）。期间股价在 6/26 探至 ~$192、7/10 回到 $210.96；**估值结论完全未变**：base 5y IRR **+4.7% < 8% hurdle → 无安全边际**。FILED 财务数（Q1 FY27 / FY26）未变。新增 robotics lens 见 `robotics_lens.md`。

## 1. 倍数起点
- Trailing GAAP EPS (FY26) $4.90 → **P/E ~43x**（GAAP 含股权证券收益，偏高、FY26 旧口径）。
- Forward run-rate non-GAAP EPS ~$7.48（Q1 $1.87 ×4，仍升）→ **forward P/E ~28.2x**。
- 起始 owner-earnings yield（经营 OE 年化 ~$182B / $5.145T）≈ **3.5%**（仍优于 GOOGL 但不便宜）。
- 现价距 52 周高 **−10.8%**、距 52 周低（$161.61，旧 $142 低点已滚出窗口）**+30.5%** → **在区间上部，不在低位**。

## 2. owner earnings 锚（未变）
- 经营性 owner earnings ≈ non-GAAP 净利 ≈ FCF（capex 极轻）→ run-rate **~$180–185B/年**（剔除 GAAP 净利中 ~$30.2B 股权证券收益）。
- 与 GOOGL 关键差异：**无 capex 黑洞**，估值不确定性不在 OE 桥，而在 **run-rate 可持续性 + 入场价**。

## 3. 三情景 IRR（5 年，hurdle 8%）@ $210.96
| 情景 | OE 起点 | 5y CAGR | 退出 P/OE | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−17.6%** |
| Base | $182B | +12% | 20x | ~$266 | **+4.7%** |
| Bull | $185B | +22% | 24x | ~$495 | **+18.6%** |

- **base IRR +4.7% < 8% 门槛** → 现价**无安全边际**（与 06-20 的 +4.8% 实质相同）。
- 赔率：上行 +18.6% / 基准 +4.7% / 下行 −17.6% → **不对称不偏向上行**。
- 8%-hurdle 中性入场（base）：$266 / 1.08^5 ≈ **$181**。现价 $210.96 在其**上方** → 付溢价。

## 4. 价格带（buy-below / size 锚）
| 档位 | 含义 | 价格 | vs $210.96 |
|---|---|---:|---:|
| No new money | 现价无 MOS | **现价 $210.96** | — |
| Starter 区 | base IRR 回到 8%+ | **~$155–181** | −12% 至 −26% |
| Add zone | base IRR ~12–14% | **~$142–155** | −27% 至 −33% |
| No-chase | 现价即是 | **> ~$181**，硬不追向 $236.54 | 现价已在内 |
| 下行保护参考 | bear 兑现 | ~$80（−62%）| 资产负债表存活 |

## 5. binding constraint（未变）
- **是估值（无 MOS），不是 run-rate，更不是机器人**。$210.96：forward 28x、yield 3.5%、base IRR +4.7% < 8%、距高点仅 −10.8% → 价格是 go/no-go 卡点。
- robotics 期权对现价估值贡献 ~nil，不改结论（见 `robotics_lens.md`）。
- run-rate 可持续性（pull-forward + custom-silicon）仍是 size 控制 + kill 监控，次于价格。

## 6. 与完整度的关系
- 完整度 ~65%（10-K 逐行、custom-silicon 定量份额、proxy、纯机器人收入未取）→ verdict 上限本封在 STARTER（60–80%）。
- M6 价格门更严：现价无 MOS → 实际 verdict 封到 **WATCH / 0% 新钱**。镜像 GOOGL/AAPL。
