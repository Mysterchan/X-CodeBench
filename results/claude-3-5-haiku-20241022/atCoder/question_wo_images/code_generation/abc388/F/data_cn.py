from collections import deque

def solve():
    N, M, A, B = map(int, input().split())
    
    bad_ranges = []
    for _ in range(M):
        L, R = map(int, input().split())
        bad_ranges.append((L, R))
    
    # BFS to find if we can reach N from 1
    queue = deque([1])
    visited = {1}
    
    while queue:
        x = queue.popleft()
        
        # Try all possible jumps from x
        for jump in range(A, B + 1):
            next_pos = x + jump
            
            # Check if next_pos is valid
            if next_pos > N:
                break
            
            if next_pos in visited:
                continue
            
            # Check if next_pos is a bad block
            is_bad = False
            for L, R in bad_ranges:
                if L <= next_pos <= R:
                    is_bad = True
                    break
            
            if not is_bad:
                if next_pos == N:
                    print("Yes")
                    return
                
                visited.add(next_pos)
                queue.append(next_pos)
    
    print("No")

solve()