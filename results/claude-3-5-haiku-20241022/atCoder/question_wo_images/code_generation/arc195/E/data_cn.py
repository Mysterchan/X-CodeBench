MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve():
    N, Q = map(int, input().split())
    A = [0, 0] + list(map(int, input().split()))
    
    # Precompute factorials
    fact = [1] * N
    for i in range(1, N):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * N
    inv_fact[N-1] = modinv(fact[N-1])
    for i in range(N-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    for _ in range(Q):
        u, v = map(int, input().split())
        
        if u > v:
            u, v = v, u
        
        # Calculate the sum of distances
        total = 0
        
        # For each vertex i from 2 to N, calculate contribution
        for i in range(2, N + 1):
            # Count trees where edge (P_i, i) is on path from u to v
            
            # Case 1: i is on the path and P_i < i
            # One of u, v is in subtree of i, the other is not
            
            # Count configurations where i is ancestor of exactly one of u, v
            if i == u or i == v:
                # If i is u or v, edge is used when P_i is ancestor of the other vertex
                other = v if i == u else u
                
                if other < i:
                    # P_i must equal other or be ancestor of other
                    # Count: configurations where path goes through this edge
                    count = fact[N-2]
                    total = (total + A[i] * count) % MOD
                else:
                    # other > i, so i < other
                    # P_i can be 1 to i-1
                    # Edge used when other is descendant of i
                    # Probability other is in subtree rooted at i
                    count = fact[N-2]
                    total = (total + A[i] * count) % MOD
            else:
                # i is neither u nor v
                # Edge (P_i, i) is on path iff exactly one of u,v is in subtree of i
                
                if i < u:
                    # i < u < v, so both u,v > i
                    # Both could be descendants of i
                    # P(both in subtree) + P(neither in subtree) = no contribution
                    # P(exactly one in subtree) contributes
                    count = fact[N-2]
                    total = (total + A[i] * count) % MOD
                elif u < i < v:
                    # u < i < v
                    count = fact[N-2]
                    total = (total + A[i] * count) % MOD
                else:
                    # i > v, so i > u and i > v
                    count = fact[N-2]
                    total = (total + A[i] * count) % MOD
        
        print(total)

solve()