import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="day", hue="sex", multiple="dodge", shrink=.9)
plt.show()