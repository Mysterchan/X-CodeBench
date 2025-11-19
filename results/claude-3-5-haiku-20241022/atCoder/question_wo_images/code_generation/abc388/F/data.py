from collections import deque

def solve():
    N, M, A, B = map(int, input().split())
    
    bad_ranges = []
    for _ in range(M):
        L, R = map(int, input().split())
        bad_ranges.append((L, R))
    
    # BFS approach focusing on reachable positions
    # We'll track positions we can reach, focusing on critical points
    
    # Create a set of all critical positions to check
    critical = {1, N}
    for L, R in bad_ranges:
        # Add positions just before and after bad ranges
        if L - 1 > 0:
            critical.add(L - 1)
        if R + 1 <= N:
            critical.add(R + 1)
        # Also add positions we might land on around these ranges
        for offset in range(-B, B+1):
            if 1 <= L + offset <= N:
                critical.add(L + offset)
            if 1 <= R + offset <= N:
                critical.add(R + offset)
    
    critical = sorted(critical)
    
    # Check if a position is bad
    def is_bad(pos):
        for L, R in bad_ranges:
            if L <= pos <= R:
                return True
        return False
    
    # BFS from position 1
    queue = deque([1])
    visited = {1}
    
    while queue:
        pos = queue.popleft()
        
        if pos == N:
            print("Yes")
            return
        
        # Try all possible jumps
        for jump in range(A, B + 1):
            next_pos = pos + jump
            
            if next_pos > N:
                continue
            
            if is_bad(next_pos):
                continue
            
            if next_pos in visited:
                continue
            
            visited.add(next_pos)
            queue.append(next_pos)
        
        # Also check critical positions we can reach
        for crit in critical:
            if crit <= pos or crit > N:
                continue
            
            # Can we reach this critical position from pos?
            diff = crit - pos
            if A <= diff <= B and not is_bad(crit) and crit not in visited:
                visited.add(crit)
                queue.append(crit)
    
    print("No")

solve()