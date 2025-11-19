def count_good_trees(N, M, permutations):
    MOD = 998244353

    # Create a list to store the positions of each number in each permutation
    pos = [[0] * (N + 1) for _ in range(M)]
    
    for i in range(M):
        for j in range(N):
            pos[i][permutations[i][j]] = j

    # Check if a tree is valid for all permutations
    def is_good_tree(edges):
        for u, v in edges:
            for i in range(M):
                if not (pos[i][u] < pos[i][v] and (pos[i][v] - pos[i][u]) == 1) and \
                       not (pos[i][v] < pos[i][u] and (pos[i][u] - pos[i][v]) == 1):
                    return False
        return True

    # Generate all trees using a DFS approach
    def dfs(current, parent):
        if current == N:
            # Check if the current tree is good for all permutations
            if is_good_tree(edges):
                return 1
            return 0
        
        count = 0
        for next in range(1, N + 1):
            if next != parent:
                edges.append((current + 1, next))
                count += dfs(current + 1, next)
                count %= MOD
                edges.pop()
        
        return count

    edges = []
    total_trees = dfs(0, -1)
    
    return total_trees

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
permutations = [list(map(int, line.split())) for line in data[1:M + 1]]

# Calculate and print the result
result = count_good_trees(N, M, permutations)
print(result)