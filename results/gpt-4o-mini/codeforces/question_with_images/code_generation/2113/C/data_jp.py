def max_gold_from_dynamite(test_cases):
    results = []
    
    for n, m, k, grid in test_cases:
        total_gold = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    # This is an empty cell where Smilo can place dynamite
                    # Calculate boundaries
                    for x in range(max(0, i - k), min(n, i + k + 1)):
                        for y in range(max(0, j - k), min(m, j + k + 1)):
                            if grid[x][y] == 'g':
                                # If gold is on the boundary
                                if (abs(x - i) == k + 1 or abs(y - j) == k + 1):
                                    total_gold += 1
        results.append(total_gold)
    
    return results


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n, m, k = map(int, data[index].split())
    grid = data[index + 1:index + 1 + n]
    test_cases.append((n, m, k, grid))
    index += n + 1

# Get results
results = max_gold_from_dynamite(test_cases)

# Print outputs
for result in results:
    print(result)