def count_good_trees(N, M, permutations):
    MOD = 998244353

    # Create a list to store the positions of each number in each permutation
    pos = [[0] * (N + 1) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            pos[i][permutations[i][j]] = j

    # Function to check if a tree is good for all permutations
    def is_good_tree(edges):
        for u, v in edges:
            for i in range(M):
                if (pos[i][u] > pos[i][v] and pos[i][u] - pos[i][v] < N // 2) or \
                   (pos[i][v] > pos[i][u] and pos[i][v] - pos[i][u] < N // 2):
                    return False
        return True

    # Generate all trees using a DFS approach
    def dfs(current, parent):
        if current == N:
            # Check if the current tree is good
            if is_good_tree(edges):
                return 1
            return 0

        count = 0
        for next_node in range(1, N + 1):
            if next_node != parent:
                edges.append((current + 1, next_node))
                count += dfs(current + 1, next_node)
                count %= MOD
                edges.pop()
        return count

    edges = []
    return dfs(0, -1)

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
permutations = [list(map(int, line.split())) for line in data[1:M + 1]]

# Calculate and print the result
result = count_good_trees(N, M, permutations)
print(result)