import sys
input = sys.stdin.readline

# Problem restatement and key points:
# Given N (even), P (prime), for M = N-1 to N(N-1)/2,
# count connected graphs with N vertices and M edges,
# such that the number of vertices at even distance from vertex 1
# equals the number of vertices at odd distance from vertex 1.
# Output counts mod P.

# Key observations:
# - N is even.
# - The condition "number of vertices at even distance = number at odd distance"
#   means the BFS layers from vertex 1 split the graph into two equal parts.
# - This implies the graph is bipartite with bipartition sizes N/2 and N/2,
#   with vertex 1 in the "even" part.
# - The graph is connected.
# - Edges only between the two parts (since bipartite).
# - So the graph is a connected bipartite graph with parts of size N/2 and N/2,
#   vertex 1 in the even part.
# - Number of edges M ranges from N-1 to N(N-1)/2.
# - But since the graph is bipartite with parts of size N/2 and N/2,
#   max edges = (N/2)*(N/2) = N^2/4.
# - So for M > N^2/4, answer is 0.

# So the problem reduces to:
# Count connected bipartite graphs with bipartition sizes (N/2, N/2),
# vertex 1 in the first part, with exactly M edges, for M in [N-1, N^2/4].

# Let's denote:
# n = N/2
# The bipartite graph has parts A and B, each size n.
# Vertex 1 is in A.

# We want to count connected bipartite graphs on (A,B) with M edges,
# where A and B are labeled sets of size n,
# and vertex 1 in A is fixed.

# Connected bipartite graphs with parts A,B correspond to connected bipartite graphs
# with bipartition (A,B).

# The total number of bipartite graphs with parts A,B is 2^(n*n).
# We want to count connected bipartite graphs with M edges.

# Approach:
# Use inclusion-exclusion on connected bipartite graphs.

# Let f(M) = number of bipartite graphs with parts A,B, M edges.
# f(M) = C(n*n, M)

# Let g(M) = number of connected bipartite graphs with parts A,B, M edges.

# We have the standard relation for connected graphs:
# f(M) = sum over partitions of the graph into connected components.
# But here, the graph is bipartite with fixed parts A,B.

# The connectedness is defined on the bipartite graph.

# We can use the exponential formula for bipartite graphs:
# The generating function for bipartite graphs is:
# G(x) = sum_{M} f(M) x^M = (1 + x)^{n*n}

# The generating function for connected bipartite graphs is:
# C(x) = log(G(x)) = log((1+x)^{n*n}) = n*n * log(1+x)

# But this counts connected bipartite graphs without labeling parts separately.

# However, since parts are labeled and fixed, and vertex 1 is fixed in A,
# the connectedness is standard.

# The number of connected bipartite graphs with parts A,B and M edges is:
# g(M) = sum_{k=1}^M mu(k) * (1/k) * sum_{d|k} f(M/d) * d

# This is complicated.

# Alternative approach:
# Use the known formula for connected bipartite graphs with parts sizes n,n:
# The number of connected bipartite graphs with parts sizes n,n is:
# sum_{k=1}^{n} (-1)^{k+1} * C(n,k) * 2^{k*n} * number of connected bipartite graphs on smaller sets.

# This is complicated.

# Instead, use the following approach:

# The number of bipartite graphs with parts A,B is 2^{n*n}.
# The number of bipartite graphs with parts A,B that are disconnected can be counted by inclusion-exclusion on subsets of A or B.

# We want to count connected bipartite graphs with parts A,B.

# The connectivity means the graph is connected as a bipartite graph.

# The graph is connected iff there is no nontrivial partition of A or B that disconnects the graph.

# Use the standard formula for counting connected bipartite graphs:

# Let S be a nonempty proper subset of A.
# The bipartite graph is disconnected if there is no edge between S and B\S or between A\S and B.

# Similarly for subsets of B.

# Use inclusion-exclusion on subsets of A and B to count disconnected graphs.

# But this is exponential in n.

# Since N ≤ 30, n ≤ 15, this is borderline but possibly feasible with bitmask DP.

# However, the problem is hard.

# Alternative approach:

# The problem is known in combinatorics as counting connected bipartite graphs with fixed bipartition sizes.

# The number of connected bipartite graphs with parts sizes n,n is given by:

# g(M) = sum_{k=1}^{2n} (-1)^{k+1} * sum over partitions of the vertex set into k parts * product of number of bipartite graphs on each part.

# This is complicated.

# Since the problem is from a contest, and sample outputs are given,
# and the problem is hard, the intended solution is to use the following:

# The graphs satisfying the condition are exactly connected bipartite graphs with parts sizes n,n,
# vertex 1 in the even part.

# The number of such graphs with M edges is:

# g(M) = number of connected bipartite graphs with parts sizes n,n and M edges.

# The total number of bipartite graphs with parts sizes n,n and M edges is C(n*n, M).

# The number of disconnected bipartite graphs can be computed by inclusion-exclusion on subsets of A.

# Let's define:

# For S subset of A, let B_S = B (all vertices in B).

# The bipartite graph is disconnected if there exists a nonempty proper subset S of A such that
# no edges between S and B\S (which is empty since B_S = B), or no edges between A\S and B.

# Since B is fixed, the graph is disconnected if there exists a nonempty proper subset S of A such that
# no edges between S and B or no edges between A\S and B.

# Similarly for subsets of B.

# So the disconnected bipartite graphs are those where there exists a nonempty proper subset of A or B
# with no edges connecting it to the other part.

# So the number of disconnected bipartite graphs is:

# sum over nonempty proper subsets S of A of number of bipartite graphs with no edges between S and B
# plus sum over nonempty proper subsets T of B of number of bipartite graphs with no edges between A and T
# minus sum over pairs (S,T) of subsets of A and B with no edges between S and B and no edges between A and T (to correct double counting)

# This inclusion-exclusion can be done on subsets of A and B.

# The number of edges possible is n*n.

# For a subset S of A, the edges between S and B are |S|*n.

# If no edges between S and B, then edges can only be chosen from edges between A\S and B, which is (n - |S|)*n edges.

# So number of bipartite graphs with no edges between S and B and M edges is C((n - |S|)*n, M).

# Similarly for subsets T of B.

# For pairs (S,T), no edges between S and B and no edges between A and T means edges only between A\S and B\T.

# Number of edges possible is (n - |S|)*(n - |T|).

# So number of bipartite graphs with no edges between S and B and no edges between A and T and M edges is C((n - |S|)*(n - |T|), M).

# Using inclusion-exclusion:

# disconnected(M) = sum_{S⊂A, S≠∅} C((n - |S|)*n, M)
#                 + sum_{T⊂B, T≠∅} C(n*(n - |T|), M)
#                 - sum_{S⊂A, S≠∅} sum_{T⊂B, T≠∅} C((n - |S|)*(n - |T|), M)

# Then connected(M) = total(M) - disconnected(M)

# total(M) = C(n*n, M)

# We must be careful with the empty subsets and full subsets.

# Implementation plan:

# 1. Precompute factorials and inverse factorials modulo P for combinations up to n*n.
# 2. For each M in [N-1, n*n]:
#    - Compute total = C(n*n, M)
#    - Compute sumS = sum over s=1 to n-1 of C(n, s) * C((n - s)*n, M)
#    - Compute sumT = same as sumS (symmetry)
#    - Compute sumST = sum over s=1 to n-1 sum over t=1 to n-1 of C(n, s)*C(n, t)*C((n - s)*(n - t), M)
#    - disconnected = sumS + sumT - sumST
#    - connected = total - disconnected mod P
# 3. Output connected for M in [N-1, n*n], and 0 for M > n*n up to N(N-1)/2.

# Note: For M < N-1, connected graphs do not exist, so no output needed.
# For M > n*n, output 0.

# Also, vertex 1 is fixed in A, so the count is correct.

# Let's implement this.

MOD = None

def modinv(a, p):
    return pow(a, p-2, p)

def precompute_factorials(max_n, p):
    fact = [1]*(max_n+1)
    invfact = [1]*(max_n+1)
    for i in range(2, max_n+1):
        fact[i] = fact[i-1]*i % p
    invfact[max_n] = modinv(fact[max_n], p)
    for i in reversed(range(1, max_n)):
        invfact[i] = invfact[i+1]*(i+1) % p
    return fact, invfact

def comb(n, r, fact, invfact, p):
    if r > n or r < 0:
        return 0
    return fact[n]*invfact[r]%p*invfact[n-r]%p

def main():
    global MOD
    N, P = map(int, input().split())
    MOD = P
    n = N//2
    max_edges = n*n
    max_total_edges = N*(N-1)//2

    fact, invfact = precompute_factorials(max_total_edges, MOD)

    # Precompute C(n, s) for s=0..n
    Cn = [comb(n, s, fact, invfact, MOD) for s in range(n+1)]

    # Precompute combinations C(x, m) for all x <= n*n and m in [N-1, max_total_edges]
    # But this is too large.

    # Instead, for each M, compute needed combinations on the fly.

    # To speed up, precompute all needed combinations C(x, M) for x in [0, n*n], M in [N-1, max_total_edges]
    # But max_total_edges can be up to 435 for N=30, which is feasible.

    # We'll precompute factorials up to max_total_edges.

    # For each M in [N-1, max_total_edges]:
    #   total = C(n*n, M)
    #   sumS = sum_{s=1}^{n-1} C(n, s)*C((n - s)*n, M)
    #   sumT = same as sumS
    #   sumST = sum_{s=1}^{n-1} sum_{t=1}^{n-1} C(n, s)*C(n, t)*C((n - s)*(n - t), M)
    #   disconnected = sumS + sumT - sumST
    #   connected = total - disconnected mod P

    # For M > n*n, connected = 0

    # Output connected for M in [N-1, max_total_edges], then 0 for M in (max_total_edges, max_total_edges]

    # Precompute C(x, M) for all x in [0, n*n] and M in [N-1, max_total_edges]
    # We'll do on the fly with memoization.

    from functools import lru_cache

    @lru_cache(None)
    def c(x, m):
        return comb(x, m, fact, invfact, MOD)

    results = []
    for M in range(N-1, max_total_edges+1):
        total = c(n*n, M)
        sumS = 0
        for s in range(1, n):
            val = Cn[s]*c((n - s)*n, M) % MOD
            sumS = (sumS + val) % MOD
        sumT = sumS  # symmetric
        sumST = 0
        for s in range(1, n):
            Cs = Cn[s]
            for t in range(1, n):
                Ct = Cn[t]
                val = Cs*Ct*c((n - s)*(n - t), M) % MOD
                sumST = (sumST + val) % MOD
        disconnected = (sumS + sumT - sumST) % MOD
        connected = (total - disconnected) % MOD
        results.append(connected)

    # For M > max_edges up to max_total_edges, output 0
    zeros = [0]*(max_total_edges - max_edges)
    results.extend(zeros)

    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()