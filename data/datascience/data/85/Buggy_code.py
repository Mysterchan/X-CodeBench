import seaborn as sns
group = ['Simple', 'Simple', 'Complex', 'Complex', 'Cool']
alg = ['Alg 1', 'Alg 2', 'Alg 3', 'Alg 4', 'Alg 2']
results = [i+1 for i in range(len(group))]
sns.barplot(x=group, y=results, hue=alg)