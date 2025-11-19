import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # dp[u][0]: max alternating sum starting at u with sign +a[u]
    # dp[u][1]: max alternating sum starting at u with sign -a[u]
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(u, par):
        visited[u] = True
        dp[u][0] = a[u]
        dp[u][1] = -a[u]
        for v in adj[u]:
            if v == par:
                continue
            dfs(v, u)
            # If we start at u with +a[u], next is -a[v], so add dp[v][1]
            dp[u][0] = max(dp[u][0], a[u] + dp[v][1])
            # If we start at u with -a[u], next is +a[v], so add dp[v][0]
            dp[u][1] = max(dp[u][1], -a[u] + dp[v][0])

    dfs(1, 0)

    # The threat for each vertex is dp[u][0] because the path starts at u with +a[u]
    # But the problem states the path starts at vertex i, so we need to compute dp for all nodes as roots.
    # The above dfs only computes dp from root 1 downwards.
    # We need to reroot the tree to compute dp for all nodes efficiently.

    # To do this, we use a rerooting technique:
    # We'll do a second dfs to propagate dp values from parent to children.

    # For each node u, we want to know dp[u][0] and dp[u][1] considering the whole tree rooted at u.

    # We'll store:
    # up_dp[u][0], up_dp[u][1]: dp values coming from the parent side (excluding subtree u)

    up_dp = [[float('-inf'), float('-inf')] for _ in range(n + 1)]

    def dfs_up(u, par):
        # Precompute prefix and suffix max arrays for children to efficiently compute up_dp for each child
        children = [v for v in adj[u] if v != par]
        prefix0 = [float('-inf')] * (len(children) + 1)
        prefix1 = [float('-inf')] * (len(children) + 1)
        suffix0 = [float('-inf')] * (len(children) + 1)
        suffix1 = [float('-inf')] * (len(children) + 1)

        prefix0[0] = float('-inf')
        prefix1[0] = float('-inf')
        for i, v in enumerate(children, 1):
            prefix0[i] = max(prefix0[i-1], dp[v][1])
            prefix1[i] = max(prefix1[i-1], dp[v][0])

        suffix0[len(children)] = float('-inf')
        suffix1[len(children)] = float('-inf')
        for i in range(len(children)-1, -1, -1):
            v = children[i]
            suffix0[i] = max(suffix0[i+1], dp[v][1])
            suffix1[i] = max(suffix1[i+1], dp[v][0])

        for i, v in enumerate(children):
            # For child v, compute up_dp[v] using up_dp[u] and dp of siblings
            # dp[u][0] = max(a[u], a[u] + max of dp[v][1] for children)
            # So for up_dp[v][0], we consider:
            # max of:
            #   up_dp[u][1] + a[u] (parent side)
            #   a[u] + max dp[w][1] for siblings w != v
            # Similarly for up_dp[v][1]

            # max dp[w][1] for siblings excluding v
            max_sib_1 = max(prefix0[i], suffix0[i+1])
            # max dp[w][0] for siblings excluding v
            max_sib_0 = max(prefix1[i], suffix1[i+1])

            # up_dp[v][0]: starting at v with +a[v]
            # The parent side contributes with sign flipped:
            # from u's up_dp[1] + a[u] (since u's dp[0] = a[u] + max child dp[1])
            candidate0 = float('-inf')
            if up_dp[u][1] != float('-inf'):
                candidate0 = max(candidate0, a[v] + up_dp[u][1])
            if max_sib_1 != float('-inf'):
                candidate0 = max(candidate0, a[v] + a[u] + max_sib_1)

            # up_dp[v][1]: starting at v with -a[v]
            candidate1 = float('-inf')
            if up_dp[u][0] != float('-inf'):
                candidate1 = max(candidate1, -a[v] + up_dp[u][0])
            if max_sib_0 != float('-inf'):
                candidate1 = max(candidate1, -a[v] - a[u] + max_sib_0)

            up_dp[v][0] = candidate0
            up_dp[v][1] = candidate1

            dfs_up(v, u)

    # Initialize up_dp for root
    up_dp[1][0] = float('-inf')
    up_dp[1][1] = float('-inf')
    dfs_up(1, 0)

    # Now compute final answer for each node:
    # max threat = max(dp[u][0], up_dp[u][0])
    # Because dp[u][0] is max starting at u going down,
    # up_dp[u][0] is max starting at u going up (excluding subtree u)
    # Actually, up_dp[u][0] is the max alternating sum starting at u considering the rest of the tree excluding subtree u.

    # But we must consider the path starting at u going up to root and down other branches.

    # The threat value for each vertex u is max(dp[u][0], up_dp[u][0]) because the path starts at u.

    res = [0] * (n + 1)
    for u in range(1, n + 1):
        res[u] = max(dp[u][0], up_dp[u][0])
        # If both are -inf (should not happen), fallback to a[u]
        if res[u] == float('-inf'):
            res[u] = a[u]

    print(' '.join(map(str, res[1:])))

t = int(input())
for _ in range(t):
    solve()