import seaborn as sns
import matplotlib.pyplot as plt


p = sns.load_dataset('penguins')
sns.displot(data=p, x='flipper_length_mm', 
            col='species', row='sex', 
            facet_kws=dict(margin_titles=True)
           )