def solve():
    MOD = 998244353
    N = int(input())
    s = input().strip()
    
    k = s.count('1')
    
    # Use a set to store unique in-degree tuples
    sequences = set()
    
    # Try all 2^(N+k) orientations
    total_edges = N + k
    
    # For small N, we can enumerate
    if total_edges <= 20:
        for mask in range(1 << total_edges):
            in_deg = [0] * (N + 1)
            
            bit = 0
            # Cycle edges
            for i in range(N):
                if mask & (1 << bit):
                    in_deg[(i + 1) % N] += 1
                else:
                    in_deg[i] += 1
                bit += 1
            
            # Edges to N
            for i in range(N):
                if s[i] == '1':
                    if mask & (1 << bit):
                        in_deg[N] += 1
                    else:
                        in_deg[i] += 1
                    bit += 1
            
            sequences.add(tuple(in_deg))
        
        print(len(sequences) % MOD)
    else:
        # For larger N, use DP
        # dp[d_N][state] where state encodes partial in-degrees
        # This is complex, let me use a different approach
        
        # Generate using recursion with memoization
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def count_sequences(edge_idx, in_degs):
            if edge_idx == total_edges:
                return {in_degs}
            
            in_degs_list = list(in_degs)
            result = set()
            
            if edge_idx < N:
                # Cycle edge from edge_idx to (edge_idx+1)%N
                u, v = edge_idx, (edge_idx + 1) % N
                
                # Orient u->v
                in_degs_list[v] += 1
                result.update(count_sequences(edge_idx + 1, tuple(in_degs_list)))
                in_degs_list[v] -= 1
                
                # Orient v->u
                in_degs_list[u] += 1
                result.update(count_sequences(edge_idx + 1, tuple(in_degs_list)))
                in_degs_list[u] -= 1
            else:
                # Edge to N
                vertex_idx = edge_idx - N
                while vertex_idx < N and s[vertex_idx] == '0':
                    vertex_idx += 1
                
                # Orient vertex_idx->N
                in_degs_list[N] += 1
                result.update(count_sequences(edge_idx + 1, tuple(in_degs_list)))
                in_degs_list[N] -= 1
                
                # Orient N->vertex_idx
                in_degs_list[vertex_idx] += 1
                result.update(count_sequences(edge_idx + 1, tuple(in_degs_list)))
                in_degs_list[vertex_idx] -= 1
            
            return result
        
        sequences = count_sequences(0, tuple([0] * (N + 1)))
        print(len(sequences) % MOD)

solve()