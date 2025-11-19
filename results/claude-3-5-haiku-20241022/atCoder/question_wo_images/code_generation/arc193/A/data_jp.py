import sys
from collections import deque

def read_input():
    input = sys.stdin.read().split()
    idx = 0
    
    N = int(input[idx])
    idx += 1
    
    W = list(map(int, input[idx:idx+N]))
    idx += N
    
    intervals = []
    for i in range(N):
        L = int(input[idx])
        R = int(input[idx+1])
        intervals.append((L, R))
        idx += 2
    
    Q = int(input[idx])
    idx += 1
    
    queries = []
    for i in range(Q):
        s = int(input[idx])
        t = int(input[idx+1])
        queries.append((s-1, t-1))
        idx += 2
    
    return N, W, intervals, queries

def intervals_disjoint(i1, i2):
    return i1[1] < i2[0] or i2[1] < i1[0]

def build_graph(N, intervals):
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if intervals_disjoint(intervals[i], intervals[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def bfs_min_weight(graph, W, start, end, N):
    visited = [False] * N
    queue = deque([(start, W[start])])
    visited[start] = True
    min_weight = [float('inf')] * N
    min_weight[start] = W[start]
    
    while queue:
        node, weight = queue.popleft()
        
        if node == end:
            continue
        
        for neighbor in graph[node]:
            new_weight = weight + W[neighbor]
            if new_weight < min_weight[neighbor]:
                min_weight[neighbor] = new_weight
                visited[neighbor] = True
                queue.append((neighbor, new_weight))
    
    if min_weight[end] == float('inf'):
        return -1
    return min_weight[end]

def main():
    N, W, intervals, queries = read_input()
    graph = build_graph(N, intervals)
    
    for s, t in queries:
        result = bfs_min_weight(graph, W, s, t, N)
        print(result)

if __name__ == "__main__":
    main()