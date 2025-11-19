def solve():
    N, M, Q = map(int, input().split())
    
    people = []
    for _ in range(M):
        s, t = map(int, input().split())
        people.append((s, t))
    
    def can_satisfy(L, R):
        # Check if people L to R (0-indexed: L-1 to R-1) can be satisfied
        active_people = []
        for i in range(L-1, R):
            s, t = people[i]
            if s > t:
                s, t = t, s
            active_people.append((s, t))
        
        if not active_people:
            return True
        
        # Build constraints
        # For each person going from s to t, we need:
        # - sum of w[s..t-1] = 0
        # - All prefix sums > 0 (except at s where it's 0 and at t where it's 0)
        
        # We need to check if there's a conflict
        # Key insight: if two people's paths overlap, they must agree on the sum
        # Also, the alternating pattern constraint
        
        # For each road, track what constraints are placed on it
        # Let's use a different approach: check if the system is consistent
        
        # We'll check using the alternating pattern requirement
        # For a person from s to t, the partial sums must alternate or stay positive
        
        # Check for conflicts using events
        events = []
        for s, t in active_people:
            events.append((s, 1, s, t))  # start
            events.append((t, -1, s, t))  # end
        
        events.sort()
        
        # Check if paths are compatible
        # Two paths conflict if they overlap and have different parity requirements
        
        # Simpler approach: check if there are overlapping paths with incompatible constraints
        # For paths [s1, t1] and [s2, t2], if they overlap significantly, check compatibility
        
        for i in range(len(active_people)):
            for j in range(i+1, len(active_people)):
                s1, t1 = active_people[i]
                s2, t2 = active_people[j]
                
                # Check if paths overlap
                overlap_start = max(s1, s2)
                overlap_end = min(t1, t2)
                
                if overlap_start < overlap_end:
                    # They overlap
                    # Check if they have the same direction in overlap
                    # Both go left-to-right in our representation
                    
                    # If one path contains the start/end of another, there's a conflict
                    if s1 < s2 < t1 < t2 or s2 < s1 < t2 < t1:
                        return False
                    
                    # If one completely contains another
                    if s1 <= s2 and t2 <= t1:
                        return False
                    if s2 <= s1 and t1 <= t2:
                        return False
        
        return True
    
    for _ in range(Q):
        L, R = map(int, input().split())
        if can_satisfy(L, R):
            print("Yes")
        else:
            print("No")

solve()