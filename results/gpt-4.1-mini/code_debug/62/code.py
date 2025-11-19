import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.boxplot(x="day", y="total_bill", data=tips)

# Calculate medians for each day
medians = tips.groupby('day')['total_bill'].median().values
# Get the positions of the boxes on the x-axis
positions = range(len(medians))

# Add median labels centered on each box
for pos, median in zip(positions, medians):
    ax.text(pos, median, f'{median:.2f}', ha='center', va='center', color='white', fontweight='bold')

plt.show()