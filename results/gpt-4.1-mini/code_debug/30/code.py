import matplotlib.pyplot as plt

x = range(1, 100)
y = range(1, 100)

def my_plot_1(ax, x, y):
    ax.plot(x, y)

def my_plot_2(ax, x, y):
    ax.plot(x, y)

fig, fig_axes = plt.subplots(ncols=2, nrows=1)

my_plot_1(fig_axes[0], x, y)
my_plot_2(fig_axes[1], x, y)

plt.show()