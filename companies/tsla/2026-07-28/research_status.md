# TSLA Research Status — as_of 2026-07-28 (mega7_2026-07-28 refresh)

最后更新: 2026-07-28 · as_of=2026-07-28 · pipeline_version=lean-6module-v1 · weights_version=none · run_date=2026-07-28

**诚实状态标签: `DECISION_DRAFT`（**不是 COMPLETE**）· completeness ~57% · ceiling = WATCH**

> 本轮是 6/19 基线 dossier 的**聚焦刷新（focused refresh, NOT from-scratch）**: 业务基线（M2 主题 / M3 护城河·operator）快速复核后 carry forward；用今天的价 $307.44 重算 M4/M5/M6 + 叠加 2026-07-28 regime + 并入 Q2-2026 财报（7/22 已出）。诚实目标 = 决策草案（55–75% 完整度），不是彻底跑完。

Decision question: 价格从 $400.49 跌到 $307.44（−23%）+ Q2 交付创记录但利润率塌到 1.4% + FCF 转负 + regime 轮动出 AI 叙事——是否改变 6/19 的 WATCH/TRIM 结论？

---

## Final Verdict 摘要
**new_money = WATCH（0%）· existing_position = HOLD（低信念，贴 TRIM）· business = uncertain · ceiling = WATCH**

- **价格 −23%**（$400.49→$307.44，−38.4% off high，仅 +3.2% 高于 52 周低）→ IRR 阶梯抬高: base −17%→**−12%**、bull +5%→**+11%（现过 8% 门槛）**。价格做掉了 6/19 TRIM 的大部分活。
- **Q2-2026（7/22 已出）**: 营收 $28.24B（+26% 记录）、交付 480,126（+25% 记录）——**量反加速**；但营业利润率 **1.4%**（−57% 营业利润）、监管积分 **−67%**、FCF **−$1.09B**（首次季度烧钱）、capex **+142%**。**更便宜的价 + 更差的利润质量**。
- **Regime**: 轮动出 AI 叙事成长、"AI capex 审计年"直接打 TSLA（capex 猛增却 FCF 转负、零 AI 单位经济）；CXMT/内存 N/A（无 memory 敞口）；FOMC 周三 = swing factor。
- **模块位移**: M4 −1→**−2**（FCF 转负、利润率 1.4%）；M6 −2→**−1**（de-rate 改善入场）→ **对冲，总体不动**。
- **binding constraint 重心从价格转向利润池塌缩**: 营业利润率 1.4% + 积分断 + FCF 转负（regime 放大）+ base 仍无 MOS + Musk key-man/12% 稀释。非硬 veto（fortress、交付创记录、可存活）。

---

## Stage Checklist（刷新范围）
| Stage | Artifact | Status |
|---|---|---|
| 0 基线 carry | ../2026-06-19/ 全 dossier | ✅ 复核 |
| M2 业务复核 | business_model（6/19）+ delta（量反加速修正）| ✅ carry+adj |
| M3 护城河/operator 复核 | moat_map/operator（6/19，未破裂）| ✅ carry |
| M4 财务现实（大刷新）| Q2-2026 并入（freshness.guidance + delta_vs_0619 §1B）| ✅ refreshed |
| M5 反演（叠 regime）| inversion_map.md（regime 表 + K5 新增）| ✅ refreshed |
| M6 估值（现价）| valuation.md + model/scenario_model.csv（$307.44）| ✅ refreshed |
| 两轴 verdict | decision_card.json/.md | ✅ |
| delta | delta_vs_0619.md | ✅ |
| freshness manifest | freshness.json（价格 3 源、Q2 guidance）| ✅ |
| freshness 机械门 | freshness_check.json（verify_freshness.py）| 见下 |

## 完整度 / ceiling
- **~57%**（6/19 的 55% + Q2 一季一手 → 略升）。ceiling 表: 40–60% → **WATCH**。
- 价格改善但 base 无 MOS + M4 恶化 + regime 逆风 → 新钱仍封 WATCH（不因 −23% 便宜就升级）。
- 完整度封顶（57%→WATCH）与 base-IRR 封顶（−12% 无 MOS）**方向一致** → net ceiling = WATCH。batch 的"cap 到 STARTER 除非 >80%"guardrail 不 binding（更紧的 name-specific ceiling 是 WATCH）。

## OPEN（blocking / monitoring 分类）
- **O1**（monitoring→部分 blocking）: SEC 10-Q 逐行/**分部利润**（能源/AI 是否真赚钱）——关键缺口，仍未直取。
- **O2**（monitoring）: robotaxi/Optimus 单位经济不可量化。
- **O5**（monitoring）: 能源分部真实利润率。
- **O7**（monitoring，新）: 股数口径 3,528M（模型）vs ~3.95B（stockanalysis）——若后者，每股/IRR 差 ~11%。
- 以上均**不解封价格/利润池封顶**——即便补齐，base 无 MOS + 利润率 1.4% 仍封 WATCH。

## freshness 机械门
- 已运行 `python scripts/verify_freshness.py --dossier companies/tsla/2026-07-28` → **status = PASS（exit 0）**，`freshness_check.json` 已落盘。
- 价格 $307.44 三源一致（Yahoo fetch + Yahoo meta + stockanalysis，delta 0%）；T1/T3/T4/T5 全 PASS；T2 low-hug PASS（+3.2% off low > 3% band，且已 justified：真实 de-rate 非极值抓取）；T6 guidance PASS（Q2 6d）；T6 active_litigation = **WARN（$1T 包 264d，仍是最新权威治理事件，非 block）**。

## Next Review
- Q3-2026 财报（~2026-10）: 营业利润率是否企稳/继续塌、FCF 是否仍为负（K5）、robotaxi 单位经济、Optimus 是否真量产。
- 价格触发: <~$200 才进入 STARTER 讨论；深 MOS ~$110–130。
- 事件: FOMC 周三（Warsh）利率决定（长久期敏感）。
