"""NBIS 大跌的量化拆解：回撤史、波动与 beta、行业 vs 个股归因、历史基率。

数据：Yahoo v8 日线（curl 拉取，存 data/yahoo_*.json，已有不重下）；历史基率用
studies/美股风气40年_兴衰统计_2026-10-06/data/raw/prices/*.csv.gz（239 只风气明星股日线）。
as_of：2026-10-22 收盘（10-23 开盘前运行）。
运行：python quant_drawdown.py → 打印结果，写 data/quant_results.json、data/base_rate_events.csv、quant_drawdown.png
"""
import csv
import datetime as dt
import gzip
import json
import math
import statistics as st
import subprocess
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
D = HERE / "data"
D.mkdir(exist_ok=True)
FADS = HERE.parents[2] / "studies" / "美股风气40年_兴衰统计_2026-10-06" / "data" / "raw" / "prices"
AS_OF = dt.date(2026, 10, 22)
TICKERS = ["NBIS", "QQQ", "SMH", "NVDA", "CRWV", "IREN", "ORCL", "APLD", "^IXIC"]


def yahoo(t):
    f = D / f"yahoo_{t.replace('^', 'IDX_')}.json"
    if not f.exists() or f.stat().st_size < 1000:
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{t.replace('^', '%5E')}"
               "?period1=0&period2=9999999999&interval=1d&includeAdjustedClose=true&events=div,split")
        f.write_bytes(subprocess.run(["curl", "-s", "-m", "60", "-A", "Mozilla/5.0", url], capture_output=True).stdout)
    r = json.loads(f.read_text(encoding="utf-8"))["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0)
    q, adj = r["indicators"]["quote"][0], r["indicators"]["adjclose"][0]["adjclose"]
    out = {}
    for ts, c, a in zip(r["timestamp"], q["close"], adj):
        if c is None:
            continue
        d = dt.datetime.utcfromtimestamp(ts + off).date()
        if d <= AS_OF:
            out[d] = (c, a if a is not None else c)
    return out


px = {t: yahoo(t) for t in TICKERS}
for t in TICKERS:
    ds = sorted(px[t])
    print(f"{t:6s} {ds[0]} → {ds[-1]}  last close {px[t][ds[-1]][0]:.2f}  n={len(ds)}")

nb = {d: v for d, v in px["NBIS"].items() if d >= dt.date(2024, 10, 21)}  # 复牌后（此前为 YNDX）
nd = sorted(nb)
nclose = np.array([nb[d][0] for d in nd])
res = {"as_of": str(AS_OF), "last_close": float(nclose[-1])}


def close_on(t, d, adj=True):
    """d 当日或之前最近一个交易日的收盘（默认复权价）。"""
    s = px[t]
    while d not in s:
        d -= dt.timedelta(days=1)
    return s[d][1 if adj else 0]


# ---------- 1. 价格窗口
peak_i = int(nclose.argmax())
peak_d, peak_p = nd[peak_i], float(nclose[peak_i])
windows = {
    "NBIS 收盘高点以来（%s）" % peak_d: peak_d,
    "10-06 以来（本轮科技抛售起点）": dt.date(2026, 10, 6),
    "09-04（上上张卡）以来": dt.date(2026, 9, 4),
    "10-16（上一张卡 as_of）以来": dt.date(2026, 10, 16),
    "年初以来": dt.date(2025, 12, 31),
}
print(f"\nNBIS 复牌后收盘最高 {peak_p:.2f}（{peak_d}），as_of {nclose[-1]:.2f}，距高点 {nclose[-1] / peak_p - 1:+.1%}")
res["peak"] = {"date": str(peak_d), "close": peak_p, "dd": float(nclose[-1] / peak_p - 1)}
res["windows"] = {}
print("\n窗口涨跌（复权）：", "  ".join(f"{t:>6s}" for t in TICKERS[:-1]))
for name, d0 in windows.items():
    row = {}
    for t in TICKERS[:-1]:
        try:
            row[t] = close_on(t, AS_OF) / close_on(t, d0) - 1
        except KeyError:
            row[t] = None
    res["windows"][name] = row
    print(f"  {name:28s}", "  ".join(f"{v:+6.1%}" if v is not None else "   n/a" for v in row.values()))

print("\nNBIS 近期日线：")
res["recent"] = []
for d in nd:
    if d >= dt.date(2026, 10, 1):
        i = nd.index(d)
        r = nclose[i] / nclose[i - 1] - 1
        res["recent"].append({"date": str(d), "close": float(nclose[i]), "ret": float(r)})
        print(f"  {d} {nclose[i]:8.2f} {r:+6.1%}")

# ---------- 2. 回撤史（复牌后，深度 ≥ 25% 的峰谷段）
episodes, i = [], 0
run_max_i = 0
in_dd = False
for k in range(1, len(nclose)):
    if nclose[k] > nclose[run_max_i]:
        if in_dd:
            tr = run_max_i + int(nclose[run_max_i:k].argmin())
            depth = nclose[tr] / nclose[run_max_i] - 1
            if depth <= -0.25:
                episodes.append((run_max_i, tr, k))
            in_dd = False
        run_max_i = k
    elif nclose[k] < nclose[run_max_i] * 0.999:
        in_dd = True
if in_dd:
    tr = run_max_i + int(nclose[run_max_i:].argmin())
    if nclose[tr] / nclose[run_max_i] - 1 <= -0.25:
        episodes.append((run_max_i, tr, None))
print("\n复牌以来回撤 ≥25% 的段：")
res["episodes"] = []
for p, tr, rec in episodes:
    e = {"peak": str(nd[p]), "peak_close": float(nclose[p]), "trough": str(nd[tr]), "trough_close": float(nclose[tr]),
         "depth": float(nclose[tr] / nclose[p] - 1), "days_to_trough": (nd[tr] - nd[p]).days,
         "recovered": str(nd[rec]) if rec else None, "days_trough_to_recover": (nd[rec] - nd[tr]).days if rec else None}
    res["episodes"].append(e)
    print(f"  顶 {e['peak']} {e['peak_close']:.2f} → 底 {e['trough']} {e['trough_close']:.2f}  {e['depth']:+.1%}"
          f"  用 {e['days_to_trough']} 天；收复 {e['recovered'] or '未收复'}"
          + (f"（底后 {e['days_trough_to_recover']} 天）" if rec else ""))

# ---------- 3. 波动与 beta（日对数收益）


def logret(t, d0, d1):
    s = px[t]
    ds = [d for d in sorted(s) if d0 <= d <= d1]
    return {ds[k]: math.log(s[ds[k]][1] / s[ds[k - 1]][1]) for k in range(1, len(ds))}


def aligned(ts, d0, d1):
    rs = [logret(t, d0, d1) for t in ts]
    common = sorted(set.intersection(*[set(r) for r in rs]))
    return common, np.array([[r[d] for d in common] for r in rs])


yr0 = AS_OF - dt.timedelta(days=365)
res["vol"] = {}
for t in ["NBIS", "CRWV", "IREN", "NVDA", "SMH", "QQQ"]:
    r = np.array(list(logret(t, yr0, AS_OF).values()))
    res["vol"][t] = float(r.std(ddof=1) * math.sqrt(252))
print("\n近一年年化波动：", "  ".join(f"{t} {v:.0%}" for t, v in res["vol"].items()))

res["beta"] = {}
for f in ["QQQ", "SMH", "CRWV"]:
    _, m = aligned(["NBIS", f], yr0, AS_OF)
    b = np.cov(m[0], m[1])[0, 1] / m[1].var(ddof=1)
    c = np.corrcoef(m[0], m[1])[0, 1]
    res["beta"][f] = {"beta": float(b), "corr": float(c), "n": int(m.shape[1])}
print("NBIS 对各因子（近一年）：", "  ".join(f"{f} β={v['beta']:.2f} ρ={v['corr']:.2f}" for f, v in res["beta"].items()))

# ---------- 4. 归因：估计窗用高点之前一年（不偷看下跌段），双因子 SMH + CRWV
est0, est1 = peak_d - dt.timedelta(days=365), peak_d
_, m = aligned(["NBIS", "SMH", "CRWV"], est0, est1)
X = np.column_stack([np.ones(m.shape[1]), m[1], m[2]])
coef, *_ = np.linalg.lstsq(X, m[0], rcond=None)
resid_sd = float((m[0] - X @ coef).std(ddof=3))
r2 = 1 - ((m[0] - X @ coef) ** 2).sum() / ((m[0] - m[0].mean()) ** 2).sum()
print(f"\n归因模型（估计窗 {est0}→{est1}，n={m.shape[1]}）：NBIS = {coef[0] * 252:+.0%}/年 + {coef[1]:.2f}×SMH + {coef[2]:.2f}×CRWV，R²={r2:.2f}")
res["attribution_model"] = {"window": [str(est0), str(est1)], "b_smh": float(coef[1]), "b_crwv": float(coef[2]), "r2": float(r2)}
res["attribution"] = {}
for name, d0 in [("高点以来", peak_d), ("10-06 以来", dt.date(2026, 10, 6))]:
    _, w = aligned(["NBIS", "SMH", "CRWV"], d0, AS_OF)
    act, smh, crwv = w.sum(axis=1)
    exp_smh, exp_crwv = coef[1] * smh, coef[2] * crwv  # 不计截距：截距是上涨期的超额，不应外推
    resid = act - exp_smh - exp_crwv
    n = w.shape[1]
    z = resid / (resid_sd * math.sqrt(n))
    a = {"actual": math.expm1(act), "smh_part_log": float(exp_smh), "crwv_part_log": float(exp_crwv),
         "resid_log": float(resid), "resid_z": float(z), "days": n,
         "smh_move": math.expm1(smh), "crwv_move": math.expm1(crwv)}
    res["attribution"][name] = a
    print(f"  {name}（{n} 个交易日）：实际 {a['actual']:+.1%}（对数 {act:+.3f}）= SMH 部分 {exp_smh:+.3f}"
          f"（SMH {a['smh_move']:+.1%}）+ CRWV 部分 {exp_crwv:+.3f}（CRWV {a['crwv_move']:+.1%}）+ 个股残差 {resid:+.3f}（z={z:+.1f}）")

# 单因子对照：只用 SMH
_, m1 = aligned(["NBIS", "SMH"], est0, est1)
b1 = np.cov(m1[0], m1[1])[0, 1] / m1[1].var(ddof=1)
res["attribution_smh_only_beta"] = float(b1)
for name, d0 in [("高点以来", peak_d), ("10-06 以来", dt.date(2026, 10, 6))]:
    _, w = aligned(["NBIS", "SMH"], d0, AS_OF)
    act, smh = w.sum(axis=1)
    res["attribution"][name]["smh_only_resid_log"] = float(act - b1 * smh)
    print(f"  只用 SMH（β={b1:.2f}）{name}：个股残差 {act - b1 * smh:+.3f}")

# 这次回撤以本股的波动看算多大
sig = res["vol"]["NBIS"]
dd_days = len([d for d in nd if d > peak_d])
res["dd_in_sigma"] = float(math.log(nclose[-1] / peak_p) / (sig * math.sqrt(dd_days / 252)))
print(f"\n从高点到今天 {dd_days} 个交易日，对数跌幅 / (年化波动×√时长) = {res['dd_in_sigma']:.2f} σ")

# ---------- 5. 历史基率：风气明星股「一年内涨 ≥3 倍、创新高后 6 个月内跌去 45%」之后发生了什么


def load_fads(path):
    rows = list(csv.DictReader(gzip.open(path, "rt", encoding="utf-8")))
    ds = [dt.date.fromisoformat(r["date"]) for r in rows]
    a = np.array([float(r["adjclose"] or r["close"]) for r in rows])
    return ds, a


ixic = px["^IXIC"]
ixd = sorted(ixic)
ixa = np.array([ixic[d][0] for d in ixd])
ix_runmax = np.maximum.accumulate(ixa)
ix_dd = {d: ixa[k] / ix_runmax[k] - 1 for k, d in enumerate(ixd)}


def ixic_dd(d):
    while d not in ix_dd and d > ixd[0]:
        d -= dt.timedelta(days=1)
    return ix_dd.get(d)


events = []
HZ = {"6m": 126, "12m": 252, "24m": 504, "36m": 756}
for f in sorted(FADS.glob("*.csv.gz")):
    tk = f.name[:-7]
    if tk == "NBIS":
        continue
    try:
        ds, a = load_fads(f)
    except Exception:
        continue
    if len(a) < 400:
        continue
    k, last_peak_used = 252, -1
    runmax = np.maximum.accumulate(a)
    while k < len(a):
        # k 是创新高日，且相对一年内最低点 ≥ 3 倍
        if a[k] >= runmax[k] and a[k] / a[k - 252:k].min() >= 3 and k > last_peak_used:
            # 从这个高点往后：在再创新高之前，6 个月内是否跌破 55%
            pk = k
            j = k + 1
            hit = None
            while j < len(a) and j <= pk + 126:
                if a[j] > a[pk]:
                    pk = j  # 高点被刷新，窗口从新高点重算
                elif a[j] <= 0.55 * a[pk]:
                    hit = j
                    break
                j += 1
            if hit is None:
                k = max(k + 1, j)
                continue
            e = {"ticker": tk, "peak_date": str(ds[pk]), "event_date": str(ds[hit]), "days_peak_to_event": hit - pk,
                 "run_up_x": float(a[pk] / a[max(0, pk - 252):pk].min()), "ixic_dd": ixic_dd(ds[hit])}
            for h, n in HZ.items():
                e[f"fwd_{h}"] = float(a[hit + n] / a[hit] - 1) if hit + n < len(a) else None
            e["min_fwd_12m"] = float(a[hit:hit + 253].min() / a[hit] - 1)
            rec = next((m for m in range(hit, len(a)) if a[m] > a[pk]), None)
            e["recover_days"] = (ds[rec] - ds[hit]).days if rec else None
            e["data_end"] = str(ds[-1])
            events.append(e)
            last_peak_used = pk
            # 下一个事件要求重新创新高
            k = next((m for m in range(hit, len(a)) if a[m] > a[pk]), len(a))
            continue
        k += 1

def summarize(evs, label):
    out = {"label": label, "n": len(evs)}
    for h in HZ:
        v = [e[f"fwd_{h}"] for e in evs if e[f"fwd_{h}"] is not None]
        if len(v) >= 5:
            q = np.percentile(v, [25, 50, 75])
            out[h] = {"n": len(v), "p25": float(q[0]), "median": float(q[1]), "p75": float(q[2]),
                      "pos": float(np.mean(np.array(v) > 0)), "gt50": float(np.mean(np.array(v) > 0.5)),
                      "lt_m50": float(np.mean(np.array(v) < -0.5)), "missing": len(evs) - len(v)}
    mf = [e["min_fwd_12m"] for e in evs]
    out["min_fwd_12m_median"] = float(np.median(mf))
    out["further_dd_25_share"] = float(np.mean(np.array(mf) <= -0.25))
    for yrs in (1, 3, 5):
        out[f"recover_{yrs}y"] = float(np.mean([e["recover_days"] is not None and e["recover_days"] <= 365 * yrs for e in evs]))
    return out


ctab = HERE.parents[2] / "studies" / "美股风气40年_兴衰统计_2026-10-06" / "data" / "companies_table.csv"
role = {}
for r in csv.DictReader(ctab.open(encoding="utf-8-sig")):
    role.setdefault(r["yahoo"], r["role"])
for e in events:
    e["role"] = role.get(e["ticker"], "")
with open(D / "base_rate_events.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(events[0]))
    w.writeheader()
    w.writerows(events)

# NBIS 自己按同一规则的触发日（高点后第一次收盘 ≤ 高点 × 0.55）
trig = next(d for d in nd if d > peak_d and nb[d][0] <= 0.55 * peak_p)
res["nbis_trigger"] = {"date": str(trig), "close": nb[trig][0], "threshold": 0.55 * peak_p,
                       "since_trigger": float(nclose[-1] / nb[trig][0] - 1), "ixic_dd_now": ixic_dd(AS_OF)}
print(f"\nNBIS 按同一规则的触发日：{trig}（收盘 {nb[trig][0]:.2f}，阈值 {0.55 * peak_p:.2f}），触发后至今 {res['nbis_trigger']['since_trigger']:+.1%}；"
      f"纳指当前距高点 {ixic_dd(AS_OF):+.1%}")

groups = [
    ("全部事件", events),
    ("卖铲子 / 基础设施角色", [e for e in events if "卖铲子" in e["role"] or "矿工" in e["role"]]),
    ("主题龙头", [e for e in events if "龙头" in e["role"]]),
    ("纳指当时回撤 < 15%（个股/板块式崩，像现在）", [e for e in events if e["ixic_dd"] is not None and e["ixic_dd"] > -0.15]),
    ("纳指当时回撤 ≥ 15%（大盘一起崩）", [e for e in events if e["ixic_dd"] is not None and e["ixic_dd"] <= -0.15]),
    ("2009 年以后", [e for e in events if e["event_date"] >= "2009-01-01"]),
]
res["base_rate"] = [summarize(g, lab) for lab, g in groups if len(g) >= 5]
res["base_rate_n_tickers"] = len({e["ticker"] for e in events})
print(f"\n历史基率：{len(events)} 个事件，{res['base_rate_n_tickers']} 只股票（来自 {len(list(FADS.glob('*.csv.gz')))} 只风气明星股）")
for s in res["base_rate"]:
    print(f"  【{s['label']}】n={s['n']}  之后 12 个月内再跌 ≥25% 的比例 {s['further_dd_25_share']:.0%}，"
          f"12 个月内最低点中位数 {s['min_fwd_12m_median']:+.0%}；1/3/5 年内收复前高 {s['recover_1y']:.0%}/{s['recover_3y']:.0%}/{s['recover_5y']:.0%}")
    for h in HZ:
        if h in s:
            v = s[h]
            print(f"     {h:>3s}: n={v['n']:3d} 中位数 {v['median']:+.0%}（四分位 {v['p25']:+.0%} ~ {v['p75']:+.0%}），"
                  f"为正 {v['pos']:.0%}，>+50% {v['gt50']:.0%}，<−50% {v['lt_m50']:.0%}，数据缺失 {v['missing']}")

(D / "quant_results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

# ---------- 6. 图
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 8.5,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 160})
fig, axs = plt.subplots(2, 2, figsize=(11, 7))

ax = axs[0][0]
ax.plot(nd, nclose, color="#235e7c", lw=1.2)
ax.axhspan(150, 180, color="#2e8b57", alpha=0.12, label="卡上买入带 $150–180")
ax.axhline(313.46, color="#b9484a", lw=0.8, ls="--", label="2030 可转债转股价 $313")
ax.axhline(223.90, color="#999", lw=0.8, ls=":", label="可转债定价参考价 $223.9")
ax.scatter([peak_d, nd[-1]], [peak_p, nclose[-1]], color="#b9484a", s=14, zorder=3)
ax.annotate(f"{peak_p:.0f}\n{peak_d:%m-%d}", (peak_d, peak_p), xytext=(-34, -8), textcoords="offset points", fontsize=7.5)
ax.annotate(f"{nclose[-1]:.0f}", (nd[-1], nclose[-1]), xytext=(4, -10), textcoords="offset points", fontsize=7.5)
ax.set_title("NBIS 复牌以来收盘价（美元）", loc="left", fontweight="bold", fontsize=9.5)
ax.set_ylim(0, 345)
ax.legend(fontsize=7, frameon=False, loc="center left", bbox_to_anchor=(0.0, 0.55))
ax.grid(alpha=0.25)

ax = axs[0][1]
cols = {"NBIS": "#235e7c", "CRWV": "#b9484a", "IREN": "#c98a2b", "NVDA": "#2e8b57", "SMH": "#7a5aa6", "QQQ": "#555"}
d0 = dt.date(2026, 6, 1)
for t, c in cols.items():
    s = {d: v[1] for d, v in px[t].items() if d >= d0}
    ds = sorted(s)
    base = s[ds[0]]
    ax.plot(ds, [s[d] / base * 100 for d in ds], color=c, lw=1.5 if t == "NBIS" else 1.0, label=t)
ax.axvline(dt.date(2026, 10, 6), color="#999", lw=0.7, ls="--")
ax.set_title("2026-06-01 = 100：NBIS 与同业、芯片、纳指", loc="left", fontweight="bold", fontsize=9.5)
ax.legend(fontsize=7, frameon=False, ncol=3)
ax.grid(alpha=0.25)

ax = axs[1][0]
a = res["attribution"]
labels = list(a)
x = np.arange(len(labels))
parts = [("SMH（芯片板块）部分", "smh_part_log", "#7a5aa6"), ("CRWV（同业信用）部分", "crwv_part_log", "#b9484a"),
         ("个股残差", "resid_log", "#235e7c")]
bottom_neg = np.zeros(len(labels))
bottom_pos = np.zeros(len(labels))
for lab, key, c in parts:
    v = np.array([a[n][key] for n in labels])
    b = np.where(v < 0, bottom_neg, bottom_pos)
    ax.bar(x, v, bottom=b, color=c, width=0.5, label=lab)
    bottom_neg += np.where(v < 0, v, 0)
    bottom_pos += np.where(v >= 0, v, 0)
for k, n in enumerate(labels):
    act = math.log1p(a[n]["actual"])
    ax.plot([k - 0.3, k + 0.3], [act, act], color="k", lw=1.5)
    ax.annotate(f"实际 {a[n]['actual']:+.0%}", (k + 0.3, act), xytext=(3, -3), textcoords="offset points", fontsize=7.5)
ax.axhline(0, color="#555", lw=0.7)
ax.set_xticks(x, labels)
ax.set_ylabel("对数收益")
ax.set_title(f"跌幅归因（β 用高点前一年估：SMH {coef[1]:.2f}，CRWV {coef[2]:.2f}）", loc="left", fontweight="bold", fontsize=9.5)
ax.legend(fontsize=7, frameon=False, loc="center", bbox_to_anchor=(0.5, 0.3))
ax.grid(alpha=0.25, axis="y")

ax = axs[1][1]
v = [e["fwd_12m"] for e in events if e["fwd_12m"] is not None]
bins = np.linspace(-1, 3, 33)
ax.hist(np.clip(v, -1, 3), bins=bins, color="#235e7c", alpha=0.8)
med = float(np.median(v))
ax.axvline(0, color="#555", lw=0.7)
ax.axvline(med, color="#b9484a", lw=1.2, ls="--")
ax.annotate(f"中位数 {med:+.0%}", (med, ax.get_ylim()[1] * 0.9), xytext=(4, 0), textcoords="offset points", fontsize=7.5, color="#b9484a")
ax.set_title(f"历史基率：一年涨 ≥3 倍、半年内跌去 45% 之后 12 个月的收益（n={len(v)}）", loc="left", fontweight="bold", fontsize=9.5)
ax.set_xlabel("此后 12 个月收益（右端截在 +300%）")
ax.grid(alpha=0.25)

fig.suptitle(f"NBIS：这次下跌有多大、跌在哪里、历史上类似情形之后怎样（as_of {AS_OF}）", x=0.01, ha="left", fontweight="bold", fontsize=11)
fig.text(0.01, 0.004, "数据：Yahoo 日线（复权）；基率样本为 studies/美股风气40年 的 238 只风气明星股（不含 NBIS），有幸存者偏差（退市且无数据的公司不在样本里）。",
         fontsize=7, color="#666")
fig.tight_layout(rect=(0, 0.02, 1, 0.95))
fig.savefig(HERE / "quant_drawdown.png")
print("\n图：", HERE / "quant_drawdown.png")
