def solve():
    N, M, Q = map(int, input().split())
    people = []
    for _ in range(M):
        S, T = map(int, input().split())
        people.append((S, T))
    
    queries = []
    for _ in range(Q):
        L, R = map(int, input().split())
        queries.append((L-1, R-1))  # 0-indexed
    
    def check_compatible(person_indices):
        # For each prefix position, track what constraints we have
        # We use prefix sums: prefix[i] = sum of w[1] to w[i]
        must_be_zero = set()
        must_be_positive = set()
        
        for idx in person_indices:
            S, T = people[idx]
            if S > T:
                S, T = T, S
            
            # Path goes from S to T
            # At position T, prefix sum must be 0
            must_be_zero.add(T-1)
            
            # At positions S+1 to T-1, cumulative sum must be positive
            for pos in range(S, T-1):
                must_be_positive.add(pos)
        
        # Check for direct conflicts
        if must_be_zero & must_be_positive:
            return False
        
        # Build a constraint graph to check feasibility
        # This is more complex - we need to check if the system is solvable
        # A simpler approach: check pairwise compatibility
        
        for i, idx1 in enumerate(person_indices):
            for idx2 in person_indices[i+1:]:
                S1, T1 = people[idx1]
                S2, T2 = people[idx2]
                
                if S1 > T1:
                    S1, T1 = T1, S1
                if S2 > T2:
                    S2, T2 = T2, S2
                
                # Check if paths overlap
                left = max(S1, S2)
                right = min(T1, T2)
                
                if left < right:
                    # Overlapping region
                    # Both must sum to 0 at their endpoints
                    # This creates constraints that might conflict
                    if T1 == T2 and S1 != S2:
                        # Different starts, same end - could be issue
                        pass
                    if S1 == S2 and T1 != T2:
                        # Same start, different ends
                        pass
                    
                    # More detailed check needed
                    if T1 < T2 and S1 < S2:
                        # Person 1 ends before person 2, but starts before
                        # At T1, prefix must be 0 (person 1)
                        # But person 2 needs positive at T1-1 if T1-1 >= S2
                        if S2 <= T1 - 1:
                            return False
                    if T2 < T1 and S2 < S1:
                        if S1 <= T2 - 1:
                            return False
        
        return True
    
    for L, R in queries:
        indices = list(range(L, R+1))
        if check_compatible(indices):
            print("Yes")
        else:
            print("No")

solve()