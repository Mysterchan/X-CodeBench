import heapq
from collections import defaultdict

def intervals_disjoint(l1, r1, l2, r2):
    return r1 < l2 or r2 < l1

def dijkstra(graph, start, end, weights, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = weights[start]
    pq = [(weights[start], start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        if u == end:
            return dist[end]
        
        for v in graph[u]:
            new_dist = dist[u] + weights[v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return -1

# Read input
n = int(input())
weights = [0] + list(map(int, input().split()))
intervals = [(0, 0)]
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

# Build adjacency list
graph = defaultdict(list)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        l1, r1 = intervals[i]
        l2, r2 = intervals[j]
        if intervals_disjoint(l1, r1, l2, r2):
            graph[i].append(j)
            graph[j].append(i)

# Process queries
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    result = dijkstra(graph, s, t, weights, n)
    print(result)