import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
w = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# We want to find the minimal fuel consumption to reach each vertex i from 1.
# The cost to move from u to v is current_weight * 1 (edge cost),
# and current_weight increases by w[v] when arriving at v.
# The weight at u is sum of weights of vertices on the path from 1 to u.

# Define dist[v] = minimal fuel consumption to reach v
# Define weight[v] = sum of weights on the path from 1 to v

# We can use Dijkstra with state (fuel_consumed, weight, vertex)
# and relax edges accordingly:
# When moving from u to v:
#   fuel += weight[u]
#   weight[v] = weight[u] + w[v-1]

INF = 1 << 60
dist = [INF] * (n + 1)
weight = [INF] * (n + 1)

dist[1] = 0
weight[1] = w[0]

heap = [(0, w[0], 1)]  # (fuel_consumed, weight, vertex)

while heap:
    fuel, wt, u = heapq.heappop(heap)
    if dist[u] < fuel:
        continue
    if dist[u] == fuel and weight[u] < wt:
        continue
    for v in adj[u]:
        nfuel = fuel + wt
        nwt = wt + w[v - 1]
        if dist[v] > nfuel or (dist[v] == nfuel and weight[v] > nwt):
            dist[v] = nfuel
            weight[v] = nwt
            heapq.heappush(heap, (nfuel, nwt, v))

# For vertex 1, fuel consumption is 0 (starting point)
dist[1] = 0

for i in range(1, n + 1):
    print(dist[i])