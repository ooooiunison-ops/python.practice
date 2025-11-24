import matplotlib.pyplot as plt
import matplotlib.dates as dt
import pandas as pd
import japanize_matplotlib
import matplotlib.ticker as ticker

df=pd.read_csv('15日の気温と湿度.csv',index_col='時間'
               ,parse_dates=True,encoding='Shift-JIS')
x=df.index
y1=df['気温']
y2=df['湿度']

fig,ax1= plt.subplots()
ax1.plot(x,y1,color='red',label='温度')
ax1.tick_params(axis='x',labelsize=8,labelrotation=10)
ax1.set_ylim(0,35)
ax1.set_ylabel('気温(℃)',color='red',loc='bottom')
ax1.set_xlabel('時間',color='black',loc='right')
ax1.grid(axis='y')

ax2=ax1.twinx()
ax2.plot(x,y2,color='blue',label='湿度')
ax2.set_ylim(0,100)
ax2.set_ylabel('湿度(%)',color='blue',loc='bottom')
ax2.xaxis.set_major_formatter(dt.DateFormatter('%H:%M'))

ax1.legend(bbox_to_anchor=(1,1),loc='upper right',frameon=False,fontsize=14)
ax2.legend(bbox_to_anchor=(1,0.9),frameon=False,fontsize=14)

ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(2))

plt.title('一日の気温と湿度の変化')
plt.show()