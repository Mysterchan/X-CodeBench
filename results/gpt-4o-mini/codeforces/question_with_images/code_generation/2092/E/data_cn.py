def count_ways(n, m, k, cells):
    MOD = 10**9 + 7
    
    total_cells = n * m
    colored_cells = set(cells)
    
    # Count the number of odd and even colored cells
    parity_count = [0, 0]
    for (x, y, c) in colored_cells:
        parity_index = (x + y) % 2
        parity_count[parity_index] += 1

    # The number of cells we need to fill
    green_cells = total_cells - k
    if green_cells == 0:
        # No green cells to fill
        return 1 if (parity_count[0] + parity_count[1]) % 2 == 0 else 0
    
    # Calculate the possible coloring configurations
    if (parity_count[0] % 2) == (parity_count[1] % 2):
        return pow(2, green_cells - 1, MOD)
    else:
        return pow(2, green_cells, MOD)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, m, k = map(int, data[index].split())
        cells = []
        
        for i in range(k):
            x, y, c = map(int, data[index + 1 + i].split())
            cells.append((x, y, c))
        
        index += k + 1
        
        result = count_ways(n, m, k, cells)
        results.append(result)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()