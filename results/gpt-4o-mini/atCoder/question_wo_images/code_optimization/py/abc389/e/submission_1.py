N, M = map(int, input().split())
P = list(map(int, input().split()))

# Max possible units we can buy
max_units = 0

for price in sorted(P):
    # Calculate the maximum possible k for the current price
    k = 0
    low, high = 0, int(1e9)  # Initial range for k since k^2 is large

    while low <= high:
        mid = (low + high) // 2
        cost = mid * mid * price
        
        if cost <= M:  # Check if we can afford mid units
            k = mid  # We can buy mid units
            low = mid + 1  # Try for more units
        else:
            high = mid - 1  # Try for fewer units

    # Deduct the total cost for k units from M
    total_cost = k * k * price
    M -= total_cost
    max_units += k

print(max_units)