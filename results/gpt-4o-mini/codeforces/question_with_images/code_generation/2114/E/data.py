def calculate_threat_values(t, test_cases):
    results = []

    for case in test_cases:
        n, a, edges = case
        from collections import defaultdict
        
        # Create an adjacency list for the tree
        tree = defaultdict(list)
        for v, u in edges:
            tree[v].append(u)
            tree[u].append(v)

        # To store threat values
        threat_values = [0] * n
        visited = [False] * (n + 1)
        
        def dfs(node, parent, level):
            if level % 2 == 0:  # even level (including root)
                threat_values[node - 1] = a[node - 1]
            else:  # odd level
                threat_values[node - 1] = -a[node - 1]

            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node, level + 1)
        
        # DFS to calculate the initial threats starting from the root (1)
        dfs(1, -1, 0)

        # Compute the max alternating sum from the calculated threats
        max_threats = [0] * n
        max_threats[0] = threat_values[0]
        
        for i in range(1, n):
            max_threats[i] = max(max_threats[i - 1] + (threat_values[i] if (i % 2 == 0) else -threat_values[i]), threat_values[i])

        results.append(max_threats)

    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    edges = []
    for j in range(n - 1):
        v, u = map(int, data[index + 2 + j].split())
        edges.append((v, u))
    test_cases.append((n, a, edges))
    index += n + 1

# Calculate results
results = calculate_threat_values(t, test_cases)

# Print results
for result in results:
    print(" ".join(map(str, result)))