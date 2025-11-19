import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
plt.plot(X, Ya)
plt.fill_between(X, Ya, 0,
                 where=(X >= 3.00) & (Ya <= 0),
                 color='b', alpha=.1)

# Adding annotation to the filled area
plt.text(4, -0.3, 'Filled polygon', fontsize=12, color='red')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
