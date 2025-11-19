mod = 998244353

def binom(n, k):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    for j in range(1, k + 1):
        numerator = numerator * (n - j + 1) % mod
        denominator = denominator * j % mod
    return numerator * pow(denominator, mod - 2, mod) % mod

def calc(T, N, S, G):
    if not (0 <= S <= N) or not (0 <= G <= N) or (T + (S - G)) % 2 != 0:
        return 0
    H = (T + S - G) // 2
    W = (T - (S - G)) // 2
    if H < 0 or W < 0:
        return 0
    K = H - S
    L = W - N + S
    return binom(H + W, H) * binom(N + M - K - L, N) % mod if K >= 0 and L >= 0 else 0

H, W, T, A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1

resX = [0] * (T + 1)
resY = [0] * (T + 1)
for t in range(T + 1):
    resX[t] = calc(t, H - 1, A, C)
    resY[t] = calc(t, W - 1, B, D)

ans = 0
sgn = 1
for i in range(T, 0, -1):
    X = sum(resX[j] * binom(i, j) % mod for j in range(i + 1)) % mod
    Y = sum(resY[j] * binom(i, j) % mod for j in range(i + 1)) % mod
    ans = (ans + sgn * X * Y % mod * binom(T, i)) % mod
    sgn = -sgn

print(ans)