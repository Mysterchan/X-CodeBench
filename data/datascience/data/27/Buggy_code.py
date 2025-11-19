import numpy as np
from matplotlib import pyplot as plt

def hanging_line(point1, point2):
    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], 100)
    y = a*np.cosh(x) + b

    return (x,y)

n_teams = 4
n_weeks = 4

fig, ax = plt.subplots(figsize=(6,6))

t = np.array([
    [1, 2, 4, 3],
    [4, 3, 3, 2],
    [3, 4, 1, 4],
    [2, 1, 2, 1]
])

fig.patch.set_facecolor('#1b1b1b')

for nw in range(n_weeks):
    ax.scatter([nw] * n_weeks, t[:, nw], marker='o', color='#4F535C', s=100, zorder=2)
    
ax.axis('off')
    
for team in t:
    x1, x2 = 0, 1
    
    for rank in range(0, len(team) - 1):
        y1 = n_weeks - team[rank] + 1
        y2 = n_weeks - team[rank + 1] + 1
        x, y = hanging_line([x1, y1], [x2, y2])
        ax.plot(x, y, color='#4F535C', zorder=1)
        x1 += 1
        x2 += 1

plt.show()