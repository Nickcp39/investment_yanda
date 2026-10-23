# 标普500 / 纳指100 逐年成分股 + 涨幅数据说明

收集时间：2026-10-23

## 数据源（可追溯）

| 数据 | 来源 | 覆盖范围 | 格式 |
|---|---|---|---|
| 标普500 历史成分股 | [fja05680/sp500](https://github.com/fja05680/sp500)（《Trading Evolved》配套数据，维护至 2026-08-18） | **1996-01-02 ~ 2026-08-18**（event-driven，成分变动时记录） | `date,tickers` 逐快照 |
| 纳指100 历史成分股 | [unliftedq/index-constitution](https://github.com/unliftedq/index-constitution)（canonical ticker 规范化） | **2006-01-01 ~ 2026**（opt-in/opt-out） | `symbol,name,opt-in,opt-out` |
| ticker 变更审计 | unliftedq/index-constitution `event/us.csv` | 1999~2026 | 改名/退市/合并 |
| 个股复权价 | Yahoo Finance v8 chart API（`query1.finance.yahoo.com`，adjusted close 含分红+拆股） | 1989-01-01 ~ 至今 | `prices/<ticker>.csv`（date,adj_close） |

## 关键口径与边界（务必先读）

1. **无法精确回溯 40 年（1985）**：免费可得的 point-in-time 成分股数据的真实边界是——
   - 标普500：**1996 年起**（30 年）
   - 纳指100：**2006 年起**（20 年）
   再往前没有可靠的逐年成分股名单；用"今天的成分股硬回溯"会引入严重幸存者偏差，做冠军股回测会大幅虚高，**不建议**。

2. **标普500 名单是 event-driven**：源数据只在成分变动时记录快照，非逐日。`build_yearly_lists.py` 取「每年最早快照」作为该年年初名单（1 月无变动时回退到该年首个变动日）。

3. **ticker 复权价（adj_close）**：含分红再投资 + 拆股调整，是"总回报"口径。这正是回测需要的最真实口径。

4. **ticker 改名/退市处理**：
   - `ticker_changes_us.csv` 记录了改名（如 FB→META、PCLN→BKNG）与退市。
   - 改名 ticker 用 `fetch_retry.py` 以新 symbol 重拉（Yahoo 会保留改名前的历史在新 symbol 下）。
   - 真正退市且 Yahoo 无数据的 ticker（多为 1996-2005 的破产 Q 后缀股、被收购股）记为 `fetch_missing.txt`，回测时该股某年涨幅标记为缺失。
   - **幸存者偏差已规避**：成分股名单是 point-in-time（含后来退市/被踢出的股票），不会只留下"活到今天的大牛股"。

5. **纳指100 的 2006 起点快照**：unliftedq 用 2006-01-01 作起点快照，故 2006 年名单含 109 只（略多于 100，因含当年年内才退出的个股），属起点近似，误差有限。

## 生成的文件

- `sp500_historical_components.csv` — 标普500 逐快照名单（原始）
- `ndx100_historical_components.csv` — 纳指100 成分股（opt-in/opt-out）
- `ticker_changes_us.csv` — ticker 变更审计
- `sp500_yearly_constituents.csv` — 标普500 逐年年初名单（year,tickers,n）
- `ndx100_yearly_constituents.csv` — 纳指100 逐年年初名单
- `prices/<ticker>.csv` — 每只成分股的复权价日线
- `fetch_failed.txt` / `fetch_missing.txt` — 拉取失败/缺失清单

## 后续回测口径建议

"每年买上一年冠军股"策略：
- 候选池 = 上一年年初的 point-in-time 成分股名单（已在逐年名单中）
- 冠军判定 = 上一年度 adj_close 总回报最大者
- 持有回报 = 下一年度 adj_close 总回报
- 基准 = SPY/QQQ 总回报（含分红，用 ETF 复权价）
