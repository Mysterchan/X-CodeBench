import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [['Alex', 25], ['Bob', 34], ['Sofia', 26], ["Claire", 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df["sex"] = ["male", "male", "female", "female"]

# Create a new x-axis variable that adds spacing between male and female groups
# Assign numeric positions with a gap between males and females
pos_map = {'Alex': 0, 'Bob': 1, 'Sofia': 3, 'Claire': 4}
df['pos'] = df['Name'].map(pos_map)

fig, ax = plt.subplots()

# Plot bars manually to control spacing
colors = {'male': sns.color_palette()[0], 'female': sns.color_palette()[1]}
for _, row in df.iterrows():
    ax.bar(row['pos'], row['Age'], color=colors[row['sex']], width=0.8)

# Set x-ticks and labels
ax.set_xticks(list(pos_map.values()))
ax.set_xticklabels(list(pos_map.keys()), rotation=90)

ax.set_ylim(0, 40)
ax.set_ylabel("Age", fontsize=15)
ax.tick_params(labelsize=14)
ax.set_xlabel("", fontsize=1)

plt.tight_layout()
plt.show()