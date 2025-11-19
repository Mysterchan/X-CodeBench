def solve():
    N, Q = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    
    for _ in range(Q):
        U, D, L, R = map(int, input().split())
        # Convert to 0-indexed
        U -= 1
        D -= 1
        L -= 1
        R -= 1
        
        # Count 2x2 all-white squares in the region
        count = 0
        for r in range(U, D):
            for c in range(L, R):
                # Check if (r,c), (r,c+1), (r+1,c), (r+1,c+1) are all white
                if (grid[r][c] == '.' and 
                    grid[r][c+1] == '.' and 
                    grid[r+1][c] == '.' and 
                    grid[r+1][c+1] == '.'):
                    count += 1
        
        print(count)

solve()