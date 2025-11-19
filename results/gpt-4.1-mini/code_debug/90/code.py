import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.lineplot(x='size', y='total_bill', data=tips, marker='o', err_style='bars', linestyle='')

plt.show()