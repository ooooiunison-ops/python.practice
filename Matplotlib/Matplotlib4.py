import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib.dates as dt
import pandas as pd

df = pd.read_csv('売上管理表2.csv',encoding='Shift=JIS')
t_df=df[['店舗','商品分類','売上金額']].groupby(['店舗','商品分類']).sum()
t_df=t_df.unstack()


t_df.plot(kind='barh',rot=0,stacked=True)
plt.ticklabel_format(style='plain',axis='x')
plt.legend(['野菜','果物','精肉','鮮魚'],loc=3,bbox_to_anchor=(1,0))
plt.ylabel('店舗名')
plt.xlabel('売上金額(円)')
plt.title('店舗/商品分類別売上')
plt.show()