import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3, 3))
ax.annotate('', xy=(1, 2), xytext=(0, 1),
             arrowprops=dict(arrowstyle='->', color='blue', lw=2))
plt.xlim(-0.1, 1.1)
plt.ylim(0.9, 2.2)
plt.show()