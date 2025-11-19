import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1)
axes[1].axvline(15, ymin=0, ymax=1, color='red', lw=10) # wrong parameter
plt.ylim([0, 11])
plt.show()