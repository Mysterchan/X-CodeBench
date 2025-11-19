def solve():
    N, Q = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    
    # Precompute white counts for all rectangles
    # white[r][c] = number of white cells in rectangle from (0,0) to (r-1,c-1)
    white = [[0] * (N + 1) for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            white[r][c] = white[r-1][c] + white[r][c-1] - white[r-1][c-1]
            if grid[r-1][c-1] == '.':
                white[r][c] += 1
    
    def count_white(r1, c1, r2, c2):
        # Count white cells in rectangle from (r1, c1) to (r2, c2) inclusive (0-indexed)
        return white[r2+1][c2+1] - white[r1][c2+1] - white[r2+1][c1] + white[r1][c1]
    
    for _ in range(Q):
        U, D, L, R = map(int, input().split())
        U -= 1  # Convert to 0-indexed
        D -= 1
        L -= 1
        R -= 1
        
        # Count white cells in the region
        total_white = count_white(U, L, D, R)
        
        # Count 2x2 squares that are fully white in the region
        squares = 0
        for r in range(U, D):
            for c in range(L, R):
                # Check if all 4 cells are white
                if (grid[r][c] == '.' and grid[r][c+1] == '.' and
                    grid[r+1][c] == '.' and grid[r+1][c+1] == '.'):
                    squares += 1
        
        # Maximum operations = total_white - squares
        print(total_white - squares)

solve()