import matplotlib.pyplot as plt

gender = ['M', 'F']
numbers = [1644, 1771]
bars = plt.bar(gender, numbers, width=0.4, align='center')

for i in range(len(numbers)):
    plt.annotate(str(numbers[i]), xy=(gender[i], numbers[i]), ha='center', va='bottom')

plt.show()