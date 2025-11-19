import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt

data = np.random.rand(5,5)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(data, interpolation='nearest', cmap='gray')
ax2.imshow(data, interpolation='bilinear', cmap='gray')

art = patches.Circle((2, 2), 2, fill=False, edgecolor='black')
ax2.add_patch(art)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
