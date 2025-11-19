import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

n_teams = 4
n_weeks = 4
t = np.array([[1, 2, 4, 3],
              [4, 3, 3, 2],
              [3, 4, 1, 4],
              [2, 1, 2, 1]])
fig, ax = plt.subplots(figsize=(10, 4), facecolor='#1b1b1b')
ax.set_facecolor('#1b1b1b')

indent = 0.8
for tj in t:
    ax.scatter(np.arange(len(tj)), tj, marker='o', color='#4F535C', s=100, zorder=3)
    # create bezier curves
    verts = [(i + d, tij) for i, tij in enumerate(tj) for d in (-indent, 0, indent)][1:-1]
    codes = [Path.MOVETO] + [Path.CURVE4] * (len(verts) - 1)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', lw=2, edgecolor='#4F535C')
    ax.add_patch(patch)
ax.set_xticks([])
ax.set_yticks([])
ax.autoscale() # sets the xlim and ylim for the added patches
plt.show()