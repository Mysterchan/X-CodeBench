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
ax = sns.barplot(x=df.Completion, y=df.index, joinstyle='bevel')  # deleted parameter

new_patches = []
for patch in reversed(ax.patches):
    bb = patch.get_bbox()
    color = patch.get_facecolor()
    p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),
                            abs(bb.width), abs(bb.height),
                            boxstyle="round,pad=-0.0040,rounding_size=2",
                            ec="none", fc=color,
                            mutation_aspect=0.2     # Adjusted value
                            )
    patch.remove()
    new_patches.append(p_bbox)

for patch in new_patches:
    ax.add_patch(patch)

sns.despine(left=True, bottom=True)
ax.tick_params(axis=u'both', which=u'both', length=0)
plt.tight_layout()
plt.show()