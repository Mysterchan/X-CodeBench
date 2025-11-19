import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator


x = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
this = [1, 1, 1, 1, 1, 1, 1, 1]
peng = [0.502922572, 0.501331171, 0.500245216, 0.499974978, 0.498864, 0.500255225, 0.499174273, 0.500185163]
qiu = [0.6528, 0.6384, 0.6368, 0.6384,  0.648, 0.6288, 0.6384, 0.648]

fig, ax = plt.subplots()
plt.plot(x, this, marker='o', label='Proposed', color='#E71F19', linewidth=1.5, markersize=4, clip_on=False)  # missing parameter
plt.plot(x, peng, marker='s', label='[1]', color='#000000', linewidth=1.5, markersize=4, clip_on=False) # missing parameter
plt.plot(x, qiu, marker='^', label='[2]', color='#FF8C00', linewidth=1.5, markersize=4, clip_on=False) # missing parameter

plt.xlabel('Scaling ratio')
plt.ylabel('NC')

plt.xscale('log')
plt.xlim(0.0001, 10)
plt.xticks([1e-4, 1e-3, 1e-2, 1e-1, 1, 1e1, 1e2, 1e3],
           ['$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$10^{1}$', '$10^{2}$', '$10^{3}$', '$10^{4}$'])

plt.ylim(0, 1.)
plt.yticks([i / 10 for i in range(11)], fontsize=10)

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

plt.gca().xaxis.set_minor_locator(NullLocator())
plt.gca().spines['top'].set_visible(False)

plt.legend(fontsize=10, loc='lower right', frameon=False)
plt.gca().add_patch(plt.Rectangle((0, 0), 1, 1, fill=True, color='none'))

plt.gcf().set_facecolor('none')

plt.show()