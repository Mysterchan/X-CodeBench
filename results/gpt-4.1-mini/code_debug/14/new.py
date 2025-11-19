import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.facecolor'] = 'w'
plt.scatter(np.random.randn(100), np.random.randn(100), facecolors='none', edgecolors='black', marker='o')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
