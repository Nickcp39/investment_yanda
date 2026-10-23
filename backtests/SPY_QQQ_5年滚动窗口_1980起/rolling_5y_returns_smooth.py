# -*- coding: utf-8 -*-
"""
SPY / QQQ 五年滑动窗口收益率 —— 平滑 + 压缩极端值版
- 平滑：3 年中心移动平均，画平滑趋势线（原始点淡化保留）
- 压缩极端值：y 轴用对称对数刻度(symlog, linthresh=100)，
  即 ±100% 以内线性、之外对数压缩，把 +852% 这类极值压下来而不丢信息
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/backtests/SPY_QQQ_5年滚动窗口_1980起'
df = pd.read_csv(os.path.join(OUT, '五年滚动收益率_明细.csv'))

spy = df[df['label'] == 'SPY(标普500)'].reset_index(drop=True)
qqq = df[df['label'] == 'QQQ(纳斯达克100)'].reset_index(drop=True)

def smooth(series, window=3):
    return series.rolling(window, center=True, min_periods=1).mean()

spy_pct = spy['total_return'] * 100
qqq_pct = qqq['total_return'] * 100
spy_s = smooth(spy_pct)
qqq_s = smooth(qqq_pct)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(14, 7.5), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

# 原始点（淡化）+ 平滑线（加粗）
ax.plot(spy['start_year'], spy_pct, color='#4da6ff', alpha=0.28,
        marker='o', markersize=3, linewidth=0.8, zorder=1)
ax.plot(qqq['start_year'], qqq_pct, color='#ffa64d', alpha=0.28,
        marker='s', markersize=3, linewidth=0.8, zorder=1)

ax.plot(spy['start_year'], spy_s, color='#4da6ff', linewidth=2.8, zorder=3, label=f'SPY（标普500）· 平滑（5年均值 {spy_pct.mean():+.0f}%）')
ax.plot(qqq['start_year'], qqq_s, color='#ffa64d', linewidth=2.8, zorder=3, label=f'QQQ（纳斯达克100）· 平滑（5年均值 {qqq_pct.mean():+.0f}%）')

ax.axhline(0, color='#6b7280', linewidth=1, linestyle='--', zorder=2)
ax.axhline(spy_pct.mean(), color='#4da6ff', linewidth=1.4, linestyle=':', alpha=0.85, zorder=2)
ax.axhline(qqq_pct.mean(), color='#ffa64d', linewidth=1.4, linestyle=':', alpha=0.85, zorder=2)

# 对称对数刻度：压缩极端高点
ax.set_yscale('symlog', linthresh=100)
ax.set_ylim(-75, 900)
yticks = [-50, 0, 100, 200, 400, 800]
ax.set_yticks(yticks)
ax.set_yticklabels([f'{int(t)}%' for t in yticks])

# 标注关键窗口（用平滑后坐标近似，直接标原始值）
for d, color in [(spy, '#4da6ff'), (qqq, '#ffa64d')]:
    i_max = d['total_return'].idxmax()
    i_min = d['total_return'].idxmin()
    ax.annotate(f"{d.loc[i_max,'start_year']}→{d.loc[i_max,'end_year']}\n+{d.loc[i_max,'total_return']*100:.0f}%",
                xy=(d.loc[i_max,'start_year'], d.loc[i_max,'total_return']*100),
                xytext=(d.loc[i_max,'start_year']+1.5, d.loc[i_max,'total_return']*100+150),
                color=color, fontsize=8.5, fontweight='bold')
    ax.annotate(f"{d.loc[i_min,'start_year']}→{d.loc[i_min,'end_year']}\n{d.loc[i_min,'total_return']*100:.0f}%",
                xy=(d.loc[i_min,'start_year'], d.loc[i_min,'total_return']*100),
                xytext=(d.loc[i_min,'start_year']+1.5, d.loc[i_min,'total_return']*100-30),
                color=color, fontsize=8.5, fontweight='bold')

ax.set_title('SPY / QQQ 五年滑动窗口总收益率（平滑 + 对称对数刻度压缩极端值）',
             color='#e8eaed', fontsize=15, fontweight='bold', pad=14)
ax.set_xlabel('窗口起始年份（→ 5 年后）', color='#9aa0a6', fontsize=11)
ax.set_ylabel('五年总收益率（%）', color='#9aa0a6', fontsize=11)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.set_xlim(1979, 2022)
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7)
for spine in ax.spines.values():
    spine.set_color('#2a2e33')

ax.legend(loc='upper left', facecolor='#1f2428', edgecolor='#3a4046',
          labelcolor='#e8eaed', fontsize=10)

note = ('注：SPY=标普500(1980起)、QQQ=纳斯达克100(1986起)指数代理；收益率=复权价口径。'
        'y 轴为对称对数刻度(±100%内线性、之外对数)，虚线为 0%；浅色点为原始值、实线为 3 年移动平均。')
fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8)

plt.tight_layout()
png_path = os.path.join(OUT, '五年滚动收益率_1980起_平滑版.png')
plt.savefig(png_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
print('已保存:', png_path)
