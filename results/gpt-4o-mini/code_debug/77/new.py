import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="day", hue="sex", multiple="dodge", binwidth=0.4)
plt.legend(title='sex')
plt.xlabel('day')
plt.ylabel('Count')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
