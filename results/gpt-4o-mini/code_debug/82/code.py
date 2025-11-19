import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dta = pd.DataFrame(columns=["Date", "Fruit", "type"], data=[['2017-01-01','Orange', 
'FP'], ['2017-04-01','Orange', 'CP'], ['2017-07-01','Orange', 'CP'], 
['2017-10-08','Orange', 'CP'], ['2017-01-01','Apple', 'NP'], ['2017-04-01','Apple', 'CP'], 
['2017-07-01','Banana', 'NP'], ['2017-10-08','Orange', 'CP']
                                                        ])
dta['quarter'] = pd.PeriodIndex(dta.Date, freq='Q')

# Plotting the swarm plot
sns.catplot(x="quarter", y="Fruit", hue="type", kind="swarm", data=dta)

# Adding lines to connect the first and last points for each fruit type
for fruit in dta['Fruit'].unique():
    fruit_data = dta[dta['Fruit'] == fruit]
    first_point = fruit_data.iloc[0]
    last_point = fruit_data.iloc[-1]
    plt.plot([first_point['quarter'], last_point['quarter']], [first_point['Fruit'], last_point['Fruit']], marker='o', color='black')

plt.show()