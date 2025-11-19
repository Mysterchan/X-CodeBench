import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = [14, 13, 12, 15, 16, 17, 18, 24, 29, 32]

plt.plot(hours, temp, marker='o', markersize=5, color='r',
         linewidth=1, linestyle='dashed', markeredgecolor='black', markerfacecolor='yellow')
plt.xlabel("Hours")
plt.ylabel("Temp. in Celsius")
plt.title("Hours verses Temperature")
plt.xlim(0, 12)
plt.ylim(0, 35)
plt.grid(True)

ax = plt.gca()
yaxisminor = AutoMinorLocator(10)
ax.yaxis.set_minor_locator(yaxisminor)
ax.yaxis.set_tick_params(which='minor', left=False, size=10)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
