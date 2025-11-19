import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.facecolor'] = 'w'
plt.scatter(np.random.randn(100), np.random.randn(100), facecolors='none', edgecolors='black', marker='o')
plt.show()