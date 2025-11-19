import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('planets')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(9, 6))

# Create the KDE plot
sns.kdeplot(data=df.mass, ax=ax, c='k')

# Determine the x values and corresponding y values for filling
x = np.linspace(0, df.mass.max(), 1000)
kde = sns.kdeplot(data=df.mass, bw_adjust=0.5).get_lines()[0].get_data()
y = kde[1]

# Fill areas under the curve
ax.fill_between(x[x < 0], y[x < 0], color='red', alpha=0.5, label='x < 0 (19%)')
ax.fill_between(x[x >= 0], y[x >= 0], color='blue', alpha=0.5, label='x >= 0 (80%)')

# Add percentage annotations
ax.annotate('19%', xy=(0, y[x < 0].max() / 2), color='red')
ax.annotate('80%', xy=(5, y[x >= 0].max() / 2), color='blue')

# Show legend
ax.legend()

# Set labels
ax.set_xlabel('mass')
ax.set_ylabel('Density')

# Show plot
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
