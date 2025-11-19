from matplotlib import pyplot as plt

data = [1, 5, 2, 1, 1, 4, 3, 1, 7, 8, 9, 6, 1]
plt.plot(data)

ax = plt.gca()
# Set y-ticks to only min and max values
y_min, y_max = min(data), max(data)
ax.set_yticks([y_min, y_max])

# Hide y-axis line and all other ticks except min and max
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks_position('none')

# Hide x-axis line and ticks for a cleaner look (optional)
ax.spines['bottom'].set_visible(False)
ax.xaxis.set_ticks_position('none')

plt.show()