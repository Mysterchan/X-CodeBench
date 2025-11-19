import numpy as np
import matplotlib as mlp
mlp.use("Agg")

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(1.0,1.5))
X = np.arange(0,12,0.01)
data = np.sin(X) + np.random.normal(0, 0.005, (len(X),))
plt.plot(X, data, color='b', linewidth=0.6)  # increased linewidth for visibility
plt.scatter(X, data, color='k', s=5, linewidths=0)  # increased size for visibility
fig.savefig("res.pdf", bbox_inches='tight')
fig.savefig("res.png", bbox_inches='tight', dpi=5000)