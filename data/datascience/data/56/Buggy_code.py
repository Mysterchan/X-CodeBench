import seaborn as sns
import matplotlib.pyplot as plt
exercise = sns.load_dataset("exercise")
plot = exercise.groupby(['diet'])['kind'].value_counts(normalize=True).mul(100).reset_index(name='percentage%')
g = sns.catplot(x="diet", y="percentage%", hue="kind", data=plot, kind='bar')

plt.show()