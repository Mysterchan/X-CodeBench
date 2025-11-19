import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scienceplots
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, ScalarFormatter
from mpl_toolkits.mplot3d import Axes3D

plt.style.use(["science", "grid", "no-latex"])

X, Y = np.meshgrid(np.linspace(51 / 98, 1, 15), np.linspace(1933 / 17, 275, 15))

U, MU = 20000, 10000
H0, H1, HG = 10, 5, 12
C0, C1 = 25, 30
G0, G = 20, 25
V, S = 8, 5
W = 150
M = 400
O = 10
E = 300

Qg = U * (1 - (W + HG - V) / (X * (E - V)))
qm = U * (1 - (C1 + H0 + G0 - V - O) / (X * (Y + G - V))) - Qg
qs = U * (1 - (C0 + H1 - S) / (X * (Y - S))) - qm - Qg
Qa = U * (1 - (W + HG - V) / (X * (E - V)))
qa = U * (1 - (C1 + G0 + H0 - V) / (X * (E - V))) - Qa

benchmark_profit_s = (Qa + qa) * (C1 - C0)
mainmodel_profit_s = (
    (C1 - C0) * Qg
    + (C1 - C0) * qm
    + (S + O - C0 - H1) * qs
    + X * (Y - S) * (qs - ((Qg + qm + qs) ** 2 - (Qg + qm) ** 2) / (2 * U))
)

fig = plt.figure(figsize=(7, 5.5))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Add rstride and cstride to reduce shading artifacts and set edgecolor to none
ax.plot_surface(X, Y, benchmark_profit_s, label="Benchmark", color="#111111", rstride=1, cstride=1, edgecolor='none')
ax.plot_surface(X, Y, mainmodel_profit_s, label="MainModel", color="#888888", rstride=1, cstride=1, edgecolor='none')

ax.invert_xaxis()
ax.set_xlabel("$\\rho$", size=22, labelpad=10)
ax.set_ylabel("$c_2$", size=22, labelpad=10)
ax.tick_params(labelsize=18)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(30))
ax.yaxis.set_minor_locator(MultipleLocator(30))
ax.zaxis.get_offset_text().set(size=18)
z_formatter = ScalarFormatter(useMathText=True)
z_formatter.set_scientific(True)
z_formatter.set_powerlimits((-2, 2))
z_axis = ax.get_zaxis()
z_axis.set_major_formatter(z_formatter)

colors = ["#111111", "#888888"]
legend_labels = ["$E\,\\Pi_{as}$", "$E\,\\Pi_s$"]
legend_handles = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
ax.legend(
    handles=legend_handles,
    labels=legend_labels,
    fontsize=20,
    frameon=True,
    fancybox=False,
    shadow=True,
    edgecolor="black",
    loc="lower right",
    bbox_to_anchor=(1.15, 0.78),
)

ax.view_init(elev=28, azim=-45)
plt.show()