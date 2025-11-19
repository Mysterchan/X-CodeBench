def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, Q = map(int, data[0].split())
    grid = [list(data[i + 1]) for i in range(N)]
    
    queries = [list(map(int, data[N + 1 + i].split())) for i in range(Q)]
    
    results = []
    
    for U, D, L, R in queries:
        # Convert to 0-based indexing
        U -= 1
        D -= 1
        L -= 1
        R -= 1
        
        # Create a temporary grid for the current query
        temp_grid = [row[:] for row in grid]
        
        # Paint the cells that do not satisfy the condition
        for r in range(N):
            for c in range(N):
                if not (U <= r <= D and L <= c <= R):
                    temp_grid[r][c] = '#'
        
        # Count the number of 2x2 white squares
        count = 0
        for r in range(U, D):
            for c in range(L, R):
                if (temp_grid[r][c] == '.' and
                    temp_grid[r][c + 1] == '.' and
                    temp_grid[r + 1][c] == '.' and
                    temp_grid[r + 1][c + 1] == '.'):
                    count += 1
        
        results.append(count)
    
    # Print all results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()