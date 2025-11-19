import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))  # A[2..N], pad A[0], A[1]=0

# Precompute factorials and inverse factorials for (N-1)!
# But we only need (N-1)! modulo MOD once
fact = 1
for i in range(2, N):
    fact = fact * i % MOD

# Precompute prefix sums of A for distance calculation
# distance(u,v) = sum_{i=u+1}^{v} A_i (since u < v)
prefix = [0] * (N + 1)
for i in range(2, N + 1):
    prefix[i] = (prefix[i - 1] + A[i]) % MOD

# For each query (u,v), output (N-1)! * distance(u,v) mod MOD
for _ in range(Q):
    u, v = map(int, input().split())
    dist = (prefix[v] - prefix[u]) % MOD
    ans = dist * fact % MOD
    print(ans)