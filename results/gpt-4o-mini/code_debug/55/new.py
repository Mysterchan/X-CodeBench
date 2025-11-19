import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data  = {'year': [2016, 2013, 2014, 2015, 2016, 2013, 2014, 2015, 2016, 2013, 2014, 2015, 2016, 2013, 2014, 2015, 2016, 2013, 2014, 2015], 
          'geo_name': ['Michigan', 'Michigan', 'Michigan', 'Michigan', 
                       'Washtenaw County, MI', 'Washtenaw County, MI', 
                       'Washtenaw County, MI', 'Washtenaw County, MI', 
                       'Ann Arbor, MI', 'Ann Arbor, MI', 'Ann Arbor, MI', 
                       'Ann Arbor, MI', 'Philadelphia, PA', 'Philadelphia, PA', 
                       'Philadelphia, PA', 'Philadelphia, PA', 
                       'Ann Arbor, MI Metro Area', 'Ann Arbor, MI Metro Area', 
                       'Ann Arbor, MI Metro Area', 'Ann Arbor, MI Metro Area'], 
          'geo': ['04000US26', '04000US26', '04000US26', '04000US26', 
                  '05000US26161', '05000US26161', '05000US26161', '05000US26161', 
                  '16000US2603000', '16000US2603000', '16000US2603000', 
                  '16000US2603000', '16000US4260000', '16000US4260000', 
                  '16000US4260000', '16000US4260000', '31000US11460', 
                  '31000US11460', '31000US11460', '31000US11460'], 
          'income': [50803.0, 48411.0, 49087.0, 49576.0, 62484.0, 59055.0, 
                     60805.0, 61003.0, 57697.0, 55003.0, 56835.0, 55990.0, 
                     39770.0, 37192.0, 37460.0, 38253.0, 62484.0, 
                     59055.0, 60805.0, 61003.0], 
          'income_moe': [162.0, 163.0, 192.0, 186.0, 984.0, 985.0, 
                         958.0, 901.0, 2046.0, 1688.0, 1320.0, 1259.0, 
                         567.0, 424.0, 430.0, 511.0, 984.0, 985.0, 
                         958.0, 901.0]}
df = pd.DataFrame(data)

g = sns.catplot(x='year', y='income', data=df, kind='bar', hue='geo_name', legend=True)
g.map_dataframe(plt.bar, x='year', y='income', color='blue')

# Annotate bars with income values in 'K' format
for ax in g.axes.flat:
    for p in ax.patches:
        ax.annotate(f"{p.get_height() / 1000:.1f}K", 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', 
                    fontsize=10)

g.figure.set_size_inches(15, 8)
g.figure.subplots_adjust(top=0.81, right=0.86)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
