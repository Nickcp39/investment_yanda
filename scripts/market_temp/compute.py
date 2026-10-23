#!/usr/bin/env python
"""Compute layer: turns the cache in data/market_temp/ into the gauge table + a stats dict.

Methods are copied from the 2026-10 studies so the readings reconcile with those PDFs:
  * percentile  = share of history (within a base) strictly below the current reading
  * heat        = percentile in the 1980 base, flipped when "low = hot"
  * trend_idx   = log-linear trend on trading-day index (1980 S&P / 1985 NDX gauges, as build_temperature.py)
  * fit_era     = log-linear trend on calendar years from a cycle trough (four rulers, as build_panels.py)
  * nodes       = three peaks / three troughs found by argmax/argmin in fixed windows
  * GDP lines   = BEA quarterly, extrapolated at trailing 4-quarter growth, log-interpolated daily;
                  L1 = nominal GDP, L3 = L1 x (1+premium)^t with premium = S&P EPS CAGR - nominal GDP CAGR (1990-last full year)
  * DCA channel = OLS ln(adj close) on calendar days since 2010-01-04 (same as scripts/log_trend_channel.py "full")
Pass as_of="YYYY-MM-DD" to truncate every series and reproduce an earlier reading.
"""
import datetime as dt
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, REPO, log, read_json  # noqa: E402

EQ_WIN = {"2000": ("2002-07-01", "2003-03-31"), "2008": ("2008-09-01", "2009-06-30"),
          "2015": ("2015-08-01", "2016-03-31"), "2021": ("2022-06-01", "2022-12-31")}
PEAK_WIN = {"2007": ("2007-01-01", "2007-12-31"), "2015": ("2015-01-01", "2015-12-31"), "2021": ("2021-10-01", "2022-01-31")}
TROUGH_WIN = {"2009": ("2008-09-01", "2009-06-30"), "2016": ("2015-08-01", "2016-03-31"), "2022": ("2022-06-01", "2022-12-31")}
ANCHORS = {"2010": "2010-01-04", "2020": "2020-01-02"}
DCA_START = "2010-01-04"
LUMP_DCA_SUMMARY = REPO / "backtests" / "QQQ_定投vs一次性_2026-10-11" / "summary.csv"


# ---------------------------------------------------------------- loading
def _series(label, col="close"):
    df = pd.read_csv(DATA / f"{label}_daily.csv", parse_dates=["date"]).set_index("date").sort_index()
    return df[col].dropna()


def _dated(fname):
    return pd.read_csv(DATA / fname, parse_dates=["date"]).set_index("date").sort_index()["value"].dropna()


def load(as_of=None):
    D = {}
    for l in ["GSPC", "SP500TR", "SPY", "NDX", "QQQ", "W5000", "TNX", "IRX", "FVX", "VIX", "GCF", "DXY"]:
        try:
            D[l] = _series(l)
        except Exception as e:  # noqa: BLE001
            log("missing series", l, e)
            D[l] = None
    D["QQQ_adj"] = _series("QQQ", "adj_close")
    D["SPY_adj"] = _series("SPY", "adj_close")
    bls = pd.read_csv(DATA / "bls_cpi_unrate_monthly.csv")
    bls["dt"] = pd.to_datetime(bls["month"])
    bls = bls.set_index("dt").sort_index()
    D["cpi"], D["unr"] = bls["cpi_u_nsa"].dropna(), bls["unrate_sa"].dropna()
    m2 = pd.read_csv(DATA / "us_m2_monthly.csv")
    m2["dt"] = pd.to_datetime(m2["month"])
    D["m2"] = m2.set_index("dt").sort_index()["m2_sa_usd_bn"].dropna()
    g = pd.read_csv(DATA / "gold_lbma_pm_daily.csv", parse_dates=[0])
    g = g.set_index(g.columns[0]).iloc[:, 0].astype(float).dropna().sort_index()
    D["gold_lbma_last"] = str(g.index[-1].date())
    gcf = D["GCF"]
    D["gold"] = pd.concat([g, gcf[gcf.index > g.index[-1]]]) if gcf is not None else g
    D["gold_splice_gap_pct"] = float(gcf[gcf.index > g.index[-1]].iloc[0] / g.iloc[-1] - 1) * 100 if gcf is not None and (gcf.index > g.index[-1]).any() else 0.0
    D["cape"], D["spe"], D["fpe"] = _dated("multpl_shiller_pe.csv"), _dated("multpl_sp500_pe.csv"), _dated("ndx_forward_pe_weekly.csv")
    try:
        D["tpe"] = _dated("ndx_trailing_pe_daily.csv")
    except Exception:  # noqa: BLE001
        D["tpe"] = None
    if as_of:
        cut = pd.Timestamp(as_of)
        for k, v in list(D.items()):
            if isinstance(v, pd.Series):
                D[k] = v[v.index <= cut]
    return D


# ---------------------------------------------------------------- helpers
def pct_below(sub, now):
    sub = pd.Series(sub).dropna()
    return float((sub < now).mean() * 100) if len(sub) > 20 else np.nan


def trend_idx(s, start):
    s = s[s.index >= start].dropna()
    x = np.arange(len(s))
    b, c = np.polyfit(x, np.log(s.values), 1)
    fit = pd.Series(np.exp(c + b * x), index=s.index)
    per = 252 if (s.index[1:] - s.index[:-1]).median().days <= 3 else 12
    return fit, (s / fit - 1) * 100, (np.exp(b * per) - 1) * 100


def fit_era(s, d):
    d = pd.Timestamp(d)
    seg = s[s.index >= d].dropna()
    t = np.asarray((seg.index - d).days / 365.25)
    b, c = np.polyfit(t, np.log(seg.values), 1)
    fit = np.exp(c + b * t)
    dev = pd.Series((seg.values / fit - 1) * 100, index=seg.index)
    a, g, years, now, line_now = float(np.exp(c)), float((np.exp(b) - 1) * 100), float(t[-1]), float(seg.iloc[-1]), float(fit[-1])
    return dict(start=str(d.date()), p0=float(seg.iloc[0]), a=a, g=g, b=float(b), c=float(c), years=years, now=now, line_now=line_now,
                dev=float(dev.iloc[-1]), pct=pct_below(dev, dev.iloc[-1]), p90=float(dev.quantile(.9)), p10=float(dev.quantile(.1)),
                max=float(dev.max()), max_date=str(dev.idxmax().date()), min=float(dev.min()), min_date=str(dev.idxmin().date()),
                to_line_pct=float((line_now / now - 1) * 100),
                implied={str(h): float(a * (1 + g / 100) ** (years + h)) for h in (1, 3, 5)})


def sigma_channel(s, start=DCA_START):
    s = s[s.index >= start].dropna()
    t = (s.index - s.index[0]).days.values.astype(float)
    y = np.log(s.values)
    b, a = np.polyfit(t, y, 1)
    fit = a + b * t
    sigma = float((y - fit).std(ddof=1))
    now, trend_now = float(s.iloc[-1]), float(np.exp(fit[-1]))
    m1 = float(np.exp(fit[-1] - sigma))
    return dict(start=start, n=int(len(s)), cagr=float((np.exp(b * 365.25) - 1) * 100), sigma_log=sigma,
                cur_sigma=float((y[-1] - fit[-1]) / sigma), price=now, trend=trend_now, dev_pct=float((now / trend_now - 1) * 100),
                minus1sd=m1, plus1sd=float(np.exp(fit[-1] + sigma)), minus2sd=float(np.exp(fit[-1] - 2 * sigma)),
                plus2sd=float(np.exp(fit[-1] + 2 * sigma)), to_minus1sd_pct=float((m1 / now - 1) * 100))


def _ret(s, k):
    return (s / s.shift(k) - 1) * 100


# ---------------------------------------------------------------- main
def compute(as_of=None):
    D = load(as_of)
    gspc, tr, ndx, qqq, qqqa, spy, spya = D["GSPC"], D["SP500TR"], D["NDX"], D["QQQ"], D["QQQ_adj"], D["SPY"], D["SPY_adj"]
    tnx, irx, fvx, vix, dxy = D["TNX"], D["IRX"], D["FVX"], D["VIX"], D["DXY"]
    cpi, unr, m2, gold, cape, spe, fpe = D["cpi"], D["unr"], D["m2"], D["gold"], D["cape"], D["spe"], D["fpe"]
    AS_OF = str(qqq.index[-1].date())
    S = {"as_of": AS_OF, "computed_utc": dt.datetime.utcnow().isoformat(timespec="seconds"), "as_of_override": as_of,
         "method": "scripts/market_temp v1; reconciles with backtests/市场体温_三节点_1980起_2026-10-11 and QQQ_现在高不高_2026-10-08"}
    cpiy = (cpi / cpi.shift(12) - 1) * 100
    S["levels"] = dict(qqq=float(qqq.iloc[-1]), spy=float(spy.iloc[-1]), spx=float(gspc.iloc[-1]), ndx=float(ndx.iloc[-1]),
                       spx_date=str(gspc.index[-1].date()), gold=float(gold.iloc[-1]), gold_date=str(gold.index[-1].date()),
                       gold_lbma_last=D["gold_lbma_last"], gold_splice_gap_pct=D["gold_splice_gap_pct"],
                       tnx=float(tnx.iloc[-1]), irx=float(irx.iloc[-1]), fvx=float(fvx.iloc[-1]), vix=float(vix.iloc[-1]), dxy=float(dxy.iloc[-1]),
                       cpi_date=str(cpi.index[-1].date()), cpi_yoy=float(cpiy.iloc[-1]), unrate=float(unr.iloc[-1]), unrate_date=str(unr.index[-1].date()),
                       m2_date=str(m2.index[-1].date()), m2_yoy=float(((m2 / m2.shift(12) - 1) * 100).iloc[-1]),
                       fwd_pe=float(fpe.iloc[-1]), fwd_pe_date=str(fpe.index[-1].date()), fwd_pe_10y_mean=float(fpe[fpe.index >= fpe.index[-1] - pd.DateOffset(years=10)].mean()),
                       trailing_pe=float(D["tpe"].iloc[-1]) if D["tpe"] is not None and len(D["tpe"]) else None,
                       cape=float(cape.iloc[-1]), cape_date=str(cape.index[-1].date()), spe=float(spe.iloc[-1]), spe_date=str(spe.index[-1].date()))

    # ---- nodes ----
    PK = {k: gspc[a:b].idxmax() for k, (a, b) in PEAK_WIN.items()}
    TR = {k: gspc[a:b].idxmin() for k, (a, b) in TROUGH_WIN.items()}
    PKN = {k: ndx[a:b].idxmax() for k, (a, b) in PEAK_WIN.items()}
    TRN = {k: ndx[a:b].idxmin() for k, (a, b) in TROUGH_WIN.items()}
    S["nodes"] = {"spx_peaks": {k: str(v.date()) for k, v in PK.items()}, "spx_troughs": {k: str(v.date()) for k, v in TR.items()},
                  "ndx_peaks": {k: str(v.date()) for k, v in PKN.items()}, "ndx_troughs": {k: str(v.date()) for k, v in TRN.items()},
                  "spx_drawdowns": {k: float((gspc[TR[k]] / gspc[PK[p]] - 1) * 100) for k, p in zip(TR, PK)},
                  "ndx_drawdowns": {k: float((ndx[TRN[k]] / ndx[PKN[p]] - 1) * 100) for k, p in zip(TRN, PKN)}}
    BASES = {"1980 起": pd.Timestamp("1980-01-01"), "2009 起": TR["2009"], "2016 起": TR["2016"], "2022 起": TR["2022"]}

    # ---- gauges (same 25 as the 10-11 study) ----
    G = []

    def asof(s, d):
        s2 = s[:d]
        return float(s2.iloc[-1]) if len(s2) else np.nan

    def gauge(name, group, s, hot="high", fmt="{:+.0f}%", note=""):
        try:
            s = s.dropna()
            now = float(s.iloc[-1])
            rec = dict(指标=name, 组=group, 现值=now, fmt=fmt, hot=hot, note=note, start=str(s.index[0].date()), last=str(s.index[-1].date()))
            for b, d in BASES.items():
                rec[f"分位 {b}"] = pct_below(s[s.index >= d], now)
            for k, d in PK.items():
                rec[f"{k} 顶"] = asof(s, d)
            for k, d in TR.items():
                rec[f"{k} 底"] = asof(s, d)
            p = rec["分位 1980 起"]
            rec["热度"] = p if hot == "high" else (100 - p if hot == "low" else np.nan)
            G.append(rec)
            return rec
        except Exception as e:  # noqa: BLE001
            log("gauge skipped:", name, e)
            return None

    fit80, dev80, cagr80 = trend_idx(gspc, "1980-01-01")
    gauge("标普500 偏离 1980 起趋势线", "价格", dev80, note=f"趋势年化 {cagr80:.1f}%")
    gauge("标普500 相对 200 日均线", "价格", ((gspc / gspc.rolling(200).mean() - 1) * 100)["1980":])
    gauge("标普500 过去 3 年价格回报", "价格", _ret(gspc, 756)["1980":])
    if tr is not None:
        gauge("标普500 过去 5 年总回报（1993 起）", "价格", _ret(tr, 1260)["1993":])
    gauge("标普500 距历史最高", "价格", ((gspc / gspc.cummax() - 1) * 100)["1980":], fmt="{:.1f}%")
    fitN, devN, cagrN = trend_idx(ndx, "1985-10-01")
    gauge("纳指100 偏离 1985 起趋势线", "价格", devN, note=f"趋势年化 {cagrN:.1f}%")
    gauge("纳指100 相对 200 日均线", "价格", (ndx / ndx.rolling(200).mean() - 1) * 100)
    gauge("QQQ 过去 3 年总回报", "价格", _ret(qqqa, 756))
    gauge("标普500 CAPE", "估值", cape["1980":], fmt="{:.1f}")
    gauge("标普500 滚动 PE", "估值", spe["1980":], fmt="{:.1f}")
    ey = 100 / spe
    gap = (ey - tnx.resample("MS").first().reindex(ey.index, method="nearest"))["1980":]
    gauge("标普500 盈利收益率 − 10 年国债（Fed 模型）", "估值", gap, hot="low", fmt="{:+.1f}pp")
    gauge("纳指100 前瞻 PE（2001 起）", "估值", fpe, fmt="{:.1f}")
    gauge("失业率", "经济", unr["1980":], hot="low", fmt="{:.1f}%")
    gauge("Sahm 指标（3 月均值 − 12 月最低）", "经济", (unr.rolling(3).mean() - unr.rolling(12).min())["1980":], hot="low", fmt="{:+.2f}pp", note="≥0.5 历史上对应衰退开始")
    gauge("CPI 同比", "经济", cpiy["1980":], fmt="{:.1f}%")
    gauge("收益率曲线 10 年 − 3 月", "经济", (tnx - irx)["1980":], hot="low", fmt="{:+.2f}pp", note="倒挂后 6–18 个月常见衰退")
    irx_m = irx.resample("MS").first()
    gauge("实际短期利率（3 月国库券 − CPI 同比）", "经济", (irx_m - cpiy.reindex(irx_m.index, method="nearest"))["1980":], hot="high", fmt="{:+.1f}pp", note="高 = 政策紧")
    gauge("10 年国债收益率", "经济", tnx["1980":], hot="high", fmt="{:.2f}%")
    gauge("M2 同比", "流动性", ((m2 / m2.shift(12) - 1) * 100)["1980":], fmt="{:.1f}%")
    gauge("VIX（1990 起）", "流动性", vix, hot="low", fmt="{:.1f}")
    gauge("美元指数 DXY", "流动性", dxy["1980":], hot="high", fmt="{:.1f}")
    gm = gold.resample("MS").first()
    cpi_m = cpi.reindex(gm.index, method="ffill")
    real_gold = (gm / cpi_m * cpi.iloc[-1])["1980":]
    gauge("黄金实际价格（按今日 CPI 折算）", "黄金", real_gold, fmt="${:,.0f}")
    gauge("黄金 / 标普500 比值", "黄金", (gm / gspc.resample("MS").first().reindex(gm.index, method="nearest"))["1980":], fmt="{:.2f}")
    gauge("黄金过去 3 年回报", "黄金", _ret(gold, 756)["1980":])
    gauge("黄金 / M2（美元每十亿美元 ×1000）", "黄金", (gm / m2.reindex(gm.index, method="ffill") * 1000)["1980":].dropna(), fmt="{:.3f}")
    Gdf = pd.DataFrame(G)
    S["gauges"] = Gdf.round(2).to_dict("records")
    S["heat_by_group"] = Gdf.groupby("组")["热度"].mean().round(0).to_dict()
    S["heat_overall"] = float(Gdf["热度"].mean())
    S["n_gauges_hot90"] = int((Gdf["热度"] >= 90).sum())
    S["n_gauges_cold10"] = int((Gdf["热度"] <= 10).sum())

    # ---- QQQ block (as analyze.py 2026-10-08) ----
    p = qqq
    ath = p.cummax()
    dd = (p / ath - 1) * 100
    hi52, lo52 = p.rolling(252).max(), p.rolling(252).min()
    ma50, ma200 = p.rolling(50).mean(), p.rolling(200).mean()
    nd200 = (ndx / ndx.rolling(200).mean() - 1) * 100
    nd50 = (ndx / ndx.rolling(50).mean() - 1) * 100
    year_start = p[p.index >= pd.Timestamp(f"{p.index[-1].year}-01-01")]
    Q = dict(close=float(p.iloc[-1]), date=AS_OF, prev_close=float(p.iloc[-2]), chg_1d_pct=float((p.iloc[-1] / p.iloc[-2] - 1) * 100),
             ath=float(ath.iloc[-1]), ath_date=str(p.idxmax().date()), drawdown_pct=float(dd.iloc[-1]), days_since_ath=int((p.index[-1] - p.idxmax()).days),
             drawdown_pct_days_deeper=float((dd < dd.iloc[-1]).mean() * 100),
             high52=float(hi52.iloc[-1]), from_52w_high_pct=float((p.iloc[-1] / hi52.iloc[-1] - 1) * 100), low52=float(lo52.iloc[-1]), from_52w_low_pct=float((p.iloc[-1] / lo52.iloc[-1] - 1) * 100),
             ma50=float(ma50.iloc[-1]), vs_50dma_pct=float((p.iloc[-1] / ma50.iloc[-1] - 1) * 100), ma200=float(ma200.iloc[-1]), vs_200dma_pct=float((p.iloc[-1] / ma200.iloc[-1] - 1) * 100),
             ndx_vs_200dma_pct=float(nd200.iloc[-1]), ndx_vs_200dma_pctile_1985=pct_below(nd200, nd200.iloc[-1]),
             ndx_vs_50dma_pct=float(nd50.iloc[-1]), ndx_vs_50dma_pctile_1985=pct_below(nd50, nd50.iloc[-1]),
             ret_1m_pct=float(_ret(p, 21).iloc[-1]), ret_3m_pct=float(_ret(p, 63).iloc[-1]), ret_ytd_pct=float((p.iloc[-1] / year_start.iloc[0] - 1) * 100) if len(year_start) else np.nan,
             trailing={})
    for yrs in (1, 3, 5, 10):
        r = _ret(qqqa, 252 * yrs)
        v = float(r.iloc[-1])
        Q["trailing"][str(yrs)] = dict(value=v, pctile_1999=pct_below(r, v), pctile_2009=pct_below(r[r.index >= TR["2009"]], v),
                                       median=float(r.median()), p90=float(r.quantile(.9)), max=float(r.max()))
    S["qqq"] = Q
    rel = (qqqa / spya)
    fit_rel, dev_rel, cagr_rel = trend_idx(rel, str(rel.index[0].date()))
    S["qqq_vs_spy"] = dict(ratio=float(rel.iloc[-1]), dev_trend_pct=float(dev_rel.iloc[-1]), pctile=pct_below(dev_rel, dev_rel.iloc[-1]), trend_cagr=cagr_rel)
    vol60 = float(np.log(p / p.shift(1)).rolling(60).std().iloc[-1] * np.sqrt(252) * 100)
    vol_hist = np.log(p / p.shift(1)).rolling(60).std() * np.sqrt(252) * 100
    S["qqq_vol60"] = dict(value=vol60, pctile=pct_below(vol_hist, vol60))

    # ---- four rulers (calendar-time fits from each cycle trough) ----
    S["ndx_eras"] = {k: fit_era(ndx, ndx[a:b].idxmin()) for k, (a, b) in EQ_WIN.items()}
    S["spx_eras"] = {k: fit_era(gspc, gspc[a:b].idxmin()) for k, (a, b) in EQ_WIN.items()}
    S["ndx_long"] = dict(start="1985-10-01", cagr=cagrN, dev=float(devN.iloc[-1]), pct=pct_below(devN, devN.iloc[-1]), to_line_pct=float((fitN.iloc[-1] / ndx.iloc[-1] - 1) * 100))
    S["spx_long"] = dict(start="1980-01-01", cagr=cagr80, dev=float(dev80.iloc[-1]), pct=pct_below(dev80, dev80.iloc[-1]), to_line_pct=float((fit80.iloc[-1] / gspc.iloc[-1] - 1) * 100))
    # "how far to fall" table, QQQ terms (NDX ratios applied to QQQ price)
    S["back_to"] = {"QQQ 200 日均线": float((Q["ma200"] / Q["close"] - 1) * 100),
                    "2021 底起趋势线（纳指）": S["ndx_eras"]["2021"]["to_line_pct"], "2015 底起趋势线（纳指）": S["ndx_eras"]["2015"]["to_line_pct"],
                    "2008 底起趋势线（纳指）": S["ndx_eras"]["2008"]["to_line_pct"], "2000 底起趋势线（纳指）": S["ndx_eras"]["2000"]["to_line_pct"],
                    "1985 起趋势线（纳指）": S["ndx_long"]["to_line_pct"]}

    # ---- DCA sigma channel (execution_plans/equity_index_plan §3) ----
    S["dca_channel"] = {"QQQ": sigma_channel(qqqa), "SPY": sigma_channel(spya)}

    # ---- GDP lines ----
    try:
        S["gdp"] = gdp_block(D, AS_OF, gspc, {"QQQ 含分红": qqqa, "SPY 含分红": spya, "纳指100 价格": ndx, "标普500 价格": gspc})
    except Exception as e:  # noqa: BLE001
        log("gdp block failed:", e)
        S["gdp"] = {"error": str(e)}

    # ---- concentration ----
    man = read_json(DATA / "manifest.json", {"series": {}})
    S["concentration"] = {}
    for etf in ("qqq", "spy"):
        try:
            h = pd.read_csv(DATA / f"{etf}_holdings_top.csv")
            nv = h[h["symbol"] == "NVDA"]["weight"]
            S["concentration"][etf.upper()] = dict(top1=str(h["symbol"].iloc[0]), top1_w=float(h["weight"].iloc[0]), nvda_w=float(nv.iloc[0]) if len(nv) else None,
                                                   top3=float(h["weight"].head(3).sum()), top10=float(h["weight"].head(10).sum()),
                                                   top10_list=h.head(10)[["symbol", "weight"]].values.tolist(),
                                                   as_of=man["series"].get(f"sa_{etf}", {}).get("last"), status=man["series"].get(f"sa_{etf}", {}).get("status"))
        except Exception as e:  # noqa: BLE001
            log("holdings missing", etf, e)

    # ---- lump vs DCA reference (which bucket today's start falls in) ----
    S["lump_dca"] = lump_dca_ref(S["ndx_eras"]["2008"]["pct"])

    # ---- data freshness ----
    S["freshness"] = {k: dict(status=v.get("status"), last=v.get("last"), stale_days=v.get("stale_days"), stale=v.get("stale"), error=v.get("error"))
                      for k, v in man.get("series", {}).items()}
    S["needs_ai"] = man.get("needs_ai", [])
    return S, Gdf


def gdp_block(D, AS_OF, gspc, assets):
    Q = pd.read_csv(DATA / "bea_gdp_quarterly.csv", parse_dates=["date"]).set_index("date").sort_index()
    Q = Q[Q.index <= pd.Timestamp(AS_OF)]
    last_q = Q.index[-1]
    g_nom = Q["gdp_nominal_bn"].iloc[-1] / Q["gdp_nominal_bn"].iloc[-5]
    g_real = Q["gdp_real_bn"].iloc[-1] / Q["gdp_real_bn"].iloc[-5]
    ext_idx = pd.date_range(last_q, pd.Timestamp(AS_OF) + pd.offsets.QuarterEnd(), freq="QE")[1:]
    ext = pd.DataFrame({"gdp_nominal_bn": [Q["gdp_nominal_bn"].iloc[-1] * g_nom ** ((i + 1) / 4) for i in range(len(ext_idx))],
                        "gdp_real_bn": [Q["gdp_real_bn"].iloc[-1] * g_real ** ((i + 1) / 4) for i in range(len(ext_idx))]}, index=ext_idx)
    QX = pd.concat([Q[["gdp_nominal_bn", "gdp_real_bn"]], ext])
    days = pd.date_range("1990-01-01", AS_OF, freq="D")
    ngdp = np.exp(np.log(QX["gdp_nominal_bn"]).reindex(days.union(QX.index)).interpolate(method="time").reindex(days))
    rgdp = np.exp(np.log(QX["gdp_real_bn"]).reindex(days.union(QX.index)).interpolate(method="time").reindex(days))
    cpi = D["cpi"]
    cpi_d = cpi.reindex(days.union(cpi.index)).interpolate(method="time").reindex(days).ffill()
    spe = D["spe"]
    gm = gspc.resample("MS").first()
    gm.index = gm.index.normalize()
    eps = (gm.reindex(spe.index, method="nearest") / spe).dropna()
    eps_y = eps.groupby(eps.index.year).last()
    AN = pd.read_csv(DATA / "bea_gdp_annual.csv").set_index("year")
    ly = min(int(pd.Timestamp(AS_OF).year) - 1, int(AN.index.max()), int(eps_y.index.max()))
    prem = {}
    for a in (1970, 1990, 2010):
        if a in eps_y.index and a in AN.index:
            ce = (eps_y[ly] / eps_y[a]) ** (1 / (ly - a)) - 1
            cg = (AN["gdp_nominal_bn"][ly] / AN["gdp_nominal_bn"][a]) ** (1 / (ly - a)) - 1
            prem[f"{a}-{ly}"] = dict(eps_cagr=ce * 100, ngdp_cagr=cg * 100, premium=(ce - cg) * 100)
    PREM = prem[f"1990-{ly}"]["premium"] / 100
    end = pd.Timestamp(AS_OF)
    out = dict(bea_last_quarter=str(last_q.date()), trailing_nominal_yoy=(g_nom - 1) * 100, trailing_real_yoy=(g_real - 1) * 100,
               extrapolated_quarters=int(len(ext_idx)), premium_windows=prem, premium_used_pp=PREM * 100, premium_window=f"1990-{ly}",
               ngdp_now_bn=float(ngdp.iloc[-1]), anchors={})
    for k, a in ANCHORS.items():
        a = pd.Timestamp(a)
        rows = {}
        for name, s in assets.items():
            if s is None:
                continue
            seg = s[s.index >= a]
            p0, now = float(seg.iloc[0]), float(seg.iloc[-1])
            yrs = (seg.index[-1] - a).days / 365.25
            L1 = p0 * ngdp[end] / ngdp[a]
            L2 = p0 * (rgdp[end] / rgdp[a]) * (cpi_d[end] / cpi_d[a])
            L3 = L1 * (1 + PREM) ** yrs
            rows[name] = dict(p0=p0, now=now, years=yrs, multiple=now / p0, asset_cagr=((now / p0) ** (1 / yrs) - 1) * 100,
                              ngdp_cagr=((ngdp[end] / ngdp[a]) ** (1 / yrs) - 1) * 100, L1=L1, L2=L2, L3=L3,
                              excess_vs_L1_pct=(now / L1 - 1) * 100, excess_vs_L3_pct=(now / L3 - 1) * 100,
                              to_L1_pct=(L1 / now - 1) * 100, to_L3_pct=(L3 / now - 1) * 100)
        out["anchors"][k] = dict(date=str(a.date()), rows=rows)
    return out


def lump_dca_ref(pct_2009):
    """pick the rows of the 2026-10-11 lump-vs-DCA study that match today's starting-point bucket"""
    try:
        df = pd.read_csv(LUMP_DCA_SUMMARY, encoding="utf-8-sig")
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)}
    labels = df["样本"].unique().tolist()
    want = None
    if pct_2009 >= 90:
        want = next((l for l in labels if "90" in l), None)
    elif pct_2009 >= 80:
        want = next((l for l in labels if "80" in l), None)
    if want is None:
        want = next((l for l in labels if "全部" in l), labels[0])
    sub = df[df["样本"] == want]
    return dict(bucket=want, pct_2009=pct_2009, labels=labels, rows=sub.to_dict("records"), source=str(LUMP_DCA_SUMMARY.relative_to(REPO)))


if __name__ == "__main__":
    import json
    S, G = compute(sys.argv[1] if len(sys.argv) > 1 else None)
    print(json.dumps({k: S[k] for k in ("as_of", "levels", "heat_by_group", "ndx_eras")}, indent=1, ensure_ascii=False, default=float))
