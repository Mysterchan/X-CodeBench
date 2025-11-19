from collections import deque

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    if all(a == 1 for a in A):
        print("Yes")
        return
    
    # BFS to find if we can make all 1s
    # State: tuple of A (what we can achieve)
    initial = tuple(A)
    visited = {initial}
    queue = deque([initial])
    
    while queue:
        current = queue.popleft()
        
        if all(x == 1 for x in current):
            print("Yes")
            return
        
        # Try placing ARC or CRA at each position
        for i in range(N):
            # Try ARC at position i, i+1, i+2
            i1 = i
            i2 = (i + 1) % N
            i3 = (i + 2) % N
            
            # Operation 1: ARC pattern - sets A[i] and A[i+1] to 1
            new_state = list(current)
            new_state[i1] = 1
            new_state[i2] = 1
            new_tuple = tuple(new_state)
            if new_tuple not in visited:
                visited.add(new_tuple)
                queue.append(new_tuple)
            
            # Operation 2: CRA pattern at i, i+1, i+2 - sets A[i] and A[i+1] to 1
            # (same effect as operation 1 for different pattern)
            # This is already covered above
    
    print("No")

solve()