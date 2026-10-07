#!/usr/bin/env python3
"""make_dossiers.py — 交易通道批次：生成 13 个 dossier 的 lean-6module 文件 + decision_card.json。

数字只从三处读（单一数据源）：
  data/valuation_2026-10-06.json   估值、门槛价、情景（valuation_model.py 产物）
  <dossier>/freshness.json         价格、52 周、股数、市值（make_freshness.py 产物，Yahoo + Nasdaq 双源）
  data/snapshot_2026-10-06.json    12 个月前收盘价（fetch_data.py 产物）
判断性内容（M1–M6 文字、信号、kill criteria）在 dossier_content.py。
产物（每家）：facts.md · thesis_mechanism.md · profit_pool_durability.md · financial_reality.md ·
              inversion_trap_test.md · valuation.md · decision_card.md · decision_card.json
用法: python companies/_trading_rails_2026-10-06/make_dossiers.py
"""
from __future__ import annotations

import json
from pathlib import Path

from dossier_content import C

AS_OF = "2026-10-06"
RUN_DATE = "2026-10-07"
BATCH = "trading_rails_2026-10-06"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VAL = json.loads((HERE / "data" / f"valuation_{AS_OF}.json").read_text(encoding="utf-8"))["tickers"]
SNAP = json.loads((HERE / "data" / f"snapshot_{AS_OF}.json").read_text(encoding="utf-8"))["tickers"]
SRC = json.loads((HERE / "data" / f"sources_{AS_OF}.json").read_text(encoding="utf-8"))
SIG = lambda v: f"{v:+d}".replace("-", "−")  # noqa: E731
KIND = {"annual": "年报（10-K / 20-F）", "10Q": "最新 10-Q", "earnings": "最新财报新闻稿（8-K / 6-K）"}


def live(folder):
    man = json.loads((ROOT / folder / AS_OF / "freshness.json").read_text(encoding="utf-8"))
    return {f["field"]: f for f in man["live_fields"]}


def px(v):
    return f"{v:.2f}"


def main():
    rows = []
    for tk, c in C.items():
        d = ROOT / c["folder"] / AS_OF
        lf = live(c["folder"])
        v = VAL[tk]
        price = lf["price"]["value"]
        hi, lo = lf["52wk_high"]["value"], lf["52wk_low"]["value"]
        shares = lf["shares_out"]["value"]
        mcap = price * shares * 1e6
        off_hi = (1 - price / hi) * 100
        y1 = SNAP[tk]["yahoo"]["close_1y_ago"]
        y1d = SNAP[tk]["yahoo"]["close_1y_ago_date"]
        hp = v["hurdle_prices"]
        sc = v["scenarios"]
        sig = c["signals"]
        sources = SRC[tk]
        price_line = (f"价格 **${px(price)}**（−{off_hi:.1f}% 距 52 周高点 ${hi}；52 周低点 ${lo}）· "
                      f"12 个月：${y1}（{y1d}）→ ${px(price)}（{(price / y1 - 1) * 100:+.1f}%）· 市值 ${mcap / 1e9:,.1f}B")
        head = f"批次 `{BATCH}` · 首次建档 · 价格 = {AS_OF} 收盘（Yahoo = Nasdaq，双源，见 `freshness.json`）· 角色：{c['role']}"

        # ---------------- facts.md (M1)
        f = [f"# {tk} — Facts / M1 证据脊柱（as_of {AS_OF}）", "", head, "",
             "## 0. 行情（LIVE，双源）", price_line, "",
             f"股数口径：{v.get('shares_m'):,.1f}M —— {next(iter([x for x in [__import__('valuation_model').INPUTS[tk]['shares_note']]]))}", "",
             "## 1. 一手数据", "| 项 | 内容 |", "|---|---|"]
        f += [f"| {a} | {b} |" for a, b in c["facts"]]
        f += ["", "## 2. 源登记", "| 类型 | 日期 | URL |", "|---|---|---|"]
        f += [f"| {KIND[s['kind']]} | {s['date']} | {s['url']} |" for s in sources]
        f += ["", "标注：`[S2]` = 二手（新闻 / 数据站汇总，未用一手文件复核）；`[BG]` = 背景（公认史实，本批未逐条找来源）；"
                  "`unsourced_background` = 操作者履历未核实。", "",
              f"**完整度 ~{c['completeness']}%**。M1 信号：**{SIG(sig['M1'])}**", ""]
        (d / "facts.md").write_text("\n".join(f), encoding="utf-8")

        # ---------------- thesis_mechanism.md (M2)
        m = c["m2"]
        t = [f"# {tk} — M2 主题 / 机制", "", "| 项 | 内容 |", "|---|---|",
             f"| Theme | {m['theme']} |", f"| Why now | {m['why_now']} |", f"| 市场叙事 | {m['narrative']} |",
             f"| 市场可能高估的 | {m['over']} |", f"| 市场可能低估的 | {m['under']} |", f"| 稀缺资源 | {m['scarce']} |",
             f"| 利润池 | {m['pool']} |", f"| 迫使市场更新的一个指标 | {m['metric']} |",
             f"| **context_label** | **`{c['context']}`** |", "", f"**M2 信号：{SIG(sig['M2'])}**", ""]
        (d / "thesis_mechanism.md").write_text("\n".join(t), encoding="utf-8")

        # ---------------- profit_pool_durability.md (M3)
        p3 = [f"# {tk} — M3 利润池 / 耐久性 / 操作者", "", c["m3"], "", f"**M3 信号：{SIG(sig['M3'])}**", ""]
        (d / "profit_pool_durability.md").write_text("\n".join(p3), encoding="utf-8")

        # ---------------- financial_reality.md (M4)
        p4 = [f"# {tk} — M4 财务现实", "", "| 检验 | 结果 |", "|---|---|"] + [f"| {a} | {b} |" for a, b in c["m4"]]
        p4 += ["", f"**M4 信号：{SIG(sig['M4'])}**", ""]
        (d / "financial_reality.md").write_text("\n".join(p4), encoding="utf-8")

        # ---------------- inversion_trap_test.md (M5)
        p5 = [f"# {tk} — M5 反演 / 陷阱测试", "", c["m5"], "",
              f"bear 情景 10 年 IRR **{sc['bear']['irr'] * 100:+.1f}%**（bear 情景 8% 门槛价 ${hp['8pct_on_bear']:,.2f}）。", "",
              "| Kill criteria |", "|---|"] + [f"| {k} |" for k in c["kills"]]
        p5 += ["", f"**M5 信号：{SIG(sig['M5'])}**", ""]
        (d / "inversion_trap_test.md").write_text("\n".join(p5), encoding="utf-8")

        # ---------------- valuation.md (M6)
        p6 = [f"# {tk} — 估值（M6）· as_of {AS_OF}", "", price_line, "",
              f"模型：`companies/_trading_rails_2026-10-06/valuation_model.py`（与佩洛西 / 石油 / 电力批次同一公式）。", "",
              "## 1. OE₀ 推导", c["oe_note"], "",
              "## 2. 三情景（10 年；p = 每年派发比例）",
              "| 情景 | 第 1 年 OE | 第 10 年 OE | 增长 | 退出 | p | **IRR** |", "|---|---:|---:|---|---:|---:|---:|"]
        for name in ("bear", "base", "bull"):
            s = sc[name]
            g = f"{s['g'] * 100:+.1f}%" if s["mode"] == "oe" else f"ramp {((s['oe_10'] / s['oe_1']) ** (1 / 9) - 1) * 100:+.0f}%/年"
            p6.append(f"| {name} | ${s['oe_1']:,.2f}B | ${s['oe_10']:,.2f}B | {g} | {s['exit']}x | {s['p'] * 100:.0f}% | **{s['irr'] * 100:+.1f}%** |")
        ig = v.get("implied_g_for_8pct")
        p6 += ["", "## 3. 门槛价", "| | 值 |", "|---|---:|",
               f"| **8% 门槛价（buy_below）** | **${hp['8pct']:,.2f}**（{(hp['8pct'] / price - 1) * 100:+.1f}% 相对现价） |",
               f"| 10% / 12% | ${hp['10pct']:,.2f} / ${hp['12pct']:,.2f} |",
               f"| bull / bear 情景的 8% 门槛价 | ${hp['8pct_on_bull']:,.2f} / ${hp['8pct_on_bear']:,.2f} |",
               (f"| **要让现价拿到 8%，需要的 OE 年增速** | **{ig * 100:+.1f}%**（base 假设 "
                + (f"{sc['base']['g'] * 100:+.1f}%" if sc['base']['mode'] == 'oe' else "ramp") + "） |"),
               "", f"## 4. M6 信号：**{SIG(sig['M6'])}**", ""]
        (d / "valuation.md").write_text("\n".join(p6), encoding="utf-8")

        # ---------------- decision_card.json
        verdict = c["verdict"]
        base_irr = sc["base"]["irr"]
        price_pass = base_irr >= 0.08
        card = {
            "ticker": tk, "name": v["name"], "as_of": AS_OF, "pipeline_version": "lean-6module-v1.1", "weights_version": "none",
            "run_date": RUN_DATE, "batch": BATCH, "run_type": "first_dossier", "refresh_of": None, "status": "DECISION_DRAFT",
            "clean": False, "clean_blocked_reason": "Checker != Runner (PROTOCOL §3) not met: single agent, self-checked only",
            "price_sources": ["yahoo_chart_api", "nasdaq_historical_api"], "price_date": AS_OF,
            "valuation_method": "batch valuation_model.py (same formula as Pelosi / oil / power batches); OE0 = normalized after-tax "
                                "earnings (brokers/exchanges: OCF distorted by client funds); cycle-normalized below TTM where TTM is at a volume/rate peak",
            "currency": "USD", "as_of_price": price, "as_of_market_cap": round(mcap), "shares_out_m": shares,
            "wk52_high": hi, "wk52_low": lo, "role_in_value_chain": c["role"],
            "context_label": c["context"], "business_verdict": c["business"],
            "new_money_verdict": verdict, "runner_proposed_verdict": verdict, "runner_proposed_size_pct": 0,
            "existing_position_verdict": "N/A (not held)", "suggested_initial_size_pct": 0,
            "suggested_max_size_pct": c["max_size"], "module_signals": sig,
            "binding_constraint": c["binding"], "completeness_pct": c["completeness"],
            "price_passes_8pct_base": price_pass,
            "verdict_cap_note": ("completeness < 40% -> INFO-GAP" if c["completeness"] < 40 else
                                 "completeness 40-60% -> verdict capped at WATCH (PIPELINE.md); price " +
                                 ("passes 8% base: follow-up to >=60% + independent Checker could unlock STARTER" if price_pass
                                  else "does NOT pass 8% base: price binds before completeness")),
            "kill_criteria": c["kills"], "next_monitor_event": c["next"],
            "buy_below_price": hp["8pct"], "hurdle_prices": hp,
            "zones": {"starter": f"<= {hp['8pct']} (base >= 8%)", "add": f"<= {hp['10pct']} (base >= 10%)",
                      "no_chase": f"> {hp['8pct']}", "avoid": f"> {hp['8pct_on_bull']}"},
            "implied_g_for_8pct": ig, "scenarios_10y": sc, "factor_check": c["factor"],
            "related_studies": ["studies/铲子百年实证_2026-09-23", "studies/卖铲子的人_历史上的NVIDIA舆论周期_2026-10-06"],
            "sources_used": [{"source_id": f"{tk}-{s['kind']}", "public_date": s["date"], "url": s["url"]} for s in sources],
        }
        (d / "decision_card.json").write_text(json.dumps(card, indent=1, ensure_ascii=False), encoding="utf-8")

        # ---------------- decision_card.md
        cap = card["verdict_cap_note"]
        dm = [f"# {tk} Decision Card — as_of {AS_OF}", "",
              f"`lean-6module-v1.1` · weights `none` · 批次 `{BATCH}` · 首次建档 · **`DECISION_DRAFT`** · 完整度 **~{c['completeness']}%** · ⚠️ `clean=false`（self-checked）",
              f"**context_label** `{c['context']}` · 价值链角色：{c['role']}", "",
              "| 字段 | 值 |", "|---|---|",
              f"| 价格 | **${px(price)}**（−{off_hi:.1f}% 距 52 周高点；12 个月 {(price / y1 - 1) * 100:+.1f}%）· 市值 ${mcap / 1e9:,.1f}B |",
              f"| business_verdict | **{c['business']}** |",
              f"| **new_money_verdict** | **{verdict} 0%** |",
              "| existing_position_verdict | N/A（未持有） |",
              f"| suggested max size | {c['max_size']}% |",
              f"| base 10 年 IRR | **{base_irr * 100:+.1f}%**（bear {sc['bear']['irr'] * 100:+.1f}% / bull {sc['bull']['irr'] * 100:+.1f}%） |",
              f"| **buy_below（base 8%）** | **${hp['8pct']:,.2f}**（{(hp['8pct'] / price - 1) * 100:+.1f}%） |",
              f"| Add 区 | ≤ ${hp['10pct']:,.2f} |",
              f"| No-chase / Avoid | > ${hp['8pct']:,.2f} / > ${hp['8pct_on_bull']:,.2f} |",
              f"| 8% 所需 OE 年增速 | {ig * 100:+.1f}% |",
              f"| **binding_constraint** | **{c['binding']}** |",
              f"| 评级上限 | {cap} |", "",
              "| M1 | M2 | M3 | M4 | M5 | M6 |", "|:--:|:--:|:--:|:--:|:--:|:--:|",
              "| " + " | ".join(SIG(sig[k]) for k in ("M1", "M2", "M3", "M4", "M5", "M6")) + " |", "",
              f"一句话：**{c['one_liner']}**", "",
              "## Kill criteria"] + [f"- {k}" for k in c["kills"]] + [
              "", "## 下次回评", f"- {c['next']}", "", "## 组合层", f"- {c['factor']}", ""]
        (d / "decision_card.md").write_text("\n".join(dm), encoding="utf-8")
        rows.append((tk, price, base_irr, hp["8pct"], ig, verdict, c["completeness"], price_pass))
        print(f"{tk:5} {px(price):>8} base {base_irr * 100:+5.1f}% bb {hp['8pct']:>8.2f} need {ig * 100:+5.1f}% "
              f"{verdict:8} {c['completeness']}% {'PRICE-PASS' if price_pass else ''}")
    (HERE / "data" / f"card_summary_{AS_OF}.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
