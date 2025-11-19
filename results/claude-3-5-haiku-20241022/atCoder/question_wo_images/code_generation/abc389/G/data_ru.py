def solve():
    N, P = map(int, input().split())
    
    # Precompute factorials and inverse factorials modulo P
    max_edges = N * (N - 1) // 2
    fact = [1] * (max_edges + 1)
    for i in range(1, max_edges + 1):
        fact[i] = fact[i - 1] * i % P
    
    inv_fact = [1] * (max_edges + 1)
    inv_fact[max_edges] = pow(fact[max_edges], P - 2, P)
    for i in range(max_edges - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % P
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % P * inv_fact[n - k] % P
    
    # Generate all possible graphs with N vertices
    # We need to count connected graphs where half vertices are at even distance from vertex 1
    
    # For each number of edges M from N-1 to N*(N-1)/2
    results = []
    
    # Use BFS to check bipartiteness condition
    def is_valid_graph(edges):
        # Build adjacency list
        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS from vertex 0 (representing vertex 1)
        dist = [-1] * N
        dist[0] = 0
        queue = [0]
        head = 0
        
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        
        # Check if connected
        if any(d == -1 for d in dist):
            return False
        
        # Count even and odd distances
        even_count = sum(1 for d in dist if d % 2 == 0)
        odd_count = sum(1 for d in dist if d % 2 == 1)
        
        return even_count == odd_count
    
    # For small N, enumerate all graphs
    from itertools import combinations
    
    all_possible_edges = []
    for i in range(N):
        for j in range(i + 1, N):
            all_possible_edges.append((i, j))
    
    for M in range(N - 1, max_edges + 1):
        count = 0
        for edge_subset in combinations(all_possible_edges, M):
            if is_valid_graph(list(edge_subset)):
                count += 1
        results.append(count % P)
    
    print(' '.join(map(str, results)))

solve()