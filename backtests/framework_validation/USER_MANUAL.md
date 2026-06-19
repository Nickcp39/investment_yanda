# USER MANUAL — 怎么跑这条 pipeline

先看 `PIPELINE.md` 建立全局观,再用本手册操作。

---

## A. 分析一个新公司(实盘 — 主用法)

### 1) 一键 kickoff（把 `<TICKER>` 换掉,整段丢给 AI / 开一个 agent）
```
你是买方研究 Runner。用「精简 6 模块 pipeline」(lean-6module-v1) 对 <TICKER> 做完整的
公司 + 买入分析,产出一张锁定的 decision_card。

先读这几份 canonical 规范(别用旧 10 层模板):
- backtests/framework_validation/PROTOCOL.md            (6 模块 + decision_card schema §4)
- backtests/framework_validation/COMPANY_MATERIAL_TEMPLATE.md (产出哪些文件)
- backtests/framework_validation/WEIGHTING_HARNESS.md   (信号→仓位 + 情景门控 + 否决规则)
- backtests/framework_validation/METHODOLOGY.md         (仓位阶梯 + 卖出触发 + 耐久天花板)
- companies/_operator_underwriting_template.md          (创始人/操作者 dossier 格式)
- backtests/framework_validation/VERSIONS.md            (取当前 active 版本号盖卡)

模式 = 实盘:用「当下全部公开信息」(最新财报 / 当前价 / 现任管理层),不设 as-of、不做 QA 防穿越。

跑 M1→M6,每个模块出 {signal -2..+2, confidence, finding, drivers(source_id)}:
  M1 证据/可信度(信息缺口 = 缩仓 haircut,不是否决)
  M2 主题机制 + 选 context_label
  M3 利润池/耐久(含 operator_background 生命弧分 → durability 天花板)
  M4 财务现实(正常化盈利 / 周期位置 / 资产负债表)
  M5 反演/陷阱(是否触发硬否决)
  M6 价格/仓位(买入价 + starter/add/trim 区间)
按 WEIGHTING_HARNESS + METHODOLOGY 定性聚合(当前 weights=none)。

产出到 companies/<TICKER>/(公司主目录),用 lean 文件集:
  evidence_spine.md · thesis_mechanism.md · profit_pool_durability.md · financial_reality.md ·
  inversion_trap_test.md · operator_background.md · decision_card.md · decision_card.json
decision_card.json 必须盖 pipeline_version / weights_version / run_date(PROTOCOL §4)。

最后给我这张表:
  business_verdict ·
  新钱 = REJECT/WATCH/STARTER/CORE + 起步%/上限% + buy_below ·
  已持有 = EXIT/TRIM/HOLD/ADD ·
  binding_constraint · kill_criteria · 下次回评盯什么。
若机械结果感觉不对,写进 runner_dissent。
```

### 2) 你会拿到什么
一套 6 模块材料文件 + `operator_background.md` + 一张 `decision_card`(`.md` 给人读、`.json` 给机器读)。

### 3) 怎么读 decision_card(你真正要照着做的那张表)
| 字段 | 怎么用 |
|---|---|
| `new_money_verdict` | 没仓位时:`REJECT` 不碰 · `WATCH` 观望 · `STARTER` 小买 · `CORE` 重仓 |
| `suggested_initial_size_pct` / `_max_size_pct` | 起步仓 → 可加到的上限仓 |
| `buy_below_price` | 低于此价才值得动手 |
| `existing_position_verdict` | 已持有:`EXIT` 清 · `TRIM` 减 · `HOLD` 拿 · `ADD` 加 |
| `add_zone` / `trim_or_no_chase_zone` | 加仓区 / 减仓·不追区 |
| `kill_criteria` | 什么发生就改主意（= 回评要盯的清单） |
| `binding_constraint` | 这笔的真正胜负手(最该跟踪的一件事) |

**默认回评周期 = 下一份季度财报(~1 季度)**;价格触及加/买区、或某条 kill 触发则提前。

### 4) 几条硬纪律(pipeline 的灵魂,别绕过)
- `operator_background.md` 是**必备文件**;生命弧分进 durability 天花板(高抬 / 低压)。
- M1 信息不全 → **缩小仓位,不是打成 WATCH/0%**(这是旧框架的病,已修)。
- **新钱 vs 已持有 分开判**(好公司变贵:新钱观望,但有仓 HOLD,不是卖)。
- 当前无数值权重 → 聚合是定性推理 → **同一家公司两次跑结果可能略有出入**(已知限制,见 C)。

---

## B. 跑一个盲回测 case(验证 / 调框架用)
和实盘的差别 = **冻结一个 `as-of` 日 + 全程禁用之后的信息 + 加 QA 独立防穿越 + SC 对真实结局评分**。
- 顺序协议(一案一案跑、角色隔离):`TEST_PLAN.md`
- 防穿越清单 + 各 case 禁项:`LOOKAHEAD_CHECKER.md`
- 评分入账:`results.csv`(schema 见 `WEIGHTING_HARNESS.md §7`)
- 加新 case:先建材料包(`MATERIAL_COLLECTION_PLAN.md` 的格式),再 checker → blind Runner → Scorer。

---

## C. 已知限制(诚实)
1. **回测里 Runner 是 LLM**,对家喻户晓的大盘股有「训练知识」层面的潜在前视:流程能挡掉**材料/来源**层面的穿越,但挡不死模型权重里的结局记忆。想更硬 → 盲标的(打码公司名)/ 冷门小盘股 / 真·前向测试。
2. **v1 无数值权重**(`weights=none`)→ 聚合定性 → 有 run-to-run 方差。要"每次结果一致"得先验证补丁 + 定 `W_v1`。
3. 个别规范文件头还写 `DESIGN - NOT YET RUN` = 过时;以 `VERSIONS.md` + `SCORECARD_v1.html` 为准。
