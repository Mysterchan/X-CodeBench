import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m, S, T = map(int, input().split())
    S -= 1
    T -= 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    # Precompute distances from T and from S
    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for w in graph[u]:
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return dist

    distT = bfs(T)
    distS = bfs(S)

    # If either S or T is unreachable from the other, no solution
    if distT[S] == -1 or distS[T] == -1:
        print(-1)
        return

    # BFS over states (a_pos, b_pos)
    # Use a single visited array with a hash function to reduce memory overhead
    # But since n can be up to 2e5, storing visited as a dict is acceptable if we use a fast approach
    # We'll use a dict for visited states

    from array import array

    visited = dict()
    q = deque()
    start = (S, T)
    visited[start] = 0
    q.append(start)

    while q:
        a, b = q.popleft()
        dist = visited[(a, b)]
        if a == T and b == S:
            print(dist)
            return

        # Move piece A
        for a_next in graph[a]:
            if a_next != b:
                state = (a_next, b)
                if state not in visited:
                    visited[state] = dist + 1
                    q.append(state)

        # Move piece B
        for b_next in graph[b]:
            if b_next != a:
                state = (a, b_next)
                if state not in visited:
                    visited[state] = dist + 1
                    q.append(state)

    print(-1)

if __name__ == "__main__":
    main()