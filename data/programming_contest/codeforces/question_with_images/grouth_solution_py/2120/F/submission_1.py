for _ in range(int(input())):
    n, k = map(int, input().split())
    g, rg = [[] for _ in range(2*n)], [[] for _ in range(2*n)]
    def add(u, v):
        nu, nv = (u+n)%(2*n), (v+n)%(2*n)
        g[nu].append(v); rg[v].append(nu)
        g[nv].append(u); rg[u].append(nv)
    for _ in range(k):
        m = int(input())
        a = [[0]*n for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split()); u -= 1; v -= 1
            a[u][v] = a[v][u] = 1
        B1, M1, B2, M2 = 31, 10*9+7, 37, 10*9+9
        p1 = [pow(B1, i, M1) for i in range(n)]
        p2 = [pow(B2, i, M2) for i in range(n)]
        h = [[0, 0] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j]:
                    h[i][0] = (h[i][0] + p1[j]) % M1
                    h[i][1] = (h[i][1] + p2[j]) % M2
        for u in range(n):
            for v in range(u+1, n):
                hu = [(h[u][0] - p1[v]*a[u][v]) % M1, (h[u][1] - p2[v]*a[u][v]) % M2]
                hv = [(h[v][0] - p1[u]*a[v][u]) % M1, (h[v][1] - p2[u]*a[v][u]) % M2]
                if hu == hv: add(u, v) if a[u][v] else add(u+n, v+n)
    vis, ord = [0]*(2*n), []
    def dfs(u):
        vis[u] = 1
        for v in g[u]:
            if not vis[v]: dfs(v)
        ord.append(u)
    for i in range(2*n):
        if not vis[i]: dfs(i)
    comp, c = [-1]*(2*n), 0
    def rdfs(u):
        comp[u] = c
        for v in rg[u]:
            if comp[v] == -1: rdfs(v)
    for u in reversed(ord):
        if comp[u] == -1: rdfs(u); c += 1
    print("Yes" if all(comp[i] != comp[i+n] for i in range(n)) else "No")
