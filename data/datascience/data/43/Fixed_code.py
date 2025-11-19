import matplotlib.pyplot as plt


vals = [600.0, 222.3, 139.8, 114.0, 90.8, 80.8, 70.7, 62.8, 55.5, 47.5]
RANGE = range(1, len(vals) + 1)
plt.plot(RANGE, vals)
plt.show()