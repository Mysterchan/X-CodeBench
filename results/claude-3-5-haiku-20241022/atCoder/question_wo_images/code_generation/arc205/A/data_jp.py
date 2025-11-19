def solve():
    N, Q = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    
    for _ in range(Q):
        U, D, L, R = map(int, input().split())
        U -= 1
        D -= 1
        L -= 1
        R -= 1
        
        # Create working grid
        state = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if U <= r <= D and L <= c <= R:
                    state[r][c] = (grid[r][c] == '.')
                else:
                    state[r][c] = False
        
        count = 0
        while True:
            found = False
            for r in range(N - 1):
                for c in range(N - 1):
                    if (state[r][c] and state[r][c+1] and 
                        state[r+1][c] and state[r+1][c+1]):
                        state[r][c] = False
                        count += 1
                        found = True
                        break
                if found:
                    break
            if not found:
                break
        
        print(count)

solve()