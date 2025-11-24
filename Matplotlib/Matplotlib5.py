import matplotlib.pyplot as plt
value=[20,35.5,15,10.5,40]
animal=['dog','cat','rabbit','fox','others',]
ex=[0,0.3,0,0.3,0]
plt.pie(x=value,labels=animal,autopct='%.1f%%',startangle=180,counterclock=False
        ,shadow=True,wedgeprops={'width':0.4})
plt.show()