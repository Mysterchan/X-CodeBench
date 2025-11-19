import seaborn as sns
tips = sns.load_dataset('tips')
sns.lineplot(data=tips, x='day', y='total_bill', linewidth=0)
