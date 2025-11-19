from matplotlib import pyplot as plt

data = [1, 5, 2, 1, 1, 4, 3, 1, 7, 8, 9, 6, 1]

fig, ax = plt.subplots()
ax.plot(data)
for side in ['top','right','bottom','left']:
    ax.spines[side].set_visible(False)
ax.tick_params(axis='both',which='both',labelbottom=False,bottom=False,left=False)
ax.set_yticks([min(data),max(data)])

plt.show()
