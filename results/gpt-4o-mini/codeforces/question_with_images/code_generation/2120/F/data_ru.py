def can_map_graphs(test_cases):
    results = []
    
    for case in test_cases:
        n, k, graphs = case
        conflict_map = {}
        possible = True
        
        for g_index in range(k):
            adj_list = [set() for _ in range(n)]
            for edges in graphs[g_index]:
                u, v = edges
                adj_list[u - 1].add(v - 1)
                adj_list[v - 1].add(u - 1)
                
            color = [-1] * n
            for vertex in range(n):
                if color[vertex] == -1:
                    stack = [vertex]
                    color[vertex] = 0
                    while stack:
                        current = stack.pop()
                        for neighbor in adj_list[current]:
                            if color[neighbor] == -1:
                                color[neighbor] = 1 - color[current]
                                stack.append(neighbor)
                            elif color[neighbor] == color[current]:
                                possible = False
                                break
                if not possible:
                    break
                    
            if not possible:
                break
            
            group_by_color = {0: set(), 1: set()}
            for node in range(n):
                group_by_color[color[node]].add(node)
                
            for group in group_by_color.values():
                if len(group) > 1:
                    for vertex in group:
                        if vertex in conflict_map:
                            if conflict_map[vertex] != g_index:
                                possible = False
                                break
                        else:
                            conflict_map[vertex] = g_index
            
            if not possible:
                break
    
        results.append("Yes" if possible else "No")
        
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    graphs = []
    for _ in range(k):
        m = int(input())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        graphs.append(edges)
    test_cases.append((n, k, graphs))

# Process test cases
results = can_map_graphs(test_cases)

# Print results
for result in results:
    print(result)