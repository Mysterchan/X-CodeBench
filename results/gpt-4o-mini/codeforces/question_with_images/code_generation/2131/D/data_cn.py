def min_operations_to_reduce_diameter(test_cases):
    results = []
    
    for edges in test_cases:
        n = len(edges) + 1
        if n <= 2:
            results.append(0)
            continue
        
        # Count the degree of each vertex
        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        # Find the maximum degree to determine the minimum operations
        max_degree = max(degree)
        
        # Minimum operations needed is at least ceil((max_degree - 1) / 2)
        operations = (max_degree - 1) // 2
        results.append(operations)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    edges = []
    for i in range(n - 1):
        u, v = map(int, data[index + 1 + i].split())
        edges.append((u, v))
    test_cases.append(edges)
    index += n

# Computing results
results = min_operations_to_reduce_diameter(test_cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')