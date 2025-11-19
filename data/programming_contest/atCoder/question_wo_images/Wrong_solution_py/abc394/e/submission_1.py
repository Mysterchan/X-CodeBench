from collections import deque

def is_palindrome(s):
    return s == s[::-1]

def bfs(N, C):
    dist = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    queue = deque([(i, i, "") for i in range(N)])

    while queue:
        u, v, path = queue.popleft()
        for w in range(N):
            if C[v][w] != "-" and dist[u][w] == float("inf"):
                new_path = path + C[v][w]
                dist[u][w] = len(new_path)
                if is_palindrome(new_path):
                    queue.append((u, w, new_path))
    return dist

def solve(N, C):
    dist = bfs(N, C)
    for i in range(N):
        print(
            " ".join(
                str(dist[i][j]) if dist[i][j] != float("inf") else "-1"
                for j in range(N)
            )
        )

N = int(input())
C = [input().strip() for _ in range(N)]

solve(N, C)