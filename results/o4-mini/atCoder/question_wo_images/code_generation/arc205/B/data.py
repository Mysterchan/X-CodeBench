import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# The problem reduces to the following:
# We start with M black edges in a complete graph of N vertices.
# We can flip the colors of all edges in any chosen triangle (3 vertices).
# Flipping a triangle toggles the color of its 3 edges.
#
# The operation corresponds to adding the triangle's edge set modulo 2 to the current edge set.
# The set of all edges forms a vector space over GF(2).
#
# The key insight (from known results in similar problems) is:
# The maximum number of black edges achievable by toggling triangles is the maximum number of edges in a complete bipartite subgraph.
#
# Why?
# Because toggling triangles corresponds to adding elements from the cycle space of the complete graph,
# and the maximum black edges achievable is the maximum cut size in the graph.
#
# The maximum cut in a complete graph is achieved by partitioning vertices into two sets of sizes k and N-k,
# and coloring all edges between these two sets black.
#
# The number of edges in such a bipartite subgraph is k*(N-k).
#
# We want to find a partition of vertices into two sets S and T that maximizes the number of black edges after toggling.
#
# Since toggling triangles can flip edges inside the sets, the maximum number of black edges achievable is:
# max_{0 <= k <= N} [k*(N-k)]
#
# The maximum of k*(N-k) is at k = N//2 or k = (N+1)//2.
#
# So the maximum number of black edges achievable is:
# max_cut = max_{k} k*(N-k)
#
# The total number of edges in complete graph is total = N*(N-1)//2
#
# The initial black edges are M.
#
# The parity of the number of black edges mod 2 is invariant under toggling triangles.
# Because each toggle flips 3 edges, which is odd, so parity flips.
# Actually, toggling a triangle flips 3 edges, so parity changes by 3 mod 2 = 1.
# So parity of black edges can be flipped by toggling triangles.
#
# So parity is not invariant, we can reach any parity.
#
# Therefore, the maximum number of black edges achievable is the maximum cut size.
#
# So answer = max_cut = max_{k} k*(N-k)
#
# But we start with M black edges, and toggling triangles can change edges arbitrarily within the cycle space.
# The problem states we can perform zero or more operations.
#
# So the maximum number of black edges achievable is the maximum cut size.
#
# Hence, answer = max_{k} k*(N-k)
#
# Let's compute that.

# Compute maximum cut size in complete graph
k1 = N // 2
k2 = N - k1
max_cut = k1 * k2

print(max_cut)