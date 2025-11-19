def is_possible_funny_graph(t, test_cases):
    results = []
    
    for case in test_cases:
        n, k, graphs = case
        degrees = [0] * (n + 1)

        # Count the degrees of each node for all graphs
        for graph in graphs:
            m, edges = graph
            for u, v in edges:
                degrees[u] += 1
                degrees[v] += 1
        
        # Analyze the degrees to find any conflicts
        degree_set = set()
        for i in range(1, n + 1):
            if degrees[i] > 0:
                if degrees[i] in degree_set:
                    results.append("No")
                    break
                degree_set.add(degrees[i])
        else:
            results.append("Yes")
    
    return results

# Input handling
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
current_line = 1
test_cases = []

for _ in range(t):
    n, k = map(int, data[current_line].split())
    current_line += 1
    graphs = []
    
    for __ in range(k):
        m = int(data[current_line])
        current_line += 1
        edges = []
        for ___ in range(m):
            u, v = map(int, data[current_line].split())
            edges.append((u, v))
            current_line += 1
        graphs.append((m, edges))
    
    test_cases.append((n, k, graphs))

results = is_possible_funny_graph(t, test_cases)

# Output results
for result in results:
    print(result)