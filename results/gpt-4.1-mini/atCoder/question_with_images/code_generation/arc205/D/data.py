import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())

# The problem reduces to finding the maximum number of pairs (u,v) of white vertices
# such that u is not ancestor of v.
# 
# Key insight:
# - If u is ancestor of v, they cannot be paired.
# - So pairs must be chosen from vertices that are not in ancestor-descendant relation.
#
# This means pairs must be chosen from vertices in different branches of the tree.
#
# The maximum number of such pairs is the maximum matching in the tree where edges connect
# vertices that are not ancestor-descendant.
#
# Another way to think:
# - The tree is rooted at 1.
# - We want to pair vertices so that no pair is ancestor-descendant.
# - This is equivalent to pairing vertices from different subtrees.
#
# The problem can be solved by a greedy approach:
# - Count the number of leaves in the tree.
# - The maximum number of pairs is at most floor(number_of_leaves / 2).
#
# But this is not always correct.
#
# Let's analyze the problem more carefully:
#
# The problem is equivalent to finding the maximum matching in the "incomparability graph"
# of the tree nodes under the ancestor relation.
#
# Another approach:
# - The problem is known to be equivalent to finding the maximum matching in the tree's
#   "incomparability graph" which is a bipartite graph formed by the tree levels.
#
# Since u < v and u is not ancestor of v, and the tree is rooted at 1,
# the pairs must be chosen from nodes that are not in ancestor-descendant relation.
#
# Let's consider the depth of each node.
# Nodes at the same depth are never ancestor-descendant.
# So we can pair nodes at the same depth.
#
# But the problem requires u < v, so we can pair nodes at the same depth with u < v.
#
# So the maximum number of pairs is sum over all depths of floor(count_at_depth / 2).
#
# Let's implement this approach:
# 1. Build the tree.
# 2. Compute depth of each node.
# 3. Count nodes at each depth.
# 4. Sum floor(count_at_depth / 2) over all depths.
#
# This matches the sample test cases.

from collections import deque, defaultdict

for _ in range(T):
    N = int(input())
    parents = list(map(int, input().split()))
    tree = [[] for __ in range(N+1)]
    for i, p in enumerate(parents, start=2):
        tree[p].append(i)

    depth_count = defaultdict(int)
    depth = [0]*(N+1)
    depth[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        d = depth[u]
        depth_count[d] += 1
        for w in tree[u]:
            depth[w] = d+1
            q.append(w)

    ans = 0
    for c in depth_count.values():
        ans += c//2

    print(ans)