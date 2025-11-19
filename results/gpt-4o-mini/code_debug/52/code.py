import seaborn as sns
import matplotlib.pyplot as plt

cm = [[1102, 88],
      [85, 725]]
ax = plt.subplot()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)  # Set fmt='d' to display integers
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_ylim(2.0, 0)
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(['Fake', 'Real'])
ax.yaxis.set_ticklabels(['Fake', 'Real'])

plt.show()