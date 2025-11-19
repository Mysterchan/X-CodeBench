import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
ax.plot(X, Ya)
filled_poly  = ax.fill_between(X, Ya, 0,
                 where = (X >=3.00) & (Ya<= 0),
                 color = 'b',alpha=.1)
(x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()

ax.text((x0 + x1) / 2, (y0 + y1) / 2, "Filled\npolygon", ha='center', va='center', fontsize=16, color='crimson')
plt.show()