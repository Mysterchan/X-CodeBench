import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_style("darkgrid")
sns.histplot(data=tips, x="day", hue="sex", multiple="dodge", shrink=0.8, palette=["#F4A261", "#2A9D8F"])
plt.show()