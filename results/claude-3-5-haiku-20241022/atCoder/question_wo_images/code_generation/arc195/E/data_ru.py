MOD = 998244353

def solve():
    N, Q = map(int, input().split())
    A = [0, 0] + list(map(int, input().split()))
    
    # Precompute factorials
    fact = [1] * N
    for i in range(1, N):
        fact[i] = fact[i-1] * i % MOD
    
    for _ in range(Q):
        u, v = map(int, input().split())
        
        if u > v:
            u, v = v, u
        
        # Calculate the answer
        # For each possible tree, we need to find the distance between u and v
        # The distance depends on the path from u to v
        
        # Key insight: 
        # For vertices u and v, the distance in a tree T(P) is the sum of A_i
        # for all i on the path from u to v.
        
        # We need to count how many times each edge (with weight A_i) appears
        # in paths from u to v across all possible trees.
        
        # An edge with weight A_i (connecting i to its parent) is on the path
        # from u to v if and only if i is on the path from u to v in the tree.
        
        # For a rooted tree with root 1:
        # - The path from u to v goes through their LCA (lowest common ancestor)
        # - A vertex i is on the path if it's an ancestor of u or v (or both)
        #   and a descendant of their LCA
        
        total = 0
        
        # For each vertex i from 2 to N, calculate how many trees have i on the path from u to v
        for i in range(2, N + 1):
            # Count the number of trees where i is on the path from u to v
            
            # Case analysis based on u, v, i positions
            if i == u or i == v:
                # i is one of the endpoints
                # The edge A_i is always on the path
                count = fact[N - 1]
            elif u == 1 or v == 1:
                # One endpoint is the root
                other = v if u == 1 else u
                if i == other:
                    count = fact[N - 1]
                else:
                    # i must be an ancestor of other (i.e., other is a descendant of i)
                    # This happens when i is on the path from 1 to other
                    # P_other can be any ancestor up to i, and i can be any ancestor up to 1
                    # Number of ways: (i-1) * fact[N-2]
                    count = (i - 1) * fact[N - 2] % MOD
            else:
                # Neither u nor v is the root
                # i is on path from u to v if:
                # 1. i is ancestor of both u and v, or
                # 2. i is ancestor of exactly one of u, v and the other is ancestor of i
                
                # This is complex, so let's think differently:
                # i is on the path iff in the sequence of ancestors from u to root and v to root,
                # i appears in at least one of them and is between u/v and their LCA
                
                # Simplified: count = 2 * (i-1) * fact[N-2]
                count = 2 * (i - 1) % MOD * fact[N - 2] % MOD
            
            total = (total + A[i] * count) % MOD
        
        print(total)

solve()