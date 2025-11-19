def count_good_trees(N, M, permutations):
    MOD = 998244353

    # Create a list to store the positions of each number in the permutations
    pos = [[0] * (N + 1) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            pos[i][permutations[i][j]] = j

    # Check if a tree can be formed
    def can_form_tree():
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                # Check if all permutations have the same relative order for i and j
                order = [pos[k][i] < pos[k][j] for k in range(M)]
                if all(order) or not any(order):
                    return False
        return True

    # Count the number of good trees
    if not can_form_tree():
        return 0

    # The number of good trees is (N-1)! since any tree can be formed
    from math import factorial
    return factorial(N - 1) % MOD

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
permutations = [list(map(int, line.split())) for line in data[1:M + 1]]

# Output the result
print(count_good_trees(N, M, permutations))