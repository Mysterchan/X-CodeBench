import sys
input = sys.stdin.readline

MOD = 998244353

N, a, b = map(int, input().split())
Q = int(input())
ks = list(map(int, input().split()))

# Предварительно вычислим необходимые значения для каждого k:
# Для уровня k L-образная фигура существует только если:
# 1 ≤ k ≤ N
# и (a,b) входит в фигуру уровня k, то есть k ≤ min(a,b,N - a +1, N - b +1)
# иначе ответ 0

# Количество способов разбить сетку на L-образные фигуры уровней 1..N:
# Для каждого уровня k существует 4*(N - k +1)^2 вариантов расположения L-образной фигуры уровня k.
# Итого общее число способов:
# total_ways = Π_{k=1}^N [4*(N - k +1)^2] = 4^N * (N!)^2

# Для фиксированного k_i, чтобы (a,b) входила в L-образную фигуру уровня k_i,
# количество вариантов для фигуры уровня k_i = количество вариантов L-образной фигуры уровня k_i, содержащей (a,b).
# Для фигуры уровня k_i, количество таких вариантов = количество позиций (i,j) центра фигуры,
# при которых (a,b) входит в фигуру.
# По условию, для уровня k_i, центр (i,j) должен удовлетворять одному из 4 условий,
# и (a,b) должно быть в фигуре, то есть:
# (a,b) ∈ фигура с центром (i,j) => i ≤ a ≤ i + k_i -1 и j ≤ b ≤ j + k_i -1 (для варианта вниз-вправо)
# Аналогично для других 3 вариантов.

# Количество центров (i,j) для уровня k_i, содержащих (a,b):
# Для каждого из 4 вариантов:
# - вниз-вправо: i in [a - (k_i -1), a], j in [b - (k_i -1), b], with i,j in [1, N - k_i +1]
#   count = max(0, min(a, N - k_i +1) - max(1, a - k_i +1) +1) *
#           max(0, min(b, N - k_i +1) - max(1, b - k_i +1) +1)
# - вниз-влево: i in [a - (k_i -1), a], j in [b, b + k_i -1], j in [k_i, N]
#   count = max(0, min(a, N - k_i +1) - max(1, a - k_i +1) +1) *
#           max(0, min(N, b + k_i -1) - max(k_i, b) +1)
# - вверх-вправо: i in [a, a + k_i -1], i in [k_i, N], j in [b - (k_i -1), b]
#   count = max(0, min(N, a + k_i -1) - max(k_i, a) +1) *
#           max(0, min(b, N - k_i +1) - max(1, b - k_i +1) +1)
# - вверх-влево: i in [a, a + k_i -1], i in [k_i, N], j in [b, b + k_i -1], j in [k_i, N]
#   count = max(0, min(N, a + k_i -1) - max(k_i, a) +1) *
#           max(0, min(N, b + k_i -1) - max(k_i, b) +1)

# Суммируем эти 4 варианта - это количество центров фигуры уровня k_i, содержащих (a,b).

# Для остальных уровней j != k_i, количество вариантов расположения фигуры уровня j = 4*(N - j +1)^2

# Итого ответ для k_i:
# ways = (кол-во центров для k_i) *
#        Π_{j=1..N, j!=k_i} 4*(N - j +1)^2
#      = (кол-во центров для k_i) * (4^N * (N!)^2) / (4*(N - k_i +1)^2)
#      = (кол-во центров для k_i) * 4^{N-1} * (N!)^2 / (N - k_i +1)^2

# Для вычисления факториала и степени 4 используем предвычисления.

maxN = N

# Предвычисление факториалов и обратных элементов по модулю
fact = [1]*(maxN+1)
for i in range(2, maxN+1):
    fact[i] = fact[i-1]*i % MOD

inv_fact = [1]*(maxN+1)
inv_fact[maxN] = pow(fact[maxN], MOD-2, MOD)
for i in range(maxN-1, 0, -1):
    inv_fact[i] = inv_fact[i+1]*(i+1) % MOD

def modinv(x):
    return pow(x, MOD-2, MOD)

# 4^N mod
pow4 = pow(4, N, MOD)
pow4_minus_1 = pow(4, N-1, MOD) if N > 0 else 1

# (N!)^2 mod
fact_sq = fact[N]*fact[N] % MOD

def count_centers(k):
    # вниз-вправо
    i1 = max(1, a - k +1)
    i2 = min(a, N - k +1)
    j1 = max(1, b - k +1)
    j2 = min(b, N - k +1)
    c1 = max(0, i2 - i1 +1)*max(0, j2 - j1 +1)

    # вниз-влево
    i1 = max(1, a - k +1)
    i2 = min(a, N - k +1)
    j1 = max(k, b)
    j2 = min(N, b + k -1)
    c2 = max(0, i2 - i1 +1)*max(0, j2 - j1 +1)

    # вверх-вправо
    i1 = max(k, a)
    i2 = min(N, a + k -1)
    j1 = max(1, b - k +1)
    j2 = min(b, N - k +1)
    c3 = max(0, i2 - i1 +1)*max(0, j2 - j1 +1)

    # вверх-влево
    i1 = max(k, a)
    i2 = min(N, a + k -1)
    j1 = max(k, b)
    j2 = min(N, b + k -1)
    c4 = max(0, i2 - i1 +1)*max(0, j2 - j1 +1)

    return (c1 + c2 + c3 + c4) % MOD

for k_i in ks:
    # Проверяем, входит ли (a,b) в фигуру уровня k_i
    # Если k_i > min(a,b,N - a +1, N - b +1), то ответ 0
    if k_i > a or k_i > b or k_i > N - a +1 or k_i > N - b +1:
        print(0)
        continue

    c = count_centers(k_i)
    if c == 0:
        print(0)
        continue

    denom = (N - k_i +1)**2 % MOD
    denom_inv = modinv(denom)
    # ways = c * 4^{N-1} * (N!)^2 / denom
    ans = c * pow4_minus_1 % MOD
    ans = ans * fact_sq % MOD
    ans = ans * denom_inv % MOD
    print(ans)