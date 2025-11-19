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

# Hiding the top x ticks and labels
ax2.tick_params(top=False, labeltop=False) 
ax2.xaxis.set_tick_params(size=0)  # Disable the top ticks by setting their size to zero

plt.show()