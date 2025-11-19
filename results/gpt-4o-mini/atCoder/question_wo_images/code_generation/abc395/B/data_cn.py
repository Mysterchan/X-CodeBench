def create_pattern(N):
    grid = [['.' for _ in range(N)] for _ in range(N)]
    
    for i in range(1, N + 1):
        j = N + 1 - i
        if i <= j:
            color = '#' if i % 2 == 1 else '.'
            for x in range(i - 1, j):
                for y in range(i - 1, j):
                    grid[x][y] = color
    
    for row in grid:
        print(''.join(row))

N = int(input())
create_pattern(N)