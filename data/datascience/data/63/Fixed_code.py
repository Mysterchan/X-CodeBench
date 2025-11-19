import matplotlib.pyplot as plt

x = ["A","B","C","D","E","F","G","H"]

y = [-25, -10, 5, 10, 30, 40, 50, 60]

w = [30, 20, 25, 40, 20, 40, 40, 30]

colors = ["yellow","limegreen","green","blue","red","brown","grey","black"]

#plt.bar(x, height = y, width = w, color = colors, alpha = 0.8)

xticks=[]
for n, c in enumerate(w):
    xticks.append(sum(w[:n]) + w[n]/2)
    
w_new = [i/max(w) for i in w]
a = plt.bar(xticks, height = y, width = w, color = colors, alpha = 0.8)
_ = plt.xticks(xticks, x)

plt.legend(a.patches, x)

import os
cur_dir = os.path.dirname(__file__)
plt.savefig(os.path.join(cur_dir, 'images','2.png'))