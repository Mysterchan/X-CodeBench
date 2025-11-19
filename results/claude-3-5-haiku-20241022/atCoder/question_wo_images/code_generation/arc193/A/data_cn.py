import sys
from collections import deque, defaultdict

def read_input():
    input = sys.stdin.read().split()
    idx = 0
    
    N = int(input[idx])
    idx += 1
    
    W = [0] + [int(input[idx + i]) for i in range(N)]
    idx += N
    
    intervals = [(0, 0)]
    for i in range(N):
        L = int(input[idx])
        R = int(input[idx + 1])
        intervals.append((L, R))
        idx += 2
    
    Q = int(input[idx])
    idx += 1
    
    queries = []
    for i in range(Q):
        s = int(input[idx])
        t = int(input[idx + 1])
        queries.append((s, t))
        idx += 2
    
    return N, W, intervals, Q, queries

def intervals_disjoint(i1, i2):
    l1, r1 = i1
    l2, r2 = i2
    return r1 < l2 or r2 < l1

def build_graph(N, intervals):
    adj = defaultdict(list)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if intervals_disjoint(intervals[i], intervals[j]):
                adj[i].append(j)
                adj[j].append(i)
    return adj

def dijkstra(N, W, adj, start, end):
    dist = [float('inf')] * (N + 1)
    dist[start] = W[start]
    visited = [False] * (N + 1)
    
    pq = [(W[start], start)]
    
    while pq:
        pq.sort()
        d, u = pq.pop(0)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        if u == end:
            return dist[end]
        
        for v in adj[u]:
            if not visited[v]:
                new_dist = dist[u] + W[v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    pq.append((new_dist, v))
    
    return -1

N, W, intervals, Q, queries = read_input()
adj = build_graph(N, intervals)

for s, t in queries:
    result = dijkstra(N, W, adj, s, t)
    print(result)