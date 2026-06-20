# AMZN Step 0 Plan — Mega7 活体批次

最后更新: 2026-06-19 · as_of=2026-06-19 · pipeline_version=lean-6module-v1

## Decision question (scope frozen)

Amazon.com, Inc.（NASDAQ: AMZN，单一普通股，one-share-one-vote）是否是一门**十年后仍值得拥有**的高质量生意？以 2026-06-19 价格（$244.39 收盘，市值 ~$2.66T）买入，是否有足够安全边际？AWS 重新加速 + 零售利润率创纪录 vs **~$200B/年 AI capex 把自由现金流压到近零（TTM FCF $1.2B）+ 长债激增至 $119B**——这场 AI 基建豪赌会如何改变 owner earnings 与耐久性？

- Ticker / class: AMZN, 单一普通股（2022-05 完成 20:1 拆股，本研究用拆股后口径）
- Decision purpose: 新钱建仓 verdict + 仓位 + 监控；不替用户执行
- Horizon: 10 年所有权视角
- as_of freeze edge: 2026-06-19（活体，无未来泄漏）

## 历史盲测先验（amzn_2023-02-03，仅作 thesis 对照，事实全部重取）
- 2023-02-03 的盲测案问题: "零售成本结构 + AWS 增长是周期性低谷的优质赢家，还是结构性受损的零售 + 减速的 AWS？" thesis = cyclical_inflection（零售利润率触底 + AWS 耐久 + 成本纪律）。
- **当前（2026-06-19）该 thesis 已大幅兑现**: 零售利润率从 2022 谷底回升到 Q1 2026 创纪录 13.1% 总营业利润率、NA 段 OI +43% Y/Y；AWS 在 2025 减速后于 Q1 2026 重新加速到 +28%（15 季最快）。**但 2023 的"成本纪律"故事，到 2026 已被一个全新的"$200B AI capex 豪赌"叙事取代**——研究主轴随之从"零售利润率触底"转为"AI capex 能否赚回资本成本 + owner earnings 在重投资期如何看"。

## 1 thesis gate（单一决策门）

**AMZN 是否仍是横跨电商物流 + 云计算（AWS）+ 广告的多引擎复利机器——其利润池足够耐久、当前价格相对 owner earnings 留有安全边际——即便它正把全部自由现金流（并加杠杆）投入一场 ~$200B/年 的 AI capex 豪赌？**

- 通过条件：①各引擎（NA 零售/International/AWS/广告）增长与利润是真实、一手披露的（非故事）；②利润池被规模/网络/转换成本护城河捕获且有耐久迹象；③资产负债表能存活下行（即便 capex 激增 + 加杠杆）；④价格相对 owner earnings 三情景留有 ≥8% IRR 的边际或被结构化建仓规则覆盖。
- 否决条件（硬 veto，仅 M5）：thesis 耐久性结构性破裂（AWS 份额结构性流失 / 零售利润池被永久侵蚀）**或**资产负债表无法存活（capex + 债务把公司逼到流动性危机）。**前瞻不确定性（$200B capex 的 ROI、AWS run-rate 可持续性）= haircut，不是 veto**（修好的老病：别因重投资期 FCF 难看就 over-veto 真复利机器）。

## 证据块（Evidence Blocks）

| Block | 内容 | 主来源 | 状态 |
|---|---|---|---|
| A 身份/filings | CIK 1018724、单一普通股、最新 10-K(FY25, ended 2025-12-31)、最新季报 Q1 2026(ended 2026-03-31) | SEC EDGAR | done |
| B 锚定季度 | Q1 2026 8-K Ex99.1（rev/三段/OI/EPS/OCF/FCF/capex/guide/Anthropic 收益） | SEC 8-K (A1) | done |
| C 全年基线 | FY25 8-K Ex99.1（rev $716.9B / OI $80.0B / 净利 $77.7B / AWS $128.7B / FCF $11.2B / capex $131.8B） | SEC 8-K (A1) | done |
| D 10 年序列 | FY16–FY25 rev/OI/AWS/FCF/股本 | 二手聚合 (B2) + 官方 PR 校验 | partial（早期年份未逐年取一手，降权） |
| E 利润池/护城河 | 三段细分、AWS backlog $364B、广告、CUDA-外 Trainium、bottleneck | Q1 PR (A1) + 电话会 (A2) + 行业 (B2) | partial（电话会 transcript 未逐行重取） |
| F Operator | Andy Jassy CEO + Bezos 执行主席 + 董事会 + 治理 + 激励 | DEF 14A (A1) + 历史 (B1) | partial（proxy 未重取，用先验+一般立场） |
| G 反演/陷阱 | $200B capex ROI、AWS 减速复发、加杠杆、Anthropic 收益失真、估值 | 多源 | done |
| H 估值 | owner earnings 桥（重投资期 capex 拆维护 vs 增长）+ 三情景 + 隐含预期 | 派生模型 (E1，明标 scenario) | done |

## Stop 条件（何时停止研究、交卡）

- 锚定季度（Q1 2026）+ 全年基线（FY25）的载荷性数字全部回挂 A1/A2 → 已满足，可交 DECISION_DRAFT。
- 10 年精确序列、proxy 细节、capex ROI / AWS backlog 转化的定量证据未达 A 级 → 标 OPEN，封顶完整度，不阻断交卡。
- 一遍现实目标 = DECISION_DRAFT（≈65%），非 COMPLETE。

## Sources opened（见 source_register.md 完整版）

- AMZN Q1 2026 8-K Ex99.1: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000012/amzn-20260331xex991.htm
- AMZN Q4/FY2025 8-K Ex99.1: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm
- AMZN 2025 Annual Report (10-K) PDF: https://s2.q4cdn.com/299287126/files/doc_financials/2026/ar/Amazon-2025-Annual-Report.pdf
- Yahoo chart API AMZN (price): https://query1.finance.yahoo.com/v8/finance/chart/AMZN
