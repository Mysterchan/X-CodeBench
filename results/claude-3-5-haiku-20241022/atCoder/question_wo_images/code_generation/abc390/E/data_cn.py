def solve():
    N, X = map(int, input().split())
    foods = []
    for _ in range(N):
        v, a, c = map(int, input().split())
        foods.append((v-1, a, c))  # v-1 to make it 0-indexed
    
    # Separate foods by vitamin type
    vitamins = [[], [], []]
    for v, a, c in foods:
        vitamins[v].append((a, c))
    
    # For each vitamin type, we want to find all possible (amount, min_calories) pairs
    # using knapsack-like approach
    def get_reachable(items, max_cal):
        # dp[cal] = max vitamin amount with exactly cal calories
        dp = [-1] * (max_cal + 1)
        dp[0] = 0
        
        for amount, cal in items:
            new_dp = dp[:]
            for c in range(max_cal + 1):
                if dp[c] >= 0 and c + cal <= max_cal:
                    new_dp[c + cal] = max(new_dp[c + cal], dp[c] + amount)
            dp = new_dp
        
        # Convert to list of (amount, min_calories)
        result = {}
        for c in range(max_cal + 1):
            if dp[c] >= 0:
                amt = dp[c]
                if amt not in result or result[amt] > c:
                    result[amt] = c
        return result
    
    # Get reachable states for each vitamin
    reachable = []
    for i in range(3):
        reachable.append(get_reachable(vitamins[i], X))
    
    max_min = 0
    
    # Try all combinations of vitamin amounts
    for amt1, cal1 in reachable[0].items():
        for amt2, cal2 in reachable[1].items():
            remaining = X - cal1 - cal2
            if remaining < 0:
                continue
            for amt3, cal3 in reachable[2].items():
                if cal3 <= remaining:
                    min_amt = min(amt1, amt2, amt3)
                    max_min = max(max_min, min_amt)
    
    print(max_min)

solve()