import matplotlib.pyplot as plt

fig, ax = plt.subplots(4, 1, sharex=True)

for i in range(4):
    ax[i].set_ylim((-300, 300))
    ax[i].set_yticks([-300, 0, 300])  # add ticks
    ax[i].set_ylabel(f"axis {i}")
fig.tight_layout()
plt.show()