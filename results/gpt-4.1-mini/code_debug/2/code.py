import matplotlib.pyplot as plt

theta = [0, 1, 2, 3, 4, 5, 6]
r = [0, 1, 0.5, 1, 0.5, 1, 0]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_title("stuff")
plt.show()