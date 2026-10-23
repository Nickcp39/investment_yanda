# -*- coding: utf-8 -*-
"""
SPY vs QQQ 差距拆解（2008 年起，含分红再投资）
- 用真实 ETF 复权价(adj_close)，含股息再投资
- 图1：累计涨幅对比（对数刻度）
- 图2：QQQ/SPY 相对强度比值（>1 表示 QQQ 跑赢）
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/backtests/SPY_QQQ_5年滚动窗口_1980起'
DATA = r'D:/work/investment/financial-analysis-lab/backtests/黄金_货币供应_估值_2026-08-07/data'

spy = pd.read_csv(DATA + '/SPY_daily_adjusted.csv', parse_dates=['date']).set_index('date')['adj_close'].sort_index()
qqq = pd.read_csv(DATA + '/QQQ_daily_adjusted.csv', parse_dates=['date']).set_index('date')['adj_close'].sort_index()

START = pd.Timestamp('2008-01-01')
END = pd.Timestamp('2026-02-01')

def idx(s):
    base = s.asof(START)
    s = s.loc[(s.index >= START) & (s.index <= END)]
    return s / base * 100.0

spy_i = idx(spy)
qqq_i = idx(qqq)
ratio = qqq_i / spy_i  # QQQ 相对 SPY 的强度

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

SPY_C = '#f0f6fc'
QQQ_C = '#ffd166'

# ============ 图1：累计涨幅（对数刻度） ============
fig, ax = plt.subplots(figsize=(13, 7), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

ax.plot(spy_i.index, spy_i, color=SPY_C, linewidth=2.8, label='SPY（标普500，含分红）')
ax.plot(qqq_i.index, qqq_i, color=QQQ_C, linewidth=2.8, label='QQQ（纳斯达克100，含分红）')

ax.axhline(100, color='#6b7280', linewidth=1, linestyle='-', alpha=0.6)
ax.set_yscale('log')
ax.set_ylim(45, 1600)

# 标注几个关键节点
for d, label, dy in [('2009-03-09', '危机底', 0.75), ('2020-02-19', '疫情前顶', 1.15),
                      ('2022-10-12', '加息底', 0.72), ('2026-02-01', '现在', 1.05)]:
    x = pd.Timestamp(d)
    ax.axvline(x, color='#3a4046', linewidth=0.8, linestyle=':', alpha=0.6)
    ax.text(x, 1400 * dy, label, color='#9aa0a6', fontsize=8.5, ha='center')

ax.annotate(f'QQQ +{qqq_i.iloc[-1]-100:.0f}%',
            xy=(qqq_i.index[-1], qqq_i.iloc[-1]), xytext=(pd.Timestamp('2023-06-01'), 1350),
            color=QQQ_C, fontsize=11, fontweight='bold')
ax.annotate(f'SPY +{spy_i.iloc[-1]-100:.0f}%',
            xy=(spy_i.index[-1], spy_i.iloc[-1]), xytext=(pd.Timestamp('2023-06-01'), 590),
            color=SPY_C, fontsize=11, fontweight='bold')

ax.set_title('2008 年以来 SPY vs QQQ 累计总回报（含分红再投资，2008-01=100，对数刻度）',
             color='#e8eaed', fontsize=14, fontweight='bold', pad=14)
ax.set_ylabel('累计回报指数（2008-01=100）', color='#9aa0a6', fontsize=11)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.set_xlim(pd.Timestamp('2008-01-01'), pd.Timestamp('2026-06-01'))
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7, which='both')
for spine in ax.spines.values():
    spine.set_color('#2a2e33')
ax.legend(loc='upper left', facecolor='#1f2428', edgecolor='#3a4046', labelcolor='#e8eaed', fontsize=10)
plt.tight_layout()
p1 = os.path.join(OUT, 'SPY_vs_QQQ_累计_2008起.png')
plt.savefig(p1, facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.close(fig)

# ============ 图2：QQQ/SPY 相对强度 ============
fig, ax = plt.subplots(figsize=(13, 5.5), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

ax.plot(ratio.index, ratio, color='#56d4a3', linewidth=2.4)
ax.axhline(1.0, color='#6b7280', linewidth=1, linestyle='--')
ax.fill_between(ratio.index, 1.0, ratio, where=(ratio >= 1.0), color='#56d4a3', alpha=0.12)
ax.fill_between(ratio.index, 1.0, ratio, where=(ratio < 1.0), color='#ff6b6b', alpha=0.15)

ax.annotate(f'QQQ/SPY = {ratio.iloc[-1]:.2f}',
            xy=(ratio.index[-1], ratio.iloc[-1]), xytext=(pd.Timestamp('2022-08-01'), 2.45),
            color='#56d4a3', fontsize=12, fontweight='bold')

ax.set_title('QQQ 相对 SPY 的强度（比值 >1 表示 QQQ 跑赢，2008-01=1.0）',
             color='#e8eaed', fontsize=13.5, fontweight='bold', pad=12)
ax.set_ylabel('QQQ/SPY 比值', color='#9aa0a6', fontsize=11)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.set_xlim(pd.Timestamp('2008-01-01'), pd.Timestamp('2026-06-01'))
ax.set_ylim(0.7, 2.7)
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7)
for spine in ax.spines.values():
    spine.set_color('#2a2e33')
plt.tight_layout()
p2 = os.path.join(OUT, 'QQQ相对SPY强度_2008起.png')
plt.savefig(p2, facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.close(fig)

print('图1:', p1)
print('图2:', p2)
print(f'SPY 全程 +{spy_i.iloc[-1]-100:.1f}% | QQQ 全程 +{qqq_i.iloc[-1]-100:.1f}% | 比值 {ratio.iloc[-1]:.2f}x')
