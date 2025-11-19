import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

exercise = sns.load_dataset("exercise")

# Create figure and two subplots sharing x-axis but with broken y-axis
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8,6), gridspec_kw={'height_ratios':[1,3]})

# Plot violin plots on both axes
sns.violinplot(x="time", y="pulse", hue="kind", data=exercise, ax=ax1, split=True)
sns.violinplot(x="time", y="pulse", hue="kind", data=exercise, ax=ax2, split=True)

# Set y-limits to create the broken axis effect
ax1.set_ylim(130, 175)
ax2.set_ylim(70, 105)

# Hide the spines between ax1 and ax2
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.tick_params(labelbottom=False)  # Hide x labels on top plot

# Create diagonal lines to indicate broken axis
d = .015  # size of diagonal lines in axes coordinates
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# Adjust legend to only show once
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles[:3], labels[:3], title="kind")

plt.tight_layout()
plt.show()