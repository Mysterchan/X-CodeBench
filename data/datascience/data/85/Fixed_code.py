import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch

group = ['Simple', 'Simple', 'Complex', 'Complex', 'Cool']
alg = ['Alg 1', 'Alg 2', 'Alg 3', 'Alg 4', 'Alg 2']
colors = plt.cm.tab10.colors
alg_cat = pd.Categorical(alg)
alg_colors = [colors[c] for c in alg_cat.codes]

results = [i + 1 for i in range(len(group))]

dist_groups = 0.4 # distance between successive groups
pos = (np.array([0] + [g1 != g2 for g1, g2 in zip(group[:-1], group[1:])]) * dist_groups + 1).cumsum()
labels = [g1 for g1, g2 in zip(group[:-1], group[1:]) if g1 != g2] + group[-1:]
label_pos = [sum([p for g, p in zip(group, pos) if g == label]) / len([1 for g in group if g == label])
             for label in labels]
plt.bar(pos, results, color=alg_colors)
plt.xticks(label_pos, labels)
handles = [Patch(color=colors[c], label=lab) for c, lab in enumerate(alg_cat.categories)]
plt.legend(handles=handles)
plt.show()