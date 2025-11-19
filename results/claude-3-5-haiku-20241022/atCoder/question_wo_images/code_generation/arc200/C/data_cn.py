def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        intervals = []
        for i in range(N):
            L, R = map(int, input().split())
            intervals.append((L, R, i + 1))
        
        # Try to find the lexicographically smallest permutation with minimum dissatisfaction
        # Strategy: Use greedy approach with backtracking consideration
        
        best_dissatisfaction = float('inf')
        best_perm = None
        
        # Generate permutations more intelligently
        # Key insight: people with overlapping intervals cause dissatisfaction
        # We want to minimize crossings
        
        def calculate_dissatisfaction(perm):
            # perm[i] is the seat position for person i+1
            total = 0
            for i in range(N):
                person = i + 1
                L_i, R_i = intervals[i][0], intervals[i][1]
                seat = perm[i]
                
                # Count how many times others cross seat position during (L_i, R_i)
                for j in range(N):
                    if i == j:
                        continue
                    other_person = j + 1
                    L_j, R_j = intervals[j][0], intervals[j][1]
                    other_seat = perm[j]
                    
                    # Other person crosses seat if their seat >= seat
                    if other_seat >= seat:
                        # Check arrival crossing
                        if L_i < L_j < R_i and L_j < R_j:
                            total += 1
                        # Check departure crossing
                        if L_i < R_j < R_i and L_j < R_j:
                            total += 1
            
            return total
        
        # Use a greedy approach with lexicographic ordering
        from itertools import permutations
        
        if N <= 8:
            # Small N: try all permutations
            for perm in permutations(range(1, N + 1)):
                diss = calculate_dissatisfaction(perm)
                if diss < best_dissatisfaction or (diss == best_dissatisfaction and (best_perm is None or perm < best_perm)):
                    best_dissatisfaction = diss
                    best_perm = perm
        else:
            # Larger N: use greedy heuristic
            # Sort by L_i (arrival time)
            sorted_indices = sorted(range(N), key=lambda i: intervals[i][0])
            perm = [0] * N
            used = [False] * (N + 1)
            
            for idx in sorted_indices:
                # Assign smallest available seat
                for seat in range(1, N + 1):
                    if not used[seat]:
                        perm[idx] = seat
                        used[seat] = True
                        break
            
            best_perm = tuple(perm)
            best_dissatisfaction = calculate_dissatisfaction(perm)
        
        print(' '.join(map(str, best_perm)))

solve()