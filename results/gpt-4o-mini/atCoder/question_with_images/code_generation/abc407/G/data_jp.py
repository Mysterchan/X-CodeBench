H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# Calculate the total sum of all cells
total_sum = sum(sum(row) for row in A)

# Initialize a variable to track the minimum score from unoccupied cells
min_unoccupied_score = 0

# Iterate through the grid to find the minimum values in pairs
for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:  # Only consider cells in the "even" positions
            if j < W - 1:  # Check right neighbor
                min_unoccupied_score = max(min_unoccupied_score, A[i][j] + A[i][j + 1])
            if i < H - 1:  # Check bottom neighbor
                min_unoccupied_score = max(min_unoccupied_score, A[i][j] + A[i + 1][j])

# The maximum score is the total sum minus the minimum unoccupied score
max_score = total_sum - min_unoccupied_score
print(max_score)