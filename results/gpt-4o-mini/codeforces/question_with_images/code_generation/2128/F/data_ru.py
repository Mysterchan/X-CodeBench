import sys
from collections import defaultdict, deque

def bfs(graph, weights_min, weights_max, start):
    # Initialize distances
    dist_min = [float('inf')] * (n + 1)
    dist_max = [float('-inf')] * (n + 1)
    
    dist_min[start] = 0
    dist_max[start] = 0
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor, l, r in graph[current]:
            if dist_min[neighbor] > dist_min[current] + l:
                dist_min[neighbor] = dist_min[current] + l
                queue.append(neighbor)
            if dist_max[neighbor] < dist_max[current] + r:
                dist_max[neighbor] = dist_max[current] + r
                queue.append(neighbor)
    
    return dist_min, dist_max

input = sys.stdin.read
data = input().splitlines()
index = 0

t = int(data[index])
index += 1
results = []

for _ in range(t):
    n, m, k = map(int, data[index].split())
    index += 1
    
    graph = defaultdict(list)
    
    for __ in range(m):
        u, v, l, r = map(int, data[index].split())
        graph[u].append((v, l, r))
        graph[v].append((u, l, r))
        index += 1
    
    # Getting distances from node 1
    dist_min_1, dist_max_1 = bfs(graph, None, None, 1)
    # Getting distances from node k
    dist_min_k, dist_max_k = bfs(graph, None, None, k)
    # Getting distances from node n
    dist_min_n, dist_max_n = bfs(graph, None, None, n)

    # Check if the condition is satisfied
    # dist_w(1, n) != dist_w(1, k) + dist_w(k, n)
    min_dist_1k = dist_min_1[k]
    min_dist_kn = dist_min_k[n]
    min_dist_1n = dist_min_1[n]

    max_dist_1k = dist_max_1[k]
    max_dist_kn = dist_max_k[n]
    max_dist_1n = dist_max_1[n]

    # We check for the case where the distances can be equal.
    # The max can still be <= the min
    if (min_dist_1n < min_dist_1k + min_dist_kn) and (max_dist_1n == max_dist_1k + max_dist_kn):
        results.append("NO")
    else:
        results.append("YES")

print("\n".join(results))