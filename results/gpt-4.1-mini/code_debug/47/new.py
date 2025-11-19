import matplotlib.pyplot as plt
import numpy as np

train_predictions_std_dev = 0.18179760873317719
test_predictions_std_dev  = 0.1591469645500183

train_data_model_corr =  0.9759789999233454
test_data_model_corr  = -0.9616011980701071

degrees =  90 if (train_data_model_corr > 0) and (test_data_model_corr > 0) else 180

std_ref = 1.0 
models_std_dev = [train_predictions_std_dev, test_predictions_std_dev]
models_corr    = [train_data_model_corr    , test_data_model_corr    ]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_thetalim(thetamin=0, thetamax=degrees)
ax.set_theta_zero_location('E')
ax.set_theta_direction(1)

ax.xaxis.grid(color='blue')
correlation_range = np.arange(0 if degrees == 90 else -1, 1.1, 0.1)
ax.set_xticks(np.arccos(correlation_range))
ax.set_xticklabels([f'{c:.1f}' for c in correlation_range], color='blue', fontsize=10 if degrees == 90 else 7)

ax.yaxis.grid(color='black')
ax.set_ylim(0, max(models_std_dev) * 1.2)  # Set lower limit to 0 for proper y-axis

yticks = np.arange(0, max(models_std_dev) * 1.2 + 0.01, 0.1)
ax.set_yticks(yticks)

if degrees == 180:
    for tick in yticks:
        if tick != 0.0:
            # Place negative labels on the left side (theta=pi) aligned with ticks
            ax.text(np.pi, tick, f'-{tick:.1f}', ha='center', va='center', color='black', fontsize=10)

ax.set_xlabel('Standard Deviation')
ax.xaxis.set_label_coords(0.5, 0.15 if degrees == 180 else -0.1)
if degrees == 90:
    ax.set_ylabel('Standard Deviation', labelpad=4)
if degrees == 90:
    ax.text(np.pi / 4.2, 0.26, 'Pearson Correlation Coefficient', ha='center', va='center', color='blue', rotation=-45)
elif degrees == 180:
    ax.text(np.pi / 2, 0.27, 'Pearson Correlation Coefficient', ha='center', va='bottom', color='blue')

ax.set_title('Taylor Diagram')

ax.plot(np.arccos(models_corr), models_std_dev, 'ro', label='Models')
ax.plot([0], [std_ref], 'mo', label='Reference')
plt.legend()

ax.text(np.arccos(train_data_model_corr), train_predictions_std_dev + 0.005, 'train', ha='center', va='bottom')
ax.text(np.arccos(test_data_model_corr), test_predictions_std_dev + 0.005, 'test', ha='center', va='bottom')

fig.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
