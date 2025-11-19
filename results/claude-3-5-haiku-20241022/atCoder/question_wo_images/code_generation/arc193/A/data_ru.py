import sys
from collections import deque

def read_input():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    
    N = int(input_lines[idx])
    idx += 1
    
    W = list(map(int, input_lines[idx].split()))
    idx += 1
    
    intervals = []
    for i in range(N):
        L, R = map(int, input_lines[idx].split())
        intervals.append((L, R))
        idx += 1
    
    Q = int(input_lines[idx])
    idx += 1
    
    queries = []
    for i in range(Q):
        s, t = map(int, input_lines[idx].split())
        queries.append((s-1, t-1))
        idx += 1
    
    return N, W, intervals, Q, queries

def intervals_disjoint(int1, int2):
    L1, R1 = int1
    L2, R2 = int2
    return R1 < L2 or R2 < L1

def build_graph(N, intervals):
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if intervals_disjoint(intervals[i], intervals[j]):
                adj[i].append(j)
                adj[j].append(i)
    return adj

def dijkstra(N, W, adj, start, end):
    import heapq
    
    dist = [float('inf')] * N
    dist[start] = W[start]
    pq = [(W[start], start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        if u == end:
            return dist[end]
        
        for v in adj[u]:
            new_dist = dist[u] + W[v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return -1 if dist[end] == float('inf') else dist[end]

def main():
    N, W, intervals, Q, queries = read_input()
    adj = build_graph(N, intervals)
    
    for s, t in queries:
        result = dijkstra(N, W, adj, s, t)
        print(result)

if __name__ == "__main__":
    main()