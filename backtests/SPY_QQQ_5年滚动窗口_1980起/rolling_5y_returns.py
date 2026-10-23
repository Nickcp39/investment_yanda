# -*- coding: utf-8 -*-
"""
SPY / QQQ 五年滑动窗口收益率分析（1980 年起）
数据口径：用标的指数回溯
  - SPY  -> 标普500 指数 (IDX_GSPC)  1970 年起，窗口从 1980 开始
  - QQQ  -> 纳斯达克100 指数 (IDX_NDX) 1985-10 诞生，窗口从 1986 开始
窗口口径：每个自然年 1 月 1 日(取当年首个交易日) -> 5 年后 1 月 1 日(取当年首个交易日)
总收益率 = 结束复权价 / 起始复权价 - 1
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BASE = r'D:/work/investment/financial-analysis-lab/studies/美股风气40年_兴衰统计_2026-10-06/data/raw/prices'
OUT = r'D:/work/investment/financial-analysis-lab/backtests/SPY_QQQ_5年滚动窗口_1980起'
os.makedirs(OUT, exist_ok=True)

gspc = pd.read_csv(os.path.join(BASE, 'IDX_GSPC.csv.gz'), parse_dates=['date']).set_index('date')
ndx  = pd.read_csv(os.path.join(BASE, 'IDX_NDX.csv.gz'),  parse_dates=['date']).set_index('date')

# 确认数据范围
print('GSPC 范围:', gspc.index.min(), '->', gspc.index.max())
print('NDX  范围:', ndx.index.min(),  '->', ndx.index.max())


def rolling_5y(df, label, start_year):
    rows = []
    for Y in range(start_year, 2022):  # 2021->2026 是最后一个完整五年窗口
        s = df.loc[df.index >= pd.Timestamp(year=Y, month=1, day=1)]
        e = df.loc[df.index >= pd.Timestamp(year=Y + 5, month=1, day=1)]
        if len(s) == 0 or len(e) == 0:
            continue
        start_price = float(s['adjclose'].iloc[0])
        end_price = float(e['adjclose'].iloc[0])
        start_date = s.index[0]
        end_date = e.index[0]
        total_return = end_price / start_price - 1
        # 按实际天数计算 CAGR
        days = (end_date - start_date).days
        cagr = (end_price / start_price) ** (365.0 / days) - 1 if days > 0 else 0.0
        rows.append(dict(
            label=label, start_year=Y, end_year=Y + 5,
            start_date=start_date, end_date=end_date,
            start_price=round(start_price, 4), end_price=round(end_price, 4),
            total_return=round(total_return, 6), cagr=round(cagr, 6),
        ))
    return pd.DataFrame(rows)


spy = rolling_5y(gspc, 'SPY(标普500)', 1980)
qqq = rolling_5y(ndx,  'QQQ(纳斯达克100)', 1986)

# 合并保存
df = pd.concat([spy, qqq], ignore_index=True)
df.to_csv(os.path.join(OUT, '五年滚动收益率_明细.csv'), index=False, encoding='utf-8-sig')

# 打印关键统计
for name, d in [('SPY(标普500)', spy), ('QQQ(纳斯达克100)', qqq)]:
    r = d['total_return']
    print(f"\n===== {name} =====  窗口数 {len(d)}")
    print(f"  五年总收益率: 平均 {r.mean()*100:.1f}% | 中位 {r.median()*100:.1f}%")
    print(f"  最低 {r.min()*100:.1f}% ({d.loc[r.idxmin(),'start_year']}->{d.loc[r.idxmin(),'end_year']})")
    print(f"  最高 {r.max()*100:.1f}% ({d.loc[r.idxmax(),'start_year']}->{d.loc[r.idxmax(),'end_year']})")
    print(f"  年化CAGR 平均 {d['cagr'].mean()*100:.1f}%")
    # 亏损窗口
    neg = d[d['total_return'] < 0]
    print(f"  亏损窗口 {len(neg)} 个:")
    for _, row in neg.iterrows():
        print(f"     {row['start_year']}->{row['end_year']}: {row['total_return']*100:.1f}%")

# ============ 画图 ============
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(14, 7.5), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

ax.plot(spy['start_year'], spy['total_return'] * 100,
        color='#4da6ff', linewidth=2.2, marker='o', markersize=3.5, label='SPY（标普500）')
ax.plot(qqq['start_year'], qqq['total_return'] * 100,
        color='#ffa64d', linewidth=2.2, marker='s', markersize=3.5, label='QQQ（纳斯达克100）')

ax.axhline(0, color='#6b7280', linewidth=1, linestyle='--')
ax.fill_between(spy['start_year'], 0, spy['total_return'] * 100,
                color='#4da6ff', alpha=0.06)
ax.fill_between(qqq['start_year'], 0, qqq['total_return'] * 100,
                color='#ffa64d', alpha=0.06)

# 标注几个关键窗口
def annotate(d, color):
    i_max = d['total_return'].idxmax()
    i_min = d['total_return'].idxmin()
    ax.annotate(f"{d.loc[i_max,'start_year']}→{d.loc[i_max,'end_year']}: +{d.loc[i_max,'total_return']*100:.0f}%",
                xy=(d.loc[i_max,'start_year'], d.loc[i_max,'total_return']*100),
                xytext=(d.loc[i_max,'start_year']+0.3, d.loc[i_max,'total_return']*100+8),
                color=color, fontsize=9, fontweight='bold')
    ax.annotate(f"{d.loc[i_min,'start_year']}→{d.loc[i_min,'end_year']}: {d.loc[i_min,'total_return']*100:.0f}%",
                xy=(d.loc[i_min,'start_year'], d.loc[i_min,'total_return']*100),
                xytext=(d.loc[i_min,'start_year']+0.3, d.loc[i_min,'total_return']*100-15),
                color=color, fontsize=9, fontweight='bold')

annotate(spy, '#4da6ff')
annotate(qqq, '#ffa64d')

# 2000->2005 互联网泡沫标注（QQQ 历史最差之一）
if (qqq['start_year'] == 2000).any():
    row = qqq[qqq['start_year'] == 2000].iloc[0]
    ax.annotate('互联网泡沫破裂', xy=(2000, row['total_return']*100),
                xytext=(1994, -52), color='#ffa64d', fontsize=9,
                arrowprops=dict(arrowstyle='->', color='#ffa64d', lw=0.8))

ax.set_title('SPY / QQQ 五年滑动窗口总收益率（1980 年起，每年滚动一次）',
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

# 图注
note = ('注：SPY/QQQ ETF 分别于 1993 / 1999 年上市，本图用其追踪指数回溯——SPY=标普500(1980起)、'
        'QQQ=纳斯达克100(指数1985年诞生，故从1986起)。收益率=复权价口径，未含股息现金再投资之外的税费。')
fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8)

plt.tight_layout()
png_path = os.path.join(OUT, '五年滚动收益率_1980起.png')
plt.savefig(png_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
print('\n图已保存:', png_path)
print('数据已保存:', os.path.join(OUT, '五年滚动收益率_明细.csv'))
