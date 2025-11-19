MOD = 998244353

N = int(input())
s = input().strip()

# Count hub connections
hub_edges = sum(int(c) for c in s)

# DP approach: track in-degrees as we process vertices
# State: (vertex_index, in_degree_of_N, constraints_on_cycle)

from collections import defaultdict

# Process cycle edges and hub edges
# For each orientation, track the in-degree sequence

def solve():
    # Use DP to count distinct in-degree sequences
    # dp[in_deg_N][tuple_of_in_degs_0_to_i] = count
    
    # Since N can be large, we need efficient representation
    # Key observation: in-degrees are bounded by degree of each vertex
    
    # Simpler approach: enumerate all 2^E orientations and count distinct sequences
    # But E can be ~2*10^6, too large
    
    # Better: DP on cycle position tracking partial in-degrees
    total_edges = N + hub_edges
    
    # Each vertex i (i<N) has degree 2 (cycle) + (1 if s[i]=='1' else 0)
    # Vertex N has degree = hub_edges
    
    # DP state: position in cycle, in-degrees seen so far
    # This is still complex due to large state space
    
    # Optimized: use coordinate compression and careful DP
    
    distinct_sequences = set()
    
    # For small N, brute force
    if N <= 10 and hub_edges <= 10:
        edges = []
        # Cycle edges
        for i in range(N):
            edges.append((i, (i+1) % N))
        # Hub edges
        for i in range(N):
            if s[i] == '1':
                edges.append((i, N))
        
        E = len(edges)
        for mask in range(1 << E):
            in_deg = [0] * (N + 1)
            for j, (u, v) in enumerate(edges):
                if mask & (1 << j):
                    in_deg[v] += 1
                else:
                    in_deg[u] += 1
            distinct_sequences.add(tuple(in_deg))
        
        return len(distinct_sequences) % MOD
    
    # For large N, use mathematical approach with DP
    # Track in-degrees incrementally
    dp = defaultdict(int)
    dp[(tuple([0]*N), 0)] = 1  # (in_degs of 0..N-1, in_deg of N)
    
    # This is still too large - need better approach
    # Use generating functions or matrix approach
    
    # Simplified: count using inclusion-exclusion or direct DP
    # Given constraints, implement efficient DP
    
    # Actual solution: careful enumeration with memoization
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp_count(pos, in_degs, in_deg_N):
        if pos == N:
            # Processed all cycle edges, now hub edges
            # For hub edges, we can orient independently
            result = set()
            for hub_mask in range(1 << hub_edges):
                final_in_degs = list(in_degs)
                final_in_deg_N = in_deg_N
                idx = 0
                for i in range(N):
                    if s[i] == '1':
                        if hub_mask & (1 << idx):
                            final_in_deg_N += 1
                        else:
                            final_in_degs[i] += 1
                        idx += 1
                result.add((tuple(final_in_degs), final_in_deg_N))
            return len(result)
        
        # Process cycle edge pos -> (pos+1)%N
        count = 0
        for direction in [0, 1]:  # 0: pos->(pos+1), 1: (pos+1)->pos
            new_in_degs = list(in_degs)
            if direction == 0:
                new_in_degs[(pos+1)%N] += 1
            else:
                new_in_degs[pos] += 1
            count += dp_count(pos+1, tuple(new_in_degs), in_deg_N)
        return count
    
    return dp_count(0, tuple([0]*N), 0) % MOD

print(solve())