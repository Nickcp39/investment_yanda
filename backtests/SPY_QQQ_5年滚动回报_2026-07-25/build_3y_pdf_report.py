import csv
import json
import os
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, ".pdf_deps"))

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing, String

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, "output", "pdf")
OUT_PDF = os.path.join(OUT_DIR, "SPY_QQQ三年滚动回报统计报告_2026-07-25.pdf")

pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\simhei.ttf"))
NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#4472C4")
ORANGE = colors.HexColor("#ED7D31")
LIGHT_GRAY = colors.HexColor("#F2F4F7")
DARK = colors.HexColor("#233142")

with open(os.path.join(BASE, "analysis_3y_snapshot.json"), encoding="utf-8-sig") as f:
    summary = json.load(f)

rows = []
with open(os.path.join(BASE, "rolling_3y_2008_to_2026.csv"), encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        row["StartYear"] = int(row["StartYear"])
        row["EndYear"] = int(row["EndYear"])
        row["TotalReturn"] = float(row["TotalReturn"])
        row["CAGR"] = float(row["CAGR"])
        rows.append(row)

by_ticker = defaultdict(list)
for row in rows:
    by_ticker[row["Ticker"]].append(row)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCN", fontName="CN", fontSize=22, leading=28,
                          textColor=NAVY, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name="SubCN", fontName="CN", fontSize=10, leading=15,
                          textColor=colors.HexColor("#5B6573"), alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="H1CN", fontName="CN", fontSize=15, leading=20,
                          textColor=NAVY, spaceBefore=6, spaceAfter=8))
styles.add(ParagraphStyle(name="BodyCN", fontName="CN", fontSize=9.5, leading=15,
                          textColor=DARK, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="SmallCN", fontName="CN", fontSize=7.5, leading=10,
                          textColor=colors.HexColor("#5B6573")))


def p(text, style="BodyCN"):
    return Paragraph(text, styles[style])


def pct(value):
    return f"{value:.2%}"


def table(data, widths, font_size=8.3):
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, -1), "CN"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("LEADING", (0, 0), (-1, -1), font_size + 3),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#C7CDD4")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def bar_chart():
    labels = [f"{r['StartYear']}→{r['EndYear']}" for r in by_ticker["SPY"]]
    spy = [r["TotalReturn"] * 100 for r in by_ticker["SPY"]]
    qqq = [r["TotalReturn"] * 100 for r in by_ticker["QQQ"]]
    d = Drawing(245 * mm, 112 * mm)
    d.add(String(8 * mm, 104 * mm, "逐年三年窗口累计总回报（%）",
                 fontName="CN", fontSize=12, fillColor=NAVY))
    c = VerticalBarChart()
    c.x, c.y, c.width, c.height = 14*mm, 20*mm, 216*mm, 70*mm
    c.data = [spy, qqq]
    c.categoryAxis.categoryNames = labels
    c.categoryAxis.labels.fontName = "CN"
    c.categoryAxis.labels.fontSize = 5.7
    c.categoryAxis.labels.angle = 45
    c.categoryAxis.labels.dy = -10
    c.valueAxis.valueMin = min(-20, int(min(spy + qqq) / 20) * 20)
    c.valueAxis.valueMax = int(max(spy + qqq) / 50 + 1) * 50
    c.valueAxis.valueStep = 50
    c.valueAxis.labels.fontName = "CN"
    c.valueAxis.labels.fontSize = 7
    c.bars[0].fillColor = BLUE
    c.bars[1].fillColor = ORANGE
    c.barWidth = 4.5
    c.groupSpacing = 4
    d.add(c)
    legend = Legend()
    legend.x, legend.y = 105*mm, 98*mm
    legend.fontName, legend.fontSize = "CN", 8
    legend.colorNamePairs = [(BLUE, "SPY"), (ORANGE, "QQQ")]
    d.add(legend)
    return d


def line_chart():
    labels = [str(r["StartYear"]) for r in by_ticker["SPY"]]
    spy = [r["CAGR"] * 100 for r in by_ticker["SPY"]]
    qqq = [r["CAGR"] * 100 for r in by_ticker["QQQ"]]
    d = Drawing(245 * mm, 112 * mm)
    d.add(String(8 * mm, 104 * mm, "逐年三年窗口 CAGR（%）",
                 fontName="CN", fontSize=12, fillColor=NAVY))
    c = HorizontalLineChart()
    c.x, c.y, c.width, c.height = 14*mm, 20*mm, 216*mm, 70*mm
    c.data = [spy, qqq]
    c.categoryAxis.categoryNames = labels
    c.categoryAxis.labels.fontName = "CN"
    c.categoryAxis.labels.fontSize = 6.5
    c.valueAxis.valueMin = int(min(spy + qqq) / 10) * 10
    c.valueAxis.valueMax = int(max(spy + qqq) / 10 + 1) * 10
    c.valueAxis.valueStep = 10
    c.valueAxis.labels.fontName = "CN"
    c.valueAxis.labels.fontSize = 7
    c.lines[0].strokeColor, c.lines[0].strokeWidth = BLUE, 2
    c.lines[1].strokeColor, c.lines[1].strokeWidth = ORANGE, 2
    d.add(c)
    legend = Legend()
    legend.x, legend.y = 105*mm, 98*mm
    legend.fontName, legend.fontSize = "CN", 8
    legend.colorNamePairs = [(BLUE, "SPY"), (ORANGE, "QQQ")]
    d.add(legend)
    return d


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("CN", 7)
    canvas.setFillColor(colors.HexColor("#77808B"))
    canvas.drawString(15*mm, 9*mm, "数据来源：Yahoo Finance Chart API（adjusted close）")
    canvas.drawRightString(282*mm, 9*mm, f"第 {doc.page} 页")
    canvas.restoreState()


summary_table = [["区间", "ETF", "完整窗口", "平均累计回报", "中位累计回报", "最低", "最高", "平均 CAGR"]]
for label, key in [("近30年/全部历史", "History"), ("2008年至今", "Since2008")]:
    for ticker in ("SPY", "QQQ"):
        s = summary[ticker][key]
        summary_table.append([
            label, ticker, str(s["CompleteWindowCount"]), pct(s["AverageTotalReturn"]),
            pct(s["MedianTotalReturn"]), pct(s["MinimumTotalReturn"]),
            pct(s["MaximumTotalReturn"]), pct(s["AverageCAGR"])
        ])

story = [
    p("SPY / QQQ 三年滚动回报统计报告", "TitleCN"),
    p("三年窗口复算 | 数据截至 2026-07-24 | 复权收盘口径", "SubCN"),
    p("一、结论摘要", "H1CN"),
    table(summary_table, [35*mm, 14*mm, 20*mm, 27*mm, 27*mm, 20*mm, 20*mm, 24*mm]),
    Spacer(1, 7*mm),
    p("结论：AI 行情在三年窗口中非常明显。最新完整窗口 2022 年末→2025 年末，"
      "SPY 累计回报 85.50%、CAGR 22.84%；QQQ 累计回报 134.86%、CAGR 32.88%。"
      "两者均显著高于 2008 年以来三年窗口平均 CAGR（SPY 13.98%、QQQ 19.39%）。"),
    Spacer(1, 4*mm),
    p("为什么此前五年窗口看起来没有想象中强？因为五年窗口从 2021 年末高位起算，"
      "完整包含了 2022 年科技股回撤。它把 2023 年以来的 AI 主升浪与前期下跌合并，形成明显的高基数效应。"
      "三年窗口从 2022 年末低位起算，更直接捕捉了 AI 行情。"),
    Spacer(1, 4*mm),
    p("当前未完成三年窗口 2023 年末→2026-07-24：SPY 累计 60.15%、CAGR 20.13%；"
      "QQQ 累计 69.33%、CAGR 22.76%。仍然高于各自长期三年窗口平均 CAGR。"),
    Spacer(1, 7*mm),
    p("方法说明", "H1CN"),
    p("每个窗口按起始年最后交易日到三年后最后交易日计算；累计回报 = 结束复权价 ÷ 起始复权价 - 1；"
      "CAGR 按实际经过天数计算。2023→2026 尚未满三年，单列且不进入完整窗口统计。"),
    PageBreak(),
    p("二、2008 年以来三年累计回报对比", "H1CN"),
    bar_chart(),
    p("最后一组 2023→2026 为截至 2026-07-24 的未完成窗口。", "SmallCN"),
    PageBreak(),
    p("三、三年窗口年化回报走势", "H1CN"),
    line_chart(),
    PageBreak(),
    p("四、逐年三年窗口明细", "H1CN"),
]

detail = [["窗口", "SPY 累计", "SPY CAGR", "QQQ 累计", "QQQ CAGR", "状态"]]
spy_map = {r["StartYear"]: r for r in by_ticker["SPY"]}
qqq_map = {r["StartYear"]: r for r in by_ticker["QQQ"]}
for year in sorted(spy_map):
    s, q = spy_map[year], qqq_map[year]
    status = "未满三年" if "Partial" in s["Status"] else "完整"
    detail.append([
        f"{year}→{year+3}", pct(s["TotalReturn"]), pct(s["CAGR"]),
        pct(q["TotalReturn"]), pct(q["CAGR"]), status
    ])
story += [
    table(detail, [34*mm, 30*mm, 27*mm, 30*mm, 27*mm, 28*mm], font_size=7.8),
    Spacer(1, 4*mm),
    p("解读限制：三年滚动窗口同样高度重叠，相邻窗口共享两年的回报，不能视为独立样本。"
      "2022 年末是回撤后的低基数，因此 2022→2025 的强劲结果同时包含估值修复与 AI 盈利预期扩张。"),
    Spacer(1, 4*mm),
    p("五、判断", "H1CN"),
    p("三年结果并不支持“当前 QQQ/SPY 表现偏低”的判断。相反，最近完整三年属于历史偏强区间，"
      "QQQ 的强度尤其突出。2026 年至今仍为正回报，但是否低估不能仅靠历史回报判断，"
      "还需要结合当前估值、盈利增速、利率和大型科技股集中度。"),
]

os.makedirs(OUT_DIR, exist_ok=True)
doc = SimpleDocTemplate(
    OUT_PDF, pagesize=landscape(A4), rightMargin=14*mm, leftMargin=14*mm,
    topMargin=13*mm, bottomMargin=15*mm, title="SPY / QQQ 三年滚动回报统计报告",
    author="OpenAI Codex"
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Three-year PDF report generated successfully.")
