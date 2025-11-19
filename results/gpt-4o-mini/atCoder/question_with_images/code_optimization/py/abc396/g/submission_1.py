import sys
input = sys.stdin.read

def solve():
    data = input().split()
    H = int(data[0])
    W = int(data[1])
    grid = [list(map(int, data[i + 2])) for i in range(H)]
    
    min_total = float('inf')
    
    # Iterate through all possible patterns of column flips
    for flip_pattern in range(1 << W):
        total = 0

        # Calculate the count of 1s in the transformed rows based on the flip pattern
        for row in grid:
            count_ones = 0
            for j in range(W):
                if (flip_pattern >> j) & 1:  # If we are flipping this column
                    count_ones += 1 - row[j]  # Count flipped values
                else:
                    count_ones += row[j]  # Count original values
            
            total += count_ones  # Add the number of 1s in the current configuration
            
        min_total = min(min_total, total)  # Keep track of the minimum found

    print(min_total)

solve()