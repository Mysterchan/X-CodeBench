def max_candy_edges(n, edges):
    from collections import defaultdict
    
    # Graph adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, parent):
        visited.add(node)
        cycle_edges = []
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue  # Skip the parent node
            if neighbor in visited:
                # Found a cycle
                cycle_edges.append((node, neighbor))
            else:
                cycle_edges.extend(dfs(neighbor, node))
        
        return cycle_edges

    visited = set()
    cycle_count = []
    
    for node in range(1, n + 1):
        if node not in visited:
            cycle_edges = dfs(node, -1)
            cycle_count.extend(cycle_edges)
    
    # Each cycle counts as 1 for maximum edges
    return len(cycle_count) // 2

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        edges = []
        
        for __ in range(m):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        
        result = max_candy_edges(n, edges)
        results.append(result)
    
    print("\n".join(map(str, results)))

solve()