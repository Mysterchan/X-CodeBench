def process_case(n, m, k, edges):
    from collections import defaultdict
    import sys
    
    graph = defaultdict(list)
    
    for u, v, l, r in edges:
        graph[u].append((v, l, r))
        graph[v].append((u, l, r))

    def get_distance(source, target, is_min):
        # Use Dijkstra's algorithm to calculate distances
        import heapq
        
        dist = {node: (0, 0) for node in range(1, n + 1)}  # (min_dist, max_dist)
        dist[source] = (0, 0)
        pq = []
        heapq.heappush(pq, (0, source, 0))  # (current_distance, current_node, is_min)
        
        while pq:
            current_dist, current_node, is_min = heapq.heappop(pq)
            if current_dist != dist[current_node][is_min]:
                continue
            
            for neighbor, l, r in graph[current_node]:
                new_dist_min = current_dist + l
                new_dist_max = current_dist + r
                
                if new_dist_min < dist[neighbor][0]:
                    dist[neighbor] = (new_dist_min, dist[neighbor][1])
                    heapq.heappush(pq, (new_dist_min, neighbor, 0))
                
                if new_dist_max < dist[neighbor][1]:
                    dist[neighbor] = (dist[neighbor][0], new_dist_max)
                    heapq.heappush(pq, (new_dist_max, neighbor, 1))
        
        return dist[target]
    
    dist_1_n = get_distance(1, n, True)[0]  # minimum distance from 1 to n
    dist_1_k = get_distance(1, k, True)[0]  # minimum distance from 1 to k
    dist_k_n = get_distance(k, n, True)[0]  # minimum distance from k to n
    
    dist_max_1_n = get_distance(1, n, False)[1]  # maximum distance from 1 to n
    dist_max_1_k = get_distance(1, k, False)[1]  # maximum distance from 1 to k
    dist_max_k_n = get_distance(k, n, False)[1]  # maximum distance from k to n
    
    # Check if the distances can be arranged to satisfy the condition
    if dist_1_n == dist_1_k + dist_k_n:
        # Check the case with the maximum distances
        if dist_max_1_n == dist_max_1_k + dist_max_k_n:
            return "NO"
    
    return "YES"

def main():
    input_data = sys.stdin.read().strip().splitlines()
    index = 0
    t = int(input_data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m, k = map(int, input_data[index].split())
        index += 1
        edges = []
        
        for __ in range(m):
            u, v, l, r = map(int, input_data[index].split())
            edges.append((u, v, l, r))
            index += 1
        
        result = process_case(n, m, k, edges)
        results.append(result)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()