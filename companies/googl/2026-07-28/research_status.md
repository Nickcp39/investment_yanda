# GOOGL Research Status — as_of 2026-07-28

最后更新: 2026-07-28（Q2-2026 + 7/28 regime 重定价 refresh）

真实状态标签: **DECISION_DRAFT**（不是 COMPLETE）· completeness ~72%

Decision question:
Alphabet/Google 是否是一门十年后仍值得拥有的高质量生意？$333.71 是否有足够安全边际？Q2-2026 财报、AI-capex 审计、7/28 半导体轮动如何改变 owner earnings 与裁决？

---

## 这一轮做了什么（focused refresh，非从零重研究）
本轮是对 `../2026-06-19/` 基线的 **PRICE + REGIME 重定价**，把 **Q2-2026 财报**（2026-07-22 出）并入，并叠加 **7/28 regime**。持久业务分析（M2 主题、M3 护城河/operator）继承 6/19 并快速复核（6 周内不变）。

| 项 | 状态 |
|---|---|
| M2/M3 thesis-breaking 复核 | ✅ 无破坏性新闻；Q2 反而强化需求端（Cloud +82%、Search +17%） |
| M4 Q2 财报并入 | ✅ **GOOGL 已于 2026-07-22 报 Q2-2026**（季度止 6/30/26）——见下 owner-earnings 更新 |
| M5 regime 叠加 + kill_criteria 更新 | ✅ `inversion_map.md`（F1×F3 拆解 + 7/28 regime 传导 + K-REGIME 新增） |
| M6 重算 MOS/IRR @ $333.71 | ✅ `valuation.md`（三情景全 <8%；buy_below $117） |
| 两轴裁决重导 | ✅ new_money=WATCH / existing=HOLD |
| 价格双源交叉验证 | ✅ Yahoo chart API $333.71 + stockinvest.us $333.71（delta 0.0%）；07-27 close $326.56 由 MacroTrends 佐证 |
| freshness_check.py 机械门 | ✅ **PASS**（exit 0；见文末） |

## Q2-2026 owner-earnings 更新（M4 的核心）
- **营收 $119.8B（+24%）** / **Search $63.4B（+17%）** / **Cloud $24.8B（+82%）**，Cloud 利润率 ~35.5%、backlog $513.9B / 营业利润 $40.8B（+30%）、op 利润率 34%。
- **capex $44.9B（记录）**；**FY2026 指引升至 $195–205B**（自 $180–190B），2027 再升。
- **自由现金流 Q2 转负 −$5.9B**（vs Q1 +$10.1B）；**TTM FCF ~$53.3B（−20% YoY）**；capex/OCF 单季 ~115% / TTM ~71%。
- **回购 $0**；股数升至 12,230M；**首派股息 $0.22/季**（9/14）；发行 ~$18B 强制可转优先股 + LT 债约翻倍至 ~$98B。
- **报表净利 $112B（+298%）严重虚高**：含 ~$99B 非现金未实现股权收益（EPS $9.11 中 ~$6.26）。干净读数 = 营业利润 +30%。
- → **M4 −1 → −2**：capex-吃-owner-earnings 警告**兑现**（强警告，非 veto——资产负债表存活，Cloud 为成长读反证）。

## Final Verdict 摘要
**WATCH · 0% 仓位 · HOLD · 好生意，价格仍不要。**
- $333.71 三情景 10y IRR：bear −11.7% / base −1.5% / **bull +7.7%**——全部 <8% 门槛。
- +5% 反弹（自 7/23 谷底 $317.69）把谷底那丝 bull 缓冲(+8.2%)消掉；按 TTM FCF ~76.6x，比 6/19、7/24 都贵。
- 唯一卡点仍是**价格**（K-E ACTIVE）；被 M4（K-B 触发中）强化。
- buy-below ~$117（base 10%）；avoid above ~$323。

**解除 WATCH / 上修路径**：① 价格回 ~$99–117（base 10–12% IRR）重开 IC 讨论 starter；或 ② capex 见顶 + FCF/share 回升 + 管理层给出 ROI 框架，使 owner-earnings 区间收敛、base 落点上移。7/28 AI-capex 轮动可能是送出①的催化（K-REGIME）。

## 完整度封顶（~72%，未到 COMPLETE 的原因）
- O1 维护 vs 成长 capex 拆分 + incremental ROIC 仍未披露（决定 base 落点；capex 上调 + FCF 转负使其**更**绑定）。
- O2 capex ROI 门槛/预期 ROIC 管理层仍未给（K-C 两周期未解）。
- O3 未重建完整 owner-earnings 桥 / 十年逐年序列（仅并入 Q2 关键行；模型继承 6/19→7/24）。
- O4 Cloud 35.5% 利润率在 Q3 第三方算力桥接下的可持续性未验。
- O5 DOJ adtech 最终救济形态、FOMC(周三)利率路径未定。

> 措辞纪律：本 dossier 为 **DECISION_DRAFT**，非"完成/彻底跑完"。verdict 由**价格**（非信息不足）封顶 WATCH；完整度 ~72%（<80%）另将新钱 ceiling 封在 STARTER，价格封得更低。

## Next Review
- Q3-2026 财报（~10 月下旬）：capex 是否见顶、FCF/share 是否回升、Cloud 利润率能否守 30%+（Q3 第三方算力桥接期）、Search 增速。
- 事件触发：DOJ adtech 救济裁决、FOMC(周三 Warsh)结果、数据中心/TPU 减值（→ K-C 升 🔴）。
- 价格触发：~$139 进观察、~$117 重开 panel、~$250–280（若 regime 轮动拖到）提前重开（K-REGIME）。

## freshness_check 状态 — ✅ PASS
- `freshness.json` manifest 已提交（price + market_cap + 52wk + shares，各 ≥2 独立源；价格自 52wk 低 +78% / 高 −17%，非 INC-001 式低/高贴合）。
- `python scripts/verify_freshness.py --dossier companies/googl/2026-07-28` → **STATUS: PASS（exit 0）**，产物 `freshness_check.json`。
  - price: card 333.71 vs **独立重抓 Yahoo 333.7099**（2026-07-28）→ PASS，2 独立源 1% 内一致。
  - tripwires: T1 band ✅ / T2 low-high-hug ✅（+77.7% off low, −17.1% off high）/ T3 mkt-cap identity ✅（12230M×333.71=4.081T）/ T5 single-value-of-truth ✅ / T6 LIVE-qualitative ✅（litigation 4d, guidance 6d）/ T4 SKIP。
  - 机械门满足，INC-001 式错价风险已排除。
