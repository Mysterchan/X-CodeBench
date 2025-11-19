def knapsack(T, test_cases):
    results = []
    
    for case in test_cases:
        N, W, items = case
        # Convert items to (weight, value) pairs
        weight_value_pairs = [(2 ** x, y) for x, y in items]
        
        # Sort items by weight
        weight_value_pairs.sort()
        
        total_value = 0
        current_weight = 0
        
        for weight, value in weight_value_pairs:
            if current_weight + weight <= W:
                current_weight += weight
                total_value += value
            else:
                # If we can't take the whole item, we can skip it
                continue
        
        results.append(total_value)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N, W = map(int, data[index].split())
    items = []
    for j in range(N):
        x, y = map(int, data[index + 1 + j].split())
        items.append((x, y))
    test_cases.append((N, W, items))
    index += N + 1

results = knapsack(T, test_cases)
print('\n'.join(map(str, results)))