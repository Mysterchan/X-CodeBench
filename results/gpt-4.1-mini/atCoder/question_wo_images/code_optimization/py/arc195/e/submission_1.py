import sys
input = sys.stdin.readline

mod = 998244353

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Precompute factorials and inverse factorials
fact = [1] * (N + 1)
inv_fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % mod
inv_fact[N] = pow(fact[N], mod - 2, mod)
for i in range(N - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

# Precompute prefix sums v[x] = sum_{i=2}^x [2*(i-1)/(i*(i+1)) * A_i] mod
# Note: 2*(i-1)/(i*(i+1)) mod = 2*(i-1)*inv(i)*inv(i+1) mod
v = [0] * (N + 1)
for x in range(2, N):
    val = 2 * (x - 1) % mod
    val = val * pow(x, mod - 2, mod) % mod
    val = val * pow(x + 1, mod - 2, mod) % mod
    val = val * A[x - 2] % mod
    v[x] = (v[x - 1] + val) % mod
v[N] = v[N - 1]  # For convenience

# Precompute prefix sums of A for quick sum queries
prefixA = [0] * (N + 1)
for i in range(2, N + 1):
    prefixA[i] = (prefixA[i - 1] + A[i - 2]) % mod

# Precompute inverses of 1..N for quick access
inv = [0] * (N + 2)
for i in range(1, N + 2):
    inv[i] = pow(i, mod - 2, mod)

factN_1 = fact[N - 1]

for _ in range(Q):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    # Compute result as per formula:
    # result = fact[N-1] * (v[a-1] + sum_{x=a}^{b-1} (1/x)*A_x + A_b) mod
    # sum_{x=a}^{b-1} (1/x)*A_x = prefix weighted sum difference

    # sum_{x=a}^{b-1} (1/x)*A_x
    # We'll compute on the fly since no prefix for (1/x)*A_x is precomputed

    # To optimize, precompute prefix of (1/x)*A_x
    # But since Q is large, precomputing prefix for all x is expensive
    # Instead, precompute prefix of A and use formula:
    # sum_{x=a}^{b-1} (1/x)*A_x = sum_{x=2}^{b-1} (1/x)*A_x - sum_{x=2}^{a-1} (1/x)*A_x

# So precompute prefix sums of (1/x)*A_x for x=2..N
prefix_invA = [0] * (N + 1)
for i in range(2, N + 1):
    prefix_invA[i] = (prefix_invA[i - 1] + inv[i] * A[i - 2]) % mod

# Now process queries
for _ in range(Q):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    # sum_{x=a}^{b-1} (1/x)*A_x = prefix_invA[b - 1] - prefix_invA[a - 1]
    s = (prefix_invA[b - 1] - prefix_invA[a - 1]) % mod

    # result = fact[N-1] * (v[a-1] + s + A[b-1]) mod
    res = (v[a - 1] + s + A[b - 1]) % mod
    res = res * factN_1 % mod
    print(res)