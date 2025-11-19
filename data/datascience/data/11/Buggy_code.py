import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1)
axes[1].axvline(15, ymin=1, ymax=10, color='red', lw=10)
plt.ylim([0, 11])
plt.show()