N, M = map(int, input().split())
P = list(map(int, input().split()))

def cost_for_total(total):
    """Calculate minimum cost to buy 'total' units using greedy selection"""
    if total == 0:
        return 0
    
    # For each product, determine how many units to buy
    # We need to find the threshold marginal cost such that we buy exactly 'total' units
    
    # Binary search on the marginal cost threshold
    left, right = 0, 2 * total * max(P)
    
    while left < right:
        mid = (left + right + 1) // 2
        
        # Count how many units we can buy with marginal cost <= mid
        count = 0
        for p in P:
            # Marginal cost for k-th unit is (2k-1)*p
            # We want (2k-1)*p <= mid
            # So k <= (mid/p + 1) / 2
            if mid >= p:
                k_max = (mid // p + 1) // 2
                count += k_max
        
        if count >= total:
            left = mid
        else:
            right = mid - 1
    
    threshold = left
    
    # Calculate actual cost with this threshold
    total_cost = 0
    units_bought = 0
    
    for p in P:
        if threshold >= p:
            k_max = (threshold // p + 1) // 2
            units_bought += k_max
            total_cost += k_max * (k_max + 1) * (2 * k_max + 1) // 6 * p - k_max * (k_max + 1) // 2 * p
            # Simplified: sum of k^2 from 1 to k_max
            total_cost += p * k_max * (k_max + 1) * (2 * k_max + 1) // 6
    
    # Adjust for exact total
    excess = units_bought - total
    for p in P:
        if threshold >= p:
            k_max = (threshold // p + 1) // 2
            while excess > 0 and k_max > 0:
                total_cost -= k_max * k_max * p
                k_max -= 1
                excess -= 1
                units_bought -= 1
    
    return total_cost

# Binary search on the answer
left, right = 0, int(2e9)

while left < right:
    mid = (left + right + 1) // 2
    
    # Calculate minimum cost to buy mid units
    total_cost = 0
    units = []
    
    for p in P:
        k = int((M / p) ** 0.5) + 1
        for j in range(1, min(k + 1, mid + 1)):
            units.append((2 * j - 1) * p)
    
    units.sort()
    cost = sum(units[:mid])
    
    if cost <= M:
        left = mid
    else:
        right = mid - 1

print(left)