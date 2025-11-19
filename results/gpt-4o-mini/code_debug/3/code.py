import matplotlib.pyplot as plt
import numpy as np

res = [[1, 0], [0, 0.0], [0, 1.0], [0, 0], [0, 0.0], [0, 0], [0, 0], [0, 0], [0, 0.0]]

fig, ax = plt.subplots(1,1)
yticks = ['init', 'full :D', 'satisfied :)', 'hungry :(', 'starving :((', 'rawr', 'hunt >:D', 'desparate hunt!', 'dead...']
ax.set_yticks(np.arange(len(yticks)))  # Set y-ticks to match length of yticks
ax.set_yticklabels(yticks)

ax.imshow(res, cmap='hot', interpolation='nearest', aspect="equal")
plt.xlabel("steps")
plt.ylabel("states")
plt.show()