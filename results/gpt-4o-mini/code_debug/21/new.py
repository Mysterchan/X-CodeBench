import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3']
yesterday_test1_mean = [20, 12, 23]
yesterday_test2_mean = [21, 14, 25]
today_test1_mean = [18, 10, 12]
today_test2_mean = [13, 13, 9]

x = np.arange(len(labels))
width = 0.3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Yesterday's data
ax1.bar(x - width/2, yesterday_test1_mean, width, label='Test 1', color='blue')
ax1.bar(x + width/2, yesterday_test2_mean, width, label='Test 2', color='orange')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_title("Yesterday's Data")
ax1.legend()

# Today's data
ax2.bar(x - width/2, today_test1_mean, width, label='Test 1', color='blue')
ax2.bar(x + width/2, today_test2_mean, width, label='Test 2', color='orange')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_title("Today's Data")
ax2.legend()

plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
