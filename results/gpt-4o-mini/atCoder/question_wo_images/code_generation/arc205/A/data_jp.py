def count_operations(N, grid, queries):
    results = []
    
    for U, D, L, R in queries:
        # Create a temporary grid to mark the black cells
        temp_grid = [row[:] for row in grid]
        
        # Mark the cells that are outside the query bounds as black
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if not (U <= r <= D and L <= c <= R):
                    temp_grid[r - 1][c - 1] = '#'
        
        # Count the number of valid 2x2 squares
        count = 0
        for r in range(1, N):
            for c in range(1, N):
                if (temp_grid[r - 1][c - 1] == '.' and
                    temp_grid[r - 1][c] == '.' and
                    temp_grid[r][c - 1] == '.' and
                    temp_grid[r][c] == '.'):
                    count += 1
        
        results.append(count)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

N, Q = map(int, data[0].split())
grid = [list(data[i + 1]) for i in range(N)]
queries = [tuple(map(int, data[N + i + 1].split())) for i in range(Q)]

# Get results
results = count_operations(N, grid, queries)

# Output results
for result in results:
    print(result)