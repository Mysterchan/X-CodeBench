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
            if distances[neighbor] == -1:  # Not visited
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

def min_moves_to_swap(N, M, S, T, edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    dist_from_A = bfs(S, graph, N)
    dist_from_B = bfs(T, graph, N)
    
    if dist_from_A[T] == -1 or dist_from_B[S] == -1:
        return -1
    
    min_moves = float('inf')
    
    for i in range(1, N + 1):
        if i != S and i != T:
            if dist_from_A[i] != -1 and dist_from_B[i] != -1:
                moves = dist_from_A[i] + dist_from_B[i] + 2
                min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

def main():
    data = input().splitlines()
    N, M, S, T = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]
    
    result = min_moves_to_swap(N, M, S, T, edges)
    print(result)

if __name__ == "__main__":
    main()