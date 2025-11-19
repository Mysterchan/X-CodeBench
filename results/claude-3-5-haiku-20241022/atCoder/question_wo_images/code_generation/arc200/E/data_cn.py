MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def comb(n, r, mod=MOD):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    num = 1
    den = 1
    for i in range(r):
        num = num * ((n - i) % mod) % mod
        den = den * ((i + 1) % mod) % mod
    return num * modinv(den, mod) % mod

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = pow(2, M, MOD) * comb(M + 1, N, MOD) % MOD
    print(result)