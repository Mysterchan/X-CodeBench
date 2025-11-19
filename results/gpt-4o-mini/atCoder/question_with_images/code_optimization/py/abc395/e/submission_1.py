import heapq

def optimized_solution():
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        reverse_graph[v-1].append(u-1)

    # Priority queue for (cost, node, is_reversed)
    pq = []
    dp = [[float('inf')] * 2 for _ in range(n)]
    
    # Starting at node 1 (index 0), not reversed (0)
    heapq.heappush(pq, (0, 0, 0))
    
    while pq:
        cost, node, is_reversed = heapq.heappop(pq)
        
        if dp[node][is_reversed] != float('inf'):
            continue
        
        dp[node][is_reversed] = cost
        
        # Cost to reverse and go to the same node
        if is_reversed:
            # If reversed, go on the original edges
            for neighbor in graph[node]:
                if dp[neighbor][1] == float('inf'):
                    heapq.heappush(pq, (cost + 1, neighbor, 1))
            # Also consider reversing the edges
            if dp[node][0] == float('inf'):
                heapq.heappush(pq, (cost + x, node, 0))
        else:
            # If not reversed, go on the reversed edges
            for neighbor in reverse_graph[node]:
                if dp[neighbor][0] == float('inf'):
                    heapq.heappush(pq, (cost + 1, neighbor, 0))
            # Also consider reversing the edges
            if dp[node][1] == float('inf'):
                heapq.heappush(pq, (cost + x, node, 1))
    
    ans = min(dp[n-1])
    print(ans if ans != float('inf') else -1)

optimized_solution()