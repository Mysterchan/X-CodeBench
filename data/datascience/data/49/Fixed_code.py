import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

channel = ["Red", "Green", "Blue", "Red", "Green", "Blue", "Red", "Green", "Blue"]
average= [83.438681, 36.512924, 17.826646, 83.763724, 36.689707, 17.892932, 84.747069, 37.072383, 18.070416]
sd = [7.451285, 3.673155, 1.933273, 7.915111, 3.802536, 2.060639, 7.415741, 3.659094, 2.020355]
conc = ["0.00", "0.00", "0.00", "0.25", "0.25", "0.25", "0.50", "0.50", "0.50"]

df = pd.DataFrame({"channel": channel,
                  "average": average,
                  "sd" : sd,
                  "conc": conc})

order = ["0.00", "0.25", "0.50"]
sns.barplot(x="conc", y="average", hue="channel", data=df, ci=None, 
            order=order)


conc2=[0,0,0,1,1,1,2,2,2]
width = .25
add = [-1*width, 0 , width, -1*width, 0 , width, -1*width, 0 , width,]
x = np.array(conc2)+np.array(add)

plt.errorbar(x = x, y = df['average'],
            yerr=df['sd'], fmt='none', c= 'black', capsize = 2)
plt.show()