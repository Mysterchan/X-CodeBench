import matplotlib.pyplot as plt

x = ["A","B","C","D","E","F","G","H"]

y = [-25, -10, 5, 10, 30, 40, 50, 60]

w = [30, 20, 25, 40, 20, 40, 40, 30]

colors = ["yellow","limegreen","green","blue","red","brown","grey","black"]

w_new = [i/max(w) for i in w]
plt.bar(x, height = y, width = w_new, color = colors, alpha = 0.8)

plt.xlim((-0.5, 7.5))

