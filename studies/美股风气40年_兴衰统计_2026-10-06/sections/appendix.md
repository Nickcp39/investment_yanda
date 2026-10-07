<!-- PAGEBREAK -->

## 附录 A：每年年末“过去 5 年最热的行业”（1985–2025）

{{TABLE:hot_annual}}

口径：Kenneth French 49 行业，市值加权月总回报；“相对市场” = 行业财富 ÷ 市场财富（同库 Mkt-RF + RF）；“之后排名”是之后 5 年相对表现在 49 个行业中的名次。2021 年以后的起点不满 5 年，括号里注明实际月数。

## 附录 B：规则细节

**B1 指数回撤（第 4 章）**：日收盘价格指数，1985-01 起，从前高回撤 ≥20% 记为一次。谷底取收复前的最低收盘价；“收复”指收盘价第一次回到前高。不含股息。

**B2 行业暴涨时代（第 5.2 节）**：

- 信号：某月过去 36 个月总回报 ≥2.5 倍，且相对市场 ≥2.0 倍。
- 从首个信号开始，只要上一个信号之后 24 个月内又出现新信号，就算同一个暴涨时代在延续。
- 期间一旦从顶点回撤 ≥30%，这个时代即告结束，记为“崩”。下一个时代必须从谷底之后的新信号重新开始。
- “信号月买入”检验：在首个信号月末买入，持有 60 个月，与市场对比。
- 月末总回报指数，月内的极值更深。

**B3 公司层（第 6–13 章）**：

- 峰值搜索窗口：研究员给出的公司峰值月 ±9 个月；没有给出时，用主题兴起前 6 个月到主题谷底（没有谷底时用顶点后 24 个月）。进行中的主题，取兴起以来至今的最高点。
- “收复”：拆股复权后的日收盘价**严格高于**峰值收盘价。
- “持有至今倍数”：用含股息的复权价。
- 结局：有完整 Yahoo 报价的，按价格判定“活着·曾收复高点”或“活着·未回高点”；破产、清算、退市、被收购的，按研究员给出的来源判定。研究员判为死亡、但 Yahoo 仍有场外报价的（如 Lordstown、TuSimple、Silvergate），结局按研究员判定，价格只作参考。
- 主题真实性的五档判定和兑现标志，由研究员按非股价证据给出，每条都附来源。

## 附录 C：数据问题与陷阱

**代码复用和改名**（已人工核对，研究中均已避开）：

| 情况 | 代码 |
|---|---|
| 今天的代码已经属于另一家公司 | BBBY（原 Overstock）、SI（2025 年起的新公司）、SPWR（Complete Solaria）、LAZR（ETF）、BTU / CHK / ARCH / UAL（重整后的新股权）、STX（2002 年重新上市的 Seagate，与 1980 年代旧股无关）、BIIB（Yahoo 历史是 IDEC 的）、DNA（Genentech 1999 年重新上市后的股票） |
| 改名但仍是同一股权 | FB→META、SQ→XYZ、RIMM→BB、PEIX→ALTO、MOT→MSI（2011 年拆分）、Overstock→NXH |
| 反向拆股（复权后看起来是天文数字的峰值） | Faraday Future 累计 1:1,440,000、Momentus 约 1:12,495、Canoo 1:460、AMC 1:10（另有 APE 转换）、Citigroup 1:10、AIG 1:20 |

**价格口径的人工核对**：Amazon、eBay、JDS Uniphase 的研究员峰值价用的是更早的拆股口径，换算后与 Yahoo 一致，见 `scripts/analyze_themes.py` 中的 `MANUAL_OK`。Kroger 1988 年为抵御收购派发了每股 $40 的特别现金，只复权拆股的价格会出现约 -86% 的假暴跌，因此改用含股息复权价（`USE_ADJ`）。

**收购价与峰值的口径**：没有 Yahoo 价格的被收购、清算公司，表中的“最大回撤/损失”是研究员给出的收购价或清算价值相对峰值的比例。中间隔了拆股或反向拆股的，已经换算到同一口径：Chiron 实为峰值的约 2 倍，Ariba 约 -96%，VerticalNet 约 -99.99%。CMGI、Internet Capital Group、Gensia 的口径无法核实，不给数字（`LOSS_OVERRIDE`）。

**已知的缺口**：

- 已退市公司的历史价格在 Yahoo 上基本查不到。Nikola、Fisker、SunPower、Luminar、Bed Bath & Beyond、WCI 等，峰值价按研究员来源，部分留空，不影响“死亡”这一判定。
- 研究员的网页检索配额中途用完，后半程改用 SEC EDGAR、FRED、Wikipedia 等已知网址补证。Wikipedia 来源和只能读到聚合标题的 2026 年新闻，在数据文件里标为中或低可信度。2025–2026 年的部分事件（Waymo 运营规模、个别公司 2026 年动态）属于此类。
- 篮子是人挑的。虽然按当年口径选并刻意纳入输家，仍可能偏向“后来还被记得的名字”，那些默默消失的小公司可能被低估。所以真实的死亡率大概率**高于**本报告的统计。行业层（第 5 章）不受这个问题影响，可以作为对照。
- Motorola→MSI、Lennar（2025 年分拆）等涉及拆分的公司，Yahoo 的复权未必完整反映分拆的价值，结论为低可信度。

## 附录 D：复跑

在研究目录下依次执行（Python 3.9，需要 matplotlib、reportlab；第一步只补缺，已存在的价格文件不会重抓）：

```
python -X utf8 scripts/fetch_prices.py --companies
python -X utf8 scripts/assemble_source.py
python -X utf8 scripts/analyze_industry_market.py
python -X utf8 scripts/analyze_themes.py
python -X utf8 scripts/make_figures.py
python -X utf8 scripts/build_report.py
python -X utf8 scripts/render_pdf.py
```

正文在 `sections/*.md` 中编辑，由 `scripts/assemble_source.py` 拼成 `report_source.md`，再由 `build_report.py` 把 `{{TABLE:…}}` 和 `{{AGG:…}}` 占位符替换成计算结果，生成 `report.md`。不要直接改 `report.md`。研究员的原始结果在 `data/research/`（每个时代一个 json 加一份 notes），价格原文的哈希在 `data/raw/prices/manifest.json`。研究其他截止日，请另建日期目录，不要覆盖本快照。
