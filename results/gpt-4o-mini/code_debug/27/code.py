import numpy as np
from matplotlib import pyplot as plt

def smooth_line(x1, y1, x2, y2):
    # Create bezier curve control points for smooth transition
    control_x = [x1, (x1 + x2) / 2, x2]
    control_y = [y1, min(y1, y2) + 0.5, y2]  # Control point y-value above the min of y1, y2
    t = np.linspace(0, 1, 100)
    x = (1-t)**2 * control_x[0] + 2*(1-t)*t * control_x[1] + t**2 * control_x[2]
    y = (1-t)**2 * control_y[0] + 2*(1-t)*t * control_y[1] + t**2 * control_y[2]
    return x, y

n_teams = 4
n_weeks = 4

fig, ax = plt.subplots(figsize=(6, 6))

# Create a sample ranking data for 4 teams over 4 weeks
t = np.array([
    [1, 2, 4, 3],
    [4, 3, 3, 2],
    [3, 4, 1, 4],
    [2, 1, 2, 1]
])

fig.patch.set_facecolor('#1b1b1b')

# Plot the points for each team
for nw in range(n_weeks):
    ax.scatter([nw] * n_teams, t[:, nw], marker='o', color='#4F535C', s=100, zorder=2)

ax.axis('off')

# Draw smooth lines connecting the points
for team in t:
    for rank in range(len(team) - 1):
        x1, x2 = rank, rank + 1
        y1 = n_weeks - team[rank] + 1
        y2 = n_weeks - team[rank + 1] + 1
        x, y = smooth_line(x1, y1, x2, y2)
        ax.plot(x, y, color='#4F535C', zorder=1)

plt.show()