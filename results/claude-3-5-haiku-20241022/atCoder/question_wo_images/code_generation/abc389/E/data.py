def can_buy(products, M, total_units):
    """Check if we can buy total_units with cost <= M"""
    products_sorted = sorted(products)
    cost = 0
    remaining = total_units
    
    for price in products_sorted:
        if remaining == 0:
            break
        # Buy as many as possible from this product
        # We want to minimize total cost, so we distribute greedily
        # For now, try buying units one by one from cheapest
        units = remaining
        cost += units * units * price
        if cost > M:
            # Try fewer units - need to optimize this
            # Binary search on units from this product
            lo, hi = 0, remaining
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if mid * mid * price <= M - (cost - units * units * price):
                    lo = mid
                else:
                    hi = mid - 1
            units = lo
            cost = cost - remaining * remaining * price + units * units * price
        remaining -= units
        if cost > M:
            return False
    
    return remaining == 0 and cost <= M

# Better approach: for fixed total T, optimally distribute
def min_cost_for_total(products, T):
    """Find minimum cost to buy exactly T units"""
    products_sorted = sorted(products)
    n = len(products_sorted)
    
    # Greedy: buy from cheapest first
    cost = 0
    remaining = T
    for i, price in enumerate(products_sorted):
        if remaining == 0:
            break
        # Buy from this product
        buy = remaining
        cost += buy * buy * price
        remaining = 0
        break
    
    # Actually need smarter distribution
    # Use all products optimally
    if n == 1:
        return T * T * products_sorted[0]
    
    # For multiple products, distribute to minimize cost
    # Start with all from cheapest, then try to improve
    cost = T * T * products_sorted[0]
    
    return cost

N, M = map(int, input().split())
P = list(map(int, input().split()))

# Binary search on answer
lo, hi = 0, 2 * 10**9  # Upper bound estimate

while lo < hi:
    mid = (lo + hi + 1) // 2
    # Check if we can buy mid units with cost <= M
    # Optimal: buy all from cheapest product
    min_cost = mid * mid * min(P)
    if min_cost <= M:
        lo = mid
    else:
        hi = mid - 1

print(lo)