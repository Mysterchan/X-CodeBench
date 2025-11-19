def min_repaints(H, W, grid):
    repaints = 0
    for i in range(H - 1):
        for j in range(W - 1):
            # Check the 2x2 block
            block = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
            if block.count('#') == 4:  # All black
                # We need to repaint at least 3 cells to make one white
                repaints += 3
                # Change the block to avoid counting it again
                grid[i][j] = '.'
                grid[i][j + 1] = '.'
                grid[i + 1][j] = '.'
                grid[i + 1][j + 1] = '.'
    return repaints

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    index = 1
    
    for _ in range(T):
        H, W = map(int, data[index].split())
        grid = [list(data[index + i + 1]) for i in range(H)]
        index += H + 1
        
        result = min_repaints(H, W, grid)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()