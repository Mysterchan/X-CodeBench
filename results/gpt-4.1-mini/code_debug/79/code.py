import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {"domain": ["econ", "econ", "public_affairs", "culture", "communication", "public_affairs", "communication",  "culture", "public_affairs", "econ",  "culture", "econ", "communication"],
        "score": [0.25, 0.3, 0.5684, 0.198, 0.15, 0.486, 0.78, 0.84, 0.48, 0.81, 0.1, 0.23, 0.5]}

df = pd.DataFrame(data)

# Create a new dataframe for the "All" category with all scores
all_df = pd.DataFrame({
    "domain": ["All"] * len(df),
    "score": df["score"]
})

# Combine the original and "All" dataframes
combined_df = pd.concat([all_df, df], ignore_index=True)

# Set the order so "All" appears at the top
order = ["All"] + sorted(df["domain"].unique())

ax = sns.boxplot(x="score", y="domain", data=combined_df, order=order, palette="pastel")

# Add a horizontal line to separate "All" from the other domains
# The y-axis is categorical, so the line should be between "All" and "econ"
# The y positions are 0 for "All", 1 for "econ", etc.
ax.axhline(0.5, color='black', linewidth=1)

plt.show()