#!/usr/bin/env python3
"""valuation_model.py — 交易通道批次 _trading_rails_2026-10-06 的 M6 统一估值模型
（由 _power_majors_2026-10-03/valuation_model.py 复制；公式不变，只换输入）

公式（与佩洛西 / 石油 / 电力批次相同，保证横向可比）：
  • 10 年持有期，逐年 owner earnings（OE）；每年把 p×OE 以现金分给股东，第 10 年按 exit 倍数（P/OE）退出
  • IRR 解：市值 = Σ p·OE_t/(1+r)^t + OE_10·exit/(1+r)^10
  • 库口径（MSFT 公式，不计中期分配）：(OE_10·exit / 市值)^(1/10) − 1
  • 门槛价：r 固定为 8% / 10% / 12%，反解每股价格

本批 OE₀ 的口径（推导见各家 valuation.md）：
  • 券商 / 交易所 / 做市商的经营现金流被客户资金、保证金、交易头寸扭曲，FCF 不可用 → OE₀ = 正常化的税后净利
    （交易所、BR 用公司"adjusted"口径：加回并购无形资产摊销，这部分是非现金且无须再投入）
  • **周期正常化**：本批 13 家里 9 家的 TTM 处在交易量 / 利率的高位（美股成交 2025 年 +44.6%，期权连续 6 年创纪录），
    base OE₀ 一律打在 TTM 之下；bear 用 2022 年式的交易量回落 + 降息
  • IBKR / VIRT 按"全部转换为普通股并全额纳税"的口径（IBKR：A 类 453.1M + Holdings 持有的 LLC 单位 1,250.7M；
    VIRT：公司披露的 Weighted Average Adjusted shares）
  • 亏损或刚起步的公司（CRCL / BTGO / SECZ）用 ramp：OE₁ → OE₁₀ 两点几何插值
  • 管理层指引：base 给 50% 信用（与前几批一致）
金额单位：十亿美元；price 为美元每股（FUTU 为每 ADS，1 ADS = 8 股 A 类普通股；报表港元按 7.84 折美元）。

用法: python companies/_trading_rails_2026-10-06/valuation_model.py
输出: data/valuation_2026-10-06.json + data/valuation_2026-10-06.md
"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-10-06"
OUT = Path(__file__).resolve().parent / "data"
HURDLES = (0.08, 0.10, 0.12)


def oe(oe0, g, exit_, p):
    return {"mode": "oe", "oe0": oe0, "g": g, "exit": exit_, "p": p}


def ramp(oe1, oe10, exit_, p=0.0):
    return {"mode": "ramp", "oe1": oe1, "oe10": oe10, "exit": exit_, "p": p}


# price = 2026-10-06 收盘（Yahoo = Nasdaq，双源一致，见 freshness.json）
INPUTS = {
    "IBKR": {"name": "Interactive Brokers", "ccy": "USD", "price": 90.58, "unit": 1, "shares_m": 1703.8,
             "shares_note": "A 类 453.1M（10-Q 封面 2026-08-05）+ IBG Holdings 持有的 LLC 单位 1,250.7M（8-K 表，73.5%）= 全部转换口径",
             "scen": {"bear": oe(3.0, 0.04, 15, 0.10), "base": oe(3.7, 0.11, 22, 0.10), "bull": oe(4.2, 0.15, 25, 0.10)}},
    "HOOD": {"name": "Robinhood", "ccy": "USD", "price": 112.00, "unit": 1, "shares_m": 925.0,
             "shares_note": "A 类 790.6M + B 类 108.5M（10-Q 封面 2026-07-23）；估值用 Q2 摊薄加权 912M + 2026-06 可转债 12.6M ≈ 925M",
             "scen": {"bear": oe(1.1, 0.06, 15, 0.10), "base": oe(1.7, 0.15, 25, 0.10), "bull": oe(2.2, 0.22, 30, 0.10)}},
    "COIN": {"name": "Coinbase", "ccy": "USD", "price": 185.74, "unit": 1, "shares_m": 275.0,
             "shares_note": "A 类 222.8M + B 类 41.0M（10-Q 封面 2026-07-23）；估值用盈利季度的摊薄口径约 275M（2025Q2 摊薄 278.9M）",
             "scen": {"bear": oe(0.4, 0.05, 18, 0.0), "base": oe(1.2, 0.12, 25, 0.0), "bull": oe(2.5, 0.18, 30, 0.0)}},
    "FUTU": {"name": "Futu Holdings", "ccy": "USD", "price": 113.21, "unit": 1, "shares_m": 140.0,
             "shares_note": "Q2 2026 摊薄普通股 1,120.1M ÷ 8 = 140.0M ADS（6-K）",
             "scen": {"bear": oe(0.8, 0.03, 8, 0.20), "base": oe(1.35, 0.10, 12, 0.20), "bull": oe(1.7, 0.15, 16, 0.20)}},
    "VIRT": {"name": "Virtu Financial", "ccy": "USD", "price": 61.62, "unit": 1, "shares_m": 159.9,
             "shares_note": "Weighted Average Adjusted shares 159.9M（Q2 2026 8-K，假设非控股权益全部转换）",
             "scen": {"bear": oe(0.45, 0.00, 8, 0.80), "base": oe(0.75, 0.04, 11, 0.80), "bull": oe(1.0, 0.06, 13, 0.70)}},
    "CBOE": {"name": "Cboe Global Markets", "ccy": "USD", "price": 278.20, "unit": 1, "shares_m": 105.0,
             "shares_note": "Q2 2026 摊薄加权 105.0M（8-K）",
             "scen": {"bear": oe(1.05, 0.04, 16, 0.55), "base": oe(1.25, 0.08, 22, 0.55), "bull": oe(1.36, 0.11, 26, 0.55)}},
    "CME": {"name": "CME Group", "ccy": "USD", "price": 270.18, "unit": 1, "shares_m": 361.3,
            "shares_note": "A 类 359.6M（10-Q 封面 2026-07-08）；估值用 Q2 摊薄 361.3M",
            "scen": {"bear": oe(3.8, 0.03, 17, 0.90), "base": oe(4.3, 0.06, 22, 0.90), "bull": oe(4.5, 0.085, 25, 0.90)}},
    "ICE": {"name": "Intercontinental Exchange", "ccy": "USD", "price": 153.49, "unit": 1, "shares_m": 568.0,
            "shares_note": "561.4M（10-Q 封面 2026-07-27）；估值用 H1 摊薄加权 568M",
            "scen": {"bear": oe(3.8, 0.04, 16, 0.60), "base": oe(4.3, 0.07, 21, 0.60), "bull": oe(4.5, 0.095, 24, 0.60)}},
    "NDAQ": {"name": "Nasdaq", "ccy": "USD", "price": 92.27, "unit": 1, "shares_m": 567.8,
             "shares_note": "Q2 2026 摊薄加权 567.8M（8-K）",
             "scen": {"bear": oe(1.9, 0.04, 16, 0.50), "base": oe(2.15, 0.08, 22, 0.50), "bull": oe(2.3, 0.11, 26, 0.50)}},
    "BR": {"name": "Broadridge", "ccy": "USD", "price": 158.66, "unit": 1, "shares_m": 115.6,
           "shares_note": "FY2026 Q4 摊薄加权 115.6M（8-K）",
           "scen": {"bear": oe(1.0, 0.02, 12, 0.55), "base": oe(1.11, 0.07, 18, 0.55), "bull": oe(1.15, 0.10, 22, 0.55)}},
    "CRCL": {"name": "Circle", "ccy": "USD", "price": 84.13, "unit": 1, "shares_m": 268.6,
             "shares_note": "A 类 234.7M + B 类 19.2M（10-Q 封面 2026-07-30）；估值用 Q2 摊薄 268.6M",
             "scen": {"bear": ramp(0.10, 0.40, 15), "base": ramp(0.25, 1.80, 20), "bull": ramp(0.40, 5.0, 25)}},
    "BTGO": {"name": "BitGo", "ccy": "USD", "price": 7.19, "unit": 1, "shares_m": 117.5,
             "shares_note": "A 类 108.7M + B 类 8.9M（10-Q 封面 2026-08-07）",
             "scen": {"bear": ramp(0.005, 0.03, 12), "base": ramp(0.01, 0.10, 15), "bull": ramp(0.02, 0.25, 20)}},
    "SECZ": {"name": "Securitize", "ccy": "USD", "price": 12.70, "unit": 1, "shares_m": 163.3,
             "shares_note": "163.3M（XBRL 封面，SPAC 合并后；未逐项核对 earn-out / 认股权证）",
             "scen": {"bear": ramp(0.005, 0.05, 15), "base": ramp(0.01, 0.25, 20), "bull": ramp(0.02, 0.60, 25)}},
}


def oe_path(s):
    if s["mode"] == "oe":
        return [s["oe0"] * (1 + s["g"]) ** t for t in range(1, 11)]
    if s["mode"] == "ramp":
        k = (s["oe10"] / s["oe1"]) ** (1 / 9)
        return [s["oe1"] * k ** (t - 1) for t in range(1, 11)]
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
          "IRR = 含中期分配的 10 年 IRR；库口径 = 不计中期分配（MSFT 公式）。门槛价 = base 情景下 IRR 恰为该门槛的每股价。",
          "金额 = 十亿美元；价格为美元每股（FUTU 为每 ADS）。", ""]
    for tk, x in INPUTS.items():
        mcap = x["price"] * x["unit"] * x["shares_m"] / 1000  # 十亿本币
        r = {"name": x["name"], "ccy": x["ccy"], "price": x["price"], "shares_m": x["shares_m"],
             "mcap_b": round(mcap, 1), "scenarios": {}}
        md += [f"## {tk} {x['name']} · {x['price']:,} · 市值 {mcap:,.1f}B {x['ccy']}（{x['shares_note']}）", "",
               "| 情景 | OE₁ | OE₁₀ | g | 退出 | 派发比例 | 第10年股权价值 | **IRR** | 库口径 IRR |",
               "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for name, s in x["scen"].items():
            path = oe_path(s)
            tv = path[-1] * s["exit"]
            i = irr(mcap, path, s)
            lib = (tv / mcap) ** 0.1 - 1 if tv > 0 else float("nan")
            r["scenarios"][name] = {**s, "oe_1": round(path[0], 3), "oe_10": round(path[-1], 3),
                                   "tv_10_b": round(tv, 1), "irr": round(i, 4), "irr_lib": round(lib, 4)}
            gtxt = f"{s['g']:+.1%}" if s["mode"] == "oe" else f"ramp {((path[-1] / path[0]) ** (1 / 9) - 1):+.0%}/年"
            md.append(f"| {name} | {path[0]:.2f} | {path[-1]:.2f} | {gtxt} | {s['exit']}x | {s['p']:.0%} | "
                      f"{tv:,.1f}B | **{i:+.1%}** | {lib:+.1%} |")
        to_px = 1000 / x["shares_m"] / x["unit"]  # 十亿本币 → 每股价格单位
        base, bull, bear = x["scen"]["base"], x["scen"]["bull"], x["scen"]["bear"]
        bpath = oe_path(base)
        hp = {f"{int(h*100)}pct": round(pv(bpath, base, h) * to_px, 2) for h in HURDLES}
        hp["8pct_on_bull"] = round(pv(oe_path(bull), bull, 0.08) * to_px, 2)
        hp["8pct_on_bear"] = round(pv(oe_path(bear), bear, 0.08) * to_px, 2)
        r["hurdle_prices"] = hp
        r["distance_to_8pct"] = round(hp["8pct"] / x["price"] - 1, 4)
        # 8% 所需的 10 年 OE 增速：保持 base 的 OE₀ / exit / p，只解 g（ramp 情景：保持 OE₁，解第 10 年 OE）
        if base["mode"] == "oe":
            lo, hi = -0.10, 0.40
            for _ in range(100):
                mid = (lo + hi) / 2
                s = dict(base, g=mid)
                if irr(mcap, oe_path(s), s) < 0.08:
                    lo = mid
                else:
                    hi = mid
            r["implied_g_for_8pct"] = round(mid, 4)
            gline = f"8% 所需的 10 年每股 OE 年增速（OE₀ / 退出倍数 / 派发不变）：**{mid:+.1%}**（base 假设 {base['g']:+.1%}）"
        else:
            lo, hi = base["oe1"] * 1.01, 1000.0
            for _ in range(200):
                mid = (lo + hi) / 2
                s = dict(base, oe10=mid)
                if irr(mcap, oe_path(s), s) < 0.08:
                    lo = mid
                else:
                    hi = mid
            r["implied_oe10_for_8pct_b"] = round(mid, 3)
            r["implied_g_for_8pct"] = round((mid / base["oe1"]) ** (1 / 9) - 1, 4)
            gline = (f"8% 所需的第 10 年 OE（OE₁ / 退出倍数不变）：**${mid:,.2f}B**（base 假设 ${base['oe10']:,.2f}B），"
                     f"即 OE 年增 {r['implied_g_for_8pct']:+.0%}")
        res["tickers"][tk] = r
        md += ["", f"门槛价（base）：8% **{hp['8pct']:,.2f}**（距现价 {hp['8pct']/x['price']-1:+.1%}）· "
                   f"10% {hp['10pct']:,.2f} · 12% {hp['12pct']:,.2f} · bull 情景 8% 门槛价 {hp['8pct_on_bull']:,.2f} · "
                   f"bear 情景 8% 门槛价 {hp['8pct_on_bear']:,.2f}",
               gline, ""]
    (OUT / f"valuation_{AS_OF}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"valuation_{AS_OF}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
