# AI-机器人 4 龙头批次 — 运行计划 (PLAN)

**批次 ID**: `ai_robotics_2026-07-10`
**as_of**: 2026-07-10 · **pipeline_version**: `lean-6module-v1.1` · **weights_version**: `none`
**主目录**: `D:\work\investment\financial-analysis-lab\companies\_ai_robotics_2026-07-10\`

---

## 0. 来源与选股
线索来自美股投资网视频《未来1年最大美股投资机会——AI机器人产业链》(`notes/videos/2026-07-08_QWXjVbCaExE_..._note.md`,**D1/KOL,仅线索**)。从 ~20 只里选 4 个每层龙头:

| Ticker | 定位 | 本批动作 |
|---|---|---|
| **NVDA** | 平台/算力(机器人只是其一) | **刷新**(基于 `companies/nvda/2026-06-20/`,重抓价+加机器人 lens+重锁 2026-07-10 卡,不重建) |
| **TER** | Teradyne — 唯一有真实已部署机器人收入(UR cobot + MiR) | **全建** |
| **ON** | onsemi — 传感+功率,高级感知 ~1/3 份额 | **全建** |
| **NOVT** | Novanta — 精密编码器/手术级,已入 NVIDIA Holoscan | **全建** |

## 1. 本批要回答的 thesis(用户核心质疑,每家必答)
> 机器人链里有没有一个"**需求已暴增 + 卡死瓶颈 + 已经在赚钱**"的真龙头(像 NVDA 之于 AI 算力),还是全是"**人形起量才受益**"的期权 → WATCH?

每个 Runner 除常规 M1-M6 外,**必须显式回答**:
1. **机器人收入占比%**:当前真正来自机器人/具身智能的收入是多少?vs 汽车/工业/AI 数据中心/半导体测试。
2. **需求是真是预期**:机器人这块是**已发生的现金**还是**anticipation**?给出 dated 证据(订单/出货量),别用发布会。
3. **`CAPITAL_CYCLE.md` lens(必套)**:applicable / stage / supply_barrier / caution —— 针对**机器人段**判,不是整个公司。
4. **真瓶颈 vs 概念**:有没有可证伪的定价权/护城河(替换成本、稀缺 know-how),还是商品化/纯概念?
5. **拆分**:把"机器人期权价值"和"主业(车/工业/半导体)价值"**分开**——现价买的到底是哪个。

## 2. 铁律(沿用 Mega7 + v1.1)
- **freshness 门强制**:`scripts/verify_freshness.py` 必须 PASS(post-INC-001),价格 ≥2 源交叉。
- 一手优先;KOL 只作线索,不进 facts、不支撑 BUY。
- verdict 上限 = 完整度(<40 INFO-GAP / 40-60 WATCH / 60-80 STARTER / >80 CORE)。
- 诚实目标 = `DECISION_DRAFT`,禁谎称 COMPLETE;不确定写 runner_dissent。
- IC 五灵魂(段永平主审 + 巴菲特/芒格/Marks/Klarman),无伪造引语。

## 3. 执行
4 runner → 各自独立 checker(过 `_mega7_2026-06-19/CHECKER.md` v1.1)→ 末端 synthesis(4 家排序 + 直接回答 §1 thesis + capital-cycle 横向 + 机器人收入占比表)。产物落 `companies/<ticker>/2026-07-10/`。

## 4. 进度
| Ticker | Runner | Checker | 状态 | verdict | 机器人收入占比 | capital_cycle | 备注 |
|---|---|---|---|---|---|---|---|
| NVDA | ✅ | ⬜ | RUNNER done (DECISION_DRAFT) | WATCH (0%) / HOLD | <1% (undisclosed; Automotive incl. robotics ~1.09% FY26) | partial/N/A · early · barrier high · caution NONE (robotics seg) | 刷新完成 @ $210.96；freshness PASS；买 NVDA=AI 算力非机器人 alpha |
| TER | ⬜ | ⬜ | — | — | — | — | |
| ON | ⬜ | ⬜ | — | — | — | — | |
| NOVT | ✅ | ⬜ | RUNNER done (DECISION_DRAFT ~60%) | WATCH (0%) / HOLD | ~15–25% est. (undisclosed; humanoid <1–2% prototype) | partial · humanoid=early-anticipation / 工业=mid-recovery · barrier med-high(在位)/low(humanoid) · caution EARLY-ANTICIPATION | @ $156.65 无 MOS(base 5y IRR +1.2%<<8%)；好零件商非 chokepoint；freshness PASS；buy_below ~$115 |

> 预期(基于讨论):大概率**全 WATCH**——若真如此,这批的价值是**用一手数据证实"机器人现在没有可买的真瓶颈"**这个判断,并给每家写死"什么信号出现才从 WATCH 转 STARTER"。
