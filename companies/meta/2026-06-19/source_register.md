# META Source Register — as_of 2026-06-19

每来源: source_id · 名 · 公开/取数日期 · link/path · tier（A1/A2/B1/B2/C2/D1/E1，见 sources/source_policy.md）

| source_id | 来源 | 公开日期 | retrieved | tier | link/path |
|---|---|---|---|---|---|
| S001 | META Q1 2026 8-K 新闻稿 EX-99.1（quarter ended 2026-03-31）| 2026-04-29 | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028364/meta-03312026xexhibit991.htm （本地 raw/_meta_pr_q1_2026.html）|
| S002 | META Q1 2026 10-Q（period ended 2026-03-31）| 2026-04-29 | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/0001326801/000162828026028526/meta-20260331.htm |
| S003 | META FY2025 Q4/全年 8-K 新闻稿（year ended 2025-12-31）| 2026-01(approx) | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003832/meta-12312025xexhibit991.htm |
| S004 | META FY2025 10-K（year ended 2025-12-31）| 2026-02(approx) | 2026-06-19 | A1 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm |
| S005 | Yahoo chart API META 日频价格序列 | 2026-06-18(最新close) | 2026-06-19 | B1(行情聚合) | https://query2.finance.yahoo.com/v8/finance/chart/META |
| S006 | META DEF 14A 2026 proxy（治理/双层股权/董事会）| 2026-04(approx) | 2026-06-19 | A1 | SEC EDGAR DEF 14A 2026（治理事实经多源二手核对，proxy 全文未逐行重取）|
| S007 | Reuters/Yahoo/财经媒体 二手报道（Q1 2026 + 2026 AGM 结果）| 2026-04/05 | 2026-06-19 | B1 | finance.yahoo.com / variety.com（仅辅助/语境，载荷数回挂 A1）|
| S008 | RL 全年损失二手聚合（Auganix 报道 FY2025 RL 营业损失 $19.19B / 营收 $2.21B）| 2026-01 | 2026-06-19 | B2 | https://www.auganix.org/xr-news-meta-reality-labs-2025-financial-report/（待 10-K 逐行核，量级与 Q1 $4.0B/季一致）|
| S009 | META 2022-11-10 历史盲测案 decision_card | 2022-11-10 | 2026-06-19 | (先验) | backtests/framework_validation/cases/meta_2022-11-10/（仅 thesis 先验/对照，历史价格事实不当当前）|
| S010 | NPR/CBS 报道: Boasberg(DDC) 判 META 非垄断、不强制拆 IG/WhatsApp（FTC 反垄断案）| 2025-11-18 | 2026-06-21 | B1（LIVE-qualitative）| https://www.npr.org/2025/11/18/nx-s1-5495626/meta-ftc-instagram-whatsapp-antitrust-ruling |
| S011 | CNBC/Law360 报道: FTC 上诉 DC Circuit（2026-01）+ 24+ 州 AG 加入（2026-06-01）| 2026-06-01 | 2026-06-21 | B1（LIVE-qualitative）| https://www.cnbc.com/amp/2026/01/20/ftc-appeals-metaruling-antitrust-instagram-whatsapp.html ; "States Back FTC's DC Circ. Appeal In Meta Monopoly Case" (Law360) |

## Tier 纪律备注
- **载荷性当前事实（Q1 2026 锚定季度 + FY2025 基线）全部回挂 A1**（S001–S004，SEC 直取，curl + SEC-compliant UA）。
- 价格走 S005（Yahoo chart query2 host，repo 既定来源，Stooq 已失效）；行情属 B1 聚合，52wk high $796.25 / low $520.26，末收盘 $577.22（2026-06-18，≤ as_of）。
- 治理事实（Zuckerberg ~61% voting power、controlled company、双层股权 10:1）经多源 B1/B2 一致核对 + 2022 proxy 先验；proxy 全文未逐行重取 → 精确持股 % 与最新薪酬标 OPEN，用可考的一般性事实，不杜撰数字。
- S008（RL 全年损失）为 B2，量级与 Q1 一手 $4.028B/季高度一致，作辅助；FY2025 RL 全年损失逐行待 10-K（O2）。
- 无 D1 社媒进入 EVIDENCE。
