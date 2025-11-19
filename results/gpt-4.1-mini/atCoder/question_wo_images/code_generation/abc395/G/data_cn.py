import sys
input = sys.stdin.readline

N, K = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Floyd-Warshall to get shortest paths between all pairs
for k in range(N):
    Ck = C[k]
    for i in range(N):
        Ci = C[i]
        ik = Ci[k]
        for j in range(N):
            val = ik + Ck[j]
            if val < Ci[j]:
                Ci[j] = val

# We want to find the minimum cost of a connected subgraph containing:
# vertices 1..K plus s_i and t_i (s_i,t_i in [K+1..N])
# The cost is sum of edges in the subgraph.
# The subgraph can be any connected graph on these vertices (and possibly some others),
# but since we want minimal cost, the minimal Steiner tree on these terminals.

# Since K <= 8, terminals = K + 2 vertices:
# terminals = {1..K} + {s_i, t_i}
# We want minimal Steiner tree on these terminals in a complete graph with edge weights = shortest paths.

# Approach:
# 1. Precompute shortest paths between all vertices (done).
# 2. For the terminals 1..K, precompute minimal Steiner trees for all subsets of terminals.
# 3. For each query, add s_i and t_i as terminals, and find minimal Steiner tree cost.

# But s_i and t_i vary per query, so we cannot precompute all subsets including s_i,t_i.

# Instead, we do:
# - Precompute minimal Steiner tree for terminals 1..K only.
# - For each query, we add s_i and t_i terminals.
# - The minimal Steiner tree on terminals {1..K, s_i, t_i} can be found by:
#   - Build a complete graph on terminals {1..K, s_i, t_i} with edge weights = shortest path distances.
#   - Find minimal Steiner tree on these terminals.
# But this is again a Steiner tree problem with K+2 terminals.

# Since K+2 <= 10, we can do DP Steiner tree on terminals per query.

# To speed up:
# - Precompute shortest paths between all vertices (done).
# - For each query, terminals = [0..K-1] + [s_i-1, t_i-1]
#   (0-based indexing)
# - Build a distance matrix between these terminals.
# - Run Steiner tree DP on these terminals.

# Steiner tree DP:
# Let M = K+2 terminals.
# dp[mask][v] = minimal cost of subtree covering terminals in mask, ending at terminal v
# Initialization:
# dp[1<<i][i] = 0 for i in [0..M-1]
# Transition:
# For mask, for submask in mask:
#   dp[mask][v] = min(dp[submask][v] + dp[mask^submask][v])
# Then relax edges between terminals:
# For each edge u-v:
#   dp[mask][v] = min(dp[mask][v], dp[mask][u] + dist[u][v])

# But this is O(3^M * M^2), too large for M=10 and Q=5000.

# Optimization:
# Use Dreyfus-Wagner algorithm for Steiner tree:
# dp[mask][v] = min over submask of dp[submask][v] + dp[mask^submask][v]
# Then relax edges.

# But still expensive.

# Alternative:
# Since the graph is complete with shortest path distances,
# the minimal Steiner tree on terminals is the minimal spanning tree on terminals with edge weights = shortest path distances.

# Because the graph is metric (shortest path distances), the minimal Steiner tree on terminals in a complete metric graph is the minimal spanning tree on these terminals.

# So minimal Steiner tree cost = MST on terminals with edge weights = shortest path distances.

# So for each query:
# - terminals = [1..K] + s_i + t_i
# - Build complete graph on these terminals with edge weights = shortest path distances
# - Compute MST cost on these terminals

# Since K <= 8, terminals <= 10, MST is fast.

# Precompute terminal indices for 1..K: 0..K-1
# For each query, terminals = [0..K-1] + [s_i-1, t_i-1]

def mst_cost(terminals):
    # terminals: list of vertex indices in [0..N-1]
    m = len(terminals)
    edges = []
    for i in range(m):
        u = terminals[i]
        for j in range(i+1, m):
            v = terminals[j]
            w = C[u][v]
            edges.append((w, i, j))
    edges.sort()
    parent = list(range(m))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    res = 0
    count = 0
    for w,u,v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            res += w
            count += 1
            if count == m-1:
                break
    return res

terminals_base = list(range(K))  # 0-based terminals for 1..K

output = []
for s, t in queries:
    s -= 1
    t -= 1
    terminals = terminals_base + [s, t]
    ans = mst_cost(terminals)
    output.append(str(ans))

print('\n'.join(output))