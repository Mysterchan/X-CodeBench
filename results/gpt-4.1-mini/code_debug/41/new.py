import matplotlib
from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np

x = [u'Rimegepant',u'Rimegepant',u'Zavegepant',u'Zavegepant',u'Troriluzole',u'Troriluzole',u'Troriluzole',u'Verdiperstat',u'Verdiperstat']
y = [4,3,3,3,2,3,3,3,3]
Disease = ['Acute Treatment of Migraine','Preventive Treatment of Migraine','Acute and Preventive Migraine','Lung Inflammation COVID-19',
           "Alzheimer's Disease", "OCD", "Spinocerebellar Ataxia", "Multiple System Atrophy", "Amyotrophic Lateral Sclerosis"]

fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the y locations for the groups
bars = ax.barh(ind, y, width, color="green", align='edge')
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plt.xticks(np.arange(5),('Pre-clinical','Phase I','Phase II','Phase III', 'Approved'))
plt.margins(0,0.05)
plt.title('BHVN')
plt.ylabel('Drug')

# Add disease names inside the bars
for bar, disease in zip(bars, Disease):
    width = bar.get_width()
    yloc = bar.get_y() + bar.get_height() / 2
    ax.text(width * 0.05, yloc, disease, va='center', ha='left', color='white', fontsize=9)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
