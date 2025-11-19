N, M = map(int, input().split())

edges_seen = set()
remove_count = 0

for _ in range(M):
    u, v = map(int, input().split())
    
    # Check for self-loop
    if u == v:
        remove_count += 1
        continue
    
    # Normalize edge representation (smaller vertex first)
    edge = (min(u, v), max(u, v))
    
    # Check if this edge already exists
    if edge in edges_seen:
        remove_count += 1
    else:
        edges_seen.add(edge)

print(remove_count)