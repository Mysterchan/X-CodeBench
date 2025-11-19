import numpy as np
from matplotlib import pyplot as plt

def hanging_line(point1, point2):
    # Use cosh on x shifted to start at 0 for smooth curves between points
    x_vals = np.linspace(0, 1, 100)
    a = (point2[1] - point1[1]) / (np.cosh(1) - 1)
    b = point1[1] - a * 1
    y_vals = a * np.cosh(x_vals) + b
    x_vals = x_vals + point1[0]  # shift x_vals to start at point1[0]
    return (x_vals, y_vals)

n_teams = 4
n_weeks = 4

fig, ax = plt.subplots(figsize=(8, 4))

t = np.array([
    [1, 2, 4, 3],
    [4, 3, 3, 2],
    [3, 4, 1, 4],
    [2, 1, 2, 1]
])

fig.patch.set_facecolor('#1b1b1b')
ax.set_facecolor('#1b1b1b')

# Plot points
for nw in range(n_weeks):
    ax.scatter([nw] * n_teams, n_weeks - t[:, nw] + 1, marker='o', color='#4F535C', s=100, zorder=2)

ax.axis('off')

# Plot curves
for team in t:
    for i in range(len(team) - 1):
        x1, x2 = i, i + 1
        y1 = n_weeks - team[i] + 1
        y2 = n_weeks - team[i + 1] + 1
        x, y = hanging_line([x1, y1], [x2, y2])
        ax.plot(x, y, color='#4F535C', zorder=1, lw=2)

plt.xlim(-0.1, n_weeks - 0.9)
plt.ylim(0.5, n_teams + 0.5)
plt.tight_layout()
plt.show()