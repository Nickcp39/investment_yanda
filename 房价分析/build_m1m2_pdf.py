# -*- coding: utf-8 -*-
"""
剪刀差与房价走势 · 跨国一对一对比 PDF — 2026-07-26 云端会话
以中国为base(每页=中国+一个对手),按各自房价峰值 T=0 对齐(参考 PIR 一对一系列):
  中国 T0=2021 · 日本 T0=1991 · 美国 T0=2006 · 韩国 T0=2022
每页四条序列: 中国剪刀差(红线) + 中国一线房价同比(蓝柱); 对手货币指标(深灰虚线) + 对手房价同比(灰阶柱)
产出: output/剪刀差跨国对比_2026-07.pdf
"""
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

sys.path.insert(0, 'data')
from anchors_and_chains import CN_DEC_YOY, CN_2026_JUN_YOY
from m1m2_anchors import CN, CN_HP_EARLY, US_M2, KR, JP_M2CD, JP_LAND

plt.rcParams['font.family'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

A4L = (11.69, 8.27)
BG = '#fcfcfb'; INK = '#1a1a1a'; MUT = '#777'; ACC = '#8a5a00'
CN_RED = '#e34948'; CN_BAR = '#cfe0f5'; OP_LN = '#444444'; OP_BAR = '#d9d4c8'

# ---------- 序列组装 ----------
cn_hp = dict(CN_HP_EARLY)
for y in range(2015, 2026):
    cn_hp[y] = np.mean([CN_DEC_YOY[y][c] - 100 for c in ['深圳', '北京', '上海', '广州']])
cn_hp[2026] = np.mean([CN_2026_JUN_YOY[c] - 100 for c in ['深圳', '北京', '上海', '广州']])
cn_sc = {y: v[0] - v[1] for y, v in CN.items() if isinstance(y, int)}
cn_sc[2026] = CN[2026.5][0] - CN[2026.5][1]   # 2026H1硬锚(-4.0)
CN_T0 = 2021

cs = pd.read_csv('data/us_case_shiller.csv', parse_dates=['Date'])
nat = cs[['Date', 'National-US']].dropna(); nat['y'] = nat['Date'].dt.year
dec = nat[nat['Date'].dt.month == 12].set_index('y')['National-US']
us_hp = {int(y): float(dec[y] / dec[y - 1] * 100 - 100) for y in dec.index if y - 1 in dec.index}
US_T0 = 2006

kb = pd.read_csv('data/kr_kb_seoul_apt_index.csv', dtype={'date': str})
kb['y'] = kb['date'].str[:4].astype(int); kb['m'] = kb['date'].str[4:6].astype(int)
kdec = kb[kb['m'] == 12].set_index('y')['idx'].astype(float)
kr_hp = {int(y): float(kdec[y] / kdec[y - 1] * 100 - 100) for y in kdec.index if y - 1 in kdec.index}
kr_m1 = {y: v[0] for y, v in KR.items()}
KR_T0 = 2022
JP_T0 = 1991

def rel(d, t0, lo=-6, hi=6):
    return {y - t0: v for y, v in d.items() if isinstance(y, (int, float)) and lo <= y - t0 <= hi}

def pair_page(pdf, opp_name, opp_money, opp_money_lbl, opp_hp, opp_t0,
              title, subtitle, notes):
    fig, ax = plt.subplots(figsize=A4L, dpi=150)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    c_sc = rel(cn_sc, CN_T0); c_hp = rel(cn_hp, CN_T0)
    o_m = rel(opp_money, opp_t0); o_hp = rel(opp_hp, opp_t0)
    ks = sorted(c_hp)
    ax.bar([k - 0.2 for k in ks], [c_hp[k] for k in ks], width=0.38, color=CN_BAR,
           label=f'中国 一线房价同比 (T0={CN_T0})', zorder=2)
    ks = sorted(o_hp)
    ax.bar([k + 0.2 for k in ks], [o_hp[k] for k in ks], width=0.38, color=OP_BAR,
           label=f'{opp_name} 房价同比 (T0={opp_t0})', zorder=2)
    ks = sorted(c_sc)
    ax.plot(ks, [c_sc[k] for k in ks], color=CN_RED, lw=2.6, marker='o', ms=4,
            label='中国 M1-M2剪刀差', zorder=4)
    ks = sorted(o_m)
    ax.plot(ks, [o_m[k] for k in ks], color=OP_LN, lw=2.2, ls='--', marker='s', ms=3.5,
            label=f'{opp_name} {opp_money_lbl}', zorder=3)
    ax.axvline(0, color='#999', lw=1.0, ls=':')
    ax.text(0.06, 0.965, 'T=0 = 各自房价峰值', transform=ax.transAxes, fontsize=8, color=MUT)
    ax.axhline(0, color='#999', lw=0.7)
    ax.set_xlim(-6.5, 6.5); ax.set_ylim(-30, 35)
    ax.set_xticks(range(-6, 7))
    ax.set_xlabel('距各自房价峰值的年数', fontsize=11)
    ax.set_ylabel('年同比 / 百分点', fontsize=11)
    ax.set_title(title, fontsize=15, fontweight='bold', pad=30, loc='left')
    ax.text(0, 1.022, subtitle, transform=ax.transAxes, fontsize=9.5, color=MUT)
    ax.legend(fontsize=9, loc='lower left', framealpha=0.9)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', color='#e8e8e4', lw=0.7)
    y0 = 0.055
    for i, line in enumerate(notes):
        fig.text(0.09, y0 - i * 0.026, line, fontsize=8.5, color=INK)
    plt.tight_layout(rect=[0, 0.06 + 0.026 * (len(notes) - 1), 1, 1])
    pdf.savefig(fig, facecolor=BG); plt.close(fig)

with PdfPages('output/剪刀差跨国对比_2026-07.pdf') as pdf:
    # ---- P1 封面/结论 ----
    fig = plt.figure(figsize=A4L); fig.patch.set_facecolor(BG)
    fig.text(0.07, 0.90, '剪刀差与房价 · 跨国一对一对比 (以中国为base)', fontsize=20, fontweight='bold', color=INK)
    fig.text(0.07, 0.855, 'T=0 = 各自房价峰值 (中国2021 · 日本1991 · 美国2006 · 韩国2022) · as_of 2026-07', fontsize=10, color=MUT)
    blocks = [
        ('核心结论', [
            '1. M2总量无用: 中国 M2→房价 r=0.45; 美国≤2019 r≈0.28。印钱多≠房价涨。',
            '2. M1(剪刀差)才是温度计: 中国剪刀差同步 r=0.81(最好单一指标); 韩国 M1 与首尔V型同步 r=0.63-0.77。',
            '3. 2021年后中国 M2 彻底失效(M2 +11.8% 房价照跌) — 正是日本1992"M2失速→流动性陷阱"的镜像;',
            '   但剪刀差仍有效(lead1 r=0.74): 2024剪刀差最深(-8.7) → 2025房价最深; 2025收窄(-3.1) → 2026H1环比转正。',
            '4. 拐点信号清单(第四条为本轮新增): 成交量连续12月放大 + PIR<15 + 租金企稳 + M1/剪刀差连续回升。',
        ]),
        ('相关性一览 (年度分辨率)', [
            '中国: 剪刀差 r=0.81(同步) | M1 r=0.78 | M2 r=0.45 | 2021后剪刀差 lead1 r=0.74',
            '美国: M2 全样本 lead1 r=0.42(全靠2020-21极端值); ≤2019 r=-0.19~0.28 ≈ 无信号',
            '韩国: M1 r=0.63 | M2 r=0.77(同步)',
            '日本: 文献叙事 — M2+CD 11.7%→0.6%(1990→92), 地价连跌14年',
        ]),
        ('口径备忘', [
            '货币=锚点法(硬锚+估, 见 data/m1m2_anchors.py; 本环境宏观API被阻断, 待本地FRED月度校准);',
            '房价=仓库硬数据(统计局70城链/Case-Shiller/KB)。中国2007-14房价、日本地价为叙事锚(估)。',
        ]),
    ]
    y = 0.79
    for head, lines in blocks:
        fig.text(0.07, y, head, fontsize=13, fontweight='bold', color=ACC); y -= 0.042
        for ln in lines:
            fig.text(0.09, y, ln, fontsize=10, color=INK); y -= 0.034
        y -= 0.020
    fig.text(0.07, 0.04, 'investment_yanda/房价分析 · 姊妹篇: 房价三维度报告_2026-07.pdf (PIR/售租比/绝对值)', fontsize=8, color=MUT)
    pdf.savefig(fig, facecolor=BG); plt.close(fig)

    # ---- P2 中国 vs 日本 ----
    pair_page(pdf, '日本', JP_M2CD, 'M2+CD同比(文献)', JP_LAND, JP_T0,
        '① 中国 vs 日本(1991): 唯一在货币层面也走同一剧本的对手',
        '日本: M2+CD 从 T-1 的 +11.7% 失速到 T+1 的 +0.6%, 地价从 T=0 起连跌14年 | 日本地价为文献锚(估)',
        ['读法: 日本货币失速发生在峰值前后一年内、又快又深, 之后再宽松也无效(流动性陷阱);',
         '中国剪刀差从 T-5(2016 +10.1) 一路走低到 T+3(2024 -8.7), 是"慢版日本" — 失速更缓, 但方向相同;',
         '关键差异: 中国 T+4(2025)剪刀差开始收窄, 对应日本从未出现过的"T+4边际改善" — 这是两条曲线的分岔点候选。'])

    # ---- P3 中国 vs 美国 ----
    pair_page(pdf, '美国', {y: v for y, v in US_M2.items() if isinstance(y, int)}, 'M2同比', us_hp, US_T0,
        '② 中国 vs 美国(2006): 货币担不了责的崩盘, 和货币退不了烧的下跌',
        '美国2008是信贷/杠杆崩盘, M2当时还在+6~10%照常增长 — 货币指标完全没预警 | CS National 12月同比(硬数据)',
        ['读法: 美国房价 T+0~T+5 深跌时 M2始终为正 → 美国的崩盘不是货币现象, 是信贷结构现象(次贷);',
         '所以M2在美国平时无信号(≤2019 r≈-0.19~0.28), 只有2020 +24.8% 那种极端脉冲才有用(→2021房价+18%);',
         '对照中国: 中国的下跌与货币(M1)同步性极高 — 中国是"意愿型"下跌(没人肯花钱), 美国是"能力型"崩盘(还不起贷)。'])

    # ---- P4 中国 vs 韩国 ----
    pair_page(pdf, '韩国', kr_m1, 'M1同比', kr_hp, KR_T0,
        '③ 中国 vs 韩国(2022): 同代见顶, M1同摆, 两种幅度',
        '韩国 M1: 2020 +26 → 2023 -10 (2021-23为OECD硬锚), 与首尔急跌25%后V型收复同步 | KB指数12月同比(硬数据)',
        ['读法: 韩国 M1 摆幅(+26→-10)远大于中国(+8.6→-1.4), 房价反应也更剧烈(急跌急回) — 高杠杆+浮动利率放大器;',
         '韩国证明 M1 的方向变化几乎实时映射房价方向变化(同步 r=0.63), 与中国结论一致;',
         '中国的钝化版本: 摆幅小、反应慢, 但方向规律相同 — 2025-26 中国 M1 回升对应的应是"钝化版企稳", 不是首尔式V型。'])

    # ---- P5 中国 base 全景(日历时间) ----
    fig, ax = plt.subplots(figsize=A4L, dpi=150)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    yrs = sorted(y for y in cn_sc if y in cn_hp)
    ax.bar(yrs, [cn_hp[y] for y in yrs], color=CN_BAR, width=0.7, label='一线四城房价年同比')
    ax.plot(yrs, [cn_sc[y] for y in yrs], color=CN_RED, lw=2.6, marker='o', ms=4, label='M1-M2剪刀差')
    for y_, txt, dy in [(2009, '四万亿\n剪刀差+4.7', 6), (2016, '棚改+去库存\n剪刀差+10.1', 3),
                        (2021, '房价见顶', 8), (2024, '剪刀差最深-8.7', -4), (2026, 'M1回升中', 5)]:
        if y_ in cn_sc:
            ax.annotate(txt, (y_, cn_sc[y_]), textcoords='offset points', xytext=(0, dy * 4),
                        fontsize=8, color=ACC, ha='center')
    ax.axvspan(2020.5, 2026.6, color='#f4d47c', alpha=0.15)
    ax.axhline(0, color='#999', lw=0.7)
    ax.set_xlim(2006.3, 2027); ax.set_ylim(-30, 35)
    ax.set_xlabel('年份', fontsize=11); ax.set_ylabel('年同比 / 百分点', fontsize=11)
    ax.set_title('④ 中国 base 全景(2007-2026): 三轮剪刀差张开=三轮房价上行, 2021后进入负剪刀差长区间',
                 fontsize=14.5, fontweight='bold', pad=28, loc='left')
    ax.text(0, 1.022, '2007-14房价为叙事锚(估), 2015起为统计局链(硬) | 2024起M1新口径', transform=ax.transAxes, fontsize=9, color=MUT)
    ax.legend(fontsize=9.5, loc='lower left')
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', color='#e8e8e4', lw=0.7)
    fig.text(0.09, 0.045, '盯的就是红线: 剪刀差连续回升(2025→2026H1: -8.7→-3.1→-4.0) + 成交量 + 租金企稳 + PIR<15, 四信号共振才是底。',
             fontsize=9, color=INK)
    plt.tight_layout(rect=[0, 0.06, 1, 1])
    pdf.savefig(fig, facecolor=BG); plt.close(fig)

print('saved output/剪刀差跨国对比_2026-07.pdf')
