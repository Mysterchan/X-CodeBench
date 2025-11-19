import sys
input = sys.stdin.readline

T = int(input())
MAX_X = 60

for _ in range(T):
    N, W = map(int, input().split())
    # For each power of two weight, keep the max value item
    max_values = [-1] * MAX_X
    for __ in range(N):
        x, y = map(int, input().split())
        if max_values[x] < y:
            max_values[x] = y

    # We want to pick items with max value for each weight 2^x
    # Greedy approach: pick items with highest value first, but we must respect weight limit W
    # Since weights are powers of two, we can try to pick items from largest value to smallest
    # But we only have one item per weight class (the max one)
    # So just pick items in descending order of value if weight fits

    # Create list of (value, weight)
    candidates = []
    for x in range(MAX_X):
        if max_values[x] != -1:
            candidates.append((max_values[x], 1 << x))
    # Sort by value descending
    candidates.sort(key=lambda x: x[0], reverse=True)

    total_value = 0
    remaining_weight = W
    for val, wt in candidates:
        if wt <= remaining_weight:
            total_value += val
            remaining_weight -= wt

    print(total_value)