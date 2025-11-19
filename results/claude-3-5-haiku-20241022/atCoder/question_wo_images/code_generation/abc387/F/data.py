def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Convert to 0-indexed
    A = [a - 1 for a in A]
    
    # Build adjacency list
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i].append(A[i])
    
    # Find SCCs using Tarjan's algorithm
    index_