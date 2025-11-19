def calculate_threats(tree_input):
    n = tree_input[0]
    a = tree_input[1]
    edges = tree_input[2:]

    from collections import defaultdict, deque

    # Build the tree
    tree = defaultdict(list)
    for v, u in edges:
        tree[v].append(u)
        tree[u].append(v)

    threats = [0] * n
    max_threats = [0] * n

    # Function to perform DFS to calculate threats
    def dfs(node, parent, sign):
        current_threat = sign * a[node]
        max_threat = current_threat
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_threat = dfs(neighbor, node, -sign)
            max_threat = max(max_threat, current_threat + child_threat)

        threats[node] = max_threat
        return max_threat

    # Start DFS from the root (1)
    dfs(0, -1, 1)

    return threats


import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
result = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    edges = []
    for _ in range(n - 1):
        v, u = map(int, data[index].split())
        edges.append((v - 1, u - 1))
        index += 1
    threats = calculate_threats([n, a, edges])
    result.append(" ".join(map(str, threats)))

print("\n".join(result))