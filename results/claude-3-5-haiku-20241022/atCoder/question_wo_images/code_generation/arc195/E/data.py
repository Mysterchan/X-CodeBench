MOD = 998244353

def solve():
    N, Q = map(int, input().split())
    A = [0, 0] + list(map(int, input().split()))  # A[2], A[3], ..., A[N]
    
    # Precompute factorials
    fact = [1] * N
    for i in range(1, N):
        fact[i] = fact[i-1] * i % MOD
    
    for _ in range(Q):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        
        result = 0
        
        # For each vertex i >= 2, calculate contribution of edge (i, parent(i))
        for i in range(2, N + 1):
            # Count number of trees where edge from i to its parent is on path from u to v
            # This happens when i is on the path from u to v
            
            if i == u or i == v:
                # Edge from i is always used (i is endpoint)
                # Number of such trees = (i-1) * (N-1)! / (N-1) = (i-1)!*(N-i)!*(i-1)
                count = (i - 1) * fact[N - 1] % MOD
            elif u < i < v:
                # i is between u and v, on path when i is ancestor of exactly one
                # Count = 2 * (i-1)! * (N-i)! (by symmetry and combinatorics)
                count = 2 * fact[i - 1] * fact[N - i] % MOD
            elif i < u:
                # i < u < v: i on path when i is ancestor of exactly one of u, v
                count = 2 * fact[i - 1] * fact[N - i] % MOD
            else:  # i > v
                # u < v < i: i cannot be on path from u to v
                count = 0
            
            result = (result + A[i] * count) % MOD
        
        print(result)

solve()