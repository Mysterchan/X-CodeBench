import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt

data = np.random.rand(5,5)

fig = plt.figure()
ax1, ax2 = fig.subplots(1,2)
ax1.imshow(data, interpolation='nearest', cmap='gray',)
ax2.imshow(data, interpolation='bilinear', cmap='gray',)
if 1:
    art = patches.Circle((2, 2), 2, fill=0)
    ax1.add_artist(art)
    art.remove()
    art.set_transform(ax2.transData)
    ax2.add_artist(art)
plt.show()