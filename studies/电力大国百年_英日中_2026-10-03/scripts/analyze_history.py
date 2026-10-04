#!/usr/bin/env python3
"""analyze_history.py — 股东到底赚没赚到钱：各电力股 vs 本国大盘的价格回报、含息回报、最深回撤、分红史。

读取 data/prices_monthly.json / dividends.json（fetch_history.py 产物），输出 data/history_stats.json 并打印汇总。
口径：
  price  = Yahoo close（仅拆股调整）
  TR     = 自行用 close + 逐笔分红（除息月按月末价再投资）重建 —— 不用 Yahoo adjclose：它对英股月线几乎不含分红
           （NG 2007-12 → 2019-12 的 adjclose 只给出 +18%，而同期仅股息就约 60%），已核实不可用
  大盘含息代理 = 本国指数 ETF（1321.T / ISF.L / 2800.HK / 510300.SS）同样用 close + 分红重建；起点晚于个股时只比重叠段
  月度序列取月末收盘；as_of 月取最新收盘（2026-10-02 / A 股 09-30）
  年度每股分红 = 当年除息日所在日历年的分红合计（Yahoo，拆股调整后）
"""
from __future__ import annotations

import json
import math
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
M = json.loads((DATA / "prices_monthly.json").read_text(encoding="utf-8"))
DIV = json.loads((DATA / "dividends.json").read_text(encoding="utf-8"))

# 每只股票：本国价格指数 + 含息代理（及其起点）
PAIRS = {
    "9501.T": ("^N225", "1321.T"), "9503.T": ("^N225", "1321.T"), "9508.T": ("^N225", "1321.T"),
    "9513.T": ("^N225", "1321.T"), "9502.T": ("^N225", "1321.T"),
    "NG.L": ("^FTAS", "ISF.L"), "SSE.L": ("^FTAS", "ISF.L"),
    "600900.SS": ("000001.SS", "510300.SS"), "600011.SS": ("000001.SS", "510300.SS"),
    "003816.SZ": ("000001.SS", "510300.SS"),
    "1816.HK": ("^HSI", "2800.HK"), "0902.HK": ("^HSI", "2800.HK"), "0836.HK": ("^HSI", "2800.HK"),
}
# 历史窗口（检验"制度 / 冲击"前后）
WINDOWS = {
    "JP": [("2000-01", "2011-02", "福岛前十年"), ("2011-02", "2012-06", "福岛冲击"), ("2012-06", "2020-12", "停堆与重启"),
           ("2020-12", "2026-10", "燃料危机后复苏")],
    "UK": [("1995-12", "2007-12", "私有化红利期"), ("2007-12", "2019-12", "低利率 + RIIO"), ("2019-12", "2026-10", "能源危机 + 电网扩张")],
    "CN": [("2005-01", "2007-10", "牛市"), ("2007-10", "2015-06", "煤价周期"), ("2015-06", "2020-12", "去产能与煤价反弹"),
           ("2020-12", "2026-09", "煤价冲击与红利行情")],
}
REGION = {"9501.T": "JP", "9503.T": "JP", "9508.T": "JP", "9513.T": "JP", "9502.T": "JP", "NG.L": "UK", "SSE.L": "UK",
          "600900.SS": "CN", "600011.SS": "CN", "003816.SZ": "CN", "1816.HK": "CN", "0902.HK": "CN", "0836.HK": "CN"}


def series(tk, field="close"):
    s = M[tk]["series"]
    if field == "adj":
        return tr_series(tk)
    return {k: v[field] for k, v in sorted(s.items()) if v.get(field) is not None}


def tr_series(tk):
    """含息总回报指数：TR_t = TR_{t-1} × (P_t + D_t) / P_{t-1}，D_t = 当月除息的每股分红。"""
    px = {k: v["close"] for k, v in sorted(M[tk]["series"].items()) if v.get("close")}
    dm = {}
    for dte, amt in DIV.get(tk, []):
        dm[dte[:7]] = dm.get(dte[:7], 0) + amt
    out, prev, lvl = {}, None, 100.0
    for k, p in px.items():
        if prev is not None:
            lvl *= (p + dm.get(k, 0)) / prev
        out[k] = lvl
        prev = p
    return out


def ratio(s, a, b):
    ks = sorted(s)
    a2 = next((k for k in ks if k >= a), None)
    b2 = max((k for k in ks if k <= b), default=None)
    if not a2 or not b2 or a2 >= b2:
        return None, None, None
    return s[b2] / s[a2], a2, b2


def cagr(r, a, b):
    yrs = (int(b[:4]) * 12 + int(b[5:7]) - int(a[:4]) * 12 - int(a[5:7])) / 12
    return r ** (1 / yrs) - 1 if yrs > 0 else None


def max_dd(s):
    peak_v, peak_k, worst = -1, None, (0, None, None)
    for k, v in s.items():
        if v > peak_v:
            peak_v, peak_k = v, k
        dd = v / peak_v - 1
        if dd < worst[0]:
            worst = (dd, peak_k, k)
    return worst


def annual_div(tk):
    out = {}
    for dte, amt in DIV.get(tk, []):
        out[dte[:4]] = out.get(dte[:4], 0) + amt
    return dict(sorted(out.items()))


def main():
    stats = {}
    for tk, (px_idx, tr_idx) in PAIRS.items():
        if tk not in M:
            continue
        p, a = series(tk), series(tk, "adj")
        ip, it = series(px_idx), series(tr_idx, "adj")
        first, last = min(p), max(p)
        rp, _, _ = ratio(p, first, last)
        ra, _, _ = ratio(a, first, last)
        rip, _, _ = ratio(ip, first, last)
        tr_start = max(min(it), first)
        ra2, a2, b2 = ratio(a, tr_start, last)
        rit, _, _ = ratio(it, tr_start, last)
        peak_k = max(p, key=p.get)
        dd, ddp, ddt = max_dd(a)
        wins = []
        for w0, w1, label in WINDOWS[REGION[tk]]:
            r1, x0, x1 = ratio(a, w0, w1)
            r2, _, _ = ratio(ip, w0, w1)
            if r1:
                wins.append({"window": label, "from": x0, "to": x1, "stock_tr": round(r1 - 1, 3),
                             "index_price": round(r2 - 1, 3) if r2 else None})
        rec = {"name": M[tk]["name"], "ccy": M[tk]["currency"], "first": first, "last": last,
               "price_x": round(rp, 3), "tr_x": round(ra, 3), "tr_cagr": round(cagr(ra, first, last), 4),
               "index_price_x": round(rip, 3) if rip else None, "index": px_idx,
               "tr_vs_proxy": {"from": a2, "stock_tr_x": round(ra2, 3) if ra2 else None, "proxy": tr_idx,
                               "proxy_tr_x": round(rit, 3) if rit else None,
                               "stock_cagr": round(cagr(ra2, a2, b2), 4) if ra2 else None,
                               "proxy_cagr": round(cagr(rit, a2, b2), 4) if rit else None},
               "price_peak": {"month": peak_k, "price": p[peak_k], "now_vs_peak": round(p[last] / p[peak_k] - 1, 3)},
               "max_drawdown_tr": {"dd": round(dd, 3), "peak": ddp, "trough": ddt},
               "windows": wins, "annual_dividends": annual_div(tk)}
        stats[tk] = rec
        print(f"{tk:10} {rec['name'][:12]:12} {first}->{last} price x{rp:6.2f} TR x{ra:6.2f} ({rec['tr_cagr']:+.1%}/yr) | "
              f"{px_idx} price x{rip:5.2f} | TR since {a2}: stock x{ra2:.2f} ({rec['tr_vs_proxy']['stock_cagr']:+.1%}) vs "
              f"{tr_idx} x{rit:.2f} ({rec['tr_vs_proxy']['proxy_cagr']:+.1%}) | peak {peak_k} {p[peak_k]:.0f} now {rec['price_peak']['now_vs_peak']:+.0%} | "
              f"maxDD {dd:.0%} {ddp}->{ddt}")
        for w in wins:
            print(f"      {w['window']:12} {w['from']}->{w['to']} stock TR {w['stock_tr']:+.0%} | index price {w['index_price']:+.0%}")
    (DATA / "history_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
