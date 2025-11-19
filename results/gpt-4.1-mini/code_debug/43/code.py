import matplotlib.pyplot as plt

def plot_vals(vals, RANGE):
    plt.grid()
    plt.xticks(RANGE)
    plt.plot(range(1, len(vals) + 1), vals, 'ro-')

RANGE = range(1, 11)

vals = [600.0, 222.3, 139.8, 114.0, 90.8, 80.8, 70.7, 62.8, 55.5, 47.5]
plot_vals(vals, RANGE)

plt.show()