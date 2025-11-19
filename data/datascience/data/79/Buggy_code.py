import seaborn as sns
data = {"domain": ["econ", "econ", "public_affairs", "culture", "communication", "public_affairs", "communication",  "culture", "public_affairs", "econ",  "culture", "econ", "communication"],
        "score": [0.25, 0.3, 0.5684, 0.198, 0.15, 0.486, 0.78, 0.84, 0.48, 0.81, 0.1, 0.23, 0.5]}
ax = sns.boxplot(x="score", y="domain", data=data)