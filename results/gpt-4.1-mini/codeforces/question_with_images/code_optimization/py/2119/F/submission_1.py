import sys
from collections import deque

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, st = map(int, input().split())
        w = [0] + list(map(int, input().split()))
        tree = [[] for _ in range(n + 1)]
        for __ in range(n - 1):
            u, v = map(int, input().split())
            tree[u].append(v)
            tree[v].append(u)

        # Compute distance from root (1) to all nodes
        dist = [-1] * (n + 1)
        dist[1] = 0
        q = deque([1])
        while q:
            u = q.popleft()
            for v in tree[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        # We will do a BFS from st with states (node, life)
        # To avoid large memory and time, we keep track of max life reached at each node and time
        # But time can be large, so we use a dictionary per node is expensive.
        # Instead, we use a dictionary keyed by (node, life) or better:
        # Since life can be large, we use a dictionary keyed by (node, life) is also expensive.
        # We can use a dictionary keyed by (node, life) but prune states with life <= 0 or flooded nodes.
        # To optimize, we use a dictionary visited[node] = max life reached at node at any time.
        # We only enqueue if current life > visited[node]

        visited = [-1] * (n + 1)
        q = deque()
        # Initial state: at st, time=0, life=1 (before adding w[st])
        # But problem states at time 0, life += w[u], so life = 1 + w[st] initially
        # w[st] = 1 guaranteed
        initial_life = 1 + w[st]
        if initial_life <= 0 or dist[st] <= 0:
            # Die immediately, no moves possible
            print(0)
            continue

        q.append((st, initial_life, 0))
        visited[st] = initial_life
        max_moves = 0

        while q:
            u, life, t = q.popleft()
            # Check if flooded or dead
            if life <= 0 or dist[u] <= t:
                continue

            # Update max moves
            max_moves = max(max_moves, t)

            for v in tree[u]:
                # Next time step
                nt = t + 1
                # Life at next node after adding w[v]
                nl = life + w[v]
                # Check if alive and not flooded at next time
                if nl <= 0 or dist[v] <= nt:
                    continue
                # Prune states with no improvement
                if visited[v] >= nl:
                    continue
                visited[v] = nl
                q.append((v, nl, nt))

        print(max_moves)

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()