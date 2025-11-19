import matplotlib.pyplot as plt

x = range(1,100)
y = range(1,100)

def my_plot_1(x, y, ax):
    ax.plot(x, y)

def my_plot_2(x, y, ax):
    ax.plot(x, y)

fig, axs = plt.subplots(ncols=2, nrows=1)

# pass the Axes you created above
my_plot_1(x, y, axs[0])
my_plot_2(x, y, axs[1])

plt.show()