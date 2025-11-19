import sys
from itertools import combinations

def read_input():
    N, K = map(int, input().split())
    C = []
    for _ in range(N):
        C.append(list(map(int, input().split())))
    Q = int(input())
    queries = []
    for _ in range(Q):
        s, t = map(int, input().split())
        queries.append((s-1, t-1))
    return N, K, C, queries

def prim_mst(vertices, C):
    if len(vertices) == 0:
        return 0
    vertices = list(vertices)
    n = len(vertices)
    if n == 1:
        return 0
    
    in_mst = [False] * n
    in_mst[0] = True
    total_cost = 0
    
    for _ in range(n - 1):
        min_cost = float('inf')
        min_u = -1
        min_v = -1
        
        for i in range(n):
            if in_mst[i]:
                for j in range(n):
                    if not in_mst[j]:
                        cost = C[vertices[i]][vertices[j]]
                        if cost < min_cost:
                            min_cost = cost
                            min_u = i
                            min_v = j
        
        in_mst[min_v] = True
        total_cost += min_cost
    
    return total_cost

def solve_query(K, s, t, N, C):
    required = set(range(K))
    required.add(s)
    required.add(t)
    
    optional = set(range(K, N)) - {s, t}
    
    min_cost = float('inf')
    
    for r in range(len(optional) + 1):
        for subset in combinations(optional, r):
            vertices = required | set(subset)
            cost = prim_mst(vertices, C)
            min_cost = min(min_cost, cost)
    
    return min_cost

def main():
    N, K, C, queries = read_input()
    
    for s, t in queries:
        result = solve_query(K, s, t, N, C)
        print(result)

if __name__ == "__main__":
    main()