def count_trees(T, cases):
    MOD = 998244353
    results = []
    
    for case in cases:
        N, A = case
        # Create a list to track the connected components
        visited = [False] * N
        components = []
        
        # DFS to find connected components
        def dfs(node, component):
            stack = [node]
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    component.append(u)
                    for v in range(N):
                        if A[u][v] == 1 and not visited[v]:
                            stack.append(v)

        for i in range(N):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(component)

        # Check if each component is a valid tree
        valid = True
        for component in components:
            size = len(component)
            if size == 1:
                continue
            # Check if the component forms a tree
            edges = 0
            for u in component:
                for v in component:
                    if A[u][v] == 1:
                        edges += 1
            edges //= 2  # Each edge is counted twice
            if edges != size - 1:
                valid = False
                break

        if not valid:
            results.append(0)
            continue

        # Calculate the number of trees
        num_trees = 1
        for component in components:
            size = len(component)
            num_trees *= 1  # Each component can be arranged in 1 way as a tree
            num_trees %= MOD

        results.append(num_trees)

    return results

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
print('\n'.join(map(str, results)))