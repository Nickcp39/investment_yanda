# 买方研究 Pipeline — START HERE

这个文件夹 = **精简 6 模块买方研究 pipeline 的「canonical 规范 + 验证机器」**。
新 AI / 下次开工,**从这份 README 进**,别直接乱翻十几个 md。

> 文件夹名叫 `backtests/framework_validation/` 是历史原因——它装的不只是回测,而是
> **这条 pipeline 的规范本身** + 它的盲回测验证集。

## 现在的状态(一句话)
- 当前版本 **`lean-6module-v1`**(见 `VERSIONS.md`;每张决策卡必盖版本号)。
- 已用 **10 个已知结局的历史案例盲测验证 → 9 PASS / 1 FAIL**(见 `SCORECARD_v1.html`)。
- 2 个改进待验证(`PATCH_LEDGER.md`,目前 **INACTIVE**,不改现行行为)。

## 我想…(选一条)
| 你要做的 | 去读 |
|---|---|
| **分析一个新公司、出买入决策** | **`USER_MANUAL.md` → A 节**(含一键 kickoff prompt) |
| 理解整条 pipeline 的流程/模块 | `PIPELINE.md` |
| 跑 / 扩展盲回测 | `USER_MANUAL.md → B 节` + `TEST_PLAN.md` |
| 看验证结果 | `SCORECARD_v1.html` · `results.csv` · `cases/CASE_INDEX.md` |
| 改框架(加补丁) | `PATCH_LEDGER.md`(防过拟合的规矩在里面) |

## 文档地图(每份一句话)
| 文件 | 是什么 | 类型 |
|---|---|---|
| `PIPELINE.md` | 端到端流程总览(先建立全局观) | 总览 |
| `USER_MANUAL.md` | 怎么实际跑(实盘新公司 + 回测) | HOWTO |
| `PROTOCOL.md` | 6 模块定义 + `decision_card` schema + agent 角色 | 规范 ★ |
| `COMPANY_MATERIAL_TEMPLATE.md` | 每个 case 产出哪些文件(P0/P1/P2) | 规范 ★ |
| `WEIGHTING_HARNESS.md` | 信号怎么聚合成仓位 + 情景门控 + 否决规则 | 规范 ★ |
| `METHODOLOGY.md` | 仓位阶梯 / 现金 / 卖出触发 / 耐久天花板 | 规范 ★ |
| `../../companies/_operator_underwriting_template.md` | 创始人/操作者生命弧 dossier | 规范 ★ |
| `VERSIONS.md` | 版本注册表(单一真相源) | 治理 |
| `PATCH_LEDGER.md` | 待验证的框架改动(防过拟合) | 治理 |
| `LOOKAHEAD_CHECKER.md` | 回测防穿越闸门 + 各 case 禁项注册表 | 回测专用 |
| `MATERIAL_COLLECTION_PLAN.md` | 某批回测材料采集计划 | 回测专用(历史) |
| `TEST_PLAN.md` | 盲回测顺序执行协议 | 回测专用 |
| `cases/` | 13 个 case(材料 + 决策 + 评分)+ `CASE_INDEX.md` | 数据 |
| `results.csv` | 评分总账(每个 scored case 一行) | 数据 |
| `SCORECARD_v1.html` · `experiment_design.html` | 结果记分卡 / 交互流程图 | 结果 |

★ = canonical 规范,**实盘和回测共用同一套**。

## 模板:用哪个?(这是以前最容易走岔的地方)
- **Canonical = 精简 6 模块** → 本文件夹 `COMPANY_MATERIAL_TEMPLATE.md`,产出 `decision_card.json`。**新公司用这个。**
- **Legacy = 10 层老模板** → `companies/_company_research_template/`,产出 `memo-v1.md`。
  10 层已被 6 模块吸收(映射见 `PIPELINE.md` 末尾),保留作参考/深研,**新公司不要从它起**。

## 小提醒
个别规范文件头部还写着 `Status: DESIGN - NOT YET RUN`——**已过时**,v1 已跑过 10 案并验证。
以 `VERSIONS.md` + `SCORECARD_v1.html` 为准。
