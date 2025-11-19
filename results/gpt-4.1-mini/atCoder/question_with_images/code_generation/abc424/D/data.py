def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        grid = [list(input().strip()) for __ in range(H)]

        # Collect all black cells positions
        black_cells = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == '#']

        # Check if grid satisfies condition (no 2x2 all black)
        def valid(g):
            for i in range(H - 1):
                for j in range(W - 1):
                    if g[i][j] == '#' and g[i][j+1] == '#' and g[i+1][j] == '#' and g[i+1][j+1] == '#':
                        return False
            return True

        # If already valid, answer is 0
        if valid(grid):
            print(0)
            continue

        # We try to repaint minimal number of black cells to white
        # Since H,W <= 7, max black cells <= 49, we can try subsets of black cells to repaint
        # We'll try from 1 to len(black_cells) repaints

        from itertools import combinations

        ans = len(black_cells)  # worst case repaint all black cells
        for r in range(1, len(black_cells) + 1):
            for comb in combinations(black_cells, r):
                # Create a copy of grid
                new_grid = [row[:] for row in grid]
                for (x, y) in comb:
                    new_grid[x][y] = '.'
                if valid(new_grid):
                    ans = r
                    break
            if ans != len(black_cells):
                break

        print(ans)

if __name__ == "__main__":
    main()