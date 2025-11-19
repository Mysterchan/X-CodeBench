import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_style("darkgrid")
sns.histplot(data=tips, x="day", hue="sex", multiple="dodge", shrink=0.8, palette=["#F4A261", "#2A9D8F"])
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
