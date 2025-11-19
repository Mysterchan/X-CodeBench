import seaborn as sns
import matplotlib.pyplot as plt

p = sns.load_dataset('penguins')
g = sns.displot(data=p, x='flipper_length_mm', 
                col='species', row='sex', 
                facet_kws=dict(margin_titles=True)
               )

# Set margin titles color to red without affecting main titles
for ax in g.fig.axes:
    # Margin titles are the y-axis labels on the right (row facets)
    if ax.yaxis.get_label().get_text().startswith('sex ='):
        ax.yaxis.label.set_color('red')