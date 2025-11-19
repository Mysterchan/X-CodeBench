import sys
from collections import defaultdict

def min_insertions(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # dp[i][v] = minimum insertions to reduce arr[0:i+1] to a single element with value v
    # We need to track what value we can achieve at each position
    
    # Use memoization with dictionary
    memo = {}
    
    def solve(pos, target):
        # Try to merge arr[pos:] into a single element with value `target`
        # Returns minimum insertions needed, or infinity if impossible
        
        if pos == n:
            return 0 if target == -1 else float('inf')
        
        if (pos, target) in memo:
            return memo[(pos, target)]
        
        result = float('inf')
        
        if target == -1:
            # We need to decide what final value to achieve
            # Try merging from position pos onwards
            current_val = arr[pos]
            cost = 0
            for end in range(pos, n):
                if end > pos:
                    # Need to merge arr[pos:end] into current_val
                    # This requires inserting elements to make consecutive pairs
                    cost += solve_range(pos, end, current_val)
                
                # Now try to continue from end+1
                remaining = solve(end + 1, -1)
                result = min(result, cost + remaining)
                
                # Try to merge with next element
                if end + 1 < n:
                    next_val = arr[end + 1]
                    if current_val == next_val:
                        current_val += 1
                    else:
                        break
        else:
            # We need to achieve exactly `target` value from position pos onwards
            # and consume some elements
            pass
        
        memo[(pos, target)] = result
        return result
    
    # Different approach: interval DP
    # dp[i][j] = (min_insertions, final_value) to reduce arr[i:j+1] to single element
    
    INF = float('inf')
    dp = {}
    
    def get_cost(i, j):
        if i > j:
            return (0, -1)
        if i == j:
            return (0, arr[i])
        if (i, j) in dp:
            return dp[(i, j)]
        
        result = (INF, -1)
        
        # Try to split at each position
        for k in range(i, j):
            left_cost, left_val = get_cost(i, k)
            right_cost, right_val = get_cost(k + 1, j)
            
            if left_val == -1 or right_val == -1:
                continue
            
            total_cost = left_cost + right_cost
            
            # Merge left_val and right_val
            if left_val == right_val:
                final_val = left_val + 1
            elif left_val < right_val:
                # Need to insert elements to make left_val equal to right_val
                insertions = right_val - left_val
                total_cost += insertions
                final_val = right_val + 1
            else:
                # left_val > right_val
                insertions = left_val - right_val
                total_cost += insertions
                final_val = left_val + 1
            
            if total_cost < result[0]:
                result = (total_cost, final_val)
        
        dp[(i, j)] = result
        return result
    
    cost, _ = get_cost(0, n - 1)
    return cost

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    t = int(input_lines[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_lines[idx])
        idx += 1
        arr = list(map(int, input_lines[idx].split()))
        idx += 1
        
        result = min_insertions(arr)
        print(result)

if __name__ == "__main__":
    main()