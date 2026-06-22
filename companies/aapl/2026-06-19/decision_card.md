# AAPL Decision Card — as_of 2026-06-19

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-06-19
**context_label**: exceptional_compounder_overpriced · **status**: DECISION_DRAFT · **completeness**: ~60%

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$298.01**（2026-06-18 收盘，≤ as_of）|
| market cap | **~$4.39T**（14.726B 稀释股 × $298.01）|
| business_verdict | **exceptional** |
| new_money_verdict | **WATCH** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%**（新钱；价格门未过）|
| suggested_max_size | **~15%**（耐久性支持 Core 级，但需价格配合，非现状）|
| buy_below | **~$231**（base IRR 8%，~28x trailing OE）|
| verdict ceiling | **WATCH**（价格门 binding；完整度 ~60% 一致）|
| binding_constraint | **价格（估值起点），非耐久性、非完整度** |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度+全年全回挂 A1；价格 A2 |
| M2 主题/机制 | context+conviction | **+2** | high | 装机量年金 + Services 复利，多年一手坐实 |
| M3 利润池/耐久 | conviction | **+2** | med | 生态切换成本 + 品牌定价权；operator 4/5；TAC/App Store/AI 入口是耐久 haircut |
| M4 财务现实 | conviction | **+2** | high | owner earnings 干净(capex-light, FCF≈净利)、净现金 $61.9B |
| M5 反演/陷阱 | risk | **−1** | med | 价格风险(M6 处理)+TAC/App Store 边际侵蚀(haircut)；无结构破裂/无资产负债表死亡 → 非 veto |
| M6 定价/仓位 | price+output | **−1** | high | ~36x、yield 2.7%、base IRR +2.7% « 8%、贴 52 周高 → 价格 binding，新钱 WATCH |

## 价格带
- **WATCH 现价区**: $280–317，不加新钱。
- **STARTER 触发**: ≤ ~$231（base IRR 8%，~28x），开 3–5%。
- **ADD**: ≤ ~$210（base IRR ~10%，~26x），向 8–15%（耐久性支持，价格配合）。
- **No-chase**: 现价 $298 及以上。
- **bear 参考**: ~$203（−32%，可存活非永久减值）。

## 三情景（5y IRR，含缩股 2.5%/yr + 股息，hurdle 8%）
| 情景 | OE CAGR | 退出 P/OE | y5 OE/sh | 退出价 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | 0% | 22x | ~$9.3 | ~$203 | **−7%** |
| Base | 6% | 27x | ~$12.4 | ~$334 | **+2.7%** |
| Bull | 11% | 32x | ~$15.6 | ~$499 | **+11%** |

## Kill Criteria
K1 iPhone 连续 2–3 季降 **且** Services 跌破高个位数（年金桥断）/ K2 Google TAC 实质裁减 + Services 毛利率压缩（O1）/ **K3 App Store 全球强制低费率致 Services 结构受损（唯一可升 veto）** / K4 装机量绝对下滑 / K5 价格 ≥$298 维持（新钱仍 WATCH，≤$231 才解锁）/ K6 Cook 继任风险。

## runner_dissent
2016 SEVERE-UNDERSIZE 教训在此最响: 当年因"成熟/见顶"叙事给 +1318% 复利机器封过低天花板。WATCH-0% 有重蹈覆辙之忧——**但本案由价格(客观)封顶，不由耐久性(叙事)封顶**: 2016 入场 ~10x + 净现金占市值 31%（世代级边际），2026 ~36x + 净现金 1.4%（边际消失），base 5y IRR +2.7% « 8% 且赔率向下不对称。**耐久性先验未下调（正是 2016 的修复）**，只让价格做封顶。2016 错在便宜时胆小；贵时不追新钱是相反的对的纪律，不是复发。存量 HOLD（不为"贵了"卖十年生意），新钱 WATCH（零边际）。价格回到 ~$231 即翻 STARTER。详见 decision_card.json。

## OPEN（封顶完整度；价格门已是更严卡点）
O1 Google TAC 量级（binding 监控）· O2 10-K 逐行 · O3 proxy/继任 · O4 AI 入口变现/留存定量 · O5 早期 10 年序列(B2) · O6 关税/供应链。
