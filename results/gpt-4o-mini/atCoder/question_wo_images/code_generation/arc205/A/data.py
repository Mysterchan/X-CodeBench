def max_operations(N, grid, queries):
    results = []
    
    for U, D, L, R in queries:
        # Create a temporary grid to mark the area of interest
        temp_grid = [['#' for _ in range(N)] for _ in range(N)]
        
        # Fill the temporary grid with the original grid values in the specified range
        for r in range(U - 1, D):
            for c in range(L - 1, R):
                temp_grid[r][c] = grid[r][c]
        
        # Count the number of 2x2 white squares
        count = 0
        for r in range(U - 1, D - 1):
            for c in range(L - 1, R - 1):
                if (temp_grid[r][c] == '.' and
                    temp_grid[r][c + 1] == '.' and
                    temp_grid[r + 1][c] == '.' and
                    temp_grid[r + 1][c + 1] == '.'):
                    count += 1
        
        results.append(count)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

# First line contains N and Q
N, Q = map(int, data[0].split())
grid = [data[i + 1] for i in range(N)]
queries = [tuple(map(int, data[N + i + 1].split())) for i in range(Q)]

# Get results
results = max_operations(N, grid, queries)

# Print results
for result in results:
    print(result)