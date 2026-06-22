# NBIS Audit (Stage 7 · 质量门)

最后更新: 2026-06-18 · 审计本轮 10-layer dossier 的完整度、内部一致性、verdict 封顶（packaged 2026-06-21 under lean-6module-v1.1）

## 1. 完整度评估

| 维度 | 状态 | 说明 |
|---|---|---|
| 一手证据底座 | 强 | FY2025 20-F(CIK 0001513845)+ Q1'26 6-K 股东信 + MSFT 合同 6-K;51 条 claim 入 ledger,载荷性数字基本回挂 A1/A2 |
| 财务模型 | 中 | 历史 anchor(FY24/FY25/Q1'26)挂证据;owner-earnings DCF **不可用**(FCF 负至 ≥2028)→ EV/forward-sales 三情景 + implied-expectations 反推;算术勾稽 |
| 8/10 分析模块 | 齐全 | business/value_chain/moat/bottleneck/operator/inversion/financial_quality/valuation 全部存在;Stage 8 IC Panel 五灵魂(段永平主审)已出 |
| 缺口 | 见下 | active MW(O-A,公司 withhold)、集中度精确 %(O-B)、FY26 capex actual(O-C)、Russia indemnity(O-D)未一手化 |

**完整度估计:~70%**(10 层首跑 + 6 子代理 ~547k tokens;比 MSFT cold-start ~65% 略高,因合同/财务/电力一手覆盖更深;但 active MW 缺口是硬伤)。

## 2. 硬规则封顶检查
- "缺模块封顶":8 模块 + IC Panel 齐全 → **不触发**。
- "来源不足封顶 INFO-GAP/WATCH":载荷性数字回挂 A1/A2,但存在重大信息缺口,其中 **active MW(O-A)直接影响"建设-通电"转化论点的可验证性**。
- **verdict 上限 = 价格 + 完整度,取更紧者**:
  - **价格(主)**:$286.69 EV ≈ 2.2× 全部 RPO ≈ 8–10× YE26 exit-ARR(当作已兑现),**无安全边际、bear −50%+** → 新钱 ceiling = **WATCH**(铁律:无 MOS 不可 STARTER+)。
  - **完整度(次)**:~70% 落在 INFO-GAP 区,active MW 缺口独立把转化论点封在"未证明"。
  - → **新钱 WATCH;存量 HOLD**(生意被一手验证更好,但不因更便宜——价格反而在 ATH)。

## 3. ceiling 来源(与 MSFT 案的关键不同)
- MSFT 案:ceiling=STARTER,来源是**完整度(~65%)+ 信息缺口**,**不是**价格(估值端有正安全边际,公允价 $436 > 现价 $379)。
- **NBIS 案:ceiling=WATCH(新钱),来源是价格——$286.69 无安全边际**(EV 把 YE26 ARR 当兑现),**外加**完整度 ~70%(active MW 缺口)。
- 即:MSFT 是"好公司对价格,但研究未做完(完整度封顶)";**NBIS 是"好公司错价格(+ active MW 缺口)(价格封顶)"**。**镜像对照**,证明 harness 在同 AI-capex 因子内按价格/MOS 分辨。

## 4. 内部一致性检查
- ✅ 各模块信号与 facts 一致;capex 两个口径($20–25B 电话会 / $31–35B 二手)在 facts O-C、financial_quality §red-flag6、inversion 一致登记并标 OPEN,FCF 计算一律用已报 OCF−capex 口径(≈ −$3.66B FY25)。
- ✅ 估值用 253.9M 基本股 + **$286.69** → 市值 $72.79B basic、EV ~$71.9B,全文一致(decision_card.json/.md、valuation.md、facts.md、model/scenario_model.csv)。canonical as_of_price = **$286.69**(= Yahoo adjclose last-close ≤ as_of,三源核验 0.0% delta;prior draft 的 ~$287.73/~$288 已统一为 $286.69)。
- ✅ RPO $33.6B(审计口径)与"$46–50B backlog"(媒体=合同上限之和)明确区分(C044/C045)。
- ✅ take-or-pay(C014)与交付义务/LD(C015)登记为"已解决、不矛盾",残留=交付风险。
- ✅ 无 stale 文件声称不同状态;旧单视频 brief(`../../nbis.md`)明确标 C 级、仅作对照。
- ✅ freshness.json + freshness_check.json 存在,verify_freshness.py **PASS(exit 0)**:price 三源核验、T1–T5 全过、T2 hug 因 ATH 区已 justified、T6 仅 active_litigation WARN(49d,非阻断)。

## 5. 给 IC 的质询点(panel 须正面回应)
1. **active MW 被 withhold(最硬,O-A)**:Q1'26 active(live)MW 未披露(最后 ~170MW YE2025)——这是"建设-通电"转化论点的证明指标,新钱不可 STARTER 的核心原因之一。
2. **$286.69 无安全边际**:EV ≈ 2.2× 全部 RPO ≈ 8–10× YE26 exit-ARR(当作已兑现);bear −50%+ → 价格封顶 WATCH。
3. **极端资本强度 + 负 FCF + 折旧 tailwind**:capex ~7.7×、FCF ≈ −$3.66B、4→5yr 折旧进更快 GPU 周期、两年 adverse ICFR + ClickHouse 非现金净利。
4. **集中度 + 合同结构**:2 客户 ~90%+;take-or-pay 保利用率但 NBIS 背交付义务(违约 → MSFT LD/终止)。
5. **治理**:创始人超级投票(~52–55% vote / ~11–13% econ)+ 无 ROIC/capex-效率激励钩子。

## 6. 完整度结论
**~70% · 新钱 ceiling = WATCH（价格无安全边际,主)+ 完整度封顶（active MW 缺口,次)· 存量 = HOLD（生意被一手验证更好)。** 上修 STARTER（仅新钱）的路径:**价格 de-rate 到 ~$150–180 + active MW 披露并证明转化 on/ahead of 800MW–1GW + capex 坐实 $20–25B 且有相称转化**——三者齐备方可重评,而非更多乐观叙事。
