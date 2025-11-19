def can_assign_weights(test_cases):
    results = []
    for n, m, k, edges in test_cases:
        # Construct the graph with ranges
        graph = [[] for _ in range(n + 1)]
        for u, v, l, r in edges:
            graph[u].append((v, l, r))
            graph[v].append((u, l, r))

        # Calculate d1, dk, dn lower and upper bounds
        inf = float('inf')
        
        d1_min, d1_max = 0, 0
        dk_min, dk_max = 0, 0
        dn_min, dn_max = 0, 0
        
        def bfs(start):
            import collections
            dist_min = [inf] * (n + 1)
            dist_max = [-inf] * (n + 1)
            dist_min[start], dist_max[start] = 0, 0
            
            queue = collections.deque([start])
            while queue:
                node = queue.popleft()
                for neighbor, l, r in graph[node]:
                    new_min = dist_min[node] + l
                    new_max = dist_max[node] + r
                    
                    if new_min < dist_min[neighbor]:
                        dist_min[neighbor] = new_min
                        queue.append(neighbor)
                    if new_max > dist_max[neighbor]:
                        dist_max[neighbor] = new_max
                        queue.append(neighbor)
            
            return dist_min, dist_max
        
        # Get the distances from 1, k, and n
        d1_min, d1_max = bfs(1)
        dk_min, dk_max = bfs(k)
        dn_min, dn_max = bfs(n)
        
        # Verify the condition dist_w(1, n) != dist_w(1, k) + dist_w(k, n)
        if d1_min[n] < dk_min + dn_min or d1_max[n] > dk_max + dn_max:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n, m, k = map(int, data[index].split())
    index += 1
    edges = []
    for __ in range(m):
        u, v, l, r = map(int, data[index].split())
        edges.append((u, v, l, r))
        index += 1
    test_cases.append((n, m, k, edges))

# Invoke the function and print the results
results = can_assign_weights(test_cases)
print("\n".join(results))