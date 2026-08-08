#!/usr/bin/env python
"""Gold relative-return test against SPY and QQQ.

Uses month-end prices so each observation means the same thing: buy gold, SPY,
and QQQ at the end of a month and compare the result 12 or 36 calendar months
later.  SPY/QQQ use Yahoo adjusted closes (splits + cash distributions); gold
uses the LBMA PM fixing and has no yield.  The script reads the already archived
raw inputs from the two preceding backtests and writes portable result tables in
this folder.

The `z_full_money` measure is deliberately labelled *descriptive*: it is the
full-sample gold-vs-M2 regression residual and therefore knows the future.  The
primary `z_roll10_money` counterpart is a strict 120-month rolling,
information-available-at-the-time version. Old gold regimes are deliberately
discarded rather than allowed to influence today's slope.
"""
from __future__ import annotations

import csv
import json
import math
import statistics
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The two input backtests live alongside this result folder.
ROOT = HERE.parent
GOLD_DIR = next(ROOT.glob("黄金_货币供应_估值_*"))
ETF_DIR = next(ROOT.glob("SPY_QQQ_*"))


def month_of(day: str) -> str:
    return day[:7]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def end_of_month_adjusted(path: Path) -> dict[str, tuple[date, float]]:
    """Last trading-day adjusted close in each calendar month."""
    out: dict[str, tuple[date, float]] = {}
    for row in read_csv(path):
        d = date.fromisoformat(row["Date"])
        out[f"{d:%Y-%m}"] = (d, float(row["AdjClose"]))
    return out


def shift_month(month: str, amount: int) -> str:
    y, m = map(int, month.split("-"))
    n = y * 12 + (m - 1) + amount
    return f"{n // 12:04d}-{n % 12 + 1:02d}"


def f(value: str) -> float | None:
    return float(value) if value not in ("", None) else None


def pct(value: float | None, digits: int = 1) -> str:
    return "" if value is None else f"{value:.{digits}%}"


def avg(values: list[float]) -> float | None:
    return statistics.mean(values) if values else None


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def residual_z(months: list[str], gold: dict[str, float], panel: dict[str, dict[str, str]]) -> tuple[dict[str, float], dict[str, float | None], tuple[float, float, float], dict[str, tuple[float, float, float]]]:
    """Fit the money model to month-end gold, including a strict 10-year roll."""
    x = [math.log(float(panel[m]["m2"])) for m in months]
    y = [math.log(gold[m]) for m in months]

    def fit(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
        mean_x, mean_y = statistics.mean(xs), statistics.mean(ys)
        slope = sum((a - mean_x) * (b - mean_y) for a, b in zip(xs, ys)) / sum((a - mean_x) ** 2 for a in xs)
        intercept = mean_y - slope * mean_x
        sigma = math.sqrt(statistics.mean((b - intercept - slope * a) ** 2 for a, b in zip(xs, ys)))
        return intercept, slope, sigma

    intercept, slope, sigma = fit(x, y)
    full = {m: (y[i] - intercept - slope * x[i]) / sigma for i, m in enumerate(months)}
    rolling: dict[str, float | None] = {}
    rolling_params: dict[str, tuple[float, float, float]] = {}
    for i, m in enumerate(months):
        # At time t, fit only t and its preceding 119 months: no old 1970s
        # regime and no later information can influence the reading.
        if i + 1 < 120:
            rolling[m] = None
            continue
        a, b, s = fit(x[i - 119: i + 1], y[i - 119: i + 1])
        rolling[m] = (y[i] - a - b * x[i]) / s
        rolling_params[m] = (a, b, s)
    return full, rolling, (intercept, slope, sigma), rolling_params


@dataclass
class Episode:
    start: str
    end: str
    rows: list[dict]


def winning_episodes(rows: list[dict], horizon: int) -> list[Episode]:
    eligible = [r for r in rows if r["horizon_months"] == horizon and r["beats_both"]]
    episodes: list[Episode] = []
    current: list[dict] = []
    for row in eligible:
        if current and row["month"] != shift_month(current[-1]["month"], 1):
            episodes.append(Episode(current[0]["month"], current[-1]["month"], current))
            current = []
        current.append(row)
    if current:
        episodes.append(Episode(current[0]["month"], current[-1]["month"], current))
    return episodes


def main() -> None:
    panel = {r["month"]: r for r in read_csv(GOLD_DIR / "monthly_panel.csv")}
    spy = end_of_month_adjusted(ETF_DIR / "SPY_daily_adjusted.csv")
    qqq = end_of_month_adjusted(ETF_DIR / "QQQ_daily_adjusted.csv")

    # Monthly LBMA PM price is deliberately the last available fix, matching an
    # ETF's last available trading close rather than the monthly average.
    gold_month_end: dict[str, float] = {}
    gold_daily = read_csv(GOLD_DIR / "data" / "gold_lbma_pm_daily.csv")
    for row in gold_daily:
        gold_month_end[month_of(row["date"])] = float(row["gold_usd_per_oz"])

    model_months = sorted(set(panel) & set(gold_month_end))
    z_full, z_roll10, (intercept, slope, sigma), roll10_params = residual_z(model_months, gold_month_end, panel)
    latest_daily = gold_daily[-1]
    latest_model_month = model_months[-1]
    roll_intercept, roll_slope, roll_sigma = roll10_params[latest_model_month]
    latest_daily_z = (
        math.log(float(latest_daily["gold_usd_per_oz"]))
        - roll_intercept - roll_slope * math.log(float(panel[latest_model_month]["m2"]))
    ) / roll_sigma

    records: list[dict] = []
    for month in sorted(set(panel) & set(gold_month_end) & set(spy) & set(qqq)):
        p = panel[month]
        for horizon in (12, 36):
            end = shift_month(month, horizon)
            if end not in gold_month_end or end not in spy or end not in qqq:
                continue
            gold_multiple = gold_month_end[end] / gold_month_end[month]
            spy_multiple = spy[end][1] / spy[month][1]
            qqq_multiple = qqq[end][1] / qqq[month][1]
            rec = {
                "month": month,
                "end_month": end,
                "horizon_months": horizon,
                "gold_start": gold_month_end[month],
                "gold_end": gold_month_end[end],
                "spy_start": spy[month][1],
                "spy_end": spy[end][1],
                "qqq_start": qqq[month][1],
                "qqq_end": qqq[end][1],
                "gold_total_return": gold_multiple - 1,
                "spy_total_return": spy_multiple - 1,
                "qqq_total_return": qqq_multiple - 1,
                "gold_cagr": gold_multiple ** (12 / horizon) - 1,
                "spy_cagr": spy_multiple ** (12 / horizon) - 1,
                "qqq_cagr": qqq_multiple ** (12 / horizon) - 1,
                "gold_minus_spy_cagr": gold_multiple ** (12 / horizon) - spy_multiple ** (12 / horizon),
                "gold_minus_qqq_cagr": gold_multiple ** (12 / horizon) - qqq_multiple ** (12 / horizon),
                "beats_spy": gold_multiple > spy_multiple,
                "beats_qqq": gold_multiple > qqq_multiple,
                "beats_both": gold_multiple > spy_multiple and gold_multiple > qqq_multiple,
                "z_full_money": z_full[month],
                "z_roll10_money": z_roll10[month],
                "pct_rt_ratio": f(p["pct_rt_ratio"]),
            }
            records.append(rec)

    fields = list(records[0])
    write_csv(HERE / "monthly_relative_returns.csv", records, fields)

    bins = [
        ("<-1σ", lambda x: x < -1),
        ("-1σ to 0σ", lambda x: -1 <= x < 0),
        ("0σ to +1σ", lambda x: 0 <= x < 1),
        ("+1σ to +2σ", lambda x: 1 <= x < 2),
        (">=+2σ", lambda x: x >= 2),
    ]
    summary: list[dict] = []
    for horizon in (12, 36):
        base = [r for r in records if r["horizon_months"] == horizon]
        for z_name in ("z_full_money", "z_roll10_money"):
            for label, contains in bins:
                part = [r for r in base if r[z_name] is not None and contains(r[z_name])]
                summary.append({
                    "horizon_months": horizon,
                    "signal": z_name,
                    "sigma_band": label,
                    "months": len(part),
                    "gold_beats_spy": avg([float(r["beats_spy"]) for r in part]),
                    "gold_beats_qqq": avg([float(r["beats_qqq"]) for r in part]),
                    "gold_beats_both": avg([float(r["beats_both"]) for r in part]),
                    "mean_gold_cagr": avg([r["gold_cagr"] for r in part]),
                    "mean_spy_cagr": avg([r["spy_cagr"] for r in part]),
                    "mean_qqq_cagr": avg([r["qqq_cagr"] for r in part]),
                    "mean_gold_minus_spy_cagr": avg([r["gold_minus_spy_cagr"] for r in part]),
                    "mean_gold_minus_qqq_cagr": avg([r["gold_minus_qqq_cagr"] for r in part]),
                })
    write_csv(HERE / "sigma_band_summary.csv", summary, list(summary[0]))

    episode_rows: list[dict] = []
    for horizon in (12, 36):
        for episode in winning_episodes(records, horizon):
            # Very short runs are kept: excluding them would quietly make the
            # conclusion look more regime-like than the monthly evidence allows.
            episode_rows.append({
                "horizon_months": horizon,
                "buy_month_start": episode.start,
                "buy_month_end": episode.end,
                "consecutive_months": len(episode.rows),
                "median_z_full_money": statistics.median(r["z_full_money"] for r in episode.rows),
                "min_z_full_money": min(r["z_full_money"] for r in episode.rows),
                "max_z_full_money": max(r["z_full_money"] for r in episode.rows),
                "median_z_roll10_money": statistics.median(r["z_roll10_money"] for r in episode.rows if r["z_roll10_money"] is not None),
                "mean_gold_minus_spy_cagr": avg([r["gold_minus_spy_cagr"] for r in episode.rows]),
                "mean_gold_minus_qqq_cagr": avg([r["gold_minus_qqq_cagr"] for r in episode.rows]),
            })
    write_csv(HERE / "gold_wins_both_episodes.csv", episode_rows, list(episode_rows[0]))

    def table(signal: str, horizon: int) -> list[dict]:
        return [r for r in summary if r["signal"] == signal and r["horizon_months"] == horizon]

    lines = [
        "# 黄金相对 SPY / QQQ：1 年、3 年前瞻回测",
        "",
        "更新：2026-08-07。共同样本从 QQQ 上市后的 1999-03 开始。每行都是各月最后一个可用价格买入，并与 12 或 36 个日历月后的最后可用价格比较（ETF 数据最后一月为 2026-07-24）。",
        "",
        "## 口径",
        "",
        "- 黄金：LBMA Gold Price PM 月末最后一个可用定盘价，未计任何持有成本或收益。",
        "- SPY、QQQ：Yahoo Finance 调整后收盘价，包含现金分红与拆股；因此对黄金是更严格的比较。",
        "- `胜出两者` = 同一持有期内，黄金累计回报同时高于 SPY 和 QQQ；采用重叠月度窗口，月数不能当作独立样本数。",
        "- σ = 用月末黄金价格重新拟合的 `ln(金价) ~ ln(M2)` 对数残差。主信号是**严格 10 年滚动 σ**：每个月仅用当月及此前 119 个月估计斜率和 σ；不含未来，也不让更早历史影响读数。全样本 σ 仅作描述性对照。",
        "",
        "## 全样本 σ：黄金胜出概率与平均年化差",
        "",
    ]
    for horizon in (12, 36):
        lines += [f"### 持有 {horizon // 12} 年", "", "| 买入时全样本 σ | 月数 | 胜 SPY | 胜 QQQ | 同时胜两者 | 黄金−SPY 年化 | 黄金−QQQ 年化 |", "|---|---:|---:|---:|---:|---:|---:|"]
        for row in table("z_full_money", horizon):
            lines.append(f"| {row['sigma_band']} | {row['months']} | {pct(row['gold_beats_spy'])} | {pct(row['gold_beats_qqq'])} | {pct(row['gold_beats_both'])} | {pct(row['mean_gold_minus_spy_cagr'])} | {pct(row['mean_gold_minus_qqq_cagr'])} |")
        lines.append("")

    high_comparable = {
        horizon: [r for r in records if r["horizon_months"] == horizon and r["z_roll10_money"] is not None and r["z_roll10_money"] >= latest_daily_z]
        for horizon in (12, 36)
    }
    lines += [
        "## 当前价放进相对回报框架",
        "",
        f"模型最近可配对的月末是 {latest_model_month}：月末金价 ${gold_month_end[latest_model_month]:,.2f}，**10 年滚动读数 {z_roll10[latest_model_month]:+.2f}σ**。用最新 LBMA 定盘 ${float(latest_daily['gold_usd_per_oz']):,.2f}（{latest_daily['date']}）配同一笔 {latest_model_month} M2，读数升至 **{latest_daily_z:+.2f}σ**；这是货币数据滞后下的近似值。",
        "",
        "以这个最新读数作为门槛，在已经走完持有期的历史月里：",
        "",
        "| 持有期 | 10 年滚动 σ ≥ 当前的可比月数 | 黄金同时胜 SPY、QQQ | 说明 |",
        "|---|---:|---:|---|",
    ]
    for horizon, part in high_comparable.items():
        wins = sum(r["beats_both"] for r in part)
        months = ", ".join(r["month"] for r in part)
        lines.append(f"| {horizon // 12} 年 | {len(part)} | {wins}/{len(part)} ({pct(wins / len(part)) if part else ''}) | {months or '无'} |")
    lines += [
        "",
        "这些可比月主要来自 2001–04、2006–08、2020，以及（仅完成 1 年持有期的）2024–25，且同一轮周期内的月份高度重叠。高滚动 σ 在这里代表金价相对近 10 年货币关系的**趋势突破**，不是“绝对高估”；因此它可以是趋势型买入的必要条件，但不能把几十个相邻月当成几十次独立验证。",
        "",
    ]

    lines += ["## 10 年滚动 σ：主信号（无未来函数）", ""]
    for horizon in (12, 36):
        lines += [f"### 持有 {horizon // 12} 年", "", "| 买入时 10 年滚动 σ | 月数 | 胜 SPY | 胜 QQQ | 同时胜两者 | 黄金−SPY 年化 | 黄金−QQQ 年化 |", "|---|---:|---:|---:|---:|---:|---:|"]
        for row in table("z_roll10_money", horizon):
            lines.append(f"| {row['sigma_band']} | {row['months']} | {pct(row['gold_beats_spy'])} | {pct(row['gold_beats_qqq'])} | {pct(row['gold_beats_both'])} | {pct(row['mean_gold_minus_spy_cagr'])} | {pct(row['mean_gold_minus_qqq_cagr'])} |")
        lines.append("")

    lines += ["## 黄金同时跑赢 SPY 与 QQQ 的连续买入期", "", "这不是持有区间，而是连续的**买入月份**：例如 `2007-01 至 2008-08` 在 3 年栏表示该段内每一个月末买入、持有 3 年，黄金都跑赢两只 ETF。", ""]
    for horizon in (12, 36):
        lines += [f"### 持有 {horizon // 12} 年", "", "| 买入月范围 | 连续月数 | 全样本 σ（中位；范围） | 10 年滚动 σ 中位 | 黄金−SPY 年化 | 黄金−QQQ 年化 |", "|---|---:|---:|---:|---:|---:|"]
        for row in [r for r in episode_rows if r["horizon_months"] == horizon]:
            z_range = f"{row['median_z_full_money']:+.2f}σ ({row['min_z_full_money']:+.2f} to {row['max_z_full_money']:+.2f})"
            rt = "" if row["median_z_roll10_money"] is None else f"{row['median_z_roll10_money']:+.2f}σ"
            lines.append(f"| {row['buy_month_start']} 至 {row['buy_month_end']} | {row['consecutive_months']} | {z_range} | {rt} | {pct(row['mean_gold_minus_spy_cagr'])} | {pct(row['mean_gold_minus_qqq_cagr'])} |")
        lines.append("")

    lines += [
        "## 如何使用",
        "",
        "这份表先回答的是相对资产配置问题：历史上在某个 σ 区间买黄金，随后 1 或 3 年是否比两只美股 ETF 更划算。只有先看 `同时胜两者`，再谈绝对的金价高低。",
        "",
        "但别把连续月度窗口当成几十次独立交易；同一次宏观周期会制造很多相邻的、几乎相同的买点。并且，σ 不是触发器：它必须用 10 年滚动栏验证，不能由全样本栏倒推一个当时不可能知道的规则。",
        "",
        "## 文件",
        "",
        "- `monthly_relative_returns.csv`：逐月、逐持有期的完整结果。",
        "- `sigma_band_summary.csv`：全样本/10 年滚动两种 σ 的分组统计。",
        "- `gold_wins_both_episodes.csv`：黄金同时胜过 SPY、QQQ 的所有连续买入月。",
        "- `build_relative_backtest.py`：可重复运行；读取同级已归档的黄金与 SPY/QQQ 原始数据。",
    ]
    (HERE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    snapshot = {
        "as_of": "2026-08-07",
        "common_start": min(r["month"] for r in records),
        "latest_complete_1y_buy_month": max(r["month"] for r in records if r["horizon_months"] == 12),
        "latest_complete_3y_buy_month": max(r["month"] for r in records if r["horizon_months"] == 36),
        "observations": {str(h): sum(r["horizon_months"] == h for r in records) for h in (12, 36)},
        "full_sample_model": {"intercept": intercept, "slope": slope, "sigma": sigma},
        "primary_model": {
            "type": "120-month rolling OLS",
            "window_months": 120,
            "intercept": roll_intercept,
            "slope": roll_slope,
            "sigma": roll_sigma,
        },
        "current_position": {
            "m2_month": latest_model_month,
            "month_end_gold": gold_month_end[latest_model_month],
            "month_end_z_roll10": z_roll10[latest_model_month],
            "latest_gold_date": latest_daily["date"],
            "latest_gold_price": float(latest_daily["gold_usd_per_oz"]),
            "latest_gold_z_with_latest_m2": latest_daily_z,
            "completed_history_at_or_above_latest_z": {
                str(h): {"months": len(part), "gold_beats_both": sum(r["beats_both"] for r in part)}
                for h, part in high_comparable.items()
            },
        },
        "data_sources": {
            "gold": str(GOLD_DIR / "data" / "gold_lbma_pm_daily.csv"),
            "valuation_panel": str(GOLD_DIR / "monthly_panel.csv"),
            "spy_adjusted": str(ETF_DIR / "SPY_daily_adjusted.csv"),
            "qqq_adjusted": str(ETF_DIR / "QQQ_daily_adjusted.csv"),
        },
    }
    (HERE / "analysis_snapshot.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} monthly comparisons.")


if __name__ == "__main__":
    main()
