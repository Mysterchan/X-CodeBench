import sys
from itertools import combinations

def prim_mst(vertices, C):
    if len(vertices) <= 1:
        return 0
    
    vertices = list(vertices)
    n = len(vertices)
    visited = [False] * n
    visited[0] = True
    total_cost = 0
    edges = []
    
    for _ in range(n - 1):
        min_cost = float('inf')
        min_edge = None
        
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j]:
                        u, v = vertices[i], vertices[j]
                        cost = C[u][v]
                        if cost < min_cost:
                            min_cost = cost
                            min_edge = j
        
        if min_edge is not None:
            visited[min_edge] = True
            total_cost += min_cost
    
    return total_cost

def solve():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    
    N, K = map(int, input_lines[idx].split())
    idx += 1
    
    C = []
    for i in range(N):
        C.append(list(map(int, input_lines[idx].split())))
        idx += 1
    
    Q = int(input_lines[idx])
    idx += 1
    
    # Precompute MST for all subsets that include vertices 1..K
    required = set(range(K))
    optional = list(range(K, N))
    
    mst_cache = {}
    
    for r in range(len(optional) + 1):
        for subset in combinations(optional, r):
            vertices = required | set(subset)
            cost = prim_mst(vertices, C)
            mst_cache[frozenset(subset)] = cost
    
    for _ in range(Q):
        s, t = map(int, input_lines[idx].split())
        idx += 1
        s -= 1
        t -= 1
        
        min_cost = float('inf')
        
        for r in range(len(optional) + 1):
            for subset in combinations(optional, r):
                subset_set = set(subset)
                if s in subset_set and t in subset_set:
                    key = frozenset(subset)
                    if key in mst_cache:
                        min_cost = min(min_cost, mst_cache[key])
        
        print(min_cost)

solve()