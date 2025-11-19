def min_operations(N, S, T):
    def rotate(grid):
        return [''.join(grid[N - j - 1][i] for j in range(N)) for i in range(N)]

    def count_differences(grid1, grid2):
        return sum(1 for i in range(N) for j in range(N) if grid1[i][j] != grid2[i][j])

    min_ops = float('inf')
    current_S = S

    for _ in range(4):
        differences = count_differences(current_S, T)
        min_ops = min(min_ops, differences)
        current_S = rotate(current_S)

    return min_ops

# Read input
N = int(input().strip())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(N)]

# Get the result and print it
result = min_operations(N, S, T)
print(result)