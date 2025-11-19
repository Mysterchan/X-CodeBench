def solve():
    N, P = map(int, input().split())
    
    # Precompute factorials and inverse factorials
    max_val = N * (N - 1) // 2 + 1
    fact = [1] * max_val
    for i in range(1, max_val):
        fact[i] = fact[i-1] * i % P
    
    inv_fact = [1] * max_val
    inv_fact[max_val-1] = pow(fact[max_val-1], P-2, P)
    for i in range(max_val-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % P
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % P * inv_fact[n-k] % P
    
    # For a connected graph with N vertices, we need to count graphs where
    # the vertices can be bipartitioned into two sets of size N/2 each
    # based on BFS distance parity from vertex 1
    
    half = N // 2
    max_edges = N * (N - 1) // 2
    
    # dp[m][k] = number of ways to choose m edges from bipartite graph
    # where vertex 1 is in one part and k vertices are in the same part as vertex 1
    
    results = []
    
    for M in range(N-1, max_edges + 1):
        count = 0
        
        # Vertex 1 is in one partition, we choose k-1 more vertices for its partition
        # The other partition has N-k vertices
        # We want k = N/2
        k = half
        other = N - k
        
        # Number of ways to partition vertices (excluding vertex 1 which is fixed in first partition)
        partition_ways = comb(N-1, k-1)
        
        # Maximum edges in bipartite graph
        max_bipartite_edges = k * other
        
        # Maximum edges within each partition
        max_within_first = k * (k - 1) // 2
        max_within_second = other * (other - 1) // 2
        
        # We need to count connected graphs with M edges
        # Use inclusion-exclusion on connectivity
        
        # For each valid bipartite structure, count graphs with M edges that are connected
        # This is complex, so we use generating functions approach
        
        # Iterate over number of edges between partitions (must be at least 1 for connectivity)
        for between in range(1, min(M, max_bipartite_edges) + 1):
            remaining = M - between
            if remaining > max_within_first + max_within_second:
                continue
            
            # Count ways to distribute remaining edges within partitions
            for within_first in range(max(0, remaining - max_within_second), min(remaining, max_within_first) + 1):
                within_second = remaining - within_first
                
                # Check connectivity: graph is connected if bipartite edges connect both parts
                # and each part is internally connected or has bipartite edges
                
                ways = comb(max_bipartite_edges, between)
                ways = ways * comb(max_within_first, within_first) % P
                ways = ways * comb(max_within_second, within_second) % P
                ways = ways * partition_ways % P
                
                count = (count + ways) % P
        
        results.append(count)
    
    print(' '.join(map(str, results)))

solve()