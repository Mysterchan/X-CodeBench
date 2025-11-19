def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    # Read N and M
    N, M = map(int, data[0].split())
    
    # Read edges
    edges = []
    graph = defaultdict(set)
    for i in range(1, M + 1):
        u, v = map(int, data[i].split())
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    
    # Read Q
    Q = int(data[M + 1])
    
    # Read operations
    operations = list(map(int, data[M + 2].split()))
    
    # Initialize pieces positions
    pieces = list(range(1, N + 1))
    
    # To keep track of the number of edges
    edge_count = M
    results = []
    
    for op in operations:
        u, v = edges[op - 1]
        pu, pv = pieces[u - 1], pieces[v - 1]
        
        if pu == pv or v not in graph[pu]:
            results.append(edge_count)
            continue
        
        # Contract the edge
        new_vertex = N + 1
        N += 1
        
        # Create a new graph after contraction
        new_graph = defaultdict(set)
        for x in range(1, N):
            if x == pu or x == pv:
                continue
            if x in graph[pu] or x in graph[pv]:
                new_graph[new_vertex].add(x)
                new_graph[x].add(new_vertex)
        
        # Add edges from pu and pv
        for neighbor in graph[pu]:
            if neighbor != pv:
                new_graph[new_vertex].add(neighbor)
                new_graph[neighbor].add(new_vertex)
        
        for neighbor in graph[pv]:
            if neighbor != pu:
                new_graph[new_vertex].add(neighbor)
                new_graph[neighbor].add(new_vertex)
        
        # Remove old vertices and edges
        del graph[pu]
        del graph[pv]
        
        # Update the graph
        graph[new_vertex] = new_graph[new_vertex]
        for neighbor in new_graph[new_vertex]:
            graph[neighbor].add(new_vertex)
        
        # Remove self-loops and count edges
        edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2
        
        # Update pieces
        for i in range(1, N + 1):
            if pieces[i - 1] == pu or pieces[i - 1] == pv:
                pieces[i - 1] = new_vertex
        
        results.append(edge_count)
    
    # Print results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()