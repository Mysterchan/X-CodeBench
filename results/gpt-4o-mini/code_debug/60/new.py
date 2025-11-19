import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a random DataFrame
df = pd.DataFrame(np.random.random((10, 10)))

# Create a 2x2 grid of subplots
fig, axn = plt.subplots(2, 2, sharex=True, sharey=True)

# Create a single color map from the data
vmin = df.values.min()
vmax = df.values.max()

# Plotting heatmaps on each subplot
for ax in axn.flat:
    sns.heatmap(df, ax=ax, cbar=False, vmin=vmin, vmax=vmax)

# Add a single colorbar for all subplots
cbar = fig.colorbar(axn[0, 0].collections[0], ax=axn, orientation='vertical')
cbar.ax.set_ylabel('Colorbar Label')

# Show the plot
plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
