import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.DataFrame({'Name': ['Alex', 'Bob', 'Sofia', 'Claire'], 'Age': [15, 18, 16, 22], 'Gender': ['M', 'M', 'F', 'F']})
df = pd.concat([df[df.Gender == 'M'], pd.DataFrame({'Name': [''], 'Age': [0], 'Gender': ['M']}), df[df.Gender == 'F']])

age_plot = sns.barplot(data=df, x="Name", y="Age", hue="Gender", dodge=False)
age_plot.get_legend().remove()
plt.setp(age_plot.get_xticklabels(), rotation=90)
plt.ylim(0, 40)
age_plot.tick_params(labelsize=14)
age_plot.tick_params(length=0, axis='x')
age_plot.set_ylabel("Age", fontsize=15)
age_plot.set_xlabel("", fontsize=1)
plt.tight_layout()
plt.show()