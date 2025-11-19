def solve():
    N = int(input())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]  # Convert to 0-indexed
    
    Q = int(input())
    
    # Precompute MEX table
    mex_table = [
        [0, 2, 1],
        [2, 0, 0],
        [1, 0, 0]
    ]
    
    # For each query, we need to find the maximum score
    for _ in range(Q):
        A = list(map(int, input().split()))
        
        # Build a graph representation
        # For each position i, we have edge i -> P[i]
        visited = [False] * N
        cycles = []
        
        for start in range(N):
            if not visited[start]:
                cycle = []
                curr = start
                while not visited[curr]:
                    visited[curr] = True
                    cycle.append(curr)
                    curr = P[curr]
                cycles.append(cycle)
        
        # For each cycle, we need to assign values 0, 1, 2
        # to maximize the total MEX score
        
        # Dynamic programming approach
        # dp[cycle_idx][a0][a1][a2] = max score using first cycle_idx cycles
        # with a0, a1, a2 remaining counts
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(cycle_idx, a0, a1, a2):
            if cycle_idx == len(cycles):
                if a0 == 0 and a1 == 0 and a2 == 0:
                    return 0
                else:
                    return float('-inf')
            
            cycle = cycles[cycle_idx]
            cycle_len = len(cycle)
            
            max_score = float('-inf')
            
            # Try all possible assignments for this cycle
            # We need to assign values 0, 1, 2 to positions in the cycle
            for c0 in range(min(a0, cycle_len) + 1):
                for c1 in range(min(a1, cycle_len - c0) + 1):
                    c2 = cycle_len - c0 - c1
                    if c2 < 0 or c2 > a2:
                        continue
                    
                    # Try all rotations/assignments
                    best_cycle_score = try_all_assignments(cycle, c0, c1, c2)
                    
                    future_score = dp(cycle_idx + 1, a0 - c0, a1 - c1, a2 - c2)
                    if future_score != float('-inf'):
                        max_score = max(max_score, best_cycle_score + future_score)
            
            return max_score
        
        def try_all_assignments(cycle, c0, c1, c2):
            cycle_len = len(cycle)
            best = 0
            
            # Generate all possible assignments
            from itertools import permutations
            values = [0] * c0 + [1] * c1 + [2] * c2
            
            seen = set()
            for perm in permutations(values):
                if perm in seen:
                    continue
                seen.add(perm)
                
                # Calculate score for this assignment
                score = 0
                for idx, pos in enumerate(cycle):
                    val_i = perm[idx]
                    next_pos = P[pos]
                    next_idx = cycle.index(next_pos)
                    val_pi = perm[next_idx]
                    score += mex_table[val_i][val_pi]
                
                best = max(best, score)
            
            return best
        
        result = dp(0, A[0], A[1], A[2])
        print(result)

solve()