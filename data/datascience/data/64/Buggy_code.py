import seaborn as sns
from scipy.stats import gaussian_kde
from scipy.integrate import simps
import numpy as np
import matplotlib.pyplot as plt

df = sns.load_dataset('planets')
kde = gaussian_kde(df.mass.dropna())

fig, ax = plt.subplots(figsize=(9, 6))
g = sns.kdeplot(data=df.mass, ax=ax, c='k')