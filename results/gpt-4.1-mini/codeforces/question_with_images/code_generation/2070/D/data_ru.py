import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    # Build tree adjacency list
    g = [[] for __ in range(n+1)]
    for i, par in enumerate(p, start=2):
        g[par].append(i)

    # We want to count the number of valid sequences.
    # The problem states:
    # - The chip starts at root (1).
    # - Moves only from depth d to depth d+1.
    # - From root, can move to any child.
    # - From non-root v, can move to u with d_u = d_v+1, but u must NOT be adjacent to v.
    #
    # The sequences are sequences of vertices visited in order, starting at 1,
    # such that each move is valid.
    #
    # We want to count all such sequences (including the sequence [1]).
    #
    # Key observations:
    # - The tree is rooted at 1.
    # - Depths are well-defined.
    # - Moves go strictly down one level.
    #
    # Let's analyze the moves from a node v at depth d:
    # - If v=1 (root), can move to any child (depth 1).
    # - If v != 1, can move to any node u at depth d+1 that is NOT adjacent to v.
    #
    # Since the tree is rooted, edges only connect nodes at depth d and d+1.
    # So adjacency between nodes at depth d and d+1 is given by the tree edges.
    #
    # So from a non-root node v at depth d, the forbidden next nodes are exactly the children of v.
    # Because adjacency between v and nodes at depth d+1 is only via v's children.
    #
    # So from v != 1, the allowed next nodes at depth d+1 are all nodes at depth d+1 except v's children.
    #
    # From root, allowed next nodes are all children of root.
    #
    # We want to count sequences starting at 1, where each next node is at depth+1 and allowed by above rules.
    #
    # Let's define:
    # - For each depth d, let S_d be the set of nodes at depth d.
    # - Let size_d = |S_d|
    #
    # For each node v at depth d, define:
    # - children_count[v] = number of children of v (nodes at depth d+1 adjacent to v)
    #
    # From v at depth d:
    # - If v=1: next nodes are children of root => count = children_count[1]
    # - Else: next nodes are all nodes at depth d+1 except children of v
    #   => count = size_{d+1} - children_count[v]
    #
    # The sequences correspond to paths starting at 1, where at each step we choose a next node from allowed set.
    #
    # We want to count the number of sequences (including the empty sequence [1]) that can be formed.
    #
    # Let's define dp[v] = number of sequences starting at node v.
    #
    # Then:
    # dp[v] = 1 + sum over allowed next nodes u of dp[u]
    #
    # But the allowed next nodes depend on v:
    # - If v=1: allowed next nodes = children of root
    # - Else: allowed next nodes = all nodes at depth d+1 except children of v
    #
    # This is complicated to do per node.
    #
    # Let's try to compute dp by depth:
    #
    # Let dp_d[v] = number of sequences starting at node v at depth d.
    #
    # For the deepest depth (max_depth), dp_d[v] = 1 (only the sequence [v])
    #
    # For depth d < max_depth:
    # For v at depth d:
    # - If v=1:
    #   dp_1[v] = 1 + sum_{u in children of root} dp_{d+1}[u]
    # - Else:
    #   dp_d[v] = 1 + sum_{u in S_{d+1} \ children_of_v} dp_{d+1}[u]
    #
    # Let's precompute:
    # - For each depth d, sum_dp_d = sum of dp_d[v] over all v in S_d
    #
    # Then for v != 1:
    # dp_d[v] = 1 + (sum_dp_{d+1} - sum_{children_of_v} dp_{d+1}[child])
    #
    # For v=1:
    # dp_1[1] = 1 + sum_{children_of_1} dp_2[child]
    #
    # We can compute dp bottom-up:
    #
    # Steps:
    # 1) Compute depth of each node.
    # 2) Group nodes by depth.
    # 3) Compute dp for max_depth: dp[v] = 1
    # 4) For d from max_depth-1 down to 1:
    #    - Compute sum_dp_{d+1}
    #    - For each v in S_d:
    #       if v=1:
    #          dp[v] = 1 + sum of dp of children of root
    #       else:
    #          dp[v] = 1 + sum_dp_{d+1} - sum of dp of children of v
    #
    # Finally, answer = dp[1]
    #
    # This counts sequences starting at 1.
    #
    # The problem wants the number of sequences that can be formed starting at 1.
    #
    # The sample matches this approach.
    #
    # Let's implement.

    depth = [0]*(n+1)
    depth[1] = 1
    from collections import deque
    q = deque([1])
    while q:
        v = q.popleft()
        for u in g[v]:
            depth[u] = depth[v] + 1
            q.append(u)

    max_depth = max(depth)

    nodes_by_depth = [[] for __ in range(max_depth+1)]
    for v in range(1, n+1):
        nodes_by_depth[depth[v]].append(v)

    dp = [0]*(n+1)

    # For max_depth, dp[v] = 1
    for v in nodes_by_depth[max_depth]:
        dp[v] = 1

    # Precompute children sets for quick sum of dp of children
    # children[v] = list of children of v
    children = g

    for d in range(max_depth-1, 0, -1):
        sum_dp_next = 0
        for v in nodes_by_depth[d+1]:
            sum_dp_next = (sum_dp_next + dp[v]) % MOD

        # For quick sum of dp of children of v
        # We'll sum dp[c] for c in children[v]
        # children[v] are at depth d+1

        # For v=1:
        # dp[1] = 1 + sum dp of children of 1
        # For others:
        # dp[v] = 1 + sum_dp_next - sum dp of children[v]

        for v in nodes_by_depth[d]:
            if v == 1:
                s = 0
                for c in children[v]:
                    s = (s + dp[c]) % MOD
                dp[v] = (1 + s) % MOD
            else:
                s = 0
                for c in children[v]:
                    s = (s + dp[c]) % MOD
                dp[v] = (1 + sum_dp_next - s) % MOD

    print(dp[1] % MOD)