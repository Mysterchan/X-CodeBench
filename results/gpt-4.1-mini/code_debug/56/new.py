import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

exercise = sns.load_dataset("exercise")

# Calculate counts instead of percentages for stacking
plot = exercise.groupby(['diet', 'kind']).size().reset_index(name='count')

# Pivot the data to have kinds as columns for stacking
plot_pivot = plot.pivot(index='diet', columns='kind', values='count').fillna(0)

# Plot stacked bar chart using matplotlib directly
plot_pivot.plot(kind='bar', stacked=True)

plt.ylabel('Count')
plt.xlabel('diet')
plt.legend(title='kind')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
