def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    pieces = [i for i in range(n) if a[i] == '1']
    targets = [i for i in range(n) if b[i] == '1']
    
    if len(pieces) < len(targets):
        return -1
    
    if len(targets) == 0:
        return 0
    
    # Binary search on number of operations
    def can_reach(ops):
        # Check if we can cover all targets with 'ops' operations
        # For each target, we need at least one piece that can reach it
        for target in targets:
            can_cover = False
            for piece in pieces:
                # Can this piece reach this target in 'ops' operations?
                # The piece can move at most 'ops' positions total
                if abs(piece - target) <= ops:
                    can_cover = True
                    break
            if not can_cover:
                return False
        
        # Now check if assignment is possible
        # Greedy: try to assign pieces to targets optimally
        used = [False] * len(pieces)
        for target in targets:
            found = False
            for i, piece in enumerate(pieces):
                if not used[i] and abs(piece - target) <= ops:
                    used[i] = True
                    found = True
                    break
            if not found:
                return False
        return True
    
    left, right = 0, 2 * n
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if can_reach(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

t = int(input())
for _ in range(t):
    print(solve())