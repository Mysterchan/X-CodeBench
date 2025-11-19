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
        
        # Check if the matrix satisfies the tree conditions
        valid = True
        for i in range(N):
            for j in range(N):
                if adj[i][j] == 1:
                    # Check if i is an ancestor of j or j is an ancestor of i
                    is_ancestor = False
                    for k in range(N):
                        if adj[i][k] == 1 and adj[j][k] == 1:
                            is_ancestor = True
                            break
                    if not is_ancestor:
                        valid = False
                        break
            if not valid:
                break
        
        if not valid:
            results.append(0)
            continue
        
        # Count the number of valid trees
        # The number of valid trees is 2^(number of edges) where edges are the connections
        edges = 0
        for i in range(N):
            for j in range(i + 1, N):
                if adj[i][j] == 1:
                    edges += 1
        
        # The number of trees is 2^(edges) % MOD
        result = pow(2, edges, MOD)
        results.append(result)
    
    return results

# Read input
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

# Get results
results = count_trees(T, cases)

# Print results
for result in results:
    print(result)