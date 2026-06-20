# TSLA Step 0 Plan — Mega7 活体批次

最后更新: 2026-06-19 · as_of=2026-06-19 · pipeline_version=lean-6module-v1

## Decision question (scope frozen)

Tesla, Inc.（NASDAQ: TSLA，单一普通股，one-share-one-vote）是否是一门**十年后仍值得拥有**的高质量生意？以 2026-06-19 价格（~$400.49 收盘，市值 ~$1.41T）买入，是否有足够安全边际？在**核心汽车生意收缩 + 利润率压缩**、能源存储高增、robotaxi/Optimus/AI optionality 尚未兑现、Musk ~$1T 薪酬包巨额稀释悬顶的情况下，DELIVERED owner earnings 能否支撑当前极端倍数？

- Ticker / class: TSLA, 单一普通股
- Decision purpose: 新钱建仓 verdict + 仓位 + 监控；不替用户执行
- Horizon: 10 年所有权视角
- as_of freeze edge: 2026-06-19（活体，无未来泄漏）
- **冷启动**: TSLA 从未跑过此 pipeline，无历史盲测案，无先验 thesis。

## 1 thesis gate（单一决策门）

**Tesla 是否是一门十年后更强、利润池耐久、且当前价格留有安全边际的好生意——即：DELIVERED 基本面（汽车 + 能源 + 已上线 robotaxi/FSD）能否支撑 $1.41T 市值，而不必依赖尚未兑现的 NARRATIVE（Optimus/全无人 robotaxi/AI 终局）？**

- 通过条件：①DELIVERED 利润池（不含未兑现期权）相对市值留有 ≥8% IRR 边际，或被结构化建仓规则覆盖；②利润池有耐久迹象（汽车份额/利润率企稳 或 能源/AI 已成真利润腿）；③资产负债表能存活；④operator/治理不构成结构性减值风险。
- 否决条件（硬 veto，仅 M5）：thesis 耐久性结构性破裂（核心汽车永久性份额/利润坍塌且无替代利润池）**或**资产负债表无法存活。**注意**: 前瞻不确定性（robotaxi/Optimus 能否兑现）= haircut/不计入，**不是 veto**；但**极端估值 + 故事驱动**会通过"价格无安全边际"封顶 verdict（GOOGL 式价格封顶），不是 veto 而是 ceiling。

## 证据块（Evidence Blocks）

| Block | 内容 | 主来源 | 状态 |
|---|---|---|---|
| A 身份/filings | CIK 1318605、单一普通股、最新 10-Q Q1 2026、10-K FY2025 | SEC EDGAR | done（SEC 直取 403，逐行 OPEN）|
| B 锚定季度 | Q1 2026（rev/GM/op/NI/FCF/交付/库存/积分）| B1 交叉 + B2 | done（多源一致）|
| C 全年基线 | FY2025（rev −2.9%/op margin 4.6%/NI −46%/FCF/capex/交付 −9%/储能 46.7GWh）| B2 + 官方运营 A2 | done |
| D 10 年序列 | FY21–FY25 营收/利润率/净利/FCF | B2 | done（利润率压缩趋势清晰）|
| E 利润池/护城河 | 品牌/超充网络/能源/FSD 数据 vs 传统车企+中国 EV 竞争 | 行业 B1/B2 | partial |
| F Operator | Musk key-man、$1T 薪酬包 423.7M 股稀释、治理 | B1 + filing 登记 | partial（proxy OPEN）|
| G 反演/陷阱 | 汽车需求/利润率塌、估值无 MOS、Musk key-man、稀释、narrative 落空 | 多源 | done |
| H 估值 | DELIVERED owner earnings 桥 + 三情景（narrative 严格区隔）| 派生模型 E1 | done |

## Stop 条件（何时停止研究、交卡）

- 锚定季度（Q1 2026）+ 全年基线（FY2025）的载荷性数字多源交叉一致 → 满足 DECISION_DRAFT。
- SEC 逐行（分部利润）、robotaxi/Optimus 单位经济、proxy 细节未达 A 级 → 标 OPEN，封顶完整度，不阻断交卡。
- 一遍现实目标 = DECISION_DRAFT（≈55–60%，本案因 SEC 403 + optionality 不可量化，完整度低于 NVDA），非 COMPLETE。

## Sources opened（见 source_register.md 完整版）

- 价格: https://query2.finance.yahoo.com/v8/finance/chart/TSLA （close $400.49 @ 2026-06-18）
- Q1 2026: CNBC/Electrek/Teslarati（B1 交叉）+ stockanalysis（B2）
- FY2025 运营: Tesla 官方 X 交付报告（A2）
- Operator: TechCrunch/Fortune $1T 薪酬包（B1）+ SEC PX14A6G（filing 登记）
- SEC 10-Q/10-K/proxy: 已登记 URL，WebFetch 403 → 逐行 OPEN
