import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

exercise = sns.load_dataset("exercise")

# Create a single figure with subplots 
fig, (ax1, ax2) = plt.subplots(ncols=1, nrows=2, sharex=True, figsize=(8, 6))

# First plot: Violin plot for pulse rates from 0 to 6.5
sns.violinplot(x="time", y="pulse", hue="kind", data=exercise, ax=ax1, split=True, inner='quartile')
ax1.set_ylim(0, 6.5)  # Set the limits for the first axis
ax1.legend().set_visible(False)

# Add a broken y-axis effect
ax1.set_yticks([0, 3, 6])  # You can customize these ticks

# Second plot: Violin plot for pulse rates from 13.5 upwards
sns.violinplot(x="time", y="pulse", hue="kind", data=exercise, ax=ax2, split=True, inner='quartile')
ax2.set_ylim(13.5, 20)  # Set the limits for the second axis

# Create a divider to add a break in the y-axis to the first subplot
divider = make_axes_locatable(ax2)
ax3 = divider.append_axes("left", size="5%", pad=0.1)

# Break line for visual effect
ax3.set_ylim(6.5, 13.5)
ax3.axis('off')  # Hide the axis for the broken effect

plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
