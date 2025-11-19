def max_units(N, M, P):
    P.sort()
    
    total_units = 0
    remaining_budget = M
    
    for price in P:
        # Initialize binary search bounds
        low, high = 0, int(1e9)  # 10^9 is an upper limit on units of a single product
        
        while low < high:
            mid = (low + high + 1) // 2  # upper mid to avoid infinite loop when low=high-1
            
            cost = mid * mid * price  # Cost to buy mid units of the current product
            
            if cost <= remaining_budget:
                low = mid  # It is possible to buy mid units, try to buy more
            else:
                high = mid - 1  # mid units are too expensive, try less
                
        total_units += low  # low is the maximum units we can afford for this product
        remaining_budget -= low * low * price  # reduce the budget
        
        if remaining_budget <= 0:  # If we have exhausted the budget, break
            break
        
    return total_units

# Read inputs
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
P = list(map(int, data[2:2+N]))

# Calculate and print the result
result = max_units(N, M, P)
print(result)