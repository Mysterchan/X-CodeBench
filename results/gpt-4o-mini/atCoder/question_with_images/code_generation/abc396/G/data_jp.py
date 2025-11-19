def min_sum_after_operations(H, W, grid):
    # Count the number of 1s in each column
    column_counts = [0] * W
    for row in grid:
        for j in range(W):
            if row[j] == '1':
                column_counts[j] += 1

    # Calculate the minimum possible sum
    min_sum = 0
    for count in column_counts:
        # For each column, we can either keep it as is or flip it
        # We want the minimum of the count of 1s or the count of 0s
        min_sum += min(count, H - count)

    return min_sum

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
grid = data[1:H + 1]

# Get the result and print it
result = min_sum_after_operations(H, W, grid)
print(result)