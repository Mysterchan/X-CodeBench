import sys
from collections import deque
import threading

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, st = map(int, input().split())
        w = [0] + list(map(int, input().split()))
        tree = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            tree[u].append(v)
            tree[v].append(u)

        dist = [-1] * (n + 1)
        dist[1] = 0
        q = deque([1])
        while q:
            u = q.popleft()
            for v in tree[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        q = deque()
        q.append((st, 1, 0))
        visited = [{} for _ in range(n + 1)]
        max_moves = 0

        while q:
            u, life, t = q.popleft()
            life += w[u]

            if life <= 0 or dist[u] <= t:
                continue

            if visited[u].get(t, -1) >= life:
                continue
            visited[u][t] = life

            for v in tree[u]:
                q.append((v, life, t + 1))

            max_moves = max(max_moves, t + 1)

        print(max_moves)

threading.Thread(target=main).start()
