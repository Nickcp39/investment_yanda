# MSFT Research Status — as_of 2026-07-28 (mega7_2026-07-28 re-run)

**Type**: FOCUSED REFRESH of the 2026-06-19 lean-6module-v1 dossier (business baseline carried; M4/M5/M6 recomputed at today's price + current regime). NOT a from-scratch rebuild.
**Pipeline**: `lean-6module-v1` · weights `none` · run_date `2026-07-28` · as_of `2026-07-28`.

Decision question (unchanged): 微软在 AI-capex 大周期下是否仍是十年级别高质量复利机?capex 恐慌 de-rate 后的当前价 $393.35 是否有足够安全边际可建仓?

## 真实状态标签: `DECISION_DRAFT` (非 COMPLETE)
- completeness **~63%**(carry 6/19 的 ~65%,O3 略收窄但 Q3 数据更旧 + 收敛缺口的 Q4/10-K 未落地)
- ceiling = **STARTER**(完整度 + O2/O3/O4 信息缺口封顶,**非价格**;价格端仍有正 MOS ~10%)
- **Verdict**: new_money **STARTER**(init 3% / max 9%);existing **HOLD**;buy_below **$436**

> 诚实声明(铁律5):本轮**未达 COMPLETE**,是财报前夜的决策草案。**不使用"完成/彻底跑完/full research complete"语言。**

## 本轮做了什么(focused refresh)
| 模块 | 动作 | 结果 |
|---|---|---|
| M1 证据 | 三源重验现价 $393.35(Yahoo+stockanalysis+websearch,0.0% delta) | 无价格 bug;完整度 ~63% |
| M2 主题 | 快速复核,扫 6/19 后新闻 | **无 thesis-break**;OpenAI $250B Azure 承诺强化需求腿 |
| M3 护城河/operator | 快速复核 | 原样 carry(+2 / operator 5/5,一股一票) |
| M4 财务现实 | **查 Q4 FY26 是否已出** | **未出**——定 2026-07-29 盘后(as_of 后 1 天)。最新一手仍 Q3 FY26 + FY25 10-K;仅并入 Q4 **指引**。owner-earnings 读数 carry |
| M5 反演 | 叠加 regime | +K-F(需求裂缝/capex 审计);内存降价对 MSFT 是**成本顺风**非威胁 |
| M6 定价 | 现价 $393.35 重算 | base IRR ~9.1%(>8%),MOS ~10%(变薄);M6 +1,但二元事件在即 → 初始收到 3%、建议分批 |

## 关键事实(本轮定盘)
- 现价 **$393.35**(2026-07-28 close),市值 ~**$2.922T**,P/E ~23.3×,base 10y IRR **~9.1%**,MOS 到 $436 ~**10%**。
- **MSFT 尚未发 Q4 FY2026 财报**;7/29 盘后发布 + 10-K,同日 FOMC/Warsh = **双重二元事件在 24h 后**。
- 无 6/19 后的 thesis-breaking 事件;OpenAI 4/27 重组 + $250B Azure 承诺收窄(未闭合)O3。
- Regime:半导体暴跌 / capex-审计年 / CXMT。MSFT 是内存**买方**(成本顺风)+ 轮动相对受益方,同时是 capex-审计直接靶子。

## Verdict 上限核验(audit 硬规则)
- completeness ~63% → 落 60-80% 区间 → **ceiling = STARTER**(铁律2)。**不可上 CORE**(需 >80% + 补 O2/O3/O4)。
- size 与耐久性匹配:exceptional + 一股一票 → 天花板 9%;但本轮初始收到 3%(价薄 + 二元 + regime)。

## freshness gate — **PASS**
- `freshness.json` manifest 已建(price/mcap/52wk/shares/guidance/litigation,每字段 ≥2 源)。
- `python scripts/verify_freshness.py --dossier companies/msft/2026-07-28` 已跑 → **status=PASS(exit 0)**,产物 `freshness_check.json` / `.txt`。
- 明细:price 三源 0.0% 一致(refetch $393.35 精确匹配);T1 band ✅ / T2 hug ✅(+12.6% off low, −29.2% off high)/ T3 mcap identity ✅(0.00%)/ T4 距高点对账 ✅(gap 0.0pt)/ T5 single-value ✅ / T6 guidance+litigation ✅。

## 仍未过的 gate(why not COMPLETE)
- B/D 区:O2 capex 维护/成长拆分(→ OE 区间 $73-125B 仍宽,base $112B 是假设)、O3 OpenAI 经济学/margin(需求侧已量化,拆分仍缺)、O4 分部利润率——**均待 7/29 Q4 + 10-K 收敛**。
- 时点缺口:收敛以上缺口的最大事件(Q4 + 10-K)在 as_of 后 1 天,尚未在手。

## Next Review(硬触发)
- **2026-07-29 盘后 Q4 FY26 + 10-K**:FY26 全年 capex 是否坐实 ~$190B、capex/OCF、维护/成长拆分、Azure Q4 实际 vs +39-40% 指引、**FY27 指引**、OpenAI 口径 → 可能触发 memo v2(re-open panel)。
- **2026-07-29 FOMC/Warsh**:利率/久期倍数风险。
- 价格触发:>$436 no-chase(丧失 MOS);<$363 趋 $303 加仓评估;K-A~K-F 任一转红 → 立即重审。
