# ADBE Research Status — as_of 2026-08-07

**Type**: NEW dossier（`companies/adbe/` 此前无档案）
**Pipeline**: `lean-6module-v1.1` · weights `none` · run_date 2026-08-07
**状态标签**: **DECISION_DRAFT** ——**不是 COMPLETE**
**Completeness**: **~68%** → 按 Stage I 的 verdict ceiling 规则（60–80% → STARTER 上限），本卡取 **STARTER**，**未越顶**

---

## Verdict

| 字段 | 值 |
|---|---|
| business_verdict | **good** |
| new_money_verdict | **STARTER** |
| existing_position_verdict | **HOLD_TO_ADD** |
| 初始 / 最大仓位 | **3% / 6%** |
| **buy_below** | **~$306**（base 12% IRR 锚；现价 $265.74 已在其下 13.2%） |
| **binding_constraint** | **COMPLETENESS / 可验证性**——**不是价格** |
| 数据新鲜度机械门 | **PASS**（`freshness_check.json`，exit 0；T1–T6 全过，T6 guidance 一条 WARN 已说明） |

---

## 模块状态

| Module | 文件 | Signal | 状态 |
|---|---|:--:|---|
| M1 Evidence Spine | `facts.md`、`claim_ledger.csv`（118 条）、`raw/primary_extracts.md`、`raw/arr_history.md` | **+1** | ✅ 财务侧全一手（15 条 A1 SEC 直连）；**竞争侧为空** |
| M2 Theme / Mechanism | `business_model.md`、`value_chain_map.md` | **+1** | ✅ 收入分层已推算；生成 vs 工作流的界线**公司不披露** |
| M3 Profit Pool / Durability | `moat_map.md`、`bottleneck_map.md`、`operator_underwriting.md` | **0** | ✅ 诚实的零：双层护城河，方向相反，加权不可计算 |
| M4 Financial Reality | `financials/financial_quality.md` | **+2** | ✅ 本卡最强模块 |
| M5 Inversion / Trap | `inversion_map.md` | **−1** | ✅ 实现的风险是 F5 披露退化 × F6 领导层真空，**不是 AI 路径** |
| M6 Price / Position | `valuation.md`、`model/scenario_model.csv` | **+2** | ✅ base 10y IRR +14.15%；隐含预期 = OE 十年横盘 |
| Decision | `decision_card.md`、`decision_card.json` | — | ✅ 版本戳齐（`lean-6module-v1.1` / `none` / `2026-08-07`） |
| IC Panel | `ic_panel.md` | — | ✅ 五灵魂，非一致（3 STARTER / 2 WATCH） |
| Freshness | `freshness.json`、`freshness_check.json`、`freshness_check.txt` | — | ✅ **PASS** |

**Signal vector: +1 / +1 / 0 / +2 / −1 / +2 = 净 +5**

---

## 本轮确立了什么

1. **(a) 的算术已定案，零残差。** −61.40% = 盈利 +74.5% × 倍数 −77.87%（1.7445 × 0.22128 = 0.38602）。对数归因：**倍数贡献 158.5%，盈利贡献 −58.5%（抵消项）**。三个口径（EPS / FCF-per-share / 市值-收入）互相校验一致。**崩的是倍数，不是生意。**
2. **(b) 的净新增 ARR 完整序列已落盘**（`raw/arr_history.md`）：FY23 $1.91B → FY24 $2.00B → FY25 ~$1.98B，**美元额三年持平**；增速 12.6% → 11.5% → 指引 10.2%（含 ~1.9pp 外延）→ **有机 ~8.3%**。**是滑坡，不是断崖。**
3. **发现了一条本 lab 此前没遇到过的模式**：Adobe **分两次撤掉了能证伪本论点的指标**（FY2025 撤净新增 ARR，FY2026 撤 Digital Media ARR + 三分部合一），时点与 ARR 增速下滑完全重合。**与 BSX 的对照是决定性的：BSX 是「护城河被证伪」，Adobe 是「护城河被设计成不可证伪」。**
4. **领导层双悬空**：CEO 悬空 5 个月（继任者未定）、CFO 临时 2 个月。这直接把初始仓位从赔率该给的 5–6% 压到 3%。
5. **价格已经在重估**：ADBE **不在 52 周低点附近**——2026-06-25 见底 $193.41 后已反弹 **+37.4%**。「−61.5%」是相对 2021 峰值的说法，不要读成「抄在地板上」。
6. **(d) 的答案**：Adobe **既不是纯捕获也不是纯白送**——AI-first ARR $500M（占 ARR 1.8%，窄口径、诚实小规模披露）+ **"Total AI-Influenced ARR" 有定义无数字**（宽口径，构造上可在零增量变现下逼近 100% ARR）。**它在用 AI 保住既有档位的定价权。**

---

## 阻塞项（封顶 completeness 的 5 条）

| # | 内容 | 为什么阻塞 |
|---|---|---|
| **O1** | 净新增 ARR 已被撤下，Digital Media 口径无法重建 | 论证 (b) 的最锋利指标不存在了 |
| **O2** | Firefly 独立收入无一手确认 | (d) 只能部分回答 |
| **O3** | **10-K purchase obligations（AI 算力承诺）未提取** | owner earnings 桥的最大单一未知项——可能推翻「capex 只占 0.80%」这个核心安慰 |
| **O7** | CEO 继任者未定 + CFO 临时 | 直接压 operator 评分与仓位 |
| **O8** | **竞争对手一手财务全部缺失**（web search 预算 200/200 耗尽） | (c) 的替代机制只能定性 |

**monitoring（4 条）**：O4 无 NRR/席位数 · O5 AI-Influenced ARR 有定义无数字 · O6 G&A +44.8% 未解释 · O10 电话会逐字稿未取
**non-blocking（1 条）**：O9 FY2023/24 Total ARR 历史值（datasheet PDF 抓取失败）

---

## 下一轮触发条件（按优先级）

1. **Q3 FY2026 财报（季度约 2026-08-28 结束，往年 9 月中旬发布）** —— 本 dossier 之后最近的一个硬事件。要看三样：**有机 ARR 增速是否守住 ~8%（K-A 缓冲仅 ~1.3pp）**、收入增速是否继续加速、是否有任何披露口径的**第三次**退化（K-E）。
2. **CEO 继任者公布** —— 内部人 vs 外部人、产品型 vs 财务型，决定 operator 分数与 K-D。**这是加仓的第一触发条件，不是价格。**
3. **10-K purchase obligations 提取（O3）** —— 下一轮必须先关掉这一条，它是 OE 桥唯一可能被推翻的输入。
4. **竞争对手一手财务（O8）** —— 有 web search 预算时的第一优先级；Canva / Figma 的收入规模与增速会直接决定 M3 能否从 0 走向 ±1。
5. **任何分层 ARR / 席位披露的恢复** —— **单一价值最高的事件**：会直接解除本 dossier 的 binding_constraint。
6. 价格进入 **$193–252** 且论点未破 → 加仓至 6%；价格升过 **$352** 且基本面无升级 → 不追（K-G）。

---

## 措辞纪律声明

本 dossier **未完成**。它跑到了 **DECISION_DRAFT**，被 5 条 blocking OPEN 封顶在 **~68%**。
财务侧（M4/M6）的证据强度接近 A 级；**护城河侧（M3）与竞争侧的证据强度是 D/F 级**。任何把本卡读成「Adobe 已研究透彻」的说法都是错的——正确的读法是：**「(a) 的算术已经定案；(b) 的趋势已经定案；(c)/(e) 只做到了结构性推理；(d) 部分回答。」**
