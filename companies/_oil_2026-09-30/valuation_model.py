#!/usr/bin/env python3
"""valuation_model.py — batch _oil_2026-09-30 的 M6 统一估值模型（由 _pelosi_book_2026-09-28/valuation_model.py 复制；公式不变，只换输入 + 增加『隐含油价』）

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

用法: python companies/_oil_2026-09-30/valuation_model.py
输出: data/valuation_2026-09-28.json + data/valuation_2026-09-28.md
"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-09-30"
OUT = Path(__file__).resolve().parent / "data"
HURDLES = (0.08, 0.10, 0.12)

# price: 2026-09-25 收盘（Yahoo = Nasdaq）；shares: 百万股，口径见各家 facts.md；金额单位 $B
# price: 2026-09-29 收盘（Yahoo = Nasdaq）；shares: 百万股（10-Q/10-K 封面）；金额 $B
# OE₀ = 在"周期中间价"下的所有者收益（FCF − SBC，OXY 另扣优先股股息），推导见各家 valuation.md：
#   油价假设（名义、10 年持平）：bear WTI $55 / Brent $60 · base WTI $65 / Brent $70（≈2016–2025 均值）· bull WTI $80 / Brent $85
# g：base = 管理层 2029–30 自由现金流目标的 50% 信用折算成 10 年恒定增速；bull = 100% 信用；bear = 0（仅 1–1.5%）
# sens: 每 $1/bbl 油价变动对年度税后 OE 的影响（$B）及其挂钩的基准；base_px = base 情景对应的基准价
INPUTS = {
    "XOM": {"price": 161.35, "shares_m": 4111.9, "shares_note": "10-Q 封面 2026-06-30（ExxonMobil Holdings Corp）",
            "sens": 0.70, "bench": "Brent", "base_px": 70,
            "scen": {"bear": {"mode": "oe", "oe0": 15.5, "g": 0.010, "exit": 10, "p": 0.95},
                     "base": {"mode": "oe", "oe0": 22.5, "g": 0.055, "exit": 12, "p": 0.85},
                     "bull": {"mode": "oe", "oe0": 33.0, "g": 0.089, "exit": 14, "p": 0.80}}},
    "CVX": {"price": 204.38, "shares_m": 1975.8, "shares_note": "10-Q 封面 2026-06-30",
            "sens": 0.60, "bench": "Brent", "base_px": 70,
            "scen": {"bear": {"mode": "oe", "oe0": 12.5, "g": 0.010, "exit": 10, "p": 0.95},
                     "base": {"mode": "oe", "oe0": 18.5, "g": 0.040, "exit": 12, "p": 0.85},
                     "bull": {"mode": "oe", "oe0": 27.5, "g": 0.060, "exit": 14, "p": 0.80}}},
    "OXY": {"price": 54.94, "shares_m": 999.6, "shares_note": "10-Q 封面 2026-07-31（不含伯克希尔 8,390 万股 $59.59 认股权证）",
            "sens": 0.212, "bench": "WTI", "base_px": 65,
            "scen": {"bear": {"mode": "oe", "oe0": 0.4, "g": 0.00, "exit": 9, "p": 0.50},
                     "base": {"mode": "oe", "oe0": 2.5, "g": 0.04, "exit": 11, "p": 0.50},
                     "bull": {"mode": "oe", "oe0": 5.7, "g": 0.05, "exit": 13, "p": 0.50}}},
    "COP": {"price": 125.44, "shares_m": 1201.3, "shares_note": "10-Q 封面 2026-06-30",
            "sens": 0.29, "bench": "WTI", "base_px": 65,
            "scen": {"bear": {"mode": "oe", "oe0": 4.2, "g": 0.015, "exit": 10, "p": 0.90},
                     "base": {"mode": "oe", "oe0": 7.1, "g": 0.048, "exit": 12, "p": 0.90},
                     "bull": {"mode": "oe", "oe0": 11.45, "g": 0.075, "exit": 14, "p": 0.85}}},
    "KMI": {"price": 30.45, "shares_m": 2226.8, "shares_note": "10-Q 封面 2026-07-23",
            "sens": 0.0, "bench": "fee-based", "base_px": None,
            "scen": {"bear": {"mode": "oe", "oe0": 4.3, "g": 0.01, "exit": 11, "p": 0.55},
                     "base": {"mode": "oe", "oe0": 5.0, "g": 0.04, "exit": 13, "p": 0.50},
                     "bull": {"mode": "oe", "oe0": 5.5, "g": 0.06, "exit": 15, "p": 0.50}}},
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
    # ---- 隐含油价：保持 base 的 g / exit / p，只让 OE₀ 随油价线性变化（OE₀(P) = OE_base + sens × (P − base_px)），
    #      解出 base IRR 恰为 8% 时的长期油价
    md += ["## 隐含油价：要拿到 8% 的 10 年回报，需要多高的长期油价", "",
           "| Ticker | 基准 | base 油价 | 敏感度（$B OE / $1） | **8% 所需长期油价** |", "|---|---|---:|---:|---:|"]
    for tk, x in INPUTS.items():
        if not x["sens"]:
            md.append(f"| {tk} | {x['bench']} | — | — | 不适用（收费型） |")
            continue
        mcap = x["price"] * x["shares_m"] / 1000
        base = x["scen"]["base"]
        lo_p, hi_p = 20.0, 200.0
        for _ in range(100):
            mid = (lo_p + hi_p) / 2
            s = dict(base, oe0=base["oe0"] + x["sens"] * (mid - x["base_px"]))
            if s["oe0"] <= 0 or irr(mcap, oe_path(s), s) < 0.08:
                lo_p = mid
            else:
                hi_p = mid
        res["tickers"][tk]["implied_oil_price_for_8pct"] = round(mid, 1)
        md.append(f"| {tk} | {x['bench']} | ${x['base_px']} | {x['sens']:.3f} | **${mid:.1f}** |")
    md.append("")
    (OUT / f"valuation_{AS_OF}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"valuation_{AS_OF}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
