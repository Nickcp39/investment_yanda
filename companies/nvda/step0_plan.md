# NVDA Step 0 Plan — Mega7 活体批次

最后更新: 2026-06-19 · as_of=2026-06-19 · pipeline_version=lean-6module-v1

## Decision question (scope frozen)

NVIDIA Corp（NASDAQ: NVDA，单一普通股，one-share-one-vote）是否是一门**十年后仍值得拥有**的高质量生意？以 2026-06-19 价格（~$145.48 收盘，市值 ~$3.55T）买入，是否有足够安全边际？AI 数据中心建设周期、China 出口管制、custom-silicon/AMD 竞争、capex 是否 pull-forward，会如何改变 owner earnings 与耐久性？

- Ticker / class: NVDA, 单一普通股（10:1 拆股已于 2024-06 完成，本研究全部用拆股后口径）
- Decision purpose: 新钱建仓 verdict + 仓位 + 监控；不替用户执行
- Horizon: 10 年所有权视角（叠周期/bottleneck 检验）
- as_of freeze edge: 2026-06-19（活体，无未来泄漏）

## 1 thesis gate（单一决策门）

**NVDA 是否仍是 AI 加速计算的"全栈瓶颈"（GPU + CUDA + NVLink/InfiniBand 网络 + 先进封装/HBM 供应链）——即整个 AI 产业必须绕过的稀缺资源，并且这门生意的利润池足够耐久、当前价格留有安全边际？**

- 通过条件：①需求是真实、已被一手披露强制更新的（非故事）；②利润池被全栈护城河捕获且有耐久迹象；③资产负债表能存活下行；④价格相对 owner earnings 三情景留有 ≥8% IRR 的边际或被结构化建仓规则覆盖。
- 否决条件（硬 veto，仅 M5）：thesis 耐久性结构性破裂（CSP 大规模迁出 NVDA 到 custom silicon / AMD 致 DC 份额坍塌）**或**资产负债表无法存活。前瞻不确定性（pull-forward / China）= haircut，不是 veto。

## 证据块（Evidence Blocks）

| Block | 内容 | 主来源 | 状态 |
|---|---|---|---|
| A 身份/filings | CIK 1045810、单一普通股、最新 10-K(FY26, ended 2026-01-25)、最新季报 Q1 FY27(ended 2026-04-26) | SEC EDGAR | done |
| B 锚定季度 | Q1 FY27 8-K PR + CFO commentary（rev/DC/margin/EPS/OCF/FCF/guide/China） | SEC 8-K (A1) | done |
| C 全年基线 | FY26 10-K（rev $215.9B / 净利 $120.1B / GM 71.1% / capex $6.1B / 股东回报 $41.1B） | SEC 10-K + 官方 PR (A1/A2) | partial（10-K 全文未逐行摘） |
| D 10 年序列 | FY17–FY26 rev/净利/GM/FCF/股本 | 二手聚合 (B2) + 官方 PR 校验 | partial（早期年份口径有冲突，降权） |
| E 利润池/护城河 | DC 细分（Compute/Networking）、CUDA 锁定、份额、bottleneck | CFO commentary (A2) + 行业 (B2) | partial |
| F Operator | Jensen Huang 创始人 + 董事会 + 治理 + 激励 | DEF 14A (A1) + 历史 (B1) | partial（proxy 未重取，用先验+一般立场） |
| G 反演/陷阱 | pull-forward、China、custom silicon、key-man、估值 air-pocket | 多源 | done |
| H 估值 | owner earnings 桥 + 三情景 + 隐含预期 | 派生模型 (E1，明标 scenario) | done |

## Stop 条件（何时停止研究、交卡）

- 锚定季度（Q1 FY27）+ 全年基线（FY26）的载荷性数字全部回挂 A1/A2 → 已满足，可交 DECISION_DRAFT。
- 早期 10 年序列、proxy 细节、custom-silicon 份额定量未达 A 级 → 标 OPEN，封顶完整度，不阻断交卡。
- 一遍现实目标 = DECISION_DRAFT（≈65–70%），非 COMPLETE。

## Sources opened（见 source_register.md 完整版）

- NVDA Q1 FY27 8-K PR: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm
- NVDA Q1 FY27 CFO commentary: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm
- NVDA FY26 10-K (ended 2026-01-25): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- NVDA Q4/FY26 PR: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm
- NVDA 官方 newsroom Q1 FY27: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027
- Yahoo chart API NVDA (price): https://query1.finance.yahoo.com/v8/finance/chart/NVDA
