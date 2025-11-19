import sys
import threading
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N, M, X = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]
    rev = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        rev[v].append(u)

    # dist[node][state]: minimal cost to reach node with edge direction state
    # state = 0 means edges as given, state = 1 means edges reversed
    INF = 1 << 60
    dist = [[INF, INF] for _ in range(N + 1)]
    dist[1][0] = 0

    # Use 0-1 BFS with deque:
    # - moving along an edge costs 1
    # - flipping all edges costs X
    # We can move from (node, state) to:
    #   - (neighbor, state) with cost +1 (normal edge traversal)
    #   - (node, 1 - state) with cost +X (flip all edges)
    # Because X can be large, we use Dijkstra with a deque and push front/back accordingly.

    from heapq import heappush, heappop
    heap = []
    heappush(heap, (0, 1, 0))  # cost, node, state

    while heap:
        cost, node, state = heappop(heap)
        if dist[node][state] < cost:
            continue
        if node == N:
            print(cost)
            return

        # Flip edges
        nstate = 1 - state
        ncost = cost + X
        if dist[node][nstate] > ncost:
            dist[node][nstate] = ncost
            heappush(heap, (ncost, node, nstate))

        # Move along edges
        if state == 0:
            neighbors = adj[node]
        else:
            neighbors = rev[node]

        ncost = cost + 1
        for nxt in neighbors:
            if dist[nxt][state] > ncost:
                dist[nxt][state] = ncost
                heappush(heap, (ncost, nxt, state))

threading.Thread(target=main).start()