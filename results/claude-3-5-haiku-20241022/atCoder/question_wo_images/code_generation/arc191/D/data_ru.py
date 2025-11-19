from collections import deque

def solve():
    N, M, S, T = map(int, input().split())
    
    # Построение графа
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS для поиска минимального количества ходов
    # Состояние: (позиция A, позиция B)
    start = (S, T)
    target = (T, S)
    
    if start == target:
        print(0)
        return
    
    queue = deque([start])
    visited = {start}
    dist = {start: 0}
    
    while queue:
        pos_a, pos_b = queue.popleft()
        current_dist = dist[(pos_a, pos_b)]
        
        # Перемещаем фигуру A
        for next_a in graph[pos_a]:
            if next_a != pos_b:  # Не можем переместить A туда, где B
                new_state = (next_a, pos_b)
                if new_state not in visited:
                    visited.add(new_state)
                    dist[new_state] = current_dist + 1
                    if new_state == target:
                        print(current_dist + 1)
                        return
                    queue.append(new_state)
        
        # Перемещаем фигуру B
        for next_b in graph[pos_b]:
            if next_b != pos_a:  # Не можем переместить B туда, где A
                new_state = (pos_a, next_b)
                if new_state not in visited:
                    visited.add(new_state)
                    dist[new_state] = current_dist + 1
                    if new_state == target:
                        print(current_dist + 1)
                        return
                    queue.append(new_state)
    
    print(-1)

solve()