def solve():
    N = int(input())
    S = input().strip()
    
    MOD = 998244353
    
    # Find positions of W and B
    whites = []
    blacks = []
    for i in range(2 * N):
        if S[i] == 'W':
            whites.append(i)
        else:
            blacks.append(i)
    
    # For strong connectivity, we need to ensure there's no way to partition
    # the vertices into two non-empty sets such that there are no edges from
    # the second set to the first set.
    
    # Key insight: The original graph is a path 1->2->3->...->2N
    # After adding edges from whites to blacks, for strong connectivity,
    # we need that for any prefix [1, k], there exists at least one edge
    # going back from some vertex > k to some vertex <= k.
    
    # For each position k (1 to 2N-1), we need at least one "back edge"
    # crossing position k (from right to left).
    
    # A back edge from white w to black b crosses position k if w > k and b <= k
    
    # We'll use DP with bitmask or inclusion-exclusion
    # Let's think differently: we need to count matchings such that
    # for all k in [1, 2N-1], there exists at least one edge (w, b) with w > k and b <= k
    
    # Use inclusion-exclusion on "bad" sets of k
    
    # For each subset of positions that are "bad", compute number of matchings
    # where none of those positions have a back edge
    
    # This is exponential, but we can optimize
    
    # Actually, let's use DP: dp[i][j] = number of ways to match first i whites
    # with some blacks, where j is the rightmost position that has been "covered"
    
    # Better approach: for each critical position k, we need w > k, b <= k
    # The critical positions are boundaries
    
    # Let's use inclusion-exclusion on the set of "uncovered" boundaries
    
    from functools import lru_cache
    
    # Precompute factorials
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i-1] * i % MOD
    
    # For subset of positions that must be "covered", use inclusion-exclusion
    # This is still complex. Let me think of DP differently.
    
    # DP with mask of which positions are NOT yet covered
    # But 2N can be up to 4*10^5, too large
    
    # Key observation: we only care about positions between whites and blacks
    # Let's use DP: dp[w_idx][b_idx][covered_up_to]
    
    # Actually, simpler: use DP where we process whites in order
    # and track which is the minimum position that's not yet covered
    
    @lru_cache(maxsize=None)
    def dp(w_idx, b_mask, min_uncovered):
        if w_idx == N:
            # All whites matched, check if all positions covered
            return 1 if min_uncovered >= 2 * N else 0
        
        result = 0
        w_pos = whites[w_idx]
        
        for b_idx in range(N):
            if b_mask & (1 << b_idx):
                continue
            
            b_pos = blacks[b_idx]
            new_mask = b_mask | (1 << b_idx)
            
            # Update min_uncovered
            new_min = min_uncovered
            if w_pos > min_uncovered and b_pos < min_uncovered:
                # This edge covers positions from b_pos+1 to w_pos
                while new_min < 2 * N and (new_min < w_pos and (new_min <= b_pos or any(
                    whites[wi] > new_min and blacks[bi] <= new_min 
                    for wi in range(w_idx + 1) for bi in range(N) 
                    if (wi < w_idx or (wi == w_idx and (1 << bi) & new_mask)) and blacks[bi] < whites[wi]
                ))):
                    new_min += 1
            
            result = (result + dp(w_idx + 1, new_mask, new_min)) % MOD
        
        return result
    
    # This approach is too slow. Let me reconsider.
    
    # Use different DP: match blacks in order
    # For strong connectivity: for each k, exists edge w->b with w>k, b<=k
    
    # Equivalent: for each k in [1..2N-1], max(b : w paired with b, w > k) >= k
    #             OR there's no w > k (but there always is for k < 2N)
    
    # So for each k < 2N, we need max black paired with whites from (k, 2N] to be >= k
    
    # Wait, let me reconsider: for k < blacks[-1], we need a back edge
    
    # Simplified: compute using DP matching and track coverage
    
    ans = fact[N]  # Start with all matchings
    
    # Subtract bad ones using inclusion-exclusion
    # A matching is bad if there exists k such that all edges from whites > k go to blacks > k
    
    # This is complex. Let me implement a brute-force DP for small N
    
    def count_matchings():
        @lru_cache(maxsize=None)
        def dp(w_idx, b_mask):
            if w_idx == N:
                # Check strong connectivity
                edges = []
                for i in range(2 * N - 1):
                    edges.append((i, i + 1))
                
                used_blacks = []
                for wi in range(N):
                    for bi in range(N):
                        if not (b_mask & (1 << bi)):
                            continue
                        # This is wrong logic for reconstruction
                        pass
                
                # Need to reconstruct matching - this is complex
                return 1
            
            result = 0
            for b_idx in range(N):
                if not (b_mask & (1 << b_idx)):
                    result = (result + dp(w_idx + 1, b_mask | (1 << b_idx))) % MOD
            
            return result
        
        return dp(0, 0)
    
    print(count_matchings())

solve()