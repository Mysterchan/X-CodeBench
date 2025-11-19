def min_recolor_to_avoid_black_squares(test_cases):
    results = []
    
    for case in test_cases:
        H, W, grid = case
        count = 0
        
        for i in range(H - 1):
            for j in range(W - 1):
                # Check the 2x2 block
                block = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
                black_count = block.count('#')
                
                if black_count == 4:
                    count += 1
        
        results.append(count)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    H, W = map(int, data[index].split())
    grid = data[index + 1:index + 1 + H]
    test_cases.append((H, W, grid))
    index += H + 1

# Get results
results = min_recolor_to_avoid_black_squares(test_cases)

# Print results
for result in results:
    print(result)