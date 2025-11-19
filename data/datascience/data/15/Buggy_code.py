import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
hours=[1,2,3,4,5,6,7,8,9,10]
temp=[14,13,12,15,16,17,18,24,29,32]
plt.plot(hours,temp,marker='o',markersize=5,color='r',
         linewidth='1',linestyle='dashed',markeredgecolor='black',markerfacecolor='yellow')
plt.xlabel("Hours")
plt.ylabel("Temp. in Celsius")
plt.title("Hours verses Temperature")
plt.xlim(0,12)
plt.ylim(0,35)
plt.grid(True)
yaxisminor=AutoMinorLocator(10)
plt.axes().yaxis.set_minor_locator(yaxisminor)
plt.axes().yaxis.set_tick_params(which='minor' , left='off' , size= 10)
plt.show()