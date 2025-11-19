N, M = map(int, input().split())
seen_edges = set()
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    
    if u == v:
        ans += 1
    else:
        edge = (min(u, v), max(u, v))
        if edge in seen_edges:
            ans += 1
        else:
            seen_edges.add(edge)

print(ans)