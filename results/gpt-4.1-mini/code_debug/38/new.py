import matplotlib.pyplot as plt

gender = ['M', 'F']
numbers = [1644, 1771]
bars = plt.bar(gender, numbers, width=0.1, align='center')
for i, bar in enumerate(bars):
    plt.annotate(str(numbers[i]),
                 xy=(bar.get_x() + bar.get_width() / 2, numbers[i]),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
