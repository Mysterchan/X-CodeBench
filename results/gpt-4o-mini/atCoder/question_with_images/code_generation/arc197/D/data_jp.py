def count_trees(T, cases):
    MOD = 998244353
    results = []
    
    for case in cases:
        N, A = case
        # Create a list to store the adjacency matrix
        adj = [[0] * N for _ in range(N)]
        
        # Fill the adjacency matrix based on the input
        for i in range(N):
            for j in range(N):
                adj[i][j] = A[i][j]
        
        # Check for the conditions
        valid = True
        for i in range(N):
            for j in range(N):
                if adj[i][j] == 1:
                    # Check if i and j are ancestors of each other
                    if not (is_ancestor(adj, i, j) or is_ancestor(adj, j, i)):
                        valid = False
                        break
            if not valid:
                break
        
        if not valid:
            results.append(0)
            continue
        
        # Count the number of valid trees
        count = count_valid_trees(N, adj)
        results.append(count % MOD)
    
    return results

def is_ancestor(adj, u, v):
    # Check if u is an ancestor of v using DFS
    visited = [False] * len(adj)
    stack = [u]
    
    while stack:
        node = stack.pop()
        if node == v:
            return True
        visited[node] = True
        for neighbor in range(len(adj)):
            if adj[node][neighbor] == 1 and not visited[neighbor]:
                stack.append(neighbor)
    
    return False

def count_valid_trees(N, adj):
    # Count the number of valid trees based on the adjacency matrix
    # This is a placeholder for the actual counting logic
    # The actual implementation would depend on the specific tree counting algorithm
    return 1  # Placeholder return value

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    A = []
    for i in range(N):
        A.append(list(map(int, data[index + 1 + i].split())))
    cases.append((N, A))
    index += N + 1

results = count_trees(T, cases)
for result in results:
    print(result)