import heapq

def main():

    N = int(input())
    W = list(map(int, input().split()))
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))

    G = [[] for _ in range(N)]
    for i in range(N):
        L_i, R_i = intervals[i]
        for j in range(i+1, N):
            L_j, R_j = intervals[j]
            if R_i < L_j or R_j < L_i:
                G[i].append(j)
                G[j].append(i)

    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1

        min_weight = dijkstra(G, s, t, W)
        print(min_weight)

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