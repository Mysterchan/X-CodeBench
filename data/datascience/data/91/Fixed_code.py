import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
exercise = sns.load_dataset("exercise")
f, (ax_top, ax_bottom) = plt.subplots(ncols=1, nrows=2, sharex=True, gridspec_kw={'hspace':0.05})
sns.violinplot(x="time", y="pulse", hue="kind",data=exercise, ax=ax_top)
sns.violinplot(x="time", y="pulse", hue="kind",data=exercise, ax=ax_bottom)
ax_top.set_ylim(bottom=125)   # those limits are fake
ax_bottom.set_ylim(0,100)

sns.despine(ax=ax_bottom)
sns.despine(ax=ax_top, bottom=True)

ax = ax_top
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal

ax2 = ax_bottom
kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal

#remove one of the legend
ax_bottom.legend_.remove()
plt.show()