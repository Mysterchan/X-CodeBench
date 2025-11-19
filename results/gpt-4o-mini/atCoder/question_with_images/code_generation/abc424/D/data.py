def min_repaints_to_avoid_black_squares(test_cases):
    results = []
    
    for grid in test_cases:
        H, W, S = grid
        repaint_count = 0
        
        # Check each 2x2 subgrid
        for i in range(H - 1):
            for j in range(W - 1):
                # Count the number of black cells in the 2x2 subgrid
                black_count = 0
                if S[i][j] == '#':
                    black_count += 1
                if S[i][j + 1] == '#':
                    black_count += 1
                if S[i + 1][j] == '#':
                    black_count += 1
                if S[i + 1][j + 1] == '#':
                    black_count += 1
                
                # If there are 4 black cells, we need to repaint 3 of them
                if black_count == 4:
                    repaint_count += 3
                # If there are 3 black cells, we need to repaint 2 of them
                elif black_count == 3:
                    repaint_count += 2
                # If there are 2 black cells, we need to repaint 1 of them
                elif black_count == 2:
                    repaint_count += 1
        
        results.append(repaint_count)
    
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
    S = data[index + 1:index + 1 + H]
    test_cases.append((H, W, S))
    index += H + 1

# Get results
results = min_repaints_to_avoid_black_squares(test_cases)

# Print results
for result in results:
    print(result)