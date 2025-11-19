import random
from matplotlib import pyplot

fig, axes = pyplot.subplots()

upper_bound = 1.0

x = [random.uniform(0.0, upper_bound) for _ in range(1000)]
y = [random.uniform(0.0, upper_bound) for _ in range(1000)]
axes.plot(x, y, 'o')
axes.set_xscale("symlog", linthresh=1e-3)
axes.set_yscale("symlog", linthresh=1e-3)

pyplot.show()