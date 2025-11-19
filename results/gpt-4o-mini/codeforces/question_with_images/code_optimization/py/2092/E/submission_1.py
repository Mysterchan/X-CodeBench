def solve():
    MOD = 10**9 + 7
    t = int(input())
    
    for _ in range(t):
        n, m, k = map(int, input().split())
        painted_cells = {}
        
        for _ in range(k):
            x, y, c = map(int, input().split())
            painted_cells[(x, y)] = c
        
        # Count the number of black and white cells
        black_count = sum(1 for c in painted_cells.values() if c == 1)
        white_count = k - black_count
        
        # Determine the parity of the number of different adjacent pairs
        diff_pairs = 0
        
        for (x, y), c in painted_cells.items():
            if (x + 1, y) in painted_cells and painted_cells[(x + 1, y)] != c:
                diff_pairs += 1
            if (x, y + 1) in painted_cells and painted_cells[(x, y + 1)] != c:
                diff_pairs += 1
        
        # Calculate the number of unpainted cells
        unpainted_cells = n * m - k
        
        # If the number of different pairs is odd, we need to adjust the colorings
        if diff_pairs % 2 == 1:
            # If we have unpainted cells, we can only have 0 valid configurations
            if unpainted_cells > 0:
                print(0)
                continue
            else:
                # If no unpainted cells and diff_pairs is odd, it's invalid
                print(0)
                continue
        
        # If diff_pairs is even, we can paint the unpainted cells freely
        # Each unpainted cell can be either black or white
        result = pow(2, unpainted_cells, MOD)
        print(result)

solve()