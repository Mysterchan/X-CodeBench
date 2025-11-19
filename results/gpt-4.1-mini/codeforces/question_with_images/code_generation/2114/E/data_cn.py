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

    # 威脅值 = 從該節點開始往根方向的最大交替和
    # 交替和定義為 a_i - a_p + a_pp - ...
    # 根節點(1)威脅值 = a_1
    # 對於子節點 v，威脅值 = max(a_v, a_v - 威脅值(parent))
    # 因為交替和是從該節點開始往上走，交替符號交替，且父節點威脅值已包含父節點往上的最大交替和
    # 故可用DFS從根往下計算威脅值

    res = [0]*n
    res[0] = a[0]

    def dfs(u, p):
        for w in g[u]:
            if w == p:
                continue
            # 子節點威脅值 = max(a[w], a[w] - res[u])
            res[w] = max(a[w], a[w] - res[u])
            dfs(w, u)

    dfs(0, -1)
    print(*res)