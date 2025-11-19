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

    # dp[i][0]: 頂点iから始まる垂直パスの最大交互和で、iの符号が+のときの最大値
    # dp[i][1]: 頂点iから始まる垂直パスの最大交互和で、iの符号が-のときの最大値
    # ここで、iの符号が+のときは a[i] - dp[child][1]
    # iの符号が-のときは -a[i] + dp[child][0]
    # ただし、子がいなければ dp[i][0] = a[i], dp[i][1] = -a[i]

    # 木は根1(0)からの親子関係を決める
    parent = [-1]*n
    from collections import deque
    q = deque([0])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nx in g[v]:
            if nx == parent[v]:
                continue
            if parent[nx] == -1 and nx != 0:
                parent[nx] = v
                q.append(nx)

    dp = [[0,0] for __ in range(n)]
    # 葉から逆順に計算
    for v in reversed(order):
        # dp[v][0] = a[v] + max(0, -dp[child][1])
        # dp[v][1] = -a[v] + max(0, dp[child][0])
        # ただし複数子がいる場合は最大を取る
        max0 = 0
        max1 = 0
        for c in g[v]:
            if c == parent[v]:
                continue
            # 子のdp[c][0], dp[c][1]は計算済み
            max0 = max(max0, -dp[c][1])
            max1 = max(max1, dp[c][0])
        dp[v][0] = a[v] + max0
        dp[v][1] = -a[v] + max1

    # 各頂点の脅威値は dp[i][0]
    print(*[dp[i][0] for i in range(n)])