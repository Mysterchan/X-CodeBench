def can_construct_superb_graphs(test_cases):
    results = []

    for _ in range(test_cases):
        n, k = map(int, input().split())
        edges_count = [0] * k
        independent_sets = [set() for _ in range(k)]
        
        for idx in range(k):
            m = int(input())
            edges_count[idx] = m
            graph_edges = []
            for __ in range(m):
                u, v = map(int, input().split())
                # Store edges for each graph
                graph_edges.append((u, v))
            
            # Store independent sets found in the graph for verification later.
            graph_nodes = set(range(1, n + 1))  # Assuming vertices are numbered from 1 to n
            all_edges = set()
            for u, v in graph_edges:
                all_edges.add(u)
                all_edges.add(v)
            independent_sets[idx] = graph_nodes - all_edges  # nodes not in any edge
        
        # Now check if there's overlap among independent vertex sets
        independent_count = {}
        
        for i in range(k):
            for node in independent_sets[i]:
                if node in independent_count:
                    independent_count[node] += 1
                else:
                    independent_count[node] = 1
        
        # Check if any node appears in more than one independent set
        valid = all(count <= 1 for count in independent_count.values())
        
        results.append("Yes" if valid else "No")

    return results

# Read the number of test cases
t = int(input())
results = can_construct_superb_graphs(t)
for result in results:
    print(result)