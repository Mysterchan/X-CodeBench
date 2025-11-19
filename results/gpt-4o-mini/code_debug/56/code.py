import seaborn as sns
import matplotlib.pyplot as plt

# Load the exercise dataset
exercise = sns.load_dataset("exercise")

# Group by diet and kind, normalizing to get percentages
plot = exercise.groupby(['diet', 'kind']).size().reset_index(name='count')
plot['percentage%'] = plot['count'] / plot.groupby('diet')['count'].transform('sum') * 100

# Create a stacked bar plot using the count instead of percentage
g = sns.catplot(x="diet", y="count", hue="kind", data=plot, kind='bar', height=5, aspect=1)

# Adjust the y-axis to show the percentage
g.set_ylabels("Count")

plt.show()