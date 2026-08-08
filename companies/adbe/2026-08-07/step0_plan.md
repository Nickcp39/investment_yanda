# ADBE Step 0 Plan — as_of 2026-08-07

**Trigger**：批次论点「**当一只股票因为『AI 杀死它』的叙事跌了 61.5%，崩的是倍数还是生意？**」需要一个最干净的公开样本来定案。Adobe 被选中。
**Type**：NEW dossier（`companies/adbe/` 此前无档案）。
**Pipeline**：`lean-6module-v1.1` · weights `none` · run_date 2026-08-07。

---

## 要回答的问题（冻结在动手之前）

- **(a)** 把 −61.5% 拆成「倍数压缩」与「盈利/FCF 基数变化」两部分，**把算术摆出来**。峰值 vs 现在的收入、EPS、FCF、ARR、P/E、EV/FCF 各是多少。
- **(b)** 生意本身在不在被侵蚀？分部收入增速、**ARR / 净新增 ARR 及其趋势**、NRR、席位数、定价动作。**净新增 ARR 是单一最可证伪的指标。**
- **(c)** AI 替代机制要**具体**：哪个产品被哪个替代品攻击、在哪一层。区分「图像/视频**生成**」（真替代）与「专业编辑工作流 / 文件格式 / 团队协作 / 合规 PDF / 资产管理」（结构性切换成本）。Adobe 的收入在这条界线两侧各占多少？
- **(d)** Firefly 与 Adobe 自身的 AI 变现：在捕获、在白送、还是都不是？**若不单独披露，非披露本身就是一条发现**（按本 lab 处理 Wiley AI 授权行的标准处理）。
- **(e)** 护城河测试，**用 BSX 那把尺**：哪些是结构性（挡住品类），哪些只是在位惯性？常设结论：**先发/在位若无结构性锁定，一旦资金充足的对手认真下场就会崩得很快**（Farapulse 美国 PFA 份额 100% → 41%，2.5 年）。

## 完成标准（先于结论写下）

- 每个数字带 source id + URL + 日期；**一手（SEC 10-K/10-Q/8-K、IR）优先于二手**；推算值单独标注。
- `as_of` 价格 = ≤ 今天的已结算收盘，**双源交叉并说明 delta**。
- 门槛 **8%**；三情景（bear/base/bull）显式给出 owner-earnings 起点、CAGR、退出倍数、IRR。
- 显式 `buy_below` + 价格阶梯（WATCH / STARTER / ADD / no-chase / bear 下行）。
- 裁决字段齐：`business_verdict` / `new_money_verdict` / `existing_position_verdict` / 初始与最大仓位 / `binding_constraint` / `completeness`。
- Kill criteria 三态（🟢/🟡/🔴）；诚实的 `runner_dissent`；`OPEN` 清单封顶 completeness。
- **不编造。** 拿不到出处的数字进 OPEN 并压 completeness。诚实的 60% 胜过编造的 90%。
- 机械门：`freshness.json` + `python scripts/verify_freshness.py` 必须 exit 0。

## 需要验证的锚点事实（≥2 源 + 一手）

峰值 $688.37（2021-11-19）· 现价 ~$265 · FY2021 与 FY2025/TTM 的收入/EPS/FCF/股本 · 各季 ARR 与净新增 ARR · FY2026 指引及其修订 · Firefly / AI ARR 的任何披露 · 分部与客户组口径。**[全部已验证 — 见 facts.md 与 raw/]**

## 载荷性重算

−61.40% 的三口径拆解（EPS / FCF-per-share / 市值-收入）与对数归因 · owner earnings 桥（FCF − SBC）· 三情景 5y/10y IRR · **现价隐含的 OE 增速反推** · buy-below 阶梯。

## 输出

`companies/adbe/2026-08-07/`，镜像 `companies/_company_research_template/` 的标准件，外加 `raw/arr_history.md`（本 run 最关键的数据集单独成文）。

---

## 执行中发生的偏离（诚实记录）

1. **本 run 分两段执行**：第一段在写完 `facts.md` + `raw/primary_extracts.md` 后因会话额度中断；第二段恢复后按「先把 ARR 数据集落盘」的顺序重启。
2. **禁止 sub-agent**：第二段全程单线程执行，不再 fan-out。
3. **Web search 预算耗尽（200/200）**：竞争对手一手财务（Canva / Figma / OpenAI / Google）**全部未取**，(c) 的替代机制只能定性、不能定量 → 列为 blocking **O8**，封顶 completeness。
4. **Adobe 的 investor datasheet PDF 抓取失败**（ECONNRESET），FY2023/FY2024 的 Total Adobe ARR 历史值未取 → 非 blocking **O9**。
5. **改用 SEC EDGAR 直连 + 合规 User-Agent**（默认 WebFetch UA 被 SEC 403），成功取得全部一手 8-K/10-K/10-Q 正文，逐条 verbatim 存入 `raw/primary_extracts.md`。**这反而使财务侧的证据等级高于原计划。**
