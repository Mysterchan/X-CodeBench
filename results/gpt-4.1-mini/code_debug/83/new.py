import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Map days to specified x-axis positions
day_order = ["Thur", "Fri", "Sat", "Sun"]
x_positions = [1, 2, 4, 6]
pos_dict = dict(zip(day_order, x_positions))

# Create a new column with numeric positions for x
tips['day_pos'] = tips['day'].map(pos_dict)

# Plot violinplot using numeric positions for x
ax = sns.violinplot(x="day_pos", y="total_bill", hue="sex",
                    data=tips, palette="Set2", split=True,
                    scale="count", inner="stick",
                    scale_hue=False, bw=.2)

# Set x-ticks and labels to match specified positions and day names
ax.set_xticks(x_positions)
ax.set_xticklabels(day_order)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
