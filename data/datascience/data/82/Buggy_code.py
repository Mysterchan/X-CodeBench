import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dta = pd.DataFrame(columns=["Date", "Fruit", "type"], data=[['2017-01-01','Orange', 
'FP'], ['2017-04-01','Orange', 'CP'], ['2017-07-01','Orange', 'CP'], 
['2017-10-08','Orange', 'CP'],['2017-01-01','Apple', 'NP'], ['2017-04-01','Apple', 'CP'], 
['2017-07-01','Banana', 'NP'], ['2017-10-08','Orange', 'CP']
                                                        ])
dta['quarter'] = pd.PeriodIndex(dta.Date, freq='Q')

sns.catplot(x="quarter", y="Fruit", hue="type", kind="swarm", data=dta)