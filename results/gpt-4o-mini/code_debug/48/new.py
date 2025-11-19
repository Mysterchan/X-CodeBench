import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(0)
uniform_data = np.random.rand(10, 12)

# Set up the heatmap with the parameter to remove the color bar
ax = sns.heatmap(uniform_data, cbar=False)
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
