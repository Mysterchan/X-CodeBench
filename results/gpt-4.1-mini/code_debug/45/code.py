import numpy as np 
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
x = np.arange(0.1, 100, 0.1)
y = np.sin(x)

xlim = [1e-1, 1e2]

ax.plot(x, y)
ax.set_xlim(xlim)
ax.set_xscale('log')

ax2 = ax.twiny()
ax2.set_xscale('log')
ax2.set_xlim(xlim)

# Instead of tick_params, disable the top ticks and labels by setting the ticks and labels to empty lists
ax2.set_xticks([])
ax2.set_xticklabels([])

plt.show()