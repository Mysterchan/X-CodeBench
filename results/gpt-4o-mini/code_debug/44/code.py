import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, ax = plt.subplots(figsize=(11.69, 8.27))

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim(1, 10000)
ax.set_ylim(10, 1000)

ax.plot([2000], [999], color='black', linestyle='-', marker='o', markersize=2, linewidth=0.5, clip_on=True)

divider = make_axes_locatable(ax)
axLin = divider.append_axes("top", size='44.8%', pad=0, sharex=ax)
axLin.set_yscale('linear')
axLin.set_ylim(1000, 1007)

axLin.plot([1000], [1000.001], color='black', linestyle='-', marker='o', markersize=2, linewidth=0.5, clip_on=False)

plt.show()