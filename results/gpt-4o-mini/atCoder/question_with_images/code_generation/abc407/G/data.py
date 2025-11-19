def max_domino_score(H, W, A):
    total_sum = sum(sum(row) for row in A)
    max_score = total_sum
    
    # Iterate through the grid to find the best domino placements
    for i in range(H):
        for j in range(W):
            if j < W - 1:  # Check horizontal domino
                score_with_domino = total_sum - (A[i][j] + A[i][j + 1])
                max_score = max(max_score, score_with_domino)
            if i < H - 1:  # Check vertical domino
                score_with_domino = total_sum - (A[i][j] + A[i + 1][j])
                max_score = max(max_score, score_with_domino)
    
    return max_score

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
A = [list(map(int, line.split())) for line in data[1:H + 1]]

# Get the result and print it
result = max_domino_score(H, W, A)
print(result)