# -*- coding: utf-8 -*-
"""生成"锁类型 vs 超额收益"SVG 图（纯 Python 手写 SVG，无外部依赖）"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (标签, 超额pp, 锁类型, 区间)
# 锁类型: L=带锁(售后/寡头/转换成本)  W=窗口稀缺  B=裸铲子
data = [
    ("TransDigm 专有件", 17.1, "L", "2006-26"),
    ("Howmet 专有件", 19.1, "L", "2016-26"),
    ("Hubbell 电网设备", 11.9, "L", "1985-26"),
    ("AMAT 半导体设备", 11.1, "L", "1985-26"),
    ("卡特彼勒 挖矿设备", 6.6, "L", "1985-26"),
    ("小松 挖矿设备", 6.5, "L", "1999-26"),
    ("伊顿 Eaton 电网", 5.6, "L", "1985-26"),
    ("RTX(Pratt) 发动机", 3.4, "L", "1985-26"),
    ("GE Aerospace 发动机", 1.9, "L", "1970-26"),
    ("赛峰 Safran 发动机", 1.9, "L", "1999-26"),
    ("康宁 Corning", 2.8, "L", "1985-26"),
    ("三星重工 造船", 0.4, "B", "1999-26"),
    ("麦格纳 汽配", -0.3, "B", "1985-26"),
    ("Enphase 逆变器", -1.3, "B", "2012-26"),
    ("韩华海洋(大宇) 造船", -2.6, "B", "2001-26"),
    ("NOV 钻井设备", -2.7, "B", "1996-26"),
    ("贝克休斯 油服", -2.8, "B", "1987-26"),
    ("斯伦贝谢 油服", -2.9, "B", "1985-26"),
    ("哈里伯顿 油服", -3.6, "B", "1985-26"),
    ("Ciena 光网络", -4.7, "B", "1997-26"),
    ("安波福(德尔福) 汽配", -5.8, "B", "2011-26"),
    ("SolarEdge 逆变器", -8.1, "B", "2015-26"),
]

# 窗口稀缺单独一列（当前超额大，但历史结局归零）
window = [
    ("GEV 燃气轮机", 100.1, "2024-26*"),
    ("Vertiv 散热", 36.8, "2018-26"),
    ("西门子能源", 20.6, "2020-26"),
    ("思科 Cisco", 14.2, "1990-26"),
    ("三菱重工 燃机", 4.8, "1999-26"),
]

COLOR = {"L": "#1a7f4d", "B": "#c0392b", "W": "#d68910"}

# 布局参数
W = 920
row_h = 30
top = 70
left = 300
plot_w = 520
x0 = left + plot_w / 2  # 0 轴位置
scale = plot_w / 2 / 22.0  # 22pp 对应半宽（截断 GEV）

rows = []
y = top
# 先画带锁（上半），再画裸铲子（下半）
locked = [d for d in data if d[2] == "L"]
bare = [d for d in data if d[2] == "B"]
ordered = locked + bare

max_pp = 22
def x_of(pp):
    pp = max(-max_pp, min(max_pp, pp))
    return x0 + pp * scale

parts = []
# 标题
parts.append(f'<text x="{W/2}" y="34" font-size="20" font-weight="bold" text-anchor="middle" fill="#1a1a1a">铲子百年实证 · 超额收益（相对标普500，年化 pp）</text>')
parts.append(f'<text x="{W/2}" y="54" font-size="12" text-anchor="middle" fill="#666">带锁的铲子（售后/寡头/转换成本）为正 · 裸铲子（可替换承包商）为负 · 判据：客户明天能否换一家买</text>')

ys = {}
for d in ordered:
    label, pp, lock, rng = d
    x = x_of(pp)
    color = COLOR[lock]
    y1 = y - row_h + 8
    # bar
    if pp >= 0:
        parts.append(f'<rect x="{x0}" y="{y1}" width="{x-x0:.1f}" height="{row_h-10}" fill="{color}" rx="2"/>')
    else:
        parts.append(f'<rect x="{x:.1f}" y="{y1}" width="{x0-x:.1f}" height="{row_h-10}" fill="{color}" rx="2"/>')
    # label
    parts.append(f'<text x="{left-10}" y="{y}" font-size="12" text-anchor="end" fill="#333">{label}</text>')
    # value
    vx = x + 6 if pp >= 0 else x - 6
    anchor = "start" if pp >= 0 else "end"
    parts.append(f'<text x="{vx}" y="{y}" font-size="11" text-anchor="{anchor}" fill="{color}">{pp:+.1f}</text>')
    # range
    parts.append(f'<text x="{W-10}" y="{y}" font-size="10" text-anchor="end" fill="#999">{rng}</text>')
    y += row_h

# 零轴
parts.append(f'<line x1="{x0}" y1="{top-10}" x2="{x0}" y2="{y}" stroke="#aaa" stroke-width="1"/>')
# 轴刻度
for v in [-20, -15, -10, -5, 0, 5, 10, 15, 20]:
    x = x_of(v)
    parts.append(f'<line x1="{x:.1f}" y1="{top-16}" x2="{x:.1f}" y2="{top-10}" stroke="#999"/>')
    parts.append(f'<text x="{x:.1f}" y="{top-22}" font-size="10" text-anchor="middle" fill="#888">{v}pp</text>')

# 图例
ly = y + 16
parts.append(f'<rect x="{left}" y="{ly}" width="14" height="14" fill="{COLOR["L"]}" rx="2"/>')
parts.append(f'<text x="{left+20}" y="{ly+12}" font-size="12" fill="#333">带锁的铲子（售后锁定/寡头/转换成本）</text>')
parts.append(f'<rect x="{left+330}" y="{ly}" width="14" height="14" fill="{COLOR["B"]}" rx="2"/>')
parts.append(f'<text x="{left+350}" y="{ly+12}" font-size="12" fill="#333">裸铲子（可替换承包商）</text>')

# 底部注释：窗口稀缺
ny = ly + 34
parts.append(f'<text x="{left}" y="{ny}" font-size="12" fill="{COLOR["W"]}">窗口稀缺（当前超额最大，历史结局归零）：</text>')
nx = left + 340
for label, pp, rng in window:
    parts.append(f'<text x="{nx}" y="{ny}" font-size="12" fill="{COLOR["W"]}">{label} {pp:+.0f}pp</text>')
    nx += 190
    if nx > W - 10:
        nx = left + 340
        ny += 18

H = ny + 30
parts.append(f'<text x="{left}" y="{H-8}" font-size="10" fill="#999">* GEV 仅 2024 拆分至今 2.5 年样本；HD现代重工 2021 分拆上市样本过短未列。超额 = 标的全期 CAGR − 同期标普500 CAGR。国际股本币口径。</text>')

svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Segoe UI, Microsoft YaHei, sans-serif" background="#ffffff">\n'
svg += '<rect width="100%" height="100%" fill="#ffffff"/>\n'
svg += "\n".join(parts)
svg += "\n</svg>"

out = os.path.join(BASE, "fig1_excess_return_by_lock.svg")
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print("Saved ->", out)
print("size", W, "x", H)
