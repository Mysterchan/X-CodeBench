def solve():
    N, Q = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    
    for _ in range(Q):
        U, D, L, R = map(int, input().split())
        U -= 1  # Convert to 0-indexed
        D -= 1
        L -= 1
        R -= 1
        
        # Create modified grid
        modified = [[False] * N for _ in range(N)]  # False = white, True = black
        
        for r in range(N):
            for c in range(N):
                if U <= r <= D and L <= c <= R:
                    # Inside rectangle, use original color
                    modified[r][c] = (grid[r][c] == '#')
                else:
                    # Outside rectangle, paint black
                    modified[r][c] = True
        
        # Count 2x2 white squares
        count = 0
        for r in range(N - 1):
            for c in range(N - 1):
                if not modified[r][c] and not modified[r][c+1] and \
                   not modified[r+1][c] and not modified[r+1][c+1]:
                    count += 1
        
        print(count)

solve()