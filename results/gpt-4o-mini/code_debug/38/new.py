import matplotlib.pyplot as plt

gender = ['M', 'F']
numbers = [1644, 1771]
bars = plt.bar(gender, numbers, width=0.4, align='center')

for i in range(len(numbers)):
    plt.annotate(str(numbers[i]), xy=(gender[i], numbers[i]), ha='center', va='bottom')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
