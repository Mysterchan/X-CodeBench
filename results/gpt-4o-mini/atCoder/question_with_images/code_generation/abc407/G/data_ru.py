def max_domino_score(H, W, A):
    total_sum = sum(sum(row) for row in A)
    min_coverable_sum = 0

    # Iterate through the grid to find the minimum coverable sum
    for i in range(H):
        for j in range(W):
            if j < W - 1:  # Check horizontal domino
                min_coverable_sum = max(min_coverable_sum, A[i][j] + A[i][j + 1])
            if i < H - 1:  # Check vertical domino
                min_coverable_sum = max(min_coverable_sum, A[i][j] + A[i + 1][j])

    # The maximum score is the total sum minus the minimum coverable sum
    max_score = total_sum - min_coverable_sum
    return max_score

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
A = [list(map(int, line.split())) for line in data[1:H + 1]]

# Calculate and print the result
result = max_domino_score(H, W, A)
print(result)