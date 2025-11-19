def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    # Count pieces and target positions
    num_pieces = a.count('1')
    num_targets = b.count('1')
    
    if num_pieces != num_targets:
        return -1
    
    # Get positions of pieces and targets
    pieces = [i for i in range(n) if a[i] == '1']
    targets = [i for i in range(n) if b[i] == '1']
    
    # Binary search on the answer
    def can_achieve(max_ops):
        # For each piece, compute the range of final positions it can reach
        # with at most max_ops operations
        piece_ranges = []
        for p in pieces:
            # Piece at position p can reach [p - max_ops, p + max_ops]
            piece_ranges.append((p - max_ops, p + max_ops))
        
        # Try to match pieces to targets using greedy approach
        # Sort both by position (already sorted)
        # For each target, assign the leftmost available piece that can reach it
        used = [False] * len(pieces)
        for t in targets:
            assigned = False
            for i in range(len(pieces)):
                if not used[i]:
                    left, right = piece_ranges[i]
                    if left <= t <= right:
                        used[i] = True
                        assigned = True
                        break
            if not assigned:
                return False
        return True
    
    # Binary search
    left, right = 0, 2 * n
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if can_achieve(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

t = int(input())
for _ in range(t):
    print(solve())