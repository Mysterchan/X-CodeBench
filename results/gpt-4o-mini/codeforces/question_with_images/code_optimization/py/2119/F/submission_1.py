import sys
from collections import deque

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

        max_moves = 0
        life = 1
        t = 0
        current = st
        
        while True:
            life += w[current]
            if life <= 0 or dist[current] <= t:
                break

            max_moves += 1
            t += 1
            
            # Moving to the next possible vertex
            next_vertex = None
            for neighbor in tree[current]:
                if dist[neighbor] > t:
                    next_vertex = neighbor
                    break

            if next_vertex is not None:
                current = next_vertex
            else:
                break
        
        print(max_moves)

main()