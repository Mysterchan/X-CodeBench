import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.pointplot(x='size', y='total_bill', data=tips, markers='o', ci='sd')

plt.show()