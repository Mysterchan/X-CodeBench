import sys
input = sys.stdin.readline

N, M = map(int, input().split())
deg = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1

total_edges = N * (N - 1) // 2
sum_deg = sum(deg)
sum_deg_sq = 0
for d in deg[1:]:
    sum_deg_sq += d * d

# Maximum number of black edges after operations:
# max_black = (sum_deg_sq + sum_deg) // 2
# but cannot exceed total edges
ans = (sum_deg_sq + sum_deg) // 2
if ans > total_edges:
    ans = total_edges

print(ans)