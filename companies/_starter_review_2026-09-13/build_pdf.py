#!/usr/bin/env python
"""Build the STARTER review PDF (2026-09-13).

Source of truth: companies/_starter_review_2026-09-13/report.md
Output:          output/pdf/starter_review_2026-09-13.pdf

Re-run: python companies/_starter_review_2026-09-13/build_pdf.py
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, ".pdf_deps"))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
)

OUT_DIR = os.path.join(REPO, "output", "pdf")
OUT_PDF = os.path.join(OUT_DIR, "starter_review_2026-09-13.pdf")
os.makedirs(OUT_DIR, exist_ok=True)

pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\simhei.ttf"))
pdfmetrics.registerFont(TTFont("CNB", r"C:\Windows\Fonts\simhei.ttf"))

INK, MUTED, LINE = colors.HexColor("#1a1d24"), colors.HexColor("#5b6472"), colors.HexColor("#d8dee8")
GOOD, WARN, BAD = colors.HexColor("#0f766e"), colors.HexColor("#b45309"), colors.HexColor("#b91c1c")
SOFT, HEAD = colors.HexColor("#f4f7fb"), colors.HexColor("#eef2f8")

ss = getSampleStyleSheet()
S = dict(
    title=ParagraphStyle("t", parent=ss["Title"], fontName="CN", fontSize=19, leading=25,
                         textColor=INK, spaceAfter=3, alignment=0),
    sub=ParagraphStyle("s", fontName="CN", fontSize=9, leading=13, textColor=MUTED, spaceAfter=11),
    h1=ParagraphStyle("h1", fontName="CN", fontSize=13.5, leading=18, textColor=INK,
                      spaceBefore=13, spaceAfter=6),
    h2=ParagraphStyle("h2", fontName="CN", fontSize=11, leading=15, textColor=INK,
                      spaceBefore=10, spaceAfter=4),
    p=ParagraphStyle("p", fontName="CN", fontSize=8.6, leading=13.2, textColor=INK, spaceAfter=5),
    small=ParagraphStyle("sm", fontName="CN", fontSize=7.6, leading=11.4, textColor=MUTED, spaceAfter=4),
    quote=ParagraphStyle("q", fontName="CN", fontSize=8.3, leading=12.6, textColor=INK,
                         leftIndent=8, borderPadding=(5, 5, 5, 7), backColor=SOFT, spaceAfter=6),
    cell=ParagraphStyle("c", fontName="CN", fontSize=7.5, leading=10.2, textColor=INK),
    cellr=ParagraphStyle("cr", fontName="CN", fontSize=7.5, leading=10.2, textColor=INK, alignment=2),
    cellh=ParagraphStyle("ch", fontName="CN", fontSize=7.5, leading=10.2, textColor=INK),
)


def P(t, k="p"):
    return Paragraph(t, S[k])


def tbl(rows, widths, aligns=None, hi=None):
    """rows[0] = header. aligns: list of 'l'/'r'. hi: {rowidx: color}"""
    aligns = aligns or ["l"] * len(rows[0])
    data = []
    for i, r in enumerate(rows):
        out = []
        for j, c in enumerate(r):
            st = "cellh" if i == 0 else ("cellr" if aligns[j] == "r" else "cell")
            out.append(Paragraph(str(c), S[st]))
        data.append(out)
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), HEAD),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, LINE),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]
    for ri, col in (hi or {}).items():
        cmds.append(("BACKGROUND", (0, ri), (-1, ri), col))
    t.setStyle(TableStyle(cmds))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("CN", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 11 * mm, "STARTER 名单复查 · as_of 2026-09-11 收盘 · 生成 2026-09-13")
    canvas.drawRightString(A4[0] - 18 * mm, 11 * mm, "第 %d 页" % doc.page)
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 14.5 * mm, A4[0] - 18 * mm, 14.5 * mm)
    canvas.restoreState()


W = A4[0] - 36 * mm
F = []

# ---------- cover ----------
F += [P("STARTER 名单复查", "title"),
      P("6 家 STARTER · 全部 38 张 decision card 的 buy_below 接近度板<br/>"
        "价格 as_of 2026-09-11 收盘 · 报告生成 2026-09-13", "sub")]

F.append(tbl(
    [["", "本报告是什么 / 不是什么"],
     ["✅ 是", "价格 vs 各卡 buy_below 的比价 + <b>每家自建卡以来新一手文件的基本面复查</b>(SEC EDGAR 全查)"],
     ["❌ 不是", "<b>没有重跑六模块;没有重新推导任何一个 buy_below / IRR 锚</b>"]],
    [22 * mm, W - 22 * mm]))
F.append(Spacer(1, 5))
F.append(P("所有 buy_below 沿用各卡原值。锚的口径不同(8% / 10% / 12% IRR hurdle),卡日期从 2026-06-19 到 2026-09-05 不等。"
           "<b>横向排名只是粗序,不是精确可比。</b>", "small"))

# ---------- 1 结论速览 ----------
F.append(P("一、结论速览", "h1"))
F.append(P("<b>6 家 STARTER,复查后只有 1 家可以直接进下一步。</b>", "p"))
F.append(tbl(
    [["名字", "现价", "buy_below", "位置", "新一手文件", "基本面复查", "判定"],
     ["<b>INTU</b>", "$321.57", "$328", "<b>线内 +2.0%</b>", "8-K 8/25 + <b>10-K 9/9</b>", "✅ 稳,增速下台阶", "<b>🥇 可进 IC panel</b>"],
     ["<b>SYK</b>", "$275.56", "$366", "线下 +32.8%", "10-Q 7/31", "✅ <b>明显改善</b>", "🥈 卡需刷新"],
     ["<b>ISRG</b>", "$369.15", "$452", "线下 +22.4%", "10-Q 7/21", "✅ <b>明显改善</b>", "🥈 卡需刷新"],
     ["<b>ADBE</b>", "$252.23", "$306", "线下 +21.3%", "8-K 9/8 + 9/10", "⚠️ 封顶项解一半", "🥉 有新警号"],
     ["<b>MELI</b>", "$1,897.37", "$1,900", "线内 +0.1%", "10-Q 8/6", "🔴 <b>利润率腰斩</b>", "❌ <b>锚已过期</b>"],
     ["<b>MSFT</b>", "$495.63", "$363–379", "<b>线上 −23.5%</b>", "10-K 7/29", "✅ 稳", "❌ <b>verdict 失效</b>"]],
    [15 * mm, 18 * mm, 19 * mm, 20 * mm, 30 * mm, 27 * mm, W - 129 * mm],
    ["l", "r", "r", "r", "l", "l", "l"],
    hi={1: colors.HexColor("#eaf6f3"), 5: colors.HexColor("#fdeeee"), 6: colors.HexColor("#fdeeee")}))
F.append(Spacer(1, 5))
F.append(Paragraph(
    "<b>最重要的一条:MELI 正好站在 buy_below 上($1,897 vs $1,900),但它的营业利润率在卡之后从 17.2% 腰斩到 9.7%。</b><br/>"
    "「正好到线」是假象 —— 分母变了,线就该动。<b>这和 GOOGL / NVDA 是同一个形状。</b>", S["quote"]))

# ---------- 2 逐名 ----------
F.append(PageBreak())
F.append(P("二、逐名复查", "h1"))

F.append(P("🥇 INTU —— 唯一一个封顶项被正式文件解除的", "h2"))
F.append(Paragraph("卡(2026-08-07 @ $321.91)binding_constraint 原文:「完整度 + 耐久性未决,<b>不是价格</b>。"
                   "base 10y IRR +10.2% 已过 8% hurdle 且有 2.2pt cushion;封顶的是 "
                   "<b>FY2026 全年业绩要到 2026-08-25 才出</b>、AI 变现零披露、TurboTax 单量拐点未定。」", S["quote"]))
F.append(P("<b>那个日期过了,文件都在:</b>8-K(Item 2.02)2026-08-25 + <b>10-K(FY2026,period 2026-07-31)2026-09-09 报送</b>。", "p"))
F.append(P("FY2026 实际交付(全年,截至 2026-07-31):", "p"))
F.append(tbl(
    [["项", "值", "YoY", "项", "值", "YoY"],
     ["总营收", "$21.4B", "<b>+14%</b>", "TurboTax", "$5.3B", "+7%"],
     ["Global Business Solutions", "$12.9B", "+16%(ex-MC +18%)", "TurboTax Live", "—", "<b>+37%</b>"],
     ["Online Ecosystem", "$9.9B", "+19%(ex-MC +23%)", "Credit Karma", "$2.6B", "+20%"],
     ["QuickBooks Online Acct", "—", "<b>+23%</b>", "GAAP 营业利润", "$5.9B", "<b>+20%</b>"],
     ["Consumer", "$8.6B", "+11%", "GAAP EPS", "$16.46", "<b>+20%</b>"]],
    [37 * mm, 16 * mm, 28 * mm, 30 * mm, 16 * mm, W - 127 * mm],
    ["l", "r", "r", "l", "r", "r"]))
F.append(Spacer(1, 4))
F.append(P("🔑 卡里点名「待定」的 TurboTax 单量,拿到了:", "p"))
F.append(tbl(
    [["美国 TurboTax 联邦单量", "FY2026", "FY2025", "变化"],
     ["Desktop", "4.1M", "4.4M", "<b>−7%</b>"],
     ["Online", "34.9M", "35.5M", "−2%"],
     ["<b>总计</b>", "<b>39.0M</b>", "<b>39.9M</b>", "<b>−2%</b>"]],
    [50 * mm, 24 * mm, 24 * mm, W - 98 * mm], ["l", "r", "r", "r"]))
F.append(Spacer(1, 4))
F.append(P("<b>判读:单量 −2%,营收 +7%。</b>卡里描述的「以单量换单价」机制<b>被证实,不是被推翻</b> —— "
           "而且侵蚀幅度温和(−2%),不是崩塌。", "p"))
F.append(P("<b>两个必须记进模型的变化:</b><br/>"
           "① ⚠️ <b>FY2027 指引减速:总营收 $23,279–23,512M = +9% 到 +10%</b>(FY2026 是 +14%)。"
           "卡的 base 10y IRR +10.2% 是在 FY2026 数字出来之前算的,<b>这个减速必须进模型重算</b>。<br/>"
           "② 口径变更两条(FY2027 起):<b>Mailchimp 独立成可报告分部</b>(那笔 $12B 失败收购被圈出来);"
           "<b>股权激励费用不再从 non-GAAP 剔除</b>(会计诚实度提升,但会压低 non-GAAP)。", "p"))
F.append(Paragraph("<b>结论:基本面没有大变化,反而比卡里假设的更实。唯一新变量是增速下台阶。"
                   "这是 6 家里唯一一个「封顶项有正式文件、价格在线内、verdict 已是 STARTER」的。</b>", S["quote"]))

F.append(P("🥈 SYK / ISRG —— 基本面明显改善,但卡完全没吃进 Q2", "h2"))
F.append(tbl(
    [["", "营收 YoY", "营业利润 YoY", "营业利润率", "股价 vs 卡", "10-Q 报送"],
     ["<b>SYK</b> Q2'26", "+9.4%", "<b>+49.1%</b>", "18.5% → <b>25.2%</b>", "≈ −25%", "2026-07-31"],
     ["<b>ISRG</b> Q2'26", "<b>+18.5%</b>", "<b>+30.7%</b>", "30.5% → <b>33.6%</b>", "≈ −13%", "2026-07-21"]],
    [24 * mm, 22 * mm, 26 * mm, 32 * mm, 24 * mm, W - 128 * mm],
    ["l", "r", "r", "l", "r", "l"]))
F.append(Spacer(1, 4))
F.append(P("两家<b>营收与利润率双双扩张,而股价在卡之后分别跌了约 25% 和 13%</b> —— 价格与基本面背离,这本身需要解释。"
           "卡分别是 7/5 和 7/2 的,财报是 7/30 和 7/21 的 → <b>卡完全没吃进这个季度,必须刷新。</b>", "p"))

F.append(PageBreak())
F.append(P("🥉 ADBE —— 封顶项解了一半,并出现一个新警号", "h2"))
F.append(P("卡(2026-08-07 @ $265.74)binding_constraint 是<b>可验证性,不是价格</b>:"
           "<b>O1</b> 公司连续两次撤掉最能证伪论点的 ARR 指标;<b>O7</b> CEO 继任者未定、CFO 是临时的。<br/>"
           "现价 <b>$252.23</b>(比卡再跌 5.1%),线下 <b>21.3%</b>。base 10y IRR +14.2%,P/E 15.2x,P/FCF 10.7x。", "p"))
F.append(tbl(
    [["文件", "内容", "对封顶项的影响"],
     ["<b>8-K 2026-09-08</b><br/>(Item 5.02)",
      "<b>Anil Chakravarthy 获任正式 President &amp; CEO</b>,2026-12-01 生效;"
      "Narayen 转任 Executive Chair。<b>永久任命,非过渡。</b>",
      "<b>O7 的 CEO 腿解除</b><br/>但 <b>CFO 仍是临时的</b>(9/10 财报署名 "
      "“Steve Day, SVP and <b>interim CFO</b>”)→ O7 未完全解除"],
     ["<b>8-K 2026-09-10</b><br/>(Item 2.02)<br/>Q3 FY2026",
      "营收 <b>$6.76B,+13% YoY</b>;GAAP 摊薄 EPS <b>$4.62</b>;"
      "<b>Total Adobe ARR $27.272B,增速 ~10%</b>;AI-first ARR <b>+150%</b>;"
      "MAU 突破 <b>10 亿</b>;<b>上调全年营收和 EPS 目标</b>",
      "<b>O1 部分解除</b> —— 但口径换了"]],
    [28 * mm, 72 * mm, W - 100 * mm]))
F.append(Spacer(1, 5))
F.append(Paragraph(
    "⚠️ <b>两个必须看清的点:</b><br/>"
    "① <b>口径换了。</b>恢复披露的是<b>全公司总 ARR</b>,不是卡点名要的<b>净新增 ARR / Digital Media ARR</b>。"
    "刀钝了一档,不是原来那把。O1 只能算部分解除。<br/>"
    "② 🔴 <b>ARR 增速 ~10% &lt; 营收增速 13%。</b>ARR 是前瞻指标、营收是滞后指标 —— "
    "<b>ARR 跑得比营收慢,意味着减速还在前面。这恰恰是卡怀疑、而公司撤指标想盖住的那件事。</b>"
    "这是本次复查在 ADBE 上发现的<b>新警号</b>。", S["quote"]))
F.append(P("市场反应:9/01 $286.08 → 9/04 $266.51 → <b>9/10 $248.83(Q3 财报日)</b> → 9/11 $252.23。"
           "<b>「创纪录 Q3 + 上调全年指引 + CEO 落定」,八个交易日仍跌 13%。</b>", "p"))

F.append(P("❌ MELI —— 正好到线,但锚已过期", "h2"))
F.append(P("卡(2026-07-02):buy_below ≤ $1,900,「today qualifies」。现价 <b>$1,897.37 —— 距线 0.1%</b>,"
           "看上去是全表最「正好」的一个。<b>但 Q2 财报(10-Q,2026-08-06)显示:</b>", "p"))
F.append(tbl(
    [["MELI", "Q2'26", "Q2'25", "YoY"],
     ["营收", "$7,055M", "$4,803M", "<b>+46.9%</b>"],
     ["营业利润", "$683M", "$825M", "<b>−17.2%</b>"],
     ["净利润", "$466M", "$523M", "−10.9%"],
     ["<b>营业利润率</b>", "<b>9.7%</b>", "17.2%", "<b>−7.5pp</b>"]],
    [32 * mm, 26 * mm, 26 * mm, W - 84 * mm], ["l", "r", "r", "r"],
    hi={4: colors.HexColor("#fdeeee")}))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>营收涨 47%,营业利润反而掉 17%,利润率从 17.2% 腰斩到 9.7%。</b><br/>"
                   "$1,900 这条线是用 Q2 之前的盈利能力推的。分母变了,线就该往下走。"
                   "<b>「正好到买点」是假象。在重推 buy_below 之前,MELI 不应被当作在线内。</b><br/>"
                   "这是本次复查最重要的单一发现。", S["quote"]))

F.append(P("❌ MSFT —— verdict 已失效", "h2"))
F.append(P("卡(2026-06-19 @ $379.40):<b>STARTER 4%</b>,公允价 $436,binding constraint 是<b>完整度不是价格</b>。"
           "现价 <b>$495.63,+30.6%</b>:", "p"))
F.append(tbl(
    [["卡上阶梯", "价位", "现价相对位置"],
     ["Add / 评 CORE(12% IRR)", "$303", "+63.6%"],
     ["STARTER 带上沿", "$379", "<b>+30.8%</b>"],
     ["<b>no-chase 上沿(8% IRR)</b>", "<b>$436</b>", "<b>+13.7%</b>"]],
    [52 * mm, 22 * mm, W - 74 * mm], ["l", "r", "r"], hi={3: colors.HexColor("#fdeeee")}))
F.append(Spacer(1, 4))
F.append(P("<b>价格已越过它自己的 8% IRR 线 13.7%。约束从「不是价格」变成了「是价格」。</b>"
           "基本面复查:最新季营收 +18.3%、营业利润 +20.0%、利润率 45.7%→46.3% —— <b>生意没问题,是价格跑了。</b>"
           "这张 STARTER 卡不能再被引用,M6 必须重跑。", "p"))

# ---------- 3 board ----------
F.append(PageBreak())
F.append(P("三、完整 buy_below 接近度板(38 家,2026-09-11)", "h1"))
F.append(P("已在线内 / 线下", "h2"))
F.append(tbl(
    [["#", "名字", "现价", "buy_below", "已在线下", "卡日期", "卡 verdict"],
     ["1", "TEM", "$59.01", "$84.14", "<b>+42.6%</b>", "07-04", "WATCH"],
     ["2", "<b>SYK</b>", "$275.56", "$366", "<b>+32.8%</b>", "07-05", "<b>STARTER</b>"],
     ["3", "<b>ISRG</b>", "$369.15", "$452", "<b>+22.4%</b>", "07-02", "<b>STARTER</b>"],
     ["4", "<b>ADBE</b>", "$252.23", "$306", "<b>+21.3%</b>", "08-07", "<b>STARTER</b>"],
     ["5", "BSX", "$42.98", "$52", "+21.0%", "07-05", "WATCH"],
     ["6", "EW", "$84.37", "$92", "+9.0%", "07-05", "WATCH"],
     ["7", "<b>INTU</b>", "$321.57", "$328", "<b>+2.0%</b>", "08-07", "<b>STARTER</b>"],
     ["8", "NVDA", "$218.29", "$222.44", "+1.9% ⚠️", "09-05", "WATCH"],
     ["9", "<b>MELI</b>", "$1,897.37", "$1,900", "+0.1% 🔴", "07-02", "<b>STARTER</b>"]],
    [8 * mm, 20 * mm, 24 * mm, 24 * mm, 24 * mm, 20 * mm, W - 120 * mm],
    ["l", "l", "r", "r", "r", "l", "l"],
    hi={7: colors.HexColor("#eaf6f3"), 9: colors.HexColor("#fdeeee")}))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>NVDA 的 +1.9% 是假的。</b>$148–222 这个带建立在 owner earnings $182B 上,"
                   "而 Q2 FY27 10-Q(2026-08-26 报送)显示 H1 FCF 年化仅 <b>$140B</b>"
                   "(OCF/NI 63.1%、FCF/NI 59.3%)。<b>带本身要下修,粗算落到 $114–$171 区间。</b>", S["quote"]))

F.append(P("还差多少(按接近度)", "h2"))
far = [("ON", "−5.4%"), ("AXON", "−6.1%"), ("NFLX", "−8.9%"), ("GEHC", "−9.3%"), ("RMD", "−10.7%"),
       ("ABT", "−15.6%"), ("GEV", "−17.9%"), ("NBIS", "−19.8%"), ("NOVT", "−21.5%"), ("MSFT", "−23.5%"),
       ("HWM", "−24.2%"), ("META", "−25.9%"), ("TMO", "−26.2%"), ("TER", "−28.9%"), ("AMZN", "−29.9%"),
       ("AAPL", "−30.5%"), ("ORCL", "−32.8%"), ("MU", "−33.4%"), ("GEO", "−42.8%"), ("ASML", "−43.5%"),
       ("CXW", "−51.3%"), ("IREN", "−52.1%"), ("SNDK", "−52.9%"), ("TSLA", "−56.2%"),
       ("GOOGL", "−65.4%"), ("BFLY", "−68.9%")]
rows = [["名字", "差距", "名字", "差距", "名字", "差距"]]
for i in range(0, len(far), 3):
    ch = far[i:i + 3]
    r = []
    for n, g in ch:
        r += [("<b>%s</b>" % n) if n == "MSFT" else n, g]
    while len(r) < 6:
        r += ["", ""]
    rows.append(r)
cw = (W - 0) / 6
F.append(tbl(rows, [cw] * 6, ["l", "r", "l", "r", "l", "r"]))

# ---------- 4 pattern ----------
F.append(P("四、一个横跨全表的模式", "h1"))
F.append(P("<b>跌破 buy_below 越深,越要怀疑锚过期,而不是越兴奋。</b>", "p"))
F.append(P("线下最深的六个里有<b>四个是医疗器械</b>:SYK +32.8% · ISRG +22.4% · BSX +21.0% · EW +9.0%。"
           "卡全部来自 <b>_sp500_medical_2026-07-05</b> 批次,都是 7 月初写的,<b>全部没吃进 Q2 财报</b>。<br/>"
           "一整个板块同时跌穿自己的线,只有两种解释:板块级机会,或者那批卡写在板块顶上。"
           "SYK 和 ISRG 的 Q2 数据指向前者(利润率双双扩张),<b>但在刷新之前这是假设,不是结论</b>。", "p"))
F.append(P("本轮已验证的三个同形案例:", "p"))
F.append(tbl(
    [["名字", "现象"],
     ["GOOGL", "价格 −14%,但 owner earnings 跌得更多 → <b>没有产生安全边际</b>"],
     ["NVDA", "价格进带,但 OE 从 $182B → $140B → <b>带要下修</b>"],
     ["<b>MELI</b>", "价格正好到线,但营业利润率 17.2% → 9.7% → <b>线要下修</b>"]],
    [20 * mm, W - 20 * mm]))
F.append(Spacer(1, 4))
F.append(Paragraph("<b>这张表是「该去查什么」的清单,不是「可以买什么」的清单。</b>", S["quote"]))

# ---------- 5 order ----------
F.append(P("五、建议执行顺序", "h1"))
F.append(tbl(
    [["#", "动作", "理由"],
     ["<b>1</b>", "<b>INTU light refresh</b>",
      "封顶项已有正式文件(10-K,9/9)、价格在线内、verdict 已是 STARTER。"
      "<b>唯一一个跑完就能给出可执行答案的。</b>重点:把 FY2027 +9–10% 的减速指引打进 10y IRR"],
     ["<b>2</b>", "<b>MELI 重推 buy_below</b>",
      "营业利润率腰斩,$1,900 这条线已经不成立。<b>在重推前不要把它当「在线内」</b>"],
     ["3", "SYK + ISRG 刷新", "基本面 Q2 明显改善但卡没吃进;两家都在线下 20%+"],
     ["4", "ADBE 刷新", "CEO 解了、CFO 没解;ARR 回来但换了口径且增速 &lt; 营收 —— 需判断这是不是新的封顶理由"],
     ["5", "MSFT M6 重跑", "STARTER 卡已失效,现价越过自己的 8% IRR 线"],
     ["6", "NVDA band 重推", "OE $182B → $140B"],
     ["7", "医疗器械批次板块级复查", "四家同时跌穿线,先查是不是共同的分母变化"]],
    [8 * mm, 42 * mm, W - 50 * mm],
    hi={1: colors.HexColor("#eaf6f3")}))

# ---------- appendix ----------
F.append(P("附:数据来源与验证", "h1"))
F.append(P(
    "• <b>价格</b>:Yahoo Finance chart API,2026-09-11 收盘;<b>macro/market_panel/</b> 面板同步刷新至 2026-09-11<br/>"
    "• <b>通道</b>:scripts/log_trend_channel.py 重算<br/>"
    "• <b>一手财务</b>:SEC EDGAR data.sec.gov submissions + XBRL companyconcept API;各家 CIK 逐一核对,"
    "<b>仅采用卡日期之后报送</b>的 10-K / 10-Q / 8-K<br/>"
    "• <b>ADBE Q3 / INTU FY26 明细</b>:直接取自 8-K 的 EX-99 新闻稿原文<br/>"
    "• <b>未做</b>:六模块重跑、buy_below / IRR 重新推导、claim ledger 回挂", "p"))
F.append(Paragraph("本文件是<b>复查与比价</b>,不是 decision card。任何 verdict 变更须走各名 light refresh 流程。", S["quote"]))

SimpleDocTemplate(
    OUT_PDF, pagesize=A4,
    leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=18 * mm,
    title="STARTER 名单复查 2026-09-13", author="yc_research",
).build(F, onFirstPage=footer, onLaterPages=footer)

print("PDF ->", OUT_PDF, os.path.getsize(OUT_PDF), "bytes")
