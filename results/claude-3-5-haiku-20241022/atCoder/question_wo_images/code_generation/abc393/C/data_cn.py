def solve():
    N, M = map(int, input().split())
    
    if M == 0:
        print(0)
        return
    
    edges = set()
    removed = 0
    
    for _ in range(M):
        u, v = map(int, input().split())
        
        # Check if it's a self-loop
        if u == v:
            removed += 1
            continue
        
        # Normalize edge representation (smaller vertex first)
        if u > v:
            u, v = v, u
        
        # Check if it's a duplicate edge
        if (u, v) in edges:
            removed += 1
        else:
            edges.add((u, v))
    
    print(removed)

solve()