import sys
import collections

def main():
    input = sys.stdin.readline
    N, M, S, T = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # We want to find the minimal number of moves to get:
    # A: S -> T
    # B: T -> S
    # Moves: move either A or B along an edge, but they cannot be on the same vertex at any time.

    # State: (posA, posB)
    # Initial: (S, T)
    # Goal: (T, S)
    # Constraint: posA != posB at all times

    # BFS over states (posA, posB)
    # Number of states: up to N*N = 4*10^10, too large to store all.
    # But we can prune and use a visited set.

    # Use a queue for BFS
    from collections import deque

    visited = set()
    queue = deque()
    queue.append((S, T, 0))
    visited.add((S, T))

    while queue:
        a, b, dist = queue.popleft()
        if a == T and b == S:
            print(dist)
            return

        # Move A
        for na in graph[a]:
            if na != b and (na, b) not in visited:
                visited.add((na, b))
                queue.append((na, b, dist+1))

        # Move B
        for nb in graph[b]:
            if nb != a and (a, nb) not in visited:
                visited.add((a, nb))
                queue.append((a, nb, dist+1))

    print(-1)

if __name__ == "__main__":
    main()