import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(0)
uniform_data = np.random.rand(10, 12)

# Set up the heatmap with the parameter to remove the color bar
ax = sns.heatmap(uniform_data, cbar=False)
plt.show()