N, Q = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353

# Precompute factorials and inverse factorials
factorials = [1] * (N + 1)
inv_factorials = [1] * (N + 1)

for i in range(2, N + 1):
    factorials[i] = factorials[i - 1] * i % mod

inv_factorials[N] = pow(factorials[N], mod - 2, mod)
for i in range(N - 1, 0, -1):
    inv_factorials[i] = inv_factorials[i + 1] * (i + 1) % mod

# Precompute the prefix sums
v = [0] * (N + 1)
for x in range(2, N + 1):
    w = x * (x + 1) % mod
    p = pow(w, mod - 2, mod)
    p = 2 * (x - 1) * p % mod
    v[x] = (v[x - 1] + p * A[x - 2]) % mod

# Process queries
results = []
for _ in range(Q):
    a, b = map(int, input().split())
    result = (v[b] - v[a] + mod) % mod  # Path contribution between a and b
    result = result * inv_factorials[N - 1] % mod  # Scale by (N-1)!
    results.append(result)

print('\n'.join(map(str, results)))