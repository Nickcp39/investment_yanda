#!/usr/bin/env python3
"""valuation_model.py — UBER / ADBE 刷新批次 _refresh_uber_adbe_2026-10-20 的 M6 统一估值模型
（由 _trading_rails_2026-10-06/valuation_model.py 复制；公式不变，新增 extra_cf 叠加层）

公式（与佩洛西 / 石油 / 电力 / 交易通道批次相同，保证横向可比）：
  • 10 年持有期，逐年 owner earnings（OE）；每年把 p×OE 以现金分给股东，第 10 年按 exit 倍数（P/OE）退出
  • IRR 解：市值 = Σ [p·OE_t + extra_cf_t]/(1+r)^t + OE_10·exit/(1+r)^10
  • 库口径（MSFT 公式，不计中期分配）：(OE_10·exit / 市值)^(1/10) − 1
  • 门槛价：r 固定为 8% / 10% / 12%，反解每股价格

本批新增 extra_cf（叠加层，默认全零）：
  UBER 的 Delivery Hero 要约 —— 第 2 年（2027 下半年交割）一次性现金流出（收购剩余约 75% 股权），
  之后逐年并入 Delivery Hero 的自由现金流（按 2026 指引 FCF > €250M 的保守口径起步，与 base 同增速）。
  这样做的原因：这笔支出不走 capex、不在 FCF 里，但它是真实的股东现金流出（独立 Checker 2026-09-28 的修正项 C.1-1）。

OE₀ 口径（推导见各家 valuation.md）：
  UBER：FCF − SBC（$8.18B）− 现金税正常化（−$1.44B，NOL 递延税资产正在消耗）− 一半 AV 投入（−$1.25B）= 严格口径 $5.5B；
        base 取 $5.9B（与独立 Checker 盲估一致；差额 $0.4B 是尚余约 3 年的税盾按 10 年摊）
  ADBE：TTM FCF（$10.59B）− TTM SBC（$2.07B）= $8.52B；base 取 $8.5B。全公司（市值）口径，净债 $0.7B 忽略不计
金额单位：十亿美元；price 为美元每股。
用法: python companies/_refresh_uber_adbe_2026-10-20/valuation_model.py
输出: data/valuation_2026-10-20.json + data/valuation_2026-10-20.md
"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-10-20"
OUT = Path(__file__).resolve().parent / "data"
HURDLES = (0.08, 0.10, 0.12)

# Delivery Hero 叠加层（UBER）：第 2 年流出 $11.1B（100% 股权 $14.8B × 剩余 75%），第 2 年起并入 DH 自由现金流
DH_OUTFLOW_B = 11.1
DH_FCF_START_B = 0.30  # €250M 指引下限 ≈ $0.29B；bear 取 0，bull 取 0.6


def oe(oe0, g, exit_, p, extra=None, note=""):
    return {"mode": "oe", "oe0": oe0, "g": g, "exit": exit_, "p": p, "extra_cf": extra or [0.0] * 10, "note": note}


def dh_overlay(dh_fcf0, g):
    """Delivery Hero：第 2 年末流出 DH_OUTFLOW_B，第 2 年起每年并入 DH FCF（按 g 增长，p 视同 1 —— 全部归股东口径的简化）"""
    cf = [0.0] * 10
    for t in range(2, 11):
        cf[t - 1] = dh_fcf0 * (1 + g) ** (t - 2)
    cf[1] -= DH_OUTFLOW_B
    return cf


# price = 2026-10-20 收盘（Yahoo = Nasdaq，双源一致，见 freshness.json）
INPUTS = {
    "UBER": {"name": "Uber Technologies", "ccy": "USD", "price": 68.94, "unit": 1, "shares_m": 2050.2,
             "shares_note": "Q2 2026 摊薄加权 2,050.2M（10-Q / XBRL）；封面 2,042.56M（2026-07-31）",
             "scen": {
                 "bear": oe(5.0, 0.03, 12, 0.5, dh_overlay(0.0, 0.03), "AV 全额计为维护；DH 并入后零自由现金流"),
                 "base": oe(5.9, 0.10, 17, 0.6, dh_overlay(DH_FCF_START_B, 0.10), "局部侵蚀；DH 按指引下限 FCF 并入"),
                 "bull": oe(6.9, 0.14, 22, 0.7, dh_overlay(0.6, 0.14), "Uber 成为 AV 车队的需求层；DH 协同兑现"),
                 "base_no_DH": oe(5.9, 0.10, 17, 0.6, None, "对照：不含 Delivery Hero（与 09-28 Checker 盲估同口径）"),
             }},
    "ADBE": {"name": "Adobe", "ccy": "USD", "price": 256.73, "unit": 1, "shares_m": 395.0,
             "shares_note": "Q3 FY26 摊薄加权 395M（8-K）；2026-08-28 在外 391M（10-Q 封面）",
             "scen": {
                 "bear": oe(8.5, -0.06, 7, 0.9, None, "生成式替代咬进来：收入归零转负、利润率 45% → 33%"),
                 "base": oe(8.5, 0.06, 13, 0.9, None, "有机 ARR 稳在 7–8%、利润率守住、回购继续；倍数不重估"),
                 "bull": oe(8.5, 0.10, 18, 0.9, None, "freemium 转化跑通 + AI-first ARR 上量；倍数部分修复"),
                 "harvest": oe(8.5, 0.02, 10, 0.9, None, "对照：净新增 ARR 持续 −36% 的延伸 —— 收入增速滑到低个位数、倍数再压"),
             }},
}


def oe_path(s):
    return [s["oe0"] * (1 + s["g"]) ** t for t in range(1, 11)]


def pv(path, s, r):
    cf = sum((s["p"] * o + s["extra_cf"][t - 1]) / (1 + r) ** t for t, o in enumerate(path, start=1))
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
          "IRR = 含中期分配的 10 年 IRR；库口径 = 不计中期分配（MSFT 公式）。门槛价 = base 情景下 IRR 恰为该门槛的每股价。",
          "金额 = 十亿美元；价格为美元每股。UBER 的 base / bear / bull 已叠加 Delivery Hero 现金流（第 2 年流出 $11.1B）。", ""]
    for tk, x in INPUTS.items():
        mcap = x["price"] * x["unit"] * x["shares_m"] / 1000
        r = {"name": x["name"], "ccy": x["ccy"], "price": x["price"], "shares_m": x["shares_m"],
             "mcap_b": round(mcap, 1), "scenarios": {}}
        md += [f"## {tk} {x['name']} · {x['price']:,} · 市值 {mcap:,.1f}B {x['ccy']}（{x['shares_note']}）", "",
               "| 情景 | OE₁ | OE₁₀ | g | 退出 | 派发比例 | 叠加现金流合计 | 第10年股权价值 | **IRR** | 库口径 IRR | 说明 |",
               "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
        for name, s in x["scen"].items():
            path = oe_path(s)
            tv = path[-1] * s["exit"]
            i = irr(mcap, path, s)
            lib = (tv / mcap) ** 0.1 - 1 if tv > 0 else float("nan")
            r["scenarios"][name] = {**{k: v for k, v in s.items() if k != "extra_cf"}, "extra_cf_sum_b": round(sum(s["extra_cf"]), 2),
                                   "oe_1": round(path[0], 3), "oe_10": round(path[-1], 3), "tv_10_b": round(tv, 1),
                                   "irr": round(i, 4), "irr_lib": round(lib, 4)}
            md.append(f"| {name} | {path[0]:.2f} | {path[-1]:.2f} | {s['g']:+.1%} | {s['exit']}x | {s['p']:.0%} | "
                      f"{sum(s['extra_cf']):+.1f}B | {tv:,.1f}B | **{i:+.1%}** | {lib:+.1%} | {s['note']} |")
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
            s = dict(base, g=mid)
            if irr(mcap, oe_path(s), s) < 0.08:
                lo = mid
            else:
                hi = mid
        r["implied_g_for_8pct"] = round(mid, 4)
        # 敏感性：只改一个参数
        sens = {}
        for label, kw in {"g-2pt": {"g": base["g"] - 0.02}, "g-4pt": {"g": base["g"] - 0.04}, "exit-3x": {"exit": base["exit"] - 3},
                          "exit-5x": {"exit": base["exit"] - 5}, "oe0-10%": {"oe0": base["oe0"] * 0.9}}.items():
            s = dict(base, **kw)
            sens[label] = round(irr(mcap, oe_path(s), s), 4)
        r["sensitivity_base"] = sens
        res["tickers"][tk] = r
        md += ["", f"门槛价（base）：8% **{hp['8pct']:,.2f}**（距现价 {hp['8pct']/x['price']-1:+.1%}）· "
                   f"10% {hp['10pct']:,.2f} · 12% {hp['12pct']:,.2f} · bull 情景 8% 门槛价 {hp['8pct_on_bull']:,.2f} · "
                   f"bear 情景 8% 门槛价 {hp['8pct_on_bear']:,.2f}",
               f"8% 所需的 10 年每股 OE 年增速（OE₀ / 退出倍数 / 派发不变）：**{mid:+.1%}**（base 假设 {base['g']:+.1%}）",
               "敏感性（base 只改一个参数）：" + " · ".join(f"{k} → {v:+.1%}" for k, v in sens.items()), ""]
    (OUT / f"valuation_{AS_OF}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"valuation_{AS_OF}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
