# AAPL Step 0 Plan — Mega7 活体批次

最后更新: 2026-06-19 · as_of=2026-06-19 · pipeline_version=lean-6module-v1

## Decision question (scope frozen)

Apple Inc.（NASDAQ: AAPL，单一普通股，one-share-one-vote）是否是一门**十年后仍值得拥有**的高质量生意？以 2026-06-19 价格（$298.01 收盘，市值 ~$4.37T）买入，是否有足够安全边际？iPhone 17 超级周期、Services 复利、Greater China、AI（Apple Intelligence）落地节奏、~40x P/E 的高估值起点，会如何改变 owner earnings 与新钱的预期回报？

- Ticker / class: AAPL, 单一普通股, one-share-one-vote。
- Decision purpose: 新钱建仓 verdict + 仓位 + 监控；不替用户执行。
- Horizon: 10 年所有权视角。
- as_of freeze edge: 2026-06-19（活体，无未来泄漏）。

## 历史盲测先验（仅作 thesis 对照，事实全部重取）
- `backtests/.../aapl_2016-05-12`: 当年 as_of $90.34 / ~10x trailing / ~6.7x EV-earnings / 净现金 ~$153B（占市值 ~31%），verdict=STARTER。实际 +1318% 总回报（never underwater），被评为 **SEVERE UNDERSIZE**（4–11% ceiling 封住了 methodology 自己的 Core 范本）。
- **教训**: 不要因"成熟/增长见顶"叙事给一门真正耐久的复利机器封过低的耐久性天花板。
- **但 2016 ≠ 2026**: 2016 是 ~10x + 净现金占市值 31% 的世代级入场；2026 是 ~40x trailing P/E + 净现金仅占市值 ~1.4%。耐久性先验沿用，**价格起点完全不同**——本案必须独立判断价格是否封顶。

## 1 thesis gate（单一决策门）

**AAPL 是否仍是一门以 1B+(20 亿+)装机量为护城河、Services 年金复利、品牌/生态锁定的耐久优质生意——且当前 ~$298 / ~40x trailing P/E / ~2.3% owner-earnings yield 的价格，对新钱是否留有 ≥8% 5y IRR 的安全边际，或被结构化建仓规则覆盖？**

- 通过条件：①生意耐久性真实（装机量年金 + Services + 品牌锁定，多年一手坐实）；②利润池被生态护城河捕获且有耐久迹象；③资产负债表能存活下行；④价格相对 owner earnings 三情景留有 ≥8% IRR 边际**或**被结构化建仓规则覆盖。
- 否决条件（硬 veto，仅 M5）：thesis 耐久性结构性破裂（生态/装机量年金崩坏）**或**资产负债表无法存活。前瞻不确定性（iPhone 周期/China/AI 落后）= haircut 不是 veto。**价格过高 = 把 verdict 封到 WATCH（M6 价格门），不是 M5 硬 veto。**

## 证据块（Evidence Blocks）

| Block | 内容 | 主来源 | 状态 |
|---|---|---|---|
| A 身份/filings | CIK 320193、单一普通股、最新 10-K(FY25, ended 2025-09-27)、最新季报 Q2 FY26(ended 2026-03-28) | SEC EDGAR | done |
| B 锚定季度 | Q2 FY26 8-K PR（rev $111.2B/+17%、iPhone/Services 拆分、GM、EPS $2.01、OCF、回购+股息、$100B 新授权） | SEC 8-K (A1) | done |
| C 全年基线 | FY25 10-K/Q4 PR（rev $416.2B / 净利 $112.0B / GM 46.9% / capex $12.7B / FCF ~$98.8B / 回购 $90.7B） | SEC 8-K + 10-K (A1) | partial（10-K 全文未逐行摘）|
| D 10 年序列 | FY16–FY25 rev/净利/GM/FCF/股本 | FY24/FY25 官方 (A1) + 早期年份二手 (B2) | partial（FY16–FY23 二手，降权）|
| E 利润池/护城河 | 装机量 2B+ 年金、Services GM ~75%、生态锁定、segment 拆分 | 8-K (A1) + 公司历史 (B1) | partial |
| F Operator | Tim Cook + Luca→Kevan Parekh CFO + 董事会 + 治理 + 激励 | DEF 14A (A1) + 历史 (B1) | partial（proxy 未重取，用先验+一般立场）|
| G 反演/陷阱 | iPhone 周期、China、AI 落后、监管(App Store/Google TAC)、估值过高 | 多源 | done |
| H 估值 | owner earnings 桥 + 三情景 + 隐含预期 | 派生模型 (E1，明标 scenario) | done |

## Stop 条件（何时停止研究、交卡）

- 锚定季度（Q2 FY26）+ 全年基线（FY25/FY24）的载荷性数字全部回挂 A1 → 已满足，可交 DECISION_DRAFT。
- 早期 10 年序列、proxy 细节、Apple Intelligence 落地定量、监管裁决量级未达 A 级 → 标 OPEN，封顶完整度，不阻断交卡。
- 一遍现实目标 = DECISION_DRAFT（≈60%），非 COMPLETE。

## Sources opened（见 source_register.md 完整版）
- AAPL Q2 FY26 8-K PR (ended 2026-03-28): https://www.sec.gov/Archives/edgar/data/320193/000032019326000011/a8-kex991q2202603282026.htm
- AAPL Q4/FY25 8-K PR (ended 2025-09-27): https://www.sec.gov/Archives/edgar/data/320193/000032019325000077/a8-kex991q4202509272025.htm
- AAPL FY25 10-K (ended 2025-09-27): https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm
- AAPL Q2 FY26 10-Q (ended 2026-03-28): https://www.sec.gov/Archives/edgar/data/320193/000032019326000013/aapl-20260328.htm
- Yahoo chart API AAPL (price): https://query1.finance.yahoo.com/v8/finance/chart/AAPL
