#!/usr/bin/env python3
"""oil_shocks.py — 历次油价冲击分类表：冲击持续多久、见顶后油价与石油股（相对大盘）怎么走。

数据（均可复核）：
  油价：EIA MER 表 9.1 国内首购价 CODPUUS（1974-01 起月度；1973 用年度值作冲击前价）
        + EIA WTI 现货 RWTC（1986-01 起月度，覆盖同期时优先用 WTI）
  股票：Fama-French 12 行业 "Enrgy" 市值加权月收益 vs 市场（Mkt-RF + RF），CRSP 202607 版
        （复用 studies/电力需求与电力公司盈利_百年实证_2026-09-16/data/ 中已下载的文件）
输出：data/oil_shocks.csv + data/oil_shocks.md
口径：名义油价；超额收益 = (1+能源累计) / (1+市场累计) − 1，按月复利。
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
FFDIR = HERE.parent / "电力需求与电力公司盈利_百年实证_2026-09-16" / "data"

# (名称, 类型, 冲击起始月, 冲击前参照月, 寻找峰/谷的窗口月数)
SHOCKS = [
    ("1973 阿拉伯石油禁运", "供给冲击", "1973-10", "1973", 18),
    ("1979 伊朗革命 + 两伊战争", "供给冲击", "1979-01", "1978-12", 30),
    ("1990 伊拉克入侵科威特", "供给冲击", "1990-08", "1990-07", 6),
    ("2007–08 需求超级周期", "需求驱动", "2007-01", "2006-12", 20),
    ("2022 俄乌战争", "供给冲击", "2022-03", "2022-02", 6),
    ("2026 霍尔木兹断流", "供给冲击", "2026-03", "2026-02", 5),
    ("1986 沙特价格战", "负向（供给放开）", "1986-01", "1985-12", 8),
    ("2014 OPEC 不减产", "负向（供给放开）", "2014-07", "2014-06", 20),
    ("2020 疫情 + 价格战", "负向（需求崩塌）", "2020-02", "2020-01", 4),
]


def ym_add(ym, n):
    y, m = int(ym[:4]), int(ym[5:7])
    t = y * 12 + (m - 1) + n
    return f"{t // 12}-{t % 12 + 1:02d}"


def load_oil():
    oil = {}
    annual = {}
    with (HERE / "data" / "eia_mer_T09.01.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["MSN"] != "CODPUUS" or r["Value"] in ("", "Not Available"):
                continue
            ym = r["YYYYMM"]
            if ym.endswith("13"):
                annual[ym[:4]] = float(r["Value"])
            else:
                oil[f"{ym[:4]}-{ym[4:]}"] = float(r["Value"])
    wti = json.loads((HERE / "data" / "eia_monthly_spot.json").read_text(encoding="utf-8"))["WTI_spot"]
    oil.update(wti)  # 1986 起用 WTI 覆盖首购价
    return oil, annual


def load_ff():
    def section(path, header_key):
        raw = path.read_bytes().decode("utf-8", errors="replace")
        lines = raw.replace(chr(13) + chr(13) + chr(10), chr(10)).replace(chr(13) + chr(10), chr(10)).split(chr(10))  # 原文件为 CR CR LF 换行
        start = next(i for i, l in enumerate(lines) if header_key in l)
        hdr = None
        data = {}
        for l in lines[start + 1:]:
            if l.startswith(","):
                hdr = [h.strip() for h in l.split(",")]
                continue
            if hdr and l.strip() == "" and data:
                break
            parts = [p.strip() for p in l.split(",")]
            if hdr and len(parts) == len(hdr) and parts[0].isdigit() and len(parts[0]) == 6:
                data[f"{parts[0][:4]}-{parts[0][4:]}"] = dict(zip(hdr[1:], map(float, parts[1:])))
        return data
    ind = section(FFDIR / "ff12.csv", "Average Value Weighted Returns -- Monthly")
    fac = section(FFDIR / "ff_factors.csv", "")  # 因子文件第一段即月度
    return ind, fac


def cum(ind, fac, a, b):
    """a 月到 b 月（含两端）的能源、市场累计收益；数据不足返回 None。"""
    e = m = 1.0
    ym = a
    n = 0
    while ym <= b:
        if ym not in ind or ym not in fac:
            return None
        e *= 1 + ind[ym]["Enrgy"] / 100
        m *= 1 + (fac[ym]["Mkt-RF"] + fac[ym]["RF"]) / 100
        ym = ym_add(ym, 1)
        n += 1
    return e - 1, m - 1, e / m - 1, n


def main():
    oil, annual = load_oil()
    ind, fac = load_ff()
    last_ff = max(ind)
    rows = []
    for name, kind, start, pre_ref, win in SHOCKS:
        pre = annual[pre_ref] if len(pre_ref) == 4 else oil[pre_ref]
        window = [ym_add(start, i) for i in range(win + 1) if ym_add(start, i) in oil]
        neg = kind.startswith("负向")
        pk = (min if neg else max)(window, key=lambda k: oil[k])
        r = {"shock": name, "type": kind, "start": start, "pre_price": round(pre, 2), "extreme_month": pk,
             "extreme_price": round(oil[pk], 2), "multiple": round(oil[pk] / pre, 2),
             "months_to_extreme": (int(pk[:4]) * 12 + int(pk[5:7])) - (int(start[:4]) * 12 + int(start[5:7]))}
        for h in (12, 36):
            t = ym_add(pk, h)
            r[f"oil_{h}m_after_vs_extreme"] = round(oil[t] / oil[pk] - 1, 3) if t in oil else None
            c = cum(ind, fac, ym_add(pk, 1), t) if t <= last_ff else None
            r[f"energy_excess_{h}m_after"] = round(c[2], 3) if c else None
        c = cum(ind, fac, start, pk)
        r["energy_excess_start_to_extreme"] = round(c[2], 3) if c else None
        rows.append(r)
    out = HERE / "data" / "oil_shocks.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    pct = lambda v: "—" if v is None else f"{v * 100:+.0f}%"  # noqa: E731
    md = ["| 冲击 | 类型 | 起始 | 冲击前油价 | 极值月 | 极值油价 | 倍数 | 到极值月数 | 极值后12月油价 | 极值后36月油价 | 起始→极值 能源超额 | 极值后12月 能源超额 | 极值后36月 能源超额 |",
          "|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in rows:
        md.append(f"| {r['shock']} | {r['type']} | {r['start']} | ${r['pre_price']} | {r['extreme_month']} | ${r['extreme_price']} | "
                  f"{r['multiple']}x | {r['months_to_extreme']} | {pct(r['oil_12m_after_vs_extreme'])} | {pct(r['oil_36m_after_vs_extreme'])} | "
                  f"{pct(r['energy_excess_start_to_extreme'])} | {pct(r['energy_excess_12m_after'])} | {pct(r['energy_excess_36m_after'])} |")
    md.append("")
    md.append(f"FF12 数据截至 {last_ff}；油价截至 {max(oil)}。名义价格；1986 年前为国内首购价，之后为 WTI 现货。")
    (HERE / "data" / "oil_shocks.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
