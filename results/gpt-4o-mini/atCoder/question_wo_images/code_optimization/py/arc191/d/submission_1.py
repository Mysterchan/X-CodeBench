import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    S = int(data[idx]) - 1; idx += 1
    T = int(data[idx]) - 1; idx += 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        graph[u].append(v)
        graph[v].append(u)

    distT_arr = [-1] * n
    distS_arr = [-1] * n

    def bfs(start, dist_arr):
        queue = deque([start])
        dist_arr[start] = 0
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist_arr[v] == -1:
                    dist_arr[v] = dist_arr[u] + 1
                    queue.append(v)

    bfs(T, distT_arr)
    bfs(S, distS_arr)

    if distT_arr[S] == -1:
        print(-1)
        return

    min_moves = float('inf')

    for i in range(n):
        if distT_arr[i] != -1 and distS_arr[i] != -1:
            d1 = distT_arr[i]
            d2 = distS_arr[i]
            moves_to_i = d1 + d2
            if moves_to_i % 2 == 0:
                min_moves = min(min_moves, moves_to_i)

    result = -1 if min_moves == float('inf') else min_moves + distT_arr[S]
    print(result)

if __name__ == "__main__":
    main()