def max_sum_after_operations(N, A):
    S = []
    for i in range(N):
        if A[i] > 0:
            S.append(A[i])
        elif S:
            S.pop()
    return sum(S)

# Чтение входных данных
N = int(input())
A = list(map(int, input().split()))

# Вывод результата
print(max_sum_after_operations(N, A))