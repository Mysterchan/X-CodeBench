# Чтение входных данных
import sys

input = sys.stdin.read
data = input().strip().split('\n')

N = int(data[0])  # количество строк
strings = data[1:N + 1]  # строки

# Сортировка строк по длине
sorted_strings = sorted(strings, key=len)

# Конкатенация отсортированных строк
result = ''.join(sorted_strings)

# Вывод результата
print(result)