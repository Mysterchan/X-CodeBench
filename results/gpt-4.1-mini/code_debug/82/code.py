import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dta = pd.DataFrame(columns=["Date", "Fruit", "type"], data=[
    ['2017-01-01','Orange', 'FP'], ['2017-04-01','Orange', 'CP'], ['2017-07-01','Orange', 'CP'], 
    ['2017-10-08','Orange', 'CP'], ['2017-01-01','Apple', 'NP'], ['2017-04-01','Apple', 'CP'], 
    ['2017-07-01','Banana', 'NP'], ['2017-10-08','Orange', 'CP']
])
dta['quarter'] = pd.PeriodIndex(dta.Date, freq='Q')

# Create the catplot with swarm kind
g = sns.catplot(x="quarter", y="Fruit", hue="type", kind="swarm", data=dta)

ax = g.ax

# Map quarters to their numeric positions on the x-axis
quarter_order = sorted(dta['quarter'].unique())
quarter_to_x = {q: i for i, q in enumerate(quarter_order)}

# Map fruits to their y-axis positions
fruit_order = dta['Fruit'].unique()
fruit_to_y = {fruit: i for i, fruit in enumerate(ax.get_yticklabels())}
# Actually get the y positions from the axis ticks
yticks = ax.get_yticks()
yticklabels = [tick.get_text() for tick in ax.get_yticklabels()]
fruit_to_y = {fruit: yticks[yticklabels.index(fruit)] for fruit in fruit_order}

# Map types to colors from the legend
legend = ax.get_legend()
type_to_color = {}
for legline, legtext in zip(legend.get_lines(), legend.get_texts()):
    type_to_color[legtext.get_text()] = legline.get_color()

# For each fruit and type, find the min and max quarter and draw a horizontal line connecting them
for fruit in dta['Fruit'].unique():
    for t in dta['type'].unique():
        subset = dta[(dta['Fruit'] == fruit) & (dta['type'] == t)]
        if len(subset) > 1:
            # Get numeric x positions for min and max quarter
            min_q = subset['quarter'].min()
            max_q = subset['quarter'].max()
            x_start = quarter_to_x[min_q]
            x_end = quarter_to_x[max_q]
            y = fruit_to_y[fruit]
            ax.hlines(y, x_start, x_end, color=type_to_color[t], linewidth=2)

plt.show()