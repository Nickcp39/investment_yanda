# NVDA Facts — as_of 2026-07-10 (REFRESH)

> REFRESH of `../2026-06-20/`. **只 LIVE 数据（价格/市值/52 周带）重取；FILED 财务数（Q1 FY27 / FY26 营收/利润/资产负债表）未变，原样带过。** 新增 robotics 段（see `robotics_lens.md`）。价格 $210.69 → **$210.96**（+0.13%，实质持平）。

## EVIDENCE — LIVE（本次重取，≥2 源交叉，过 freshness 门）

### 价格 [S106] — LIVE
- 末收盘（≤ as_of）**$210.96（2026-07-10）**（Yahoo chart 再抓 $210.96 + stockanalysis $210.96，两源一致，过 `verify_freshness.py`）。
- 52 周高 **$236.54** / 52 周低 **$161.61**（旧 $142.03 低点已滚出 52 周窗口）→ **现价距高点 −10.8%、距低点 +30.5%，在区间上部**。
- 市值 ≈ **$5.145T**（24,391M × $210.96）。stockanalysis 报 ~$5.11T（差 ~0.7%，稀释 vs 基本股本口径）。
- 相对 06-20（$210.69）：期间 6/26 探至 ~$192、7/10 回 $210.96 → **净变动 +0.13%，估值结论未变**。

### China / 出口管制 [S002/S010/S011] — LIVE-qualitative（未见新权威事件，沿用 06-20）
- 2026-02 美国政府重发对华 H200 出口许可（限特定客户）；黄仁勋 2026-03 GTC 称已收中国 H200 订单、重启生产 → China 是 Q2 指引**未计入的可恢复期权**，非永久损失。
- ⚠ freshness T6 WARN：最新权威事件 2026-03-18 距 as_of >45d；本次未检索到更新的确权事件，维持保守处理（Q2 指引仍归零 China DC compute）。作为上行期权，不进 base。

## EVIDENCE — FILED（未变，锚定 06-20，回挂 A1/A2）
### 锚定季度 Q1 FY27（ended 2026-04-26）[S001/S002]
- 总营收 **$81.615B**（+85% Y/Y、+20% Q/Q）。Data Center **$75.246B**（+92% Y/Y，占 **~92%**）。DC Compute $60.4B（+77%）、DC Networking $14.8B（+199%）。
- 段：Compute & Networking $74.55B（+88%）；Graphics $7.07B（+58%）。
- **市场平台口径 [S102]**：Data Center $75,246M · Edge Computing（含 PC/游戏机/工作站/AI-RAN/**机器人+汽车**）$6,369M · Total $81,615M。
- GAAP/non-GAAP GM **74.9%/75.0%**；GAAP 营业利润 $53.536B（+147%）；GAAP 净利 $58.321B（含 ~$30.2B 股权证券收益）；GAAP EPS $2.39 / non-GAAP $1.87；稀释股 24,391M。
- OCF **$50.344B**；capex **$1.757B**；FCF **$48.554B**（~96%）。净现金 ~$72B（现金+证券 ~$80.6B vs 债务 ~$8.47B）。
- Q2 FY27 指引 **$91.0B ±2%**，明确不含 China DC compute。

### 机器人/汽车段 [S101/S102/S103] — 新增（回答 batch thesis）
- **Automotive 平台 FY26 $2,350M（+39% Y/Y；Q4 FY26 $604M）≈ 总营收 1.09%** [S101, B1 回挂 8-K]，多为 DRIVE 自动驾驶 design-win，非机器人。
- 纯 robotics/embodied-AI（Jetson+Isaac+GR00T dev business）**NVDA 未单独披露** → 估 **<1%（~0.3–0.5%）**，OPEN(O7)。
- 机器人产品/生态（A2/B1，dated 但非营收）：Jetson Thor / T4000 模块（$1,999/颗 @1,000 量）、IGX Thor 工业边缘；Isaac/GR00T/Cosmos/Omniverse 开放模型；客户 Boston Dynamics/Caterpillar/Franka/LG/NEURA [S103]。→ **产品/生态是真的，机器人营收体量是 anticipation**。

### 全年 FY26（ended 2026-01-25）[S004/S003]
- 营收 **$215.9B**（+65%）；GAAP 净利 $120.1B；GM 71.1%/71.3%；EPS $4.90/$4.77。capex 仅 $6.1B。
- 资本配置：2026-05-18 股息 $0.01→$0.25、新增 $80B 回购授权（在 near-high 执行，非低位）。

## INTERPRETATION（派生）
- **买 NVDA = 买 AI 数据中心算力（~92%），不是机器人 alpha**。机器人是嵌在平台里的近乎免费期权（详见 `robotics_lens.md`）。
- 估值（$210.96）：forward P/E ~28x、起始 OE yield ~3.5%、base 5y IRR **+4.7% < 8% hurdle → 无安全边际**。
- owner earnings ≈ FCF ≈ non-GAAP 净利（capex 极轻）；GAAP 净利含 ~$30.2B 非经营股权收益需剔除。

## SENTIMENT（仅情绪/线索）
- 现价距 52 周高仅 −10.8%、在区间上部——不是低位/偏空。市场对 AI capex 持续性 + custom-silicon 替代仍分歧，但价格未 price-in 见顶。
- 机器人/humanoid 是强多头叙事（美股投资网 D1 线索，仅 lead），但**未进 NVDA 现金流**——不支撑 buy。

## OPEN（封顶完整度）
- O1 FY26 10-K 逐行现金流/D&A/库存承诺（OCF/FCF 为 B1 近似）。
- O2 10 年精确序列（早年二手口径冲突）。
- O3 DEF 14A proxy 未重取（Huang 薪酬/董事会/succession）。
- O4 custom-silicon 对 DC 份额的**定量**侵蚀未取一手（blocking）。
- O5 China H200 重启金额量级未建模（按保守归零 + 上行期权）。
- O6 供应链（CoWoS/HBM）产能与 purchase obligations 库存风险（存货 $25.8B）。
- **O7 纯机器人/具身智能收入金额（NVDA 未单独披露，估 <1%）。**
- **O8 humanoid 起量收入量级与时点（期权，未建模，拐点不可知）。**

## Contradictions
- C1 fiscal-year off-by-one（二手把官方 FY26 标 FY2025）；以 SEC 官方口径为准。
- C2 FY26 OCF/FCF 为 B1 聚合，待 10-K 逐行。
- C3 GAAP 净利含股权证券收益，用 non-GAAP / 经营 OE 看估值更稳。
- C4 52 周低口径：Yahoo adjclose $163.85 vs stockanalysis 盘中 $161.61（差 ~1.4%，均远高于现价，不影响判断；采用 $161.61）。
