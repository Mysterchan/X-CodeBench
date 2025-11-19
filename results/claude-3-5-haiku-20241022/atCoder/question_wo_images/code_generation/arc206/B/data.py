def solve():
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    # Find all inversions
    inversions = []
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                inversions.append((i, j))
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for i, j in inversions:
        adj[i].append(j)
        adj[j].append(i)
    
    # Find connected components
    visited = [False] * n
    components = []
    
    def dfs(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)
    
    for i in range(n):
        if not visited[i] and adj[i]:
            component = []
            dfs(i, component)
            components.append(component)
    
    total_cost = 0
    
    # For each component, find minimum cost coloring
    for component in components:
        # Try to find a valid coloring that minimizes cost
        # Use greedy: keep colors that don't conflict
        comp_set = set(component)
        min_cost = float('inf')
        
        # Try different strategies - keep original colors greedily
        current_colors = [c[i] for i in range(n)]
        changed = [False] * n
        
        # Check conflicts and fix them greedily
        cost = 0
        for node in component:
            if changed[node]:
                continue
            
            # Check if current color conflicts with any neighbor
            conflict = False
            for neighbor in adj[node]:
                if not changed[neighbor] and current_colors[node] == current_colors[neighbor]:
                    conflict = True
                    break
            
            if conflict:
                # Need to change this node
                cost += c[node]
                changed[node] = True
                # Assign a color that doesn't conflict
                used = set(current_colors[neighbor] for neighbor in adj[node] if not changed[neighbor])
                for new_color in range(1, n + 1):
                    if new_color not in used:
                        current_colors[node] = new_color
                        break
        
        total_cost += cost
    
    print(total_cost)

solve()