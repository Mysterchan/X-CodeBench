import seaborn as sns
import matplotlib.pyplot as plt

p = sns.load_dataset("penguins")
grid = sns.displot(
    data=p,
    x="flipper_length_mm",
    col="species",
    row="sex",
    facet_kws=dict(margin_titles=True),
)
for margin_title in grid._margin_titles_texts:
    margin_title.set_color("red")