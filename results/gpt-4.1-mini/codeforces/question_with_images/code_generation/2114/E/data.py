import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    g = [[] for __ in range(n)]
    for __ in range(n-1):
        v,u = map(int, input().split())
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)

    # We want to find for each vertex i:
    # max over k >= 0 of sum_{j=0}^k (-1)^j * a_{p^j(i)}
    # where p^j(i) is the j-th ancestor of i (0-th ancestor is i itself)
    #
    # Let's define dp[i][0] = max alternating sum starting at i with sign +
    # dp[i][1] = max alternating sum starting at i with sign -
    #
    # The path is vertical (up to root), so we can do a DFS from root to leaves,
    # but since the path is from i up to root, we need to process from root down,
    # passing dp values down.
    #
    # Actually, we can do a BFS or DFS from root:
    # For root (vertex 0):
    # dp[0][0] = a[0]
    # dp[0][1] = -a[0]
    #
    # For child c of node v:
    # dp[c][0] = max(a[c], a[c] - dp[v][0]) because:
    #   starting at c with + sign:
    #   - path length 1: a[c]
    #   - path length >1: a[c] - (max alternating sum starting at v with + sign)
    #     but since signs alternate, the parent's dp with + sign corresponds to the next term with - sign at c
    #
    # Wait, we need to be careful with signs:
    #
    # Let's define dp[i] = max alternating sum starting at i with sign +
    #
    # The alternating sum starting at i is:
    # a[i] - (max alternating sum starting at parent with sign +)
    #
    # So dp[i] = max(a[i], a[i] - dp[parent])
    #
    # For root, dp[root] = a[root]
    #
    # So we can do a DFS from root:
    # dp[root] = a[root]
    # for each child c of v:
    # dp[c] = max(a[c], a[c] - dp[v])
    #
    # This matches the example:
    # For vertex 4 in example:
    # dp[1] = a[1] = 4
    # dp[2] = max(a[2], a[2] - dp[1]) = max(5, 5 - 4) = 5
    # dp[3] = max(a[3], a[3] - dp[2]) = max(2, 2 - 5) = 2
    # dp[4] = max(a[4], a[4] - dp[3]) = max(6, 6 - 2) = 6
    # But the answer for vertex 4 is 9, so this is not enough.
    #
    # So the above is not sufficient.
    #
    # Let's try to define two dp arrays:
    # dp[i][0] = max alternating sum starting at i with sign +
    # dp[i][1] = max alternating sum starting at i with sign -
    #
    # For root:
    # dp[root][0] = a[root]
    # dp[root][1] = -a[root]
    #
    # For child c of v:
    # dp[c][0] = max(a[c], a[c] + dp[v][1])
    # dp[c][1] = max(-a[c], -a[c] + dp[v][0])
    #
    # Because:
    # starting at c with + sign:
    # - path length 1: a[c]
    # - path length >1: a[c] - (max alternating sum starting at parent with sign +)
    #   but since signs alternate, the parent's dp with sign - is used here
    #
    # Similarly for dp[c][1]
    #
    # Let's test on example:
    # root = 0, a[0] = 4
    # dp[0][0] = 4
    # dp[0][1] = -4
    #
    # For vertex 1 (index 1), a[1] = 5, parent = 0
    # dp[1][0] = max(5, 5 + dp[0][1]) = max(5, 5 - 4) = 5
    # dp[1][1] = max(-5, -5 + dp[0][0]) = max(-5, -5 + 4) = -1
    #
    # For vertex 2 (index 2), a[2] = 2, parent = 1
    # dp[2][0] = max(2, 2 + dp[1][1]) = max(2, 2 -1) = 2
    # dp[2][1] = max(-2, -2 + dp[1][0]) = max(-2, -2 + 5) = 3
    #
    # For vertex 3 (index 3), a[3] = 6, parent = 2
    # dp[3][0] = max(6, 6 + dp[2][1]) = max(6, 6 + 3) = 9
    # dp[3][1] = max(-6, -6 + dp[2][0]) = max(-6, -6 + 2) = -4
    #
    # For vertex 4 (index 4), a[4] = 7, parent = 0
    # dp[4][0] = max(7, 7 + dp[0][1]) = max(7, 7 - 4) = 7
    # dp[4][1] = max(-7, -7 + dp[0][0]) = max(-7, -7 + 4) = -3
    #
    # The answers are dp[i][0]:
    # 0:4, 1:5, 2:2, 3:9, 4:7 which matches sample output.
    #
    # So the plan:
    # - Build tree
    # - DFS from root (0)
    # - For each child c of v:
    #   dp[c][0] = max(a[c], a[c] + dp[v][1])
    #   dp[c][1] = max(-a[c], -a[c] + dp[v][0])
    #
    # Output dp[i][0] for all i.
    #
    # Complexity: O(n) per test, total sum n <= 2*10^5, efficient enough.

    dp = [[0,0] for __ in range(n)]
    parent = [-1]*n
    parent[0] = -1

    # Build adjacency list and find parents with BFS
    from collections import deque
    q = deque([0])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for w in g[v]:
            if w == parent[v]:
                continue
            if parent[w] == -1 and w != 0:
                parent[w] = v
                q.append(w)

    dp[0][0] = a[0]
    dp[0][1] = -a[0]

    for v in order[1:]:
        p = parent[v]
        dp[v][0] = max(a[v], a[v] + dp[p][1])
        dp[v][1] = max(-a[v], -a[v] + dp[p][0])

    print(*[dp[i][0] for i in range(n)])