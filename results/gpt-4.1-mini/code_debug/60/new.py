import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random((10,10,)))

fig, axn = plt.subplots(2, 2, sharex=True, sharey=True)

# Plot the first heatmap and keep the QuadMesh object for the colorbar
mesh = sns.heatmap(df, ax=axn[0,0], cbar=False)

# Plot the remaining heatmaps without colorbars
for ax in axn.flat[1:]:
    sns.heatmap(df, ax=ax, cbar=False)

# Create a single colorbar for all heatmaps
fig.colorbar(mesh.get_children()[0], ax=axn, orientation='vertical', fraction=0.05, pad=0.04)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
