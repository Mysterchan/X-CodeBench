import matplotlib.pyplot as plt

theta = [0, 1, 2, 3, 4, 5, 6]
r = [0, 1, 0.5, 1, 0.5, 1, 0]

plt.polar(theta, r)    # replace plt.title() order
plt.title("stuff")
plt.show()