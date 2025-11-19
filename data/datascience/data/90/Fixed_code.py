import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.lineplot(x='size', y='total_bill', data=tips, marker='o', linestyle='', err_style='bars')

plt.show()
