def min_operations_to_reduce_diameter(t, test_cases):
    results = []
    for case in test_cases:
        n, edges = case
        if n == 2:
            # There are only two vertices, the diameter is already minimized (1).
            results.append(0)
            continue

        # Degree counts to find maximum degree
        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        # Find the maximum degree in the tree
        max_degree = max(degree)

        # The minimum number of operations to reduce the diameter
        # is max degree - 1
        results.append(max_degree - 1)

    return results

# Input reading and function execution
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
    test_cases.append((n, edges))
    index += n

results = min_operations_to_reduce_diameter(t, test_cases)
print('\n'.join(map(str, results)))