import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Build the pandas Series from the table
win_corr = pd.Series(
    {
        "fruity": -0.380938,
        "hard": -0.310382,
        "pluribus": -0.247448,
        "nougat": 0.199375,
        "caramel": 0.213416,
        "crispedricewafer": 0.324680,
        "peanutyalmondy": 0.406192,
        "bar": 0.429929,
        "chocolate": 0.636517,
    },
    name="winpercent",
)

colors = ['black', 'red', 'green', 'orange', 'blue', 'limegreen', 'darkgreen', 'royalblue', 'navy']

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=win_corr.values, y=win_corr.index, orient="h", palette=colors, ax=ax)
ax.set_ylabel("")
ax.set_xlabel("Value")
ax.set_title("Correlation Coefficients for winpercent")
ax.bar_label(ax.containers[0], fmt="%.1f", label_type="center")

plt.tight_layout()
plt.show()