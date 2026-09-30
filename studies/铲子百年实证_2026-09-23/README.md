# 铲子百年实证 · 深研重写版

先读 [完整研究](report.md) 或 [22 页 PDF](../../output/pdf/铲子百年实证_深研版_2026-09-23.pdf)。本版按用户要求重新补充研究，正文包括百年行业检验、八组经营案例和 AI 电力映射；第一轮审计移入附录。六张数据图，41 个直接来源链接，另附 41 家候选证券的完整计算表。

百年部分：French 官方 49 行业中的五个上游相关行业及公用事业对照，1926-07 至 2026-07，共 1,201 个月；同期美国市场基准，十个时期、91 个年度起点十年窗口及权重/起点敏感性。它是美国行业代理组合，不是全球纯上游因果面板。

现代部分：41 家候选，40 家取得价格，APTV 隔离、SPR 缺失；同月美元、复权 SPY 对照。原始 `data/shovel_prices.json` 保持不变。供应商复权与复杂公司行动仍有审核边界。

证据与附表：[直接来源索引](source_index.md)、[行业附表](industry_appendix.md)、[现代收益表](returns_appendix.md)、[数据审计](DATA_AUDIT.md)、[前轮主张台账](claim_ledger.md)。`archive/v1/` 保留原稿，`archive/v2_audit/` 保留被用户指出深度不足的审计稿；两者均非当前主报告。

## 复跑

从仓库根目录，在PowerShell执行（已用本仓库现有Python环境跑通）：

```powershell
.\.venv\Scripts\python.exe -X utf8 'studies\铲子百年实证_2026-09-23\scripts\analyze_industry.py'
.\.venv\Scripts\python.exe -X utf8 'studies\铲子百年实证_2026-09-23\scripts\build_research_tables.py'
.\.venv\Scripts\python.exe -X utf8 'studies\铲子百年实证_2026-09-23\scripts\rebuild_analysis.py'
.\.venv\Scripts\python.exe -X utf8 'studies\铲子百年实证_2026-09-23\scripts\build_report.py'
.\.venv\Scripts\python.exe -X utf8 'studies\铲子百年实证_2026-09-23\scripts\verify_results.py'
```

分析不访问网络，使用保存的原始响应生成 JSON、附表和图。标准库负责数据处理；图需 matplotlib。编辑正文用 `report_source.md`，由 `build_report.py` 填入计算表；不要只改生成的 report.md。

PDF 用包含 ReportLab、pypdf、pdfplumber 的 Python 执行 `scripts/render_pdf.py`，随后执行 `scripts/verify_research.py`。本机使用 Codex bundled Python：`C:\Users\nickc\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`。中文字体来自 Windows YaHei。PDF 输出到仓库 `output/pdf/`。正文中的财报链接在 PDF 中可点击，主章节有书签。

补采缺少的价格文件才运行 `scripts/fetch_audit_data.py`。已存在文件使用缓存，避免悄悄把本次快照变成另一天的数据；要研究新的截止日期，请另建快照目录并修改明确的截止参数，不直接覆盖原研究。抓取脚本的截止时间为2026-09-24 UTC，分析只取至2026-08完整月。SPR失败保留失败状态，不补零。

`scripts/fetch_data.py`、`scripts/analyze.py`、`scripts/gen_chart.py` 保留为兼容入口，转向新版流程。旧图入口文件显示停用提示。

## 验收边界

`data/verification.json` 核对现代序列哈希、端点、公式、异常隔离与链接；`data/research_verification.json` 从行业原始文件独立乘积复算年化、回撤、全部十年窗口，并检查 PDF 文本边界和来源链接。另已使用 Poppler 渲染逐页查看。公式与排版验收不验证“铲子必胜”等因果命题，也不替代退市、分拆及配股现金流重建。
