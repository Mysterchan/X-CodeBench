import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import numpy as np

np.random.seed(0)

ratings = ['AA', 'A', 'B', 'C', 'D', 'E', 'HR']
samples = np.repeat(ratings, np.random.randint(10, 100, len(ratings)))
np.random.shuffle(samples)
clean_loan_data = pd.DataFrame({'ProsperRating': samples})

# Specify the order of the categories for the countplot
ordered_ratings = ['AA', 'A', 'B', 'C', 'D', 'E', 'HR']

plt.figure(figsize=[10, 8])
sb.countplot(data=clean_loan_data, x='ProsperRating', order=ordered_ratings)
plt.xlabel('Prosper Rating')
plt.ylabel('Count')
plt.title('Prosper Rating Counts')
plt.show()