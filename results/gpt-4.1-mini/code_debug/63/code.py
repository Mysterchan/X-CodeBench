import matplotlib.pyplot as plt

x = ["A","B","C","D","E","F","G","H"]
y = [-25, -10, 5, 10, 30, 40, 50, 60]
colors = ["yellow","limegreen","green","blue","red","brown","grey","black"]

bars = plt.bar(x, height=y, color=colors, alpha=0.8)

# Add legend with category labels and colors
plt.legend(bars, x, title="Category")

plt.xlim((-0.5, 7.5))
plt.show()