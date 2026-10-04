#!/usr/bin/env python3
"""valuation_model.py — batch _pelosi_book_2026-09-28 的 M6 统一估值模型（可原地重跑）

一个公式跑 8 家，保证横向可比：
  • 10 年持有期，逐年 owner earnings（OE = FCF − SBC，或公司自身的"扣维护后"口径，见各家 valuation.md）
  • 每年把 p×OE 分给股东（股息 + 回购），其余再投资驱动增长；第 10 年按 exit 倍数（P/OE）退出
  • IRR 解：市值 = Σ p·OE_t/(1+r)^t + OE_10·exit/(1+r)^10
  • 同时给出本库 MSFT 口径（不计中期分配）：(OE_10·exit / 市值)^(1/10) − 1，便于与库内旧卡对照
  • 门槛价：把上式的 r 固定为 8% / 10% / 12%，反解每股价格

三种 OE 路径：
  oe   : OE_t = OE0·(1+g)^t
  ramp : OE_1 → OE_10 几何插值（适用于 OE≈0 的转型股，g 无意义）
  rev  : Rev_t = Rev1·(1+g)^(t−1)，OE 利润率从 m1 线性走到 m10（适用于 SBC 吃掉 FCF 的高增长软件）

用法: python companies/_pelosi_book_2026-09-28/valuation_model.py
输出: data/valuation_2026-09-28.json + data/valuation_2026-09-28.md
"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-09-28"
OUT = Path(__file__).resolve().parent / "data"
HURDLES = (0.08, 0.10, 0.12)

# price: 2026-09-25 收盘（Yahoo = Nasdaq）；shares: 百万股，口径见各家 facts.md；金额单位 $B
INPUTS = {
    "AVGO": {"price": 352.81, "shares_m": 4887.0, "shares_note": "Q3 FY26 摊薄加权",
             "scen": {"bear": {"mode": "oe", "oe0": 30.9, "g": 0.02, "exit": 14, "p": 0.6},
                      "base": {"mode": "oe", "oe0": 45.0, "g": 0.08, "exit": 18, "p": 0.6},
                      "bull": {"mode": "oe", "oe0": 52.0, "g": 0.13, "exit": 24, "p": 0.6}}},
    "BE": {"price": 288.70, "shares_m": 323.3, "shares_note": "Q2'26 摊薄加权（含可转债 if-converted）",
           "scen": {"bear": {"mode": "oe", "oe0": 0.45, "g": 0.15, "exit": 15, "p": 0.0},
                    "base": {"mode": "oe", "oe0": 0.67, "g": 0.25, "exit": 20, "p": 0.0},
                    "bull": {"mode": "oe", "oe0": 0.80, "g": 0.32, "exit": 25, "p": 0.0}}},
    "INTC": {"price": 123.00, "shares_m": 5285.0, "shares_note": "增发后（424B5：5,253.5M + 绿鞋 31.6M）",
             "scen": {"bear": {"mode": "ramp", "oe1": 1.0, "oe10": 10.0, "exit": 14, "p": 0.0},
                      "base": {"mode": "ramp", "oe1": 3.0, "oe10": 30.0, "exit": 18, "p": 0.0},
                      "bull": {"mode": "ramp", "oe1": 5.0, "oe10": 60.0, "exit": 22, "p": 0.0}}},
    "CRWD": {"price": 252.13, "shares_m": 1044.5, "shares_note": "Q2 FY27 摊薄加权",
             "scen": {"bear": {"mode": "rev", "rev1": 6.0, "g": 0.12, "m1": 0.06, "m10": 0.18, "exit": 18, "p": 0.0},
                      "base": {"mode": "rev", "rev1": 6.0, "g": 0.18, "m1": 0.06, "m10": 0.25, "exit": 25, "p": 0.0},
                      "bull": {"mode": "rev", "rev1": 6.0, "g": 0.23, "m1": 0.06, "m10": 0.30, "exit": 30, "p": 0.0}}},
    "VST": {"price": 138.46, "shares_m": 339.2, "shares_note": "Q2'26 摊薄加权",
            "scen": {"bear": {"mode": "oe", "oe0": 3.40, "g": 0.00, "exit": 9, "p": 0.8},
                     "base": {"mode": "oe", "oe0": 4.00, "g": 0.04, "exit": 12, "p": 0.7},
                     "bull": {"mode": "oe", "oe0": 4.50, "g": 0.07, "exit": 15, "p": 0.7}}},
    "AB": {"price": 35.76, "shares_m": 93.08, "shares_note": "AB Holding 单位数（10-Q 封面）；OE = 每单位分配",
           "scen": {"bear": {"mode": "oe", "oe0": 3.00 * 0.09308, "g": 0.00, "exit": 9, "p": 1.0},
                    "base": {"mode": "oe", "oe0": 3.40 * 0.09308, "g": 0.03, "exit": 11, "p": 1.0},
                    "bull": {"mode": "oe", "oe0": 3.55 * 0.09308, "g": 0.05, "exit": 13, "p": 1.0}}},
    "UBER": {"price": 69.62, "shares_m": 2050.2, "shares_note": "Q2'26 摊薄加权",
             "scen": {"bear": {"mode": "oe", "oe0": 5.7, "g": 0.03, "exit": 12, "p": 0.7},
                      "base": {"mode": "oe", "oe0": 7.4, "g": 0.10, "exit": 17, "p": 0.7},
                      "bull": {"mode": "oe", "oe0": 8.2, "g": 0.14, "exit": 20, "p": 0.7}}},
    "PANW": {"price": 374.74, "shares_m": 845.0, "shares_note": "FY27 指引摊薄股数中值",
             "scen": {"bear": {"mode": "rev", "rev1": 14.15, "g": 0.08, "m1": 0.22, "m10": 0.22, "exit": 18, "p": 0.0},
                      "base": {"mode": "rev", "rev1": 14.15, "g": 0.13, "m1": 0.22, "m10": 0.28, "exit": 23, "p": 0.0},
                      "bull": {"mode": "rev", "rev1": 14.15, "g": 0.17, "m1": 0.22, "m10": 0.32, "exit": 28, "p": 0.0}}},
}


def oe_path(s):
    if s["mode"] == "oe":
        return [s["oe0"] * (1 + s["g"]) ** t for t in range(1, 11)]
    if s["mode"] == "ramp":
        k = (s["oe10"] / s["oe1"]) ** (1 / 9)
        return [s["oe1"] * k ** (t - 1) for t in range(1, 11)]
    if s["mode"] == "rev":
        out = []
        for t in range(1, 11):
            rev = s["rev1"] * (1 + s["g"]) ** (t - 1)
            m = s["m1"] + (s["m10"] - s["m1"]) * (t - 1) / 9
            out.append(rev * m)
        return out
    raise ValueError(s["mode"])


def pv(path, s, r):
    cf = sum(s["p"] * oe / (1 + r) ** t for t, oe in enumerate(path, start=1))
    return cf + path[-1] * s["exit"] / (1 + r) ** 10


def irr(mcap, path, s):
    lo, hi = -0.9, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(path, s, mid) > mcap:
            lo = mid
        else:
            hi = mid
    return mid


def main():
    OUT.mkdir(exist_ok=True)
    res = {"as_of": AS_OF, "hurdles": HURDLES, "tickers": {}}
    md = [f"# 估值模型输出 {AS_OF}（valuation_model.py 生成，勿手改）", "",
          "IRR = 含中期分配的 10 年 IRR；库口径 = 不计中期分配（MSFT 公式）。门槛价 = base 情景下 IRR 恰为该门槛的每股价。", ""]
    for tk, x in INPUTS.items():
        mcap = x["price"] * x["shares_m"] / 1000  # $B
        r = {"price": x["price"], "shares_m": x["shares_m"], "mcap_b": round(mcap, 1), "scenarios": {}}
        md += [f"## {tk} · ${x['price']} · 市值 ${mcap:,.1f}B（{x['shares_note']}）", "",
               "| 情景 | 模式 | OE₁ | OE₁₀ | 退出 | 派发比例 | 第10年股权价值 | **IRR** | 库口径 IRR |",
               "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
        for name, s in x["scen"].items():
            path = oe_path(s)
            tv = path[-1] * s["exit"]
            i = irr(mcap, path, s)
            lib = (tv / mcap) ** 0.1 - 1 if tv > 0 else float("nan")
            r["scenarios"][name] = {**s, "oe_1": round(path[0], 3), "oe_10": round(path[-1], 3),
                                   "tv_10_b": round(tv, 1), "irr": round(i, 4), "irr_lib": round(lib, 4)}
            md.append(f"| {name} | {s['mode']} | {path[0]:.2f} | {path[-1]:.2f} | {s['exit']}x | {s['p']:.0%} | "
                      f"${tv:,.0f}B | **{i:+.1%}** | {lib:+.1%} |")
        base = x["scen"]["base"]
        bpath = oe_path(base)
        hp = {f"{int(h*100)}pct": round(pv(bpath, base, h) / x["shares_m"] * 1000, 2) for h in HURDLES}
        # bull 情景的 8% 门槛价（"最乐观也只能付到多少"）
        bull = x["scen"]["bull"]
        hp["8pct_on_bull"] = round(pv(oe_path(bull), bull, 0.08) / x["shares_m"] * 1000, 2)
        bear = x["scen"]["bear"]
        hp["8pct_on_bear"] = round(pv(oe_path(bear), bear, 0.08) / x["shares_m"] * 1000, 2)
        r["hurdle_prices"] = hp
        r["distance_to_8pct"] = round(hp["8pct"] / x["price"] - 1, 4)
        res["tickers"][tk] = r
        md += ["", f"门槛价（base）：8% **${hp['8pct']:,.2f}**（距现价 {hp['8pct']/x['price']-1:+.1%}）· "
                   f"10% ${hp['10pct']:,.2f} · 12% ${hp['12pct']:,.2f} · bull 情景 8% 门槛价 ${hp['8pct_on_bull']:,.2f} · bear 情景 8% 门槛价 ${hp['8pct_on_bear']:,.2f}", ""]
    # ---- AB 用户专属变体：第 3 年（2028）起分配按 37% 预扣（AB qualified notice：对外国投资者 100% ECI）
    x = INPUTS["AB"]; base = x["scen"]["base"]; path = oe_path(base); mcap = x["price"] * x["shares_m"] / 1000
    def pv_nra(r):
        cf = sum(oe * (0.63 if t >= 3 else 1.0) / (1 + r) ** t for t, oe in enumerate(path, start=1))
        return cf + path[-1] * base["exit"] / (1 + r) ** 10
    lo, hi = -0.9, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if pv_nra(mid) > mcap else (lo, mid)
    res["tickers"]["AB"]["base_irr_if_nra_from_2028"] = round(mid, 4)
    md += ["## AB 用户专属变体", "",
           f"base 情景，若 2028 年起按非居民身份持有（分配预扣 37%，不计出售时 §1446(f) 10% 预扣与申报成本）：IRR **{mid:+.1%}**（税前 base 为 {res['tickers']['AB']['scenarios']['base']['irr']:+.1%}）", ""]
    (OUT / f"valuation_{AS_OF}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"valuation_{AS_OF}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
