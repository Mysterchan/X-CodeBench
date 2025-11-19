import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    N, Q = map(int, sys.stdin.readline().split())
    A = [0] + list(map(int, sys.stdin.readline().split()))  # A[2..N], A[1]=0 for convenience

    # Precompute factorials and inverse factorials modulo MOD
    # factorials up to N-1
    fact = [1] * (N)
    for i in range(2, N):
        fact[i] = fact[i-1] * i % MOD

    # Precompute inverse factorials using Fermat's little theorem
    inv_fact = [1] * (N)
    inv_fact[N-1] = pow(fact[N-1], MOD-2, MOD)
    for i in reversed(range(1, N-1)):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    # Combination function modulo MOD
    def comb(n, k):
        if k > n or k < 0:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

    # Precompute prefix sums of A
    prefixA = [0] * (N+1)
    for i in range(2, N+1):
        prefixA[i] = (prefixA[i-1] + A[i]) % MOD

    # Precompute factorials for (N-1)! and (N-2)!
    factN_1 = fact[N-1]  # (N-1)!
    factN_2 = fact[N-2] if N >= 2 else 1  # (N-2)!

    # For each query (u,v), compute:
    # sum over all P of dist(u,v) in T(P) modulo MOD
    # dist(u,v) = sum of A_i over edges on path u-v
    # sum over all P of dist(u,v) = (N-2)! * sum_{i=u+1}^v A_i * (i-1)*(N - i)
    # modulo MOD

    for _q in range(Q):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        # sum over i in (u+1..v) of A_i * (i-1)*(N - i)
        # compute sum_i = sum_{i=u+1}^v A_i * (i-1)*(N - i)
        # We can compute directly in O(v-u) but that can be large.
        # So we need a prefix sums approach.

        # Precompute prefix sums of A_i*(i-1)*(N - i)
        # We'll do it once before queries.

        # So let's precompute once outside the queries:
        # prefixW[i] = sum_{j=2}^i A_j * (j-1)*(N-j)
        # Then sum_i = prefixW[v] - prefixW[u]

        # So we move this precomputation outside the loop.

    # Precompute prefixW
def precompute():
    import sys
    MOD = 998244353
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    fact = [1] * (N)
    for i in range(2, N):
        fact[i] = fact[i-1] * i % MOD

    factN_2 = fact[N-2] if N >= 2 else 1

    prefixW = [0] * (N+1)
    for i in range(2, N+1):
        val = A[i] * (i-1) % MOD
        val = val * (N - i) % MOD
        prefixW[i] = (prefixW[i-1] + val) % MOD

    for _ in range(Q):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        res = (prefixW[v] - prefixW[u]) % MOD
        res = res * factN_2 % MOD
        print(res)

threading.Thread(target=precompute).start()