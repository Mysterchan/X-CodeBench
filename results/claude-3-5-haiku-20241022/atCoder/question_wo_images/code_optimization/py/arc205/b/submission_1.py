n, m = map(int, input().split())

if m == 0:
    print(n * (n - 1) // 2)
else:
    edges = set()
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.add((u, v))
    
    # The key insight: we can reduce the edge set using XOR properties
    # When we have edges forming patterns, we can simplify
    while len(edges) > 1:
        e1 = edges.pop()
        e2 = edges.pop()
        
        a, b = e1
        c, d = e2
        
        # Find common vertex and create new edge
        vertices = [a, b, c, d]
        
        if b == c:
            new_edge = (a, d) if a < d else (d, a)
        elif a == c:
            new_edge = (b, d) if b < d else (d, b)
        elif a == d:
            new_edge = (b, c) if b < c else (c, b)
        elif b == d:
            new_edge = (a, c) if a < c else (c, a)
        else:
            # No common vertex, arbitrary choice
            new_edge = (a, c) if a < c else (c, a)
        
        if new_edge in edges:
            edges.remove(new_edge)
        else:
            edges.add(new_edge)
    
    total_edges = n * (n - 1) // 2
    print(total_edges - len(edges))