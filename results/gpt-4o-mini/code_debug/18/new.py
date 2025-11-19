import random
from matplotlib import pyplot

fig, axes = pyplot.subplots()

upper_bound = 1.0

x = [random.uniform(0.01, upper_bound) for _ in range(1000)]  # Change lower bound to avoid zero
y = [random.uniform(0.01, upper_bound) for _ in range(1000)]  # Change lower bound to avoid zero
pyplot.plot(x, y, 'o')
axes.set_xscale("symlog")
axes.set_yscale("symlog")

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
pyplot.savefig(output_path)
