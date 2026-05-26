# 当前进度 (Current Process)

最后更新: 2026-05-22

## 这份文档的用途

快照式记录 lab 当前阶段、最近做完什么、下一步要做什么。每次阶段性
push 时刷新一次，避免回头时丢失上下文。

不是 changelog (那个看 git log)。是"我现在在哪一关"。

---

## 当前阶段

**Phase**: 行业深度调研 + 灵魂训练 并行推进

- 灵魂方向：上一阶段定调 **Adopt(Buffett) + Build(其他)**，benchmark
  跑分待补
- 行业方向：**US Healthcare(PBM) + China Healthcare(流通/零售) + 个人职业
  方向** 三线并行，已经进入 L2 / L3 真研究阶段（带一手数据 + 出处）
- 个人方向：开了 `personal/` namespace，跟市场研究分开放，专门承载
  "人生与职业"的 thesis 与决策日志

---

## 最近一轮工作 (2026-05-22)

### 1. `personal/` namespace 落地（新）

正式拉出 `personal/` 目录，跟 `companies/` / `sectors/` / `macro/`
分层级。规则在 `personal/README.md` 里写死：

- `personal/career-thesis/` — 当前职业/路径 thesis 演进
- `personal/research/` — 支撑职业 thesis 的研究
- 跨链规则：如果职业 thesis 推出市场仓位（例如 long 联影/迈瑞），
  *职业理由* 留在这里，*市场备忘* 写到对应 `companies/` / `sectors/`，
  双向交叉引用

### 2. 云迹科技（02670.HK）对赌条款核查

- `personal/yunji-vam-verify/plan.md` — 调研计划
- `personal/yunji-vam-verify/verification.md` — 核查结论

**结论**：用户拿到的"上市后 2025–2029 业绩对赌 / 支涛个人无限连带 /
管理层按持股比例分摊"那套说法，**主要内容在招股书与一手资料里找
不到出处**，疑似 AI 生成或自媒体演绎。

- ✓ 人物 / 持股比例 / D 轮金额 与招股书一致
- ✗ "上市后业绩对赌" 框架 — 实际是 Pre-IPO 赎回权，上市落地即解除
- ✗ "支涛个人无限连带 + 管理层分层有限责任" — 公开资料无任何对应
  披露
- ✗ "(30% − 实际增速) / 30%" 补偿公式 — 无出处
- ✗ "连续 2 年增速 <15% + 破发" 触发回购 — 无出处

⚠ 归档位置临时放在 `personal/`，但严格来说属于市场研究核查，后续
可能挪到 `companies/yunji/` 或 `sectors/china-robotics/`。

### 3. `.gitignore` 补充

- 加入 `.claude/worktrees/` — Claude Code worktree 状态目录不入库

---

## 上一轮工作 (2026-05-16)：行业深度调研集中产出

### US Healthcare — PBM L1 + L2 完整调研

`sectors/us-healthcare/` 全新目录，按层级深度推进：

- L1：`层1-完整调研.md` + `层1-规则与监管-深度.md` + `流程跑通-层1.md`
- L2：`层2-付费与保险-完整调研.md` + `层2-子题-PBM拆解.md`
- 行业结构：`行业结构与机会分析.md`（v1，2024 NHE ~$5T、占 GDP 17.8%）
- 工作机会矩阵：`各层工作机会矩阵.md`
- PBM 子题深度：三巨头详解（Caremark / OptumRx / Express Scripts）、
  FTC 第二期 interim 报告抽取、analyst views 与 2025 监管落地、内部
  员工口径（Glassdoor / Blind 引文）
- 数据底子：`data/analysis/` 含 4 个派生 CSV
  - `PBM-2024-segment-baseline.csv`
  - `PBM-Cost-Plus-disruption-scenarios.csv`
  - `PBM-reform-2027-cliff-model.csv`
  - `PBM-specialty-generic-markup-projection.csv`
- 数据出处：`data/sources/sources-PBM.csv`
- 调研笔记：`research-notes/PBM/` 5 个 raw search batch + search-log

### China Healthcare — L3 v2 真研究（流通与零售）

`sectors/china-healthcare/L3-v2-deep.md`，跟 v1 的本质区别：

- **24 次精准 web 搜索**全部保存到 `research-notes/L3/raw-searches/`
  - 1A：流通巨头 batch 1 + 2
  - 1B：零售连锁
  - 1C：互联网医药
  - 1D：DTP / JD 内部
- **148 个 L3 数据点**入库 `data/sources.csv`（每条带 URL + 日期 +
  source_type）
- **6 个派生计算 CSV** in `data/analysis/`：
  - L3-DTP-CAGR-reconciliation.csv
  - L3-productivity-comparison.csv（单人产出比）
  - L3-margin-trajectory.csv（利润率轨迹）
  - L3-employment-bottoms-up.csv
  - L3-internet-pharma-growth-projection.csv
  - L3-4-chains-extinction-projection.csv（4 大连锁灭亡投影）
- 研究协议：`research-notes/L3/_research-protocol.md`
- v1（凭印象）→ v2（每个数字标 source id；推算单独标出）的方法论
  升级在这一轮固化下来

### 配套结构性文档

- `sectors/china-healthcare/_research-plan.md` — China 6+1 层结构方案
  （不照搬 US 的 6 层，加 1.7 出海路径层）
- `行业结构与机会分析.md` / `行业全景与切入点.md` / `各层工作机会矩阵.md`

---

## 上上轮工作 (2026-05-06)

### 测试结论：ai-hedge-fund 全部 agent 不采纳

- 跑了 ai-hedge-fund 仓库里的 investor personas (Munger / Cathie Wood /
  Damodaran 等)，结论：**整体不如自训灵魂卡 + buffett-perspective 的
  组合**
- 输出形态是 trading signal（buy/sell/hold + confidence），不是
  investment memo lens — 用途不匹配
- 撤销 5/4 audit 里 "fork ai-hedge-fund" 的 P1 计划

### 影响：外部 Skill 采纳通道收窄

hybrid plan 实际上退化成 **Adopt(Buffett) + Build(其他全部)** 两档。
Fork 这一档先放进 backlog。

---

## Skill 采纳状态

| 灵魂 | 候选 Skill | 状态 | 下一步 |
|---|---|---|---|
| Warren Buffett | `buffett-perspective` | prompt sanity + 会话验证均通过 | 跑 benchmark_cases.jsonl 全量 |
| Charlie Munger | `expert-munger` | 一次会话验证通过 (NBIS) | 多场景 + benchmark |
| Howard Marks | 待找 | Build candidate | 收集 Oaktree 备忘录全集 |
| Seth Klarman | 待找 | Build candidate | 一手材料盘点 |
| 段永平 | 无 | **Build 必须** | 雪球 export pipeline |
| Li Lu | 无 | **Build 必须** | 一手材料盘点 |

⚠ "通过会话验证"≠ 正式采纳。正式采纳门槛仍然是 `rubric.md` ≥ 75
分跨 ≥ 3 案例。

---

## 数据采集 Pipeline 状态

频道索引 + 元数据 + ASR 三层基础设施已搭好（无变化）：

- ✅ `scripts/channel_video_index.py` — Bilibili / YouTube 频道索引
- ✅ `scripts/bilibili_channel_queue.py` — Bilibili 元数据队列
- ✅ `scripts/youtube_asr_queue.py` — YouTube 无字幕兜底 ASR

已收录频道：

- `tradesmax` (YouTube) — 美股投资网，AI 主题视频源
- `zhanguoshidai` (YouTube + ASR) — 战国时代频道
- `bilibili-1039025435` (Bilibili) — 段永平相关（待确认归类）

⚠ audio/ 与 transcripts/ 全部 gitignore（zhanguoshidai/audio 已 725 MB）。

---

## 下一步 (按优先级)

1. **跑 buffett-perspective 全 benchmark** — `benchmark_cases.jsonl`
   至少 5 个不同类型案例，rubric 5 项打分，过 75 分门槛即正式采纳
2. **跑 expert-munger 全 benchmark** — 同上
3. **US Healthcare：L3 推进 + L1/L2 review** — 跟 China 那边 L3
   研究协议对齐，每个数据点配 source id
4. **China Healthcare：L3 验收 → 合并入"各层工作机会矩阵"** —
   `L3-v2-deep.md` 等 greenlight
5. **Howard Marks Build 路径启动** — 收集 Oaktree memo 全集，自建
   灵魂卡（5/6 测试后已确认 Fork 档不可行，直接 Build）
6. **段永平雪球 export pipeline** — 中文专属，没人做过，必须自建
7. **整理 personal/career-thesis** — `2026-05-thesis.md` 与 PBM /
   China 流通 研究产出做交叉引用
8. **决定 yunji-vam-verify 归档位置** — 留在 personal/ 还是挪到
   companies/sectors/

---

## 已知风险

- Skill 验证目前只有"我手动跑 + 主观判断"一种方式，没有自动化 rubric
  打分流水线
- benchmark 案例数量可能不足以验证灵魂的泛化能力（跨行业 / 跨周期）
- 上游 Skill 可能后续更新，需要锁定 commit / 版本号
- 会话状态 vs Skill 状态可能错位 — 同一 Claude 会话连续切换多个灵魂
  Skill 时存在隐性记忆污染
- L3 真研究方法论（每条数字带 source id）目前只跑在 China 流通这一
  个子题上，US 那边的 L1/L2 还是更松散的引用方式，下一轮要对齐

---

## 相关文档导航

- [souls_workflow.md](frameworks/souls_workflow.md) — 灵魂使用与 panel 编排规则
- [hybrid_adoption_plan.md](frameworks/agent_testing/hybrid_adoption_plan.md) — Adopt vs Build 决策
- [training_plan.md](frameworks/agent_testing/training_plan.md) — 长期训练目标
- [frameworks/agent_testing/README.md](frameworks/agent_testing/README.md) — 测试框架总览
- [companies/nbis.md](companies/nbis.md) — NBIS 简报（灵魂测试主要案例）
- [sectors/us-healthcare/行业结构与机会分析.md](sectors/us-healthcare/行业结构与机会分析.md) — 美国医疗 v1
- [sectors/us-healthcare/层2-子题-PBM拆解.md](sectors/us-healthcare/层2-子题-PBM拆解.md) — PBM L2 深度
- [sectors/china-healthcare/L3-v2-deep.md](sectors/china-healthcare/L3-v2-deep.md) — 中国流通零售 L3 真研究
- [sectors/china-healthcare/_research-plan.md](sectors/china-healthcare/_research-plan.md) — China 6+1 层方案
- [personal/README.md](personal/README.md) — personal namespace 规则
- [personal/yunji-vam-verify/verification.md](personal/yunji-vam-verify/verification.md) — 云迹对赌核查
