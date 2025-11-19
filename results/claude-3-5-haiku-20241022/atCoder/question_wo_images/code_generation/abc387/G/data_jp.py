MOD = 998244353

def pow_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def inv_mod(a, mod):
    return pow_mod(a, mod - 2, mod)

N = int(input())

# 2-edge-connected components can only have cycles of odd prime length
# A graph satisfies the condition iff all its 2-edge-connected components are trees or odd cycles

# For trees: all cycles have even length (not prime)
# For odd cycles of length p (prime): satisfies condition
# For even cycles: length is even (not prime if > 2)

# Key insight: A connected graph satisfies the condition iff it's a cactus graph
# where all cycles have odd prime length

# We need to count connected graphs where every 2-edge-connected component
# is either a single edge or an odd-length cycle

# Using exponential generating functions:
# Let T(x) = EGF for labeled trees = sum_{n>=1} n^{n-2} * x^n / n!
# Let C_p(x) = EGF for labeled cycles of prime length p

# For a cactus with odd prime cycles:
# We use the fact that such graphs can be built by:
# 1. Start with trees
# 2. Replace edges with odd prime cycles

# Actually, we need the EGF for "forests of cacti with odd prime cycles"
# Let F(x) be this EGF. Then connected cacti G(x) = log(F(x))

# For cacti where cycles have odd prime length:
# F(x) = exp(T(x) + sum_{p odd prime} C_p(x))

# T(x) for trees (rooted): T = x * exp(T)
# C_p(x) = x^p / (2p) for labeled cycles of length p

# Compute using DP on the EGF coefficients

fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact = [1] * (N + 1)
inv_fact[N] = inv_mod(fact[N], MOD)
for i in range(N - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# Sieve for primes
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

# Compute EGF coefficients
# F[n] = coefficient of x^n/n! in exp(sum over edges and odd prime cycles)
# Edge contribution: x^2/2
# Odd prime cycle of length p: x^p/(2p)

F = [0] * (N + 1)
F[0] = 1

# Contribution from edges and cycles
edge_cycle = [0] * (N + 1)
edge_cycle[2] = inv_mod(2, MOD)  # x^2/2 for edges

for p in range(3, N + 1, 2):
    if is_prime[p]:
        edge_cycle[p] = (edge_cycle[p] + inv_mod(2 * p, MOD)) % MOD

# F = exp(edge_cycle)
for i in range(1, N + 1):
    for j in range(i, 0, -1):
        F[j] = (F[j] + F[j - 1] * edge_cycle[1] * inv_mod(i, MOD)) % MOD
    for k in range(2, i + 1):
        F[i] = (F[i] + F[i - k] * edge_cycle[k] * inv_mod(i - k + 1, MOD)) % MOD

# Connected graphs: G[n] = n! * [x^n] log(F(x))
# log(F) computed from F
log_F = [0] * (N + 1)
for i in range(1, N + 1):
    log_F[i] = F[i] * i % MOD
    for j in range(1, i):
        log_F[i] = (log_F[i] - log_F[j] * F[i - j] % MOD) % MOD
    log_F[i] = log_F[i] * inv_mod(i, MOD) % MOD

result = log_F[N] * fact[N] % MOD
print(result)