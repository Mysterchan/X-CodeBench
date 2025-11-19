def solve(N, P):
    from math import comb
    
    # Precompute factorials and inverses for modular arithmetic
    def modinv(a, p):
        return pow(a, p - 2, p)
    
    def mod_comb(n, k, p):
        if k < 0 or k > n:
            return 0
        return comb(n, k) % p
    
    max_edges = N * (N - 1) // 2
    min_edges = N - 1
    
    results = []
    
    # Size of each partition
    half = N // 2
    
    # Maximum edges in bipartite graph with partitions of size half each
    max_bip_edges = half * half
    
    for M in range(min_edges, max_edges + 1):
        if M > max_bip_edges:
            results.append(0)
            continue
        
        # Count connected bipartite graphs with vertex 1 in partition A of size half
        # Total bipartite graphs: choose (N-1) choose (half-1) vertices for partition A (excluding vertex 1)
        # Then choose M edges from possible half*half edges
        
        # Ways to partition: vertex 1 in A, choose half-1 from remaining N-1 vertices
        partitions = mod_comb(N - 1, half - 1, P)
        
        # Ways to choose M edges from half*half possible edges
        edge_choices = mod_comb(max_bip_edges, M, P)
        
        # Total bipartite graphs
        total_bip = (partitions * edge_choices) % P
        
        # Use inclusion-exclusion to count connected graphs
        # Subtract disconnected ones
        
        # For simplicity with small N, enumerate all possible subsets containing vertex 1
        # and subtract graphs where vertex 1's component is smaller
        
        connected = total_bip
        
        # Subtract cases where vertex 1 is in a component of size k < N
        for k in range(1, N):
            if k > half:  # Component too large for partition A
                continue
            if M < k - 1:  # Not enough edges
                continue
            
            # Vertices in component with vertex 1 (including vertex 1)
            # Must respect bipartition: some in A, some in B
            for a in range(1, min(k, half) + 1):  # vertices from A in component (including vertex 1)
                b = k - a  # vertices from B in component
                if b < 0 or b > half:
                    continue
                if a < 1:  # vertex 1 must be in A
                    continue
                
                # Choose a-1 more vertices from A (half-1 available)
                ways_a = mod_comb(half - 1, a - 1, P)
                # Choose b vertices from B (half available)
                ways_b = mod_comb(half, b, P)
                
                # Edges within this component (at most a*b)
                max_comp_edges = a * b
                
                for m in range(k - 1, min(M, max_comp_edges) + 1):
                    comp_edges = mod_comb(max_comp_edges, m, P)
                    
                    # Remaining graph
                    remaining_n = N - k
                    remaining_a = half - a
                    remaining_b = half - b
                    remaining_max_edges = remaining_a * remaining_b
                    remaining_m = M - m
                    
                    if remaining_m < 0 or remaining_m > remaining_max_edges:
                        continue
                    
                    remaining_graphs = mod_comb(remaining_max_edges, remaining_m, P)
                    
                    contribution = (ways_a * ways_b % P * comp_edges % P * remaining_graphs) % P
                    connected = (connected - contribution) % P
        
        results.append(connected)
    
    return results

N, P = map(int, input().split())
ans = solve(N, P)
print(' '.join(map(str, ans)))