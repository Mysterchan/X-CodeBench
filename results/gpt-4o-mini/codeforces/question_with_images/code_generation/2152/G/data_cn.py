import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1

results = []

def bfs_count_paths(n, a, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Finding the number of paths required to cover all monsters
    root = 1
    monster_count = [0] * (n + 1)
    for i in range(1, n + 1):
        monster_count[i] = a[i - 1]
    
    def dfs(node, parent):
        total = monster_count[node]
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            total += dfs(neighbor, node)
        return total
    
    total_monsters = dfs(root, -1)

    return total_monsters

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    edges = []
    
    for __ in range(n - 1):
        u, v = map(int, data[index].split())
        edges.append((u, v))
        index += 1
    
    q = int(data[index])
    index += 1
    queries = []
    
    for __ in range(q):
        v = int(data[index])
        queries.append(v)
        index += 1
    
    total_monsters = bfs_count_paths(n, a, edges)
    results.append(str(total_monsters))
    
    # Tree representation for query updates
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    state = a[:]
    visited = [False] * (n + 1)

    def toggle_state(node, parent):
        state[node - 1] ^= 1
        for neighbor in tree[node]:
            if neighbor != parent:
                toggle_state(neighbor, node)

    for v in queries:
        toggle_state(v, -1)
        # Recompute the number of paths after toggling
        total_monsters = bfs_count_paths(n, state, edges)
        results.append(str(total_monsters))

print("\n".join(results))