import matplotlib.pyplot as plt

x = range(1,100)
y = range(1,100)

def my_plot_1(x,y):
    fig = plt.plot(x,y)
    return fig

def my_plot_2(x,y):
    fig = plt.plot(x,y)
    return fig

my_fig_1 = my_plot_1(x,y)
my_fig_2 = my_plot_2(x,y)

fig, fig_axes = plt.subplots(ncols=2, nrows=1)
fig_axes[0] = my_fig_1
fig_axes[1] = my_fig_2

plt.show()