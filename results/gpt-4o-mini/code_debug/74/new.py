import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns 

con_matrix = np.array([[55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
                       [0, 199, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
                       [0, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 4, 3],
                       [0, 0, 0, 1, 0, 35, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 5, 0, 26, 0, 0, 1, 0, 1, 0],
                       [0, 5, 0, 0, 0, 1, 0, 44, 0, 0, 3, 0, 1],
                       [0, 1, 0, 0, 0, 0, 0, 0, 52, 0, 0, 0, 0],
                       [0, 1, 0, 0, 2, 0, 0, 0, 0, 235, 0, 1, 1],
                       [1, 2, 0, 0, 0, 0, 0, 3, 0, 0, 34, 0, 3],
                       [0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 40, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 46]])

party_names = ['Blues', 'Browns', 'Greens', 'Greys', 'Khakis', 'Oranges', 
               'Pinks', 'Purples', 'Reds', 'Turquoises', 'Violets', 'Whites', 'Yellows']

sns.set()
my_mask = np.zeros((con_matrix.shape[0], con_matrix.shape[0]), dtype=int)
for i in range(con_matrix.shape[0]):
    for j in range(con_matrix.shape[0]):
        my_mask[i][j] = con_matrix[i][j] == 0 

fig_dims = (10, 10)
plt.subplots(figsize=fig_dims)
ax = sns.heatmap(con_matrix, annot=True, fmt="d", linewidths=.5, cmap="Pastel1",
                 cbar=False, mask=my_mask, vmax=15)

plt.xticks(ticks=np.arange(len(party_names)) + 0.5, labels=party_names, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(party_names)) + 0.5, labels=party_names, rotation='horizontal', va='center')
plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
