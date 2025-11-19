import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.boxplot(x="day", y="total_bill", data=tips)

# Calculate the medians for each day
medians = tips.groupby("day")["total_bill"].median()

# Overlay the median value on the boxplot
for x, median in enumerate(medians):
    ax.text(x, median, f'{median:.2f}', ha='center', va='center', color='white')

plt.show()