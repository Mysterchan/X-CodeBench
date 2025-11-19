import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    "domain": ["econ", "econ", "public_affairs", "culture", "communication", 
               "public_affairs", "communication", "culture", "public_affairs", 
               "econ", "culture", "econ", "communication"],
    "score": [0.25, 0.3, 0.5684, 0.198, 0.15, 0.486, 0.78, 0.84, 0.48, 
              0.81, 0.1, 0.23, 0.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add the "All" category
df_all = pd.DataFrame({"domain": ["All"] * len(df), "score": df["score"]})
df_combined = pd.concat([df_all, df], ignore_index=True)

# Create the boxplot
plt.figure(figsize=(8, 6))
ax = sns.boxplot(x="score", y="domain", data=df_combined, 
                 order=["All", "econ", "public_affairs", "culture", "communication"],
                 palette={"All": "gray", "econ": "C0", "public_affairs": "C1", 
                          "culture": "C2", "communication": "C3"})
                 
# Create a horizontal line to separate "All" from the other domains
plt.axhline(y=0.5, color='k', linestyle='-')

# Display the plot
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
