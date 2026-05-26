# PBM Research Notes

> 用途：所有 PBM 调研的 raw 搜索日志、原始数据、JD 抓取、insider quote 的 source of truth。
> 规则：每次 search 完毕都要 append 到 `search-log.md`，不要只在 chat 里漂。

## 结构

```
research-notes/PBM/
├── README.md                       <- 本文件
├── search-log.md                   <- 所有搜索 query + URL + key 摘录的时间线
├── failed-searches.md              <- 死胡同、找不到、被 paywall 挡的记录
├── 1A-pbm-母公司-10K-segment.md   <- Phase 1A 原始 raw
├── 1B-ftc-2nd-interim-extract.md  <- Phase 1B 原始 raw
├── 1C-analyst-views.md            <- Phase 1C 原始 raw
├── 1D-insider-quotes.md           <- Phase 1D 原始 raw
└── ...
```

## 关联输出

最终入：
- `data/sources/sources-PBM.csv` (每个 fact 一行)
- `data/analysis/*.csv` (派生计算)
- `层2-子题-PBM拆解-v2.md` (synthesis)
