import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

labels = ['abc','def','ghi','jkl','mno']
actual = [36,35,41,36,33]
target = [31,39,32,37,37]

data_dict_people = {'Labels':labels,'Actual':actual,'Target':target}
df_people_nps_graph = pd.DataFrame(data = data_dict_people)

index_labels = ['a', 'b', 'c', 'd', 'e']
nps_data_table = [[81,85,77,87,82],[89,89,90,89,89],[93,91,94,99,94],[85,86,86,86,86],[81,87,96,90,91]]
df_people_nps_table = pd.DataFrame(data = nps_data_table, columns=labels, index=index_labels)

nps_colors = []
for i in range(0,len(nps_data_table)):
    nps_colors.append(['#000000']*len(nps_data_table[0]))

matplotlib.rc_file_defaults()
sns.set_theme(style="ticks", 
                context="talk", 
                rc={'axes.facecolor':'#0E1117', 
                'figure.facecolor':'#0E1117', 
                'text.color':'white',
                'font.size':14,
                'axes.labelcolor':'white',
                'xtick.color': 'white'})

fig = plt.figure(constrained_layout = True)
subfigs = fig.subfigures(2,1, height_ratios=[1,1], hspace=0)

ax1 = subfigs[0].subplots(1,1,sharey=True)
bp = sns.barplot(data = df_people_nps_graph, x='Labels', y='Actual', alpha=0.8, ax=ax1, color='grey', label='Actual') 
lp = sns.lineplot(data = df_people_nps_graph, x='Labels', y='Target', marker='o', sort = False, ax=ax1, alpha=0.8, color='green', linewidth=7, label='Target')

ax2 = subfigs[1].subplots()
p_table = ax2.table(cellText = df_people_nps_table.values, rowLabels=df_people_nps_table.index, colLabels=df_people_nps_table.columns, bbox=[0, 0, 1, 1], cellColours=nps_colors, rowColours=['#000000']*len(nps_data_table), colColours=['#000000']*len(nps_data_table[0]), edges='horizontal')
p_table.set_fontsize(12)

ax1.grid(False)
ax1.set(ylim=(0,df_people_nps_graph['Actual'].max()*1.2),
        xlabel=None, 
        yticklabels=[], 
        xticks=[], 
        ylabel=None)
ax1.bar_label(ax1.containers[0])
ax1.margins(x=0.02)
ax1.legend(loc='upper center', ncol=2, fontsize=14, frameon=False, bbox_to_anchor=(0.5, 1.1)) 
sns.despine(left=True)
plt.tight_layout()
plt.axis('off')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
