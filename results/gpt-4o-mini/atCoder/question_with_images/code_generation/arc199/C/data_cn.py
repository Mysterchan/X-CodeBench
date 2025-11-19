def count_good_trees(N, M, permutations):
    MOD = 998244353

    # Create a list to store the positions of each number in each permutation
    pos = [[0] * (N + 1) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            pos[i][permutations[i][j]] = j

    # Check if a tree is a good arrangement
    def is_good_tree(edges):
        for u, v in edges:
            if abs(pos[0][u] - pos[0][v]) > 1 and abs(pos[1][u] - pos[1][v]) > 1:
                return False
        return True

    # Generate all trees using Prüfer sequence
    def generate_trees(n):
        if n == 1:
            return [[]]
        trees = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                edges = [(i, j)]
                for k in range(1, n + 1):
                    if k != i and k != j:
                        edges.append((k, i))
                if is_good_tree(edges):
                    trees.append(edges)
        return trees

    # Count the number of good trees
    good_tree_count = 0
    for edges in generate_trees(N):
        if is_good_tree(edges):
            good_tree_count += 1
            good_tree_count %= MOD

    return good_tree_count

# Read input
N, M = map(int, input().split())
permutations = [list(map(int, input().split())) for _ in range(M)]

# Output the result
print(count_good_trees(N, M, permutations))