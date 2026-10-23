# -*- coding: utf-8 -*-
"""
SPY / QQQ 五年滑动窗口收益率 —— 只看 2002 之后 / 只看 2009 之后
平滑：3 年中心移动平均；线性刻度（此区间已无极端值）
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

OUT = r'D:/work/investment/financial-analysis-lab/backtests/SPY_QQQ_5年滚动窗口_1980起'
df = pd.read_csv(os.path.join(OUT, '五年滚动收益率_明细.csv'))

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

SPY_COLOR = '#4da6ff'
QQQ_COLOR = '#ffa64d'


def smooth(s, w=3):
    return s.rolling(w, center=True, min_periods=1).mean()


def plot_since(start_year, fname, title_extra):
    d = df[df['start_year'] >= start_year]
    spy = d[d['label'] == 'SPY(标普500)'].reset_index(drop=True)
    qqq = d[d['label'] == 'QQQ(纳斯达克100)'].reset_index(drop=True)

    spy_pct = spy['total_return'] * 100
    qqq_pct = qqq['total_return'] * 100

    fig, ax = plt.subplots(figsize=(12.5, 7), dpi=130)
    fig.patch.set_facecolor('#121417')
    ax.set_facecolor('#121417')

    # 原始点（淡化）+ 平滑线
    ax.plot(spy['start_year'], spy_pct, color=SPY_COLOR, alpha=0.25,
            marker='o', markersize=4, linewidth=0.8, zorder=1)
    ax.plot(qqq['start_year'], qqq_pct, color=QQQ_COLOR, alpha=0.25,
            marker='s', markersize=4, linewidth=0.8, zorder=1)
    spy_mean = spy_pct.mean()
    qqq_mean = qqq_pct.mean()
    ax.plot(spy['start_year'], smooth(spy_pct), color=SPY_COLOR, linewidth=2.8,
            zorder=3, label=f'SPY（标普500）· 平滑（5年均值 {spy_mean:+.0f}%）')
    ax.plot(qqq['start_year'], smooth(qqq_pct), color=QQQ_COLOR, linewidth=2.8,
            zorder=3, label=f'QQQ（纳斯达克100）· 平滑（5年均值 {qqq_mean:+.0f}%）')

    ax.axhline(0, color='#6b7280', linewidth=1, linestyle='--', zorder=2)
    # 五年均值线
    ax.axhline(spy_mean, color=SPY_COLOR, linewidth=1.4, linestyle=':', alpha=0.85, zorder=2)
    ax.axhline(qqq_mean, color=QQQ_COLOR, linewidth=1.4, linestyle=':', alpha=0.85, zorder=2)

    # 线性刻度，y 轴范围
    ax.set_ylim(-30, 270)
    ax.set_yticks([0, 50, 100, 150, 200, 250])
    ax.set_yticklabels([f'{t}%' for t in [0, 50, 100, 150, 200, 250]])

    # 标注最高/最低
    for d_, color in [(spy, SPY_COLOR), (qqq, QQQ_COLOR)]:
        i_max = d_['total_return'].idxmax()
        i_min = d_['total_return'].idxmin()
        ax.annotate(f"{d_.loc[i_max,'start_year']}→{d_.loc[i_max,'end_year']}\n+{d_.loc[i_max,'total_return']*100:.0f}%",
                    xy=(d_.loc[i_max,'start_year'], d_.loc[i_max,'total_return']*100),
                    xytext=(d_.loc[i_max,'start_year']-3.5, d_.loc[i_max,'total_return']*100+20),
                    color=color, fontsize=8.5, fontweight='bold',
                    ha='center')
        ax.annotate(f"{d_.loc[i_min,'start_year']}→{d_.loc[i_min,'end_year']}\n{d_.loc[i_min,'total_return']*100:.0f}%",
                    xy=(d_.loc[i_min,'start_year'], d_.loc[i_min,'total_return']*100),
                    xytext=(d_.loc[i_min,'start_year']+2.2, d_.loc[i_min,'total_return']*100-22),
                    color=color, fontsize=8.5, fontweight='bold')

    ax.set_title(f'SPY / QQQ 五年滑动窗口总收益率（{title_extra}）',
                 color='#e8eaed', fontsize=15, fontweight='bold', pad=14)
    ax.set_xlabel('窗口起始年份（→ 5 年后）', color='#9aa0a6', fontsize=11)
    ax.set_ylabel('五年总收益率（%）', color='#9aa0a6', fontsize=11)
    ax.tick_params(colors='#9aa0a6', labelsize=10)
    ax.set_xlim(start_year - 1, 2022)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(2))
    ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7)
    for spine in ax.spines.values():
        spine.set_color('#2a2e33')

    ax.legend(loc='upper left', facecolor='#1f2428', edgecolor='#3a4046',
              labelcolor='#e8eaed', fontsize=10)

    note = ('注：SPY=标普500、QQQ=纳斯达克100 指数代理；收益率=复权价口径。'
            '浅色点为原始值，实线为 3 年移动平均。')
    fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8)

    plt.tight_layout()
    p = os.path.join(OUT, fname)
    plt.savefig(p, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close(fig)
    print('已保存:', p)


plot_since(2002, '五年滚动收益率_2002起.png', '2002 年之后')
plot_since(2009, '五年滚动收益率_2009起.png', '2009 年之后')
