# NVDA Facts — as_of 2026-06-20

> 只收录已审计、回挂 source_id 的事实。EVIDENCE = A1/A2 一手或高可靠二手已核；INTERPRETATION = 派生判断；SENTIMENT/OPEN 单列。
> **CORRECTED**：价格、距高/低点、China 出口管制三处 LIVE 数据相对 `../2026-06-19/` 已改正（错版把 52 周低 $142.03 当成现价 $145.48，并把 China 写成"永久损失"）。FILED 财务数（营收/利润/资产负债表）未变（原版已经独立核验正确）。

## EVIDENCE（一手锚定，A1/A2）

### 锚定季度 Q1 FY27（quarter ended 2026-04-26）[S001/S002]
- 总营收 **$81.615B**，record，+20% Q/Q、+85% Y/Y。
- Data Center **$75.246B**（+92% Y/Y），占总营收 **~92%**。DC 内: Hyperscale $37.87B（~50% DC）、AI Clouds/Industrial/Enterprise $37.38B、Edge $6.37B。
- DC Compute $60.4B record（+77% Y/Y）；DC Networking $14.8B record（+199% Y/Y）→ 网络是新的高增长第二腿。
- 段: Compute & Networking $74.55B（+88%）；Graphics $7.07B（+58%）。
- GAAP/non-GAAP 毛利率 **74.9% / 75.0%**（环比基本持平，Blackwell 占多数营收）。
- GAAP 营业利润 **$53.536B**（+147% Y/Y）；GAAP 净利 **$58.321B**（+211% Y/Y，**含可交易股权证券收益**）；GAAP 稀释 EPS **$2.39**，non-GAAP **$1.87**。
- 稀释加权股数 **24,391M**。
- 经营现金流 **$50.344B**；capex 仅 **$1.757B**；自由现金流 **$48.554B**（FCF/OCF ~96%）。
- 资产负债表（4/26）: 现金等价物 $13.24B + 可交易债券 $37.10B + **可交易股权证券 $30.24B**；存货 **$25.80B**；总债务 **$8.47B**（ST $1.0B + LT $7.47B）；股东权益 $195.47B；总资产 $259.47B。
- **资产负债表 fortress**: 现金+证券 ~$80.6B vs 总债务 ~$8.47B → 净现金 ~$72B。

### 指引 [S001]
- Q2 FY27 营收指引 **$91.0B ±2%**，**明确不含任何 China DC compute 营收**。
- Q2 毛利率指引 74.9%/75.0% ±50bps；opex ~$8.5B/$8.3B；FY27 税率 16–18%。

### China / 出口管制 [S002/S010/S011] — CORRECTED（LIVE-qualitative）
- Q1 FY27 **对 China 的 Hopper DC 产品出货 = $0**（vs Q1 FY26 的 $4.6B）；Q2 指引把 China DC compute 归零（NVDA **保守**口径）。
- **但管制在松动，不是扩大**: **2026-02 美国政府重发了对华 H200 出口许可**（限特定客户）；**黄仁勋在 2026-03 GTC 表示已收到中国 H200 订单、正重启生产** → China 是 Q2 指引**未计入的可恢复期权**，**非"永久损失"**（这是错版 2026-06-19 的过时偏空措辞）。
- 上年同期有 **$4.5B H20 超额库存计提**；本季无类似计提 → 毛利率环比改善的对照项。

### 资本配置 [S001/S003]
- 2026-05-18 董事会: 季度股息 **$0.01 → $0.25/股**；新增 **$80.0B** 回购授权。
- FY26 全年返还股东 **$41.1B**（回购 + $974M 股息）；FY-end 剩余授权 $58.5B。
- 注：$80B 回购是在现价 **距高点仅 −11%（near-high）** 时进行，**非"低位回购"**（错版据错价误判为低位）。

### 全年 FY26（year ended 2026-01-25）[S004/S003]
- 营收 **$215.9B**（+65%）；GAAP 净利 **$120.1B**；GAAP 营业利润 **$130.4B**；GM 71.1%/71.3%；GAAP EPS **$4.90**，non-GAAP **$4.77**。
- OCF ~$102.7B、FCF ~$96.6B（B1，待 10-K 逐行核）。**FY26 capex 仅 $6.1B**（vs $3.4B FY25）→ owner earnings ≈ FCF（asset-light）。

### 价格 [S006] — CORRECTED（LIVE）
- 末收盘（≤ as_of）**$210.69（2026-06-18）**（Yahoo + stockanalysis + websearch 三源一致，过 `verify_freshness.py`）；52 周高 $236.54 / 低 $142.03 → **现价距高点 −10.9%、距低点 +48.3%，在区间上部**。
- 市值 ≈ **$5.139T**（24,391M × $210.69）。
- ⚠ 错版 `../2026-06-19/` 写的 $145.48 ≈ 52 周最低 $142.03，是抓取取到了序列最低点而非最新收盘（见 INC-001）。

## INTERPRETATION（派生，非新事实）
- **owner earnings ≈ FCF**: capex（$6.1B FY26 / $1.76B Q1）远小于折旧与 OCF，维护性 capex 微，报表净利与 owner earnings 缺口主要来自**可交易股权证券公允价值波动**（Q1 GAAP 净利 $58.3B 含 ~$30.2B 非经营性股权收益，应剔除以看经营 owner earnings）。
- **生意属性**: 全栈 AI 加速计算瓶颈（GPU + CUDA + NVLink/InfiniBand/Spectrum-X 网络 + 先进封装/HBM）；DC 占 ~92%，已从"多元半导体公司"变为"AI 基础设施单一引擎"。
- **估值倍数**（$210.69）: trailing FY26 GAAP EPS $4.90 → P/E ~43x（GAAP 含股权收益，偏高）；FY27 run-rate（Q1 非 GAAP $1.87×4≈$7.5）→ forward P/E **~28x**。起始 OE yield ~3.5%，base 5y IRR +4.8% < 8% hurdle → **现价无安全边际**（详见 valuation.md）。

## SENTIMENT（仅情绪/线索，不支撑 buy）— CORRECTED
- 现价 $210.69 **距 52 周高仅 −11%、在区间上部**——**不是"贴 52 周低/情绪偏空"**（错版据错价误述）。市场对 AI capex 周期持续性 + custom-silicon 替代仍有分歧，但价格并未 price-in 一个见顶。
- 管理层"AI 工厂 = 人类史上最大基建扩张"为强多头叙事（CEO 主观陈述，非事实）。

## OPEN（未取/未核，封顶完整度）
- O1: FY26 10-K 逐行现金流/D&A/库存承诺/purchase commitments 未逐项摘（OCF/FCF 为 B1 近似）。
- O2: 10 年精确序列（FY17–FY23 各年净利/GM/股本）二手口径冲突，未达 A 级。
- O3: DEF 14A proxy 未重取 → Huang 薪酬、董事会独立性比例、succession 披露 OPEN。
- O4: custom-silicon（CSP 自研 ASIC）与 AMD MI 系列对 NVDA DC 份额的**定量**侵蚀未取一手。
- O5: China H200 重启的**金额量级**（许可范围、能恢复多少 DC compute 营收）未建模——现按 Q2 指引保守归零、作为未计入的上行期权处理。
- O6: 供应链（TSMC CoWoS / HBM）产能与 purchase obligations 的库存风险未逐项核（存货已升至 $25.8B）。

## Contradictions（冲突登记，不提前择优）
- C1: **fiscal-year 标注冲突** — stockanalysis 等二手把官方 FY2026 标为 "FY2025"（off-by-one）。已以 SEC 官方口径（FY26 = year ended 2026-01-25）为准，二手早期年份降权。
- C2: FY26 OCF/FCF（$102.7B/$96.6B）来自二手聚合（B1），与 10-K 逐行可能有小差异；标注待核，不影响量级判断。
- C3: GAAP 净利含可交易股权证券收益（Q1 $30.2B 头寸），使 GAAP EPS 高于经营性盈利能力 → 用 non-GAAP / 经营 owner earnings 看估值更稳。
