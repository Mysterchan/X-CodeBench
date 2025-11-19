import matplotlib.pyplot as plt

def plot_vals(vals, RANGE):
    plt.grid()
    plt.xticks(RANGE)
    plt.plot(RANGE, vals, 'ro-')  # Change to plot with x values from RANGE

RANGE = range(1, 12)  # Adjust the RANGE to start from 1 and include 11

vals = [600.0, 222.3, 139.8, 114.0, 90.8, 80.8, 70.7, 62.8, 55.5, 47.5]
plot_vals(vals, RANGE)

plt.show()