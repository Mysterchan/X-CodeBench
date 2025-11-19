import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    S = int(next(it)) - 1
    T = int(next(it)) - 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph[u].append(v)
        graph[v].append(u)

    # BFS from both starting positions to check reachability
    dist_from_T = [-1] * n
    q = deque([T])
    dist_from_T[T] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist_from_T[v] == -1:
                dist_from_T[v] = dist_from_T[u] + 1
                q.append(v)
    
    dist_from_S = [-1] * n
    q = deque([S])
    dist_from_S[S] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist_from_S[v] == -1:
                dist_from_S[v] = dist_from_S[u] + 1
                q.append(v)

    # Early termination checks
    if dist_from_T[S] == -1 or dist_from_S[T] == -1:
        print(-1)
        return

    # BFS on state space (a, b)
    visited = [[False] * n for _ in range(n)]
    q = deque([(S, T, 0)])
    visited[S][T] = True

    while q:
        a, b, moves = q.popleft()
        
        if a == T and b == S:
            print(moves)
            return

        # Move piece A
        for a_next in graph[a]:
            if a_next != b and not visited[a_next][b]:
                visited[a_next][b] = True
                q.append((a_next, b, moves + 1))

        # Move piece B
        for b_next in graph[b]:
            if b_next != a and not visited[a][b_next]:
                visited[a][b_next] = True
                q.append((a, b_next, moves + 1))

    print(-1)

if __name__ == "__main__":
    main()