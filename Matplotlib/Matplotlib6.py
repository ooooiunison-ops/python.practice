import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
import numpy as np


df=pd.read_csv("売上管理表2.csv",encoding='Shift-JIS')
s_df=df[['商品分類','売上金額']].groupby('商品分類').sum()
s_df=s_df.sort_values(by='売上金額',ascending=True)

c_map=plt.get_cmap('Paired')
color=c_map(np.arange(2,9,2))
exp=(0.1,0,0.1,0)

value = s_df['売上金額']
product=s_df.index

plt.pie(x=value,labels=product,autopct='%.2f',colors=color
        ,pctdistance=0.4,labeldistance=None,shadow=True
        ,startangle=180,counterclock=False,explode=exp)
plt.legend(product,loc=3,bbox_to_anchor=(1,0))
plt.title('商品分類ごとの売上金額合計',fontsize=16)
plt.show()