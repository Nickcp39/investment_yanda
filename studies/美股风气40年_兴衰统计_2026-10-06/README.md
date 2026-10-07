# 美股风气四十年 · 兴衰、存活与用时统计（2026-10-06）

先读 [56 页 PDF](美股风气40年_兴衰统计_2026-10-06.pdf) 或 [report.md](report.md)。

**问题**（用户 2026-10-06）：做一份 40 年美股投资风气转换的统计，写清当年的兴衰：哪些活下来了，哪些是真的，哪些灭亡了，各用了多长时间。

**三层证据**

| 层 | 数据 | 产出 |
|---|---|---|
| 市场 | Yahoo 日线 ^IXIC / ^GSPC / ^NDX，FRED 联邦基金利率 | `data/market_drawdowns.json`，图 1 |
| 行业（无幸存者偏差） | Kenneth French 49 行业月度（复制自 `studies/铲子百年实证_2026-09-23/data/industry_raw`，CRSP 202607） | `data/industry_fads.json`，图 3、图 4 |
| 主题 / 公司 | 7 个时代研究员按 `data/research/BRIEF.md` 统一口径整理：42 个风气、326 个上市明星席位（291 家公司），每条带来源；有价格的用 Yahoo 日线重算 | `data/research/e*.json` + notes，`data/themes_computed.json`，`data/companies_table.csv`，图 2、5、6、7 |

**主要结论**：已结束的 278 个明星席位中，死亡 24%、被收购 19%、活着但没回到高点 30%、曾收复高点 26%；今天有价格可查的 155 个幸存席位里，只有 50 个现价高于当年峰值。回撤超过 95% 的幸存者，只有 14% 收复过高点，中位用时 14.5 年。大多数风气的主题是真的（被判“基本是炒作”的只有 5 个），但最常见的结局是“真实，但利润没留给当年的股东”。

**复跑**（研究目录下，Python 3.9 + matplotlib + reportlab）：

```
python -X utf8 scripts/fetch_prices.py --companies
python -X utf8 scripts/analyze_industry_market.py
python -X utf8 scripts/analyze_themes.py
python -X utf8 scripts/make_figures.py
python -X utf8 scripts/assemble_source.py
python -X utf8 scripts/build_report.py
python -X utf8 scripts/render_pdf.py
python -X utf8 scripts/verify_report.py
```

正文在 `sections/*.md` 中编辑；表格和汇总数字由 `{{TABLE:…}}` / `{{AGG:…}}` 等占位符从数据生成，不要直接改 `report.md`。`fetch_prices.py` 只补缺，不会覆盖已有价格文件；研究新的截止日请另建日期目录。

**自检**：`scripts/verify_report.py` 用独立代码路径从原始价格重算关键收复用时（纳指 15.1 年、Cisco 25.7 年、Intel 25.6 年等），并检查占位符、主题表、来源链接（729 个）和 PDF 书签，结果在 `data/verification.json`。

**已知边界**：篮子由人挑，虽按当年口径并刻意纳入输家，真实死亡率大概率高于统计；已退市公司的峰值价部分缺失；部分 2025–26 年事件只有二手或聚合来源（数据文件中标为中/低可信度）。人工核对过的口径例外在 `scripts/analyze_themes.py` 的 `MANUAL_OK`、`USE_ADJ`、`LOSS_OVERRIDE` 中，并在 PDF 附录 C 说明。不构成投资建议。
