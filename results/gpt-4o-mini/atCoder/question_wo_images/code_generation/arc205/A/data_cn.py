def max_operations(N, Q, grid, queries):
    results = []
    
    for U, D, L, R in queries:
        # Create a temporary grid to mark black cells
        temp_grid = [list(row) for row in grid]
        
        # Mark the cells that are out of the query bounds as black
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if not (U <= r <= D and L <= c <= R):
                    temp_grid[r - 1][c - 1] = '#'
        
        # Count the number of valid operations
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

N, Q = map(int, data[0].split())
grid = data[1:N + 1]
queries = [tuple(map(int, line.split())) for line in data[N + 1:]]

# Get results
results = max_operations(N, Q, grid, queries)

# Print results
for result in results:
    print(result)