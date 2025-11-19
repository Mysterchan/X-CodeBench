def solve():
    N = int(input())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]  # 0-indexed
    
    Q = int(input())
    
    # Precompute MEX table
    mex = [[0] * 3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            for m in range(3):
                if m != x and m != y:
                    mex[x][y] = m
                    break
    
    for _ in range(Q):
        A0, A1, A2 = map(int, input().split())
        counts = [A0, A1, A2]
        
        # Find cycles in permutation
        visited = [False] * N
        cycles = []
        
        for i in range(N):
            if not visited[i]:
                cycle = []
                j = i
                while not visited[j]:
                    visited[j] = True
                    cycle.append(j)
                    j = P[j]
                cycles.append(cycle)
        
        # DP for each cycle
        max_score = 0
        
        def dp_cycle(cycle, counts):
            n = len(cycle)
            # state: (pos, c0, c1, c2, first_value)
            # We need to track what value we assigned to the first position
            memo = {}
            
            def rec(pos, c0, c1, c2, first_val):
                if pos == n:
                    return 0
                
                state = (pos, c0, c1, c2, first_val)
                if state in memo:
                    return memo[state]
                
                result = -float('inf')
                curr_idx = cycle[pos]
                next_idx = cycle[(pos + 1) % n]
                
                for val in range(3):
                    new_c = [c0, c1, c2]
                    if new_c[val] == 0:
                        continue
                    new_c[val] -= 1
                    
                    if pos == n - 1:
                        # Last position, need to check with first
                        score = mex[val][first_val]
                        result = max(result, score)
                    else:
                        next_val = -1
                        for nv in range(3):
                            nc = new_c[:]
                            if nc[nv] == 0:
                                continue
                            
                            if pos == 0:
                                score = rec(pos + 1, new_c[0], new_c[1], new_c[2], val)
                            else:
                                score = rec(pos + 1, new_c[0], new_c[1], new_c[2], first_val)
                            
                            if pos < n - 1:
                                # Add contribution from current edge
                                pass
                            
                            result = max(result, score)
                
                memo[state] = result
                return result
            
            # Try different strategies - assign greedily
            best = -float('inf')
            
            # Try all possible assignments using backtracking
            assignment = [-1] * n
            
            def backtrack(pos, c):
                nonlocal best
                if pos == n:
                    score = 0
                    for i in range(n):
                        j = (i + 1) % n
                        score += mex[assignment[i]][assignment[j]]
                    best = max(best, score)
                    return
                
                for val in range(3):
                    if c[val] > 0:
                        assignment[pos] = val
                        c[val] -= 1
                        backtrack(pos + 1, c)
                        c[val] += 1
                        assignment[pos] = -1
            
            backtrack(0, counts[:])
            return best
        
        for cycle in cycles:
            max_score += dp_cycle(cycle, counts)
            # Update counts
            pass
        
        # Simpler approach: greedy assignment
        total_score = 0
        remaining = counts[:]
        
        for cycle in cycles:
            cycle_len = len(cycle)
            assignment = [-1] * cycle_len
            
            # Try to maximize MEX sum for this cycle
            best_cycle_score = -float('inf')
            
            def try_assign(pos, rem, assign, score):
                nonlocal best_cycle_score
                if pos == cycle_len:
                    best_cycle_score = max(best_cycle_score, score)
                    return
                
                for val in range(3):
                    if rem[val] > 0:
                        new_rem = rem[:]
                        new_rem[val] -= 1
                        new_score = score
                        if pos > 0:
                            new_score += mex[assign[pos-1]][val]
                        if pos == cycle_len - 1:
                            new_score += mex[val][assign[0]]
                        new_assign = assign[:]
                        new_assign[pos] = val
                        try_assign(pos + 1, new_rem, new_assign, new_score)
            
            try_assign(0, remaining, assignment, 0)
            total_score += best_cycle_score
            
            # Update remaining counts
            for i in range(cycle_len):
                # assignment was local, need to recompute
                pass
        
        print(total_score)

solve()