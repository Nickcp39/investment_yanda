# 当前进度 (Current Process)

最后更新: 2026-07-25

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

---

## 最近一轮工作 (2026-07-25)

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
4. **韩国第三条对照线**（可选）—— 2018 年后地产+老龄化，介于中日之间
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
- [studies/jp_cn_relative_timeline/](studies/jp_cn_relative_timeline/) — 中日相对时间轴系列（本轮主产出）
- [companies/mindray/2026-07-25/decision_card.md](companies/mindray/2026-07-25/decision_card.md) — 迈瑞裁决
- [theses/2026-market-map.md](theses/2026-market-map.md) — 市场地图
- [execution_plans/btc_investment_plan_2026-07-17_v2.md](execution_plans/btc_investment_plan_2026-07-17_v2.md) — BTC 执行计划 v2
- [frameworks/investment_research_pipeline_detailed.md](frameworks/investment_research_pipeline_detailed.md) — 研究流程
- [research_queue.md](research_queue.md) — 选题队列
