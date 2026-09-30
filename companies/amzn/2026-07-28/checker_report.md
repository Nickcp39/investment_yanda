# AMZN Checker Report — mega7_2026-07-28

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT（~62% 完整度）** ← 与 research_status.md / decision_card 自述一致；显式声明"不是 COMPLETE"，无越级措辞
verdict / size / ceiling: **新钱 WATCH · 存量 HOLD · size 0%/0% · ceiling = WATCH（价格封顶，先于 62% 完整度的 STARTER 封顶生效）** ← 是否被完整度正确封顶: **是**
数据新鲜度: **PASS（freshness_check.json，exit 0）** ← 且经 Checker 独立外部交叉验证价格（见下），非仅信 Runner 落盘

---

## Gate 勾选: A✓ / B~ / C~(carry) / D✓ / E✓ / F✓

- **A Scope**: ticker / share class（post-20:1）/ as_of=2026-07-28 / 决策问题（当前 regime 下 $230.86 对新钱是否有 MOS）/ 时间跨度全冻结；完成标准先于结论写下；状态标签 DECISION_DRAFT 不 stale。✓
- **B Evidence**: 本轮为**聚焦刷新**（换价 + 叠 regime + 重算 M4/M5/M6），非从零重研究。锚定季（Q1 2026 + FY25）沿用 6/19 已落盘的 SEC 8-K Ex99.1 [S001][S002]（6/19 checker 已逐项 grep 命中、零失配）。8 个来源带 id + 日期 + link/tier；KOL/社媒零进 EVIDENCE。**注**：本刷新文件夹未新建 source_register.md / claim_ledger.csv / facts.md / raw/（继承 6/19 基线），与"刷新非重研究"的 62% 诚实标签一致，未伪装成完整证据脊柱。~（carry，合规）
- **C 11-Stage 覆盖**: 六模块信号齐（M1–M6 均有 finding）；M2/M3 业务基线快速复核沿用 6/19（business_model / moat_map / operator_underwriting），M4/M5/M6 本轮重算。**Stage 8 IC Panel：本刷新未重跑，沿用 6/19 的五灵魂票**（decision_card 仅以"same five-soul panel put GOOGL at WATCH"作**结构性引用**，无逐字名言、无杜撰引语）。对 DECISION_DRAFT 刷新合规。~(carry)
- **D Model & Math**: owner-earnings 三情景按现价 $230.86 重算；净利 vs 正常化 OE **显式分开**（GAAP EPS 因 Anthropic 公允价值收益被弃用，改双口径 NOPAT $67B / 保守 OE $45–65B band）；implied IRR 从**当前价**反推；关键公式可审计（见独立重算）。owner-earnings 桥 O4 显式标 blocking、未假装算出点估。✓
- **E Open Questions**: O0 Q2-2026 未出（迫近二元催化）/ O4 capex 维护·增长拆分+ROIC（**显式 blocking，封顶 verdict**）/ O1 10-K / O3 proxy / O5 backlog / O6 Anthropic 会计 — 分类清楚，blocking 项封顶、其余 haircut 不封顶。✓
- **F Audit & Consistency**: 数字前后一致（见下逐项对账）；decision_card.json schema 完整且版本戳 = `lean-6module-v1` / weights `none` / run_date `2026-07-28`；research_status 报真实状态（DECISION_DRAFT）不报更好看的。✓

---

## 独立验证结果（非信任 Runner）

### 1. 价格完整性（INC-001 核心）— 通过，且经外部独立源确认
- **Checker 独立 WebFetch** 直连 Yahoo chart API（query2.finance.yahoo.com/v8/finance/chart/AMZN）：最新收盘 **$230.86**、52 周低 **$196.00**（与卡/manifest 完全一致）、最近 5 日收盘为下行序列 $244.85→$233.66→$232.11→$231.39→**$230.86**（与"自 6/19 −5.5%、未贴极值"叙述吻合）。**$230.86 是真实、可外部复现的 Yahoo 收盘价，绝非 52 周极值**（居 $196–$278.56 区间中上部）。
- 卡内三源（Yahoo / stockanalysis / statmuse）均报 $230.86、delta 0.0%；freshness_check.json 的独立 Yahoo 重抓 = `230.86000061035156`（float32 往返特征 = 真实 API 返回，非人工伪造）。**INC-001 失败模式（拿 52 周低当现价）在本卡不存在。**
- **距高 −16.0%**（$274.99 收盘基）/ **距低 +17.8%**（$196.00）— 我方手算复核一致。卡采用 $274.99（收盘基，较保守、更贴近现价）而 Yahoo meta / stockanalysis 报 $278.56（盘中极值），**两值均在 freshness.json 显式披露**，非隐匿；采保守值不影响"未贴极值"结论。

### 2. 数字重算（Checker 手算）— 全口径对账通过
- 市值：10,874M × $230.86 = **$2,510.4B ≈ $2.51T**（卡 2510000000000 ✓，0.01%）。
- P/E：230.86 / 7.17 = **32.2x**（卡"~32x" ✓）。
- 起始收益率：NOPAT 67/2510=**2.67%**、保守中值 55/2510=**2.19%**、低端 45/2510=**1.79%**（卡 2.2–2.7% ✓）。
- 三情景 5y IRR @$230.86：bear (118/230.86)^.2−1=**−12.6%**、base (226/230.86)^.2−1=**−0.4%**、bull (353/230.86)^.2−1=**+8.9%**（卡 −12.6/−0.4/+8.9 ✓，且 y5 每股 118/226/353 与 NOPAT×退出倍数/股数自洽）。
- Δ vs 6/19：6/19 卡确为价 $244.39 / mcap $2.657T / base −1.5% / bull +7.7% / bear −13.5% / buy-below $178（回读 6/19 decision_card.json 逐项命中）；gap 到 buy-below −27%→−23%（(178−244.39)/244.39 vs (178−230.86)/230.86 ✓）。**delta_vs_0619 全部叙述属实。**

### 3. Regime 是否真并入 M4/M5（非忽略）— 是
- M4 finding 显式并入 capex-审计年 + Q2-2026 print 时点（7/30）+ FOMC；M5 finding + inversion_map.md 逐条重估失败路径当下 salience（F1 capex-ROIC↑↑、F4 FOMC/Warsh↑），并给出 **AMZN 名字级细读**：半导体/存储暴跌对 AMZN 混合偏中性（内存买方 + 自研 Trainium 隔离，CXMT 更便宜 DRAM 降 capex 成本）。regime 来自 batch PLAN.md 的既定前提，Runner 如实叠加、未自造。✓

### 4. 伪造引语 / 失配数字排查
- **无杜撰逐字名言**：本刷新未重跑 IC Panel，decision_card 仅结构性引用五灵魂立场（"same panel put GOOGL at WATCH"），无带引号的伪造原话。
- **无失配数字**：grep 全文件夹，$244.39 / $2.66T 每次出现均**显式标注为 6/19 对照**；$230.86 为唯一真值现于所有价格文件；NVDA 坏价 $145.48 零出现。✓

### 5. verdict 上限
- 完整度 62% → 完整度 ceiling = STARTER（60–80 档）；价格无 MOS（base IRR −0.4%、起始收益率 ~2%）→ 价格封顶 WATCH，**取更严者 = WATCH，未超顶**。size 0%/0% 与"周期/未确认不得给开仓档"一致（AMZN 为重投资期、owner-earnings 桥未闭合、Q2 未出，明确不够 size）。✓

### 6. 状态标签诚实
- research_status.md 首行即"**诚实标签: DECISION_DRAFT（~62%）· 不是 COMPLETE**"；措辞与标签匹配，无"彻底跑完 / full research complete"越级。**加分项**：本卡主动**诚实修正 6/19** 的一处松表述（6/19 称 buy-below $175–180 = base IRR 回 8%；精算 base=8% 实需 ~$154，$175–180 对应 base ~+5%，故 $178 重定义为 MOS-emergence/STARTER 触发线）— 自纠而非掩盖。✓

---

## 数据新鲜度（强制机械门）
- **PASS**：freshness_check.json `status=="PASS"` / `exit_code=0`，六 tripwire 全过（T1 band 196≤230.86≤274.99 · T2 +17.8%/−16.0% 未贴极值 · T3 市值恒等 0.01% · T4 距高对账 gap 0.0pt · T5 单一真值 · T6 指引 13d 新鲜）。
- **freshness.json manifest 存在**：每个 LIVE 字段 ≥2 源 — price(3) / market_cap(2) / 52wk_high(2) / 52wk_low(2) / shares_out(2) / guidance(3)。✓
- **价格源合规**：走 Yahoo chart API + 3 独立源交叉（非单源只验日期）。✓
- **Checker 侧说明（透明）**：本 Checker 环境的本地 python 执行被 sandbox 拦截（Bash exit 49 / PowerShell 未寻得 python 9009），**未能亲自重跑 verify_freshness.py**；改以**独立 WebFetch 外部复现 Yahoo 价格 $230.86 + 52 周低 $196.00**达成等效独立核验（脚本的核心动作 = 独立重抓价 + 非极值探测，二者均由外部源确认）。committed PASS 产物存在且经外部佐证为真，机械门满足。

---

## FIX 清单
**无强制 FIX。** 可选改进（非封顶、不影响裁定）：
1) freshness.json 顶部 note 保守地写"dated-scenario run 里独立 Yahoo 重抓**可能**无法复现 $230.86"，但实际 freshness_check.json 的重抓**确已**复现（230.86000061035156）且 Checker 外部 WebFetch 亦得 $230.86 — note 的对冲措辞与实际 clean PASS 略不一致，纯文案，建议改为"重抓已复现"。（freshness.json:5）
2) O4（$200B capex 维护/增长拆分 + ROIC）+ O0（Q2-2026 7/30 print）是解 WATCH 封顶的胜负手；7/30 财报后应即刷新 M4 并重评升/降档 — 已在 research_status/monitor 记录，仅作进度提醒。

## 伪造引语 / 失配数字
**无。** 无杜撰逐字名言（本刷新未重跑 IC Panel，仅结构性引用）；as_of_price / market_cap / P/E / 起始收益率 / 三情景 IRR / 52 周位置 / Δ-vs-6/19 在 decision_card(.json+.md) / valuation.md / inversion_map.md / delta_vs_0619.md / freshness*.json 间**完全一致**，且经手算重演 + 外部 Yahoo WebFetch 双重核对通过。

## 一句话
**这家这轮可信度高 — CLEAN**：现价 $230.86 经 Checker 独立外部源（Yahoo chart API）确认为真实、可复现、非 52 周极值（INC-001 防护实测通过），全部衍生数（市值/P-E/收益率/三情景 IRR/Δ-vs-6/19）手算零失配，状态标签诚实（DECISION_DRAFT 而非 COMPLETE 且主动自纠 6/19 松表述），verdict=WATCH 被价格正确封顶（先于 62% 完整度的 STARTER 封顶生效，与 GOOGL 同构），regime 如实叠入 M4/M5、无杜撰引语；唯一实质开口是 owner-earnings 桥因 $200B capex 拆分缺一手（O4）+ Q2-2026 财报 2 天后（7/30）才出、本卡诚实锁定于 print 前 — 两者均被显式披露为封顶/迫近催化，非掩盖。
