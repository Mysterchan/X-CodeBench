import pandas as pd
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

# Create the barplot without confidence intervals
ax = sns.barplot(x="conc", y="average", hue="channel", data=df, ci=None, order=order)

# Add error bars manually using the precomputed standard deviations
for i in range(len(df)):
    # Get the x position of the bar
    # Bars are grouped by 'conc' and colored by 'channel'
    # We need to find the x coordinate of each bar to plot error bars
    # The bars are positioned with some offset for each hue level
    # We can get the positions from the patches in the axes
    bar = ax.patches[i]
    x = bar.get_x() + bar.get_width() / 2
    y = bar.get_height()
    err = df.loc[i, "sd"]
    ax.errorbar(x, y, yerr=err, fmt='none', c='black', capsize=5)

plt.show()