import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# Generate data
x = np.random.normal(0.25, 0.5, 10)
y = np.random.normal(0.25, 0.5, 10)

# Create the jointplot
g = sns.jointplot(x=x, y=y, kind='kde', xlim=(-.75, 1.25), ylim=(-.75, 1.25), height=4)

# Add vertical dashed line at x=0 on the joint axes
g.ax_joint.axvline(0, color='red', linestyle='--', linewidth=2)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
