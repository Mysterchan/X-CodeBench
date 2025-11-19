import matplotlib.pyplot as plt

fig, ax = plt.subplots(4, 1, sharex=True)

for i in range(4):
    ax[i].set_ylim((-300, 300))  # Set the desired y-limits correctly
    ax[i].set_ylabel(f"axis {i}")

plt.tight_layout()  # Correct placement of tight_layout to ensure proper spacing
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
