import csv
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".pdf_deps")))

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
)
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing, String


BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(BASE, "..", "..", "output", "pdf"))
OUT_PDF = os.path.join(OUT_DIR, "SPY_QQQ五年滚动回报统计报告_2026-07-25.pdf")
FONT = r"C:\Windows\Fonts\simhei.ttf"

pdfmetrics.registerFont(TTFont("CN", FONT))

NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#4472C4")
ORANGE = colors.HexColor("#ED7D31")
LIGHT_BLUE = colors.HexColor("#D9EAF7")
LIGHT_GRAY = colors.HexColor("#F2F4F7")
DARK = colors.HexColor("#233142")
GREEN = colors.HexColor("#548235")
RED = colors.HexColor("#C00000")


def pct(value):
    return f"{value:.2%}"


def load_data():
    with open(os.path.join(BASE, "analysis_snapshot.json"), encoding="utf-8-sig") as f:
        summary = json.load(f)
    rows = []
    with open(os.path.join(BASE, "rolling_5y_2008_to_2026.csv"), encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            for key in ("StartYear", "EndYear"):
                row[key] = int(row[key])
            for key in ("ActualYears", "TotalReturn", "CAGR"):
                row[key] = float(row[key])
            rows.append(row)
    return summary, rows


summary, rolling = load_data()
by_ticker = defaultdict(list)
for item in rolling:
    by_ticker[item["Ticker"]].append(item)


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCN", fontName="CN", fontSize=22, leading=28, textColor=NAVY,
    alignment=TA_CENTER, spaceAfter=10
))
styles.add(ParagraphStyle(
    name="SubCN", fontName="CN", fontSize=10, leading=15, textColor=colors.HexColor("#5B6573"),
    alignment=TA_CENTER, spaceAfter=16
))
styles.add(ParagraphStyle(
    name="H1CN", fontName="CN", fontSize=15, leading=20, textColor=NAVY,
    spaceBefore=6, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="BodyCN", fontName="CN", fontSize=9.5, leading=15, textColor=DARK,
    alignment=TA_LEFT
))
styles.add(ParagraphStyle(
    name="SmallCN", fontName="CN", fontSize=7.5, leading=10, textColor=colors.HexColor("#5B6573")
))


def p(text, style="BodyCN"):
    return Paragraph(text, styles[style])


def styled_table(data, widths=None, percent_cols=None, font_size=8.3):
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    commands = [
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
    ]
    if percent_cols:
        for col in percent_cols:
            commands.append(("TEXTCOLOR", (col, 1), (col, -1), DARK))
    table.setStyle(TableStyle(commands))
    return table


def comparison_chart(rows, title, field="TotalReturn"):
    years = [f"{r['StartYear']}→{r['EndYear']}" for r in by_ticker["SPY"]]
    spy = [r[field] * 100 for r in by_ticker["SPY"]]
    qqq = [r[field] * 100 for r in by_ticker["QQQ"]]
    drawing = Drawing(245 * mm, 105 * mm)
    drawing.add(String(8 * mm, 98 * mm, title, fontName="CN", fontSize=12, fillColor=NAVY))
    chart = VerticalBarChart()
    chart.x = 14 * mm
    chart.y = 18 * mm
    chart.width = 216 * mm
    chart.height = 68 * mm
    chart.data = [spy, qqq]
    chart.categoryAxis.categoryNames = years
    chart.categoryAxis.labels.fontName = "CN"
    chart.categoryAxis.labels.fontSize = 6
    chart.categoryAxis.labels.angle = 45
    chart.categoryAxis.labels.dy = -10
    chart.valueAxis.valueMin = min(-20, int(min(spy + qqq) / 20) * 20)
    chart.valueAxis.valueMax = int(max(spy + qqq) / 50 + 1) * 50
    chart.valueAxis.valueStep = 50 if field == "TotalReturn" else 5
    chart.valueAxis.labels.fontName = "CN"
    chart.valueAxis.labels.fontSize = 7
    chart.bars[0].fillColor = BLUE
    chart.bars[1].fillColor = ORANGE
    chart.barWidth = 5
    chart.groupSpacing = 5
    drawing.add(chart)
    legend = Legend()
    legend.x = 105 * mm
    legend.y = 92 * mm
    legend.fontName = "CN"
    legend.fontSize = 8
    legend.colorNamePairs = [(BLUE, "SPY"), (ORANGE, "QQQ")]
    drawing.add(legend)
    return drawing


def line_chart(rows, title):
    years = [f"{r['StartYear']}" for r in by_ticker["SPY"]]
    spy = [r["CAGR"] * 100 for r in by_ticker["SPY"]]
    qqq = [r["CAGR"] * 100 for r in by_ticker["QQQ"]]
    drawing = Drawing(245 * mm, 105 * mm)
    drawing.add(String(8 * mm, 98 * mm, title, fontName="CN", fontSize=12, fillColor=NAVY))
    chart = HorizontalLineChart()
    chart.x = 14 * mm
    chart.y = 18 * mm
    chart.width = 216 * mm
    chart.height = 68 * mm
    chart.data = [spy, qqq]
    chart.categoryAxis.categoryNames = years
    chart.categoryAxis.labels.fontName = "CN"
    chart.categoryAxis.labels.fontSize = 7
    chart.valueAxis.labels.fontName = "CN"
    chart.valueAxis.labels.fontSize = 7
    chart.valueAxis.valueMin = min(-20, int(min(spy + qqq) / 5) * 5)
    chart.valueAxis.valueMax = int(max(spy + qqq) / 5 + 1) * 5
    chart.valueAxis.valueStep = 5
    chart.lines[0].strokeColor = BLUE
    chart.lines[0].strokeWidth = 2
    chart.lines[1].strokeColor = ORANGE
    chart.lines[1].strokeWidth = 2
    drawing.add(chart)
    legend = Legend()
    legend.x = 105 * mm
    legend.y = 92 * mm
    legend.fontName = "CN"
    legend.fontSize = 8
    legend.colorNamePairs = [(BLUE, "SPY"), (ORANGE, "QQQ")]
    drawing.add(legend)
    return drawing


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("CN", 7)
    canvas.setFillColor(colors.HexColor("#77808B"))
    canvas.drawString(15 * mm, 9 * mm, "数据来源：Yahoo Finance Chart API（adjusted close）")
    canvas.drawRightString(282 * mm, 9 * mm, f"第 {doc.page} 页")
    canvas.restoreState()


story = [
    p("SPY / QQQ 五年滚动回报统计报告", "TitleCN"),
    p("历史回测 | 数据截至 2026-07-24 | 复权收盘口径", "SubCN"),
    p("一、结论摘要", "H1CN"),
]

summary_table = [["区间", "ETF", "完整窗口", "平均累计回报", "中位累计回报", "最低", "最高", "平均 CAGR"]]
for label, key in [("近30年/全部历史", "Rolling30YearStats"), ("2008年至今", "RollingSince2008Stats")]:
    for ticker in ("SPY", "QQQ"):
        s = summary[ticker][key]
        summary_table.append([
            label, ticker, str(s["CompleteWindowCount"]), pct(s["AverageTotalReturn"]),
            pct(s["MedianTotalReturn"]), pct(s["MinimumTotalReturn"]),
            pct(s["MaximumTotalReturn"]), pct(s["AverageCAGR"])
        ])
story += [
    styled_table(summary_table, [35*mm, 14*mm, 20*mm, 27*mm, 27*mm, 20*mm, 20*mm, 24*mm]),
    Spacer(1, 8*mm),
    p("2008 年末以来，SPY 的完整五年窗口平均累计回报为 94.33%，QQQ 为 145.27%。"
      "两者所有完整窗口均为正收益，但这段样本集中于金融危机后的长期牛市，不能直接作为未来回报预测。"),
    Spacer(1, 4*mm),
    p("当前未完成窗口（2021 年末至 2026-07-24）不进入上述平均值："
      "SPY 累计回报 65.35%、按实际天数计算 CAGR 11.66%；"
      "QQQ 累计回报 76.79%、CAGR 13.31%。"),
    Spacer(1, 4*mm),
    p("整体持有期：SPY 最近约 30 年累计回报 1,854.13%、CAGR 10.42%；"
      "QQQ 自 1999-03-10 成立以来累计回报 1,490.23%、CAGR 10.63%。"
      "QQQ 不具备完整 30 年实盘历史。"),
    Spacer(1, 7*mm),
    p("口径说明", "H1CN"),
    p("五年窗口采用起始年最后交易日到五年后最后交易日；累计回报 = 结束复权价 ÷ 起始复权价 - 1；"
      "CAGR 根据实际经过天数计算。adjusted close 用于反映拆股及现金分红调整。"),
    PageBreak(),
    p("二、2008 年以来五年累计总回报对比", "H1CN"),
    comparison_chart(rolling, "逐年五年窗口累计总回报（%）"),
    p("图中最后一组 2021→2026 为截至 2026-07-24 的未完成窗口，仅用于跟踪，不纳入完整窗口统计。", "SmallCN"),
    PageBreak(),
    p("三、五年窗口年化回报走势", "H1CN"),
    line_chart(rolling, "逐年五年窗口 CAGR（%）"),
    PageBreak(),
    p("四、逐年窗口明细", "H1CN"),
]

detail = [["窗口", "SPY 累计", "SPY CAGR", "QQQ 累计", "QQQ CAGR", "状态"]]
spy_map = {r["StartYear"]: r for r in by_ticker["SPY"]}
qqq_map = {r["StartYear"]: r for r in by_ticker["QQQ"]}
for year in sorted(spy_map):
    s = spy_map[year]
    q = qqq_map[year]
    status = "未满五年" if "Partial" in s["Status"] else "完整"
    detail.append([
        f"{year}→{year+5}", pct(s["TotalReturn"]), pct(s["CAGR"]),
        pct(q["TotalReturn"]), pct(q["CAGR"]), status
    ])
story += [
    styled_table(detail, [34*mm, 30*mm, 27*mm, 30*mm, 27*mm, 28*mm], font_size=8.5),
    Spacer(1, 6*mm),
    p("注意：滚动窗口高度重叠，相邻行共享四年的持有期，因此这些观测并非相互独立。"
      "最高、最低和平均值应视为历史描述，而非未来概率分布。"),
    Spacer(1, 5*mm),
    p("五、数据与风险提示", "H1CN"),
    p("数据来源 URL：https://query1.finance.yahoo.com/v8/finance/chart/SPY 与 /QQQ；"
      "复权定义参考：https://help.yahoo.com/kb/SLN28256.html。"
      "报告不包含当前年度或 2027 年预测；预测应在历史结果确认后，以估值、盈利增长、利率和风险情景为单独假设。"),
]

os.makedirs(OUT_DIR, exist_ok=True)
doc = SimpleDocTemplate(
    OUT_PDF, pagesize=landscape(A4), rightMargin=14*mm, leftMargin=14*mm,
    topMargin=13*mm, bottomMargin=15*mm, title="SPY / QQQ 五年滚动回报统计报告",
    author="OpenAI Codex"
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("PDF report generated successfully.")
