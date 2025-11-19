def solve():
    MOD = 998244353
    N = int(input())
    S = input().strip()
    
    whites = [i+1 for i in range(2*N) if S[i] == 'W']
    blacks = [i+1 for i in range(2*N) if S[i] == 'B']
    
    from itertools import permutations
    
    def is_strongly_connected(edges_list):
        # Build adjacency list
        adj = [[] for _ in range(2*N + 1)]
        for u, v in edges_list:
            adj[u].append(v)
        
        # Check if all vertices reachable from vertex 1
        visited = [False] * (2*N + 1)
        
        def dfs(v):
            visited[v] = True
            for u in adj[v]:
                if not visited[u]:
                    dfs(u)
        
        dfs(1)
        if not all(visited[1:2*N+1]):
            return False
        
        # Build reverse graph
        rev_adj = [[] for _ in range(2*N + 1)]
        for u, v in edges_list:
            rev_adj[v].append(u)
        
        # Check if all vertices can reach vertex 1
        visited = [False] * (2*N + 1)
        
        def dfs_rev(v):
            visited[v] = True
            for u in rev_adj[v]:
                if not visited[u]:
                    dfs_rev(u)
        
        dfs_rev(1)
        return all(visited[1:2*N+1])
    
    count = 0
    
    # Generate all permutations of blacks (pairings with whites)
    for perm in permutations(blacks):
        # Create edge list
        edges = []
        # Original path edges
        for i in range(1, 2*N):
            edges.append((i, i+1))
        # Pairing edges
        for i in range(N):
            edges.append((whites[i], perm[i]))
        
        if is_strongly_connected(edges):
            count += 1
    
    print(count % MOD)

solve()