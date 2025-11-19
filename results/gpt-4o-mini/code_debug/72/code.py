import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

data = {
    11: [-3, 4, 1, -6],
    22: [5, 3, -2, 4],
    33: [7, 8, 1, -4],
    44: [8, 1, -4, 9],
    55: [-9, 4, 8, -4],
    66: [4, 4, 8, 2],
    77: [7, -12, -8, -6]
}
hehe = pd.DataFrame(data, index=["s1", "s2", "s3", "s4"])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 4), gridspec_kw={'width_ratios': (1, 15)})
sns.heatmap(hehe, ax=ax2, cbar=False, cmap="coolwarm", linewidth=1, vmin=-25, vmax=25)
ax2.set_aspect("equal")
ax2.set_title("A", fontsize=20, pad=30)

plt.colorbar(plt.cm.ScalarMappable(cmap="coolwarm", norm=mpl.colors.Normalize(vmin=-25, vmax=25)), cax=ax1)
ax1.yaxis.set_ticks_position('left')

# Add significance stars
ax2.text(0.5, -0.1, '*', ha='center', va='center', transform=ax2.transAxes, fontsize=15)
ax2.text(1.5, -0.1, '*', ha='center', va='center', transform=ax2.transAxes, fontsize=15)

plt.show()