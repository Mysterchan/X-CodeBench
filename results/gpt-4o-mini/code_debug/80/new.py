import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.lineplot(data=tips, x='day', y='total_bill', estimator='mean', ci='sd', lw=0)  # Set line width to 0 to hide the mean line
plt.fill_between(tips['day'].unique(), tips.groupby('day')['total_bill'].mean() - tips.groupby('day')['total_bill'].std(),
                 tips.groupby('day')['total_bill'].mean() + tips.groupby('day')['total_bill'].std(), color='blue', alpha=0.2)  # Add confidence interval area
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
