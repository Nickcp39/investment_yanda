# -*- coding: utf-8 -*-
"""
房价分析三维度合订 PDF — 2026-07-25 云端会话
维度①收入比(PIR) ②售租比(P2R) ③名义绝对值
产出: output/房价三维度报告_2026-07.pdf (A4横版, matplotlib PdfPages, 图片内嵌)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams['font.family'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

A4L = (11.69, 8.27)
INK, MUT, ACC = '#1a1a1a', '#555', '#8a5a00'
BG = '#fcfcfb'

def text_page(pdf, title, blocks, footer=''):
    fig = plt.figure(figsize=A4L); fig.patch.set_facecolor(BG)
    fig.text(0.07, 0.92, title, fontsize=21, fontweight='bold', color=INK)
    y = 0.84
    for head, body in blocks:
        if head:
            fig.text(0.07, y, head, fontsize=13, fontweight='bold', color=ACC); y -= 0.045
        for line in body:
            fig.text(0.09, y, line, fontsize=10.5, color=INK); y -= 0.036
        y -= 0.022
    if footer:
        fig.text(0.07, 0.05, footer, fontsize=8, color=MUT)
    pdf.savefig(fig, facecolor=BG); plt.close(fig)

def img_page(pdf, title, img_path, notes, footer=''):
    fig = plt.figure(figsize=A4L); fig.patch.set_facecolor(BG)
    fig.text(0.05, 0.94, title, fontsize=16, fontweight='bold', color=INK)
    ax = fig.add_axes([0.03, 0.17, 0.94, 0.74]); ax.axis('off')
    ax.imshow(mpimg.imread(img_path))
    y = 0.125
    for line in notes:
        fig.text(0.06, y, line, fontsize=9.5, color=INK); y -= 0.032
    if footer:
        fig.text(0.05, 0.03, footer, fontsize=8, color=MUT)
    pdf.savefig(fig, facecolor=BG); plt.close(fig)

def img2_page(pdf, title, items, footer=''):
    fig = plt.figure(figsize=A4L); fig.patch.set_facecolor(BG)
    fig.text(0.05, 0.94, title, fontsize=16, fontweight='bold', color=INK)
    for i, (path, cap) in enumerate(items):
        ax = fig.add_axes([0.04 + i * 0.48, 0.24, 0.45, 0.62]); ax.axis('off')
        ax.imshow(mpimg.imread(path))
        fig.text(0.06 + i * 0.48, 0.19, cap, fontsize=9.5, color=INK, fontweight='bold')
    if footer:
        fig.text(0.05, 0.03, footer, fontsize=8, color=MUT)
    pdf.savefig(fig, facecolor=BG); plt.close(fig)

FOOT = 'investment_yanda/房价分析 · as_of 2026-07 · 数据出处与方法见 east_asia_pir_report.html 与各脚本头注'

with PdfPages('output/房价三维度报告_2026-07.pdf') as pdf:
    # ---- P1 封面/总结论 ----
    text_page(pdf, '中国房价往哪走 — 三维度跨国对比报告 (2026-07)', [
        ('方法', ['以各经济体房价峰值为 T=0 对齐(中国2021 · 加拿大2022 · 首尔2022 · 台北2024 · 旧金山2006 · 新加坡2008 · 东京1991),',
                  '三个独立维度互相校验: ①房价收入比(PIR) ②售租比(房价/年租金) ③名义房价绝对值。']),
        ('维度① 收入比 — 还高', ['深圳PIR 38→24, 京沪 25/24→18/17: 挤了5年泡沫后仍高于所有东亚样本的历史峰值;',
                  '下跌斜率≈日本同期。最像的对手=日本(唯一同海拔), 轨迹最像的西方样本=加拿大(同代见顶,无V型)。']),
        ('维度② 售租比 — 修复更慢', ['深圳售租比峰95(租金回报1.1%)≈美国2006泡沫顶的3倍; PIR已修复-38%但售租比只-26%,',
                  '因为租金在同跌 → 租金企稳是比房价环比更硬的底部信号。']),
        ('维度③ 名义绝对值 — 跌幅尚浅, 时间尚短', ['统计局链: 深-20% 广-24% 京-16% 沪-13%(挂牌口径普遍更深); 对照: 日本地价-63%(跌14年),',
                  '旧金山-46%后反弹至163, 首尔已创新高(110), 加拿大仍在阴跌(83-89)。',
                  '苗头: 2026年6月四城环比首次同步转正(+0.1~+0.4), 待连续确认。']),
        ('合成结论', ['中国 = 台湾式缓降斜率 × 日本式时间长度 × 新加坡式收入消化; PIR磨到12-15倍还需5-8年。',
                  '拐点三信号(同时成立才算底): 一线二手成交量连续12个月放大 + PIR<15 + 租金企稳。']),
    ], FOOT)
    # ---- P2 维度③ 绝对值(新) ----
    img_page(pdf, '维度③ 名义房价绝对值: 跌了多少, 跌了多久',
             'output/abs_price_aligned.png',
             ['读法: 全世界的名义房价最终都涨回去了(首尔110/旧金山163/新加坡172) — 除了还在下跌的中国与加拿大, 和永远没涨回来的日本(37)。',
              '中国现值 76-88, T+5斜率未收敛; 日本剧本: 名义价连跌14年才见底。中国若走台湾/新加坡路线, 则名义价横住、靠收入追。'], FOOT)
    # ---- P3 维度① 总览 ----
    img_page(pdf, '维度① 收入比(PIR): 东亚全样本, 峰值对齐',
             'output/pir_east_asia_aligned.png',
             ['中国一线(实线)对齐后仍在所有样本上方; 东京圈虚线是唯一同海拔先例: 峰后14年到谷。',
              '一对一拆解见下两页(按相似度排序: 日#1 加#2 台#3 韩#4 新#5 美#6)。'], FOOT)
    # ---- P4-P6 一对一 ----
    img2_page(pdf, '一对一 (1/3): #1 日本 · #2 加拿大',
              [('output/pir_cn_vs_jp.png', '#1 日本: 唯一同海拔; 教训是时间不是深度(14年)'),
               ('output/pir_cn_vs_ca.png', '#2 加拿大: 同代泡沫, 西方唯一没有V型(T+4仍-7%)')], FOOT)
    img2_page(pdf, '一对一 (2/3): #3 台湾 · #4 韩国',
              [('output/pir_cn_vs_tw.png', '#3 台北: 软着陆模板, 但起点差一倍(16.6 vs 24-38)'),
               ('output/pir_cn_vs_kr.png', '#4 首尔: 供给短缺+人口流入的V型, 中国学不了')], FOOT)
    img2_page(pdf, '一对一 (3/3): #5 新加坡 · #6 美国',
              [('output/pir_cn_vs_sg.png', '#5 新加坡: 名义价新高+PIR下降=收入消化18年(愿景图)'),
               ('output/pir_cn_vs_us.png', '#6 美国: 海拔完全不同(峰9.2), 参考价值最低')], FOOT)
    # ---- P7 维度② 售租比 ----
    img2_page(pdf, '维度② 售租比: 泡沫的另一把尺子',
              [('output/p2r_dumbbell.png', '11城 峰值vs现在: 深圳95→70, 修复慢于PIR'),
               ('output/p2r_china_trend.png', '中国四城2011-2026: 租金同跌拖慢售租比修复')], FOOT)
    # ---- P8 数据与口径 ----
    text_page(pdf, '附: 数据与口径备忘', [
        ('口径', ['中国=易居PIR锚+统计局70城二手链 · 韩=KB中位口径 · 台=内政部(2019改版) · 新=HDB/URA+SingStat',
                  '美=Case-Shiller+3%收入 · 日=不动产研究所(节点插值,估) · 加=Demographia中位数倍数+Teranet外推(估)',
                  '跨经济体绝对倍数受口径影响 → 比形状与相对高低, 不比绝对值。']),
        ('已知局限', ['台北2022-23为插值段; 多伦多2022峰10.5为转引口径(估); 日本1990售租比无一手数据(文献区间40-60);',
                  '加拿大2024-25中段为稳态假设。']),
        ('复现', ['build_east_asia_pir.py(维度①) · build_rent_charts.py(维度②) · build_abs_price.py(维度③) ·',
                  'build_canada_pair.py(加拿大) · build_pdf_report.py(本PDF) — 全部在 房价分析/ 目录, 数据在 data/。']),
    ], FOOT)
print('saved output/房价三维度报告_2026-07.pdf')
