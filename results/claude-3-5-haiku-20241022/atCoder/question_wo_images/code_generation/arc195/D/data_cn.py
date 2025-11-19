from collections import deque

def solve(N, A):
    # BFS to find minimum operations
    initial = tuple(A)
    if not initial:
        return 0
    
    visited = {initial}
    queue = deque([(initial, 0)])
    
    while queue:
        state, ops = queue.popleft()
        
        if not state:
            return ops
        
        # Operation 2: Delete prefix of equal elements
        first = state[0]
        i = 1
        while i < len(state) and state[i] == first:
            i += 1
        
        # Delete elements from index 0 to i-1
        new_state = state[i:]
        if new_state not in visited:
            visited.add(new_state)
            queue.append((new_state, ops + 1))
        
        # Operation 1: Swap adjacent elements
        for i in range(len(state) - 1):
            new_state = list(state)
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, ops + 1))
    
    return -1

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))