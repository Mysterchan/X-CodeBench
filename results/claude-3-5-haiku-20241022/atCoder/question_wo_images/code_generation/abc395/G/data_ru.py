import sys
from itertools import combinations

def solve():
    input = sys.stdin.read().split()
    idx = 0
    
    N = int(input[idx])
    K = int(input[idx + 1])
    idx += 2
    
    C = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input[idx]))
            idx += 1
        C.append(row)
    
    Q = int(input[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        s = int(input[idx]) - 1
        t = int(input[idx + 1]) - 1
        idx += 2
        queries.append((s, t))
    
    # Precompute MST for each subset of first K vertices
    required = list(range(K))
    mst_cache = {}
    
    def compute_mst(vertices):
        vertices = tuple(sorted(vertices))
        if vertices in mst_cache:
            return mst_cache[vertices]
        
        n = len(vertices)
        if n == 1:
            mst_cache[vertices] = 0
            return 0
        
        # Prim's algorithm
        in_mst = [False] * n
        min_cost = [float('inf')] * n
        in_mst[0] = True
        
        for i in range(1, n):
            min_cost[i] = C[vertices[0]][vertices[i]]
        
        total = 0
        for _ in range(n - 1):
            min_val = float('inf')
            min_idx = -1
            for i in range(n):
                if not in_mst[i] and min_cost[i] < min_val:
                    min_val = min_cost[i]
                    min_idx = i
            
            in_mst[min_idx] = True
            total += min_val
            
            for i in range(n):
                if not in_mst[i]:
                    min_cost[i] = min(min_cost[i], C[vertices[min_idx]][vertices[i]])
        
        mst_cache[vertices] = total
        return total
    
    # For each query
    for s, t in queries:
        min_cost = float('inf')
        
        # Try all subsets of required vertices (1..K)
        for r in range(K + 1):
            for subset in combinations(range(K), r):
                subset = list(subset)
                
                # Compute MST on subset + s + t
                vertices = subset + [s, t]
                cost = compute_mst(vertices)
                
                # Add connection costs for vertices not in subset
                remaining = [i for i in range(K) if i not in subset]
                
                if remaining:
                    # Connect remaining to the tree
                    for v in remaining:
                        min_conn = float('inf')
                        for u in vertices:
                            min_conn = min(min_conn, C[v][u])
                        cost += min_conn
                
                min_cost = min(min_cost, cost)
        
        print(min_cost)

solve()