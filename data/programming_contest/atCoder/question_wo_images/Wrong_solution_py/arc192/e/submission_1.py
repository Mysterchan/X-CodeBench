import sys
input = sys.stdin.readline

mod = 998244353

def power(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def C(n, m):
    if m > n: return 0
    return fac[n] * inv[m] % mod * inv[n-m] % mod

fac = [1] * (2 * 10 ** 6 + 5)
for i in range(1, 2 * 10 ** 6 + 5):
    fac[i] = fac[i-1] * i % mod

inv = [0] * (2 * 10 ** 6 + 5)
inv[2 * 10 ** 6] = power(fac[2 * 10 ** 6], mod - 2)
for i in range(2 * 10 ** 6 - 1, -1, -1):
    inv[i] = inv[i+1] * (i + 1) % mod

W, H, L, R, D, U = map(int, input().split())

w1, w2 = L, W - R
h1, h2 = D, H - U

if w1 + w2 == 0 or h1 + h2 == 0:
    print(0)
    exit()

ans = 0
for i in range(w1 + w2):
    for j in range(h1 + h2):
        ans = (ans + C(i + j + 1, i) * C(w1 + w2 + h1 + h2 - i - j, w1 + w2 - i)) % mod

print(ans)