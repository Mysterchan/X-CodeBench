import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")
fmri.sort_values('timepoint', inplace=True)

# Create background column with values 0, 1, 2 for shading
arr = np.ones(len(fmri))
arr[:300] = 0
arr[300:600] = 1
arr[600:] = 2
fmri['background'] = arr

# Plot the lineplot with hue='event'
ax = sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri)

# Define colors for background shading
background_colors = {0: "#a6bddb", 1: "#fbb4b9", 2: "#b2df8a"}

# Get unique background segments and their timepoint ranges
for bg_val in fmri['background'].unique():
    subset = fmri[fmri['background'] == bg_val]
    xmin = subset['timepoint'].min()
    xmax = subset['timepoint'].max()
    ax.axvspan(xmin, xmax, color=background_colors[bg_val], alpha=0.3, zorder=0)

plt.show()