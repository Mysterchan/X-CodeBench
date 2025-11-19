import sys
import heapq

input = sys.stdin.readline

def dijkstra(n, graph, start, weight):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > dist[current_node]:
            continue
        
        for neighbor, l, r in graph[current_node]:
            new_distance = current_distance + r
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return dist

def can_assign_weights(n, m, k, edges):
    graph = [[] for _ in range(n + 1)]
    
    for u, v, l, r in edges:
        graph[u].append((v, l, r))
        graph[v].append((u, l, r))

    dist_from_1 = dijkstra(n, graph, 1, (0, 0))
    dist_from_k = dijkstra(n, graph, k, (0, 0))
    dist_from_n = dijkstra(n, graph, n, (0, 0))

    dist_1_k = dist_from_1[k]
    dist_k_n = dist_from_k[n]
    dist_1_n = dist_from_1[n]

    # We check for the condition dist_1_n != dist_1_k + dist_k_n
    if dist_1_n == dist_1_k + dist_k_n:
        return "NO"
    
    return "YES"

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        n, m, k = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        result = can_assign_weights(n, m, k, edges)
        results.append(result)
        
    print("\n".join(results))

if __name__ == "__main__":
    main()