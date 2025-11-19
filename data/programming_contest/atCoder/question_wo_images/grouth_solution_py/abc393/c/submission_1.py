n, m = map(int, input().split())
g = [[] for _ in range(n)]
ans = 0
for _ in range(m):
    u,v = map(int, input().split())
    if u == v:
        ans += 1
        continue
    u -= 1
    v -= 1
    if v in g[u] and u in g[v]:
        ans += 1
        continue
    g[u].append(v)
    g[v].append(u)

print(ans)