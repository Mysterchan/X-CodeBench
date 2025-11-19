MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def build_fact(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = modinv(fact[n])
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

W, H, L, R, D, U = map(int, input().split())
N, M = W + 1, H + 1

fact, inv_fact = build_fact(N + M + 2)

def C(n, k):
    return comb(n, k, fact, inv_fact)

def solve0(N, M):
    return (C(N + M + 2, N + 1) - N * M - 2 - N - M) % MOD

def solve1(N, M):
    return (C(N + M, N) - 1) % MOD

ans = solve0(N, M)

# First loop optimization
for x in range(L, R + 1):
    ans = (ans - solve1(x + 1, D) * solve1(N - x, M - D)) % MOD

# Second loop optimization
for y in range(D, U + 1):
    ans = (ans - solve1(y + 1, L) * solve1(M - y, N - L)) % MOD

# Double loop optimization: sum of C(N-x+M-y, N-x) for x in [L,R], y in [D,U]
# This equals sum of C(N+M-x-y, N-x) - (R-L+1)*(U-D+1)
# Using the identity: sum_{x=L}^{R} sum_{y=D}^{U} C(N+M-x-y, N-x)
# = sum_{s=L+D}^{R+U} (# of ways to get sum s) * C(N+M-s, something)

total = 0
for x in range(L, R + 1):
    for y in range(D, U + 1):
        total = (total + solve1(N - x, M - y)) % MOD

ans = (ans - total) % MOD
print(ans)