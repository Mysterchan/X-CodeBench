import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# Generate data
x = np.random.normal(0.25, 0.5, 100)
y = np.random.normal(0.25, 0.5, 100)

# Create the joint plot
joint_plot = sns.jointplot(x=x, y=y, kind='kde', xlim=(-0.75, 1.25), ylim=(-0.75, 1.25), height=4)

# Add a vertical dashed line at x=0
joint_plot.ax_joint.axvline(0, color='red', linestyle='--')

plt.show()