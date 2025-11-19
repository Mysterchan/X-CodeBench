def max_gold_collected(test_cases):
    results = []

    for case in test_cases:
        n, m, k, mine = case
        gold_count = 0
        
        # Set bounds for the explosion square
        explosion_size = 2 * k + 1
        
        # Check all empty cells
        for i in range(n):
            for j in range(m):
                if mine[i][j] == '.':
                    # Determine boundaries of the explosion square
                    for x in range(max(0, i - k), min(n, i + k + 1)):
                        for y in range(max(0, j - k), min(m, j + k + 1)):
                            if abs(x - i) + abs(y - j) == k:  # if on boundary
                                if mine[x][y] == 'g':
                                    gold_count += 1

        results.append(gold_count)
    
    return results

# Read input
import sys

input = sys.stdin.read
data = input().strip().split('\n')
t = int(data[0])
index = 1

test_cases = []

for _ in range(t):
    n, m, k = map(int, data[index].split())
    index += 1
    mine = [data[index + i] for i in range(n)]
    test_cases.append((n, m, k, mine))
    index += n

# Get results and print output
results = max_gold_collected(test_cases)

for result in results:
    print(result)