mod = 998244353

def precompute_factorials_and_inverses(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def solve(N, M, L, R, D, U):
    retu = comb(N + M - 2, N - 1, fact, inv_fact)
    retu -= N * M
    retu -= 2
    retu -= N + M
    retu %= mod
    return retu

W, H, L, R, D, U = map(int, input().split())
N, M = H + 1, W + 1

fact, inv_fact = precompute_factorials_and_inverses(N + M + 2, mod)

ans = solve(N, M, L, R, D, U)

for x in range(L, R + 1):
    ans -= comb(x, 1, fact, inv_fact) * comb(N - x, M - D, fact, inv_fact)
for y in range(D, U + 1):
    ans -= comb(y, 1, fact, inv_fact) * comb(M - y, N - L, fact, inv_fact)
for x in range(L, R + 1):
    for y in range(D, U + 1):
        ans -= comb(N - x, 1, fact, inv_fact) * comb(M - y, 1, fact, inv_fact)

ans %= mod
print(ans)