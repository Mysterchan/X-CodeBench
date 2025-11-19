import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'X': [13, 13, 13, 12, 11], 'Y':[14, 11, 13, 15, 20], 'NumberOfPlanets':[2, 5, 2, 1, 2]}
cts = pd.DataFrame(data=data)

plt.figure(figsize=(10,10))
sns.scatterplot(data=cts, x='X', y='Y', size='NumberOfPlanets', sizes=(50,500), legend=False)
sns.lineplot(data=cts.sort_values('X'), x='X', y='Y', estimator=None, color='blue')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
