import sys
import collections
input = sys.stdin.readline

N, M, S, T = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS on state space: (posA, posB)
# Initial state: (S, T)
# Goal state: (T, S)
# Moves: move A or B along an edge, but cannot move to a vertex occupied by the other piece.

from collections import deque

visited = set()
queue = deque()
queue.append((S, T, 0))
visited.add((S, T))

while queue:
    a, b, dist = queue.popleft()
    if a == T and b == S:
        print(dist)
        break
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
else:
    print(-1)