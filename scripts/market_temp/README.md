# 市场体温流水线 `scripts/market_temp` · 2026-10-23

一键回答「QQQ 现在在哪、在不在水下、整体过热还是过冷」。把 10-08（QQQ 高不高）、10-11（市场体温计 25 指标 + 四把尺子）、10-12（GDP 基准线、巨头占比）三份研究里每次手工跑的东西固化成一条流水线：**取数 → 计算 → 出表出图 → 记日志 →（可选）AI 补充**。数字永远由 Python 算；AI 只负责解释行情、补抓不到的数据、写解读。

## 怎么用

| 方式 | 命令 | 说明 |
|---|---|---|
| 双击 | 仓库根目录 `run_market_temp.bat` | 取数 + 计算 + 打开 `dashboard.png` 与 `temp.md`，约 25 秒 |
| 双击 + AI | `run_market_temp_ai.bat` | 同上，然后 `claude -p`（sonnet，预算 3 美元）写 `ai_notes.md` |
| 命令行 | `python scripts/market_temp/run.py` | 参数：`--no-fetch` 用缓存 · `--pdf` 出 PDF · `--as-of 2026-10-09` 回看某天（写到 `_backfill/`）· `--ai --model sonnet --budget 3` |
| Claude Code 会话 | `/market-temp` | 项目级 skill（`.claude/skills/market-temp/SKILL.md`）：跑脚本，然后在会话里用搜索/浏览器做 AI 三件事 |

## 输出（`output/market_temp/`）

```
<as_of>/temp.md        一页结论 + 9 节：QQQ 位置、四把尺子、σ 通道、GDP 线、集中度、25 指标、一次性 vs 分批、和上一轮比、数据新鲜度
<as_of>/dashboard.png  六图：四把尺子 / QQQ 回撤 / 25 指标热度条 / 前瞻 PE / 2010 起 σ 通道 / QQQ vs GDP 线
<as_of>/temp.json      全部数值（给 AI 和后续脚本读）
<as_of>/gauges.csv     25 指标 × 现值、四个基准分位、三顶三底读数、热度（与 10-11 研究同列）
<as_of>/needs_ai.json  抓取失败或过期的数据项清单
<as_of>/ai_notes.md    AI 步骤写入（--ai 或 /market-temp）
<as_of>/run_log.txt    本次运行日志
history.csv            每个 as_of 一行的体温日志（31 列），画趋势读这个
LATEST.txt             最新目录名（.bat 用）
_backfill/<date>/      --as-of 回看结果，不动 LATEST 和 history
```

as_of = 最后一个**已收盘**交易日（Yahoo 盘中行会被丢掉）。同一 as_of 重跑覆盖同一目录；带日期目录不回头改。

## 算什么（口径与三份研究一致）

- **25 个指标**（价格 8 / 估值 4 / 经济 6 / 流动性 3 / 黄金 4）：每个给 1980 起、2009 底起、2016 底起、2022 底起四个基准的分位（= 该基准内比现值低的历史占比），以及 2007/2015/2021 三个顶和 2009/2016/2022 三个底当天的读数。热度 = 1980 起分位，"低 = 热"的指标（失业率、Sahm、曲线、Fed 模型差、VIX）取 100 − 分位。节点日期由数据在固定窗口内 argmax/argmin 得出。
- **四把尺子**：纳指100 与标普500 分别从 2002/2008-09/2016/2022 四个周期底部起算的对数趋势线，日历年为 t，公式 `P = a × (1+g)^t`，给现偏离、时代内分位、10–90 分位区间、回到线上需跌多少、隐含 1/3/5 年点位。与 10-11 报告 `panel_fits.json` 同法。
- **QQQ 位置**：距历史最高与"历史上多少交易日回撤比今天深"、52 周高低、50/200 日线、1/3/5/10 年总回报及 1999 起分位、QQQ/SPY 比值偏离、60 日实现波动率。与 10-08 `analyze.py` 同法。
- **σ 通道**：`execution_plans/equity_index_plan_2026-08-07.md` §3 的翻倍线：2010-01-04 起含分红对数趋势，σ = 对数残差标准差，给现位置和 −1σ 价位（与 `scripts/log_trend_channel.py` "full" 窗口同法）。
- **GDP 基准线**：锚点 2010-01-04 与 2020-01-02；L1 = 名义 GDP 线，L3 = L1 × (1+溢价)^t，溢价 = 1990 到上一完整年的标普 EPS 年化 − 名义 GDP 年化（名义 EPS = 价格 ÷ multpl PE）。BEA 季度之后按最近四季增速外推并在报告里注明季度数。
- **集中度**：QQQ / SPY 第一大、英伟达、前三、前十权重（stockanalysis 持仓表）。
- **一次性 vs 分批**：按今天纳指相对 2008 底起趋势线的时代分位，从 `backtests/QQQ_定投vs一次性_2026-10-11/summary.csv` 取对应起点组的历史结果。

## 数据源与兜底（`data/market_temp/manifest.json`）

| 数据 | 来源 | 本机状态 2026-10-23 | 兜底 |
|---|---|---|---|
| 13 条日频行情 | Yahoo v8 chart | 通 | 失败则留上次缓存 |
| CPI-U、失业率 | BLS API v1（无 key，每日 25 次） | 通 | 首次用 10-11 研究缓存 |
| 纳指100 前瞻 PE | historyofmarket.com `/api/ndx/forward-pe.json`（CC BY 4.0） | 通 | 周频一致预期到 2026-08-05，之后接该站自算的日频 dl-blended FY1/FY2（接续日 22.37 vs 22.41）；滚动 PE 同源 |
| CAPE、标普 PE | multpl.com 月表（顶部几行是 multpl 估计值，已含） | 通 | 首次用缓存 |
| M2 | FRED fredgraph | **超时（本机一直不通）** | 用 `黄金_货币供应_估值_2026-08-07` 缓存（到 2026-07），列入 AI 待补 |
| GDP | BEA `gdplev.xlsx`（停在 2025Q1）→ 过期则读 `NipaDataQ.txt` 平面文件（35 MB，A191RC/A191RX，到 2026Q2） | 通 | 年度值 = 四季平均 |
| 黄金 | LBMA PM | **403** | 用缓存到 2026-09-08，之后接 COMEX GC=F，报告注明接续价差 |
| QQQ/SPY 持仓 | stockanalysis.com（需浏览器 UA） | 通 | 首次用 10-12 研究缓存 |

过期阈值：行情 5 天、BLS 60、前瞻 PE 14、CAPE/PE 45、M2 60、GDP 120、黄金 10、持仓 30。超阈值或失败的项进 `needs_ai.json`，AI 步骤逐项去找并写明来源，**不改缓存**。

## 核对（2026-10-23 用 `--as-of 2026-10-09` 回算，对照 10-11 研究 `gauges.csv`）

8 个价格指标、4 个黄金指标、M2、VIX、DXY、失业率、Sahm、曲线共 20 项现值与分位**完全一致**（如 标普偏离 1980 起趋势线 33.70 / 89.01 分位）。有差异的 5 项都是数据源在两周里变了：CAPE 41.80→40.81 与滚动 PE 25.22→26.29（multpl 改了当月行并新增估计行）、前瞻 PE 22.37→21.51（周频一致预期后接日频）、CPI 同比 3.69→4.00（9 月 CPI 已发布；回看按数据期截断，不按发布日）、Fed 模型差随 PE 变。四把尺子的拟合参数（a、g）与 `panel_fits.json` 一致。

## AI 步骤（`ai_update.py`）

`claude -p` 无头调用，stdin 传提示词，`--permission-mode acceptEdits --allowedTools WebFetch WebSearch Read Write Glob Grep Edit --max-budget-usd 3 --max-turns 30 --output-format json`。只允许新建/覆盖 `<as_of>/ai_notes.md`，内容三节：近两周为什么动（带来源）、数据补齐表、读数怎么读。调用结果（花费、轮数）记在 `ai_run.json`。CLI 的查找顺序：环境变量 `MARKET_TEMP_CLAUDE` → PATH → `%APPDATA%
pm
ode_modules\@anthropic-ai\claude-codein\claude.exe` → `~/.local/bin`；都找不到时日志写 `claude CLI not found` 并跳过（装法 `npm i -g @anthropic-ai/claude-code`）。在 Claude Code 会话里更推荐直接 `/market-temp`，不用额外付费进程。

## 已知边界

- 回看（`--as-of`）按数据日期截断，不是"当时能看到什么"：月度数据会提前一个月可见。
- 多头/空头都不在这里判断；这是体温计，不是信号。BUY 规则看 `trading-desk/discipline.md`。
- CPython 3.9：长中文模板放在 `report_template.md` 由 `render.py` 以 f-string eval，不要搬进 .py。
