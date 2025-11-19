N, Q = map(int, input().split())
A = [0, 0] + list(map(int, input().split()))
mod = 998244353

# Precompute factorials
fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % mod

# Precompute modular inverses for 1 to N
inv = [0, 1] + [0] * (N - 1)
for i in range(2, N + 1):
    inv[i] = mod - (mod // i) * inv[mod % i] % mod

# Precompute prefix sum v
v = [0] * (N + 1)
for x in range(2, N):
    # w = x * (x + 1)
    # p = 2 * (x - 1) / w = 2 * (x - 1) / (x * (x + 1))
    # Using precomputed inverses
    inv_x = inv[x]
    inv_x1 = inv[x + 1]
    p = 2 * (x - 1) % mod * inv_x % mod * inv_x1 % mod
    v[x] = (v[x - 1] + p * A[x] % mod) % mod

# Process queries
for _ in range(Q):
    a, b = map(int, input().split())
    result = 0
    z = max(a, b)
    
    for x in range(a, z + 1):
        if x == b:
            result = (result + A[x]) % mod
        elif x > a:
            result = (result + inv[x] * A[x]) % mod
        elif x == a:
            p = (x - 1) * inv[x] % mod
            result = (result + p * A[x]) % mod
    
    result = (result + v[a - 1]) % mod
    result = result * fact[N - 1] % mod
    print(result)