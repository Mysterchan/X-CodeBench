def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    
    # Convert to 0-indexed
    P = [p - 1 for p in P]
    
    # Find where each element should go
    target = list(range(N * K))
    
    # Build cycle decomposition
    visited = [False] * (N * K)
    cycles = []
    
    for start in range(N * K):
        if visited[start]:
            continue
        
        cycle = []
        curr = start
        while not visited[curr]:
            visited[curr] = True
            cycle.append(curr)
            curr = P[curr]
        
        if len(cycle) > 1:
            cycles.append(cycle)
    
    total_score = 0
    
    for cycle in cycles:
        n = len(cycle)
        
        # Count positions modulo N for each element in the cycle
        mod_counts = {}
        for pos in cycle:
            mod = pos % N
            mod_counts[mod] = mod_counts.get(mod, 0) + 1
        
        # For a cycle of length n, we need n-1 swaps
        # We want to maximize swaps where |i-j| is a multiple of N
        
        # Greedy approach: try to maximize swaps within same residue class mod N
        score = 0
        
        # For each residue class, if we have k elements, we can do k-1 swaps
        # within that class (all giving us points)
        for mod, count in mod_counts.items():
            if count > 1:
                score += count - 1
        
        # But we need exactly n-1 swaps total for the cycle
        # The maximum score is min(n-1, sum of (count-1) for each mod class)
        # which is min(n-1, n - number_of_distinct_mods)
        
        num_distinct_mods = len(mod_counts)
        max_score_for_cycle = n - num_distinct_mods
        
        total_score += max_score_for_cycle
    
    print(total_score)

solve()