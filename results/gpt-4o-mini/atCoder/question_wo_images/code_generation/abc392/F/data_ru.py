def insert_elements(N, P):
    A = []
    for i in range(1, N + 1):
        A.insert(P[i - 1] - 1, i)
    return A

# Чтение входных данных
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
P = list(map(int, data[1:]))

# Получение результата и вывод
result = insert_elements(N, P)
print(" ".join(map(str, result)))