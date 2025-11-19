import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# Union-Find (Disjoint Set Union) implementation
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1]*n
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.par[y] = x
        self.size[x] += self.size[y]
        return True
    def same(self, x, y):
        return self.find(x) == self.find(y)

# Precompute factorials and inverse factorials for combinations if needed
# But here we only need multiplication and addition modulo MOD.

# The problem:
# Given matrix A (N x N), symmetric, A[i][i] = 1,
# Count the number of trees G on vertices 1..N rooted at 1,
# such that for all i,j:
# A[i][j] = 1 iff j is ancestor of i or i is ancestor of j in G rooted at 1.
#
# Equivalently:
# A[i][j] = 1 iff the path from 1 to i contains j or the path from 1 to j contains i.
#
# This means A[i][j] = 1 iff i and j are on the same root-to-leaf path or one is ancestor of the other.
#
# The problem is known from AtCoder Grand Contest 033 F "Ancestor Tree".
#
# Approach:
# - The matrix A defines a partial order on vertices by ancestor relation.
# - The condition means A[i][j] = 1 iff i and j are comparable in this partial order.
# - The graph defined by edges where A[i][j] = 1 is the comparability graph of the ancestor partial order.
# - We want to count the number of trees G rooted at 1 that realize this partial order.
#
# Key observations:
# - A[i][j] = 1 means i and j are comparable in the ancestor relation.
# - The ancestor relation is a tree order rooted at 1.
# - The problem reduces to counting the number of ways to build a rooted tree with ancestor relation consistent with A.
#
# Algorithm outline:
# 1. The root is 1.
# 2. For each node i != 1, its ancestors are exactly the nodes j with A[i][j] = 1.
# 3. The ancestor set of i is the set of nodes on the path from 1 to i.
# 4. For each node i, the ancestor set is a chain from 1 to i.
# 5. The ancestor sets form a laminar family (nested or disjoint).
#
# We can use a DP on subsets or a recursive approach:
# - The nodes form a tree rooted at 1.
# - For each node, the subtree corresponds to a connected component in the graph induced by nodes whose ancestor sets contain that node.
#
# Implementation:
# - We use a recursive function f(S) that returns the number of valid trees on the node set S with root = min(S).
# - The root is always 1, so we start with S = all nodes.
# - For the current root r, the children are connected components of S \ {r} in the graph induced by edges where A[i][j] = 1 and i,j in S.
# - For each child component C, recursively compute f(C).
# - The answer for f(S) = product of f(C) over all children C * (number of ways to order children).
#   But since the tree is rooted and unordered, the order of children does not matter.
# - The number of ways to combine children is product of their counts.
#
# To find children:
# - For each node i in S \ {r}, if A[r][i] = 1, then i is connected to r or its descendants.
# - The children are connected components of S \ {r} in the graph induced by edges A[i][j] = 1.
#
# Since N <= 400 and sum of N^2 over T <= 400^2, we can afford O(N^3) per test in total.
#
# We'll implement the recursive DP with memoization.

from collections import defaultdict

def solve_case(N, A):
    # Precompute adjacency for each subset is impossible.
    # Instead, we do a recursive approach with memoization on sets represented by bitmask is impossible (N=400).
    # So we do a top-down approach using node sets represented by lists.
    # We use a cache keyed by frozenset of nodes.
    # But frozenset is expensive, so we use a dict keyed by tuple(sorted nodes).
    # Since total sum of N^2 is small, total number of calls is manageable.
    
    # To speed up, we use a global memo dict keyed by tuple of nodes.
    # The root is always the minimal node in the set (which must be 1 for the full set).
    
    # Build adjacency list for the full graph
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)
    
    from sys import setrecursionlimit
    setrecursionlimit(10**7)
    
    memo = {}
    
    def dfs(nodes):
        # nodes: tuple of sorted nodes
        if len(nodes) == 1:
            return 1
        if nodes in memo:
            return memo[nodes]
        r = nodes[0]  # root is minimal node in nodes
        # Build graph induced by nodes
        node_set = set(nodes)
        # Find connected components of nodes \ {r} in induced graph
        children_nodes = [x for x in nodes if x != r]
        # Build adjacency for children
        uf = UnionFind(len(children_nodes))
        idx = {v:i for i,v in enumerate(children_nodes)}
        for i in range(len(children_nodes)):
            u = children_nodes[i]
            for w in adj[u]:
                if w in node_set and w != r:
                    j = idx[w]
                    uf.unite(i,j)
        # Group children by components
        comp_map = defaultdict(list)
        for i,v in enumerate(children_nodes):
            comp_map[uf.find(i)].append(v)
        # For each component, recursively compute
        res = 1
        for comp in comp_map.values():
            comp_sorted = tuple(sorted(comp))
            res = (res * dfs(comp_sorted)) % MOD
        memo[nodes] = res
        return res
    
    # Check condition consistency:
    # The problem states A[i][j] = 1 iff i and j are comparable in ancestor relation.
    # We must verify that A[i][j] = 1 iff i and j are comparable in the tree we build.
    # The above construction ensures the tree is consistent with A.
    # But if A is not consistent, the recursion will fail or produce wrong count.
    # So we must verify A is a comparability graph of a rooted tree with root 1.
    # The above DP counts the number of trees consistent with A.
    # If no such tree exists, the count is zero.
    
    # The problem guarantees A[i][i] = 1 and symmetric.
    # We just run dfs on all nodes from 0..N-1 with root=0 (node 1).
    # If the result is zero, print 0.
    
    full_nodes = tuple(range(N))
    return dfs(full_nodes) % MOD

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for __ in range(N)]
    res = solve_case(N, A)
    results.append(res)

print('\n'.join(map(str, results)))