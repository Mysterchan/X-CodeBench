import matplotlib.pyplot as plt
import seaborn as sns

data = {"domain": ["econ", "econ", "public_affairs", "culture", "communication", "public_affairs", "communication",  "culture", "public_affairs", "econ",  "culture", "econ", "communication"],
        "score": [0.25, 0.3, 0.5684, 0.198, 0.15, 0.486, 0.78, 0.84, 0.48, 0.81, 0.1, 0.23, 0.5]}
fig, axes = plt.subplots(2, 1, sharex=True,
                         gridspec_kw={'height_ratios': [1, 4], 'hspace': 0})
sns.set_style('white')
sns.boxplot(ax=axes[0], data=data["score"], orient="h", color='0.6')
axes[0].set_yticklabels(['All'])
sns.boxplot(ax=axes[1], x="score", y="domain", palette='Set2', data=data)
plt.tight_layout()
plt.show()