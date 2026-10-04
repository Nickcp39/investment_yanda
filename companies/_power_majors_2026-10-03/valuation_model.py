#!/usr/bin/env python3
"""valuation_model.py — 电力大国批次 _power_majors_2026-10-03 的 M6 统一估值模型
（由 _oil_2026-09-30/valuation_model.py 复制；公式不变，只换输入；『隐含油价』换成『8% 所需的 10 年 OE 增速』）

公式（与佩洛西 / 石油批次相同，保证横向可比）：
  • 10 年持有期，逐年 owner earnings（OE）；每年把 p×OE 以现金分给股东，第 10 年按 exit 倍数（P/OE）退出
  • IRR 解：市值 = Σ p·OE_t/(1+r)^t + OE_10·exit/(1+r)^10
  • 库口径（MSFT 公式，不计中期分配）：(OE_10·exit / 市值)^(1/10) − 1
  • 门槛价：r 固定为 8% / 10% / 12%，反解每股价格

电力公司的 OE₀：成长性资本开支让 FCF 长期为负，FCF − SBC 不可用 → 两个锚互相校验（推导见各家 valuation.md）：
  锚 A = 归母净利润（剔除一次性特别损益；英国两家用公司"underlying / adjusted"与法定口径两头）
  锚 B = 经营现金流 − 折旧摊销（把折旧当作维护性资本开支的代理；OCF 已扣利息和税）
  OE₀ 取两锚之间偏保守的值；g 为【每股】OE 增速（英国两家管理层指引已含 scrip 稀释）。
  管理层增长指引：base 给 50% 信用（与石油批次一致），bull 100%，bear 0。
金额单位：十亿本币（日元 / 英镑 / 人民币 / 港元）；price 为报价货币每股（英股为便士 /100；人民币报表的 H 股为港元 ×0.8545）。

用法: python companies/_power_majors_2026-10-03/valuation_model.py
输出: data/valuation_2026-10-03.json + data/valuation_2026-10-03.md
"""
from __future__ import annotations

import json
from pathlib import Path

AS_OF = "2026-10-03"
OUT = Path(__file__).resolve().parent / "data"
HURDLES = (0.08, 0.10, 0.12)

# price: 日股 / 英股 = 2026-10-02 收盘（Yahoo = CNBC，双源一致），A 股 = 2026-09-30（国庆休市）
# unit: 价格单位 → 本币的换算（便士 /100）
INPUTS = {
    "9501.T": {"name": "东京电力 TEPCO", "ccy": "JPY", "price": 524.0, "unit": 1, "shares_m": 4936.0,
               "shares_note": "完全摊薄：普通股 1,602.7M（2026Q1 短信）+ 机构优先股可转 3,333.3M（短信『潜在株式』注记）；仅普通股为 1,602.7M",
               "scen": {"bear": {"mode": "oe", "oe0": 30, "g": 0.00, "exit": 6, "p": 0.0},
                        "base": {"mode": "oe", "oe0": 150, "g": 0.03, "exit": 9, "p": 0.0},
                        "bull": {"mode": "oe", "oe0": 300, "g": 0.05, "exit": 12, "p": 0.2}}},
    "9503.T": {"name": "关西电力", "ccy": "JPY", "price": 2632.5, "unit": 1, "shares_m": 1114.2,
               "shares_note": "发行 1,114.93M − 库存 0.75M（2026Q1 短信）",
               "scen": {"bear": {"mode": "oe", "oe0": 200, "g": 0.00, "exit": 7, "p": 0.30},
                        "base": {"mode": "oe", "oe0": 290, "g": 0.02, "exit": 10, "p": 0.30},
                        "bull": {"mode": "oe", "oe0": 360, "g": 0.035, "exit": 13, "p": 0.35}}},
    "642A.T": {"name": "九州电力（Kyuden Holdings）", "ccy": "JPY", "price": 1969.5, "unit": 1, "shares_m": 472.8,
               "shares_note": "9508 于 2026-10-01 按 1:1 转为 Kyuden Holdings（642A）；发行 474.18M − 库存 1.41M（FY3/2026 短信，9-30 注销库存股）；OE 已扣 B 种优先股股息约 ¥5.8B/年",
               "scen": {"bear": {"mode": "oe", "oe0": 100, "g": 0.00, "exit": 6, "p": 0.17},
                        "base": {"mode": "oe", "oe0": 140, "g": 0.025, "exit": 9, "p": 0.17},
                        "bull": {"mode": "oe", "oe0": 180, "g": 0.04, "exit": 12, "p": 0.25}}},
    "9513.T": {"name": "电源开发 J-POWER", "ccy": "JPY", "price": 4016.0, "unit": 1, "shares_m": 176.0,
               "shares_note": "发行 183.05M − 库存 7.04M（FY3/2026 短信；4 月注销 6.71M 库存股不改变流通股数）",
               "scen": {"bear": {"mode": "oe", "oe0": 55, "g": -0.02, "exit": 6, "p": 0.35},
                        "base": {"mode": "oe", "oe0": 85, "g": 0.01, "exit": 9, "p": 0.30},
                        "bull": {"mode": "oe", "oe0": 110, "g": 0.03, "exit": 12, "p": 0.35}}},
    "NG.L": {"name": "National Grid", "ccy": "GBP", "price": 1146.5, "unit": 0.01, "shares_m": 5026.8,
             "shares_note": "有表决权股 5,026.8M（2026-07-23 Total Voting Rights 6-K，已含 2025/26 末期 scrip）",
             "scen": {"bear": {"mode": "oe", "oe0": 2.95, "g": 0.03, "exit": 11, "p": 0.65},
                      "base": {"mode": "oe", "oe0": 3.45, "g": 0.06, "exit": 14, "p": 0.60},
                      "bull": {"mode": "oe", "oe0": 3.9, "g": 0.09, "exit": 16, "p": 0.55}}},
    "SSE.L": {"name": "SSE", "ccy": "GBP", "price": 2447.0, "unit": 0.01, "shares_m": 1212.2,
              "shares_note": "2026-03-31 已发行 1,215.5M − 库存 3.3M（FY26 业绩公告）；2025-11 £2bn 增发后",
              "scen": {"bear": {"mode": "oe", "oe0": 1.30, "g": 0.03, "exit": 10, "p": 0.55},
                       "base": {"mode": "oe", "oe0": 1.55, "g": 0.07, "exit": 14, "p": 0.50},
                       "bull": {"mode": "oe", "oe0": 1.86, "g": 0.10, "exit": 16, "p": 0.45}}},
    # ---- 中国（Phase 2）：A 股 = 2026-09-30 收盘（国庆休市）；港股 = 2026-10-02 收盘。
    # 人民币报表的 H 股：价格为港元，unit = 0.8545（HKD→CNY，Yahoo HKDCNY=X 2026-10-02；= CNY=X 6.7045 / HKD=X 7.8464 交叉一致）
    # 估值用 H 股价 × 全部股本（A+H）：用户可买的是 H 股，A 股价格更高（见各家 facts.md 的 A/H 溢价）
    "600900.SS": {"name": "长江电力", "ccy": "CNY", "price": 28.54, "unit": 1, "shares_m": 24468.2,
                  "shares_note": "总股本 24,468,217,716（2025 年报）",
                  "scen": {"bear": {"mode": "oe", "oe0": 31.5, "g": 0.00, "exit": 14, "p": 0.70},
                           "base": {"mode": "oe", "oe0": 34.0, "g": 0.025, "exit": 18, "p": 0.72},
                           "bull": {"mode": "oe", "oe0": 37.0, "g": 0.04, "exit": 22, "p": 0.75}}},
    "1816.HK": {"name": "中广核电力（H）", "ccy": "CNY", "price": 3.04, "unit": 0.8545, "shares_m": 50498.6,
                "shares_note": "A+H 总股本 50,498,611,100（2025 年度业绩）；A 股可转债在转股期（另计稀释约 1–2%，未计入）",
                "scen": {"bear": {"mode": "oe", "oe0": 8.0, "g": 0.00, "exit": 8, "p": 0.45},
                         "base": {"mode": "oe", "oe0": 9.5, "g": 0.03, "exit": 12, "p": 0.45},
                         "bull": {"mode": "oe", "oe0": 11.0, "g": 0.05, "exit": 15, "p": 0.45}}},
    "0902.HK": {"name": "华能国际（H）", "ccy": "CNY", "price": 6.04, "unit": 0.8545, "shares_m": 15698.1,
                "shares_note": "A+H 总股本 15,698,093,359（2025 年报）；OE 为扣除永续债（¥775 亿）利息后的普通股口径",
                "scen": {"bear": {"mode": "oe", "oe0": 5.5, "g": -0.02, "exit": 6, "p": 0.50},
                         "base": {"mode": "oe", "oe0": 8.0, "g": 0.01, "exit": 8, "p": 0.50},
                         "bull": {"mode": "oe", "oe0": 11.6, "g": 0.03, "exit": 10, "p": 0.50}}},
    "0836.HK": {"name": "华润电力", "ccy": "HKD", "price": 19.44, "unit": 1, "shares_m": 5177.1,
                "shares_note": "普通股 5,177,057,740（2026 中期业绩每股盈利分母，期内无变化）；报表货币港元",
                "scen": {"bear": {"mode": "oe", "oe0": 10.0, "g": 0.00, "exit": 6, "p": 0.40},
                         "base": {"mode": "oe", "oe0": 12.5, "g": 0.03, "exit": 8, "p": 0.40},
                         "bull": {"mode": "oe", "oe0": 15.2, "g": 0.05, "exit": 10, "p": 0.40}}},
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
          "金额 = 十亿本币；英股价格为便士。", ""]
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
            md.append(f"| {name} | {path[0]:.2f} | {path[-1]:.2f} | {s['g']:+.1%} | {s['exit']}x | {s['p']:.0%} | "
                      f"{tv:,.1f}B | **{i:+.1%}** | {lib:+.1%} |")
        to_px = 1000 / x["shares_m"] / x["unit"]  # 十亿本币 → 每股价格单位
        base, bull, bear = x["scen"]["base"], x["scen"]["bull"], x["scen"]["bear"]
        bpath = oe_path(base)
        hp = {f"{int(h*100)}pct": round(pv(bpath, base, h) * to_px, 2) for h in HURDLES}
        hp["8pct_on_bull"] = round(pv(oe_path(bull), bull, 0.08) * to_px, 2)
        hp["8pct_on_bear"] = round(pv(oe_path(bear), bear, 0.08) * to_px, 2)
        r["hurdle_prices"] = hp
        r["distance_to_8pct"] = round(hp["8pct"] / x["price"] - 1, 4)
        # 8% 所需的 10 年 OE 增速：保持 base 的 OE₀ / exit / p，只解 g
        lo, hi = -0.10, 0.40
        for _ in range(100):
            mid = (lo + hi) / 2
            s = dict(base, g=mid)
            if irr(mcap, oe_path(s), s) < 0.08:
                lo = mid
            else:
                hi = mid
        r["implied_g_for_8pct"] = round(mid, 4)
        res["tickers"][tk] = r
        md += ["", f"门槛价（base）：8% **{hp['8pct']:,.2f}**（距现价 {hp['8pct']/x['price']-1:+.1%}）· "
                   f"10% {hp['10pct']:,.2f} · 12% {hp['12pct']:,.2f} · bull 情景 8% 门槛价 {hp['8pct_on_bull']:,.2f} · "
                   f"bear 情景 8% 门槛价 {hp['8pct_on_bear']:,.2f}",
               f"8% 所需的 10 年每股 OE 年增速（OE₀ / 退出倍数 / 派发不变）：**{mid:+.1%}**（base 假设 {base['g']:+.1%}）", ""]
    (OUT / f"valuation_{AS_OF}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / f"valuation_{AS_OF}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
