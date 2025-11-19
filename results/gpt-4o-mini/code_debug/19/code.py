import numpy as np
import matplotlib as mlp
mlp.use("Agg")

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(3.0, 6.0))  # Increase figure size
X = np.arange(0, 12, 0.01)
data = np.sin(X) + np.random.normal(0, 0.05, (len(X),))  # Adjust noise for better visibility
plt.plot(X, data, color='b', linewidth=2)  # Increase line width for visibility
plt.scatter(X, data, color='k', s=10, linewidths=0)  # Increase marker size
plt.tight_layout()  # Adjust layout
fig.savefig("res.pdf", bbox_inches='tight')
fig.savefig("res.png", bbox_inches='tight', dpi=5000)