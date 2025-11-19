from collections import deque

def solve():
    N, M, S, T = map(int, input().split())
    
    # Build adjacency list
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to find shortest path
    # State: (pos_A, pos_B, steps)
    queue = deque([(S, T, 0)])
    visited = {(S, T)}
    
    while queue:
        pos_a, pos_b, steps = queue.popleft()
        
        # Check if goal is reached
        if pos_a == T and pos_b == S:
            print(steps)
            return
        
        # Move piece A
        for next_a in graph[pos_a]:
            if next_a != pos_b and (next_a, pos_b) not in visited:
                visited.add((next_a, pos_b))
                queue.append((next_a, pos_b, steps + 1))
        
        # Move piece B
        for next_b in graph[pos_b]:
            if next_b != pos_a and (pos_a, next_b) not in visited:
                visited.add((pos_a, next_b))
                queue.append((pos_a, next_b, steps + 1))
    
    print(-1)

solve()