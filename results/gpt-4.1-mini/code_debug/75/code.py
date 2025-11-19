import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')

g = sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker",
    marginal_ticks=False,
    marginal_kws=dict(bins=20, fill=True),
    kind="scatter",
    marginal="hist",
    marginal_pos="right"
)

# Remove the top marginal plot
g.ax_marg_x.remove()

plt.show()