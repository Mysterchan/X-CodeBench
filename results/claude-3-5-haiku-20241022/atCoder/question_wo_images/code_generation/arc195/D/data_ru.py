from collections import deque

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # BFS для поиска минимального количества операций
    initial = tuple(a)
    queue = deque([(initial, 0)])
    visited = {initial}
    
    while queue:
        state, ops = queue.popleft()
        
        if len(state) == 0:
            return ops
        
        # Операция 2: удаление префикса одинаковых элементов
        for i in range(1, len(state) + 1):
            if all(state[j] == state[0] for j in range(i)):
                new_state = state[i:]
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, ops + 1))
        
        # Операция 1: обмен соседних элементов
        for i in range(len(state) - 1):
            new_state = list(state)
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, ops + 1))
    
    return -1

t = int(input())
for _ in range(t):
    print(solve())