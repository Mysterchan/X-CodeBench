def is_cycle_graph(N, M, edges):
    if M != N:
        return "No"
    
    from collections import defaultdict
    
    graph = defaultdict(set)
    
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    
    for node in range(1, N + 1):
        if len(graph[node]) != 2:
            return "No"
    
    return "Yes"

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

print(is_cycle_graph(N, M, edges))