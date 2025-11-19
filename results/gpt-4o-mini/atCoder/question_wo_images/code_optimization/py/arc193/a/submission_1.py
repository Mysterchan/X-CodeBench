import heapq
import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx]); idx += 1
    W = list(map(int, data[idx:idx + N])); idx += N
    
    intervals = []
    for i in range(N):
        L, R = map(int, data[idx:idx + 2]); idx += 2
        intervals.append((L, R))

    # Build adjacency list using a line sweep technique
    G = defaultdict(list)
    events = []
    
    for i in range(N):
        L_i, R_i = intervals[i]
        events.append((L_i, 'start', i))
        events.append((R_i + 1, 'end', i))  # end is exclusive, hence R_i + 1
    
    events.sort()  # Sort events by position
    
    active = []  # will hold indices of active intervals
    for event in events:
        position, typ, index = event
        if typ == 'start':
            # Check against all active intervals for intersection
            for j in active:
                # If there's no intersection, we can add the edge
                L_j, R_j = intervals[j]
                if R_j < L_i or R_i < L_j:
                    G[i].append(j)
                    G[j].append(i)
            active.append(index)
        else:
            active.remove(index)

    Q = int(data[idx]); idx += 1
    result = []
    for _ in range(Q):
        s = int(data[idx]) - 1; idx += 1
        t = int(data[idx]) - 1; idx += 1

        min_weight = dijkstra(G, s, t, W)
        result.append(str(min_weight))
    
    print("\n".join(result))

def dijkstra(G, start, end, weights):
    if start == end:
        return weights[start]

    dist = [float('inf')] * len(weights)
    dist[start] = weights[start]

    pq = [(weights[start], start)]

    while pq:
        weight, node = heapq.heappop(pq)

        if weight > dist[node]:
            continue

        if node == end:
            return weight

        for neighbor in G[node]:
            if dist[neighbor] > weight + weights[neighbor]:
                dist[neighbor] = weight + weights[neighbor]
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return -1

if __name__ == "__main__":
    main()