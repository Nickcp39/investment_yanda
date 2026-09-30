# MSFT Checker Report — mega7_2026-07-28

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT**（非 COMPLETE，诚实标注，无 overclaim）
verdict / size / ceiling: new_money **STARTER** · init **3%** / max **9%** · ceiling **STARTER** ← 是否被完整度正确封顶: **是**
数据新鲜度: **PASS**（`freshness_check.json` status=PASS / exit 0；Checker 独立重抓 Yahoo 复现同价）
Gate 勾选: A✓ / B~ / C~ / D✓ / E✓ / F✓
伪造引语 / 失配数字: **无**

---

## 1. 价格完整性（INC-001 核心检验）— PASS

Checker **独立**重抓 Yahoo chart API（未用 Runner 产物）：

| 字段 | Runner 卡 | Checker 独立重抓 | delta |
|---|---:|---:|---:|
| regularMarketPrice | 393.35 | **393.35** | **0.0%** |
| regularMarketTime | 2026-07-28 close | **2026-07-28 20:00 UTC**（EDT 收盘） | ✓ |
| 52wk high | 555.45 | **555.45** | 0.0% |
| 52wk low | 349.20 | **349.20** | 0.0% |
| 日内区间 | 391.30–400.32 | **391.30–400.32** | ✓ |

- **不是 52 周极值**：现价 **+12.6%** 高于 52 周低、**−29.2%** 低于 52 周高（clears 3% T2 band 双侧）。INC-001 失效模式（拿 52 周低 $349.20 当现价）**明确不存在**。
- **衍生数全部内部自洽**（Checker 独立重算逐项对上）：市值 2.9218T（7428M×393.35）、P/E 23.34×、P/FCF 40.08×、收益率 4.29% / FCF 收益率 2.50%、距高 −29.2% / 距低 +12.6% / vs 6/19 +3.7%。
- **DCF 三情景独立复算精确命中**：Bear IRR −0.29%(卡 −0.3%)、Base **9.12%**(卡 9.1%)、Bull 14.75%(卡 14.8%)、6/19 基线 9.52%(卡 9.5%，Δ−0.4pp)；8% 门槛公允价 **$436.28**(卡 $436)。owner-earnings 终值法(OE0=112, g=11%, exit22×) tied to 假设，可审计。

## 2. 52 周高口径差异（唯一需点名的 nit，非缺陷）

卡 / valuation / delta 用 **$555.45**（Yahoo + stockanalysis 两独立 LIVE 源，Checker 亦重抓得 555.45），而批次 `PLAN.md` 锚表写 **$542.07**。Runner 在 `freshness.json` line 47 **透明记录**了该偏离：「PLAN 锚 542.07 为不同 vendor/adjusted-close 口径；此处记 2 个独立 LIVE 源实际返回值 555.45；对 gate immaterial——价距高 ~−29% 远在 3% hug band 外」。

判定：**Runner 取值正确**（555.45 是今日 Yahoo 实返值，比 PLAN 的 542.07 更 live），偏离已带源说明，且**不触及任何 gate / verdict / 估值数**（52 周高不进 DCF，仅进「距高」描述位；若改用 542.07，距高变 −27.4% 而非 −29.2%，纯描述性）。→ **保留 CLEAN，仅记为 nit**。

## 3. 新鲜度机械门 — PASS

- `freshness.json` manifest 齐备，每个 LIVE 字段 ≥2 独立源：price(3)/mcap(2)/52wk_hi(2)/52wk_lo(2)/shares(2)/guidance(3)/litigation(2)。
- `freshness_check.json` **status=PASS / exit_code 0**；`scripts/verify_freshness.py`(25KB) 实存；`refetched_yahoo=393.3500061035156`(float32 精确形) = 真实 live 拉取；tripwire T1 band / T2 hug / T3 mcap-identity / T4 距高对账 / T5 single-value / T6 LIVE-qual 全 PASS。
- Checker 独立复现现价 393.35（0.0% delta）→ 机械门可信，非人工放行。

## 4. Verdict 上限 — 正确封顶

completeness **~63%** → 落 60–80% 区间 → ceiling **STARTER**。new_money=STARTER **正好在顶、未超**；未称 CORE。size 与耐久性匹配：business=exceptional + 一股一票 → 天花板 9%，但初始仅 3%（starter sliver，非 Core-size）；封顶来自完整度（O2 capex 维护/成长拆分 + O4 分部利润率仍全开，O3 收窄未闭合），**非价格**（价格端仍正 MOS ~10%）。E 区 open question 分类清晰、blocking 项显式封顶。

## 5. 诚实性 / 伪造检查 — 通过

- 状态标签 `DECISION_DRAFT`，`research_status.md` 显式声明「本轮未达 COMPLETE…不使用'完成/彻底跑完/full research complete'语言」→ **无 overclaim**（铁律 5 通过）。
- **无伪造引语**：本轮为 lean-6module 聚焦刷新，无 Stage-8 五灵魂 IC panel，全文无任何冒名归属引语；`runner_dissent` 为 Runner 本人口吻的两面 dissent，非引语。
- **Regime 真的并入 M4/M5**（非忽略）：M5 `inversion_map.md` 系统叠加半导体暴跌 / CXMT / capex-审计 / FOMC，并给出高质量非偷懒读数——**MSFT 是内存买方→降价是成本顺风非威胁**（区别于 SK 海力士/美光卖方），新增 K-F kill；M4 并入「内存降价缓解 $190B 里 ~$25B 组件通胀」+ 诚实标注 Q4 未出。M2 并入轮动受益方 vs capex-审计靶子的两面性。
- **无 lookahead**：as_of 7/28，Q4 财报 7/29 盘后未发；卡明确 carry Q3 FY26+FY25 10-K、只用 Q4 **指引**，未泄未来数（`reported_q2=false` 属实）。

## 6. Gate 说明（B/C 标 ~ 的原因，非未过）

- **B 证据**：以 `sources_used[]`(10 源，含名+日期+link) + freshness manifest 充当证据脊柱，均带日期与隐含 tier（SEC/IR 一手为主）；无独立 `source_register.md`/`claim_ledger.csv`/`raw/` —— 属聚焦刷新的轻装形态，与 DECISION_DRAFT 标签一致，非违规。**唯一实质二手依赖**：$250B OpenAI→Azure 承诺仅单一二手源（valueaddvc VC 博客，7/01）未经一手佐证；但被**保守当 context/lead 使用**（不抬 verdict、反增单一对手方集中度风险），**未直接支撑 BUY**，合规——建议 7/29 10-K 落地后补一手。
- **C 11-stage/IC panel**：六模块覆盖齐（Business/Financial/Moat/Bottleneck/Inversion/Valuation 各有产物），但无独立 Stage-8 IC panel —— 这正是 completeness <80%、封顶 STARTER 的构成之一，已被 ceiling 正确反映，非需 FIX 的缺陷。

## FIX 清单
**无强制 FIX。** 建议性（不阻断）：
1. `freshness.json` 已记 52 周高 555.45 vs PLAN 542.07 的偏离 —— 一致性无碍，可选在 synthesis 里统一批次锚表口径（`PLAN.md` line 23 的 542.07 建议对齐为 live 值）。指向 `_mega7_2026-07-28/PLAN.md`。
2. $250B OpenAI→Azure 承诺（`freshness.json` active_litigation / `decision_card.json` OPENAI-AZURE-250B）7/29 后补一手（MSFT/OpenAI 官方）佐证。
3. 「7/28 +1.09% 反弹」措辞（`valuation.md` §0 / `freshness.json` price.note）偏软——当日开 ~400 收 393.35 处于 391.30–400.32 下半区；纯 cosmetic，不影响现价($393.35 精确)与任何衍生数。

## 一句话
**这家这轮高度可信**：现价 $393.35 经 Checker 独立 Yahoo 重抓 0.0% 命中、明确非 52 周极值、DCF/倍数逐项复算精确对上，新鲜度机械门真过，STARTER/3% 被 ~63% 完整度正确封顶，状态诚实标 DECISION_DRAFT 无 overclaim，regime 真并入 M4/M5——**唯一 nit 是 52 周高 555.45 vs PLAN 542.07 的 vendor 口径差，Runner 已带源披露且对 gate immaterial，不改裁定**。CLEAN。
