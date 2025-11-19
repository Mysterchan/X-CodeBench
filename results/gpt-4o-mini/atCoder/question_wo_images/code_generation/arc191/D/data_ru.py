from collections import deque, defaultdict
import sys

input = sys.stdin.read

def bfs(start, graph, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # not visited
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

def main():
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    S = int(data[2])
    T = int(data[3])
    
    graph = defaultdict(list)
    
    index = 4
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    dist_from_A = bfs(S, graph, N)
    dist_from_B = bfs(T, graph, N)
    
    min_moves = float('inf')
    
    for i in range(1, N + 1):
        if i != S and i != T:
            moves = dist_from_A[i] + dist_from_B[i]
            if moves != -2:  # -2 means unreachable
                min_moves = min(min_moves, moves)
    
    if min_moves == float('inf'):
        print(-1)
    else:
        print(min_moves)

if __name__ == "__main__":
    main()