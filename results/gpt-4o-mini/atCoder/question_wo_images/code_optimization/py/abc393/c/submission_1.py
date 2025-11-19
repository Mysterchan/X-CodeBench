N, M = map(int, input().split())
edges = set()
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        ans += 1
    else:
        edge = (min(u, v), max(u, v))
        if edge in edges:
            ans += 1
        else:
            edges.add(edge)

print(ans)