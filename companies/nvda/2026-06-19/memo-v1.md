# NVDA Decision Memo v1 — as_of 2026-06-19

**Verdict: STARTER（新钱）· initial 3–5% · max ~12% · status = DECISION_DRAFT · completeness ~65%**
价格 $145.48（2026-06-18 收盘）· 市值 ~$3.55T · pipeline_version=lean-6module-v1

## 1. 一句话论点
NVDA 是 AI 加速计算的全栈瓶颈（GPU+CUDA+网络+系统），owner earnings 异常干净（capex-light，FCF≈owner earnings≈$182B run-rate），资产负债表净现金 $72B，且当前价格 forward ~19x / 起始 OE yield 5.1% / base 5y IRR +13% **留有正安全边际**——与 GOOGL"好生意错价格"相反，这次价格站在买方这边。

## 2. 为什么是 STARTER 而非 WATCH/REJECT 或 CORE
- **非 WATCH/REJECT**: 估值友好（base IRR >8% 门槛）、owner earnings 干净、瓶颈被多季一手数据坐实、资产负债表 fortress。前瞻不确定性（pull-forward / custom-silicon）= haircut + size 控制，不是 veto（修好的 SNDK 老病: 别因前瞻不确定就 over-veto 真瓶颈）。
- **非 CORE**: ①完整度 ~65% 封 ceiling 在 STARTER；②周期股纪律封 size 在 Confirmed 以下（max ~12%，不进 Core 15–25%）；③custom-silicon 份额十年终局在能力圈边缘（O4 定量缺）。

## 3. 关键事实（全 A1/A2）
- Q1 FY27: 营收 $81.6B(+85% Y/Y)、DC $75.2B(+92%)、网络 $14.8B(+199%)、GM 74.9%、FCF $48.6B、净现金 $72B [S001/S002]。
- Q2 指引 $91B（不含 China DC compute）[S001]。FY26 全年: 营收 $215.9B、净利 $120.1B、capex 仅 $6.1B、返还股东 $41.1B [S003/S004]。
- 资本配置: 季度股息 $0.01→$0.25、新增 $80B 回购授权（低位回购）[S001]。
- 价格贴 52 周低 $142、距高点 −38% [S006]。

## 4. binding constraint
**需求耐久性 vs pull-forward + DC 份额 vs custom silicon**——不是价格。估值在 $145 是友好的；真正控制 size 的是"+85% 增速/75% 毛利率这些极值能持续多久"。

## 5. 仓位与价格带
- **Starter 主锚**: 现价区 $130–150，initial 3–5%。
- **Add zone**: ~$110–130（向 52 周低破位的回撤）或营收连续兑现指引后 → 加向 8–12%。
- **No-chase**: > ~$200（隐含 IRR <8%）。
- **下行参考**: bear ~$80（−45%，可存活非永久减值）。

## 6. Kill Criteria（见 monitor.md）
K1 营收实质 miss $91B 指引 / K2 DC 环比降或 GM 急压 / K3 大规模 CSP 迁出致份额结构性下滑（唯一可升 veto）/ K4 库存承诺大额减值 / K5 价格隐含 IRR<8%（>~$200）/ K6 Huang key-man。

## 7. runner_dissent
见 decision_card.json runner_dissent 字段。要点: 现价 $145 贴 52 周低、距高点 −38%，可能是市场提前嗅到 AI capex pull-forward 拐点；单看 Q2 $91B 指引无法证伪部分需求是周期高点抢装。但框架基于客观事实（forward 19x 已隐含减速、owner earnings 干净、资产负债表死不了、bear 可存活）给 STARTER 而非 WATCH——这是 exceptional_bottleneck + 估值友好的情形，价格不是卡点，故不重复 GOOGL 的价格封顶逻辑。

## 8. 状态
**DECISION_DRAFT**（非 COMPLETE）。OPEN: 10-K 逐行(O1)、10 年序列(O2)、proxy(O3)、custom-silicon 份额(O4)、China 损失量级(O5)、供应承诺(O6)。
