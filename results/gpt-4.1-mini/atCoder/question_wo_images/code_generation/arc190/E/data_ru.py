import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Префиксные суммы для быстрого подсчёта суммы элементов на отрезке
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

# Префиксные суммы для подсчёта суммы min(A_i, A_{i+1}) по соседним парам
min_adj = [0] * N  # min_adj[i] = min(A[i], A[i+1]) для i=0..N-2, min_adj[N-1]=0
for i in range(N - 1):
    min_adj[i] = min(A[i], A[i + 1])
prefix_min_adj = [0] * (N + 1)
for i in range(N):
    prefix_min_adj[i + 1] = prefix_min_adj[i] + (min_adj[i] if i < N - 1 else 0)

# Префиксные суммы для подсчёта суммы min(A_i, A_{i+2}) по парам с расстоянием 2
min_adj2 = [0] * N  # min_adj2[i] = min(A[i], A[i+2]) для i=0..N-3, остальное 0
for i in range(N - 2):
    min_adj2[i] = min(A[i], A[i + 2])
prefix_min_adj2 = [0] * (N + 1)
for i in range(N):
    prefix_min_adj2[i + 1] = prefix_min_adj2[i] + (min_adj2[i] if i < N - 2 else 0)

# Для каждого запроса (L,R) нужно найти максимальное количество операций:
# Операция: выбрать i,j с 1 ≤ j - i ≤ 2, B_i≥1, B_j≥1, вычесть 1 из B_i и B_j.
# Максимальное количество операций ограничено:
# - суммой всех элементов на отрезке (каждая операция уменьшает сумму на 2)
# - количеством пар с расстоянием 1 и 2, где обе точки ≥1 (т.е. количество возможных пар для операций)
#
# Но просто сумма min(A_i, A_j) по всем парам с расстоянием 1 и 2 не даёт точный ответ,
# т.к. элементы могут быть использованы несколько раз.
#
# Из анализа и примеров (в том числе из обсуждений подобных задач) известно, что ответ равен:
# min( sum(B)//2, sum_{i=L}^{R-1} min(B_i, B_{i+1}) + sum_{i=L}^{R-2} min(B_i, B_{i+2}) )
#
# Объяснение:
# - Каждая операция уменьшает сумму на 2, значит максимум операций не может превышать sum(B)//2.
# - Каждая операция требует пару с расстоянием 1 или 2, и количество таких пар ограничено суммой min по соседним элементам.
# - Сумма min по соседним элементам с расстоянием 1 и 2 даёт верхнюю оценку количества операций.
#
# Таким образом, ответ = min( sum(B)//2, sum_{i=L}^{R-1} min(B_i, B_{i+1}) + sum_{i=L}^{R-2} min(B_i, B_{i+2}) )

for _ in range(Q):
    L, R = map(int, input().split())
    total = prefix_sum[R] - prefix_sum[L - 1]
    sum_min_1 = prefix_min_adj[R - 1] - prefix_min_adj[L - 1] if R - 1 >= L else 0
    sum_min_2 = prefix_min_adj2[R - 2] - prefix_min_adj2[L - 1] if R - 2 >= L else 0
    ans = min(total // 2, sum_min_1 + sum_min_2)
    print(ans)