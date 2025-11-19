import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.lineplot(x='size', y='total_bill', data=tips, marker='o', err_style='bars', linestyle='')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
