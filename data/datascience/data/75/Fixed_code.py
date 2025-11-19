import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
g = sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker",
)
g.ax_marg_x.remove()

plt.show()