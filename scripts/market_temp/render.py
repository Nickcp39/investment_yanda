#!/usr/bin/env python
"""Render layer: temp.md (from report_template.md, evaluated as an f-string), gauges.csv, temp.json,
needs_ai.json, dashboard.png, plus the append-only history.csv and LATEST.txt pointer."""
from __future__ import annotations

import csv
import datetime as dt
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DATA, HERE, OUT, REPO, log, write_json  # noqa: E402

plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True,
                     "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False, "font.size": 8.5, "legend.fontsize": 7.5, "axes.titlesize": 10})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL, GOLD, BROWN = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285", "#b8860b", "#8c564b"
ERA_COL = {"2000": BROWN, "2008": ORANGE, "2015": TEAL, "2021": PURPLE}
GROUP_COL = {"价格": NAVY, "估值": ORANGE, "经济": GREEN, "流动性": GRAY, "黄金": GOLD}

HISTORY_COLS = ["as_of", "run_utc", "qqq_close", "qqq_dd_pct", "qqq_vs_200dma", "ndx_dev_2000", "ndx_dev_2008", "ndx_pct_2008", "ndx_dev_2015", "ndx_dev_2021",
                "spx_dev_1980", "fwd_pe", "cape", "fed_gap_pp", "tnx", "unrate", "cpi_yoy", "vix", "gold", "heat_价格", "heat_估值", "heat_经济", "heat_流动性", "heat_黄金",
                "heat_all", "qqq_sigma", "qqq_minus1sd", "qqq_excess_gdp_2010", "qqq_excess_gdp_2020", "nvda_w_qqq", "top10_qqq"]


def f(rec, key="现值"):
    return rec["fmt"].format(rec[key]) if rec is not None and rec.get(key) is not None and not (isinstance(rec[key], float) and np.isnan(rec[key])) else "—"


def pc(x, nd=0, sign=True):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    return f"{x:+.{nd}f}%" if sign else f"{x:.{nd}f}%"


def nz(x, nd=0):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:,.{nd}f}"


def heat_word(h):
    if h is None or np.isnan(h):
        return "—"
    return "过热" if h >= 90 else "偏热" if h >= 70 else "中性" if h >= 30 else "偏冷" if h >= 10 else "过冷"


def build_context(S, G: pd.DataFrame, prev: dict | None):
    g = {r["指标"]: r for r in G.to_dict("records")}
    L, Q, NE, SE = S["levels"], S["qqq"], S["ndx_eras"], S["spx_eras"]
    ctx = dict(S=S, L=L, Q=Q, NE=NE, SE=SE, g=g, AS_OF=S["as_of"], RUN=dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
    # heat table
    rows = []
    for grp in ("价格", "估值", "经济", "流动性", "黄金"):
        h = S["heat_by_group"].get(grp)
        if h is None:
            continue
        sub = G[G["组"] == grp]
        hot = sub.sort_values("热度", ascending=False).iloc[0]
        rows.append(f"| {grp} | **{h:.0f}** {heat_word(h)} | {len(sub)} 项，最热：{hot['指标']} {f(hot)}（{hot['热度']:.0f}） |")
    ctx["heat_table"] = "\n".join(rows)
    # QQQ position table
    t = Q["trailing"]
    ctx["qqq_table"] = "\n".join([
        f"| QQQ 收盘 | **{Q['close']:.2f}**（{pc(Q['chg_1d_pct'], 1)} 当日） | 历史最高 {Q['ath']:.2f}（{Q['ath_date']}，{Q['days_since_ath']} 天前） |",
        f"| 距历史最高 | **{pc(Q['drawdown_pct'], 1)}** | 1999 起只有 {Q['drawdown_pct_days_deeper']:.0f}% 的交易日回撤比今天深 |",
        f"| 距 52 周高 / 低 | {pc(Q['from_52w_high_pct'], 1)} / {pc(Q['from_52w_low_pct'], 1)} | 52 周高 {Q['high52']:.2f}，低 {Q['low52']:.2f} |",
        f"| 相对 50 / 200 日均线 | {pc(Q['vs_50dma_pct'], 1)} / {pc(Q['vs_200dma_pct'], 1)} | 纳指100 相对 200 日线 {pc(Q['ndx_vs_200dma_pct'], 1)}，1985 起 {Q['ndx_vs_200dma_pctile_1985']:.0f} 分位 |",
        f"| 1 月 / 3 月 / 年初至今 | {pc(Q['ret_1m_pct'], 1)} / {pc(Q['ret_3m_pct'], 1)} / {pc(Q['ret_ytd_pct'], 1)} | 价格口径 |",
        f"| 过去 1 / 3 / 5 / 10 年总回报 | {pc(t['1']['value'])} / {pc(t['3']['value'])} / {pc(t['5']['value'])} / {pc(t['10']['value'])} | 1999 起分位 {t['1']['pctile_1999']:.0f} / {t['3']['pctile_1999']:.0f} / {t['5']['pctile_1999']:.0f} / {t['10']['pctile_1999']:.0f} |",
        f"| QQQ / SPY 比值 | {S['qqq_vs_spy']['ratio']:.3f}，偏离自身趋势 {pc(S['qqq_vs_spy']['dev_trend_pct'])} | {S['qqq_vs_spy']['pctile']:.0f} 分位 |",
        f"| 60 日实现波动率 | {S['qqq_vol60']['value']:.0f}% | {S['qqq_vol60']['pctile']:.0f} 分位 |",
    ])
    # rulers
    rr = []
    for k in ("2000", "2008", "2015", "2021"):
        e = NE[k]
        rr.append(f"| {k} 周期底（{e['start']}） | {e['g']:.1f}% | **{pc(e['dev'])}** | **{e['pct']:.0f}** | {pc(e['p10'])} ~ {pc(e['p90'])} | {pc(e['to_line_pct'])} | {e['implied']['1']:,.0f} / {e['implied']['3']:,.0f} / {e['implied']['5']:,.0f} |")
    nl = S["ndx_long"]
    rr.append(f"| 1985 起（全史） | {nl['cagr']:.1f}% | {pc(nl['dev'])} | {nl['pct']:.0f} | — | {pc(nl['to_line_pct'])} | — |")
    ctx["ruler_table"] = "\n".join(rr)
    sr = []
    for k in ("2000", "2008", "2015", "2021"):
        e = SE[k]
        sr.append(f"| {k} 周期底（{e['start']}） | {e['g']:.1f}% | {pc(e['dev'])} | {e['pct']:.0f} | {pc(e['to_line_pct'])} |")
    sl = S["spx_long"]
    sr.append(f"| 1980 起（全史） | {sl['cagr']:.1f}% | {pc(sl['dev'])} | {sl['pct']:.0f} | {pc(sl['to_line_pct'])} |")
    ctx["spx_ruler_table"] = "\n".join(sr)
    ctx["formula_rows"] = "\n".join(f"- {k} 周期：P = {NE[k]['a']:,.0f} × (1 + {NE[k]['g']/100:.3f})^t，t = 自 {NE[k]['start']} 起的年数（现在 t = {NE[k]['years']:.1f}）" for k in ("2000", "2008", "2015", "2021"))
    # back-to table
    ctx["back_table"] = "\n".join(f"| {k} | {pc(v, 1)} |" for k, v in S["back_to"].items())
    # gauge tables by group
    def gtab(grp):
        out = []
        for r in G[G["组"] == grp].to_dict("records"):
            out.append(f"| {r['指标']} | {f(r)} | {nz(r['分位 1980 起'])} | {nz(r['分位 2009 起'])} | {nz(r['分位 2016 起'])} | {nz(r['分位 2022 起'])} | {f(r, '2007 顶')} / {f(r, '2015 顶')} / {f(r, '2021 顶')} | {f(r, '2009 底')} / {f(r, '2016 底')} / {f(r, '2022 底')} | {nz(r['热度'])} |")
        return "\n".join(out)
    for grp, key in (("价格", "price_table"), ("估值", "val_table"), ("经济", "econ_table"), ("流动性", "liq_table"), ("黄金", "gold_table")):
        ctx[key] = gtab(grp)
    # DCA channel
    dr = []
    for k, c in S["dca_channel"].items():
        dr.append(f"| {k} | {c['price']:.2f} | {c['trend']:.2f} | **{c['cur_sigma']:+.2f}σ** | {c['minus1sd']:.2f}（需 {pc(c['to_minus1sd_pct'], 1)}） | {c['cagr']:.1f}% |")
    ctx["dca_table"] = "\n".join(dr)
    # GDP
    gd = S.get("gdp", {})
    if "anchors" in gd:
        gr = []
        for k, a in gd["anchors"].items():
            for name, r in a["rows"].items():
                gr.append(f"| {k}（{a['date']}） | {name} | ×{r['multiple']:.2f}（{r['asset_cagr']:.1f}%/年） | {r['ngdp_cagr']:.1f}%/年 | **{pc(r['excess_vs_L1_pct'])}** | {pc(r['excess_vs_L3_pct'])} | {pc(r['to_L1_pct'])} / {pc(r['to_L3_pct'])} |")
        ctx["gdp_table"] = "\n".join(gr)
        ctx["gdp_note"] = (f"BEA 最新季度 {gd['bea_last_quarter']}，之后 {gd['extrapolated_quarters']} 个季度按最近四季名义增速 {gd['trailing_nominal_yoy']:.1f}% 外推；"
                           f"龙头溢价取 {gd['premium_window']} 标普 EPS 年化 − 名义 GDP 年化 = {gd['premium_used_pp']:.1f} 个百分点。")
    else:
        ctx["gdp_table"] = "| — | GDP 模块失败 | | | | | |"
        ctx["gdp_note"] = str(gd.get("error", ""))
    # concentration
    cr = []
    for etf, c in S.get("concentration", {}).items():
        top = "、".join(f"{s} {w:.1f}%" for s, w in c["top10_list"][:5])
        cr.append(f"| {etf} | {c['top1']} {c['top1_w']:.2f}% | {nz(c['nvda_w'], 2)}% | {c['top3']:.1f}% | **{c['top10']:.1f}%** | {top} | {c['as_of']}（{c['status']}） |")
    ctx["conc_table"] = "\n".join(cr) if cr else "| — | 持仓数据缺失 | | | | | |"
    # lump vs dca
    ld = S.get("lump_dca", {})
    if "rows" in ld:
        lr = [f"| {r['期限']} | {r['方式']} | {r['起点数']} | {r['中位回报']:+.0f}% | {r['最差']:+.0f}% | {r['期间最深浮亏中位']:+.0f}% / {r['期间最深浮亏最差']:+.0f}% | {r['一年后仍亏概率']:.0f}% |" for r in ld["rows"] if str(r.get("期限")) == "3y"]
        ctx["lump_table"] = "\n".join(lr)
        ctx["lump_note"] = f"今天纳指相对 2008 底起趋势线处于时代内 {ld['pct_2009']:.0f} 分位，对应样本「{ld['bucket']}」（来源 {ld['source']}）。"
    else:
        ctx["lump_table"], ctx["lump_note"] = "| — | | | | | | |", str(ld.get("error", ""))
    # freshness
    fr = []
    for k, v in S["freshness"].items():
        flag = "⚠️ 过期" if v.get("stale") else "✅"
        st = v.get("status")
        fr.append(f"| {k} | {st} | {v.get('last') or '—'} | {v.get('stale_days') if v.get('stale_days') is not None else '—'} | {flag} |")
    ctx["fresh_table"] = "\n".join(fr)
    ctx["needs_rows"] = "\n".join(f"- **{n['key']}**（{n['status']}，最后 {n['last'] or '无'}）：{n['what']}" for n in S["needs_ai"]) or "- 无，全部数据在新鲜阈值内。"
    # change vs previous run
    if prev:
        def d(cur, key, nd=1, suffix=""):
            try:
                pv = float(prev[key])
                return f"{pv:.{nd}f}{suffix} → {cur:.{nd}f}{suffix}（{cur - pv:+.{nd}f}）"
            except Exception:  # noqa: BLE001
                return f"— → {cur:.{nd}f}{suffix}"
        ctx["delta_rows"] = "\n".join([
            f"| QQQ 收盘 | {d(Q['close'], 'qqq_close', 2)} |",
            f"| QQQ 距历史最高 | {d(Q['drawdown_pct'], 'qqq_dd_pct', 1, '%')} |",
            f"| 纳指偏离 2008 底起趋势线 | {d(NE['2008']['dev'], 'ndx_dev_2008', 1, '%')} |",
            f"| 纳指偏离 2021 底起趋势线 | {d(NE['2021']['dev'], 'ndx_dev_2021', 1, '%')} |",
            f"| 纳指100 前瞻 PE | {d(L['fwd_pe'], 'fwd_pe', 1)} |",
            f"| 标普 CAPE | {d(L['cape'], 'cape', 1)} |",
            f"| 10 年国债 | {d(L['tnx'], 'tnx', 2, '%')} |",
            f"| VIX | {d(L['vix'], 'vix', 1)} |",
            f"| 黄金 | {d(L['gold'], 'gold', 0)} |",
            f"| 总热度 | {d(S['heat_overall'], 'heat_all', 0)} |",
            f"| QQQ 相对 2010 起 σ 通道 | {d(S['dca_channel']['QQQ']['cur_sigma'], 'qqq_sigma', 2, 'σ')} |",
        ])
        ctx["prev_as_of"] = prev.get("as_of")
    else:
        ctx["delta_rows"] = "| — | 首次运行，没有上一轮 |"
        ctx["prev_as_of"] = "—"
    return ctx


def render_md(ctx):
    tpl = (HERE / "report_template.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    return eval('f"""' + tpl + '"""', {"np": np, "pc": pc, "nz": nz, "f": f, "heat_word": heat_word}, ctx)


def history_row(S):
    L, Q, NE, C = S["levels"], S["qqq"], S["ndx_eras"], S["dca_channel"]["QQQ"]
    g = {r["指标"]: r for r in S["gauges"]}
    gd = S.get("gdp", {}).get("anchors", {})
    conc = S.get("concentration", {}).get("QQQ", {})
    row = dict(as_of=S["as_of"], run_utc=S["computed_utc"], qqq_close=Q["close"], qqq_dd_pct=Q["drawdown_pct"], qqq_vs_200dma=Q["vs_200dma_pct"],
               ndx_dev_2000=NE["2000"]["dev"], ndx_dev_2008=NE["2008"]["dev"], ndx_pct_2008=NE["2008"]["pct"], ndx_dev_2015=NE["2015"]["dev"], ndx_dev_2021=NE["2021"]["dev"],
               spx_dev_1980=S["spx_long"]["dev"], fwd_pe=L["fwd_pe"], cape=L["cape"], fed_gap_pp=g.get("标普500 盈利收益率 − 10 年国债（Fed 模型）", {}).get("现值"),
               tnx=L["tnx"], unrate=L["unrate"], cpi_yoy=L["cpi_yoy"], vix=L["vix"], gold=L["gold"],
               heat_all=S["heat_overall"], qqq_sigma=C["cur_sigma"], qqq_minus1sd=C["minus1sd"],
               qqq_excess_gdp_2010=gd.get("2010", {}).get("rows", {}).get("QQQ 含分红", {}).get("excess_vs_L1_pct"),
               qqq_excess_gdp_2020=gd.get("2020", {}).get("rows", {}).get("QQQ 含分红", {}).get("excess_vs_L1_pct"),
               nvda_w_qqq=conc.get("nvda_w"), top10_qqq=conc.get("top10"))
    for grp, h in S["heat_by_group"].items():
        row[f"heat_{grp}"] = h
    return {k: row.get(k) for k in HISTORY_COLS}


def read_history():
    p = OUT / "history.csv"
    if not p.exists():
        return pd.DataFrame(columns=HISTORY_COLS)
    return pd.read_csv(p, encoding="utf-8-sig")


def append_history(row, backfill=False):
    p = OUT / "history.csv"
    h = read_history()
    h = h[h["as_of"] != row["as_of"]]
    h = pd.concat([h, pd.DataFrame([row])], ignore_index=True).sort_values("as_of") if len(h) else pd.DataFrame([row])
    if not backfill or not p.exists():
        h.to_csv(p, index=False, encoding="utf-8-sig", float_format="%.4f")
    return h


def dashboard(S, D, path: Path):
    ndx, qqq, qqqa, fpe = D["NDX"], D["QQQ"], D["QQQ_adj"], D["fpe"]
    fig, axes = plt.subplots(2, 3, figsize=(16.5, 9.2))
    AS_OF = S["as_of"]
    # (1) NDX with four rulers
    ax = axes[0, 0]
    seg = ndx[ndx.index >= "2002-01-01"]
    ax.plot(seg.index, seg.values, color=NAVY, lw=.9, label="纳指100")
    for k in ("2000", "2008", "2015", "2021"):
        e = S["ndx_eras"][k]
        d0 = pd.Timestamp(e["start"])
        idx = pd.date_range(d0, pd.Timestamp(AS_OF) + pd.DateOffset(years=3), freq="7D")
        t = (idx - d0).days / 365.25
        line = e["a"] * (1 + e["g"] / 100) ** t
        past = idx <= pd.Timestamp(AS_OF)
        ax.plot(idx[past], line[past], color=ERA_COL[k], lw=1.1, label=f"{k} 底起 {e['g']:.0f}%/年，现偏离 {e['dev']:+.0f}%（{e['pct']:.0f} 分位）")
        ax.plot(idx[~past], line[~past], color=ERA_COL[k], lw=1, ls=":")
    ax.set_yscale("log")
    ax.set_title(f"图 1 · 纳指100 与四把周期尺子（截至 {AS_OF}）")
    ax.legend(loc="upper left")
    # (2) QQQ drawdown
    ax = axes[0, 1]
    dd = (qqq / qqq.cummax() - 1) * 100
    ax.fill_between(dd.index, dd.values, 0, color=RED, alpha=.35, lw=0)
    ax.plot(dd.index, dd.values, color=RED, lw=.6)
    for lvl in (-10, -20, -35):
        ax.axhline(lvl, color=GRAY, lw=.6, ls="--")
    ax.scatter([dd.index[-1]], [dd.iloc[-1]], color="black", zorder=5)
    ax.annotate(f"{dd.iloc[-1]:+.1f}%", (dd.index[-1], dd.iloc[-1]), xytext=(-60, -12), textcoords="offset points", fontsize=9, fontweight="bold")
    ax.set_title("图 2 · QQQ 距历史最高（回撤，%）")
    # (3) heat bars
    ax = axes[0, 2]
    G = pd.DataFrame(S["gauges"]).sort_values("热度")
    cols = [GROUP_COL.get(x, GRAY) for x in G["组"]]
    ax.barh(range(len(G)), G["热度"], color=cols)
    ax.set_yticks(range(len(G)))
    import re as _re
    ax.set_yticklabels([f"{_re.sub(r'（.*?）', '', r['指标'])[:16]} {r['fmt'].format(r['现值'])}" for r in G.to_dict("records")], fontsize=6.5)
    for v in (10, 50, 90):
        ax.axvline(v, color=GRAY, lw=.6, ls="--")
    ax.set_xlim(0, 100)
    ax.set_title(f"图 3 · 25 个指标的热度（1980 起分位，已按方向统一）· 总热度 {S['heat_overall']:.0f}")
    ax.grid(axis="y", alpha=0)
    # (4) forward PE
    ax = axes[1, 0]
    ax.plot(fpe.index, fpe.values, color=ORANGE, lw=.9)
    ax.axhline(S["levels"]["fwd_pe_10y_mean"], color=GRAY, lw=.7, ls="--", label=f"10 年均值 {S['levels']['fwd_pe_10y_mean']:.1f}")
    ax.scatter([fpe.index[-1]], [fpe.iloc[-1]], color="black", zorder=5)
    ax.annotate(f"{fpe.iloc[-1]:.1f}x（{S['levels']['fwd_pe_date']}）", (fpe.index[-1], fpe.iloc[-1]), xytext=(-110, 10), textcoords="offset points", fontsize=8.5, fontweight="bold")
    ax.set_ylim(10, 40)
    ax.set_xlim(pd.Timestamp("2003-01-01"), fpe.index[-1] + pd.DateOffset(months=6))
    ax.set_title("图 4 · 纳指100 前瞻 12 个月 PE（historyofmarket.com）")
    ax.legend(loc="upper left")
    # (5) sigma channel
    ax = axes[1, 1]
    c = S["dca_channel"]["QQQ"]
    s = qqqa[qqqa.index >= c["start"]]
    t = (s.index - s.index[0]).days.values.astype(float)
    y = np.log(s.values)
    b, a = np.polyfit(t, y, 1)
    fit = a + b * t
    ax.plot(s.index, s.values, color=NAVY, lw=.8, label="QQQ 含分红")
    ax.plot(s.index, np.exp(fit), color=GRAY, lw=1, label=f"趋势 {c['cagr']:.1f}%/年")
    for m, ls in ((1, "--"), (2, ":")):
        ax.plot(s.index, np.exp(fit + m * c["sigma_log"]), color=RED, lw=.7, ls=ls)
        ax.plot(s.index, np.exp(fit - m * c["sigma_log"]), color=GREEN, lw=.7, ls=ls, label=f"−{m}σ" if m == 1 else None)
    ax.set_yscale("log")
    ax.scatter([s.index[-1]], [s.iloc[-1]], color="black", zorder=5)
    ax.annotate(f"{c['cur_sigma']:+.2f}σ\n−1σ 线 {c['minus1sd']:.0f}（需 {c['to_minus1sd_pct']:+.0f}%）", (s.index[-1], s.iloc[-1]), xytext=(-120, -36), textcoords="offset points", fontsize=8.5)
    ax.set_title("图 5 · QQQ 2010 起对数趋势 ±1σ/±2σ（定投计划 §3 的翻倍线）")
    ax.legend(loc="upper left")
    # (6) QQQ vs GDP lines anchored 2010
    ax = axes[1, 2]
    gd = S.get("gdp", {})
    if "anchors" in gd:
        a0 = pd.Timestamp(gd["anchors"]["2010"]["date"])
        seg = qqqa[qqqa.index >= a0]
        r = gd["anchors"]["2010"]["rows"]["QQQ 含分红"]
        yrs = (seg.index - a0).days / 365.25
        L1 = r["p0"] * (r["L1"] / r["p0"]) ** (yrs / yrs[-1])
        L3 = r["p0"] * (r["L3"] / r["p0"]) ** (yrs / yrs[-1])
        ax.plot(seg.index, seg.values, color=NAVY, lw=.9, label="QQQ 含分红")
        ax.plot(seg.index, L1, color=GREEN, lw=1, label=f"名义 GDP 线（{r['ngdp_cagr']:.1f}%/年），现高出 {r['excess_vs_L1_pct']:+.0f}%")
        ax.plot(seg.index, L3, color=ORANGE, lw=1, ls="--", label=f"GDP + 龙头溢价 {gd['premium_used_pp']:.1f}pp，现高出 {r['excess_vs_L3_pct']:+.0f}%")
        ax.set_yscale("log")
        ax.legend(loc="upper left")
    ax.set_title("图 6 · QQQ 对比名义 GDP 基准线（锚点 2010-01-04，示意为复合线）")
    fig.suptitle(f"市场体温 · 截至 {AS_OF} 收盘 · scripts/market_temp（数据：Yahoo / BLS / BEA / multpl / historyofmarket / stockanalysis）", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def write_outputs(S, G, D, folder: Path, backfill=False):
    folder.mkdir(parents=True, exist_ok=True)
    hist = read_history()
    prev = None
    earlier = hist[hist["as_of"] < S["as_of"]]
    if len(earlier):
        prev = earlier.sort_values("as_of").iloc[-1].to_dict()
    ctx = build_context(S, G, prev)
    md = render_md(ctx)
    (folder / "temp.md").write_text(md, encoding="utf-8")
    G.to_csv(folder / "gauges.csv", index=False, encoding="utf-8-sig", float_format="%.2f")
    write_json(folder / "temp.json", S)
    write_json(folder / "needs_ai.json", {"as_of": S["as_of"], "items": S["needs_ai"]})
    try:
        dashboard(S, D, folder / "dashboard.png")
    except Exception as e:  # noqa: BLE001
        log("dashboard failed:", e)
    row = history_row(S)
    append_history(row, backfill=backfill)
    if not backfill:
        (OUT / "LATEST.txt").write_text(folder.name, encoding="utf-8")
    log("wrote", folder.relative_to(REPO))
    return md
