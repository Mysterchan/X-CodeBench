import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 4, 2]
fig, ax = plt.subplots()
ax.plot(x, y, "-o")
ax.annotate("",
            xy=(x[3], y[3]),
            xytext=(x[1], y[1]),
            xycoords="data",
            arrowprops=dict(color="blue", arrowstyle="|-|"),
            textcoords="data",
            ha='center', va='bottom'
            )

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
