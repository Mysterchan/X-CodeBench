import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read().split()
    idx = 0
    
    T = int(input[idx])
    idx += 1
    
    for _ in range(T):
        N = int(input[idx])
        W = int(input[idx + 1])
        idx += 2
        
        items = []
        for i in range(N):
            X = int(input[idx])
            Y = int(input[idx + 1])
            idx += 2
            items.append((X, Y))
        
        # Group items by weight (X value)
        weight_groups = defaultdict(list)
        for x, y in items:
            weight_groups[x].append(y)
        
        # For each weight, keep only top values
        # Since we can have at most 60 different weights (0 to 59)
        # and W <= 10^18 < 2^60, we need to be careful
        sorted_groups = []
        for x in sorted(weight_groups.keys()):
            values = sorted(weight_groups[x], reverse=True)
            sorted_groups.append((x, values))
        
        # DP approach: for each weight class, decide how many to take
        # Key insight: for weight 2^x, we can take at most W // 2^x items
        # But we should limit based on practical constraints
        
        max_value = 0
        
        # Use bitmask or recursive approach with memoization
        # Since there are at most 60 different weights, we can use DP
        
        # dp[w] = maximum value with weight exactly w
        # But W can be too large, so we use different approach
        
        # For each combination of item counts per weight class
        def search(group_idx, remaining_weight, current_value):
            nonlocal max_value
            
            if group_idx == len(sorted_groups):
                max_value = max(max_value, current_value)
                return
            
            x, values = sorted_groups[group_idx]
            item_weight = 1 << x  # 2^x
            
            if item_weight > remaining_weight:
                search(group_idx + 1, remaining_weight, current_value)
                return
            
            max_items = min(len(values), remaining_weight // item_weight)
            
            # Try taking 0 to max_items of this weight class
            cumulative_value = 0
            for count in range(max_items + 1):
                search(group_idx + 1, remaining_weight - count * item_weight, current_value + cumulative_value)
                if count < max_items:
                    cumulative_value += values[count]
        
        search(0, W, 0)
        print(max_value)

solve()