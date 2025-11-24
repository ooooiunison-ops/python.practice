import matplotlib.pyplot as plt
import japanize_matplotlib
x = ['soccer','baseball','tennis',]
y = [40,60,30]
plt.bar(x,y)
plt.savefig('各部活の生徒数.pdf')