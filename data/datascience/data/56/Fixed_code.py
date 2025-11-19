import seaborn as sns
import matplotlib.pyplot as plt
exercise = sns.load_dataset("exercise")
plot = exercise.groupby(['diet'])['kind'].value_counts(normalize=True).mul(100).reset_index(name='percentage')
g = sns.histplot(x = 'diet' , hue = 'kind',weights= 'percentage',
             multiple = 'stack',data=plot,shrink = 0.7)

plt.show()