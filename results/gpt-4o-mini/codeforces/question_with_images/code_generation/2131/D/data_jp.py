def min_operations_to_reduce_diameter(test_cases):
    from sys import stdin, stdout
    import collections
    
    input = stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        if n == 2:
            results.append(0)
            index += 2  # skip the edges
            continue
        
        # Build adjacency list for the tree
        graph = collections.defaultdict(list)
        for __ in range(n - 1):
            u = int(data[index])
            v = int(data[index + 1])
            graph[u].append(v)
            graph[v].append(u)
            index += 2
        
        # Function to perform BFS and return the farthest node and its distance
        def bfs(start):
            visited = [False] * (n + 1)
            queue = collections.deque([start])
            visited[start] = True
            farthest_node = start
            distance = 0
            
            while queue:
                current_size = len(queue)
                for _ in range(current_size):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            farthest_node = neighbor
                distance += 1
            
            return farthest_node, distance - 1
        
        # First BFS to find one endpoint of the diameter
        arbitrary_node = 1
        farthest_node_1, _ = bfs(arbitrary_node)
        # Second BFS from that farthest node to find the diameter
        farthest_node_2, diameter_length = bfs(farthest_node_1)
        
        # The required num of operations is the number of edges in the longest path minus 2
        # as we can collapse 2 edges for each operation
        min_operations = max(0, (diameter_length - 1) // 2)
        results.append(min_operations)
    
    stdout.write("\n".join(map(str, results)) + "\n")

# Read input and execute the function for multiple test cases
min_operations_to_reduce_diameter()