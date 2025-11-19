def solve():
    N, M, Q = map(int, input().split())
    
    people = []
    for _ in range(M):
        s, t = map(int, input().split())
        people.append((s, t))
    
    def can_satisfy(person_indices):
        # Build constraints for the selected people
        constraints = []
        
        for idx in person_indices:
            s, t = people[idx]
            if s > t:
                s, t = t, s
            
            # For person going from s to t
            # Path: s -> s+1 -> ... -> t
            # Edges used: s to s+1 (edge s), s+1 to s+2 (edge s+1), ..., t-1 to t (edge t-1)
            
            # Let w[i] be the strength of edge i (connecting town i to town i+1)
            # At town s: stamina = 0
            # At town s+1: stamina = w[s] (must be > 0)
            # At town s+2: stamina = w[s] + w[s+1] (must be > 0)
            # ...
            # At town t: stamina = w[s] + w[s+1] + ... + w[t-1] = 0
            
            # Constraints:
            # 1. Sum of all edges from s to t-1 = 0
            # 2. All prefix sums must be > 0
            
            path_edges = list(range(s, t))
            constraints.append((path_edges, people[idx][0] < people[idx][1]))
        
        # Check if there's a valid assignment
        # We need to check if the system of constraints is satisfiable
        
        # For each person, we have:
        # - Sum of edges = 0
        # - All prefix sums > 0 (or all suffix sums > 0 if going backwards)
        
        # Key insight: For a person going from s to t (s < t):
        # w[s] > 0, w[s] + w[s+1] > 0, ..., w[s] + ... + w[t-1] = 0
        # This means the last edge w[t-1] must be negative and cancel out all previous positive sums
        
        # Check for conflicts
        edge_must_positive = set()
        edge_must_negative = set()
        
        for idx in person_indices:
            s, t = people[idx]
            forward = (s < t)
            
            if not forward:
                s, t = t, s
            
            # Edges from s to t-1
            # First edge must be positive, last edge must be negative
            if forward == (people[idx][0] < people[idx][1]):
                edge_must_positive.add(s)
                edge_must_negative.add(t - 1)
            else:
                edge_must_positive.add(t - 1)
                edge_must_negative.add(s)
        
        # Check for direct conflicts
        if edge_must_positive & edge_must_negative:
            return False
        
        # More sophisticated check: build a graph of constraints
        # and check for consistency
        
        # Actually, we need to check if paths overlap in incompatible ways
        for i, idx1 in enumerate(person_indices):
            s1, t1 = people[idx1]
            if s1 > t1:
                s1, t1 = t1, s1
                dir1 = -1
            else:
                dir1 = 1
            
            for idx2 in person_indices[i+1:]:
                s2, t2 = people[idx2]
                if s2 > t2:
                    s2, t2 = t2, s2
                    dir2 = -1
                else:
                    dir2 = 1
                
                # Check if paths overlap
                overlap_start = max(s1, s2)
                overlap_end = min(t1, t2)
                
                if overlap_start < overlap_end:
                    # Paths overlap
                    # Check if they are compatible
                    if dir1 != dir2:
                        return False
        
        return True
    
    for _ in range(Q):
        l, r = map(int, input().split())
        person_indices = list(range(l - 1, r))
        
        if can_satisfy(person_indices):
            print("Yes")
        else:
            print("No")

solve()