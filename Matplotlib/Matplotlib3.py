import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

machine = ['電子レンジ','炊飯器','テレビ']
shopA =[20,40,50,]
shopB =[30,50,20,]


stockX=plt.barh(machine,shopA,height=0.5,color='c',label='店舗A',)
stockY=plt.barh(machine,shopB,height=0.5,color='m',label='店舗B',left=shopA)

plt.bar_label(stockX)
plt.bar_label(stockY)
plt.legend(loc='upper left',bbox_to_anchor=(1,0))
plt.title('家電ごとの各店舗の売上')
plt.show()