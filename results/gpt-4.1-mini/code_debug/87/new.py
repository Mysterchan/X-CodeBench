import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import numpy as np

np.random.seed(0)

ratings = ['AA', 'A', 'B', 'C', 'D', 'E', 'HR']
samples = np.repeat(ratings, np.random.randint(10, 100, len(ratings)))
np.random.shuffle(samples)
clean_loan_data = pd.DataFrame({'ProsperRating': samples})

plt.figure(figsize = [10, 8])
sb.countplot(data = clean_loan_data, x = 'ProsperRating', order=ratings)
plt.xlabel('Prosper Rating')
plt.ylabel('Count')
plt.title('Prosper Rating Counts')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
