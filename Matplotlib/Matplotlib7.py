import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib.gridspec as gridspec

x=['USA','Japam','Australia']
y1=[90,35,44,]
y2=[110,43,27]
fig,ax =plt.subplots(2,2,)

ax[0,0].plot(x,y1,color='blue')
ax[0,0].set(title='Male population')

ax[0,1].plot(x,y2,color='red')
ax[0,1].set(title='Female population')

ax[1,0].bar(x,y1,color='blue')

ax[1,1].bar(x,y2,color='red')


plt.show()