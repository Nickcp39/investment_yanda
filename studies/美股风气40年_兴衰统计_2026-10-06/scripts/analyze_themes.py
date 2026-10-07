#!/usr/bin/env python3
"""analyze_themes.py — 主题层与公司层：当年明星股的兴衰、存活与用时。

输入：data/research/e*.json（各时代研究员按 BRIEF.md 的口径整理、带来源）；data/raw/prices（Yahoo 周线/日线）。
规则：
- 有 Yahoo 价格的公司，峰值/回撤/收复/现价一律按日线收盘重算：“回到高点”用拆股复权价（close，不含股息），
  “持有至今倍数”用含股息复权价（adjclose）。
  峰值搜索窗口：研究员给的公司峰值月 ±9 个月；没有则用主题 [兴起-6 个月, 主题谷底或顶点+24 个月]。
- 代码复用陷阱校验：研究员给出名义峰值价时，用 Yahoo close×之后的拆股倍数还原名义价，偏差 >40% 记为 price_check=mismatch，
  该公司不使用 Yahoo 数据（防止同代码不同公司）。研究员判 dead/acquired 但 Yahoo 仍有至今价格的，也标记冲突。
- 无价格的公司（破产、被收购、退市）用研究员给的峰值、结局日期与每股最终价值，标注 source=research。
输出：data/themes_computed.json、data/companies_table.csv。
"""
from __future__ import annotations

import csv
import datetime as dt
import gzip
import io
import json
import re
import statistics
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PX = BASE / "data/raw/prices"
AS_OF = dt.date(2026, 10, 5)
MANIFEST = json.loads((PX / "manifest.json").read_text(encoding="utf-8"))
# 研究员给出的“收购价/峰值价”中间隔了拆股或反向拆股、需换算到同一口径的（2026-10-06 人工核对）。
# 值为 None：可能存在未核实的反向拆股，宁可不给数字。
LOSS_OVERRIDE = {
    "Chiron": ((48.0 * 4) / 95.125 - 1, "1996-08 1 拆 4：$48 现金 ≈ 拆股前 $192，约为 1994 年高点的 2 倍"),
    "Ariba": (7.50 / 168.75 - 1, "2004 年 1:6 反向拆股：$45 折合峰值口径 $7.50"),
    "VerticalNet": ((2.56 / 560) / 138.88 - 1, "三次反向拆股累计 560:1：$2.56 折合峰值口径约 $0.005"),
    "CMGI": (None, "2008 年前后可能有反向拆股，峰值与收购价口径未核实"),
    "Internet Capital Group": (None, "可能有反向拆股，清算分配与峰值口径未核实"),
    "Gensia": (None, "1997 年合并与后续股本变动，收购价与 1992 年峰值口径未核实"),
}
USE_ADJ = {"KR": "1988 年 LBO 防御：每股 $40 特别现金分配，未复权价格在 1988-10→12 出现约 -86% 的假跌"}
# 人工核对过的“误报”：研究员的峰值价用的是更早的拆股口径，换算后与 Yahoo 一致（2026-10-06）
MANUAL_OK = {
    "AMZN": "研究员 $113 为 2000 年拆股口径；÷2022 年 20:1 拆股 = $5.65，Yahoo 日收盘 $5.33",
    "EBAY": "研究员 $127.5 只调整了 1999/2000 年拆股；再 ÷(2×2×2.376)=9.5 → $13.4，Yahoo $12.82",
    "VIAV": "研究员注明 Yahoo VIAV 拆股+分拆口径为 $698（盘中），Yahoo 日收盘 $666.8",
}


def pdate(s, default_day=1):
    """'2000' / '2000-03' / '2000-03-10' → date；年份只给到年时取年中。"""
    if not s or not isinstance(s, str):
        return None
    m = re.search(r"\d{4}(-\d{2}(-\d{2})?)?", s)  # 研究员偶尔写区间“2024-12 ~ 2025-11”：取第一个日期
    if not m:
        return None
    s = m.group(0)
    try:
        if len(s) == 4:
            return dt.date(int(s), 7, 1)
        if len(s) == 7:
            return dt.date(int(s[:4]), int(s[5:7]), default_day)
        return dt.date.fromisoformat(s)
    except ValueError:
        return None


def months_between(a, b):
    return None if a is None or b is None else round((b - a).days / 30.4375, 1)


def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    return dt.date(d.year + y, mo + 1, min(d.day, 28))


def load_px(tk):
    meta = MANIFEST.get(tk)
    if not meta or meta.get("status") != "ok":
        return None
    fn = PX / (tk.replace("^", "IDX_").replace("/", "_").replace("=", "_") + ".csv.gz")
    if not fn.exists():
        return None
    rows = list(csv.DictReader(io.StringIO(gzip.decompress(fn.read_bytes()).decode())))
    return [(dt.date.fromisoformat(r["date"]), float(r["close"]), float(r["adjclose"])) for r in rows if float(r["adjclose"]) > 0]


def split_factor_after(tk, d):
    f = 1.0
    for sd, ratio in MANIFEST.get(tk, {}).get("splits", []):
        if dt.date.fromisoformat(sd) > d:
            n, m = ratio.split(":")
            f *= float(n) / float(m)
    return f


def price_stats(px, lo, hi, hype=None, theme_peak=None):
    """峰值/回撤/收复按拆股复权的价格（close，不含股息，= 大众说的“回到当年高点”）；
    倍数类（从风气起点或主题顶点持有至今）按含股息复权 adjclose。"""
    win = [x for x in px if lo <= x[0] <= hi]
    if not win:
        return None
    pk = max(win, key=lambda x: x[1])
    after = [x for x in px if x[0] > pk[0]]
    trough, rec = pk, None
    for x in after:
        if x[1] > pk[1]:  # 严格高于峰值才算收复（相邻两日收盘相同不算）
            rec = x
            break
        if x[1] < trough[1]:
            trough = x
    rec_tr = next((x for x in after if x[2] > pk[2]), None)
    last = px[-1]

    def at(d):  # d 当周或之后第一个价格
        return next((x for x in px if x[0] >= d), None) if d else None
    h, tp = at(hype), at(theme_peak)
    return {
        "peak_date": pk[0].isoformat(), "peak_close_splitadj": pk[1], "peak_adj": pk[2],
        "trough_date": trough[0].isoformat(), "maxdd": trough[1] / pk[1] - 1,
        "months_peak_to_trough": months_between(pk[0], trough[0]),
        "recovered_date": rec[0].isoformat() if rec else None,
        "months_to_recover": months_between(pk[0], rec[0]) if rec else None,
        "recovered_tr_date": rec_tr[0].isoformat() if rec_tr else None,
        "last_date": last[0].isoformat(), "now_vs_peak": last[1] / pk[1], "now_vs_peak_tr": last[2] / pk[2],
        "years_since_peak": round((last[0] - pk[0]).days / 365.25, 1),
        "data_first": px[0][0].isoformat(),
        "tr_mult_from_hype_start": (last[2] / h[2]) if h else None,
        "hype_start_price_date": h[0].isoformat() if h else None,
        "listed_after_hype_start": bool(hype and px[0][0] > add_months(hype, 3)),
        "tr_mult_from_theme_peak": (last[2] / tp[2]) if tp else None,
    }


UNLISTED = ("FTX", "Celsius", "Cruise", "Argo AI", "Uber ATG", "Waymo")  # 非上市主体：保留在表中，不计入股票结局统计


def analyze_company(c, th, era_in_progress):
    out = {k: c.get(k) for k in ("name", "ticker_then", "yahoo_ticker", "role_cn", "fate", "fate_date",
                                 "fate_detail_cn", "confidence", "peak_price", "price_basis", "peak_date",
                                 "final_value_per_share", "peak_mcap_usd_bn")}
    out["sources"] = c.get("sources") or []
    out["listed"] = not any(c["name"].startswith(u) for u in UNLISTED)
    out["theme"] = th["id"]
    out["research_fate"] = c.get("fate")
    tk = c.get("yahoo_ticker")
    px = load_px(tk) if tk else None
    if px and tk in USE_ADJ:  # 巨额特别股息会让“只复权拆股”的价格出现假暴跌，改用含股息复权价
        px = [(d, a, a) for d, _, a in px]
    st = None
    if px:
        cpk = pdate(c.get("peak_date"))
        hs, tp, tt = pdate(th.get("hype_start", {}).get("date")), pdate(th.get("peak", {}).get("date")), pdate(th.get("trough", {}).get("date"))
        if cpk:
            lo, hi = add_months(cpk, -9), add_months(cpk, 9)
        else:
            lo = add_months(hs or tp or px[0][0], -6)
            hi = tt or (add_months(tp, 24) if tp else AS_OF)
            if hi <= lo:  # 研究员把谷底写在顶点之前（如 AI 算力 2025-01 DeepSeek 回调）
                hi = add_months(tp, 24) if tp and add_months(tp, 24) > lo else AS_OF
        if era_in_progress:  # 进行中的主题：峰值 = 风气兴起以来至今的最高点
            lo, hi = add_months(hs, -1) if hs else px[0][0], AS_OF
        st = price_stats(px, lo, hi, hs, tp)
        if st:
            # 名义价校验
            chk = "n/a"
            try:
                rp = float(c.get("peak_price")) if c.get("peak_price") not in (None, "") else None
            except (TypeError, ValueError):
                rp = None
            if rp and (c.get("price_basis") or "").startswith("nominal"):
                nominal = st["peak_close_splitadj"] * split_factor_after(tk, dt.date.fromisoformat(st["peak_date"]))
                chk = "ok" if 0.6 <= nominal / rp <= 1.67 else "mismatch"
                st["nominal_peak_from_yahoo"] = round(nominal, 3)
            elif rp and (c.get("price_basis") or "").startswith("split"):
                chk = "ok" if 0.6 <= st["peak_close_splitadj"] / rp <= 1.67 else "mismatch"
            if chk == "mismatch" and tk in MANUAL_OK:
                chk = "ok（人工核对：" + MANUAL_OK[tk] + "）"
            st["price_check"] = chk
            stale = (AS_OF - dt.date.fromisoformat(st["last_date"])).days > 20
            if chk == "mismatch":
                out["warning"] = f"Yahoo {tk} 名义峰值与研究员峰值价不符，疑似代码复用/口径不同 → 不用价格数据"
                st = {"rejected": st}
            elif c.get("fate") in ("dead", "acquired") and not stale:
                out["warning"] = f"研究员判 {c.get('fate')}，但 Yahoo {tk} 至今仍有报价（可能是重组后新公司或代码复用）→ 结局按研究员，价格仅作参考"
                st["conflict"] = True
    out["price"] = st
    ok = st and "rejected" not in st and not st.get("conflict")
    # 计算后的结局
    if ok and not ((AS_OF - dt.date.fromisoformat(st["last_date"])).days > 20):
        if c.get("fate") == "in_progress" or (era_in_progress and not c.get("fate")):
            fate = "in_progress"
        else:
            fate = "survived_new_high" if st["recovered_date"] else "survived_below_peak"
        out["fate_computed"] = fate
        out["fate_source"] = "price"
    else:
        out["fate_computed"] = c.get("fate")
        out["fate_source"] = "research"
        if ok and st:  # 价格序列中途结束（退市）
            out["fate_source"] = "research+price_until_delist"
    # 用时：峰值 → 结局（死亡/被收购）
    pk = pdate(st["peak_date"]) if ok else pdate(c.get("peak_date"))
    fd = pdate(c.get("fate_date"))
    out["months_peak_to_fate"] = months_between(pk, fd) if out["fate_computed"] in ("dead", "acquired") else None
    try:
        fv, rp = c.get("final_value_per_share"), c.get("peak_price")
        out["loss_vs_peak_research"] = (float(fv) / float(rp) - 1) if fv is not None and rp not in (None, 0, "") else None
    except (TypeError, ValueError, ZeroDivisionError):
        out["loss_vs_peak_research"] = None
    for k, (v, why) in LOSS_OVERRIDE.items():
        if c["name"].startswith(k):
            out["loss_vs_peak_research"] = v
            out["loss_note"] = why
    return out


def proxy_stats(th):
    res = []
    tp, tt = pdate(th.get("peak", {}).get("date")), pdate(th.get("trough", {}).get("date"))
    for tk in th.get("proxy_tickers") or []:
        px = load_px(tk)
        if not px or not tp or px[0][0] > add_months(tp, -3):
            res.append({"ticker": tk, "usable": False, "reason": "无数据或晚于主题顶点才发行"})
            continue
        st = price_stats(px, add_months(tp, -6), add_months(tp, 6))
        res.append({"ticker": tk, "usable": True, **(st or {})})
    return res


def main():
    eras, themes, comps = [], [], []
    for p in sorted((BASE / "data/research").glob("e*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        eras.append({k: d.get(k) for k in ("era_id", "era_range", "macro_context_cn", "macro_sources")})
        in_prog = d.get("era_id", "").startswith("e6")
        for th in d.get("themes", []):
            hs, tp, tt = (pdate(th.get(k, {}).get("date")) for k in ("hype_start", "peak", "trough"))
            cs = [analyze_company(c, th, in_prog) for c in th.get("companies", [])]
            for c in cs:
                c["era_id"] = d.get("era_id")
            comps += cs
            fates = {}
            for c in cs:
                if c["listed"]:
                    fates[c["fate_computed"]] = fates.get(c["fate_computed"], 0) + 1
            themes.append({
                "era_id": d.get("era_id"), "id": th.get("id"), "name_cn": th.get("name_cn"), "name_en": th.get("name_en"),
                "one_line_cn": th.get("one_line_cn"), "hype_start": th.get("hype_start"), "peak": th.get("peak"),
                "trough": th.get("trough"), "months_rise": months_between(hs, tp),
                "months_bust": months_between(tp, tt) if (tp and tt and tt > tp) else None,  # 谷底写在顶点之前（进行中主题）不计
                "what_killed_it_cn": th.get("what_killed_it_cn"), "reality_verdict": th.get("reality_verdict"),
                "reality_evidence": th.get("reality_evidence"), "time_to_reality": th.get("time_to_reality"),
                "basket_method": th.get("basket_method"), "proxies": proxy_stats(th), "fate_counts": fates,
                "n_companies": len(cs),
            })
    # 汇总
    listed = [c for c in comps if c["listed"]]
    done = [c for c in listed if c["fate_computed"] != "in_progress"]
    agg = {"n_themes": len(themes), "n_entries_all": len(comps), "n_companies": len(listed),
           "n_unlisted_excluded": len(comps) - len(listed),
           "n_distinct_companies": len({(c.get("yahoo_ticker") or c["name"]) for c in listed}), "n_closed": len(done)}
    for f in ("dead", "acquired", "survived_below_peak", "survived_new_high", "in_progress"):
        agg[f] = sum(c["fate_computed"] == f for c in listed)
    pr = [c for c in done if c.get("price") and "now_vs_peak" in (c["price"] or {}) and not (c["price"] or {}).get("conflict")
          and c["fate_computed"] in ("survived_new_high", "survived_below_peak")]
    agg["n_survivors_priced"] = len(pr)
    seen, uq = set(), []
    for c in sorted(pr, key=lambda c: c["price"]["peak_date"]):
        k = (c.get("yahoo_ticker"), c["price"]["peak_date"][:7])
        if k not in seen and not c["era_id"].startswith("e6"):
            seen.add(k)
            uq.append(c)
    buckets = []
    for lo, hi, lab in ((-0.5, 0.01, "跌不到 50%"), (-0.8, -0.5, "跌 50–80%"), (-0.9, -0.8, "跌 80–90%"),
                        (-0.95, -0.9, "跌 90–95%"), (-1.01, -0.95, "跌 95% 以上")):
        g = [c for c in uq if lo < c["price"]["maxdd"] <= hi]
        r = [c["price"]["months_to_recover"] / 12 for c in g if c["price"].get("months_to_recover")]
        buckets.append({"bucket": lab, "n": len(g), "recovered": len(r),
                        "median_years_to_recover": statistics.median(r) if r else None,
                        "median_now_vs_peak": statistics.median(c["price"]["now_vs_peak"] for c in g) if g else None})
    agg["dd_buckets"] = buckets
    agg["n_dd_bucket_companies"] = len(uq)
    agg["n_survivors_now_above_peak"] = sum(c["price"]["now_vs_peak"] >= 1 for c in pr)
    old = [c for c in done if not c["era_id"].startswith("e6")]  # 用时类统计只用已结束时代，与图 6 一致
    dd = [c["price"]["maxdd"] for c in old if c.get("price") and "maxdd" in (c["price"] or {}) and not c["price"].get("conflict")
          and "rejected" not in c["price"]]
    rec = [c["price"]["months_to_recover"] for c in old if c.get("price") and (c["price"] or {}).get("months_to_recover")]
    death = [c["months_peak_to_fate"] for c in old if c["fate_computed"] == "dead" and c["months_peak_to_fate"] is not None]
    acq = [c["months_peak_to_fate"] for c in old if c["fate_computed"] == "acquired" and c["months_peak_to_fate"] is not None]
    med = lambda xs: statistics.median(xs) if xs else None  # noqa: E731
    agg.update({"median_maxdd_priced": med(dd), "n_priced": len(dd), "median_months_to_recover": med(rec), "n_recovered": len(rec),
                "median_months_peak_to_death": med(death), "n_death_dated": len(death),
                "median_months_peak_to_acquired": med(acq), "n_acq_dated": len(acq),
                # 用时中位数只用已结束时代（2023 年后的主题尚在进行，不计）
                "median_months_rise": med([t["months_rise"] for t in themes if t["months_rise"] is not None and not t["era_id"].startswith("e6")]),
                "median_months_bust": med([t["months_bust"] for t in themes if t["months_bust"] is not None and not t["era_id"].startswith("e6")])})
    by_verdict = {}
    for t in themes:
        v = t["reality_verdict"] or "?"
        b = by_verdict.setdefault(v, {"themes": 0, "companies": 0})
        b["themes"] += 1
        for f, n in t["fate_counts"].items():
            b[f] = b.get(f, 0) + n
            b["companies"] += n
    agg["by_verdict"] = by_verdict
    out = {"as_of": AS_OF.isoformat(), "eras": eras, "themes": themes, "companies": comps, "aggregate": agg,
           "warnings": [{"name": c["name"], "theme": c["theme"], "warning": c["warning"]} for c in comps if c.get("warning")]}
    (BASE / "data/themes_computed.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    with (BASE / "data/companies_table.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["era", "theme", "name", "yahoo", "role", "fate_research", "fate_computed", "fate_source", "peak_date",
                    "maxdd", "months_peak_to_trough", "recovered", "months_to_recover", "now_vs_peak", "fate_date",
                    "months_peak_to_fate", "price_check", "warning", "sources"])
        for c in comps:
            p = c.get("price") or {}
            p = {} if "rejected" in p else p
            w.writerow([c["era_id"], c["theme"], c["name"], c.get("yahoo_ticker"), c.get("role_cn"), c["research_fate"],
                        c["fate_computed"], c["fate_source"], p.get("peak_date") or c.get("peak_date"),
                        round(p["maxdd"], 3) if "maxdd" in p else "", p.get("months_peak_to_trough", ""),
                        p.get("recovered_date", ""), p.get("months_to_recover", ""),
                        round(p["now_vs_peak"], 3) if "now_vs_peak" in p else "", c.get("fate_date"),
                        c.get("months_peak_to_fate"), p.get("price_check", ""), c.get("warning", ""), " ".join(c["sources"])])
    print(json.dumps(agg, ensure_ascii=False, indent=1))
    for wn in out["warnings"]:
        print("WARN", wn)


if __name__ == "__main__":
    main()
