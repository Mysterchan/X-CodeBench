import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N = int(input())

# Предварительно вычислим длины чисел от 1 до N
# и количество чисел каждой длины
# Максимальная длина числа N <= 2*10^5, значит длина <= 6 (т.к. 10^6 > 2*10^5)
max_len = len(str(N))

count_len = [0]*(max_len+1)
for x in range(1, N+1):
    l = len(str(x))
    count_len[l] += 1

# Предварительно вычислим факториалы и обратные факториалы для N!
fact = [1]*(N+1)
for i in range(2, N+1):
    fact[i] = fact[i-1]*i % MOD

# Предварительно вычислим степени 10^k mod MOD для k до max_len*N (максимальная длина результата)
# Максимальная длина результата - сумма длин всех чисел от 1 до N
# Но это слишком большое, поэтому будем считать по длинам и позициям

# Рассмотрим позицию числа в перестановке:
# f(P) = concat(P_1, P_2, ..., P_N)
# Значение f(P) = sum_{i=1}^N P_i * 10^{sum_{j=i+1}^N len(P_j)}

# Нам нужно сумму по всем перестановкам P:
# sum_{P} f(P) = sum_{P} sum_{i=1}^N P_i * 10^{sum_{j=i+1}^N len(P_j)}

# Рассмотрим фиксированную позицию i:
# sum_{P} P_i * 10^{sum_{j=i+1}^N len(P_j)}

# Для позиции i:
# - P_i пробегает все числа от 1 до N, каждое ровно (N-1)! раз (т.к. остальные позиции - перестановки из оставшихся)
# - Остальные позиции (кроме i) - перестановки из N-1 элементов

# Значит:
# sum_{P} P_i * 10^{sum_{j=i+1}^N len(P_j)} =
# (N-1)! * sum_{x=1}^N x * sum_{all sequences of lengths at positions j>i} 10^{sum of lengths}

# Но sum_{x=1}^N x = N(N+1)/2

# Теперь нужно вычислить sum_{all sequences of lengths at positions j>i} 10^{sum of lengths}

# Количество позиций справа от i: r = N - i

# Каждая позиция справа выбирает дли l with count count_len[l]

# Количество последовательностей длин длины r:
# total = (N-1)! (но мы считаем только суммы степеней 10^{sum lengths})

# Для суммирования по длинам используем генерацию многочлена:
# G(x) = sum_{l=1}^{max_len} count_len[l] * x^l
# Тогда сумма по всем последовательностям длины r:
# S_r = (G(10))^r

# Но G(10) = sum count_len[l] * 10^l

# В итоге:
# sum_{all sequences of lengths at positions j>i} 10^{sum lengths} = (G(10))^{r}

# Теперь итоговая формула:
# sum_{P} f(P) = sum_{i=1}^N (N-1)! * (N(N+1)/2) * (G(10))^{N - i}

# sum_{i=1}^N (G(10))^{N - i} = sum_{k=0}^{N-1} (G(10))^k = ( (G(10))^N - 1 ) / (G(10) - 1) если G(10) != 1

# Если G(10) = 1, то сумма = N

# Вычислим G(10):
G10 = 0
for l in range(1, max_len+1):
    # 10^l mod MOD
    pow10l = pow(10, l, MOD)
    G10 = (G10 + count_len[l]*pow10l) % MOD

# Вычислим сумму геометрической прогрессии:
if G10 == 1:
    sum_geom = N % MOD
else:
    sum_geom = (pow(G10, N, MOD) - 1) * pow(G10 - 1, MOD-2, MOD) % MOD

# Вычислим sum_x = sum_{x=1}^N x = N(N+1)/2 mod MOD
sum_x = N*(N+1)//2 % MOD

# Итог:
# sum_f = (N-1)! * sum_x * sum_geom mod MOD
ans = fact[N-1] * sum_x % MOD
ans = ans * sum_geom % MOD

print(ans)