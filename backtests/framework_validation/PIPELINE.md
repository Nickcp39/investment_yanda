# PIPELINE — 端到端流程(canonical)

精简 **6 模块**买方 pipeline。一句话骨架:
**主题 → 机制 → 标的 → 证据 → 财务 → 反演 → 价格 → 仓位**
(细节看各规范文件;本页只建立全局观 + 指路。)

## 两种模式
| | 实盘(分析新公司) | 盲回测(验证/调框架) |
|---|---|---|
| 信息范围 | **用当下全部公开信息** | 只用某 `as-of` 日之前的信息 |
| 额外步骤 | 无 | `00 Freeze Case` + `QA 防穿越` + `SC 评分` |
| 看结局? | N/A(未来未知) | 仅 Scorer 可见(打分用) |
| 入口 | `USER_MANUAL.md → A` | `USER_MANUAL.md → B` + `TEST_PLAN.md` |

## 阶段流程
```
实盘:  01 收证据 → M1 → M2 → M3 → M4 → M5 → M6 → 锁 decision_card
回测:  00 Freeze(锁 as-of/禁后视) → 01 → M1..M6 → 锁卡 → QA(独立防穿越) → SC(对真实结局评分)
```
关键纪律:**Runner 锁卡前不看结局;回测的 checker/scorer 必须是与采集者不同的 agent**(角色隔离,见 `PROTOCOL.md §3`)。

## 6 个模块(每个必出一个 signal -2..+2;定义见 `PROTOCOL.md §1` + `COMPANY_MATERIAL_TEMPLATE.md`)
| 模块 | 角色 | 干什么 | 产出文件 |
|---|---|---|---|
| **M1** Evidence Spine | confidence | 截至现在到底知道什么、可信度;缺口 → **haircut 不否决** | `evidence_spine.md` |
| **M2** Theme/Mechanism | context+conviction | 为什么现在、机制是什么、定 `context_label` | `thesis_mechanism.md` |
| **M3** Profit Pool/Durability | conviction | 利润池归谁、能否持久(含护城河 + **操作者生命弧**) | `profit_pool_durability.md` + `operator_background.md` |
| **M4** Financial Reality | conviction/warning | 财报是否验证机制;正常化盈利 / 周期位置 | `financial_reality.md` |
| **M5** Inversion/Trap | risk/veto | 会不会是永久损失 / 结构性陷阱 / 假便宜 | `inversion_trap_test.md` |
| **M6** Price/Position | price+output | 价格够不够、买多少、加/减/卖区间 | `decision_card.md` + `.json` |

## 聚合 → 决策(详见 `WEIGHTING_HARNESS.md` + `METHODOLOGY.md`)
- conviction 来自 **M2/M3/M4**;risk/veto 来自 **M5**;confidence(haircut)来自 **M1**;price 来自 **M6** → 落到 `target_size`。
- `context_label` 选一套**情景门控**(每个情景哪几个模块主导、价格是否能否决):
  `quality_compounder · exceptional_bottleneck · cyclical_inflection · turnaround · spinoff_forced_seller · structural_decline_trap · false_cheap_value_trap · yield_or_balance_sheet_trap · too_hard`
- **操作者生命弧分** → 调 durability 天花板(高分抬顶、低分压顶)。
- 输出**两轴**(分开判,别混为一谈):
  - **新钱**:`REJECT / WATCH / STARTER / CORE`
  - **已持有**:`EXIT / TRIM / HOLD / ADD`

## 输入 → 输出
- **输入**:一个 ticker(实盘);或 ticker + `as-of` 日(回测)。
- **输出**:一套材料文件 + `operator_background.md` + 锁定的 `decision_card.json`(盖 `pipeline_version`/`weights_version`/`run_date`)+ 人读的 `decision_card.md`。

## 旧 10 层 → 新 6 模块映射(为什么 6 个就够)
旧 10 层是"**能力清单**"(确保没漏看),新 6 模块是"**会改仓位的执行单元**"。同一套东西、两层视角:
`M1←L3 · M2←L1,L2 · M3←L5,L6,L7 · M4←L4 · M5←L8 · M6←L9,L10`
(所以 `companies/_company_research_template/` 的 10 个文件不是新增工作,是被压进了 6 个模块文件。)
