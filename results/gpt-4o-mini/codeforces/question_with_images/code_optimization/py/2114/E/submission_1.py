import sys
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # Create adjacency list for the tree
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # Initialize result array and visited set
    result = [0] * n
    visited = [False] * n

    def dfs(node, current_sum, depth):
        visited[node] = True
        current_sum += a[node] if depth % 2 == 0 else -a[node]
        result[node] = current_sum

        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, current_sum, depth + 1)

    # Start DFS from the root node (0 in 0-indexed)
    dfs(0, 0, 0)

    # Output the results
    sys.stdout.write(' '.join(map(str, result)) + '\n')

t = int(input())
for _ in range(t):
    solve()