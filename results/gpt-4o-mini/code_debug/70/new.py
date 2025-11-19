import seaborn as sns
import matplotlib.pyplot as plt

p = sns.load_dataset('penguins')
g = sns.displot(data=p, x='flipper_length_mm', 
                col='species', row='sex', 
                facet_kws=dict(margin_titles=True))

# Set margin titles color to red without affecting main titles
for ax in g.axes.flatten():
    # set margin title color
    ax.set_title(ax.get_title(), color='red' if ax.get_position().y0 < 0.5 else 'black')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
