def count_ways(t, test_cases):
    MOD = 10**9 + 7
    results = []
    
    for n, m, k, colors in test_cases:
        colored_cells = set(colors)
        total_cells = n * m
        total_filled = len(colored_cells)
        green_cells = total_cells - total_filled
        
        color_diff = 0
        
        for x, y, c in colored_cells:
            checker = (x + y) % 2
            if c == 0:
                # White cell
                color_diff += 1 if checker == 0 else -1
            else:
                # Black cell
                color_diff -= 1 if checker == 0 else -1
        
        even_count = (green_cells % 2) ^ (color_diff % 2)
        
        if even_count == 0:
            results.append(0)
        else:
            results.append(pow(2, green_cells, MOD))
    
    return results


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n, m, k = map(int, data[index].split())
    colors = []
    for i in range(k):
        x, y, c = map(int, data[index + 1 + i].split())
        colors.append((x, y, c))
    test_cases.append((n, m, k, colors))
    index += k + 1

outputs = count_ways(t, test_cases)
sys.stdout.write('\n'.join(map(str, outputs)) + '\n')