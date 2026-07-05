# S&P 500 医疗/健康 筛查批次 — Career × Investment

**batch_id**: `sp500_medical_2026-07-05` · **as_of**: 2026-07-05 · **pipeline_version**: `lean-6module-v1.1` · **owner**: Nick
**状态**: IN PROGRESS

## 目的 (WHY)
筛 S&P 500 里与 Nick 职业相关(**医学影像 + 深度学习 + 中国医疗设备出海**)的医疗名。双轨:一边建域认知、一边找可投标的。每家跑一张完整 `lean-6module-v1.1` dossier(一手源 + freshness 门 + date-key 到 `companies/<ticker>/2026-07-05/`)。**5 个一批**跑,避免 agent 过载/卡死。

## ⭐ 如何续跑(会话断了/卡了,读这一段)
1. 判定某 ticker **是否已完成**:`companies/<ticker>/2026-07-05/decision_card.json` 存在 **且** `freshness_check.json` 的 `status=="PASS"` → **DONE**;否则 **PENDING**。
   一行命令查全部:`for t in <tickers>; do [ -f companies/$t/2026-07-05/freshness_check.json ] && grep -q '"status": "PASS"' companies/$t/2026-07-05/freshness_check.json && echo "$t DONE" || echo "$t PENDING"; done`
2. 取**下一批 ≤5 个 PENDING**,并行开 5 个 Runner(spec 见下)。
3. 每个开跑前**先核价**(INC-001 铁律):`python -c "import sys;sys.path.insert(0,'scripts');from market_data_download import fetch_yahoo,_retry as r;s=r(fetch_yahoo,'<T>','2026-06-20','2026-07-07');print(s[s.index<='2026-07-05'].iloc[-1])"`,把核过的价传给 Runner。
4. 一批完成后:更新下方 Status 列 + `git commit`(进度落 git = 真持久)。

## Runner spec(每个 ticker)
完整 dossier,文件集对齐 `companies/msft/2026-06-19/`:raw/(SEC 10-K/10-Q/8-K 一手)、facts.md、claim_ledger.csv、source_register.md、business_model.md、value_chain_map.md、moat_map.md、operator_underwriting.md、bottleneck_map.md、financials/financial_quality.md、inversion_map.md、valuation.md、model/scenario_model.csv、ic_panel.md、decision_card.json/.md、brief-v1.html、audit.md、completion_checker.md、research_status.md、freshness.json。
**加固**(防卡死):边做边写盘;每 URL 最多试 2 次就退备源(SEC 403 → curl+UA / stockanalysis);跑 `verify_freshness.py --dossier <path>` 到 PASS。**职业注记**:点出各家的 medical-AI/影像项目 + 中国竞争(联影/迈瑞对标)。

## 队列(26 家,5 个一批)

| 批 | ticker | 公司 | 板块 | status | 核过价 | verdict |
|---|---|---|---|---|---|---|
| 1 | MDT | Medtronic 美敦力 | 器械(综合) | PENDING | | |
| 1 | ABT | Abbott 雅培 | 器械/诊断 | PENDING | | |
| 1 | SYK | Stryker 史赛克 | 器械(骨科/手术) | PENDING | | |
| 1 | BSX | Boston Scientific 波科 | 器械(心血管) | PENDING | | |
| 1 | TMO | Thermo Fisher 赛默飞 | 生科工具 | PENDING | | |
| 2 | EW | Edwards 爱德华 | 器械(结构性心脏) | PENDING | | |
| 2 | RMD | ResMed 瑞思迈 | 器械(呼吸/睡眠) | PENDING | | |
| 2 | IDXX | Idexx | 宠物诊断 | PENDING | | |
| 2 | DXCM | Dexcom | 器械(CGM 血糖) | PENDING | | |
| 2 | ALGN | Align 隐适美 | 器械(齿科) | PENDING | | |
| 3 | PODD | Insulet | 器械(胰岛素泵) | PENDING | | |
| 3 | DHR | Danaher 丹纳赫 | 生科工具 | PENDING | | |
| 3 | A | Agilent 安捷伦 | 工具/仪器 | PENDING | | |
| 3 | MTD | Mettler-Toledo | 工具/仪器 | PENDING | | |
| 3 | WAT | Waters | 工具/仪器 | PENDING | | |
| 4 | RVTY | Revvity | 工具/诊断 | PENDING | | |
| 4 | LLY | Eli Lilly 礼来 | 药企(+AI 制药) | PENDING | | |
| 4 | MRK | Merck 默沙东 | 药企 | PENDING | | |
| 4 | ABBV | AbbVie | 药企 | PENDING | | |
| 4 | AMGN | Amgen 安进 | 生物药 | PENDING | | |
| 5 | VRTX | Vertex | 生物药(囊性纤维化) | PENDING | | |
| 5 | REGN | Regeneron | 生物药 | PENDING | | |
| 5 | UNH | UnitedHealth 联合健康 | 医疗服务/保险 | PENDING | | |
| 5 | LH | Labcorp | 诊断实验室 | PENDING | | |
| 5 | DGX | Quest Diagnostics | 诊断实验室 | PENDING | | |
| 5 | IQV | IQVIA | 医疗数据/CRO | PENDING | | |

## 已完成(勿重跑,参照)
- **GEHC** 2026-07-04 WATCH · **TEM** 2026-07-04 STARTER(小) · **BFLY** 2026-07-04 WATCH · **ISRG** 2026-07-02 STARTER
- **Mega7**(AAPL/MSFT/GOOGL/AMZN/NVDA/META/TSLA)已在书里 —— 且都有重磅医疗 AI 项目(NVDA Clara、MSFT Nuance、GOOGL Verily/Isomorphic、AMZN Health、AAPL Health)

## 变更日志
- 2026-07-05 建队列(26 家),batch 1 (MDT/ABT/SYK/BSX/TMO) 启动。
