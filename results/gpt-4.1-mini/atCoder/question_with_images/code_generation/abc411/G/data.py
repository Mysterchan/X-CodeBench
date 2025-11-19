import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Since N <= 20, we can use bitmask DP on vertices.
# The problem asks for the number of edge subsets that form a simple cycle.
# A simple cycle is a connected subgraph with equal number of edges and vertices,
# and each vertex has degree 2 in that subgraph.

# Key observations:
# - Each cycle corresponds to a subset of vertices S with |S|=k >= 2,
#   and a subset of edges E' with |E'|=k,
#   such that the induced subgraph on S with edges E' is a simple cycle.
# - We want to count all such edge subsets modulo 998244353.

# Approach:
# 1. Group edges by the pair of vertices (u,v).
#    Since multi-edges are allowed, multiple edges can connect the same pair.
# 2. For each subset of vertices S (bitmask), check if the induced subgraph can form a cycle.
#    Conditions:
#    - Number of edges in induced subgraph = number of vertices in S
#    - Each vertex in S has degree 2 in the induced subgraph
#    - The induced subgraph is connected
# 3. For each such S, count the number of ways to choose edges from the multi-edges between pairs in S
#    to form the cycle.
#    Since multiple edges can connect the same pair, the number of ways is the product of the counts
#    of edges chosen for each edge in the cycle.
# 4. Sum over all such subsets.

# Complexity:
# - There are 2^N subsets of vertices, N <= 20 => about 1 million subsets.
# - For each subset, checking connectivity and degrees can be done efficiently.
# - We must be careful to prune subsets that cannot form cycles early.

# Implementation details:
# - Precompute adjacency matrix with counts of edges between vertices.
# - For each subset S:
#   - Count number of vertices k = popcount(S)
#   - If k < 2: continue
#   - Count number of edges in induced subgraph = sum of counts of edges between vertices in S
#   - If number of edges != k: continue
#   - Check if all vertices have degree 2 in induced subgraph
#   - Check connectivity of induced subgraph
#   - If all conditions met, calculate number of ways:
#     For the cycle edges, each edge corresponds to a pair of vertices in the cycle.
#     The cycle is a permutation of vertices, but since the cycle is simple,
#     the edges form a cycle graph on S.
#     The number of ways to choose edges is the product of the counts of edges between consecutive vertices in the cycle.
#   - But how to find the cycle and count ways?
#     Since the induced subgraph is a 2-regular connected graph on k vertices,
#     it is a cycle.
#     The edges between vertices in S form a cycle graph.
#     The edges between each pair of adjacent vertices in the cycle can be multiple.
#     The number of ways to choose edges is the product of the counts of edges between adjacent vertices in the cycle.
#   - We need to find the cycle order to multiply counts.
#     Since the graph is a cycle, we can find the cycle order by DFS.

# Steps:
# - For each subset S:
#   - Check conditions
#   - Find cycle order by DFS
#   - Calculate product of counts of edges between consecutive vertices in cycle
#   - Add to answer

# Preprocessing adjacency matrix with counts of edges:
adj_count = [[0]*N for _ in range(N)]
for u,v in edges:
    u -= 1
    v -= 1
    adj_count[u][v] += 1
    adj_count[v][u] += 1

def popcount(x):
    return bin(x).count('1')

def get_vertices(S):
    return [i for i in range(N) if (S & (1 << i))]

def is_connected(S, vertices):
    # BFS or DFS on induced subgraph
    if not vertices:
        return False
    visited = set()
    stack = [vertices[0]]
    visited.add(vertices[0])
    while stack:
        u = stack.pop()
        for v in vertices:
            if v not in visited and adj_count[u][v] > 0:
                visited.add(v)
                stack.append(v)
    return len(visited) == len(vertices)

def degrees(S, vertices):
    deg = [0]*N
    for i in range(len(vertices)):
        u = vertices[i]
        for j in range(i+1, len(vertices)):
            v = vertices[j]
            if adj_count[u][v] > 0:
                deg[u] += adj_count[u][v]
                deg[v] += adj_count[u][v]
    return deg

def find_cycle_order(S, vertices):
    # The induced subgraph is a cycle graph (2-regular connected)
    # We find the cycle order by walking from any vertex
    # Each vertex has degree 2, so neighbors in S are exactly 2
    # We can find neighbors in S by checking adj_count[u][v] > 0
    # Since multiple edges can exist, neighbors are vertices with adj_count[u][v] > 0
    # We pick one neighbor to start and walk until we come back to start
    u = vertices[0]
    # find neighbors of u in S
    neighbors = [v for v in vertices if adj_count[u][v] > 0]
    # start from u, go to neighbors[0]
    cycle = [u]
    prev = u
    curr = neighbors[0]
    cycle.append(curr)
    while curr != u:
        # find neighbors of curr in S except prev
        nbrs = [w for w in vertices if w != prev and adj_count[curr][w] > 0]
        if not nbrs:
            # no next vertex, invalid
            return None
        prev, curr = curr, nbrs[0]
        if curr == u:
            break
        cycle.append(curr)
    return cycle

ans = 0

for S in range(1 << N):
    k = popcount(S)
    if k < 2:
        continue
    vertices = get_vertices(S)
    # count edges in induced subgraph
    edge_count = 0
    for i in range(k):
        u = vertices[i]
        for j in range(i+1, k):
            v = vertices[j]
            edge_count += adj_count[u][v]
    if edge_count != k:
        continue
    deg = degrees(S, vertices)
    # check all degrees == 2
    if any(deg[v] != 2 for v in vertices):
        continue
    # check connectivity
    if not is_connected(S, vertices):
        continue
    # find cycle order
    cycle = find_cycle_order(S, vertices)
    if cycle is None:
        continue
    # calculate number of ways
    ways = 1
    for i in range(k):
        u = cycle[i]
        v = cycle[(i+1) % k]
        ways = (ways * adj_count[u][v]) % MOD
    ans = (ans + ways) % MOD

print(ans)