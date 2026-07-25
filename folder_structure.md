# 项目文件夹结构 (Folder Structure)

> **给 AI / 新会话的导读**：这是一个投资研究 lab（分析层，不下单）。
> 读这一份 + `current_process.md` 就能定位任何工作，**不要全仓扫描**——
> `sources/`、`notes/`、`logs/` 是海量原始素材，按需检索即可。
>
> 最后更新: 2026-07-25 · 结构变动时同步更新本文件

## 快速入口（按优先级）

| 文件 | 用途 |
|---|---|
| `README.md` | 仓库定位与边界（分析层，不做执行） |
| `current_process.md` | **当前进度快照**：上次干了啥、下一步是啥 |
| `folder_structure.md` | 本文件：目录地图 |
| `research_queue.md` | 研究选题队列 |

## 目录地图

### 研究产出层（核心，优先读）

```
companies/            个股研究档案（最大目录，~30 个 ticker）
├── <ticker>/<日期>/     每次研究 = 一个日期快照文件夹（dossier 格式，见下）
├── _company_research_template/   dossier 模板
└── _<批次名>_<日期>/    批量研究的计划与汇总（如 _sp500_medical_2026-07-05、
                         _ai_robotics_2026-07-10、_mega7_2026-06-19）

sectors/              行业研究
├── us-healthcare/       美国医疗（PBM 深度，L1/L2 分层调研）
├── china-healthcare/    中国医疗（流通/零售 L3 真研究，每个数字带 source id）
└── medical/             医疗行业横向

studies/              专题研究（跨行业/跨资产）
├── jp_cn_relative_timeline/  中日相对时间轴系列（以房价见顶为 T=0 对比
│                             产业政策/思潮：自动化、半导体、汽车、医疗）
└── wealth_rankings/          福布斯富豪榜三快照（2008/2015/2025）利润池迁移

macro/                宏观（hyperscaler capex、存储周期、美日收益率曲线等）
theses/               市场地图与投资论文（2026-market-map.md 等）
execution_plans/      具体标的的投资执行计划（BTC、MSFT，md + html 双格式）
backtests/            回测与 pipeline 时点测试（asof_<日期>_*）
career-thesis/        职业方向论文（AI+Healthcare）
personal/             个人 namespace（职业 thesis、决策日志；规则见其 README）
```

### 方法论层

```
frameworks/           研究方法论与"灵魂"体系
├── buffett/ munger/ duan-yongping/   投资人灵魂卡与一手材料
├── agent_testing/       灵魂 Skill 的 Adopt/Build 测试框架
├── *_pipeline*.md       研究流程（选题→L1/L2/L3→checker→decision）
└── research_completion_checker.md    产出验收清单
```

### 原始素材层（海量，只按需检索，不要全读）

```
sources/              一手素材归档
├── channels/            YouTube/Bilibili 频道索引与元数据（tradesmax 等）
├── videos/              视频转录文本
├── news/wechat_mp/      微信公众号文章存档（含 dashboard.html + manifest）
└── papers/              论文/报告

notes/videos/         逐条视频笔记（数百个 md，文件名 = 日期_视频ID_标题）
data/                 行情快照 CSV/JSON（asof_<日期>_<ticker>_quotes）
logs/                 采集脚本运行日志
```

### 工具层

```
scripts/              Python 脚本
├── log_trend_*.py / rolling_log_trend_*.py   对数趋势通道与 DCA 回测系列
├── channel_video_index.py / *_queue.py       频道采集三件套（索引/元数据/ASR）
├── wechat_mp_*.py                            公众号采集与 dashboard
├── verify_freshness.py                       dossier 数据新鲜度校验
├── agents/                                   agent 相关脚本
└── _archive/                                 弃用脚本

notebooks/            Jupyter 分析
.claude/skills/       本仓库自定义 Claude skills
```

## 关键约定

1. **公司 dossier 格式**（`companies/<ticker>/<日期>/`）：标准件包括
   `plan.md` → `facts.md` / `business_model.md` / `moat_map.md` /
   `valuation.md` → `decision_card.md`(+json，含 STARTER/WATCH 等裁决) +
   `completion_checker.md` + `freshness*.json`（数据新鲜度）+
   `source_register.md`（出处登记）。**看结论先读 decision_card.md。**
2. **批次研究**：多标的一起做时，计划和汇总放 `companies/_<批次>_<日期>/`，
   个股产出仍归各自 ticker 目录。
3. **真研究标准**：L3 级研究每个数据点带 source id + URL + 日期
   （协议见 `sectors/china-healthcare/`），推算值单独标注。
4. **重素材不入库**：audio/、transcripts/ 原始音频等已 gitignore。
5. **临时文件**：根目录 `tmp_*.png` 为采集过程截图，可忽略。
6. **双语**：中文为主，代码与部分框架英文。

## 各目录"值不值得读"速查

| 想干什么 | 去哪里 |
|---|---|
| 了解某公司的最新结论 | `companies/<ticker>/` 最新日期的 `decision_card.md` |
| 了解当前整体仓位思路 | `theses/2026-market-map.md` + `execution_plans/` |
| 接着上次的活干 | `current_process.md` |
| 找研究方法/流程 | `frameworks/investment_research_pipeline_detailed.md` |
| 找某条新闻/视频原文 | `sources/` 按文件名 grep，别遍历 |
| 跑数据/回测 | `scripts/` + `data/` |
