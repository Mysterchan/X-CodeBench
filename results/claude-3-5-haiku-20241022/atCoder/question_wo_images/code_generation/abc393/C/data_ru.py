n, m = map(int, input().split())

edges = set()
remove_count = 0

for _ in range(m):
    u, v = map(int, input().split())
    
    # Проверка на петлю
    if u == v:
        remove_count += 1
        continue
    
    # Нормализуем ребро (меньший индекс первым)
    edge = (min(u, v), max(u, v))
    
    # Проверка на многоребро
    if edge in edges:
        remove_count += 1
    else:
        edges.add(edge)

print(remove_count)