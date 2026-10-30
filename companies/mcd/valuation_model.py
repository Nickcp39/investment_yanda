#!/usr/bin/env python3
"""valuation_model.py — MCD 估值模型（六模块 M6）
公式与 _refresh_uber_adbe_2026-10-20 一致，保证横向可比：
  • 10 年持有期，逐年 owner earnings (OE)；每年把 p×OE 以现金分给股东，第 10 年按 exit 倍数(P/OE)退出
  • IRR 解：市值 = Σ [p·OE_t]/(1+r)^t + OE_10·exit/(1+r)^10
  • 库口径(MSFT 公式，不计中期分配)：(OE_10·exit/市值)^(1/10) − 1
  • 门槛价：r 固定 8%/10%/12%，反解每股价格

OE₀ 口径：FY2025 FCF $7,186M − SBC $165M = $7,021M ≈ $7.0B（麦当劳 SBC 极小，仅 OCF 1.6%）
金额单位：十亿美元；price 美元/股。
"""
from __future__ import annotations
import json
from pathlib import Path

AS_OF = "2026-10-23"
OUT = Path(__file__).resolve().parent / "data"
HURDLES = (0.08, 0.10, 0.12)


def oe(oe0, g, exit_, p, note=""):
    return {"oe0": oe0, "g": g, "exit": exit_, "p": p, "note": note}


INPUTS = {
    "MCD": {
        "name": "McDonald's Corp",
        "ccy": "USD",
        "price": 248.46,
        "unit": 1,
        "shares_m": 707.6,
        "shares_note": "2026-10-23 收盘 $248.46（westock + 财经源双源）；在外股 707.6M（westock total_shares）",
        "scen": {
            "bear": oe(6.5, 0.01, 15, 0.9, "客流持续流失+提价空间耗尽；同店转负、利润率见顶、倍数压缩"),
            "base": oe(7.0, 0.05, 20, 0.9, "同店+2~3%、新店+利润率扩张(46%→50%)、回购增厚EPS；倍数不重估"),
            "bull": oe(7.3, 0.07, 24, 0.9, "NEXT 成功：鸡肉/饮料份额各+1.5pct、利润率50%+、倍数修复"),
        },
    }
}


def oe_path(s):
    return [s["oe0"] * (1 + s["g"]) ** t for t in range(1, 11)]


def pv(path, s, r):
    cf = sum((s["p"] * o) / (1 + r) ** t for t, o in enumerate(path, start=1))
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
    md = [f"# 估值模型输出 {AS_OF}（valuation_model.py 生成）", "",
          "IRR = 含中期分配的 10 年 IRR；库口径 = 不计中期分配(MSFT 公式)。门槛价 = base 情景下 IRR 恰为该门槛的每股价。金额=十亿美元。", ""]
    for tk, x in INPUTS.items():
        mcap = x["price"] * x["unit"] * x["shares_m"] / 1000
        r = {"name": x["name"], "ccy": x["ccy"], "price": x["price"], "shares_m": x["shares_m"],
             "mcap_b": round(mcap, 1), "scenarios": {}}
        md += [f"## {tk} {x['name']} · ${x['price']:,} · 市值 {mcap:,.1f}B（{x['shares_note']}）", "",
               "| 情景 | OE₁ | OE₁₀ | g | 退出 | 派发 | 第10年股权价值 | **IRR** | 库口径IRR | 说明 |",
               "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
        for name, s in x["scen"].items():
            path = oe_path(s)
            tv = path[-1] * s["exit"]
            i = irr(mcap, path, s)
            lib = (tv / mcap) ** 0.1 - 1 if tv > 0 else float("nan")
            r["scenarios"][name] = {"oe0": s["oe0"], "g": s["g"], "exit": s["exit"], "p": s["p"],
                                   "oe_1": round(path[0], 3), "oe_10": round(path[-1], 3),
                                   "tv_10_b": round(tv, 1), "irr": round(i, 4), "irr_lib": round(lib, 4)}
            md.append(f"| {name} | {path[0]:.2f} | {path[-1]:.2f} | {s['g']:+.1%} | {s['exit']}x | {s['p']:.0%} | "
                      f"{tv:,.1f}B | **{i:+.1%}** | {lib:+.1%} | {s['note']} |")
        to_px = 1000 / x["shares_m"] / x["unit"]
        base, bull, bear = x["scen"]["base"], x["scen"]["bull"], x["scen"]["bear"]
        bpath = oe_path(base)
        hp = {f"{int(h*100)}pct": round(pv(bpath, base, h) * to_px, 2) for h in HURDLES}
        hp["8pct_on_bull"] = round(pv(oe_path(bull), bull, 0.08) * to_px, 2)
        hp["8pct_on_bear"] = round(pv(oe_path(bear), bear, 0.08) * to_px, 2)
        r["hurdle_prices"] = hp
        r["distance_to_8pct"] = round(hp["8pct"] / x["price"] - 1, 4)
        lo, hi = -0.10, 0.40
        for _ in range(100):
            mid = (lo + hi) / 2
            s2 = dict(base, g=mid)
            if irr(mcap, oe_path(s2), s2) < 0.08:
                lo = mid
            else:
                hi = mid
        r["implied_g_for_8pct"] = round(mid, 4)
        sens = {}
        for label, kw in {"g-2pt": {"g": base["g"] - 0.02}, "g-4pt": {"g": base["g"] - 0.04},
                          "exit-3x": {"exit": base["exit"] - 3}, "exit-5x": {"exit": base["exit"] - 5},
                          "oe0-10%": {"oe0": base["oe0"] * 0.9}}.items():
            s2 = dict(base, **kw)
            sens[label] = round(irr(mcap, oe_path(s2), s2), 4)
        r["sensitivity_base"] = sens
        res["tickers"][tk] = r
        md += ["", f"门槛价(base)：8% **${hp['8pct']:,.2f}**（距现价 {hp['8pct']/x['price']-1:+.1%}）· 10% ${hp['10pct']:,.2f} · "
                   f"12% ${hp['12pct']:,.2f} · bull 8% ${hp['8pct_on_bull']:,.2f} · bear 8% ${hp['8pct_on_bear']:,.2f}",
               f"8% 所需 10 年每股 OE 年增速（OE₀/退出/派发不变）：**{mid:+.1%}**（base 假设 {base['g']:+.1%}）",
               "敏感性(base 只改一个参数)：" + " · ".join(f"{k}→{v:+.1%}" for k, v in sens.items()), ""]
    (OUT / f"valuation_{AS_OF}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"valuation_{AS_OF}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
