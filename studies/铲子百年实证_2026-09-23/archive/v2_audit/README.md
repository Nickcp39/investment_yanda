# 铲子百年研究 · 重建版

先读 [report.md](report.md)，再按需要查看 [数据审计](DATA_AUDIT.md)、[完整收益表](returns_appendix.md)、[证据台账](claim_ledger.md)和[母报告§19替换稿](section19_replacement.md)。原版与手填图保存在 `archive/v1/`，仅用于追踪错误，不作为当前结论。

本次为41家候选的现代描述性收益及跨时代案例重建。40家取得价格，APTV隔离、SPR缺失；不是完整百年回报数据库。原始 `data/shovel_prices.json` 保持不变。

## 复跑

从仓库根目录，在PowerShell执行（已用本仓库现有Python环境跑通）：

```powershell
.\.venv\Scripts\python.exe 'studies\铲子百年实证_2026-09-23\scripts\rebuild_analysis.py'
.\.venv\Scripts\python.exe 'studies\铲子百年实证_2026-09-23\scripts\verify_results.py'
```

分析不访问网络，使用保存的原始响应生成JSON、附表和两张图。标准库负责数据处理；图需matplotlib。

补采缺少的价格文件才运行 `scripts/fetch_audit_data.py`。已存在文件使用缓存，避免悄悄把本次快照变成另一天的数据；要研究新的截止日期，请另建快照目录并修改明确的截止参数，不直接覆盖原研究。抓取脚本的截止时间为2026-09-24 UTC，分析只取至2026-08完整月。SPR失败保留失败状态，不补零。

`scripts/fetch_data.py`、`scripts/analyze.py`、`scripts/gen_chart.py` 保留为兼容入口，转向新版流程。旧图入口文件显示停用提示。

## 验收边界

`data/verification.json` 核对哈希、币种、端点、公式、异常隔离与链接，不验证“铲子必胜”等投资命题。原始供应商复权、复杂公司行动、缺失退出者、历史时点分类及规范化经营面板仍有限制。报告明确列出了这些缺口。
