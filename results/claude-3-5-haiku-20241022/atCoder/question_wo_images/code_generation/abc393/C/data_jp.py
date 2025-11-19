N, M = map(int, input().split())

edges = set()
remove_count = 0

for _ in range(M):
    u, v = map(int, input().split())
    
    # 自己ループのチェック
    if u == v:
        remove_count += 1
        continue
    
    # 多重辺のチェック（正規化して格納）
    edge = (min(u, v), max(u, v))
    if edge in edges:
        remove_count += 1
    else:
        edges.add(edge)

print(remove_count)