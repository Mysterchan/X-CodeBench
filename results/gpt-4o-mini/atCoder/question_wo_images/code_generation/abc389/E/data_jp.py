def max_products(N, M, P):
    total_products = 0
    
    # Try to buy as many products as possible
    for price in sorted(P):
        k = 0
        while True:
            cost = (k + 1) ** 2 * price
            if total_products + k + 1 > M:  # If we cannot afford another item
                break
            if cost > M:  # If the cost exceeds the budget
                break
            M -= cost  # Deduct the cost from the budget
            total_products += (k + 1)  # Increase the count of products bought
            k += 1  # Increase the count for the next iteration
            
    return total_products

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
P = list(map(int, data[2:2 + N]))

# Call the function and output the result
result = max_products(N, M, P)
print(result)