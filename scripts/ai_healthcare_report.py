"""
Generate Phase 1 HTML report for AI Healthcare research.

Reads career-thesis/2026-ai-healthcare/data/companies.csv
Writes career-thesis/2026-ai-healthcare/REPORT-phase1.html

Self-contained HTML with:
- Inline SVG structural diagram of 7 segments
- Chart.js charts (CDN) with inline JSON data
- Findings + Nick career takeaways
- No Python deps beyond stdlib

Reusable: re-run after CSV updates to refresh the report.
"""

from __future__ import annotations

import csv
import json
import html
from collections import defaultdict
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "career-thesis" / "2026-ai-healthcare" / "data" / "companies.csv"
OUT_PATH = ROOT / "career-thesis" / "2026-ai-healthcare" / "REPORT-phase1.html"

SEGMENT_NAMES = {
    "S1": "Clinical Documentation / AI Scribe",
    "S2": "Clinical Decision Support / Medical LLM",
    "S3": "Precision Medicine / Diagnostics",
    "S4": "Drug Discovery AI",
    "S5": "Medical Imaging AI",
    "S6": "Revenue Cycle / Admin AI",
    "S7": "Consumer / Virtual Care AI",
}

# 中英对照术语表 — 用于 abbr tooltip + glossary card
GLOSSARY = [
    # 投融资 / Business
    ("ARR", "Annual Recurring Revenue", "年度经常性收入 — SaaS 公司的核心营收指标，按订阅模式年化"),
    ("ARR multiple", "Valuation / ARR", "营收倍数 — 估值除以 ARR，SaaS 行业一般 8-20x，AI 公司常 50-100x"),
    ("YoY", "Year over Year", "同比增长率（与去年同期相比）"),
    ("TAM", "Total Addressable Market", "可触达市场总规模"),
    ("Series A/B/C/D/E", "Funding rounds", "天使后的融资轮次，字母越靠后规模越大、估值越高"),
    ("SPAC IPO", "Special Purpose Acquisition Company IPO", "借壳上市（绕过传统 IPO 审查的捷径，2021-2023 大量医疗 startup 死于此路径）"),
    ("post-money valuation", "Post-money valuation", "投后估值（融资后的公司估值）"),
    ("moat", "Economic moat", "护城河 — 巴菲特术语，指公司的可持续竞争优势"),
    ("D2C", "Direct-to-Consumer", "直接面向消费者（不通过医院/保险中介）"),
    ("payer", "Payer", "付费方 — 美国医疗有 4 类：保险公司、医院、患者自付、药企"),
    ("payer ops", "Payer Operations", "保险公司内部运营"),
    ("RWE", "Real-World Evidence", "真实世界证据（不是 RCT 而是来自真实临床数据）"),
    ("pipeline", "Drug pipeline", "药物管线（biotech 公司开发中的药品组合）"),
    ("runway", "Cash runway", "现金跑道 — 按当前 burn rate 还能撑多久"),
    ("OEM", "Original Equipment Manufacturer", "原始设备制造商 — 嵌入到大厂设备里卖（如 Lunit 给 GE/Philips 提供 AI 算法）"),
    # 法规 / Regulatory
    ("FDA", "Food and Drug Administration", "美国食品药品监督管理局"),
    ("NMPA", "National Medical Products Administration", "中国国家药品监督管理局（前 CFDA）"),
    ("510(k)", "FDA 510(k) clearance", "美国 FDA 简化审批路径（证明与已批设备等效）"),
    ("De Novo", "FDA De Novo pathway", "FDA 新批准路径（用于无 predicate 的全新设备）"),
    ("PMA", "Premarket Approval", "FDA 上市前批准（最严格的设备审批）"),
    ("Breakthrough Designation", "FDA Breakthrough Designation", "FDA 突破性认定（加速审批）"),
    ("CE mark", "Conformité Européenne", "欧盟合规认证（医疗设备进入欧盟必需）"),
    ("CPT code", "Current Procedural Terminology code", "美国医疗保险报销编码 — 拿到 CPT 等于走通报销链"),
    ("reimbursement", "Insurance reimbursement", "保险报销（医疗商业化的关键卡口）"),
    ("HIPAA", "Health Insurance Portability and Accountability Act", "美国医疗数据隐私法（限制患者数据使用）"),
    ("IRB", "Institutional Review Board", "临床研究伦理审查"),
    # 系统 / Tech
    ("EHR", "Electronic Health Records", "电子病历系统（美国主要厂商 Epic 和 Cerner）"),
    ("EMR", "Electronic Medical Records", "同 EHR，同义词"),
    ("PACS", "Picture Archiving and Communication System", "影像归档与通信系统（医院存储影像的基础设施）"),
    ("RIS", "Radiology Information System", "放射科信息系统"),
    ("LLM", "Large Language Model", "大语言模型（如 GPT、Claude、文心、通义）"),
    ("foundation model", "Foundation Model", "基础模型 — 在大规模数据上预训练的通用 AI 模型"),
    ("NLP", "Natural Language Processing", "自然语言处理"),
    # 医学专业 / Clinical
    ("scribe", "Medical scribe", "医疗记录员 — 历史上是人，现在 AI 替代（自动转录医患对话生成病历）"),
    ("ambient scribe", "Ambient AI scribe", "环境 AI 记录 — 后台自动监听 + 生成病历，医生不需手动操作"),
    ("clinical documentation", "Clinical documentation", "临床文书（病历、就诊记录、出院总结等）"),
    ("CDS", "Clinical Decision Support", "临床决策支持（AI 帮医生诊断、用药）"),
    ("triage", "Triage", "分诊 — 决定患者优先级和路径"),
    ("RCM", "Revenue Cycle Management", "收入循环管理 — 医院从挂号到收款的全流程财务管理"),
    ("prior auth", "Prior Authorization", "事前授权 — 保险公司在治疗前批准（美国最大的 admin bottleneck）"),
    ("denials", "Insurance claim denials", "保险理赔拒付"),
    ("MCED", "Multi-Cancer Early Detection", "多癌种早期筛查（一次抽血查多种癌症）"),
    ("ctDNA", "circulating tumor DNA", "循环肿瘤 DNA — 血液中游离的肿瘤 DNA 片段，用于液体活检"),
    ("CGP", "Comprehensive Genomic Profiling", "全面基因组分析 — 一次性检测肿瘤中数百个基因突变"),
    ("liquid biopsy", "Liquid biopsy", "液体活检 — 用血液代替组织活检"),
    ("NGS", "Next-Generation Sequencing", "下一代测序技术（高通量 DNA 测序）"),
    ("Galleri", "GRAIL Galleri test", "GRAIL 的多癌早筛产品名"),
    ("Shield", "Guardant Shield test", "Guardant 的多癌早筛产品名"),
    ("oncology", "Oncology", "肿瘤学（癌症治疗）"),
    ("pathology", "Pathology", "病理学（组织切片诊断）"),
    ("radiology", "Radiology", "放射学（影像诊断）"),
    ("CT/CTA", "Computed Tomography Angiography", "CT 血管造影"),
    ("CT-FFR", "CT Fractional Flow Reserve", "CT 血流储备分数 — HeartFlow 的核心产品，无创评估冠脉狭窄"),
    ("echocardiography", "Echocardiography", "超声心动图（心脏超声）"),
    ("LVO", "Large Vessel Occlusion", "大血管闭塞（中风急诊关键病种）"),
    ("PE", "Pulmonary Embolism", "肺栓塞"),
    ("PA imaging", "Photoacoustic Imaging", "光声成像（Nick 的 PhD 方向 — 用激光+超声同时获得功能和结构）"),
    ("DL", "Deep Learning", "深度学习"),
    ("ML", "Machine Learning", "机器学习"),
    ("digital therapeutics / DTx", "Digital Therapeutics", "数字疗法 — FDA 批准的处方 app（如 Pear 的 reSET），多数商业化失败"),
    ("telehealth", "Telehealth", "远程医疗"),
    ("primary care", "Primary care", "初级医疗（家庭医生层级，对应中国基层医疗）"),
    ("GLP-1", "Glucagon-Like Peptide-1 agonist", "GLP-1 受体激动剂 — 即 Ozempic / Wegovy / Mounjaro 类减肥药"),
    ("GP at Hand", "GP at Hand", "Babylon Health 的英国 NHS 远程医疗产品"),
    # 中国相关
    ("HK Ch 8.05", "HKEX Chapter 8.05 listing rule", "港交所 8.05 上市规则（专为未盈利生物科技公司设的通道）"),
    ("中概股", "US-listed Chinese stocks", "在美上市的中国公司股票"),
    ("分级诊疗", "Tiered diagnosis & treatment", "中国医改政策 — 把患者按病情严重程度分配到不同层级医院"),
    ("医保局", "National Healthcare Security Administration", "国家医疗保障局（中国唯一的全民支付方）"),
]

SEGMENT_COLORS = {
    "S1": "#3b82f6",  # blue
    "S2": "#a855f7",  # purple
    "S3": "#10b981",  # green
    "S4": "#f59e0b",  # amber
    "S5": "#ef4444",  # red (Nick's focus)
    "S6": "#6b7280",  # gray
    "S7": "#ec4899",  # pink
}


def load_companies() -> list[dict]:
    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for r in reader:
            # primary segment for grouping (companies that straddle: take first)
            primary = r.get("segment", "").split("+")[0].strip()
            r["primary_segment"] = primary
            # numeric coercion
            for k in ["latest_valuation_usd_m", "total_funding_usd_m", "revenue_usd_m", "revenue_yoy_pct"]:
                v = r.get(k, "").strip()
                try:
                    r[k + "_num"] = float(v) if v else None
                except ValueError:
                    r[k + "_num"] = None
            rows.append(r)
        return rows


def aggregate(rows: list[dict]) -> dict:
    by_seg = defaultdict(list)
    for r in rows:
        by_seg[r["primary_segment"]].append(r)

    by_country = defaultdict(int)
    by_status = defaultdict(int)
    by_seg_status = defaultdict(lambda: defaultdict(int))

    for r in rows:
        by_country[r.get("hq_country", "Other")] += 1
        by_status[r.get("status", "unknown")] += 1
        by_seg_status[r["primary_segment"]][r.get("status", "unknown")] += 1

    seg_summary = []
    for seg, members in sorted(by_seg.items()):
        funding_total = sum(m["total_funding_usd_m_num"] or 0 for m in members)
        revenue_total = sum(m["revenue_usd_m_num"] or 0 for m in members)
        val_total = sum(m["latest_valuation_usd_m_num"] or 0 for m in members)
        n_with_revenue = sum(1 for m in members if m["revenue_usd_m_num"])
        n_dead = sum(1 for m in members if m.get("status") == "dead")
        n_public = sum(1 for m in members if m.get("status") == "public")
        n_acquired = sum(1 for m in members if m.get("status") == "acquired")
        seg_summary.append({
            "code": seg,
            "name": SEGMENT_NAMES.get(seg, seg),
            "color": SEGMENT_COLORS.get(seg, "#888"),
            "n_companies": len(members),
            "total_funding_b": round(funding_total / 1000, 2),
            "total_revenue_b": round(revenue_total / 1000, 2),
            "total_valuation_b": round(val_total / 1000, 2),
            "n_with_revenue": n_with_revenue,
            "n_dead": n_dead,
            "n_public": n_public,
            "n_acquired": n_acquired,
        })

    # Top 20 by valuation
    top_val = sorted(
        [r for r in rows if r["latest_valuation_usd_m_num"]],
        key=lambda r: r["latest_valuation_usd_m_num"],
        reverse=True,
    )[:20]

    # Top 15 by revenue
    top_rev = sorted(
        [r for r in rows if r["revenue_usd_m_num"]],
        key=lambda r: r["revenue_usd_m_num"],
        reverse=True,
    )[:15]

    # Capital efficiency: revenue / funding (where both exist)
    cap_eff = []
    for r in rows:
        rev = r["revenue_usd_m_num"]
        fund = r["total_funding_usd_m_num"]
        val = r["latest_valuation_usd_m_num"]
        if rev and val:
            cap_eff.append({
                "name": r["name"],
                "segment": r["primary_segment"],
                "valuation": val,
                "revenue": rev,
                "funding": fund,
                "rev_multiple": round(val / rev, 1) if rev else None,
                "color": SEGMENT_COLORS.get(r["primary_segment"], "#888"),
            })

    return {
        "n_total": len(rows),
        "by_country": dict(by_country),
        "by_status": dict(by_status),
        "by_seg_status": {k: dict(v) for k, v in by_seg_status.items()},
        "seg_summary": seg_summary,
        "top_val": [
            {
                "name": r["name"],
                "valuation_b": round(r["latest_valuation_usd_m_num"] / 1000, 2),
                "segment": r["primary_segment"],
                "color": SEGMENT_COLORS.get(r["primary_segment"], "#888"),
                "status": r.get("status", ""),
                "country": r.get("hq_country", ""),
            }
            for r in top_val
        ],
        "top_rev": [
            {
                "name": r["name"],
                "revenue_m": r["revenue_usd_m_num"],
                "segment": r["primary_segment"],
                "color": SEGMENT_COLORS.get(r["primary_segment"], "#888"),
                "yoy": r.get("revenue_yoy_pct_num"),
            }
            for r in top_rev
        ],
        "cap_eff": cap_eff,
    }


def build_glossary_html() -> str:
    """生成中英对照术语表 card（折叠式 details/summary）"""
    rows = []
    for short, en, zh in GLOSSARY:
        rows.append(
            f'<tr><td><strong>{html.escape(short)}</strong></td>'
            f'<td>{html.escape(en)}</td>'
            f'<td>{html.escape(zh)}</td></tr>'
        )
    return f'''
    <details class="card" open style="margin-bottom:20px;">
      <summary style="cursor:pointer;font-size:22px;font-weight:bold;padding:8px 0;list-style:none;">
        📖 中英对照术语表 (Glossary) — 点击展开/折叠
      </summary>
      <p style="color:#6b7280;font-size:13px;margin:12px 0;">报告里所有专业术语都加了 <code>&lt;abbr&gt;</code> tooltip，鼠标 hover 会显示中文解释。下面是完整术语表，按"投融资 → 法规 → 系统 → 临床 → 中国相关"分组。</p>
      <table style="font-size:13px;">
        <thead>
          <tr><th style="width:18%;">缩写/术语</th><th style="width:32%;">English Full Form</th><th>中文解释</th></tr>
        </thead>
        <tbody>
          {"".join(rows)}
        </tbody>
      </table>
    </details>
    '''


def build_svg_structural_diagram(seg_summary: list[dict]) -> str:
    """7 segment cards in a 2x4 grid + central Nick label + connecting lines."""
    width, height = 1000, 600
    # Layout: 7 segments around the perimeter, Nick in center
    import math
    cx, cy = width / 2, height / 2
    radius_x, radius_y = 380, 220
    n = len(seg_summary)
    positions = []
    for i, seg in enumerate(seg_summary):
        angle = -math.pi / 2 + 2 * math.pi * i / n
        x = cx + radius_x * math.cos(angle)
        y = cy + radius_y * math.sin(angle)
        positions.append((x, y, seg))

    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:1000px;height:auto;font-family:system-ui,sans-serif;">']
    # Title
    parts.append(f'<text x="{cx}" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#1f2937">7 个 AI 医疗子赛道 × Nick profile match</text>')

    # Connecting lines (center → each segment)
    for x, y, seg in positions:
        # Highlight S3 and S5 with strong lines (Nick's main candidates)
        is_main = seg["code"] in ("S3", "S5")
        stroke_color = seg["color"] if is_main else "#d1d5db"
        stroke_width = 3 if is_main else 1
        dash = "" if is_main else 'stroke-dasharray="4 4"'
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{stroke_color}" stroke-width="{stroke_width}" {dash} />')

    # Central node: Nick
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="55" fill="#1f2937" />')
    parts.append(f'<text x="{cx}" y="{cy - 5}" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Nick</text>')
    parts.append(f'<text x="{cx}" y="{cy + 15}" text-anchor="middle" fill="#9ca3af" font-size="11">PA imaging PhD</text>')
    parts.append(f'<text x="{cx}" y="{cy + 30}" text-anchor="middle" fill="#9ca3af" font-size="11">+ DL + 出海叙事</text>')

    # Segment cards
    for x, y, seg in positions:
        is_main = seg["code"] in ("S3", "S5")
        card_w, card_h = 200, 100
        rx = x - card_w / 2
        ry = y - card_h / 2
        bg = seg["color"] if is_main else "#f3f4f6"
        text_color = "white" if is_main else "#1f2937"
        subtext_color = "rgba(255,255,255,0.85)" if is_main else "#6b7280"
        stroke_color = seg["color"]
        stroke_w = 3 if is_main else 2
        parts.append(f'<rect x="{rx}" y="{ry}" width="{card_w}" height="{card_h}" rx="10" fill="{bg}" stroke="{stroke_color}" stroke-width="{stroke_w}" />')
        # Title with code badge
        parts.append(f'<text x="{x}" y="{ry + 22}" text-anchor="middle" fill="{text_color}" font-size="14" font-weight="bold">{seg["code"]}</text>')
        # Name (truncated)
        name = seg["name"]
        if len(name) > 28:
            name = name[:26] + "..."
        parts.append(f'<text x="{x}" y="{ry + 42}" text-anchor="middle" fill="{text_color}" font-size="11">{html.escape(name)}</text>')
        # Stats
        parts.append(f'<text x="{x}" y="{ry + 62}" text-anchor="middle" fill="{subtext_color}" font-size="10">{seg["n_companies"]} 家 · 累计融资 ${seg["total_funding_b"]}B</text>')
        if seg["total_revenue_b"] > 0:
            parts.append(f'<text x="{x}" y="{ry + 76}" text-anchor="middle" fill="{subtext_color}" font-size="10">营收 ${seg["total_revenue_b"]}B</text>')
        if seg["n_dead"] > 0:
            parts.append(f'<text x="{x}" y="{ry + 90}" text-anchor="middle" fill="{subtext_color}" font-size="10">⚰️ {seg["n_dead"]} 家死亡</text>')

    # Legend
    parts.append(f'<text x="20" y="{height - 30}" font-size="11" fill="#6b7280">━━ 主线候选 (S3/S5)</text>')
    parts.append(f'<text x="20" y="{height - 12}" font-size="11" fill="#6b7280">--- 备选/不相关</text>')

    parts.append('</svg>')
    return "".join(parts)


HTML_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>AI Healthcare 研究 — Phase 1 报告</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.js"></script>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
         margin: 0; background: #f9fafb; color: #1f2937; line-height: 1.6; }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 24px; }}
  header {{ background: linear-gradient(135deg, #1f2937 0%, #4b5563 100%); color: white;
            padding: 40px 24px; margin-bottom: 24px; }}
  header h1 {{ margin: 0 0 8px; font-size: 28px; }}
  header .meta {{ color: #d1d5db; font-size: 14px; }}
  .card {{ background: white; border-radius: 12px; padding: 24px; margin-bottom: 20px;
           box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
  .card h2 {{ margin-top: 0; font-size: 22px; border-bottom: 2px solid #e5e7eb;
              padding-bottom: 12px; }}
  .card h3 {{ font-size: 16px; color: #4b5563; margin: 20px 0 8px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }}
  .stat-card {{ background: #f3f4f6; padding: 16px; border-radius: 8px; border-left: 4px solid #3b82f6; }}
  .stat-card .label {{ font-size: 12px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.05em; }}
  .stat-card .value {{ font-size: 26px; font-weight: bold; color: #1f2937; }}
  .stat-card .sub {{ font-size: 12px; color: #6b7280; }}
  .chart-container {{ position: relative; height: 400px; margin: 16px 0; }}
  .chart-container.tall {{ height: 600px; }}
  .seg-card {{ background: #f9fafb; padding: 16px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid; }}
  .seg-card h4 {{ margin: 0 0 8px; font-size: 16px; }}
  .seg-card .meta {{ font-size: 12px; color: #6b7280; margin-bottom: 8px; }}
  .seg-card .finding {{ font-size: 14px; }}
  table {{ width: 100%; border-collapse: collapse; }}
  th, td {{ text-align: left; padding: 8px 12px; border-bottom: 1px solid #e5e7eb; font-size: 13px; }}
  th {{ background: #f3f4f6; font-weight: 600; }}
  .tag {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px;
          font-weight: 500; }}
  .takeaway {{ background: #fef3c7; border-left: 4px solid #f59e0b;
              padding: 16px; border-radius: 8px; margin: 12px 0; }}
  .takeaway.green {{ background: #d1fae5; border-left-color: #10b981; }}
  .takeaway.red {{ background: #fee2e2; border-left-color: #ef4444; }}
  .takeaway.blue {{ background: #dbeafe; border-left-color: #3b82f6; }}
  .nick-section {{ background: linear-gradient(135deg, #ef4444 0%, #f59e0b 100%);
                   color: white; padding: 24px; border-radius: 12px; margin: 20px 0; }}
  .nick-section h2 {{ color: white; border-color: rgba(255,255,255,0.3); margin-top: 0; }}
  footer {{ text-align: center; padding: 24px; color: #6b7280; font-size: 12px; }}
  ul {{ padding-left: 20px; }}
  li {{ margin-bottom: 6px; }}
  code {{ background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 13px; }}
  .center {{ text-align: center; }}
  abbr[title] {{
    text-decoration: underline dotted #f59e0b;
    text-underline-offset: 3px;
    cursor: help;
    color: inherit;
  }}
  abbr[title]:hover {{
    background: #fef3c7;
    border-radius: 3px;
  }}
  details summary::-webkit-details-marker {{ display: none; }}
  details[open] summary {{ margin-bottom: 8px; }}
</style>
</head>
<body>
<header>
  <div class="container">
    <h1>🏥 AI Healthcare 研究 — Phase 1 报告</h1>
    <div class="meta">71 公司 · 7 子赛道 · 数据截止 {date} · 双轨研究 (career × investment)</div>
  </div>
</header>

<div class="container">

<!-- Glossary (中英对照) -->
{glossary_html}

<!-- Executive Summary -->
<div class="card">
  <h2>📌 5 个最重要的发现</h2>
  <div class="takeaway green">
    <strong>1. S3 <abbr title="精准医疗 — 基因测序 + AI 个性化诊断/用药">Precision Medicine</abbr> 是唯一商业化彻底成立的段。</strong>
    Tempus AI 2025 营收 $1.3B (+83% <abbr title="同比增长 / Year over Year">YoY</abbr>)，Guardant $982M，Caris $412M。段头部 3 家合计营收 $2.5B+，<strong>大于所有其他 6 个段加起来</strong>。
  </div>
  <div class="takeaway blue">
    <strong>2. S5 <abbr title="医学影像 AI（放射科 / 病理科）">Medical Imaging AI</abbr> 是国际化程度最高的段。</strong>
    以色列 / 韩国 / 印度 / 澳大利亚 / 英国 / 瑞典 / 芬兰 / 西班牙 都有头部公司。和 S1/S6 (几乎 100% 美国) 完全不同——这是 Nick 出海叙事的结构性利好。
  </div>
  <div class="takeaway">
    <strong>3. OpenEvidence 是 healthcare AI 史上最猛增长曲线。</strong>
    2024 <abbr title="年度经常性收入 / Annual Recurring Revenue（SaaS 标准营收指标）">ARR</abbr> $7.9M → 2025 ARR $150M = <strong>19x YoY</strong>。$12B 估值（<abbr title="估值 / ARR — Abridge 53x、OpenEvidence 80x 都远高于 SaaS 行业平均 10-20x">80x ARR multiple</abbr>）。商业模式是 <abbr title="药企 — pharmaceutical">pharma</abbr> 广告而非 <abbr title="软件即服务（按订阅收费）">SaaS</abbr> —— 重新定义医疗 AI 的变现路径。
  </div>
  <div class="takeaway red">
    <strong>4. 死亡集中在 S6 + S7，共烧 $1.6B+。</strong>
    Olive AI ($400M), Forward Health ($650M), Babylon Health ($550M), Pear Therapeutics ($400M)。
    形成红旗清单：AI 做核心产品 (<abbr title="即 AI 本身就是付费内容；Forward Health 卖 AI 自助诊断 kiosk，结果患者卡在里面">substance</abbr>) 而非辅助 (<abbr title="即 AI 只是加速 / 优化已有付费产品；Tempus 卖基因检测，AI 加速分析">enabling</abbr>) / 付费方未验证就大额扩张 / <abbr title="借壳上市 / Special Purpose Acquisition Company — 跳过传统 IPO 审查的捷径，2021-2023 大量医疗 startup 死于此">SPAC IPO</abbr> / CEO 演讲多客户案例少。
  </div>
  <div class="takeaway green">
    <strong>5. Insilico Medicine HK IPO (2025-12) 是 Nick 出海叙事唯一已实证范本。</strong>
    中港双总部 + AI <abbr title="生物科技 / Biotechnology — 用 AI 设计药物">biotech</abbr> + <abbr title="港交所 8.05 上市规则 — 专为未盈利生物科技公司设的通道">HK Ch 8.05 IPO</abbr> + <abbr title="药物临床试验第 2 期成功 — 证明药物在小规模患者中有效">Phase 2 阳性</abbr>。证明"中国 AI 医疗公司通过 HK 上市出海"模式可走通。
  </div>
</div>

<!-- Structural Diagram -->
<div class="card">
  <h2>🗺️ 结构图：7 个子赛道 × Nick 主线候选</h2>
  <p>红线 (S3 / S5) 为 Nick 主线候选（基于 profile match + 商业化成熟度 + 中国可映射性）。其他段虚线表示备选或仅作 calibration 用。</p>
  <div class="center">{svg_diagram}</div>
</div>

<!-- Macro Stats -->
<div class="card">
  <h2>📊 整体统计</h2>
  <div class="grid">
    <div class="stat-card">
      <div class="label">入库公司总数</div>
      <div class="value">{n_total}</div>
      <div class="sub">含 {n_dead} 家死亡、{n_acquired} 家被收购、{n_public} 家上市</div>
    </div>
    <div class="stat-card">
      <div class="label">2025 全球 <abbr title="数字医疗 — 涵盖 AI 医疗 + 远程医疗 + 健康管理 app">digital health</abbr> 融资</div>
      <div class="value">$14.2B</div>
      <div class="sub">+<abbr title="同比 / Year over Year">YoY</abbr> 35%，<abbr title="AI-native = 公司从成立第一天就以 AI 为核心">AI-native</abbr> 占 54%</div>
    </div>
    <div class="stat-card">
      <div class="label">段头部最大单家估值</div>
      <div class="value">$19.7B</div>
      <div class="sub">Nuance DAX (微软 2022 收购)</div>
    </div>
    <div class="stat-card">
      <div class="label">段头部最大单家营收</div>
      <div class="value">$1.3B</div>
      <div class="sub">Tempus AI 2025 (+83% YoY)</div>
    </div>
  </div>
</div>

<!-- Chart 1: Companies per segment -->
<div class="card">
  <h2>📈 子赛道公司数 + 累计融资分布</h2>
  <div class="chart-container">
    <canvas id="segmentChart"></canvas>
  </div>
</div>

<!-- Chart 2: Top 20 by valuation -->
<div class="card">
  <h2>💰 估值 Top 20 (公开市值 + 私募 post-money)</h2>
  <div class="chart-container tall">
    <canvas id="topValChart"></canvas>
  </div>
</div>

<!-- Chart 3: Top 15 by revenue -->
<div class="card">
  <h2>🏆 营收 Top 15</h2>
  <p>这是判断"哪些 AI 医疗 idea 真的在赚钱"的最直接指标。S3 公司主导前列。</p>
  <div class="chart-container tall">
    <canvas id="topRevChart"></canvas>
  </div>
</div>

<!-- Chart 4: Capital efficiency scatter -->
<div class="card">
  <h2>📐 资本效率：营收 vs 估值（双对数坐标 / log scale）</h2>
  <p><strong>怎么读这张图：</strong>横轴 = 营收（log），纵轴 = 估值（log）。<br>
  <strong>右下方角落</strong>（高营收 + 相对低估值）= <abbr title="估值 / 营收倍数低 = 市场认为这家公司已充分定价 / 增长预期保守">营收已兑现的"价值股"</abbr>（如 Tempus, Guardant, Hims）<br>
  <strong>左上方角落</strong>（低营收 + 高估值）= <abbr title="估值 / 营收倍数极高 = 市场押注未来 5-10x 增长，相当贵">市场押注未来的"成长股"</abbr>（如 Abridge 53x、OpenEvidence 80x）<br>
  对你投资判断的含义：左上方公司风险高、回报高；右下方公司更"安全"但回报上限被定价了。
  </p>
  <div class="chart-container">
    <canvas id="capEffChart"></canvas>
  </div>
</div>

<!-- Chart 5: Geography -->
<div class="card">
  <h2>🌍 地理分布（按 HQ 国家）</h2>
  <div class="chart-container">
    <canvas id="geoChart"></canvas>
  </div>
  <p style="margin-top:12px;color:#6b7280;font-size:13px;">⚠️ 中国公司还没纳入（Phase 3 双表架构会补 ~30 家中国公司到 china_companies.csv）。</p>
</div>

<!-- Chart 6: Status by segment -->
<div class="card">
  <h2>⚰️ 存活分析（按段统计）</h2>
  <p>S6 + S7 是死亡冠军段。S5 + S3 几乎没有死亡（设备/诊断有实业现金流支撑）。</p>
  <div class="chart-container">
    <canvas id="statusChart"></canvas>
  </div>
</div>

<!-- Per-segment findings -->
<div class="card">
  <h2>📝 每个子赛道的核心发现</h2>
  {segment_findings_html}
</div>

<!-- Nick takeaways -->
<div class="nick-section">
  <h2>🎯 对 Nick 职业决策的核心 takeaways</h2>

  <h3 style="color:white;">⚠️ 2026-05-16 框架修正：entry path 不是 1 维是 2 维</h3>
  <p>初版分析犯了一个错误：把 "Nick 不擅长 leetcode" 翻译成"不该进 S2 LLM 段"。
  但 entry path 实际上是 <strong>2 维</strong>：段（S1-S7） × 角色（engineer / PM / clinical app / BD）。
  同一家公司在不同角色门槛下对 Nick 的 effort 差异极大。
  详细分析见 <code>04-synthesis/pm-pathways.md</code>。</p>

  <h3 style="color:white;">主线候选（v2 加入 PM 路径后）</h3>
  <ol>
    <li><strong>A (engineer/科研): 联影智能 海外业务（S5 imaging）</strong> — profile match 完美 + 国际化段最自然落脚 + 上海 HQ 兼容家族业务</li>
    <li><strong>B (engineer/科研): 华大智造 MGI 海外业务（S3 precision medicine）</strong> — Phase 1 新发现升级。MGI 是中国精准医疗设备厂出海最成功标杆</li>
    <li><strong>C (PM): GPS 中国 AI 部门 Product Manager</strong> — 双合规 + 外资稳定性 + clinical PM 岗</li>
    <li>🆕 <strong>Plan B (PM): 字节豆包医疗 / 阿里通义医疗 PM</strong> — 中国 LLM 大厂医疗 vertical 入口；你 PhD + 双语 + 海外经验在这里是稀缺资源</li>
    <li>🆕 <strong>Plan C (PM): 腾讯觅影 AI 影像产品经理</strong> — S5 影像段 + 腾讯生态，profile 双重对口</li>
    <li><strong>Plan D (engineer 保底): 数坤 / 推想 / 迈瑞 国内研发岗</strong> — 红旗 2/6（估值倒挂 + 长期没新轮），慎选</li>
  </ol>

  <h3 style="color:white;">不该走的赛道（在 PM 路径修正后重新评估）</h3>
  <table style="background:rgba(255,255,255,0.1);color:white;">
    <thead><tr><th style="color:white">段</th><th style="color:white">engineer 路径</th><th style="color:white">PM 路径</th><th style="color:white">结论</th></tr></thead>
    <tbody>
      <tr><td>S1 Scribe</td><td>❌ leetcode 卡 + 中国市场小</td><td>❌ 中国市场太小，PM 也救不了</td><td>不走</td></tr>
      <tr><td><strong>S2 Medical LLM</strong></td><td>❌ leetcode 卡</td><td>✅ <strong>升级为 Plan B/C</strong>（字节/阿里/腾讯/DeepSeek 医疗 vertical PM）</td><td><strong>PM 路径可走</strong></td></tr>
      <tr><td>S6 RCM/Admin AI</td><td>❌ 中国 <abbr title="付费方结构">payer</abbr>不同</td><td>❌ 同上 — 赛道在中国不存在</td><td>不走</td></tr>
      <tr><td>S7 Consumer Virtual Care</td><td>❌ PhD 不加分</td><td>⚠️ 轻微升级（京东/平安/阿里健康 PM 岗存在）但天花板低</td><td>不优先</td></tr>
    </tbody>
  </table>

  <h3 style="color:white;">案例研究 anchor（最值得 deep dive 的 4 家）</h3>
  <ul>
    <li>🌟 <strong>Insilico Medicine</strong> — 中港双总部 + AI + HK IPO 已走通的唯一范本。Phase 4 <abbr title="电梯图 / 你的职业上升路径图，10-15 年的多阶段规划">elevator map</abbr> 必读</li>
    <li>🌟 <strong>HeartFlow</strong> — IPO Aug 2025 $1.54B，走通了 AI + <abbr title="美国医保编码 / Current Procedural Terminology — 拿到代表保险愿意报销">CPT code</abbr> + 医保报销链。中国 imaging AI 公司能否复制是关键问题</li>
    <li>🌟 <strong>Tempus AI</strong> — $1.3B 营收证明"AI 是 <abbr title="辅助加速">enabling</abbr> 不是 <abbr title="核心付费产品">substance/product</abbr>"模式可成立。和中国设备厂出海逻辑同构</li>
    <li>🌟 <strong>Subtle Medical</strong> — 中美双总部 + 斯坦福 EE PhD 创始人 + 算法 + 影像 + Samsung/Siemens <abbr title="原始设备制造商合作 — 嵌入大厂设备里卖">OEM</abbr>。Nick perfect match 的直接 <abbr title="入职路径">entry path</abbr></li>
  </ul>

  <h3 style="color:white;">红旗清单（评估任何中国 AI 医疗公司用）</h3>
  <ol>
    <li>AI 做核心付费产品而非辅助工具（Forward Health 模式 → 死）</li>
    <li>付费方未验证就大额扩张（Pear Therapeutics → 死，<abbr title="FDA 批准了产品但保险公司不报销 = 商业失败">FDA 批了但保险拒付</abbr>）</li>
    <li><abbr title="借壳上市 / Special Purpose Acquisition Company — 跳过传统 IPO 审查">SPAC IPO</abbr> 路径（Babylon / Pear → 死）</li>
    <li>CEO 演讲数 / 客户案例数 比例 > 5:1（Olive AI → 死）</li>
    <li>多国家/多业务线扩张过早，没有 1 个单点突破</li>
    <li><abbr title="新一轮融资估值低于上一轮 / valuation down round">估值倒挂</abbr> + 长期没新轮（数坤 / 推想 当前红旗 2/6）</li>
  </ol>
</div>

<!-- Methodology -->
<div class="card">
  <h2>🔍 方法论 + 数据来源</h2>
  <ul>
    <li><strong>样本:</strong> 71 家公司，覆盖 7 子赛道，含 4 家已死亡公司作为 cautionary tale</li>
    <li><strong>资格筛:</strong> Series B+ / 上市 / 显著被收购 / 显著死亡 / rising star ($50M+ in &lt;3y)</li>
    <li><strong>schema:</strong> 23 列（详见 <code>_meta/schema.md</code>），含 7 列 career 相关字段</li>
    <li><strong>Source 优先级:</strong> SEC 10-K/S-1 &gt; Rock Health / Menlo VC / Sacra &gt; TechCrunch / StatNews / Fierce / 报道</li>
    <li><strong>Cross-validation:</strong> 关键数字至少 2 个独立来源（Nabla 估值被 aifundingtracker 错报 $5.3B vs StatNews 实际 $180M 是 cautionary case）</li>
    <li><strong>Reusability:</strong> 全部数据在 <code>data/companies.csv</code> + 每次重大变化前 snapshot 到 <code>data/snapshots/</code></li>
    <li><strong>研究完成度:</strong> Phase 1-4 全部完成（2026-05-16）</li>
    <li><strong>Phase 2 cross-segment 统计:</strong> <code>02-us-statistics/01-05</code> 共 5 个 md（脚本 <code>scripts/ai_healthcare_stats.py</code> 可复用）</li>
    <li><strong>Phase 3 中国对应公司:</strong> 25 家入 <code>data/china_companies.csv</code>；mapping 文档 <code>03-china-mapping/00-us-china-mapping.md</code></li>
    <li><strong>Phase 4 elevator map (最终交付物):</strong> <code>04-synthesis/elevator-map.md</code> — 5-15 年多阶段路径图 + 决策触发器列表</li>
    <li><strong>v3 框架修正:</strong> PM 路径维度（<code>04-synthesis/pm-pathways.md</code>），entry path 从 1 维升级到 2 维（段 × 角色）</li>
  </ul>
</div>

<footer>
  Generated by <code>scripts/ai_healthcare_report.py</code> · re-run after CSV updates to refresh
  <br>
  研究 owner: Nick · 数据生成时间: {date}
</footer>

</div>

<script>
const DATA = {chart_data_json};

const COMMON_OPTS = {{
  responsive: true,
  maintainAspectRatio: false,
  plugins: {{ legend: {{ position: 'top' }} }}
}};

// Chart 1: Segment companies + funding
new Chart(document.getElementById('segmentChart'), {{
  type: 'bar',
  data: {{
    labels: DATA.segments.map(s => s.code + ' ' + s.name.substring(0, 25)),
    datasets: [
      {{
        label: '公司数',
        data: DATA.segments.map(s => s.n_companies),
        backgroundColor: DATA.segments.map(s => s.color),
        yAxisID: 'y'
      }},
      {{
        label: '累计融资 ($B)',
        data: DATA.segments.map(s => s.total_funding_b),
        backgroundColor: DATA.segments.map(s => s.color + '80'),
        yAxisID: 'y1',
        type: 'line'
      }}
    ]
  }},
  options: {{
    ...COMMON_OPTS,
    scales: {{
      y: {{ type: 'linear', position: 'left', title: {{ display: true, text: '公司数' }} }},
      y1: {{ type: 'linear', position: 'right', title: {{ display: true, text: '累计融资 ($B)' }}, grid: {{ drawOnChartArea: false }} }}
    }}
  }}
}});

// Chart 2: Top 20 by valuation
new Chart(document.getElementById('topValChart'), {{
  type: 'bar',
  data: {{
    labels: DATA.top_val.map(c => c.name),
    datasets: [{{
      label: 'Valuation ($B)',
      data: DATA.top_val.map(c => c.valuation_b),
      backgroundColor: DATA.top_val.map(c => c.color)
    }}]
  }},
  options: {{
    ...COMMON_OPTS,
    indexAxis: 'y',
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{
        callbacks: {{
          afterLabel: (ctx) => {{
            const c = DATA.top_val[ctx.dataIndex];
            return [`Segment: ${{c.segment}}`, `Status: ${{c.status}}`, `Country: ${{c.country}}`];
          }}
        }}
      }}
    }},
    scales: {{ x: {{ title: {{ display: true, text: 'Valuation / Market Cap ($B)' }} }} }}
  }}
}});

// Chart 3: Top 15 by revenue
new Chart(document.getElementById('topRevChart'), {{
  type: 'bar',
  data: {{
    labels: DATA.top_rev.map(c => c.name),
    datasets: [{{
      label: 'Revenue ($M)',
      data: DATA.top_rev.map(c => c.revenue_m),
      backgroundColor: DATA.top_rev.map(c => c.color)
    }}]
  }},
  options: {{
    ...COMMON_OPTS,
    indexAxis: 'y',
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{
        callbacks: {{
          afterLabel: (ctx) => {{
            const c = DATA.top_rev[ctx.dataIndex];
            const yoy = c.yoy ? ` (YoY +${{c.yoy}}%)` : '';
            return [`Segment: ${{c.segment}}${{yoy}}`];
          }}
        }}
      }}
    }},
    scales: {{ x: {{ title: {{ display: true, text: 'Annual Revenue / ARR ($M)' }} }} }}
  }}
}});

// Chart 4: Capital efficiency scatter
const segments_set = [...new Set(DATA.cap_eff.map(c => c.segment))];
new Chart(document.getElementById('capEffChart'), {{
  type: 'scatter',
  data: {{
    datasets: segments_set.map(seg => ({{
      label: seg,
      data: DATA.cap_eff.filter(c => c.segment === seg).map(c => ({{ x: c.revenue, y: c.valuation, name: c.name, mult: c.rev_multiple }})),
      backgroundColor: DATA.cap_eff.find(c => c.segment === seg).color,
      pointRadius: 8
    }}))
  }},
  options: {{
    ...COMMON_OPTS,
    scales: {{
      x: {{ type: 'logarithmic', title: {{ display: true, text: 'Revenue ($M, log scale)' }} }},
      y: {{ type: 'logarithmic', title: {{ display: true, text: 'Valuation ($M, log scale)' }} }}
    }},
    plugins: {{
      tooltip: {{
        callbacks: {{
          label: (ctx) => `${{ctx.raw.name}}: $${{ctx.raw.x}}M rev → $${{ctx.raw.y}}M val (${{ctx.raw.mult}}x)`
        }}
      }}
    }}
  }}
}});

// Chart 5: Geography
const countries = Object.entries(DATA.by_country).sort((a, b) => b[1] - a[1]);
new Chart(document.getElementById('geoChart'), {{
  type: 'bar',
  data: {{
    labels: countries.map(c => c[0]),
    datasets: [{{
      label: '公司数',
      data: countries.map(c => c[1]),
      backgroundColor: '#3b82f6'
    }}]
  }},
  options: {{ ...COMMON_OPTS, plugins: {{ legend: {{ display: false }} }} }}
}});

// Chart 6: Status by segment (stacked)
const status_keys = ['private', 'public', 'acquired', 'dead'];
const status_colors = {{ private: '#3b82f6', public: '#10b981', acquired: '#f59e0b', dead: '#ef4444' }};
new Chart(document.getElementById('statusChart'), {{
  type: 'bar',
  data: {{
    labels: DATA.segments.map(s => s.code),
    datasets: status_keys.map(status => ({{
      label: status,
      data: DATA.segments.map(s => (DATA.by_seg_status[s.code] || {{}})[status] || 0),
      backgroundColor: status_colors[status]
    }}))
  }},
  options: {{
    ...COMMON_OPTS,
    scales: {{ x: {{ stacked: true }}, y: {{ stacked: true }} }}
  }}
}});
</script>
</body>
</html>
"""


def build_segment_findings_html(seg_summary: list[dict]) -> str:
    findings = {
        "S1": '<strong>Abridge $5.3B 估值 + $100M <abbr title="年度经常性收入">ARR</abbr> (53x <abbr title="估值/营收倍数">multiple</abbr>)</strong>。Nuance DAX 仍占 33% 市场（被微软 $19.7B 收购）。'
              '中国可映射性极低（中国医生不口述病历 / <abbr title="电子病历 / Electronic Health Records — 美国 Epic + Cerner 主导，中国卫宁/东软分散">EHR</abbr> 不标准化）',
        "S2": '<strong>OpenEvidence <abbr title="年度经常性收入">ARR</abbr> 19x YoY 是 healthcare AI 最猛增长</strong>。<abbr title="药企广告">Pharma 广告</abbr>变现模式重新定义医疗 AI。'
              '但赛道本质是 <abbr title="大语言模型 / Large Language Model — 如字节豆包、阿里通义、DeepSeek">LLM</abbr> 大厂的，不是 startup 战场',
        "S3": '<strong>段商业化最成立</strong>：Tempus $1.3B + Guardant $982M + Caris $412M。AI 是 <abbr title="辅助加速 — 不是付费内容本身">enabling</abbr> 而非 <abbr title="核心产品 — AI 本身是付费内容">substance</abbr>。'
              '<strong>MGI 华大智造海外业务是 Nick 主线候选</strong>',
        "S4": '<strong>私募狂热 vs 公开市场冷淡的最大 disconnect 段</strong>。Insilico <abbr title="香港交易所">HK</abbr> IPO Dec 2025 ($2.7B) 是中港双总部 + AI + 出海 IPO 的唯一已实证范本',
        "S5": '<strong>国际化程度最高的段</strong>（10+ 国家头部并存）。HeartFlow IPO Aug 2025 $1.54B + $136M 营收 +39% <abbr title="同比">YoY</abbr> 是商业化范本。'
              'Subtle Medical 中美双总部最对 Nick <abbr title="个人背景档案 / professional profile">profile</abbr>',
        "S6": '<strong>高增速低基数高死亡率</strong>。Olive AI ($400M) + Babylon ($550M) 双死亡。Innovaccer $3.45B 估值靠多模块平台。'
              '中国可映射性极低（<abbr title="付费方 / payer — 中国主要是医保局单一支付，美国是商业保险+雇主+患者多元支付">payer</abbr> 结构不同）',
        "S7": '<strong>段死亡率冠军</strong>：Forward / Pear / Babylon 共烧 $1.6B+。但 Hims & Hers 公开市场年化 $2.5B。Nick 应完全跳过本段',
    }
    parts = []
    for seg in seg_summary:
        code = seg["code"]
        finding = findings.get(code, "")
        parts.append(f'''
        <div class="seg-card" style="border-left-color: {seg['color']}">
          <h4><span class="tag" style="background:{seg['color']};color:white">{code}</span> {html.escape(seg['name'])}</h4>
          <div class="meta">{seg['n_companies']} 公司 · 累计融资 ${seg['total_funding_b']}B · 累计营收 ${seg['total_revenue_b']}B · {seg['n_dead']} 死亡 · {seg['n_public']} 上市 · {seg['n_acquired']} 被收购</div>
          <div class="finding">{finding}</div>
        </div>
        ''')
    return "\n".join(parts)


def main():
    rows = load_companies()
    agg = aggregate(rows)
    svg = build_svg_structural_diagram(agg["seg_summary"])
    findings_html = build_segment_findings_html(agg["seg_summary"])

    chart_data = {
        "segments": agg["seg_summary"],
        "top_val": agg["top_val"],
        "top_rev": agg["top_rev"],
        "cap_eff": agg["cap_eff"],
        "by_country": agg["by_country"],
        "by_seg_status": agg["by_seg_status"],
    }

    html_out = HTML_TEMPLATE.format(
        date=datetime.now().strftime("%Y-%m-%d"),
        svg_diagram=svg,
        glossary_html=build_glossary_html(),
        n_total=agg["n_total"],
        n_dead=agg["by_status"].get("dead", 0),
        n_acquired=agg["by_status"].get("acquired", 0),
        n_public=agg["by_status"].get("public", 0),
        segment_findings_html=findings_html,
        chart_data_json=json.dumps(chart_data, ensure_ascii=False),
    )

    OUT_PATH.write_text(html_out, encoding="utf-8")
    print(f"Wrote {OUT_PATH}")
    print(f"  - {agg['n_total']} companies aggregated")
    print(f"  - {len(agg['seg_summary'])} segments")
    print(f"  - {len(agg['top_val'])} in top valuation chart")


if __name__ == "__main__":
    main()
