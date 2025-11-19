def max_products(N, M, P):
    # Sort prices to minimize cost as much as possible
    P.sort()
    
    total_units = 0
    for price in P:
        # The maximum k for which k^2 * price <= remaining M
        k = int((M // price) ** 0.5)
        cost = k * k * price
        
        total_units += k
        M -= cost
        
        if M < 0:
            break
    
    return total_units

# Reading input
N, M = map(int, input().split())
P = list(map(int, input().split()))

# Getting the result
result = max_products(N, M, P)

# Printing the output
print(result)