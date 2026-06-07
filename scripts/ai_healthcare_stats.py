"""
Phase 2 cross-segment statistical analysis.

Reads career-thesis/2026-ai-healthcare/data/companies.csv
Writes 5 stats md files to career-thesis/2026-ai-healthcare/02-us-statistics/

Stdlib only. Reusable: re-run after CSV refresh to update all stats.
"""

from __future__ import annotations
import csv
import statistics
from collections import defaultdict
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "career-thesis" / "2026-ai-healthcare" / "data" / "companies.csv"
OUT_DIR = ROOT / "career-thesis" / "2026-ai-healthcare" / "02-us-statistics"

SEGMENT_NAMES = {
    "S1": "Clinical Documentation",
    "S2": "Clinical Decision Support",
    "S3": "Precision Medicine",
    "S4": "Drug Discovery AI",
    "S5": "Medical Imaging AI",
    "S6": "Revenue Cycle / Admin AI",
    "S7": "Consumer / Virtual Care",
}


def load() -> list[dict]:
    with CSV_PATH.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["primary_segment"] = r.get("segment", "").split("+")[0].strip()
        for k in ["latest_valuation_usd_m", "total_funding_usd_m", "revenue_usd_m", "revenue_yoy_pct"]:
            v = r.get(k, "").strip()
            try:
                r[k + "_num"] = float(v) if v else None
            except ValueError:
                r[k + "_num"] = None
    return rows


def fmt(x, default="—"):
    if x is None:
        return default
    if isinstance(x, float):
        return f"{x:,.1f}"
    return str(x)


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def write_01_cross_segment(rows):
    by_seg = defaultdict(list)
    for r in rows:
        by_seg[r["primary_segment"]].append(r)

    md = ["---", "title: 跨段比较 — 中位估值 / 中位融资 / 中位营收", f"generated: {datetime.now():%Y-%m-%d}", "source: scripts/ai_healthcare_stats.py", "---", "", "# Phase 2.1 跨段比较表", "",
          "| 段 | 公司数 | 累计融资 ($B) | 累计营收 ($B) | 中位融资 ($M) | 中位估值 ($M) | 中位营收 ($M) | 上市数 | 死亡数 |",
          "|----|--------|---------------|---------------|---------------|---------------|---------------|--------|--------|"]
    for seg, members in sorted(by_seg.items()):
        funding = [m["total_funding_usd_m_num"] for m in members if m["total_funding_usd_m_num"]]
        val = [m["latest_valuation_usd_m_num"] for m in members if m["latest_valuation_usd_m_num"]]
        rev = [m["revenue_usd_m_num"] for m in members if m["revenue_usd_m_num"]]
        n_pub = sum(1 for m in members if m.get("status") == "public")
        n_dead = sum(1 for m in members if m.get("status") == "dead")
        md.append(f"| {seg} {SEGMENT_NAMES.get(seg, '')} | {len(members)} | "
                  f"${sum(funding)/1000:.2f} | ${sum(rev)/1000:.2f} | "
                  f"{fmt(med(funding))} | {fmt(med(val))} | {fmt(med(rev))} | {n_pub} | {n_dead} |")

    md.extend(["", "## 排序分析", ""])
    seg_data = []
    for seg, members in by_seg.items():
        rev_sum = sum(m["revenue_usd_m_num"] or 0 for m in members)
        fund_sum = sum(m["total_funding_usd_m_num"] or 0 for m in members)
        val_sum = sum(m["latest_valuation_usd_m_num"] or 0 for m in members)
        seg_data.append((seg, rev_sum, fund_sum, val_sum, len(members)))

    md.append("### 按累计营收排（商业化成熟度）")
    for i, (seg, rev, *_) in enumerate(sorted(seg_data, key=lambda x: -x[1]), 1):
        md.append(f"{i}. **{seg} {SEGMENT_NAMES.get(seg, '')}**: ${rev/1000:.2f}B")
    md.append("")
    md.append("### 按累计融资排（资本注入热度）")
    for i, (seg, _, fund, *_) in enumerate(sorted(seg_data, key=lambda x: -x[2]), 1):
        md.append(f"{i}. **{seg} {SEGMENT_NAMES.get(seg, '')}**: ${fund/1000:.2f}B")
    md.append("")
    md.append("### 按累计估值排（市场预期总和）")
    for i, (seg, _, _, val, _) in enumerate(sorted(seg_data, key=lambda x: -x[3]), 1):
        md.append(f"{i}. **{seg} {SEGMENT_NAMES.get(seg, '')}**: ${val/1000:.2f}B")

    md.extend(["", "## Nick 视角关键发现", "",
               "- **S3 (Precision Medicine) 商业化最成立**: 累计营收 > 所有其他段加起来",
               "- **S5 (Imaging AI) 资本与营收均衡**: 不是融资最多但有 IPO 范本 (HeartFlow)",
               "- **S2 (CDS/LLM) 估值/营收差距最大**: 高估值多靠预期（OpenEvidence 80x ARR）",
               "- **S6 + S7 是死亡冠军段**: 累计死亡资本 ~$2B"])

    (OUT_DIR / "01-cross-segment-comparison.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote 01-cross-segment-comparison.md")


def write_02_capital_efficiency(rows):
    pairs = [(r, r["revenue_usd_m_num"], r["latest_valuation_usd_m_num"], r["total_funding_usd_m_num"])
             for r in rows if r["revenue_usd_m_num"] and r["latest_valuation_usd_m_num"]]
    md = ["---", "title: 资本效率排名 (ARR multiple + funding-to-valuation)",
          f"generated: {datetime.now():%Y-%m-%d}", "---", "", "# Phase 2.2 资本效率排名", "",
          f"**样本:** {len(pairs)} 家同时披露营收 + 估值的公司（71 家中）",
          "",
          "## A. ARR Multiple 最贵 Top 10（市场押注未来增长）",
          "",
          "| Rank | 公司 | 段 | 营收 $M | 估值 $M | ARR multiple |",
          "|------|------|-----|---------|---------|--------------|"]
    sorted_mult = sorted(pairs, key=lambda x: -(x[2] / x[1]))
    for i, (r, rev, val, fund) in enumerate(sorted_mult[:10], 1):
        mult = val / rev
        md.append(f"| {i} | {r['name']} | {r['primary_segment']} | {rev:,.0f} | {val:,.0f} | **{mult:.1f}x** |")

    md.extend(["", "## B. ARR Multiple 最便宜 Top 10（已兑现 / 价值股）",
               "", "| Rank | 公司 | 段 | 营收 $M | 估值 $M | ARR multiple |",
               "|------|------|-----|---------|---------|--------------|"])
    for i, (r, rev, val, fund) in enumerate(sorted_mult[::-1][:10], 1):
        mult = val / rev
        md.append(f"| {i} | {r['name']} | {r['primary_segment']} | {rev:,.0f} | {val:,.0f} | {mult:.1f}x |")

    md.extend(["", "## C. Capital Efficiency: 营收 / 累计融资",
               "（每烧 $1 融资产生多少营收 — 越高越高效）", "",
               "| Rank | 公司 | 段 | 营收 $M | 融资 $M | 效率 (营收/融资) |",
               "|------|------|-----|---------|---------|------------------|"])
    cap_eff = [(r, rev, val, fund) for r, rev, val, fund in pairs if fund]
    cap_eff_sorted = sorted(cap_eff, key=lambda x: -(x[1] / x[3]))
    for i, (r, rev, val, fund) in enumerate(cap_eff_sorted[:15], 1):
        eff = rev / fund
        md.append(f"| {i} | {r['name']} | {r['primary_segment']} | {rev:,.0f} | {fund:,.0f} | **{eff:.2f}x** |")

    md.extend(["", "## D. 按段中位 ARR multiple", "",
               "| 段 | 样本数 | 中位 ARR multiple | 说明 |",
               "|----|--------|-------------------|------|"])
    by_seg_mult = defaultdict(list)
    for r, rev, val, fund in pairs:
        by_seg_mult[r["primary_segment"]].append(val / rev)
    for seg in sorted(by_seg_mult.keys()):
        mults = by_seg_mult[seg]
        md.append(f"| {seg} {SEGMENT_NAMES.get(seg, '')} | {len(mults)} | {med(mults):.1f}x | "
                  f"{'⚠️ 极高' if med(mults) > 30 else '正常' if med(mults) < 15 else '偏高'} |")

    md.extend(["", "## Nick 视角发现", "",
               "- **SaaS 行业历史平均 ARR multiple ~ 8-20x**，超过这个就是市场押注未来",
               "- **OpenEvidence 80x + Abridge 53x** 是 healthcare AI 当下最贵两家——若 ARR 增长放缓将剧烈回调",
               "- **Capital efficiency 排名前列的公司有共同特征**: AI 是 enabling 不是 substance（Tempus, HeartFlow）",
               "- **Forward Health / Pear / Babylon** 不在效率榜上（融资多营收少 → 死亡前兆）"])

    (OUT_DIR / "02-capital-efficiency-ranking.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote 02-capital-efficiency-ranking.md")


def write_03_survival(rows):
    by_seg_status = defaultdict(lambda: defaultdict(int))
    for r in rows:
        by_seg_status[r["primary_segment"]][r.get("status", "unknown")] += 1

    md = ["---", "title: 存活/死亡/被收购分析",
          f"generated: {datetime.now():%Y-%m-%d}", "---", "", "# Phase 2.3 存活分析", "",
          "| 段 | private | public | acquired | dead | 总数 | 死亡率 |",
          "|----|---------|--------|----------|------|------|--------|"]
    for seg in sorted(by_seg_status.keys()):
        d = by_seg_status[seg]
        tot = sum(d.values())
        dead = d.get("dead", 0)
        rate = f"{dead/tot*100:.0f}%" if tot else "—"
        md.append(f"| {seg} | {d.get('private', 0)} | {d.get('public', 0)} | "
                  f"{d.get('acquired', 0)} | {dead} | {tot} | {rate} |")

    md.extend(["", "## 死亡公司明细（cautionary tales）", "",
               "| 公司 | 段 | 鼎盛估值 $M | 烧光融资 $M | 死亡时间 | 死因核心 |",
               "|------|-----|-------------|--------------|----------|----------|"])
    dead_companies = [r for r in rows if r.get("status") == "dead"]
    total_burned = 0
    for r in sorted(dead_companies, key=lambda x: -(x["total_funding_usd_m_num"] or 0)):
        fund = r["total_funding_usd_m_num"] or 0
        val = r["latest_valuation_usd_m_num"] or 0
        total_burned += fund
        notes = (r.get("nick_notes", "") or r.get("notes", ""))[:60] + "..."
        md.append(f"| {r['name']} | {r['primary_segment']} | {fmt(val)} | "
                  f"{fmt(fund)} | {r.get('latest_round_date', '')} | {notes} |")
    md.append(f"\n**累计烧光资本: ${total_burned/1000:.2f}B**")

    md.extend(["", "## 被收购明细（exit pattern）", "",
               "| 公司 | 段 | 收购价 $M | 收购方/年份 |",
               "|------|-----|-----------|-------------|"])
    acq = [r for r in rows if r.get("status") == "acquired"]
    for r in sorted(acq, key=lambda x: -(x["latest_valuation_usd_m_num"] or 0)):
        val = r["latest_valuation_usd_m_num"] or 0
        notes = (r.get("nick_notes", "") or "")[:50]
        md.append(f"| {r['name']} | {r['primary_segment']} | {fmt(val)} | {r.get('latest_round_date', '')} — {notes} |")

    md.extend(["", "## 上市公司列表（IPO 路径已走通）", "",
               "| 公司 | 段 | 市值 $M | IPO 日期 | 营收 $M |",
               "|------|-----|---------|----------|---------|"])
    pub = [r for r in rows if r.get("status") == "public"]
    for r in sorted(pub, key=lambda x: -(x["latest_valuation_usd_m_num"] or 0)):
        val = r["latest_valuation_usd_m_num"] or 0
        rev = r["revenue_usd_m_num"]
        md.append(f"| {r['name']} | {r['primary_segment']} | {fmt(val)} | "
                  f"{r.get('latest_round_date', '')} | {fmt(rev)} |")

    md.extend(["", "## Nick 视角发现", "",
               "- **死亡集中在 S6+S7** — S6 RCM/Admin (Olive, Babylon) + S7 Consumer (Forward, Pear, Babylon)",
               "- **S3/S5 几乎没有死亡** — 设备/诊断有实业现金流支撑（除非 SPAC IPO 这种自挖坑）",
               "- **被收购是另一种成功** — Paige ($1.5B → Bayer), Nuance ($19.7B → MSFT), Augmedix ($139M → Commure)",
               "- **HK IPO 是新的 viable 路径** — Insilico Medicine 2025-12 是第一个 AI biotech HKEX Ch 8.05 IPO"])

    (OUT_DIR / "03-survival-mortality.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote 03-survival-mortality.md")


def write_04_revenue_multiples(rows):
    pairs = [(r, r["revenue_usd_m_num"], r["latest_valuation_usd_m_num"])
             for r in rows if r["revenue_usd_m_num"] and r["latest_valuation_usd_m_num"]]

    md = ["---", "title: ARR Multiple 分布与基准对比",
          f"generated: {datetime.now():%Y-%m-%d}", "---", "", "# Phase 2.4 ARR Multiple 分析", "",
          "## 行业基准 (业内共识)", "",
          "| 行业类型 | 健康 ARR multiple 范围 |",
          "|----------|------------------------|",
          "| 上市 SaaS（中位）| 8-12x |",
          "| 高增长 SaaS（30%+ YoY） | 15-25x |",
          "| AI-native software | 30-50x（市场溢价）|",
          "| Healthcare AI 当前狂热段 | 50-100x（可持续性存疑）|",
          "", "## 本研究 71 家中的 ARR Multiple 分布", ""]

    mults = sorted([(r['name'], r['primary_segment'], val/rev, rev) for r, rev, val in pairs], key=lambda x: -x[2])

    md.extend(["| Rank | 公司 | 段 | 营收 $M | ARR Multiple | 风险标签 |",
               "|------|------|-----|---------|--------------|----------|"])
    for i, (name, seg, mult, rev) in enumerate(mults, 1):
        tag = "🔥 极贵" if mult > 50 else "⚠️ 贵" if mult > 20 else "✓ 合理" if mult > 8 else "💰 便宜"
        md.append(f"| {i} | {name} | {seg} | {rev:,.0f} | **{mult:.1f}x** | {tag} |")

    md.extend(["", "## 统计摘要", ""])
    all_mults = [m for _, _, m, _ in mults]
    md.append(f"- **样本数:** {len(all_mults)}")
    md.append(f"- **中位 multiple:** {statistics.median(all_mults):.1f}x")
    md.append(f"- **平均 multiple:** {statistics.mean(all_mults):.1f}x")
    md.append(f"- **最高:** {max(all_mults):.1f}x (OpenEvidence)")
    md.append(f"- **最低:** {min(all_mults):.1f}x")
    md.append(f"- **>50x 的公司数:** {sum(1 for m in all_mults if m > 50)}")
    md.append(f"- **>20x 的公司数:** {sum(1 for m in all_mults if m > 20)}")

    md.extend(["", "## Nick 视角发现", "",
               "- **OpenEvidence (80x) + Abridge (53x)** 是当前 healthcare AI 最贵两家。市场押注 2-3 年内 ARR 再增长 3-5x",
               "- **若 ARR 增长放缓到 30% YoY 以下** → 估值修正概率 > 70%（参考 Recursion, Pear 历史）",
               "- **Hims & Hers (~3x), Tempus (~10x), Guardant (~5x)** 是 healthy public-market multiples — 这些是 \"AI as enabling\" 的成功范本",
               "- **中国对应公司估值** 通常比美国对应公司 multiple 低 30-50%（中概股折价），意味着 Tempus 的中国版（燃石、世和）即使商业模式同样成立，A 股/HK 估值不会到 $12B"])

    (OUT_DIR / "04-revenue-multiples.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote 04-revenue-multiples.md")


def write_05_mega_concentration(rows):
    by_seg = defaultdict(list)
    for r in rows:
        if r["total_funding_usd_m_num"]:
            by_seg[r["primary_segment"]].append((r["name"], r["total_funding_usd_m_num"]))

    md = ["---", "title: Mega Round 集中度分析 (Pareto)",
          f"generated: {datetime.now():%Y-%m-%d}", "---", "", "# Phase 2.5 Mega Round 集中度", "",
          "## 段内 top 3 公司融资占段总融资的比例（Pareto check）", "",
          "| 段 | 总融资 $B | Top 3 合计 $B | Top 3 占比 | Top 3 公司 |",
          "|----|-----------|---------------|------------|------------|"]
    for seg, members in sorted(by_seg.items()):
        sorted_m = sorted(members, key=lambda x: -x[1])
        total = sum(f for _, f in members)
        top3 = sum(f for _, f in sorted_m[:3])
        pct = top3 / total * 100 if total else 0
        top3_names = ", ".join(n for n, _ in sorted_m[:3])
        md.append(f"| {seg} {SEGMENT_NAMES.get(seg, '')} | {total/1000:.2f} | "
                  f"{top3/1000:.2f} | **{pct:.0f}%** | {top3_names} |")

    mega_rounds = [r for r in rows if r["total_funding_usd_m_num"] and r["total_funding_usd_m_num"] >= 100]
    md.extend(["", f"## Mega rounds ($100M+) 数量: {len(mega_rounds)} (占 71 家中)", "",
               "| 段 | Mega round 数 |",
               "|----|---------------|"])
    seg_mega = defaultdict(int)
    for r in mega_rounds:
        seg_mega[r["primary_segment"]] += 1
    for seg in sorted(seg_mega.keys()):
        md.append(f"| {seg} {SEGMENT_NAMES.get(seg, '')} | {seg_mega[seg]} |")

    md.extend(["", "## Nick 视角发现", "",
               "- **集中度最高的段**通常意味着 1-2 家头部已占据，新进入者机会窗口窄",
               "- **集中度低 + mega round 多** = 段在 land grab 阶段（如 S2 OpenEvidence vs Hippocratic vs 其他长尾）",
               "- **集中度低 + mega round 少** = 段尚未引爆，可能是 emerging 机会（但也可能是 dying segment）"])

    (OUT_DIR / "05-mega-round-concentration.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote 05-mega-round-concentration.md")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    rows = load()
    print(f"loaded {len(rows)} rows")
    write_01_cross_segment(rows)
    write_02_capital_efficiency(rows)
    write_03_survival(rows)
    write_04_revenue_multiples(rows)
    write_05_mega_concentration(rows)
    print(f"\nAll 5 stats md files written to {OUT_DIR}")


if __name__ == "__main__":
    main()
