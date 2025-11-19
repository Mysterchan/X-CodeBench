import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


fig, ax = plt.subplots(1,1, figsize = (20, 5), facecolor = "k")

ax.set_facecolor('k')
ax.tick_params(axis='both', colors='w', labelsize = 20, size = 5, width = 2)
ax.spines[['left', 'right', 'top', 'bottom']].set_color('w')
ax.spines[['left', 'right', 'top', 'bottom']].set_lw(3)
ax.tick_params(axis = 'both', pad = 5, labelfontfamily = 'sans-serif')


ax.set_xlim(15000, 17000)
ax.set_ylim(0, 1.1)

ax.set_xticklabels(ax.get_xticks()/10000)

x1, x2, y1, y2 = 16360, 16555, 0.45, 1.06
axins_1 = ax.inset_axes([15850, 1.22, 1150, 0.7], xlim=(x1, x2), ylim=(y1, y2), 
                      transform = ax.transData, facecolor = 'k')

axins_1.tick_params(axis='both', direction = 'inout', color='w', labelsize = 14, size = 7, width = 2)
axins_1.spines[['top','bottom','left','right']].set_linewidth(2)
axins_1.spines[['left', 'right', 'top', 'bottom']].set_color('w')

axins_1.set_xticklabels(axins_1.get_xticks()/10000)

box, connectors = ax.indicate_inset_zoom(axins_1, edgecolor="w", lw = 2, alpha = 0.75)

connectors[0].set_visible(False)
verts_box_top_LH = connectors[0].get_path().vertices

connectors[1].set_visible(False)
verts_ax_bottom_LH = connectors[1].get_path().vertices

con_1 = ConnectionPatch(xyA = (verts_box_top_LH[0]), xyB = (verts_ax_bottom_LH[2]),
                      coordsA = ax.transData, coordsB = ax.transData,
                      color ="w", lw = 2, alpha = 0.75, zorder = 1)

fig.add_patch(con_1)      # wrong function

connectors[3].set_visible(False)
verts_box_top_RH = connectors[3].get_path().vertices
connectors[2].set_visible(False)
verts_ax_bottom_RH = connectors[2].get_path().vertices

con_2 = ConnectionPatch(xyA = (verts_box_top_RH[2]), xyB = (verts_ax_bottom_RH[0]),
                      coordsA = ax.transData, coordsB = ax.transData,
                      color ="w", lw = 2, alpha = 0.75, zorder = 1)

fig.add_artist(con_2)


x1, x2, y1, y2 = 15675, 15850, 0.57, 1.06
axins_2 = ax.inset_axes([15000, -1.07, 2000, 0.7], xlim=(x1, x2), ylim=(y1, y2), 
                      transform = ax.transData, facecolor = 'k')

axins_2.tick_params(axis='both', direction = 'inout', color='w', labelsize = 14, size = 7, width = 2)
axins_2.spines[['top','bottom','left','right']].set_linewidth(2)
axins_2.spines[['left', 'right', 'top', 'bottom']].set_color('w')

axins_2.set_xticklabels(axins_2.get_xticks()/10000)

box, connectors = ax.indicate_inset_zoom(axins_2, edgecolor="w", lw = 2, alpha = 0.75)

connectors[1].set_visible(False)
verts_box_bottom_LH = connectors[1].get_path().vertices
connectors[0].set_visible(False)
verts_ax_top_LH = connectors[0].get_path().vertices

con_3 = ConnectionPatch(xyA = (verts_box_bottom_LH[0]), xyB = (verts_ax_top_LH[2]),
                      coordsA = ax.transData, coordsB = ax.transData,
                      color ="w", lw = 2, alpha = 0.75, zorder = 1)

fig.add_artist(con_3)

connectors[2].set_visible(False)
verts_box_bottom_RH = connectors[2].get_path().vertices
connectors[3].set_visible(False)
verts_ax_top_RH = connectors[3].get_path().vertices

con_4 = ConnectionPatch(xyA = (verts_box_bottom_RH[2]), xyB = (verts_ax_top_RH[0]),
                      coordsA = ax.transData, coordsB = ax.transData,
                      color ="w", lw = 2, alpha = 0.75, zorder = 1)

fig.add_artist(con_4)

plt.setp(ax.get_yticklabels(), backgroundcolor="k", color = 'w')
plt.setp(ax.get_xticklabels(), backgroundcolor="k", color = 'w')

plt.setp(axins_1.get_yticklabels(), backgroundcolor="k", color = 'w')
plt.setp(axins_1.get_xticklabels(), backgroundcolor="k", color = 'w')

plt.setp(axins_2.get_yticklabels(), backgroundcolor="k", color = 'w')
plt.setp(axins_2.get_xticklabels(), backgroundcolor="k", color = 'w')

plt.show()
