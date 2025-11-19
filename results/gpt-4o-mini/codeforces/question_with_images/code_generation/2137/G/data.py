def fun_graph_game():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m, q = map(int, data[index].split())
        index += 1
        
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        colors = [0] * (n + 1)  # 0 for blue, 1 for red
        
        for __ in range(m):
            u, v = map(int, data[index].split())
            graph[u].append(v)
            in_degree[v] += 1
            index += 1
            
        query_types = []
        query_nodes = []
        
        for __ in range(q):
            x, u = map(int, data[index].split())
            query_types.append(x)
            query_nodes.append(u)
            index += 1
        
        # Analyze winners
        winner = [False] * (n + 1)  # False means Cry wins
        queue = deque()
        # Start with nodes that have no outgoing edges
        for node in range(1, n + 1):
            if not graph[node]:
                winner[node] = True  # Cry wins if starts here
                queue.append(node)
        
        # Process nodes with topological sorting (which is safe due to DAG)
        while queue:
            current = queue.popleft()
            # If current node is winning for Cry, check its predecessors
            for parent in graph:
                if current in graph[parent]:
                    # If river can force a win from parent through current
                    if winner[current]:  # If River would win from current
                        winner[parent] = False
                    else:
                        # Evaluate if we can mark this parent as a Cry win
                        all_children_winning = True
                        for child in graph[parent]:
                            if winner[child]:  # If child is winning for Cry
                                all_children_winning = False
                                break
                        if all_children_winning and not winner[parent]:
                            winner[parent] = True
                            queue.append(parent)

        # Processing queries
        for i in range(q):
            if query_types[i] == 1:
                u = query_nodes[i]
                colors[u] = 1  # Mark as red
                # Update the winner for affected nodes
                for parent in graph:
                    if u in graph[parent]:
                        if winner[parent] and not winner[u]:
                            winner[parent] = False
            
            elif query_types[i] == 2:
                u = query_nodes[i]
                # Logic check if Cry wins
                results.append("YES" if not winner[u] else "NO")
    
    sys.stdout.write("\n".join(results) + "\n")

# Call the function to execute it for the problem statement
fun_graph_game()