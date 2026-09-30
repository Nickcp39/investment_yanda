# AAPL Research Status — as_of 2026-07-28

最后更新：2026-07-28（mega7_2026-07-28 焦点重估）· pipeline_version=lean-6module-v1 · weights_version=none

**诚实标签：DECISION_DRAFT（决策草案，~55% 完整度）——不是 COMPLETE。**

这是对 6/19 基线 dossier（`companies/aapl/2026-06-19/`）的**焦点刷新**，不是从零重研究：
- M2 主题 / M3 护城河·operator = **carry 自 6/19**（6 周内业务未破，仅快速复核）；
- 用今日价 **$340.08** 重算 **M4/M5/M6**；
- 叠加 2026-07-28 regime（半导体暴跌 / 轮动 / AI-capex 审计 / CXMT / FOMC-Warsh）。

Decision question：$340.08（破 $5T、反超 NVDA 的轮动高点）对新钱是否有安全边际？6 周内价格 +14% + 继任落定 + capex 审计年如何改变 owner-earnings 回报与两轴 verdict？

---

## Final Verdict 摘要
**新钱 WATCH（0%，更硬）/ 存量 HOLD（偏减）· business exceptional（未变）· 价格是更 binding 的约束。**

- AAPL 仍是 20 亿+ 装机量年金 + Services 复利的 exceptional 耐久生意（载荷数 carry 自 6/19 一手：Q2 FY26 营收 $111.2B/+17%、Services $31.0B/+16.3%、China 季 +28%、GM 49.3%；FY25 营收 $416.2B、净利 $112.0B、净现金 $61.9B）。
- **价格 $298.01 → $340.08（+14.1%）**，市值 ~$4.39T → ~$5.008T（7/28 盘中破 $5T，史上第 2 家，反超 NVDA）。轮动/避险驱动，**非财报驱动**。
- 41.7x trailing OE / 2.40% yield / **base 5y IRR ~0%（« 8% 门槛）** / 现价 +47% 高于 $231 buy-below → **价格封 WATCH，且比 6/19 更 binding**。M6 −1 → −2。
- **无硬 veto**（无结构破裂 / 无资产负债表风险）。regime 里砸同业的风险大多不落苹果（capex-light、存储买方）。
- **M4：窗口内无苹果新财报**；6 月季（fiscal Q3 FY26）2026-07-30 才发（Cook 末次电话会）。锚定季度不变。
- **M3/operator：6/19 O3（继任）已解决**——Cook 转执行董事长、Ternus 2026-09-01 任 CEO（有序内部交棒；6/19 基线漏采的 2026-04-20 公告）。

---

## Stage Checklist（焦点刷新范围）
| Stage | Artifact | Status |
|---|---|---|
| 0 Idea Intake | ../../_mega7_2026-07-28/PLAN.md | ✅ |
| M1 Evidence（价格重锚 + 载荷数 carry）| decision_card + freshness.json | ✅（价格 3 源 0.0% delta）|
| M2 Business（carry）| ../2026-06-19/business_model.md（快速复核，未破）| ✅ carry |
| M3 Moat/Operator（carry + O3 更新）| ../2026-06-19/moat_map.md + 本卡 M3（Ternus 继任）| ✅ carry + 更新 |
| M4 Financial（重算 + 无新财报）| valuation.md + ../2026-06-19/financials/ | ✅（7/30 印证 pending, O7）|
| M5 Inversion（叠 regime）| inversion_map.md | ✅ |
| M6 Valuation（@ $340.08）| valuation.md | ✅ |
| Delta | delta_vs_0619.md | ✅ |
| 锁定卡 | decision_card.json + .md（版本戳）| ✅ |
| 数据新鲜度 | freshness.json + verify_freshness.py | ⚠️ 见下 |

---

## 数据新鲜度（强制机械门）
- `freshness.json` 已提交：price/market_cap/52wk 每 LIVE 字段 ≥2 独立源。
- 价格 $340.08：Yahoo regularMarketPrice + stockanalysis.com（$340.08 / P/E 41.23）+ CNBC/Bloomberg/Forbes（$5T 事件、盘中高 342.89）+ PLAN.md 表 → 4 源，pairwise 0.0% delta。
- **52 周高-hug 属 justified**：现价 −0.8% 于盘中高 342.89、= 收盘高、+68.8% 于 52wk 低 201.50；实价来自 regularMarketPrice（**非** INC-001 式由 52 周极值反推——那是把 52wk **低**当现价的下行错，本案是被独立多源+ $5T 新闻坐实的真实高点）。
- `verify_freshness.py` 运行结果见下节（若 PASS 附 freshness_check.json；若未能运行标 "freshness_check pending"）。

## 升 verdict / 解封顶路径
①价格回撤 ≤ ~$231（base IRR ≥8%）→ STARTER；②≤ ~$210 → 加向 8–15%；③完整度补齐（O1 TAC、10-K、7/30 印证、Ternus 资本配置）到 >80% 仅解完整度封顶——**价格门仍独立 binding**，只有价格回撤解锁新钱。

## Next Review
**2026-07-30 fiscal Q3 FY26 财报（Cook 末次电话会）**：iPhone 趋势、Services 增速、Greater China、GM、guidance。**FOMC 周三 / Warsh 记者会**：利率与倍数风险。**2026-09-01 Ternus 上任**：资本配置纪律（回购节奏）。价格触发：≤$231 开 STARTER。

## OPEN（封顶完整度；价格门更严）
O1 Google TAC 量级 · O2 10-K 逐行 · O4 AI 入口变现定量 · O5 早期 10 年序列(B2) · O6 关税/供应链 · **O7(新) 2026-07-30 fiscal Q3 印证** · **O8(新) Ternus 资本配置延续性**。（**O3 继任已关闭**。）
