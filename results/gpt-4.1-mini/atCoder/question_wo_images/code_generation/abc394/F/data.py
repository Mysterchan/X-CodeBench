import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

# We want to find a subtree that is a tree where every vertex has degree 1 or 4,
# and at least one vertex has degree 4.
# The subtree must be connected and is a subgraph of the original tree.

# Key observations:
# - The subtree is a tree.
# - Each vertex in the subtree has degree either 1 or 4.
# - At least one vertex has degree 4.
# - We want the maximum number of vertices in such a subtree.

# Approach:
# We do a DP on the tree.
# For each node, we consider the subtree rooted at that node.
# We want to select a subset of children to form a subtree with the node,
# such that the node's degree in the subtree is either 1 or 4.
# The node's degree = number of children included + (1 if parent edge included else 0).
# Since we root the tree at some node, the parent edge is considered outside the subtree,
# so the node's degree in the subtree is just the number of children included.
# But the subtree must be connected, so if the node is included, it must be connected to its parent
# (except for the root, which has no parent).
# So the degree of the node in the subtree is number of children included + (1 if parent edge included).
# For the root, parent edge is not included, so degree = number of children included.
# For other nodes, parent edge is included, so degree = number of children included + 1.

# We want degree to be 1 or 4.
# So for root: degree = number of children included ∈ {1,4}
# For other nodes: degree = number of children included + 1 ∈ {1,4} => number of children included ∈ {0,3}

# So for root:
#   number of children included = 1 or 4
# For other nodes:
#   number of children included = 0 or 3

# We want to maximize the size of the subtree.

# We do a DFS from node 1 (arbitrary root).
# For each node, we compute dp[node][is_root] = maximum subtree size including node,
# with the node as root or not (is_root = True/False).
# Actually, we only need dp[node][0] and dp[node][1]:
# dp[node][1]: node is root of subtree (no parent edge)
# dp[node][0]: node is not root (parent edge included)

# For dp[node][1]:
#   number of children included must be 1 or 4
# For dp[node][0]:
#   number of children included must be 0 or 3

# For each child, we have dp[child][0] (child included, child not root) because child's parent edge is included.
# We want to select a subset of children to maximize sum of dp[child][0] + 1 (for node itself),
# with the number of children included in the allowed set.

# If no valid subset, dp[node][x] = -inf

# After computing dp for root, answer = dp[root][1] if dp[root][1] >= 5 (since at least one vertex with degree 4,
# so subtree size >= 5 because degree 4 node has at least 5 vertices: itself + 4 children),
# else -1.

# Implementation details:
# For each node:
#   gather dp[child][0] for all children
#   try subsets with size in allowed set (1 or 4 for root, 0 or 3 for non-root)
#   pick the subset with max sum

# Since max children can be large, we cannot try all subsets.
# But allowed sizes are small (0,1,3,4).
# So we can sort dp[child][0] descending and pick top k children for k in allowed sizes.

# Note:
# - dp[child][0] can be -inf if no valid subtree including child as non-root.
# - We only pick children with dp[child][0] > -inf.

# Let's implement.

INF = 10**15

dp = [[-INF,-INF] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(u):
    visited[u] = True
    children_dp = []
    for v in edges[u]:
        if not visited[v]:
            dfs(v)
            children_dp.append(dp[v][0])
    # For dp[u][1] (u is root): number of children included in {1,4}
    # For dp[u][0] (u not root): number of children included in {0,3}

    # Sort children dp descending
    children_dp.sort(reverse=True)

    # Helper to get sum of top k children if possible
    def sum_top_k(k):
        if k > len(children_dp):
            return -INF
        # all dp must be > -INF
        for i in range(k):
            if children_dp[i] == -INF:
                return -INF
        return sum(children_dp[:k])

    # dp[u][1]
    candidates = []
    for k in [1,4]:
        s = sum_top_k(k)
        if s != -INF:
            candidates.append(s + 1)
    dp[u][1] = max(candidates) if candidates else -INF

    # dp[u][0]
    candidates = []
    for k in [0,3]:
        s = sum_top_k(k)
        if s != -INF:
            candidates.append(s + 1)
    dp[u][0] = max(candidates) if candidates else -INF

dfs(1)

# We want dp[1][1] >= 5 (since at least one vertex with degree 4, subtree size >= 5)
ans = dp[1][1]
print(ans if ans >= 5 else -1)