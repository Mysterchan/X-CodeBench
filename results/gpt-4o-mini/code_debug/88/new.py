import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import FancyBboxPatch

mydict = {
    'Event': ['Running', 'Swimming', 'Biking', 'Hiking'],
    'Completed': [2, 4, 3, 7],
    'Participants': [10, 20, 35, 10]}

df = pd.DataFrame(mydict).set_index('Event')
df = df.assign(Completion=(df.Completed / df.Participants) * 100)

plt.subplots(figsize=(5, 2))

sns.set_color_codes("pastel")
ax = sns.barplot(x=df.Completion, y=df.index, orient='h')

# Modify the patches to have rounded edges
for patch in ax.patches:
    bb = patch.get_bbox()
    color = patch.get_facecolor()
    rounded_patch = FancyBboxPatch((bb.xmin, bb.ymin),
                                    abs(bb.width), abs(bb.height),
                                    boxstyle="round,pad=0.01,rounding_size=0.2",
                                    ec="none", fc=color)
    patch.remove()
    ax.add_patch(rounded_patch)

sns.despine(left=True, bottom=True)
ax.tick_params(axis='both', which='both', length=0)
plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
