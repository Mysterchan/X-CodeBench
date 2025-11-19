import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset("tips")

# Create a violin plot with specified x-axis positions
ax = sns.violinplot(x="day", y="total_bill", hue="sex", data=tips,
                    palette="Set2", split=True, scale="count",
                    inner="stick", scale_hue=False, bw=0.2)

# Adjust x-ticks to specific locations
ax.set_xticks([1, 2, 4, 6])
ax.set_xticklabels(['Thur', 'Fri', 'Sat', 'Sun'])

# Show the plot
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
