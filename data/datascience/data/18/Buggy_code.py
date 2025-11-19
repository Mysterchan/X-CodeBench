import random
from matplotlib import pyplot

fig, axes = pyplot.subplots()

upper_bound = 1.0

x = [random.uniform(0.0, upper_bound) for x in range(1000)]
y = [random.uniform(0.0, upper_bound) for x in range(1000)]
pyplot.plot(x, y, 'o')
axes.set_xscale("symlog")
axes.set_yscale("symlog")

pyplot.show()