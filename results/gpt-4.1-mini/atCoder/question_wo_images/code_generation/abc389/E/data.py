def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    P = list(map(int, input().split()))

    # We want to maximize total units bought: sum(k_i)
    # subject to sum(k_i^2 * P_i) <= M
    # Each k_i >= 0, and stock is large enough (10^100 units)

    # Key insight:
    # For fixed total units X = sum(k_i), the minimal cost is achieved when
    # the distribution of units k_i minimizes sum(k_i^2 * P_i).
    #
    # Using Lagrange multipliers, the minimal cost distribution is:
    # k_i = X / sum_j sqrt(P_j) * 1/sqrt(P_i)
    #
    # The minimal cost for total units X is:
    # cost(X) = X^2 / (sum_j 1/sqrt(P_j))^2
    # multiplied by sum_i P_i / P_i = sum_i sqrt(P_i)^2 = (sum_i sqrt(P_i))^2
    #
    # Let's verify:
    # k_i = X * (1/sqrt(P_i)) / sum_j (1/sqrt(P_j))
    # cost = sum_i (k_i^2 * P_i)
    #      = sum_i (X^2 * (1/sqrt(P_i))^2 / (sum_j 1/sqrt(P_j))^2 * P_i)
    #      = X^2 / (sum_j 1/sqrt(P_j))^2 * sum_i (P_i / P_i)
    #      = X^2 / (sum_j 1/sqrt(P_j))^2 * N
    #
    # This is incorrect because sum_i (P_i / P_i) = N, but the factor inside is (1/sqrt(P_i))^2 * P_i = 1
    # So sum_i (k_i^2 * P_i) = X^2 / (sum_j 1/sqrt(P_j))^2 * N
    #
    # But this contradicts the sample test, so let's re-derive carefully.

    # Let's define:
    # Let a_i = sqrt(P_i)
    # k_i = c / a_i for some c
    # sum k_i = X => c * sum_i 1/a_i = X => c = X / sum_i 1/a_i
    # cost = sum_i k_i^2 * P_i = sum_i (c^2 / a_i^2) * a_i^2 = sum_i c^2 = N * c^2
    # cost = N * c^2 = N * (X / sum_i 1/a_i)^2

    # So cost(X) = N * (X / sum_i 1/sqrt(P_i))^2

    # We want cost(X) <= M
    # => N * (X / sum_i 1/sqrt(P_i))^2 <= M
    # => (X / sum_i 1/sqrt(P_i))^2 <= M / N
    # => X <= sum_i 1/sqrt(P_i) * sqrt(M / N)

    # So maximum X = floor(sum_i 1/sqrt(P_i) * sqrt(M / N))

    # Let's check sample input 1:
    # N=3, M=9, P=[4,1,9]
    # sqrt(P) = [2,1,3]
    # sum_i 1/sqrt(P_i) = 1/2 + 1/1 + 1/3 = 0.5 + 1 + 0.3333 = 1.8333
    # sqrt(M/N) = sqrt(9/3) = sqrt(3) ~1.732
    # max X = 1.8333 * 1.732 = ~3.17 => floor 3 matches sample output

    # Sample input 2:
    # N=10, M=1000, P=[2,15,6,5,12,1,7,9,17,2]
    # sqrt(P) = [1.4142,3.873,2.449,2.236,3.464,1,2.645,3,4.123,1.414]
    # sum_i 1/sqrt(P_i) = sum of reciprocals
    # Let's compute sum_i 1/sqrt(P_i):
    # 1/1.414=0.707, 1/3.873=0.258, 1/2.449=0.408, 1/2.236=0.447,
    # 1/3.464=0.288, 1/1=1, 1/2.645=0.378, 1/3=0.333, 1/4.123=0.242, 1/1.414=0.707
    # sum = 0.707+0.258+0.408+0.447+0.288+1+0.378+0.333+0.242+0.707 = ~4.768
    # sqrt(M/N) = sqrt(1000/10) = sqrt(100) = 10
    # max X = 4.768 * 10 = 47.68 floor 47, but sample output is 53

    # So the above formula underestimates the max units.

    # The discrepancy is because the minimal cost distribution is not necessarily integer units,
    # and the problem requires integer units.

    # So we need a binary search on total units X:
    # For a given X, minimal cost is sum_i (k_i^2 * P_i) with sum k_i = X
    # The minimal cost is achieved by k_i proportional to 1/sqrt(P_i)
    # k_i = X * (1/sqrt(P_i)) / sum_j (1/sqrt(P_j))
    #
    # But k_i must be integer, so we can try floor(k_i) or ceil(k_i) to minimize cost.
    #
    # To check feasibility for given X:
    # 1. Compute ideal k_i = X * (1/sqrt(P_i)) / sum_j (1/sqrt(P_j))
    # 2. Try floor(k_i) for all i, sum floor(k_i) = S
    # 3. If S < X, assign the remaining units to products with minimal incremental cost
    #    Incremental cost for adding one unit to product i is:
    #    cost(k_i+1) - cost(k_i) = ((k_i+1)^2 - k_i^2) * P_i = (2*k_i + 1)*P_i
    #
    # So we can:
    # - Start with floor(k_i)
    # - Distribute remaining units one by one to products with minimal incremental cost
    #
    # But N can be up to 2*10^5, and X can be large (up to 10^9 or more),
    # so distributing units one by one is too slow.

    # Alternative approach:
    # Since cost function is convex and separable, we can binary search on X,
    # and for each X compute minimal cost by rounding k_i to nearest integer.

    # Let's try to approximate cost for given X by rounding k_i to nearest integer:
    # k_i_ideal = X * (1/sqrt(P_i)) / sum_j (1/sqrt(P_j))
    # k_i_int = round(k_i_ideal)
    # sum k_i_int may not be exactly X, so adjust by adding or removing units from products
    # with minimal incremental cost.

    # But this is complicated.

    # Instead, let's do a binary search on X:
    # For given X, minimal cost is at least:
    # cost_min = N * (X / sum_i 1/sqrt(P_i))^2 (continuous relaxation)
    # So if cost_min > M, no need to check further.

    # For upper bound on X, we can use:
    # max_X = floor(sum_i 1/sqrt(P_i) * sqrt(M / N)) * 2 (to be safe)

    # For checking feasibility of X:
    # We can compute k_i = floor(k_i_ideal)
    # sum_k = sum k_i
    # diff = X - sum_k
    # We need to add diff units to some products.

    # To minimize cost, add units to products with minimal incremental cost:
    # incremental cost for adding one unit to product i at k_i units:
    # inc_cost_i = (2*k_i + 1)*P_i

    # We can create a min-heap of (inc_cost_i, i) for all products,
    # and pop diff times to add one unit to that product.

    # But diff can be up to N, so this is O(N log N) per check, which is acceptable.

    # After adjusting k_i, compute total cost and check if <= M.

    # Implement binary search on X from 0 to max_X.

    import math
    from heapq import heappush, heappop

    sqrtP = [math.sqrt(p) for p in P]
    inv_sqrtP = [1.0 / sp for sp in sqrtP]
    sum_inv_sqrtP = sum(inv_sqrtP)

    # Upper bound for binary search
    # Use continuous relaxation max units * 2 for safety
    max_X = int(sum_inv_sqrtP * math.sqrt(M / N)) + 10**6  # add margin

    def can_buy(X):
        if X == 0:
            return True
        # Compute ideal k_i
        k_ideal = [X * inv_sqrtP[i] / sum_inv_sqrtP for i in range(N)]
        k_floor = [int(math.floor(k)) for k in k_ideal]
        sum_floor = sum(k_floor)
        diff = X - sum_floor

        # Build min-heap for incremental cost to add one unit
        # inc_cost_i = (2*k_i + 1)*P_i
        heap = []
        for i in range(N):
            inc_cost = (2 * k_floor[i] + 1) * P[i]
            heappush(heap, (inc_cost, i))

        # Add diff units to products with minimal incremental cost
        for _ in range(diff):
            inc_cost, i = heappop(heap)
            k_floor[i] += 1
            inc_cost = (2 * k_floor[i] + 1) * P[i]
            heappush(heap, (inc_cost, i))

        # Compute total cost
        total_cost = 0
        for i in range(N):
            total_cost += k_floor[i] * k_floor[i] * P[i]
            if total_cost > M:
                return False
        return total_cost <= M

    left, right = 0, max_X
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if can_buy(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    main()