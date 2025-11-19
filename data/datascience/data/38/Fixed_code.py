import matplotlib.pyplot as plt

gender = ['M', 'F']
numbers = [1644, 1771]

plt.figure(figsize=(12, 6))
p = plt.bar(gender, numbers, width=0.1, bottom=None, align='center', data=None)

plt.bar_label(p)
plt.show()