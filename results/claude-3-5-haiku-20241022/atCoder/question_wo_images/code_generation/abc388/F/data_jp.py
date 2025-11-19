def solve():
    N, M, A, B = map(int, input().split())
    
    bad_ranges = []
    for _ in range(M):
        L, R = map(int, input().split())
        bad_ranges.append((L, R))
    
    # BFS with state compression
    # We need to track reachable positions
    # Since N can be very large but B is at most 20, we can use interval merging
    
    # Start from position 1
    reachable = {1}
    
    # Process in waves
    while reachable:
        new_reachable = set()
        
        for pos in reachable:
            # Try all jumps from A to B
            for jump in range(A, B + 1):
                next_pos = pos + jump
                
                if next_pos > N:
                    continue
                
                if next_pos == N:
                    print("Yes")
                    return
                
                # Check if next_pos is bad
                is_bad = False
                for L, R in bad_ranges:
                    if L <= next_pos <= R:
                        is_bad = True
                        break
                
                if not is_bad:
                    new_reachable.add(next_pos)
        
        # Check if we made progress
        if not new_reachable:
            print("No")
            return
        
        # Optimize: merge intervals to avoid explosion
        # Since we can only jump A to B steps, positions far apart don't interact much
        # We can use interval representation
        
        reachable = new_reachable
        
        # Optimization: if reachable set is too large, merge to intervals
        if len(reachable) > 10000:
            # Convert to sorted list and merge
            sorted_pos = sorted(reachable)
            intervals = []
            start = sorted_pos[0]
            end = sorted_pos[0]
            
            for pos in sorted_pos[1:]:
                if pos <= end + B:
                    end = pos
                else:
                    intervals.append((start, end))
                    start = pos
                    end = pos
            intervals.append((start, end))
            
            # Check if any interval can reach N
            for start, end in intervals:
                if end + A <= N <= end + B:
                    # Check if N is not bad
                    is_bad = False
                    for L, R in bad_ranges:
                        if L <= N <= R:
                            is_bad = True
                            break
                    if not is_bad:
                        print("Yes")
                        return
            
            # Generate new reachable from intervals
            reachable = set()
            for start, end in intervals:
                # Sample points from each interval
                for pos in range(start, min(end + 1, start + B + 1)):
                    reachable.add(pos)
                if end > start + B:
                    reachable.add(end)
    
    print("No")

solve()