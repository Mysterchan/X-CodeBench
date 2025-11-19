mod = 998244353
table_size = 10**6

fac = [1] * (table_size + 1)
finv = [1] * (table_size + 1)

for i in range(2, table_size + 1):
    fac[i] = fac[i - 1] * i % mod
finv[table_size] = pow(fac[table_size], mod - 2, mod)
for i in range(table_size - 1, -1, -1):
    finv[i] = finv[i + 1] * (i + 1) % mod

def rebuild(n):
    global table_size, fac, finv
    old_size = table_size
    new_size = n + 10**4
    fac.extend([0] * (new_size - old_size))
    finv.extend([0] * (new_size - old_size))
    for i in range(old_size + 1, new_size + 1):
        fac[i] = fac[i - 1] * i % mod
    finv[new_size] = pow(fac[new_size], mod - 2, mod)
    for i in range(new_size - 1, old_size, -1):
        finv[i] = finv[i + 1] * (i + 1) % mod
    table_size = new_size

def binom(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    if n > table_size:
        rebuild(n)
    return fac[n] * finv[k] % mod * finv[n - k] % mod

def calc1_sub(N, M, K, L):
    P = N + M - K - L + 2
    if P <= 0:
        return 0
    res = 0
    k_start = max(-(10**5), -(N + K - 1) // P if P > 0 else -(10**5))
    k_end = min(10**5, (N + M - K + 1) // P if P > 0 else 10**5)
    for k in range(k_start, k_end + 1):
        val1 = binom(N + M, N + k * P)
        val2 = binom(N + M, K - 1 + k * P)
        res = (res + val1 - val2) % mod
    return res

def calc1(T, N, S, G):
    if not (0 <= S <= N) or not (0 <= G <= N):
        return 0
    if (T + (S - G)) & 1:
        return 0
    H = (T + S - G) // 2
    W = (T - (S - G)) // 2
    K = H - S
    L = W - N + S
    return calc1_sub(H, W, K, L)

H, W, T, A, B, C, D = map(int, input().split())

resX = [calc1(t, H - 1, A - 1, C - 1) for t in range(T + 1)]
resY = [calc1(t, W - 1, B - 1, D - 1) for t in range(T + 1)]

cumX = [0] * (T + 1)
cumY = [0] * (T + 1)

for i in range(1, T + 1):
    for j in range(1, i + 1):
        cumX[i] = (cumX[i] + resX[j] * binom(i, j)) % mod
        cumY[i] = (cumY[i] + resY[j] * binom(i, j)) % mod

ans = 0
sgn = 1
for i in range(T, 0, -1):
    ans = (ans + sgn * cumX[i] * cumY[i] % mod * binom(T, i)) % mod
    sgn = -sgn

print(ans % mod)