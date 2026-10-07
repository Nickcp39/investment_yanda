#!/usr/bin/env python3
"""analyze_industry_market.py — 两个不依赖“挑股票”的统计层（无幸存者偏差）。

A. 行业层（Kenneth French 49 行业，市值加权月总回报，1926-07..2026-07；本研究取 1981 起）
   A1 每年年末：过去 5 年相对市场最强的行业（“当年风气”），之后 5 年相对市场表现如何？
   A2 行业泡沫事件：某行业 36 个月内跑赢市场 ≥100%（相对财富 ≥2.0）→ 记录顶点、之后的
      绝对回撤、触底用时、回到顶点用时、顶点后 5 年相对市场。
B. 市场层（Yahoo 日线价格指数，不含股息）：纳指 / 标普 1985 年以来 ≥20% 的回撤，顶点→谷底→收复用时。

输出 data/industry_fads.json、data/market_drawdowns.json。只读本地 data/raw，不联网。
"""
from __future__ import annotations

import csv
import gzip
import io
import json
import math
import statistics
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data/raw"

CN = {  # French 49 行业中文名（按 Siccodes49 定义翻译）
    "Agric": "农业", "Food": "食品", "Soda": "软饮料", "Beer": "酒类", "Smoke": "烟草", "Toys": "玩具休闲",
    "Fun": "娱乐", "Books": "出版印刷", "Hshld": "日用消费品", "Clths": "服装", "Hlth": "医疗服务",
    "MedEq": "医疗器械", "Drugs": "制药", "Chems": "化工", "Rubbr": "橡胶塑料", "Txtls": "纺织",
    "BldMt": "建材", "Cnstr": "建筑施工", "Steel": "钢铁", "FabPr": "金属制品", "Mach": "机械",
    "ElcEq": "电气设备", "Autos": "汽车及零件", "Aero": "航空器", "Ships": "造船铁路设备", "Guns": "军工",
    "Gold": "贵金属矿", "Mines": "非贵金属采矿", "Coal": "煤炭", "Oil": "石油天然气", "Util": "公用事业",
    "Telcm": "电信", "PerSv": "个人服务", "BusSv": "商业服务(含互联网)", "Hardw": "计算机硬件",
    "Softw": "软件", "Chips": "电子元件/半导体", "LabEq": "测量仪器", "Paper": "造纸", "Boxes": "包装",
    "Trans": "运输", "Whlsl": "批发", "Rtail": "零售", "Meals": "餐饮酒店", "Banks": "银行", "Insur": "保险",
    "RlEst": "房地产", "Fin": "金融服务", "Other": "其他",
}


def parse_french(path: Path, marker: str | None = None) -> dict:
    lines = path.read_text().splitlines()
    if marker:
        lines = lines[next(i for i, x in enumerate(lines) if marker in x) + 1:]
    start = next(i for i, x in enumerate(lines) if x.strip().startswith(","))
    header = [s.strip() for s in lines[start].split(",")][1:]
    rows = {}
    for line in lines[start + 1:]:
        if not line.strip():
            continue
        bits = [x.strip() for x in line.split(",")]
        if len(bits[0]) == 6 and bits[0].isdigit():
            rows[bits[0]] = {k: float(v) / 100 for k, v in zip(header, bits[1:]) if float(v) not in (-99.99, -999)}
        elif rows:
            break
    return rows


def wealth(rs):
    w = 1.0
    for r in rs:
        w *= 1 + r
    return w


def industry_layer():
    vw = parse_french(RAW / "french/ff49.txt", "Average Value Weighted Returns -- Monthly")
    fac = parse_french(RAW / "french/factors.txt")
    months = [m for m in sorted(set(vw) & set(fac)) if m >= "198101"]
    inds = [k for k in CN if all(k in vw[m] for m in months)]
    mkt = [fac[m]["Mkt-RF"] + fac[m]["RF"] for m in months]
    ret = {k: [vw[m][k] for m in months] for k in inds}
    idx = {m: i for i, m in enumerate(months)}

    def rel(k, a, b):  # 相对市场财富，月份下标 [a, b)
        return wealth(ret[k][a:b]) / wealth(mkt[a:b])

    # ---------- A1 每年最热行业（过去 60 个月）→ 之后 60 个月
    annual = []
    for y in range(1985, 2026):
        end = idx[f"{y}12"] + 1
        if end - 60 < 0:
            continue
        trail = sorted(((rel(k, end - 60, end), k) for k in inds), reverse=True)
        trail3 = sorted(((rel(k, end - 36, end), k) for k in inds), reverse=True)
        fwd_n = min(60, len(months) - end)
        row = {"year": y, "hot5": trail[0][1], "hot5_rel": trail[0][0], "top3_5y": [k for _, k in trail[:3]],
               "cold5": trail[-1][1], "cold5_rel": trail[-1][0], "hot3": trail3[0][1], "hot3_rel": trail3[0][0],
               "fwd_months": fwd_n}
        if fwd_n >= 12:
            f = {k: rel(k, end, end + fwd_n) for k in inds}
            med = statistics.median(f.values())
            row.update({"hot5_fwd_rel": f[row["hot5"]], "cold5_fwd_rel": f[row["cold5"]],
                        "top3_fwd_rel": statistics.mean(f[k] for k in row["top3_5y"]),
                        "hot3_fwd_rel": f[row["hot3"]], "all_median_fwd_rel": med,
                        "hot5_fwd_rank": 1 + sorted(f.values(), reverse=True).index(f[row["hot5"]])})
            # 之后 60 个月内，最热行业绝对总回报指数的最大回撤
            w = pk = 1.0
            dd = 0.0
            for r in ret[row["hot5"]][end:end + fwd_n]:
                w *= 1 + r
                pk = max(pk, w)
                dd = min(dd, w / pk - 1)
            row["hot5_fwd_maxdd"] = dd
        annual.append(row)
    full = [r for r in annual if r["fwd_months"] == 60]
    a1 = {
        "formation_years_full_5y": f'{full[0]["year"]}-{full[-1]["year"]}', "n": len(full),
        "hot_underperformed_next5y": sum(r["hot5_fwd_rel"] < 1 for r in full),
        "hot_median_fwd_rel": statistics.median(r["hot5_fwd_rel"] for r in full),
        "top3_median_fwd_rel": statistics.median(r["top3_fwd_rel"] for r in full),
        "cold_median_fwd_rel": statistics.median(r["cold5_fwd_rel"] for r in full),
        "cold_beat_hot": sum(r["cold5_fwd_rel"] > r["hot5_fwd_rel"] for r in full),
        "all_median_fwd_rel": statistics.median(r["all_median_fwd_rel"] for r in full),
        "hot_fwd_rank_median": statistics.median(r["hot5_fwd_rank"] for r in full),
        "n_industries": len(inds),
    }

    # ---------- A2 行业暴涨事件：36 个月绝对总回报 ≥2.5 倍 且 相对市场 ≥2.0 倍
    ABS, REL, BUST, TAIL = 2.5, 2.0, -0.30, 24
    events = []
    for k in inds:
        tr, w = [], 1.0
        for r in ret[k]:
            w *= 1 + r
            tr.append(w)
        hits = [i for i in range(36, len(months) + 1)  # i = 窗口终点(不含)
                if wealth(ret[k][i - 36:i]) >= ABS and rel(k, i - 36, i) >= REL]
        # 一个“暴涨时代”：从信号开始，信号间隔 ≤GAP 个月则延续；顶点后一旦回撤 ≥30% 即视为该时代结束（崩）。
        # 下一个时代须从上一时代谷底之后的信号重新开始（避免下跌途中残留信号被当成新热潮）。
        hit = sorted(i - 1 for i in hits)  # 月份下标
        hs, nxt = set(hit), 0
        while nxt < len(hit):
            s = last = hit[nxt]
            p, bust, j = s, None, s
            while j < len(months) and j <= last + TAIL:
                if j in hs:
                    last = j
                if tr[j] > tr[p]:
                    p = j
                if tr[j] / tr[p] - 1 <= BUST:
                    bust = j
                    break
                j += 1
            trough, dd, rec = p, 0.0, None
            for j2 in range(p + 1, len(months)):
                if tr[j2] >= tr[p]:
                    rec = j2
                    break
                if tr[j2] / tr[p] - 1 < dd:
                    dd, trough = tr[j2] / tr[p] - 1, j2
            dd5 = min([tr[x] / tr[p] - 1 for x in range(p, min(len(months), p + 61))] + [0.0])  # 顶后 5 年内最大回撤
            g = [h + 1 for h in hit if s <= h <= last]  # 窗口终点(不含)
            nxt = next((n for n, h in enumerate(hit) if h > max(trough, last)), len(hit))
            events.append({
                "industry": k, "industry_cn": CN[k], "first_signal": months[s], "last_signal": months[last],
                "abs36_max": max(wealth(ret[k][i - 36:i]) for i in g),
                "rel36_max": max(rel(k, i - 36, i) for i in g),
                "busted": dd <= BUST, "window_open": bust is None and last + TAIL >= len(months) - 1, "peak": months[p], "trough": months[trough], "maxdd": dd,
                "maxdd_5y_after_peak": dd5, "months_signal_to_peak": p - s, "months_peak_to_trough": trough - p,
                "recovered": months[rec] if rec is not None else None,
                "months_to_recover": (rec - p) if rec is not None else None,
                "months_since_peak_unrecovered": None if rec is not None else len(months) - 1 - p,
                "rel_5y_after_peak": rel(k, p + 1, p + 61) if p + 61 <= len(months) else None,
                # 公平口径：首个信号月（当时就能看到“已经暴涨”）买入，之后 5 年
                "abs_5y_after_signal": wealth(ret[k][s + 1:s + 61]) if s + 61 <= len(months) else None,
                "rel_5y_after_signal": rel(k, s + 1, s + 61) if s + 61 <= len(months) else None,
                "maxdd_after_signal_5y": min([tr[x] / tr[s] - 1 for x in range(s, min(len(months), s + 61))] + [0.0]),
                "rel_after_peak_to_now": rel(k, p + 1, len(months)),
                "months_after_peak_available": len(months) - 1 - p,
            })
    events.sort(key=lambda e: e["peak"])
    busted = [e for e in events if e["busted"]]
    a2 = {"n_events": len(events), "n_busted": len(busted),
          "median_maxdd_busted": statistics.median(e["maxdd"] for e in busted) if busted else None,
          "median_months_peak_to_trough": statistics.median(e["months_peak_to_trough"] for e in busted) if busted else None,
          "n_recovered": sum(e["recovered"] is not None for e in busted),
          "median_months_to_recover": statistics.median(e["months_to_recover"] for e in busted if e["months_to_recover"]) if busted else None,
          "rel5_after_peak_below1": sum(1 for e in events if e["rel_5y_after_peak"] is not None and e["rel_5y_after_peak"] < 1),
          "rel5_after_peak_n": sum(1 for e in events if e["rel_5y_after_peak"] is not None),
          "signal_n_5y": sum(1 for e in events if e["rel_5y_after_signal"] is not None),
          "signal_rel5_below1": sum(1 for e in events if e["rel_5y_after_signal"] is not None and e["rel_5y_after_signal"] < 1),
          "signal_rel5_median": statistics.median(e["rel_5y_after_signal"] for e in events if e["rel_5y_after_signal"] is not None),
          "signal_abs5_below1": sum(1 for e in events if e["abs_5y_after_signal"] is not None and e["abs_5y_after_signal"] < 1),
          "signal_maxdd_median": statistics.median(e["maxdd_after_signal_5y"] for e in events if e["rel_5y_after_signal"] is not None)}
    out = {"source": "Kenneth French 49 Industry Portfolios (VW, monthly, CRSP 202607)", "start": months[0],
           "end": months[-1], "industries": inds, "annual": annual, "a1_summary": a1, "bubble_events": events,
           "a2_summary": a2,
           "rule_a2": (f"信号=36 个月总回报 ≥{ABS} 倍且相对市场 ≥{REL} 倍；从首个信号起，只要末信号后 {TAIL} 个月内还有新信号就延续；"
                       f"期间顶点后一旦回撤 ≥{-BUST:.0%}，该暴涨时代即告结束（记为崩），下一时代须从谷底之后的信号重新开始；"
                       "月末总回报指数（含股息），月内极值更深")}
    (BASE / "data/industry_fads.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def load_px(tk):
    fn = RAW / "prices" / (tk.replace("^", "IDX_") + ".csv.gz")
    rows = list(csv.DictReader(io.StringIO(gzip.decompress(fn.read_bytes()).decode())))
    return [(r["date"], float(r["close"]), float(r["adjclose"])) for r in rows]


def drawdowns(series, start="1985-01-01", thresh=-0.20):
    s = [(d, c) for d, c, _ in series if d >= start]
    out, pk_i, i = [], 0, 0
    n = len(s)
    while i < n:
        if s[i][1] >= s[pk_i][1]:
            pk_i = i
            i += 1
            continue
        # 进入回撤：找收复点或结尾
        j, tr_i = i, i
        while j < n and s[j][1] < s[pk_i][1]:
            if s[j][1] < s[tr_i][1]:
                tr_i = j
            j += 1
        dd = s[tr_i][1] / s[pk_i][1] - 1
        if dd <= thresh:
            out.append({"peak": s[pk_i][0], "peak_close": s[pk_i][1], "trough": s[tr_i][0],
                        "trough_close": s[tr_i][1], "drawdown": dd,
                        "recovered": s[j][0] if j < n else None})
        if j >= n:
            break
        pk_i, i = j, j + 1
    import datetime as dt

    def days(a, b):
        return (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days
    for e in out:
        e["years_peak_to_trough"] = round(days(e["peak"], e["trough"]) / 365.25, 2)
        e["years_peak_to_recover"] = round(days(e["peak"], e["recovered"]) / 365.25, 2) if e["recovered"] else None
    return out


def market_layer():
    res = {}
    for tk in ("^IXIC", "^GSPC", "^NDX"):
        px = load_px(tk)
        res[tk] = {"first": px[0][0], "last": px[-1][0], "last_close": px[-1][1],
                   "drawdowns_ge20": drawdowns(px, start="1985-01-01" if tk != "^NDX" else "1985-10-01")}
    (BASE / "data/market_drawdowns.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


if __name__ == "__main__":
    ind = industry_layer()
    s = ind["a1_summary"]
    print("A1", json.dumps(s, ensure_ascii=False))
    for r in ind["annual"]:
        print(r["year"], f'{r["hot5"]:6s}{CN[r["hot5"]]:10s} 过去5y相对 {r["hot5_rel"]:.2f}x',
              f'→ 之后{r["fwd_months"]}m 相对 {r.get("hot5_fwd_rel", float("nan")):.2f}x 排名 {r.get("hot5_fwd_rank")}',
              f'| 最冷 {r["cold5"]:6s} → {r.get("cold5_fwd_rel", float("nan")):.2f}x')
    print("\nA2 暴涨事件", json.dumps(ind["a2_summary"], ensure_ascii=False))
    for e in ind["bubble_events"]:
        print(f'{e["industry"]:6s}{e["industry_cn"]:10s} 信号 {e["first_signal"]} 顶 {e["peak"]} {"崩" if e["busted"] else "未崩"} 36m {e["abs36_max"]:.1f}x/相对{e["rel36_max"]:.2f}x',
              f'回撤 {e["maxdd"]:.0%} 用 {e["months_peak_to_trough"]}m 收复 {e["recovered"]} ({e["months_to_recover"]}m)',
              f'顶后5y相对 {e["rel_5y_after_peak"] if e["rel_5y_after_peak"] is None else round(e["rel_5y_after_peak"], 2)}')
    mk = market_layer()
    for tk, v in mk.items():
        print("\n", tk)
        for e in v["drawdowns_ge20"]:
            print(f'  {e["peak"]} {e["peak_close"]:.0f} → {e["trough"]} {e["drawdown"]:.0%} ({e["years_peak_to_trough"]}y) 收复 {e["recovered"]} ({e["years_peak_to_recover"]}y)')
