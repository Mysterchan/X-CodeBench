import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3, 3))
ax.arrow(0,1,1,1, head_width=0.2)  # missing parameter
plt.show()