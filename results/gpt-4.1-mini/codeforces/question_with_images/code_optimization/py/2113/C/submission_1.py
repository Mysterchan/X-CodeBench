import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n,m,k = map(int,input().split())
        grid = [input().rstrip() for __ in range(n)]

        # Precompute prefix sums of gold presence for quick boundary queries
        # We'll create a 2D prefix sum array for gold cells
        prefix = [[0]*(m+1) for __ in range(n+1)]
        empty_cells = []
        total_gold = 0

        for i in range(n):
            row = grid[i]
            for j in range(m):
                prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (1 if row[j] == 'g' else 0)
                if row[j] == '.':
                    empty_cells.append((i,j))
                if row[j] == 'g':
                    total_gold += 1

        max_gold_collected = 0

        # For each empty cell, calculate gold on the boundary of the explosion square
        # Explosion square side length = 2k+1, centered at (x,y)
        # Boundary cells are those on the perimeter of the square
        # We can get total gold in the square using prefix sums
        # Then subtract gold inside the inner square (side length 2k-1) to get boundary gold
        # Handle boundaries carefully (clamp to grid limits)

        side = 2*k + 1
        inner_side = 2*k - 1

        for x,y in empty_cells:
            # Outer square boundaries
            r1 = x - k
            c1 = y - k
            r2 = x + k
            c2 = y + k

            # Clamp to grid
            r1_clamped = max(0, r1)
            c1_clamped = max(0, c1)
            r2_clamped = min(n-1, r2)
            c2_clamped = min(m-1, c2)

            # Sum gold in outer square
            outer_sum = prefix[r2_clamped+1][c2_clamped+1] - prefix[r2_clamped+1][c1_clamped] - prefix[r1_clamped][c2_clamped+1] + prefix[r1_clamped][c1_clamped]

            # Inner square boundaries (strictly inside)
            if inner_side > 0:
                ir1 = x - (k - 1)
                ic1 = y - (k - 1)
                ir2 = x + (k - 1)
                ic2 = y + (k - 1)

                ir1_clamped = max(0, ir1)
                ic1_clamped = max(0, ic1)
                ir2_clamped = min(n-1, ir2)
                ic2_clamped = min(m-1, ic2)

                inner_sum = prefix[ir2_clamped+1][ic2_clamped+1] - prefix[ir2_clamped+1][ic1_clamped] - prefix[ir1_clamped][ic2_clamped+1] + prefix[ir1_clamped][ic1_clamped]
            else:
                inner_sum = 0

            boundary_gold = outer_sum - inner_sum
            if boundary_gold > max_gold_collected:
                max_gold_collected = boundary_gold

        print(max_gold_collected)

if __name__ == "__main__":
    main()