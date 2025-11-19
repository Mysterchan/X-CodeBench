import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

def func(x):
    return (x-3)*(x+2)*(3*x+5)+25

a, b = 2, 9
x = np.linspace(0, 10, 30)
y = func(x)

fig, ax = plt.subplots(1, 1, dpi=135)
ax.plot(x, y, linewidth=2.5, color='c')

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.7', edgecolor='0.9')
ax.add_patch(poly)

ax.set_ylim(bottom=0)
ax.text(6.5, 150, r'$\int_a^b f(x)$', horizontalalignment='center', fontsize=15)

ax.set_xlabel('X', labelpad=10)  # Adjusted to have space between the label and x-axis
ax.set_ylabel('Y', rotation=0, labelpad=10)  # Adjusted to have space between the label and y-axis

ax.set_xticks((a, b))
ax.set_xticklabels(('a', 'b'))

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.set_yticks([])

plt.show()