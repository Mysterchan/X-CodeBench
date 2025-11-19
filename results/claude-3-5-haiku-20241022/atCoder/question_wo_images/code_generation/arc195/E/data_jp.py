MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve():
    N, Q = map(int, input().split())
    A = [0, 0] + list(map(int, input().split()))
    
    # For each query (u, v), we need to compute the sum of distances over all trees
    # The distance between u and v in a tree is the sum of edge weights on the path
    
    # Key insight: For each possible tree T(P), the path from u to v goes through their LCA
    # We need to count how many times each edge A_i contributes to the distance
    
    # For a given u and v, edge A_i (connecting i to P_i) contributes to the distance
    # if and only if i is on the path between u and v in tree T(P)
    
    # Let's think differently: for each edge A_i, count in how many trees it appears
    # on the path between u and v
    
    # The path from u to v passes through edge (i, P_i) if and only if:
    # - i is an ancestor of exactly one of {u, v} (or i is one of {u, v})
    
    # For each query, we need to count for each vertex i (2 <= i <= N):
    # In how many trees does the edge from i to P_i lie on the path from u to v?
    
    # Total number of trees = (N-1)!
    total_trees = 1
    for i in range(1, N):
        total_trees = (total_trees * i) % MOD
    
    for _ in range(Q):
        u, v = map(int, input().split())
        
        result = 0
        
        # For each vertex i (2 <= i <= N), we consider edge A_i
        for i in range(2, N + 1):
            # Edge A_i connects i to some parent P_i
            # This edge is on the path from u to v if:
            # - Removing this edge splits the tree into two components
            # - u and v are in different components
            
            # For vertex i, it can be placed in different positions
            # The edge from i to P_i is on the path u-v if:
            # - i is in the subtree of one of {u,v} but not both
            # - or i is an ancestor of exactly one of {u,v}
            
            # Count: in how many trees is edge i on path u-v?
            
            # Case analysis:
            # 1. If i == u or i == v: edge is on path if other endpoint is descendant/ancestor
            # 2. If i != u and i != v: edge is on path if i separates u and v
            
            # For tree T(P), edge (i, P_i) is on path u-v iff:
            # exactly one of {u, v} is in the subtree rooted at i
            
            if i == u or i == v:
                # If i is one of the endpoints
                other = v if i == u else u
                # Count trees where other is a descendant of i or i is descendant of other
                # This happens when i is an ancestor of other or vice versa
                
                # Count configurations where i is ancestor of other
                # or other is ancestor of i
                count = 0
                if i < other:
                    # i can be ancestor of other
                    # Count: other must have i in its ancestor chain
                    # Number of ways = (i-1)! * (N-other)! * (other-i-1)! * (other-i)
                    count = (total_trees * other) % MOD
                    count = (count * modinv(i)) % MOD
                else:
                    # other < i, so other can be ancestor of i
                    count = (total_trees * i) % MOD
                    count = (count * modinv(other)) % MOD
            else:
                # i is neither u nor v
                # Edge is on path if exactly one of u, v is descendant of i
                # Count such configurations
                
                # Prob that u is descendant of i = i / min(u, i) (approximately)
                # More precisely: count trees where i is ancestor of exactly one
                
                if i < u and i < v:
                    # i can be ancestor of both u and v
                    # Count where i is ancestor of exactly one
                    # = (ancestor of u only) + (ancestor of v only)
                    count = (total_trees * 2 * i) % MOD
                    count = (count * modinv(u)) % MOD
                    count = (count * modinv(v)) % MOD
                    count = (count * (u + v - 2 * i)) % MOD
                elif i > u and i > v:
                    # Neither u nor v can be ancestors of i
                    # But i can be descendant, splitting the path
                    count = 0
                else:
                    # One of u, v is less than i, other is greater
                    smaller = min(u, v)
                    larger = max(u, v)
                    if i > smaller and i < larger:
                        count = (total_trees * i * (larger - i)) % MOD
                        count = (count * modinv(smaller)) % MOD
                        count = (count * modinv(larger)) % MOD
                    else:
                        count = 0
            
            result = (result + A[i] * count) % MOD
        
        print(result)

solve()