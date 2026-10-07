#!/usr/bin/env python3
"""build_report.py — report_source.md + 计算结果 → report.md。

正文用 report_source.md 编辑；表格由数据生成，占位符形如 {{TABLE:name}} 或 {{TABLE:theme:<theme_id>}}。
不要直接改 report.md（会被覆盖）。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
D = BASE / "data"
FATE_CN = {"dead": "死亡", "acquired": "被收购", "survived_below_peak": "活着·未回高点",
           "survived_new_high": "活着·曾收复高点", "in_progress": "进行中", None: "?"}


FATE_SHORT = {"dead": "死", "acquired": "购", "survived_below_peak": "未回", "survived_new_high": "曾回", "in_progress": "进行"}


def pct(x, nd=0):
    if x is None:
        return ""
    if nd == 0 and -1 < x <= -0.99:  # -99.6% 不要四舍五入成 -100%（那会被读成归零）
        nd = 2 if x < -0.999 else 1
    return f"{x * 100:+.{nd}f}%".replace("+-", "-")


def yrs(m):
    return "" if m in (None, "") else f"{float(m) / 12:.1f} 年"


def ym(s):
    return f"{s[:4]}-{s[4:]}" if s and len(s) == 6 and s.isdigit() else (s or "")


def md_table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * len(head)) + "|"]
    out += ["| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |" for r in rows]
    return "\n".join(out)


def trim(s, lo=25, hi=72):
    """说明文字：在 lo 之后第一个句读处截断，最长 hi 个字符。"""
    s = (s or "").strip()
    if len(s) <= hi:
        return s
    cut = min([i for i in (s.find(ch, lo) for ch in "；。") if 0 < i <= hi] or [hi])
    return s[:cut] + ("。" if cut < hi else "…")


def link(srcs, label="来源"):
    srcs = [s for s in (srcs or []) if isinstance(s, str) and s.startswith("http")]
    return " ".join(f"[{label}{i + 1 if len(srcs) > 1 else ''}]({s})" for i, s in enumerate(srcs[:2]))


def t_market():
    m = json.loads((D / "market_drawdowns.json").read_text(encoding="utf-8"))
    rows = []
    for tk, nm in (("^IXIC", "纳指综合"), ("^GSPC", "标普500")):
        for e in m[tk]["drawdowns_ge20"]:
            rows.append([nm, e["peak"], f'{e["peak_close"]:,.0f}', e["trough"], pct(e["drawdown"]),
                         f'{e["years_peak_to_trough"]:.1f} 年', e["recovered"] or "未收复",
                         f'{e["years_peak_to_recover"]:.1f} 年' if e["years_peak_to_recover"] else ""])
    return md_table(["指数", "顶点", "收盘", "谷底", "回撤", "下跌用时", "收复日", "顶点→收复"], rows)


def t_hot_annual():
    d = json.loads((D / "industry_fads.json").read_text(encoding="utf-8"))
    from analyze_industry_market import CN
    rows = []
    for r in d["annual"]:
        rows.append([r["year"], CN[r["hot5"]], f'{r["hot5_rel"]:.2f}x',
                     (f'{r["hot5_fwd_rel"]:.2f}x' + ("" if r["fwd_months"] == 60 else f'（{r["fwd_months"]}月）')) if "hot5_fwd_rel" in r else "—",
                     f'{r["hot5_fwd_rank"]}/49' if r.get("hot5_fwd_rank") else "", pct(r.get("hot5_fwd_maxdd")),
                     CN[r["cold5"]], f'{r["cold5_fwd_rel"]:.2f}x' if "cold5_fwd_rel" in r else "—"])
    return md_table(["年末", "过去5年最热行业", "过去5年相对市场", "之后5年相对市场", "之后排名", "之后5年内最大回撤",
                     "过去5年最冷行业", "最冷之后5年相对"], rows)


def t_booms():
    d = json.loads((D / "industry_fads.json").read_text(encoding="utf-8"))
    rows = []
    for e in d["bubble_events"]:
        rec = (yrs(e["months_to_recover"]) if e["recovered"] else
               ("顶点太近" if e["months_after_peak_available"] < 24 else f'未收复（已 {e["months_since_peak_unrecovered"] / 12:.0f} 年）'))
        rows.append([e["industry_cn"], ym(e["first_signal"]), ym(e["peak"]), f'{e["abs36_max"]:.1f}x / {e["rel36_max"]:.1f}x',
                     pct(e["maxdd"]), yrs(e["months_peak_to_trough"]), rec,
                     f'{e["rel_5y_after_signal"]:.2f}x' if e.get("rel_5y_after_signal") is not None else "未满5年"])
    return md_table(["行业", "首个信号", "顶点", "36月涨幅/相对市场", "顶点后回撤", "下跌用时", "收复用时", "信号月买入→5年相对市场"], rows)


def load_T():
    p = D / "themes_computed.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def t_themes(T):
    rows = []
    for t in sorted(T["themes"], key=lambda t: ((t.get("hype_start") or {}).get("date") or "9999")):
        ttr = t.get("time_to_reality") or {}
        fc = t["fate_counts"]
        rows.append([t["name_cn"], (t.get("hype_start") or {}).get("date", ""), (t.get("peak") or {}).get("date", ""),
                     (t.get("trough") or {}).get("date", "") or "", yrs(t.get("months_rise")), yrs(t.get("months_bust")),
                     t.get("reality_verdict") or "", f'{ttr.get("years")} 年' if ttr.get("years") not in (None, "") else "",
                     " ".join(f"{FATE_SHORT[k]}{fc[k]}" for k in FATE_SHORT if fc.get(k))])
    return md_table(["主题", "兴起", "顶点", "谷底", "兴起→顶点", "顶点→谷底", "主题后来是否兑现", "兑现用时", "明星股结局"], rows)


def t_theme_companies(T, tid):
    rows = []
    for c in [c for c in T["companies"] if c["theme"] == tid]:
        p = c.get("price") or {}
        if "rejected" in p:
            p = {}
        if p:
            dd = pct(p.get("maxdd"))
            rec = (f'{p["recovered_date"][:7]}（{yrs(p["months_to_recover"])}）' if p.get("recovered_date") else
                   f'现为峰值 {p["now_vs_peak"] * 100:.0f}%' if c["fate_computed"] == "in_progress" else
                   f'未收复，现为峰值 {p["now_vs_peak"] * 100:.0f}%')
            pk = p["peak_date"][:7]
        else:
            dd = pct(c.get("loss_vs_peak_research")) if c.get("loss_vs_peak_research") is not None else ""
            rec = ""
            pk = c.get("peak_date") or ""
        fate = FATE_CN.get(c["fate_computed"], c["fate_computed"])
        if c["fate_computed"] in ("dead", "acquired") and c.get("fate_date"):
            fate += f'（{c["fate_date"]}，峰后 {yrs(c.get("months_peak_to_fate"))}）' if c.get("months_peak_to_fate") else f'（{c["fate_date"]}）'
        if not c.get("listed", True):
            fate = "非上市主体（不计入统计）：" + fate
        rows.append([c["name"] + (f'（{c["yahoo_ticker"]}）' if c.get("yahoo_ticker") and p else ""), c.get("role_cn") or "",
                     pk, dd, rec, fate, trim(c.get("fate_detail_cn")) + (f'［口径：{c["loss_note"]}］' if c.get("loss_note") else ""),
                     link(c.get("sources"))])
    return md_table(["公司", "角色", "峰值", "最大回撤/损失", "收复", "结局", "说明", "来源"], rows)


ERA_CN = {"e1": "1985–1994", "e2": "1995–2002", "e3": "2003–2011", "e4": "2012–2019", "e5a": "2020–2022（上）",
          "e5b": "2020–2022（下）", "e6": "2023–2026（进行中）"}


def t_agg(T):
    rows = []
    listed = [c for c in T["companies"] if c.get("listed", True)]
    eras = sorted({c["era_id"] for c in listed})
    for e in eras + ["合计"]:
        cs = listed if e == "合计" else [c for c in listed if c["era_id"] == e]
        n = len(cs)
        cnt = {f: sum(c["fate_computed"] == f for c in cs) for f in FATE_CN if f}
        rows.append([ERA_CN.get(e.split("_")[0], e), n] + [f'{cnt[f]}（{cnt[f] / n * 100:.0f}%）' if n else "" for f in
                                                            ("dead", "acquired", "survived_below_peak", "survived_new_high", "in_progress")])
    return md_table(["时代", "明星股（主题×公司）", "死亡", "被收购", "活着·未回高点", "活着·曾收复高点", "进行中"], rows)


def t_verdict(T):
    rows = []
    for v, b in T["aggregate"]["by_verdict"].items():
        n = b["companies"]
        closed = n - b.get("in_progress", 0)
        rows.append([v, b["themes"], n, f'{b.get("dead", 0)}', f'{b.get("acquired", 0)}', f'{b.get("survived_below_peak", 0)}',
                     f'{b.get("survived_new_high", 0)}',
                     f'{b.get("survived_new_high", 0) / closed * 100:.0f}%' if closed else "—"])
    return md_table(["主题后来是否兑现", "主题数", "明星股", "死亡", "被收购", "未回高点", "曾收复高点", "曾收复占比（已结束）"], rows)


def t_dd(T):
    rows = []
    for b in T["aggregate"]["dd_buckets"]:
        rows.append([b["bucket"], b["n"], f'{b["recovered"]}（{b["recovered"] / b["n"] * 100:.0f}%）' if b["n"] else "",
                     f'{b["median_years_to_recover"]:.1f} 年' if b["median_years_to_recover"] else "—",
                     f'{b["median_now_vs_peak"] * 100:.0f}%' if b["median_now_vs_peak"] is not None else ""])
    return md_table(["顶点后最大回撤", "活下来的公司数", "曾收复当年高点", "收复者中位用时", "现价/当年峰值（中位）"], rows)


def t_ttr(T):
    rows = []
    for t in sorted(T["themes"], key=lambda t: ((t.get("hype_start") or {}).get("date") or "9999")):
        r = t.get("time_to_reality") or {}
        y = r.get("years")
        marker = (r.get("marker_cn") or "").split("；")[0].split("。")[0]
        rows.append([t["name_cn"].split("（")[0], (t.get("hype_start") or {}).get("date", "")[:7], t.get("reality_verdict") or "",
                     f"{y} 年" if y not in (None, "") else "未兑现/未定", marker[:70], link([r.get("source")])])
    return md_table(["风气", "兴起", "主题后来是否兑现", "兑现用时", "以什么为兑现标志", "来源"], rows)


def ttr_median(T):
    ys = [float(t["time_to_reality"]["years"]) for t in T["themes"]
          if (t.get("time_to_reality") or {}).get("years") not in (None, "") and t.get("reality_verdict") != "进行中"]
    import statistics
    return statistics.median(ys), len(ys)


def t_long_unrec(T, years=15):
    seen, rows = set(), []
    cs = [c for c in T["companies"] if c.get("listed", True) and c["fate_computed"] == "survived_below_peak"
          and (c.get("price") or {}).get("years_since_peak", 0) >= years and not c["price"].get("conflict")
          and "rejected" not in c["price"]]
    for c in sorted(cs, key=lambda c: -c["price"]["years_since_peak"]):
        k = (c.get("yahoo_ticker"), c["price"]["peak_date"][:7])
        if k in seen:
            continue
        seen.add(k)
        p = c["price"]
        th = next(t["name_cn"] for t in T["themes"] if t["id"] == c["theme"])
        rows.append([c["name"], th.split("（")[0], p["peak_date"][:7], pct(p["maxdd"]), f'{p["years_since_peak"]:.0f} 年',
                     f'{p["now_vs_peak"] * 100:.0f}%'])
    return md_table(["公司", "当年的风气", "峰值", "最大回撤", "至今已过", "现价/当年峰值"], rows)


def main():
    import sys
    sys.path.insert(0, str(BASE / "scripts"))
    src = (BASE / "report_source.md").read_text(encoding="utf-8")
    T = load_T()
    gens = {"market": t_market, "hot_annual": t_hot_annual, "booms": t_booms}
    if T:
        gens.update({"themes": lambda: t_themes(T), "agg": lambda: t_agg(T), "verdict": lambda: t_verdict(T),
                     "dd_buckets": lambda: t_dd(T), "long_unrec": lambda: t_long_unrec(T), "ttr": lambda: t_ttr(T)})
        m, n = ttr_median(T)
        src = src.replace("{{TTR_MEDIAN}}", f"{m:.0f}").replace("{{TTR_N}}", str(n))

    def sub(m):
        key = m.group(1)
        if key.startswith("theme:"):
            return t_theme_companies(T, key.split(":", 1)[1]) if T else m.group(0)
        return gens[key]() if key in gens else m.group(0)
    out = re.sub(r"\{\{TABLE:([^}]+)\}\}", sub, src)
    if T:  # 正文里的汇总数字也由数据生成，避免手抄过时：{{AGG:k}} 原值，{{PCT:k}} 占已结束样本比例，{{YRS:k}} 月→年
        a = T["aggregate"]
        out = re.sub(r"\{\{AGG:(\w+)\}\}", lambda m: (f'{a[m.group(1)]:.0f}' if isinstance(a[m.group(1)], (int, float)) else str(a[m.group(1)])), out)
        out = re.sub(r"\{\{PCT:(\w+)\}\}", lambda m: f'{a[m.group(1)] / a["n_closed"] * 100:.0f}%', out)
        out = re.sub(r"\{\{YRS:(\w+)\}\}", lambda m: f'{a[m.group(1)] / 12:.1f}', out)
        out = re.sub(r"\{\{DDB:(\d)\.(\w+)\}\}", lambda m: (lambda b: (f'{b["recovered"] / b["n"] * 100:.0f}%' if m.group(2) == "rate"
                     else f'{b[m.group(2)]:.1f}' if isinstance(b[m.group(2)], float) else str(b[m.group(2)])))(a["dd_buckets"][int(m.group(1))]), out)
    left = re.findall(r"\{\{(?:TABLE|AGG|PCT|YRS|DDB):[^}]+\}\}", out)
    (BASE / "report.md").write_text(out, encoding="utf-8")
    print("report.md written", len(out), "chars; unresolved:", left)


if __name__ == "__main__":
    main()
