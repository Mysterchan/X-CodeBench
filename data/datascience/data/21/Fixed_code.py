import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3']
yesterday_test1_mean = [20, 12, 23]
yesterday_test2_mean = [21, 14, 25]
today_test1_mean = [18, 10, 12]
today_test2_mean = [13, 13, 9]

x = np.arange(len(labels))
width = 0.3

plt.figure(figsize=(12,5))

plt.subplot(121)
plt.bar(x-width/2, yesterday_test1_mean, width)
plt.bar(x+width/2, yesterday_test2_mean, width)    

plt.subplot(122)
plt.bar(x-width/2, today_test1_mean, width)
plt.bar(x+width/2, today_test2_mean, width)

plt.show()