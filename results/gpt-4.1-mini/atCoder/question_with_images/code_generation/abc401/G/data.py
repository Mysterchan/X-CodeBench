import sys
import math

def input():
    return sys.stdin.readline()

def can(t, dist, n):
    # Build bipartite graph edges where dist[i][j] <= t
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= t:
                graph[i].append(j)
    # Try to find a perfect matching using Hungarian or DFS-based augmenting path
    matchR = [-1] * n

    def bpm(u, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    result = 0
    for i in range(n):
        seen = [False] * n
        if bpm(i, seen):
            result += 1
    return result == n

def main():
    n = int(input())
    sx = []
    sy = []
    for _ in range(n):
        x, y = map(int, input().split())
        sx.append(x)
        sy.append(y)
    gx = []
    gy = []
    for _ in range(n):
        x, y = map(int, input().split())
        gx.append(x)
        gy.append(y)

    dist = [[0]*n for _ in range(n)]
    max_dist = 0.0
    for i in range(n):
        for j in range(n):
            dx = sx[i] - gx[j]
            dy = sy[i] - gy[j]
            d = math.sqrt(dx*dx + dy*dy)
            dist[i][j] = d
            if d > max_dist:
                max_dist = d

    left = 0.0
    right = max_dist
    for _ in range(60):
        mid = (left + right) / 2
        if can(mid, dist, n):
            right = mid
        else:
            left = mid

    print(right)

if __name__ == "__main__":
    main()