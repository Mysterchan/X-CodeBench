import heapq
from collections import defaultdict

def main():
    N = int(input())
    W = list(map(int, input().split()))
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    
    # Build adjacency list using optimized interval checking
    G = [[] for _ in range(N)]
    
    # Use events to find non-overlapping intervals
    events = []
    for i in range(N):
        L, R = intervals[i]
        events.append((L, 0, i))  # start event
        events.append((R + 1, 1, i))  # end event
    
    events.sort()
    
    active = set()
    for point, event_type, idx in events:
        if event_type == 0:  # start
            # All currently active intervals overlap with this one
            # So this interval connects to all NOT in active
            for j in range(N):
                if j != idx and j not in active:
                    # Check if they actually don't overlap
                    L_i, R_i = intervals[idx]
                    L_j, R_j = intervals[j]
                    if R_i < L_j or R_j < L_i:
                        G[idx].append(j)
                        G[j].append(idx)
            active.add(idx)
        else:  # end
            active.discard(idx)
    
    # Deduplicate edges
    for i in range(N):
        G[i] = list(set(G[i]))
    
    # Cache for query results
    cache = {}
    
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        
        if (s, t) in cache:
            print(cache[(s, t)])
        else:
            min_weight = dijkstra(G, s, t, W, N)
            cache[(s, t)] = min_weight
            cache[(t, s)] = min_weight
            print(min_weight)

def dijkstra(G, start, end, weights, N):
    dist = [float('inf')] * N
    dist[start] = weights[start]
    pq = [(weights[start], start)]
    
    while pq:
        weight, node = heapq.heappop(pq)
        
        if weight > dist[node]:
            continue
        
        if node == end:
            return weight
        
        for neighbor in G[node]:
            new_dist = weight + weights[neighbor]
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return -1

if __name__ == "__main__":
    main()