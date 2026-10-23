# -*- coding: utf-8 -*-
"""
日本：老龄化率 vs 药品市场规模 —— 量涨、价跌、金额横盘的背离
数据来源：
- 老龄化率(65+%): 日本总务省统计局 / 国立社会保障·人口问题研究所
- 药品市场(药价基准, 万亿日元): 厚生劳动省 / IQVIA 医药品市场统计(2003-2021)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/studies/日本老龄化_药企_2026-10-08'
os.makedirs(OUT, exist_ok=True)

# 老龄化率 65岁以上占比 %
aging_years = [1960, 1970, 1980, 1990, 2000, 2005, 2010, 2015, 2020, 2025]
aging = [5.7, 7.1, 9.1, 12.0, 17.4, 20.1, 23.0, 26.6, 28.8, 30.0]

# 药品市场规模（药价基准，万亿日元）
mkt_years = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
             2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
mkt = [7.6, 8.0, 8.5, 8.4, 8.8, 9.1, 9.9, 10.1, 10.9,
       11.1, 11.5, 11.7, 12.6, 12.8, 12.7, 12.7, 13.0, 12.9]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

fig, ax1 = plt.subplots(figsize=(13, 7), dpi=130)
fig.patch.set_facecolor('#121417')
ax1.set_facecolor('#121417')

# 左轴：老龄化率
ax1.plot(aging_years, aging, color='#4da6ff', linewidth=2.6, marker='o', markersize=4.5,
         label='65岁以上人口占比（左轴）')
ax1.set_ylabel('老龄化率（65岁以上 %）', color='#4da6ff', fontsize=11)
ax1.tick_params(axis='y', colors='#4da6ff', labelsize=10)
ax1.set_ylim(0, 35)

# 右轴：药品市场规模
ax2 = ax1.twinx()
ax2.plot(mkt_years, mkt, color='#ffa64d', linewidth=2.6, marker='s', markersize=4.5,
         label='药品市场规模（右轴）')
ax2.set_ylabel('国内药品市场（万亿日元，药价基准）', color='#ffa64d', fontsize=11)
ax2.tick_params(axis='y', colors='#ffa64d', labelsize=10)
ax2.set_ylim(0, 16)

# 2015 见顶标注
ax2.annotate('2015 年见顶 ≈ 12.6 万亿\n此后横盘/微降',
             xy=(2015, 12.6), xytext=(2009, 14.6),
             color='#ffa64d', fontsize=10.5, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#ffa64d', lw=1))

# 政策节点标注
ax1.axvline(1981, color='#6b7280', linewidth=1, linestyle=':', alpha=0.7)
ax1.text(1981, 33.5, '1981\n药价两年一降\n(首轮-18.6%)', color='#9aa0a6', fontsize=8.5, ha='center')
ax1.axvline(2021, color='#6b7280', linewidth=1, linestyle=':', alpha=0.7)
ax1.text(2021, 33.5, '2021\n改为每年降价\n(每次-4~7%)', color='#9aa0a6', fontsize=8.5, ha='center')

# 组合图例
l1, lab1 = ax1.get_legend_handles_labels()
l2, lab2 = ax2.get_legend_handles_labels()
ax1.legend(l1 + l2, lab1 + lab2, loc='upper left', facecolor='#1f2428',
           edgecolor='#3a4046', labelcolor='#e8eaed', fontsize=10)

ax1.set_title('日本：老龄化一路上升，但药品市场金额 2015 年后停滞（量涨、价跌、金额横盘）',
              color='#e8eaed', fontsize=13.5, fontweight='bold', pad=14)
ax1.set_xlabel('年份', color='#9aa0a6', fontsize=11)
ax1.set_xlim(1958, 2026)
ax1.tick_params(axis='x', colors='#9aa0a6', labelsize=10)
ax1.grid(color='#2a2e33', linewidth=0.6, alpha=0.7)
for spine in list(ax1.spines.values()) + list(ax2.spines.values()):
    spine.set_color('#2a2e33')

note = ('数据：老龄化率=日本总务省统计局/人口问题研究所；药品市场=厚劳省/IQVIA药价基准(2003-2020)。'
        '处方药市场2015年见顶(7.87万亿日元)后2016-2019从未再超；2014-2019药品市场CAGR约-0.2%。')
fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8)

plt.tight_layout()
p = os.path.join(OUT, '日本老龄化_vs_药品市场.png')
plt.savefig(p, facecolor=fig.get_facecolor(), bbox_inches='tight')
print('已保存:', p)
