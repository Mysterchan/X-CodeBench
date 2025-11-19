import math
import heapq

N, M, X = [int(i) for i in input().split()]
edges = [[] for i in range(N * 2)]
for i in range(M):
  from_, to = [int(j) - 1 for j in input().split()]
  edges[from_].append((to, 1))
  edges[to + N].append((from_ + N, 1))

def dijkstra(start = 0, end = N-1):
  inf = math.inf
  dist = [inf for i in range(N * 2)]
  visited = [False for i in range(N * 2)]
  dist[start] = 0
  queue = [(0, start)]
  
  while queue:
    current_dist, current_node = heapq.heappop(queue)
  
    if visited[current_node]:
      continue
    visited[current_node] = True
    
    for node, cost in edges[current_node]:
      if visited[node]:
        continue
      
      if dist[node] > current_dist + cost:
        dist[node] = current_dist + cost
        heapq.heappush(queue, (current_dist + cost, node))
        if node < N:
          heapq.heappush(queue, (current_dist + cost + X, node + N))
        else:
          heapq.heappush(queue, (current_dist + cost + X, node - N))
          
  print(min(dist[end], dist[end + N]))
        
dijkstra()