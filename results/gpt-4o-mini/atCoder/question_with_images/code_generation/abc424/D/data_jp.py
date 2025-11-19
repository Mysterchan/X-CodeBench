def min_white_cells_to_paint(H, W, grid):
    # Count the number of black cells that need to be painted white
    to_paint = 0
    for i in range(H - 1):
        for j in range(W - 1):
            # Check the 2x2 block
            black_count = sum(1 for x in range(2) for y in range(2) if grid[i + x][j + y] == '#')
            if black_count == 4:
                # If all 4 cells are black, we need to paint at least 1
                to_paint += 1
    return to_paint

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    index = 1
    
    for _ in range(T):
        H, W = map(int, data[index].split())
        grid = data[index + 1:index + 1 + H]
        index += 1 + H
        
        result = min_white_cells_to_paint(H, W, grid)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()