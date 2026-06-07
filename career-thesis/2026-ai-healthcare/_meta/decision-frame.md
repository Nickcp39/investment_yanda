---
title: 本研究的决策框架（WHY 这份研究存在）
purpose: 让 6 个月后的 Nick、或者 fresh agent，知道这份研究是为什么、给谁、回答什么问题。改 schema / 加新段 / 删数据之前，先读这一份。
owner: Nick
created: 2026-05-16
status: stable
---

# 这份研究为什么存在

## 上下文（决策一句话总结）

Nick 是一个 28-29 岁的 PhD（PA imaging + DL），2026 年 NIW 已批，
家族业务（Hongyu 水文/雨量计）已定位为兼职现金流不是主业。
**主线职业选择已经收敛到："回国，进入中国医疗设备 + AI 出海赛道"**，
原因详见对话记录 2026-05-16 一节"在电梯里做俯卧撑"。

本研究的存在是因为：决定方向之后，还需要看清电梯长什么样、哪部电梯最快、
哪部电梯能上得去（但**不是用"能不能上得去"过滤**——见下）。

## 这份研究回答 4 个问题（按重要性）

1. **β 信号:** 美国 AI 医疗哪些 idea 是真在赚钱 / 高速增长，哪些是融资虚火？
2. **生存性:** 哪些段商业模式已经验证、哪些段在 2-3 年后会显著放缓 / 死掉？
3. **中国映射:** 美国的 idea 在中国有没有对应公司？对应公司在不在 actively 出海？
4. **路径描述:** 假如 Nick 想进某家公司或某个段，**有哪些路径可以走**（不是"能不能进"）

## 这份研究**不**回答的问题

- ❌ "Nick 进 X 公司的概率是多少" —— **不靠成功率思考**（user 原话）
- ❌ "X 公司值不值得投资" —— 这是相邻问题，不是主问题；如果数据足够 inform 这个，bonus
- ❌ "Nick 应该去 A 还是 B" —— 决策是 Nick 的，研究只 inform
- ❌ "X 段会不会赢" —— 我们不押方向，我们描述方向

## ⚠️ Axis 2: 工程师 vs PM 路径（2026-05-16 重要修正）

**初版决策框架的盲点:** 第一轮 elevator map 把 "Nick 不擅长 leetcode" 翻译成了"不该进 S2 LLM 大厂"——这是把 entry path 简化成单一通道，违反了"不靠成功率思考"原则。

**修正:** entry path 不是 1 维，是 2 维：

| 维度 1 | 维度 2 |
|--------|--------|
| 段（S1-S7）| 角色（engineer / PM / clinical app / BD / research scientist）|

同一家公司在不同角色门槛下对 Nick 的"effort to entry"差异极大。例如：
- 字节豆包医疗作为 **engineer entry**: effort = 极高（leetcode binding constraint）
- 字节豆包医疗作为 **clinical PM entry**: effort = 低（你的 PhD + 双语 + 医学背景是教科书匹配）

**PM 路径对 Nick 的结构性优势:**
- PhD + 临床转化经验在医疗类 PM 招聘里是 strongly preferred（不是 dead weight）
- 不需要 leetcode；面试是 case study + 产品 sense + stakeholder 管理
- 双语 + 海外经验是 strict稀缺资源（出海类 PM 岗位）
- 35+ 没有年龄歧视（PM domain expertise 越老越值钱）
- 跨行业 / 跨公司流动性高（PM 技能可移植）

**PM 路径的代价:**
- 不积累技术 stack（如果未来想做 founder，技术合伙人需要另外找）
- 早期薪酬可能略低于资深工程师（但 5 年后追平 + 超过）
- 容易被定位为"中层管理者"而非"技术专家"

**含义:** 评估每个候选公司时都要问：**"engineer entry 不通的话，PM entry 通不通？"** 详细分析见 `04-synthesis/pm-pathways.md`。

## 决策准则（user 自陈，2026-05-16 锁定）

> "我不需要回答是否能上电梯，或者说概率也行，我们不是说 yes or no，
> 而是，比如，需要付出额外努力，这个很正常，就像是马斯克做电动车之前
> 他也不知道能不能成啊，不能用成功率去思考问题。"

**翻译成数据准则:**
- 不给公司打"profile match 分数"（数字会被滥用为概率）
- 不剔除"难进"的公司（剔除 = 隐性的成功率筛）
- 描述 entry_paths 而不是判断 entry_likelihood
- 任何一家"难进"的公司，写清楚要付出什么努力才能进

## 这份研究的"上电梯"判据（user 原话）

> "在电梯里做俯卧撑" = β >> α。**选对赛道比在赛道里跑赢同行重要一个数量级。**

落到本研究：评估一家公司 / 一个段时，问：
1. 这家/段的增长靠 β（行业 trend）还是 α（公司内部经营优秀）？
2. 如果靠 β，β 的 driver 是结构性还是周期性？（结构性 = 行业成熟到不可逆的需求；周期性 = 风口 / 政策 / FOMO）
3. β 的衰减时间窗是多久？（3 年 / 5 年 / 10 年 / 长期）

## 什么会让本研究的结论改变（trigger reread）

如果发生以下任一件事，**重读 + 重新校准**：

| 事件 | 重读什么 |
|------|---------|
| Nick 决定不回国了 | 整个研究无效；归档 |
| Nick 决定全职接手家族业务 | 整个研究无效；归档 |
| 中美脱钩硬化（科技领域全面禁止） | "出海" 叙事崩塌；重读 03-china-mapping/ |
| Abridge 等头部 ARR 增长 < 50% 两个季度 | S1 段 thesis 需修；重读 01-us-landscape/01-clinical-documentation.md |
| 某家中国医疗设备厂在欧美拿下大单 | "出海" 叙事增强；review 03-china-mapping/ |
| 联影 / 迈瑞 / 微创 / 鱼跃 中任一家发布重大裁员 | 中国主线候选受影响；review elevator-map.md |
| 出现新的有显著资金的子赛道（如 surgical AI、agentic care 等） | 加 segment；扩 schema |
| FDA 监管框架对 AI 重大变动 | review 02-us-statistics 中的 moat/regulatory 字段 |

## 这份研究的 owner 和读者

- **Owner:** Nick（一切决定他拍板）
- **主要读者:** Nick 自己 + 任何被他指派来帮他做这件事的 Claude agent
- **次要读者:** Nick 可能想给的"灵魂 panel" agents（按 frameworks/investor_agents.md 跑投资视角时）

任何 agent 在拿到本研究之前都应该先读 `_meta/decision-frame.md` 和 `_meta/agent-runbook.md`，
然后再读 `data/companies.csv`。**不要在没读 decision-frame 的情况下加新公司或改 schema。**
