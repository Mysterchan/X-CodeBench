def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input().strip())
    # Initialize an empty grid
    grid = [['?'] * N for _ in range(N)]
    
    # Apply operations for i = 1..N
    for i in range(1, N + 1):
        j = N + 1 - i
        if i > j:
            continue
        # Determine paint color: '#' for odd i, '.' for even i
        color = '#' if (i & 1) else '.'
        # Paint the rectangle from (i,i) to (j,j), converting to 0-based indices
        for r in range(i - 1, j):
            for c in range(i - 1, j):
                grid[r][c] = color
    
    # Output the final grid
    out = sys.stdout
    for row in grid:
        out.write(''.join(row) + '\n')

if __name__ == "__main__":
    main()