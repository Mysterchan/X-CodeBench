from collections import deque

def solve():
    N, M, S, T = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS in state space (pos_A, pos_B)
    start = (S, T)
    goal = (T, S)
    
    if start == goal:
        print(0)
        return
    
    queue = deque([start])
    visited = {start}
    dist = {start: 0}
    
    while queue:
        a, b = queue.popleft()
        current_dist = dist[(a, b)]
        
        # Move piece A
        for next_a in adj[a]:
            if next_a != b:  # Cannot move to where B is
                new_state = (next_a, b)
                if new_state not in visited:
                    visited.add(new_state)
                    dist[new_state] = current_dist + 1
                    if new_state == goal:
                        print(current_dist + 1)
                        return
                    queue.append(new_state)
        
        # Move piece B
        for next_b in adj[b]:
            if next_b != a:  # Cannot move to where A is
                new_state = (a, next_b)
                if new_state not in visited:
                    visited.add(new_state)
                    dist[new_state] = current_dist + 1
                    if new_state == goal:
                        print(current_dist + 1)
                        return
                    queue.append(new_state)
    
    print(-1)

solve()