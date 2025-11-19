def can_form_graphs(test_cases):
    results = []
    for n, k, graphs in test_cases:
        independent_sets = [set() for _ in range(n + 1)]  # To track the independent set members

        for g in graphs:
            edges = g['edges']
            for u, v in edges:
                independent_sets[u].add(v)
                independent_sets[v].add(u)

        # Check if each vertex either belongs to an independent set or forms a clique
        possible = True
        visited = [False] * (n + 1)

        for i in range(1, n + 1):
            if not visited[i]:
                stack = [i]
                clique = set()
                independent = True
                
                while stack:
                    node = stack.pop()
                    if visited[node]:
                        continue
                    visited[node] = True

                    if node in independent_sets:
                        independent = False
                        clique.add(node)
                    else:
                        independent = True

                    for neighbor in independent_sets[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)

                if independent and len(clique) > 1:
                    possible = False
                    break
        
        results.append("Yes" if possible else "No")

    return results


# Input reading part
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    graphs = []
    for _ in range(k):
        m = int(input())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        graphs.append({'edges': edges})
    test_cases.append((n, k, graphs))

# Process the test cases
results = can_form_graphs(test_cases)

# Output results
for result in results:
    print(result)