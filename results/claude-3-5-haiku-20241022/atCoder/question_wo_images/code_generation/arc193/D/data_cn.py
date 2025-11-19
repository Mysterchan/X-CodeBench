def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    # Get positions of pieces in A and required positions in B
    pieces = [i for i in range(n) if a[i] == '1']
    required = [i for i in range(n) if b[i] == '1']
    
    # Check if it's possible
    if len(pieces) < len(required):
        return -1
    
    # For each possible assignment of pieces to required positions,
    # we need to find the minimum cost
    # Since pieces can stack, we need to assign each required position
    # to at least one piece
    
    # Key insight: We can use a greedy approach
    # For each required position, assign it to the closest available piece
    # that hasn't been assigned yet (in a way that minimizes total operations)
    
    # Actually, we need to think about this differently:
    # Each piece needs to move to cover at least one required position
    # Multiple pieces can stack on the same position
    
    # Better approach: Binary search on the answer
    # For a given number of operations k, check if we can satisfy all requirements
    
    def can_satisfy(ops):
        # After ops operations, each piece at position p can reach any position
        # in range that's within ops moves from p
        # But moves are not independent - they're coordinated
        
        # Key insight: If we do ops operations, we can choose ops different values of i
        # Each operation moves all pieces simultaneously
        
        # This is complex. Let's think differently.
        # For each required position r, we need at least one piece to reach it
        # A piece at position p can reach position r with cost |p - r|
        # But operations are global, not per-piece
        
        # Actually, the minimum number of operations is the maximum over all required positions
        # of the minimum distance from any piece to that position
        
        min_ops = 0
        for req_pos in required:
            min_dist = min(abs(req_pos - p) for p in pieces)
            min_ops = max(min_ops, min_dist)
        
        return min_ops
    
    return can_satisfy(0)

t = int(input())
for _ in range(t):
    result = solve()
    print(result)