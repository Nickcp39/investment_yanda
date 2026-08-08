# 当前进度 (Current Process)

最后更新: 2026-08-07

## 这份文档的用途

快照式记录 lab 当前阶段、最近做完什么、下一步要做什么。每次阶段性
push 时刷新一次，避免回头时丢失上下文。

不是 changelog（那个看 `git log`）。是"我现在在哪一关"。
目录地图见 `folder_structure.md`（AI/新会话先读那份 + 这份，不要全仓扫描）。

---

## 当前阶段

**Phase**: 中日相对时间轴专题 + 个股 dossier 流水线 双线推进

- **专题线（新开）**：`studies/jp_cn_relative_timeline/` —— 以房价见顶为
  T=0（日本 1991 / 中国 2021）对齐两国相对时间轴，对比产业政策、国产
  替代、社会思潮的逐年演变，推演行业终局
- **个股线（持续）**：dossier 流水线批量跑（S&P500 医疗、AI-robotics、
  mega7 等批次），产出 decision_card 裁决
- **本轮扩充**：`sectors/macro-compare/` 把"日中医疗终局"扩成**六国对照**
  （日/韩/中/英/加/美），带源 + HTML，兑现了"下一步 #4 韩国对照线"计划

---

## 最近一轮工作 (2026-08-07)

### 黄金估值与相对资产配置：对 M2 的 σ 通道 + SPY/QQQ 回测

`backtests/黄金_货币供应_估值_2026-08-07/` —— 把 QQQ 那套 log-trend ± σ
的机器换个横轴：从"时间"换成"美国 M2"。三条免费源（LBMA 定盘价 1968-、
美联储 H.6 的 M2 1959-、BLS CPI-U），`fetch_data.py` 可原地重跑。

- **主模型** `ln(金价) = -1.03 + 0.864·ln(M2)`，σ = 0.389 对数（1σ ≈ +48%/−32%）。
  按 2026-06 的 M2 反推中枢 $2,100，±1σ 带 $1,423–$3,098。
- **当前读数**：2026-06 月均 $4,238 = **+1.81σ**；金价/M2 比值处于 1971 年
  以来第 **89.5** 百分位，CPI 平减后的实际金价第 **99.1** 百分位。今年 1 月
  高点 $5,405 = +2.44σ，是 1981-05 以来第一次冲出 +2σ 带。
- **修正后的主信号**：先前的扩张窗口仍会把 1970 年代留在 2015/2024 的斜率里，
  不可用于局部周期。相对收益研究放在
  `backtests/黄金_vs_SPY_QQQ_相对收益_2026-08-07/`，改为**严格 10 年滚动 OLS**：
  每月只用当月及此前 119 月拟合 `ln(金价) ~ ln(M2)`，同时比较后续 1/3 年
  黄金是否跑赢复权 SPY 与 QQQ。
- **两类有效节点被区分出来**：2015 年末为约 **−1.95σ** 的低估/反转节点；
  2024-01 为 +1.43σ、2024-03 后进入 +2σ 的趋势突破节点。低 σ 不是唯一买点；
  高滚动 σ 表示相对近十年关系的突破，不等于绝对高估。当前月末为 +1.82σ，
  最新 LBMA 金价配最新 M2 约 +2.08σ；要按 3 年趋势仓位理解，而非低估大仓。
- **仍然成立的纪律**：全样本拟合只可描述历史，不能当实时信号；月度重叠窗口
  不是独立样本。下一步不能再只按 σ 单因子决策，须把低估反转与趋势突破拆成两条
  规则，并加入趋势失效条件后复测。
- **样本极限**：最贵那一档只有 20 个月，实质是 1981 与 2011–12 **两段行情**；
  2025-09 起是 45 年来第三次进入该区间。

### 组合执行计划与被杀估值科技批次

- `execution_plans/btc_investment_plan_2026-08-07_v3.md`、
  `equity_index_plan_2026-08-07.md`、`dca_tracking_2026-2027.md` 固化当前
  4 桶执行：BTC $200/日（现货、含周末）；QQQ/SPY/BRK.B 为 $50/$25/$25 每交易日。
- `companies/_derated_bigtech_2026-08-07/` 汇总 ORCL/NFLX/ADBE/INTU：ADBE
  STARTER 3%、INTU STARTER 2%，ORCL/NFLX 均 WATCH 0%。本批方法论产出是把
  “跌的是倍数还是生意”拆成**是否有匹配的经营损伤**，并确认“维护 vs 成长支出”
  是六家大科技卡共同的待解瓶颈。

### 下一步（本轮新增）

1. 为黄金建立“双规则”回测：`≤−1σ` 的反转入场，与 `≥+1σ + 趋势未失效` 的
   突破入场分开评估；禁止用同一个 σ 阈值解释两种机制。
2. 将金价货币锚从美国 M2 扩展至全球货币口径，并检查 10/15/20 年滚动窗口的稳健性。
3. 完成被杀大科技批次的独立 checker；优先补维护/成长支出拆分模块，随后处理 ADBE
   可证伪性与 INTU 的 IRS Direct File 证据。

---

## 上一轮工作 (2026-07-25)

### 1. 中日相对时间轴系列（studies/jp_cn_relative_timeline/，本轮新建）

方法论：房价峰值只作为"经济压力起点"的对齐零点，不比较地产本身；
主线是各行业的政策/替代/思潮进程发生在衰退后第几年。当前 2026 =
中国 T+5 ≈ 日本 1996。

- `automation_semis.md` —— 自动化+半导体 vs（此前本地做的）医疗器械。
  核心结论：半导体中日**反向**（日本守擂被压制 vs 中国攻擂被倒逼）；
  自动化是唯一**同向**行业（汇川≈FANUC 路径，中国 T+5 走完日本 T+15-20
  的里程碑）；日本守住的是设备/材料层 → 中国对应北方华创/中微这一层
  确定性最高
- `zeitgeist_healthcare.md` —— 思潮走向 + 医疗终局。核心结论：中国
  "预习过剧本"，每个心态节点比日本提前 5-10 个相对年出现（躺平在 T=0
  前就是热词，日本"低欲望"定名在 T+24）；医疗方向上会重演日本三铁律
  （支付方永久压价 / 利润池不在国内 / "老龄化=买医疗"被证伪，被证实的
  是"买能出海的医疗"），但三处分岔（集采比日本早 14 个相对年、器械做
  替代、创新药 T+2 就 license-out 出海）
- `semis_timeline.html` —— 半导体四层时间轴（政策/市场/思潮/外压）HTML
  总结，裁决：反向
- `autos_timeline.html` —— 汽车 HTML 总结，裁决：同向但时序错位
  （日本泡沫**前**完成全球化，中国泡沫**后**才出海 → 海外接棒未完成是
  最大风险缺口，对应窗口 2031-2038）。全系列最重要镜像：半导体里日本
  是被压制的在位者，汽车里今天日本再次成为被攻擂的在位者，攻擂者换成
  中国

### 2. Mindray（迈瑞）dossier 入库（main 分支，2026-07-25）

`companies/mindray/2026-07-25/` 全套标准件——正好是"能出海的医疗"
论点的第一个个股落地，与时间轴系列互为印证。

### 3. 项目元文档（本轮）

- 新建 `folder_structure.md`（目录地图 + AI 导读 + dossier 约定速查）
- 刷新本文件（上一版停在 2026-05-22，已过时两个月）

### 4. 崩盘后·政府医疗政策 六国对照（sectors/macro-compare/，本轮新建）

把 `zeitgeist_healthcare.md` 的"日中医疗终局"做成**带源、可视化、扩到 6 国**
的专项（与 `studies/jp_cn_relative_timeline/` 互补，不重复）：

- `japan_china_healthcare_policy_2026-07-25.html` —— 日↔中双泳道 T0 对齐 +
  总开支/价格剪刀差指数图 + 中国下一步剧本表
- `global_housing_crash_healthcare_2026-07-25.html` —— 日/韩/中/英/加/美
  六国温度时间线，按医疗体系分三簇 + "中国像谁"判定矩阵 + 各国明细
- `_research/{us,uk,canada,korea}.md` —— 4 个并行 agent 的一手研究笔记（带源 + 待核）
- 核心结论：崩盘后普遍转控费、但总开支照涨；**形式取决于体系类型**（社保=
  集采砍价、税收单付=排队、美国=先扩覆盖）；**中国属东亚社保簇 → 日/韩最准**；
  真正扳机是"支付方财政"（盯医保结余 + 地方债，加拿大证）；长护险=最脆弱环节
  （英国证）

---

## 近期主线回顾 (2026-06 ~ 2026-07，详见 git log)

- **dossier 批次流水线**：S&P500 医疗批次 1-2（MDT/SYK/BSX = STARTER，
  ABT/TMO = WATCH）、AI-robotics 四龙头批次（NVDA/NOVT/ON/TER）、
  career-track 批次（GEHC/TEM/BFLY）、NBIS/MU refresh、GOOGL 重跑、
  NIO dossier
- **专题**：财富榜三快照研究（studies/wealth_rankings，利润池迁移）、
  医疗行业 deep-dive、资本周期框架笔记
- **执行计划**：BTC 投资计划 v2（execution_plans/）
- **工具**：log-trend 系列脚本扩充（对数趋势通道 + DCA 回测）

---

## 下一步 (按优先级)

1. **补齐时间轴系列的医疗器械篇** —— 器械政策时间轴此前在本地会话完成
   但未入库，需从本地 push 上来（或重做），然后五条产业线（自动化/
   半导体/汽车/医疗/器械）合并成一张可缩放 HTML 总览：自然年份 vs
   距高点年数双视图 + 思潮事件层
2. **时间轴系列数据核验** —— 两份 md 的"待办"节里列了具体项（IFR 机器人
   密度修订值、汇川份额口径、日本医疗股出海组 vs 内需组回报实证、
   中日 T=0 时点人口/GDP 精确值）
3. **"出海"筛选落地到个股** —— 用"海外收入占比及其斜率"筛医疗/汽车链/
   自动化标的，接到 dossier 流水线（迈瑞已做，联影、汇川、比亚迪链候选）
4. ~~**韩国第三条对照线**~~ **✅ 已完成并超额**（本轮）—— `sectors/macro-compare/`
   已把韩国 + 英/加/美 做成六国对照；剩余可选：把六国结论反哺 `china_deep/` 个股
   注记 + 与 `studies/jp_cn_relative_timeline/` 交叉引用
5. **S&P500 医疗批次收尾** —— batch-2 当时 API 中断记录为 PARTIAL，待续
6. （历史 backlog，5 月遗留，优先级待重估）灵魂 Skill benchmark
   （buffett-perspective / expert-munger 过 rubric 75 分门槛）、段永平
   雪球 export pipeline、Howard Marks 材料收集

---

## 已知风险 / 注意

- 时间轴系列目前是"叙事+方向"级别，关键数字未逐条核验（已在文内
  标注待验证），引用前先过一遍数据核验
- 本地会话与仓库可能不同步：器械时间轴只存在于本地；凡在本地做的
  分析要及时 push，否则云端会话看不到
- 5 月遗留的灵魂训练线已两个月未动，状态表见 git 历史版本
  （`git show aba3817~N:current_process.md` 可查旧快照），重启前先重估

---

## 相关文档导航

- [folder_structure.md](folder_structure.md) — 目录地图（先读）
- [studies/jp_cn_relative_timeline/](studies/jp_cn_relative_timeline/) — 中日相对时间轴系列（多行业）
- [sectors/macro-compare/](sectors/macro-compare/) — 崩盘后医疗政策六国对照（日中深度 HTML + 六国 HTML + agent 研究笔记，本轮新建）
- [companies/mindray/2026-07-25/decision_card.md](companies/mindray/2026-07-25/decision_card.md) — 迈瑞裁决
- [theses/2026-market-map.md](theses/2026-market-map.md) — 市场地图
- [execution_plans/btc_investment_plan_2026-07-17_v2.md](execution_plans/btc_investment_plan_2026-07-17_v2.md) — BTC 执行计划 v2
- [frameworks/investment_research_pipeline_detailed.md](frameworks/investment_research_pipeline_detailed.md) — 研究流程
- [research_queue.md](research_queue.md) — 选题队列
