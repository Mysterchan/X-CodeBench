import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
g = sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker",
    marginal_kws=dict(bins=30, fill=True),
)
g.ax_marg_y.remove()  # Remove the top marginal histogram
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
