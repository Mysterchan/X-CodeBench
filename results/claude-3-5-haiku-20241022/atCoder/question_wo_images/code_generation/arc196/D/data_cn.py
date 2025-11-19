def solve():
    N, M, Q = map(int, input().split())
    people = []
    for _ in range(M):
        S, T = map(int, input().split())
        people.append((S, T))
    
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1  # 0-indexed
        
        # Check if the subset of people [L, R) can be satisfied
        active = people[L:R]
        
        # Check for conflicts
        can_satisfy = True
        
        # For each pair of people, check if their requirements conflict
        for i in range(len(active)):
            S1, T1 = active[i]
            min1, max1 = min(S1, T1), max(S1, T1)
            dir1 = 1 if T1 > S1 else -1
            
            for j in range(i + 1, len(active)):
                S2, T2 = active[j]
                min2, max2 = min(S2, T2), max(S2, T2)
                dir2 = 1 if T2 > S2 else -1
                
                # Check if intervals overlap
                if max1 <= min2 or max2 <= min1:
                    continue
                
                # If moving in opposite directions and overlapping, check conflicts
                if dir1 != dir2:
                    # Opposite directions with overlap can cause conflicts
                    overlap_start = max(min1, min2)
                    overlap_end = min(max1, max2)
                    
                    if overlap_end > overlap_start:
                        can_satisfy = False
                        break
            
            if not can_satisfy:
                break
        
        print("Yes" if can_satisfy else "No")

solve()