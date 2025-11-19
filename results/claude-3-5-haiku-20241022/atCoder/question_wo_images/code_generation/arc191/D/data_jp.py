from collections import deque

def solve():
    N, M, S, T = map(int, input().split())
    S -= 1
    T -= 1
    
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to find shortest path with state (pos_A, pos_B)
    queue = deque([(S, T, 0)])
    visited = {(S, T)}
    
    while queue:
        pos_a, pos_b, dist = queue.popleft()
        
        if pos_a == T and pos_b == S:
            print(dist)
            return
        
        # Move piece A
        for next_a in graph[pos_a]:
            if next_a != pos_b and (next_a, pos_b) not in visited:
                visited.add((next_a, pos_b))
                queue.append((next_a, pos_b, dist + 1))
        
        # Move piece B
        for next_b in graph[pos_b]:
            if next_b != pos_a and (pos_a, next_b) not in visited:
                visited.add((pos_a, next_b))
                queue.append((pos_a, next_b, dist + 1))
    
    print(-1)

solve()