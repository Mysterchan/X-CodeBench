import matplotlib.pyplot as plt

res = [[1, 0], [0, 0.0], [0, 1.0], [0, 0], [0, 0.0], [0, 0], [0, 0], [0, 0], [0, 0.0]]

fig, ax = plt.subplots(1,1)
yticks = ['init', 'full :D', 'satisfied :)', 'hungry :(', 'starving :((', 'rawr', 'hunt >:D', 'desparate hunt!', 'dead...']

ax.imshow(res, cmap='hot', interpolation='nearest', aspect="equal")
ax.set_yticks(range(len(yticks)))
ax.set_yticklabels(yticks)

plt.xlabel("steps")
plt.ylabel("states")
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
