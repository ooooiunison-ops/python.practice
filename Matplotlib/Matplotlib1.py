
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
df = pd.read_csv('2023年度7月の最高気温.csv',
                 delimiter=',',encoding='Shift-JIS')
df2 = pd.read_csv('2024年度7月の最高気温.csv',
                 delimiter=',',encoding='Shift-JIS')
x=df['日付']
y=df['最高気温']
x2=df2['日付']
y2=df2['最高気温']
plt.grid()
plt.plot(x,y,label='2023 Max Temp')
plt.plot(x2,y2,label='2024 Max Temp')
plt.legend(fontsize=15)
plt.show()