def solve():
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    # Create position mapping: pos[i] = position of slime with size i
    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i
    
    # To sort by size, we need to move slime with size i to position i-1
    # We can only swap adjacent slimes with different colors
    
    # Check if a sequence can be sorted by counting inversions
    # For each pair (i, j) where i < j but p[i] > p[j], we need to swap them
    # This is possible if all inversions involve slimes with different colors
    
    # Use DP approach: for each slime, decide whether to change its color
    # A good sequence means we can sort it using only swaps of different-colored adjacent slimes
    
    # Key insight: We can sort if and only if for every inversion (i, j),
    # the slimes at positions i and j have different colors
    
    # Find all inversions
    inversions = []
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                inversions.append((i, j))
    
    if not inversions:
        print(0)
        return
    
    # Build conflict graph: two positions conflict if they form an inversion
    # and have the same color
    conflicts = set()
    for i, j in inversions:
        if c[i] == c[j]:
            conflicts.add((i, j))
    
    if not conflicts:
        print(0)
        return
    
    # We need to change colors to resolve all conflicts
    # For each conflict (i, j), at least one of c[i] or c[j] must be changed
    
    # This is a vertex cover problem on the conflict graph
    # Use bitmask DP for small n, or greedy for large n
    
    # Extract all positions involved in conflicts
    conflict_pos = set()
    for i, j in conflicts:
        conflict_pos.add(i)
        conflict_pos.add(j)
    
    conflict_list = sorted(conflict_pos)
    m = len(conflict_list)
    
    if m <= 20:
        # Bitmask DP
        min_cost = float('inf')
        for mask in range(1 << m):
            # Check if this mask resolves all conflicts
            valid = True
            for i, j in conflicts:
                idx_i = conflict_list.index(i) if i in conflict_pos else -1
                idx_j = conflict_list.index(j) if j in conflict_pos else -1
                # At least one must be changed
                if not (mask & (1 << idx_i)) and not (mask & (1 << idx_j)):
                    valid = False
                    break
            
            if valid:
                cost = sum(c[conflict_list[k]] for k in range(m) if mask & (1 << k))
                min_cost = min(min_cost, cost)
        
        print(min_cost)
    else:
        # Greedy approach: change colors of positions with highest cost efficiency
        # Simple greedy: for each conflict, change the one with lower cost
        changed = set()
        for i, j in conflicts:
            if i not in changed and j not in changed:
                if c[i] <= c[j]:
                    changed.add(i)
                else:
                    changed.add(j)
        
        print(sum(c[i] for i in changed))

solve()