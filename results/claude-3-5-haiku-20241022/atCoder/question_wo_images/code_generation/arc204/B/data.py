def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    
    # Convert to 0-indexed
    P = [p - 1 for p in P]
    size = N * K
    
    # Find cycles
    visited = [False] * size
    cycles = []
    
    for i in range(size):
        if not visited[i]:
            cycle = []
            curr = i
            while not visited[curr]:
                visited[curr] = True
                cycle.append(curr)
                curr = P[curr]
            if len(cycle) > 1:
                cycles.append(cycle)
    
    total_points = 0
    
    # For each cycle, find optimal way to break it
    for cycle in cycles:
        cycle_len = len(cycle)
        max_points = 0
        
        # Try each position as the "anchor" (the one that stays)
        for anchor_idx in range(cycle_len):
            points = 0
            # We swap other elements to their target positions
            # The anchor stays at cycle[anchor_idx]
            anchor_pos = cycle[anchor_idx]
            
            # For each other element in the cycle, we need to swap it
            for i in range(cycle_len):
                if i != anchor_idx:
                    curr_pos = cycle[i]
                    # Check if distance from anchor is multiple of N
                    if abs(anchor_pos - curr_pos) % N == 0:
                        points += 1
            
            max_points = max(max_points, points)
        
        total_points += max_points
    
    print(total_points)

solve()