from collections import deque

def solve(n, a):
    # BFS to find minimum operations
    initial = tuple(a)
    if not initial:
        return 0
    
    queue = deque([(initial, 0)])
    visited = {initial}
    
    while queue:
        state, ops = queue.popleft()
        
        # Try deletion operations
        # Find longest prefix of equal elements
        i = 1
        while i < len(state) and state[i] == state[0]:
            i += 1
        
        # Can delete prefix of length 1 to i
        for delete_len in range(1, i + 1):
            new_state = state[delete_len:]
            if not new_state:  # Empty sequence
                return ops + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, ops + 1))
        
        # Try swap operations
        for i in range(len(state) - 1):
            new_state = list(state)
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, ops + 1))
    
    return -1  # Should never reach here

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(solve(n, a))

for r in results:
    print(r)