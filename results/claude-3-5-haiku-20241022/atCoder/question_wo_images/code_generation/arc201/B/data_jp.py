import sys
from collections import defaultdict

def solve():
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        x, y = map(int, input().split())
        items.append((x, y))
    
    # Group items by X value
    groups = defaultdict(list)
    for x, y in items:
        groups[x].append(y)
    
    # Sort values in each group in descending order and keep only useful ones
    for x in groups:
        groups[x].sort(reverse=True)
    
    # Collect all unique X values and sort them
    unique_x = sorted(groups.keys())
    
    # For large X values (>= 60), we can take at most a few items
    # For small X values, we need DP
    
    # Split into small and large X
    threshold = 40
    small_x = [x for x in unique_x if x < threshold]
    large_x = [x for x in unique_x if x >= threshold]
    
    # For large X values, we can afford very few items
    large_items = []
    for x in large_x:
        weight = 1 << x
        for y in groups[x]:
            large_items.append((weight, y))
    
    # Generate all possible subsets of large items (with pruning)
    large_states = [(0, 0)]  # (weight, value)
    for weight, value in large_items:
        new_states = []
        for w, v in large_states:
            if w + weight <= W:
                new_states.append((w + weight, v + value))
        large_states.extend(new_states)
        # Keep only Pareto optimal states
        large_states.sort()
        filtered = []
        max_value = -1
        for w, v in large_states:
            if v > max_value:
                filtered.append((w, v))
                max_value = v
        large_states = filtered
    
    max_result = 0
    
    # For each state from large items, solve DP for small items
    for large_weight, large_value in large_states:
        remaining_capacity = W - large_weight
        if remaining_capacity < 0:
            continue
        
        # DP for small X values with remaining capacity
        # Group by X and precompute prefix sums
        dp_map = {0: 0}  # weight -> max_value
        
        for x in small_x:
            weight = 1 << x
            values = groups[x]
            
            # Compute prefix sums
            prefix = [0]
            for v in values:
                prefix.append(prefix[-1] + v)
            
            new_dp = {}
            for curr_weight, curr_value in dp_map.items():
                # Try taking 0, 1, 2, ... items of this weight
                max_count = min(len(values), remaining_capacity // weight)
                for count in range(max_count + 1):
                    new_weight = curr_weight + count * weight
                    if new_weight <= remaining_capacity:
                        new_value = curr_value + prefix[count]
                        if new_weight not in new_dp or new_dp[new_weight] < new_value:
                            new_dp[new_weight] = new_value
            
            dp_map = new_dp
        
        # Find max value in dp_map
        if dp_map:
            small_value = max(dp_map.values())
        else:
            small_value = 0
        
        max_result = max(max_result, large_value + small_value)
    
    print(max_result)

T = int(input())
for _ in range(T):
    solve()