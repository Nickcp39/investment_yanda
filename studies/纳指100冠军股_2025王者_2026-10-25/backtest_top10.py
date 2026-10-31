"""回测：每年年初买入上一年涨幅前十（每只 10%），持有一年，年底换仓。起始 $100。

两个股票池（都用 point-in-time 年初成分股名单）：
- 纳指100：名单 2006 起 → 持有年 2007–2026（20 年）
- 标普500：名单 1996 起 → 持有年 1997–2026（30 年）
2026 只到 2026-10-22（数据集最后一天），按部分年计。

涨幅：data/sp500_ndx_constituents/annual_returns.csv（Yahoo 复权，含分红拆股，年末/上年末 − 1）。
基准：SPY、QQQ 复权收盘（data/market_temp）。
对照：同一年所有"有数据"的成分股等权平均。它和策略带着同样的幸存者偏差，
      所以「策略 − 对照」才是"买去年前十"这个动作本身的效果。
不计交易成本和税。
运行：python backtest_top10.py → 打印，写 backtest_yearly.csv、backtest_summary.json、backtest_top10.png
"""
import csv
import datetime as dt
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
D = ROOT / "data" / "sp500_ndx_constituents"
MT = ROOT / "data" / "market_temp"
AS_OF = dt.date(2026, 10, 22)
N = 10
# 同一家公司的多类股：只保留一个
SAME = {"GOOG": "GOOGL", "FOX": "FOXA", "DISCK": "DISCA", "DISCB": "DISCA", "NWS": "NWSA", "CMCSK": "CMCSA",
        "LBTYK": "LBTYA", "LBTYB": "LBTYA", "UA": "UAA", "BF.A": "BF.B", "LILAK": "LILA", "FWONK": "FWONA",
        "LSXMK": "LSXMA", "LSXMB": "LSXMA", "BATRK": "BATRA", "QVCB": "QVCA", "VIA": "VIAB", "HEI.A": "HEI"}

ret = {}
for r in csv.DictReader((D / "annual_returns.csv").open(encoding="utf-8")):
    ret[r["ticker"]] = {int(k): float(v) for k, v in r.items() if k != "ticker" and v not in ("", None)}

# ticker 复用 / 数据错误：这些年份 Yahoo 的价格不是当年那家成分股（见 check_ticker_names.py 与 README），当作缺数据
BAD = {
    "SNT": (0, 9999, "名单是 Sonat，Yahoo SNT 是 Senstar（原 Magal）"),
    "WEN": (0, 2008, "2008-09 前 Yahoo WEN 是 Triarc 的历史，不是 Wendy's International"),
    "CB": (0, 2015, "2016 前 Yahoo CB 是 ACE 的历史，不是 Chubb Corp"),
    "EP": (0, 9999, "名单是 El Paso，Yahoo EP 是 Empire Petroleum（仙股）"),
    "BBT": (0, 9999, "名单是 BB&T，Yahoo BBT 是 Beacon Financial（原 Berkshire Hills）"),
    "IR": (0, 2020, "2020-03 前 Yahoo IR 是 Gardner Denver 的历史，不是老 Ingersoll-Rand（今 TT）"),
    "DLX": (2000, 2001, "eFunds 分拆的复权错位，2001 年 +189% 实为约 +70%"),
}
for t, (lo, hi, _) in BAD.items():
    for y in [y for y in ret.get(t, {}) if lo <= y <= hi]:
        del ret[t][y]


def lists(f):
    return {int(r[0]): [t for t in r[1].split(",") if t] for r in list(csv.reader((D / f).open(encoding="utf-8")))[1:]}


def bench(name):
    s = {}
    for r in csv.DictReader((MT / f"{name}_daily.csv").open(encoding="utf-8")):
        d = dt.date.fromisoformat(r["date"])
        if d <= AS_OF and r["adj_close"]:
            s[d] = float(r["adj_close"])
    ds = sorted(s)
    ye = {}
    for d in ds:
        ye[d.year] = s[d]
    return {y: ye[y] / ye[y - 1] - 1 for y in ye if y - 1 in ye}


def run(universe, yl, bench_name):
    b = bench(bench_name)
    years = [y for y in sorted(yl) if y - 1 in yl and y <= AS_OF.year]
    v_s = v_b = v_e = 100.0
    rows = []
    missing_hold = []
    for h in years:
        pool = yl[h - 1]
        cand = sorted(((ret[t][h - 1], t) for t in pool if t in ret and h - 1 in ret[t]), reverse=True)
        picks, seen = [], set()
        for r0, t in cand:
            key = SAME.get(t, t)
            if key in seen:
                continue
            seen.add(key)
            picks.append((t, r0))
            if len(picks) == N:
                break
        hold = []
        for t, r0 in picks:
            rh = ret.get(t, {}).get(h)
            if rh is None:
                missing_hold.append((h, t))
                rh = -1.0  # 保守：持有年没数据按 −100%（实际几乎没有这种情况，见输出）
            hold.append(rh)
        rs = float(np.mean(hold))
        members_h = yl[h]
        ew = [ret[t][h] for t in members_h if t in ret and h in ret[t]]
        re_ = float(np.mean(ew))
        rb = b[h]
        v_s *= 1 + rs
        v_b *= 1 + rb
        v_e *= 1 + re_
        rows.append({"universe": universe, "year": h, "picks": ";".join(f"{t}:{r0:+.0%}→{rh:+.0%}" for (t, r0), rh in zip(picks, hold)),
                     "strategy": rs, "bench": rb, "ew_control": re_, "v_strategy": v_s, "v_bench": v_b, "v_ew": v_e,
                     "coverage_pick_year": len(cand) / len(pool), "n_pool": len(pool),
                     "beat_bench": rs > rb, "partial": h == AS_OF.year})
    return rows, missing_hold


def stats(rows, key, vkey):
    yrs = len(rows) - 1 + ((AS_OF - dt.date(AS_OF.year - 1, 12, 31)).days / 365.25 if rows[-1]["partial"] else 1)
    vals = [100.0] + [r[vkey] for r in rows]
    peak, mdd = vals[0], 0.0
    for v in vals:
        peak = max(peak, v)
        mdd = min(mdd, v / peak - 1)
    rr = [r[key] for r in rows]
    full = [r for r in rows if not r["partial"]]
    return {"final": vals[-1], "years": yrs, "cagr": (vals[-1] / 100) ** (1 / yrs) - 1, "max_dd_annual": mdd,
            "best": max(rr), "best_year": rows[int(np.argmax(rr))]["year"], "worst": min(rr), "worst_year": rows[int(np.argmin(rr))]["year"],
            "neg_years": sum(x < 0 for x in rr), "median_full_year": float(np.median([r[key] for r in full]))}


out = {}
all_rows = []
for universe, f, bn, label in [("NDX100", "ndx100_yearly_constituents.csv", "QQQ", "纳指100"),
                               ("SP500", "sp500_yearly_constituents.csv", "SPY", "标普500")]:
    rows, miss = run(universe, lists(f), bn)
    all_rows += rows
    s = {k: stats(rows, k, v) for k, v in [("strategy", "v_strategy"), ("bench", "v_bench"), ("ew_control", "v_ew")]}
    beat = sum(r["beat_bench"] for r in rows)
    beat_ew = sum(r["strategy"] > r["ew_control"] for r in rows)
    out[universe] = {"stats": s, "beat_bench_years": beat, "beat_ew_years": beat_ew, "n_years": len(rows),
                     "missing_hold": miss, "first_year": rows[0]["year"]}
    print(f"\n==================== {label} 前十策略 vs {bn}（持有年 {rows[0]['year']}–{rows[-1]['year']}，2026 至 {AS_OF}）====================")
    print("年份  策略      " + f"{bn:6s}    同口径等权  选股年数据覆盖  前十（上一年涨幅 → 持有年涨幅）")
    for r in rows:
        mark = "✓" if r["beat_bench"] else " "
        print(f"{r['year']}{'*' if r['partial'] else ' '} {r['strategy']:+7.1%} {mark} {r['bench']:+7.1%}  {r['ew_control']:+7.1%}     {r['coverage_pick_year']:4.0%}    {r['picks']}")
    for k, nm in [("strategy", "前十策略"), ("bench", bn), ("ew_control", "同口径等权")]:
        x = s[k]
        print(f"  {nm:8s}: $100 → ${x['final']:>12,.0f}   年化 {x['cagr']:+6.1%}   最大年度回撤 {x['max_dd_annual']:+6.1%}   "
              f"最好 {x['best']:+.0%}（{x['best_year']}） 最差 {x['worst']:+.0%}（{x['worst_year']}）  亏损年 {x['neg_years']}")
    print(f"  跑赢 {bn} 的年份：{beat}/{len(rows)}；跑赢同口径等权：{beat_ew}/{len(rows)}；持有年缺数据的持仓：{miss or '无'}")
    # 分段：选股年数据覆盖 ≥ 80% 的年份（幸存者偏差小），以及 2009 年以后
    out[universe]["segments"] = {}
    for seg, sub in [("覆盖≥80%", [r for r in rows if r["coverage_pick_year"] >= 0.8]),
                     ("2009 年以后", [r for r in rows if r["year"] >= 2009]),
                     ("覆盖<80%（早期）", [r for r in rows if r["coverage_pick_year"] < 0.8])]:
        if not sub:
            continue
        seg_out = {}
        for k in ("strategy", "bench", "ew_control"):
            v = 100.0
            for r in sub:
                v *= 1 + r[k]
            yrs = len(sub) - 1 + ((AS_OF - dt.date(AS_OF.year - 1, 12, 31)).days / 365.25 if sub[-1]["partial"] else 1)
            seg_out[k] = {"final": v, "cagr": (v / 100) ** (1 / yrs) - 1}
        seg_out["years"] = f"{sub[0]['year']}–{sub[-1]['year']}"
        seg_out["beat"] = f"{sum(r['beat_bench'] for r in sub)}/{len(sub)}"
        out[universe]["segments"][seg] = seg_out
        print(f"  分段 {seg:10s} {seg_out['years']}: 策略 年化 {seg_out['strategy']['cagr']:+6.1%}  {bn} {seg_out['bench']['cagr']:+6.1%}  "
              f"同口径等权 {seg_out['ew_control']['cagr']:+6.1%}  跑赢 {bn} {seg_out['beat']}")

with (HERE / "backtest_yearly.csv").open("w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(all_rows[0]))
    w.writeheader()
    for r in all_rows:
        w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
(HERE / "backtest_summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
print("\n写出 backtest_yearly.csv、backtest_summary.json")
