def solve():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        if n == 2:  # For n=2, diameter is already 1, no operations needed
            results.append(0)
            index += 1  # Skip the edge input
            continue
        
        graph = defaultdict(list)
        
        for __ in range(n - 1):
            u, v = map(int, data[index].split())
            graph[u].append(v)
            graph[v].append(u)
            index += 1
        
        # Function to calculate the farthest node and its distance using BFS
        def bfs(start_node):
            queue = deque([start_node])
            visited = {start_node: 0}
            farthest_node = start_node
            max_distance = 0
            
            while queue:
                node = queue.popleft()
                current_distance = visited[node]
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited[neighbor] = current_distance + 1
                        queue.append(neighbor)
                        if visited[neighbor] > max_distance:
                            max_distance = visited[neighbor]
                            farthest_node = neighbor
            
            return farthest_node, max_distance
        
        # Find the furthest node from an arbitrary starting point (node 1)
        furthest_node_from_start, _ = bfs(1)
        # Find the furthest node from that furthest node (this gives the diameter)
        other_end, diameter = bfs(furthest_node_from_start)
        
        # The minimum number of operations is (diameter + 1) // 2
        results.append((diameter + 1) // 2)
    
    # Output all results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()